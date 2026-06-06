"""RootCourse computation engine  -  single source of truth for the course's data.

Imports the Quran Root Explorer's own modules (no re-implementation, no
redundancy) so every number is byte-identical to what students see in the app,
then layers the course's tested rigor on top:

  * single-root profile : frequency, concentration (Gini, top-3 share),
                          size-normalized home surah (support floor), partners
  * pair statistics     : raw lift, length-adjusted lift, analytic z,
                          Monte-Carlo p, tier label
  * triple/motif        : same length-aware null extended to 3 roots
  * cluster centrality  : degree / strength within a themed root set

Methodology locked with the user:
  - natural units only (root, ayah, surah); legitimate orderings only
    (canonical, revelation-as-indicative); NO arbitrary divisions
  - every co-occurrence / motif claim cleared by a length-preserving null,
    cross-checked analytic vs Monte-Carlo
  - Meccan/Medinan is NOT used as a core measure (external, surah-coarse)
"""
from __future__ import annotations
import os, sys, math, json, collections
import numpy as np

# --- locate the app (single source of the algorithms) ----------------------
APP_DIR = os.environ.get(
    "QRE_APP_DIR",
    r"/sessions/practical-intelligent-noether/mnt/Downloads/Quran_Root_Explorer_Web_v1.2",
)
sys.path.insert(0, APP_DIR)
import analysis                      # noqa: E402
import pair_classification as pc     # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS_PATH = os.path.join(HERE, "Book6.xlsx")

# --- load once --------------------------------------------------------------
C = analysis.load_corpus(CORPUS_PATH)
N = C.n_ayahs
NL = analysis.normalize_letters
IDX = C.index_norm
FREQ = C.freq_norm
SUR_COL = analysis.COL_SURAH
SURAH_OF_ROW = C.df[SUR_COL].tolist()
SURAH_SIZE = collections.Counter(SURAH_OF_ROW)

# per-ayah distinct normalized root set + ayah length (in distinct roots)
AYAH_SETS = [{NL(t) for t in toks} for toks in C.root_tokens]
LEN = np.array([len(s) for s in AYAH_SETS], dtype=float)
SUMLEN = LEN.sum()
W = LEN / SUMLEN                      # length-bias weights


# --- primitives -------------------------------------------------------------
def k(r):       return NL(r)
def rows(r):    return IDX.get(k(r), [])
def f(r):       return FREQ.get(k(r), 0)
def aset(r):    return set(rows(r))
def joint(a, b): return len(aset(a) & aset(b))

def raw_lift(a, b):
    nA, nB, j = f(a), f(b), joint(a, b)
    return (j * N) / (nA * nB) if (nA and nB and j) else 0.0

def tier(a, b):
    L = raw_lift(a, b)
    tid, label, color, desc = pc.classify_lift(L)
    return label, desc


# --- length-aware null (pairs): analytic + Monte-Carlo ----------------------
def pair_null(a, b, mc=2000, seed=0):
    nA, nB = f(a), f(b)
    if not (nA and nB):
        return None
    obs = joint(a, b)
    pa = np.minimum(1.0, nA * W)
    pb = np.minimum(1.0, nB * W)
    p = pa * pb
    E = float(p.sum())
    sd = math.sqrt(float((p * (1 - p)).sum()))
    z = (obs - E) / sd if sd > 0 else 0.0
    adj = obs / E if E > 0 else 0.0
    if mc and mc > 0:
        rng = np.random.default_rng(seed)
        ix = np.arange(N)
        ge = 0
        for _ in range(mc):
            A = set(rng.choice(ix, size=nA, replace=False, p=W))
            B = rng.choice(ix, size=nB, replace=False, p=W)
            if sum(1 for x in B if x in A) >= obs:
                ge += 1
        p_emp = (ge + 1) / (mc + 1)
    else:
        p_emp = None
    return dict(obs=obs, nA=nA, nB=nB, raw_lift=round(raw_lift(a, b), 3),
                E_len=round(E, 3), adj_lift=round(adj, 3),
                z=round(z, 2), p_mc=(round(p_emp, 4) if p_emp is not None else None),
                tier=tier(a, b)[0])


# --- length-aware null (triple/motif) ---------------------------------------
def triple_null(a, b, d, mc=2000, seed=0):
    na, nb, nd = f(a), f(b), f(d)
    if not (na and nb and nd):
        return None
    obs = len(aset(a) & aset(b) & aset(d))
    pa = np.minimum(1.0, na * W); pb = np.minimum(1.0, nb * W); pd = np.minimum(1.0, nd * W)
    p = pa * pb * pd
    E = float(p.sum()); sd = math.sqrt(float((p * (1 - p)).sum()))
    z = (obs - E) / sd if sd > 0 else 0.0
    rng = np.random.default_rng(seed); ix = np.arange(N); ge = 0
    for _ in range(mc):
        A = set(rng.choice(ix, size=na, replace=False, p=W))
        B = set(rng.choice(ix, size=nb, replace=False, p=W))
        D = rng.choice(ix, size=nd, replace=False, p=W)
        if sum(1 for x in D if x in A and x in B) >= obs:
            ge += 1
    p_emp = (ge + 1) / (mc + 1)
    return dict(obs=obs, E_len=round(E, 3), adj_lift=round(obs / E, 3) if E > 0 else 0.0,
                z=round(z, 2), p_mc=round(p_emp, 4))


# --- single-root profile ----------------------------------------------------
def gini(vals):
    v = np.sort(np.array(vals, dtype=float)); n = len(v)
    if n == 0 or v.sum() == 0: return 0.0
    cum = np.cumsum(v)
    return float((n + 1 - 2 * np.sum(cum) / cum[-1]) / n)

def home_surah(r, min_count=3, min_size=10):
    rs = rows(r)
    by = collections.Counter(SURAH_OF_ROW[i] for i in rs)
    best = None
    for s, cnt in by.items():
        if cnt < min_count or SURAH_SIZE[s] < min_size:
            continue
        prev = 1000 * cnt / SURAH_SIZE[s]
        if best is None or prev > best["prevalence_per_1k"]:
            best = dict(surah=int(s), prevalence_per_1k=round(prev, 1),
                        count=int(cnt), surah_ayahs=int(SURAH_SIZE[s]))
    return best  # None => dispersed, no dominant home above the support floor

def partners(r, min_joint=4, min_pf=15, min_z=3.0, top=8):
    sa = aset(r); out = []
    for s, nf in FREQ.items():
        if s == k(r) or nf < min_pf: continue
        j = len(sa & set(IDX[s]))
        if j < min_joint: continue
        res = pair_null(r, s, mc=0)   # analytic-only for the wide sweep (fast)
        if res and res["z"] >= min_z:
            out.append((res["adj_lift"], s, j, res["z"], res["p_mc"]))
    out.sort(reverse=True)
    return [dict(partner=s, joint=j, adj_lift=al, z=z, p_mc=p)
            for al, s, j, z, p in out[:top]]

def single_profile(r):
    rs = rows(r)
    by = collections.Counter(SURAH_OF_ROW[i] for i in rs)
    counts_all = [by.get(s, 0) for s in SURAH_SIZE]
    top3 = sum(c for _, c in by.most_common(3))
    return dict(
        root=r, norm=k(r), freq_ayahs=f(r),
        n_surahs=len(by), top3_share=round(100 * top3 / max(1, len(rs)), 1),
        gini=round(gini(counts_all), 3),
        home_surah=home_surah(r),
        partners=partners(r),
    )


if __name__ == "__main__":
    print(f"Corpus: {N} ayahs, {len(FREQ)} roots  (from {CORPUS_PATH})")
    for r in ["عدل", "ظلم", "قسط", "نفس"]:
        p = single_profile(r)
        print(f"\n{r}: freq={p['freq_ayahs']} gini={p['gini']} home={p['home_surah']}")
        print("   partners:", [(d['partner'], d['adj_lift']) for d in p['partners'][:4]])


# --- size-true normalization: term-frequency + per-1000-roots ----------------
# Added after the methodology review: a rate "per 1000 ayahs" treats every ayah
# as one equal slot, ignoring that ayahs vary in length. The size-true rate
# divides by the total number of root-TOKENS in the corpus.
import collections as _collections
_TF = _collections.Counter()
for _toks in C.root_tokens:
    for _t in _toks:
        _TF[NL(_t)] += 1
TOK_TOTAL = int(sum(_TF.values()))          # 51024 root-tokens (with repeats)

def tfreq(r):                                # term-frequency (every occurrence)
    return _TF.get(k(r), 0)

def rate_per_1k_ayahs(r):                    # document rate
    return round(1000 * f(r) / N, 2)

def rate_per_1k_roots(r):                    # size-true rate (per 1000 root-tokens)
    return round(1000 * tfreq(r) / TOK_TOTAL, 3) if TOK_TOTAL else 0.0

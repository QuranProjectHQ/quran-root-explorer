"""Ayah-content Deep-Dive — explain an ayah in light of the whole corpus.

A FIRST-CLASS endeavor distinct from Root Exploration (not a tab of it). Decomposes
an ayah into its concepts, then surfaces the corpus's most relevant OTHER ayahs,
each TYPED by how it relates on three INDEPENDENT axes (lexical / semantic-
distributional / spatial-territory):
  direct · resonant · co-located · consensus · orthogonal · divergent.

Computational cross-references with evidence (axis z-scores + shared roots), NOT
tafsir. The heavy full report (docx + pdf) is produced by the background worker
`deep_dive.py ayah <s:a>`, not on this page.
"""
from __future__ import annotations

import streamlit as st

import analysis as _A
import deep_dive as DD
import plotly_charts as PC
from state import get_corpus, hero, log_page

st.set_page_config(page_title="Ayah Deep-Dive", page_icon="🔭", layout="wide")
log_page("ayah_deep_dive")
corpus = get_corpus()
st.markdown("<style>section[data-testid='stMain'] [data-testid='stCaptionContainer'],"
            "section[data-testid='stMain'] [data-testid='stCaptionContainer'] *"
            "{color:#111111 !important;font-size:14px !important;}</style>",
            unsafe_allow_html=True)


def _show_chips(items, n=8):
    items = [str(x) for x in items]
    if not items:
        st.markdown("<span style='font-size:20px;color:#0B1320'>—</span>",
                    unsafe_allow_html=True)
        return
    out = " ".join(
        "<span style='font-size:22px;color:#0B1320;background:#E8EEF6;border-radius:7px;"
        "padding:3px 14px;margin:4px 3px;display:inline-block;font-weight:600'>" + r + "</span>"
        for r in items[:n])
    if len(items) > n:
        out += f" <span style='font-size:14px;color:#444'>+{len(items) - n} more</span>"
    st.markdown(out, unsafe_allow_html=True)

hero("🔭 Ayah-content Deep-Dive", "explain an ayah in light of all relevant ayahs")
st.caption("Distinct from Root Exploration: decompose an ayah into its concepts, then surface "
           "the corpus's most relevant OTHER ayahs — TYPED by how they relate. "
           "Computational cross-references, not tafsir.")

with st.expander("📐 Method — the three axes & how this complements Motif analysis"):
    st.markdown(
        "Each candidate ayah is scored on **three INDEPENDENT axes**: **lexical** (shared "
        "roots), **semantic** (distributional closeness of meaning, even with NO shared "
        "words), **spatial** (shared territory). It is then typed: *consensus* (≥2 axes), "
        "*direct / resonant / co-located* (one), *orthogonal* (one, others independent), "
        "*divergent* (one high, another opposed).\n\n"
        "**Where this fits vs 🔺 Motifs:** Motif analysis is the *within-verse* lens "
        "(roots sharing a verse). This is the *across-verse* complement — it links ayahs "
        "by **resonance** (same meaning, different words) and **territory**, reaching the "
        "thematic/narrative ties co-occurrence cannot see (e.g. Yūsuf's grief ↔ his prison).")

@st.cache_data
def _surah_meta(_cid):
    df = corpus.df
    g = df.groupby(df[_A.COL_SURAH].astype(int))
    name = {int(s): str(sub[_A.COL_SURAH_NAME].iloc[0]) for s, sub in g}
    mx = {int(s): int(sub[_A.COL_AYAH].astype(int).max()) for s, sub in g}
    return name, mx


@st.cache_data(show_spinner="Matching against Book6…")
def _match(_cid, pasted):
    return DD.match_pasted_ayahs(corpus, pasted)


@st.cache_data
def _diac_text(_cid):
    df = corpus.df
    col = _A.COL_DIACRITIZED if _A.COL_DIACRITIZED in df.columns else _A.COL_SEGMENTED
    return {(int(s), int(a)): str(t) for s, a, t in
            zip(df[_A.COL_SURAH], df[_A.COL_AYAH], df[col])}


def _parse_refs(txt):
    out = []
    for tok in txt.replace(",", " ").split():
        if ":" not in tok:
            continue
        sp, a = tok.split(":", 1)
        try:
            sn = int(sp)
        except ValueError:
            continue
        if "-" in a:
            lo, _, hi = a.partition("-")
            try:
                out += [f"{sn}:{x}" for x in range(int(lo), int(hi) + 1)]
            except ValueError:
                pass
        else:
            try:
                out.append(f"{sn}:{int(a)}")
            except ValueError:
                pass
    return tuple(out)


_name, _mx = _surah_meta(id(corpus))
_surahs = sorted(_name)
mode = st.radio("Choose ayah(s) by", ["📖 Browse", "⌨️ Type references", "📋 Paste ayah text"],
                horizontal=True)
refs_tuple = ()
if mode.startswith("📖"):
    cc = st.columns([3, 1, 1])
    su = cc[0].selectbox("Surah", _surahs, index=_surahs.index(2),
                         format_func=lambda s: f"{s} — {_name.get(s, '')}")
    amax = _mx.get(su, 1)
    a1 = cc[1].number_input("From ayah", 1, amax, min(255, amax) if su == 2 else 1)
    a2 = cc[2].number_input("To ayah", int(a1), amax, int(a1))
    refs_tuple = tuple(f"{su}:{a}" for a in range(int(a1), int(a2) + 1))
elif mode.startswith("⌨️"):
    typed = st.text_input("References — supports ranges & commas", value="2:255",
                          help="e.g.  2:255  ·  2:255-257  ·  2:255, 2:256, 3:18")
    refs_tuple = _parse_refs(typed)
else:
    pasted = st.text_area("Paste ayah text from any website — verse numbers, brackets and "
                          "translations are stripped automatically by matching against Book6",
                          height=130,
                          placeholder="اللَّهُ لَا إِلَٰهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ …")
    if pasted.strip():
        hits = _match(id(corpus), pasted)
        if hits:
            st.caption("Potential matches from Book6 — 90%+ are pre-ticked; tick the correct one(s):")
            _dt = _diac_text(id(corpus))
            _sel = []
            for _n, (s, a, conf) in enumerate(hits, 1):
                cb, txt = st.columns([1, 9])
                if cb.checkbox(f"{_n}", value=(conf >= 0.90), key=f"m_{s}_{a}"):
                    _sel.append(f"{s}:{a}")
                txt.markdown(
                    f"**{s}:{a}**  <span style='color:#888;font-size:12px'>"
                    f"({int(conf * 100)}%)</span><br>"
                    f"<span style='font-size:15px'>{_dt.get((s, a), '')[:140]}</span>",
                    unsafe_allow_html=True)
            refs_tuple = tuple(_sel)
        else:
            st.warning("No matching ayah found — check the text is Qur'anic Arabic.")

go = st.button("Run deep-dive", type="primary")


def _ayah(refs_tuple, normalize):
    cache = st.session_state.setdefault("_ayah_cache", {})
    key = (refs_tuple, normalize)
    if key in cache:
        return cache[key]
    seeds = [(int(s), int(a)) for s, a in (r.split(":") for r in refs_tuple)]
    bar = st.progress(0.0, text="Starting deep-dive…")
    try:
        res = DD.ayah_deep_dive(seeds, normalize=normalize, corpus=corpus,
                                progress=lambda f, m: bar.progress(min(f, 1.0), text=m))
    finally:
        bar.empty()
    cache[key] = res
    return res


if not refs_tuple:
    st.info("Choose at least one ayah above (browse, type, or paste).")
    st.stop()
if go:
    st.session_state["ayah_go"] = refs_tuple
if st.session_state.get("ayah_go") != refs_tuple:
    st.info("Selection ready — click ▶ Run deep-dive to start "
            "(it re-confirms whenever you change the selection).")
    st.stop()
try:
    res = _ayah(refs_tuple, False)
except Exception as e:
    st.warning(f"⚠️  {e}")
    st.stop()

for sd in res["seed"]:
    st.markdown(f"### {sd['ref']}")
    st.markdown(f"<div style='font-size:29px;line-height:1.95;margin:6px 0 8px;"
                f"color:#0B1320'>{sd['text']}</div>", unsafe_allow_html=True)
    st.markdown("**concepts:**")
    _show_chips(sd["roots"])

syn = res["synthesis"]
_bc = syn["by_relation"]
g = st.columns(6)
g[0].metric("candidates", syn["n_candidates"], help="related ayahs above the relevance threshold")
g[1].metric("consensus", _bc.get("consensus", 0), help="related on ≥2 independent axes (robust)")
g[2].metric("resonant", _bc.get("resonant", 0), help="distributionally close in meaning, even with NO shared words")
g[3].metric("direct", _bc.get("direct", 0), help="shares roots (lexical overlap)")
g[4].metric("co-located", _bc.get("co-located", 0), help="shares spatial territory")
g[5].metric("divergent", _bc.get("divergent", 0), help="tension: close on one axis, opposed on another")
g2 = st.columns(6)
g2[0].metric("orthogonal", _bc.get("orthogonal", 0), help="related on a single axis; independent on the rest")
g2[1].metric("seed concepts", len(res["seed_concepts"]), help="distinct roots in the seed ayah(s)")
g2[2].metric("seed ayahs", len(res["seed"]), help="number of seed ayahs analysed")

_pts = [dict(label=d["ref"], x=d["axes"]["semantic"], y=d["axes"]["lexical"],
             relation=t, size=d["axes"]["spatial"])
        for t, lst in res["related_by_type"].items() for d in lst]
if _pts:
    st.plotly_chart(PC.chart_fusion_scatter(_pts, "semantic", "lexical",
                    f"{', '.join(res['request']['seeds'])} — relational fusion map", zlab="spatial"),
                    use_container_width=True)
    import pandas as _pd
    _tbl = [{"ayah": d["ref"], "relation": t,
             "L": d["axes"]["lexical"], "S": d["axes"]["semantic"], "P": d["axes"]["spatial"],
             "shared roots": " ".join(d["shared_roots"]) or "—", "متن آیه با حرکت": d["text"]}
            for t, lst in res["related_by_type"].items() for d in lst]
    st.markdown("**Plotted ayahs — ID ↔ text (match the points on the map above):**")
    st.dataframe(_pd.DataFrame(_tbl).sort_values(["relation", "ayah"]),
                 use_container_width=True, hide_index=True, height=330)

TYPE_DESC = {
    "consensus": "≥2 axes high — robust, reinforcing",
    "resonant": "distributionally close (meaning, even without shared words)",
    "direct": "shares roots (lexical)",
    "co-located": "shares spatial territory",
    "orthogonal": "one axis only, independent on the rest",
    "divergent": "close on one axis, opposed on another (tension)",
}
for t in ["consensus", "resonant", "direct", "co-located", "orthogonal", "divergent"]:
    lst = res["related_by_type"].get(t, [])
    if not lst:
        continue
    with st.expander(f"{t.upper()}  ·  {TYPE_DESC[t]}  ({len(lst)})"):
        for d in lst[:8]:
            ax = d["axes"]
            st.markdown(
                f"<div style='margin:0 0 12px'>"
                f"<span style='color:#111;font-weight:700'>{d['ref']}</span> "
                f"<span style='color:#1B263B'>· L={ax['lexical']:+.1f} S={ax['semantic']:+.1f} "
                f"P={ax['spatial']:+.1f} · shared: {' '.join(d['shared_roots']) or '—'}</span>"
                f"<div style='font-size:18px;color:#111;line-height:1.95;margin-top:2px'>"
                f"{d['text']}</div></div>",
                unsafe_allow_html=True)

st.divider()
st.markdown("#### 📄 Report  (Word · three registers)")
if st.button("Generate report", type="primary", key="gen_ayah"):
    try:
        import report_dive as RP
        _regs = ["technical", "plain_en", "plain_fa"]
        _b = st.progress(0.0, text="Generating report…")
        _docs = {}
        for _i, _reg in enumerate(_regs):
            _b.progress(_i / len(_regs), text=f"Generating {_reg.replace('_', ' ')}…")
            _docs[_reg] = RP.docx_bytes_from_result(res, _reg)
        _b.empty()
        st.session_state["ayah_report"] = {"seeds": res["request"]["seeds"], "docs": _docs}
    except Exception as e:
        st.warning(f"Report generation unavailable: {e}")
_rep = st.session_state.get("ayah_report")
if _rep and _rep.get("seeds") == res["request"]["seeds"]:
    _slug = "_".join(res["request"]["seeds"]).replace(":", "-")
    dl = st.columns(3)
    for col, (reg, label) in zip(dl, [("technical", "Technical"),
                                      ("plain_en", "Plain English"),
                                      ("plain_fa", "فارسی / Persian")]):
        col.download_button(f"⬇ {label}", _rep["docs"][reg],
                            file_name=f"ayah_{_slug}_{reg}.docx",
                            mime=("application/vnd.openxmlformats-officedocument"
                                  ".wordprocessingml.document"),
                            key=f"dl_ayah_{reg}", use_container_width=True)
    st.caption("Generated on demand. Matching PDFs come from the local worker: "
               "`python deep_dive.py ayah <s:a> --reports`.")

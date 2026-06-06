"""Generate the master Answer Bank from Book6 via engine.py.

Outputs (into RootCourse/):
  answer_bank.json  - machine-readable, consumed by the week builders
  answer_bank.xlsx  - human-auditable workbook (one sheet per layer)

Every number is computed by engine.py (which imports the app's own modules)
and every co-occurrence/motif is cleared by the length-aware null.
"""
import json, os, itertools
import engine as E
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))

# --- locked theme families --------------------------------------------------
SPINE = ["عدل", "ظلم", "قسط", "نفس"]                 # justice & the self
COMP_A = ["عسر", "يسر", "صبر", "رزق", "شكر"]          # hardship/patience/provision
COMP_B = ["هدي", "ضلل", "صرط", "رشد"]                 # guidance & the path
AUX = ["كفر", "حقق", "بطل", "وزن"]                    # contrast/auxiliary roots
ALL_ROOTS = SPINE + COMP_A + COMP_B + AUX

# pairs: within each family + validated teaching contrasts
PAIRS = []
for fam in (SPINE, COMP_A, COMP_B):
    PAIRS += list(itertools.combinations(fam, 2))
PAIRS += [("عدل", "ظلم"), ("شكر", "كفر"), ("حقق", "بطل"),
          ("قسط", "وزن"), ("نفس", "ظلم")]
PAIRS = list(dict.fromkeys(PAIRS))   # dedupe, keep order

# motif triples to test (verified candidates + the collapsed "bridge")
TRIPLES = [("نفس", "عدل", "قسط"), ("نفس", "ظلم", "قسط"), ("عدل", "قسط", "حقق"),
           ("صبر", "رزق", "شكر"), ("حقق", "هدي", "ضلل"), ("عدل", "قسط", "وزن")]

print("Computing single-root profiles...")
profiles = {r: E.single_profile(r) for r in ALL_ROOTS}

print("Computing pairs (length-aware null, MC)...")
pairs = []
for a, b in PAIRS:
    res = E.pair_null(a, b, mc=1500)
    if res:
        res = {"a": a, "b": b, **res}
        pairs.append(res)
        print(f"  {a}-{b}: rawLift={res['raw_lift']} adjLift={res['adj_lift']} z={res['z']} p={res['p_mc']} [{res['tier']}]")

print("Computing motif triples (triple null)...")
triples = []
for a, b, d in TRIPLES:
    res = E.triple_null(a, b, d, mc=1500)
    if res:
        res = {"a": a, "b": b, "d": d, **res}
        triples.append(res)
        print(f"  {a}-{b}-{d}: obs={res['obs']} adjLift={res['adj_lift']} z={res['z']} p={res['p_mc']}")

# cluster centrality: within-family degree (significant edges) + strength
print("Computing cluster centrality...")
clusters = {}
for name, fam in [("justice_self", SPINE), ("hardship_provision", COMP_A), ("guidance_path", COMP_B)]:
    deg = {r: 0 for r in fam}; strg = {r: 0.0 for r in fam}
    for a, b in itertools.combinations(fam, 2):
        res = E.pair_null(a, b, mc=0)
        if res and res["z"] >= 3.0:           # significant edge under length null
            deg[a] += 1; deg[b] += 1
            strg[a] += res["adj_lift"]; strg[b] += res["adj_lift"]
    clusters[name] = {"degree": deg, "strength": {k: round(v, 2) for k, v in strg.items()}}

bank = {"meta": {"n_ayahs": E.N, "n_roots": len(E.FREQ),
                 "spine": SPINE, "companion_A": COMP_A, "companion_B": COMP_B},
        "profiles": profiles, "pairs": pairs, "triples": triples, "clusters": clusters}

with open(os.path.join(HERE, "answer_bank.json"), "w", encoding="utf-8") as fh:
    json.dump(bank, fh, ensure_ascii=False, indent=2)

# --- xlsx (human-auditable) -------------------------------------------------
prof_rows = []
for r, p in profiles.items():
    hs = p["home_surah"] or {}
    prof_rows.append({
        "root": r, "freq_ayahs": p["freq_ayahs"], "n_surahs": p["n_surahs"],
        "top3_share_%": p["top3_share"], "gini": p["gini"],
        "home_surah": hs.get("surah"), "home_prev_per_1k": hs.get("prevalence_per_1k"),
        "home_support": f"{hs.get('count','-')}/{hs.get('surah_ayahs','-')}",
        "top_partners": ", ".join(f"{d['partner']}({d['adj_lift']})" for d in p["partners"][:5]),
    })
with pd.ExcelWriter(os.path.join(HERE, "answer_bank.xlsx")) as xw:
    pd.DataFrame(prof_rows).to_excel(xw, sheet_name="single_roots", index=False)
    pd.DataFrame(pairs).to_excel(xw, sheet_name="pairs", index=False)
    pd.DataFrame(triples).to_excel(xw, sheet_name="motifs", index=False)
    crows = []
    for name, c in clusters.items():
        for r in c["degree"]:
            crows.append({"cluster": name, "root": r,
                          "degree": c["degree"][r], "strength": c["strength"][r]})
    pd.DataFrame(crows).to_excel(xw, sheet_name="clusters", index=False)

print("\nWrote answer_bank.json and answer_bank.xlsx")

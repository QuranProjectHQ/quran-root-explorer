# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"dlcommon.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
B=json.load(open(os.path.join(WK,"dl_data_bank.json"),encoding="utf-8"))
lets=B["letters"][:12]   # 12 members, one disjoint letter each

# ---------- EXERCISE ----------
d=new_doc("Disjoint Letters — Exercise")
TITLE(d,"Disjoint Letters — Exercise: Is your letter a code?",
      "Two parts: a hand computation (Part 1) and an app investigation (Part 2). Submit the night "
      "before class. Integrity: use only your own row; every value must be reproducible from Book6.")
H(d,"Your assignment")
P(d,"Find your member number. You are given one disjoint letter and one sample sūra (with its letter counts). "
    "Part 1: compute your letter's density in that sūra by hand. Part 2: run the enrichment test in the app and report the verdict.")
rows=[["#","your letter","sample sūra","letter count in sūra","total letters in sūra"]]
for i,x in enumerate(lets,1):
    rows.append([str(i), x["letter"], x["sample_name"], str(x["sample_count"]), str(x["sample_total"])])
table(d,rows)
H(d,"Part 1 — By hand: your letter's density",size=12)
bullet(d,"Density = (letter count in sūra ÷ total letters in sūra) × 100. Show the division.")
bullet(d,"State in one line whether a high density alone would prove a 'hidden code'. (It would not — that is what Part 2 tests.)")
H(d,"Part 2 — In the app: run the enrichment test",size=12)
bullet(d,[("Open the app → Two Books → Disjoint Letters → ",False),("🔤 Sequence → Alphabet & letter density",True),(". Choose your letter.",False)])
bullet(d,"Record your letter's density RANK across the 114 sūras (1 = lowest, 114 = highest).")
bullet(d,[("Press the enrichment-test button. Record the permutation ",False),("p",True),
          (" and the verdict: is your letter ENRICHED in its own sūras (p < 0.05) or NOT?",False)])
H(d,"What to submit")
bullet(d,"Part 1: your density calculation (the division shown) for your sample sūra.")
bullet(d,"Part 2: the density rank, the permutation p, and your one-line verdict (code / no code).")
d.save(os.path.join(WK,"DisjointLetters_Exercise.docx"))

# ---------- ANSWER KEY ----------
d=new_doc("Disjoint Letters — Exercise Answer Key")
TITLE(d,"Disjoint Letters — Exercise Answer Key (instructor)",
      "All values computed from Book6 via the app's engine. Enrichment = bearer-sūra mean density vs "
      "20,000 random same-size sūra-sets. Significant = p < 0.05.")
H(d,"Part 1 + Part 2 — per-letter results")
rows=[["#","letter","sample sūra density %","enrichment p","verdict"]]
for i,x in enumerate(lets,1):
    verdict = "ENRICHED (but a frequency artefact)" if x["p"]<0.05 else ("borderline, n.s." if x["p"]<0.12 else "no code (n.s.)")
    rows.append([str(i), x["letter"], f"{x['sample_density_pct']}", f"{x['p']:.3g}", verdict])
table(d,rows)
H(d,"Teaching point")
P(d,[("Across all 14 disjoint letters, only ",False),("one",True),
     (f" (م) is enriched in its own sūras — and م is the single most common letter in Arabic, so even "
      f"that is a frequency artefact, not a code. {B['n_sig']} of 14 letters show no enrichment; ق's famous "
      f"lead comes back p ≈ {B['qaf']['p']:.2g} (not significant).",False)])
P(d,[("The verdict the class reaches together: ",True),
     (f"the disjoint letters are a POSITIONAL pointer (they index contiguous sūra-families, book-order "
      f"p ≈ {B['contiguity_p_mushaf']:.0e}, and flag the long sūras — median {B['median_muq']} vs "
      f"{B['median_other']} verses), NOT a letter-frequency cipher.",False)])
d.save(os.path.join(WK,"DisjointLetters_Exercise_Answer_Key.docx"))
print("DL exercise + key built")

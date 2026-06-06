# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
TB=json.load(open(os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json"),encoding="utf-8"))

d=new_doc("Two Books · Disjoint Letters — Worked Example")
TITLE(d,"Two Books · Disjoint Letters — Worked Example: signal vs folklore",
      "Two claims walked end to end with live Book6 numbers, permutation nulls, and FDR. The skill: keep a validated geometric signal and reject a famous cipher claim, using the same discipline for both.")
H(d,"Step 1 — State both claims",size=13)
bullet(d,"Claim A (geometry): the 29 muqaṭṭaʿāt sūras cluster contiguously in the order.")
bullet(d,"Claim B (folklore): Sūrat Qāf (50) is saturated with the letter qāf.")
H(d,"Step 2 — Test Claim A: contiguity",size=13)
table(d,[["test","p (vs permutation null)","verdict"],
         ["contiguity, muṣḥaf order","%.4f"%TB["contiguity_mushaf"],"significant"],
         ["contiguity, nuzūl order","%.4f"%TB["contiguity_nuzul"],"significant"]])
bullet(d,"Re-tag 29 random sūras thousands of times; the real tag clusters far more than chance — and it holds in TWO independent orderings.")
bullet(d,"Corroborating geometry: marked sūras median ≈ %d āyahs vs ≈ %d for the rest (longer); letter-entropy differs at p ≈ %.3f; root-entropy and richness at p ≈ %.4f."%(TB["median_muq"],TB["median_other"],TB["letter_entropy_p"],TB["root_entropy_p"]))
bullet(d,"Verdict A: SURVIVES — a real positional/organizational signal.")
H(d,"Step 3 — Test Claim B: the Qāf myth",size=13)
table(d,[["quantity","value (Book6)"],
         ["qāf density in sūra 50","3.76%"],
         ["its rank among 114 sūras","111th"],
         ["p (vs permutation null)","≈ 0.10"]])
bullet(d,"The density is unremarkable — sūra 50 ranks 111th, not 1st — and the elevation is not significant (p ≈ 0.10).")
bullet(d,"Verdict B: FAILS — an attractive story the data does not support.")
H(d,"Step 4 — Apply FDR to the whole battery",size=13)
P(d,"Read together, not in isolation: the thematic-coding claim comes in at p = %.3f — borderline, and it does NOT survive Benjamini–Hochberg correction; the embedding-similarity claim is p ≈ %.2f. Six geometric/compositional tests survive; three cipher claims fail."%(TB["theme_p"],TB["embedding_p"]))
H(d,"Step 5 — Report: one fact + one labelled reading",size=13)
P(d,[("Fact:  ",True),("muqaṭṭaʿāt sūras are significantly contiguous (p ≈ 0.0005, two orderings), longer (median 85 vs 26), and compositionally distinct (letter- and root-entropy ≤ 0.002); the Qāf-letter claim is n.s. (p ≈ 0.10).",False)])
P(d,[("Interpretation (labelled):  ",True),("I read the disjoint letters as a validated positional/organizational pointer to a distinct block of sūras — not a letter cipher.",False)])
d.save(os.path.join(WK,"DisjointLetters_Worked_Example.docx")); print("DL worked example saved")

d=new_doc("Two Books · Disjoint Letters — Quick Reference (1 page)")
TITLE(d,"Two Books · Disjoint Letters — Quick Reference (1 page)","The workbench at a glance. Keep this beside the app.")
H(d,"The app in 4 steps",size=13)
bullet(d,"Open Two Books → Disjoint Letters. Pick the scale: 🧭 Position, 🔤 Sequence, 🧩 Semantic.")
bullet(d,"For each claim, run the permutation null (re-tag 29 random sūras).")
bullet(d,"Read the battery AFTER Benjamini–Hochberg correction — never a lone p.")
bullet(d,"Record one fact + one labelled interpretation.")
H(d,"The measures",size=13)
bullet(d,[("Contiguity",True),(" — clustering of tagged sūras; p ≈ 0.0005 in muṣḥaf AND nuzūl order.",False)])
bullet(d,[("Per-family",True),(" — each family clusters (ḤM/ALR 0.0005, ALM 0.006, ṬSM 0.035).",False)])
bullet(d,[("Size",True),(" — marked sūras median ≈ 85 āyahs vs ≈ 26.",False)])
bullet(d,[("Letter / root info",True),(" — entropy & richness differ (≤ 0.002).",False)])
bullet(d,[("FDR",True),(" — Benjamini–Hochberg across the whole battery.",False)])
H(d,"Read honestly",size=13)
bullet(d,"DO require survival of the null AND FDR before keeping a finding.")
bullet(d,"DON'T accept the Qāf-letter claim (p ≈ 0.10) or thematic coding (0.049, gone after FDR).")
bullet(d,"DON'T read contiguity as theology — it is geometry.")
H(d,"Anchor numbers",size=13)
bullet(d,"contiguity 0.0005 (two orderings) · median 85 vs 26 · letter-entropy 0.002 · root-entropy & richness 0.0005 · Qāf 3.76%% rank 111 p ≈ 0.10 (n.s.).")
H(d,"Honest spine",size=13)
P(d,"A validated positional/organizational pointer — a contiguous block of longer, compositionally distinct sūras — not a letter cipher.",size=10)
d.save(os.path.join(WK,"DisjointLetters_Quick_Reference.docx")); print("DL quick-ref saved")

# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
BIODIR=os.path.dirname(WK)
SB=json.load(open(os.path.join(BIODIR,"handson","biology_data_bank.json"),encoding="utf-8"))
TB=json.load(open(os.path.join(BIODIR,"..","_handson_build","tour_bank.json"),encoding="utf-8"))["biology"]
fat=[r for r in SB if r["sura"]==1][0]

d=new_doc("Two Books · Biology — Worked Example")
TITLE(d,"Two Books · Biology — Worked Example: reading al-Fatiha's composition",
      "One sūra, walked end to end with live Book6 numbers. The skill: read composition and richness AGAINST length, and keep the genuine grammar signal separate from the confounds.")
H(d,"Step 1 — State the question",size=13)
P(d,"What does the 'genome lens' actually measure in al-Fatiha — and which of those numbers are meaningful versus driven by length and common letters?")
H(d,"Step 2 — Pull the live numbers",size=13)
table(d,[["quantity","value (Book6)"],
         ["total letters",str(fat["total_letters"])],
         ["most frequent letter",fat["top_letter"]+"  ("+str(fat["top_pct"])+"% )"],
         ["root-tokens",str(fat["root_tokens"])],
         ["distinct roots",str(fat["unique_roots"])],
         ["lexical richness",str(fat["richness"])]])
H(d,"Step 3 — Read base composition AGAINST baseline",size=13)
bullet(d,"The top letter is %.2f%% of al-Fatiha's %d letters — but that is close to the corpus baseline; every sūra draws on the same ~28-letter alphabet."%(fat["top_pct"],fat["total_letters"]))
bullet(d,"So read the DEVIATION from baseline, not the raw share. Nothing here is a hidden code.")
H(d,"Step 4 — Read richness AGAINST length",size=13)
bullet(d,"Richness = distinct roots ÷ total root-tokens = %d ÷ %d = %s."%(fat["unique_roots"],fat["root_tokens"],fat["richness"]))
bullet(d,"al-Fatiha is short, so it scores high; longer sūras repeat vocabulary and score lower. The number is mostly a LENGTH effect — never call a long sūra 'less rich' as if it were a choice.")
H(d,"Step 5 — Separate the genuine grammar signal",size=13)
P(d,"The confounds above (composition, richness, the Zipf slope of ≈ −1.56) are baseline expectations. The signals that actually SURVIVE the shuffle are the grammar footprint: di-codon bias at p ≈ 0.005, and the conditional-entropy drop H₀ 4.086 → H₁ 3.525 bits (knowing one previous letter removes ~½ bit). Those are the meaningful results.")
H(d,"Step 6 — Report: one fact + one labelled reading",size=13)
P(d,[("Fact:  ",True),("al-Fatiha uses %d distinct roots over %d root-tokens (richness %s); its top letter is %.2f%% of %d letters — both near baseline for its length."%(fat["unique_roots"],fat["root_tokens"],fat["richness"],fat["top_pct"],fat["total_letters"]),False)])
P(d,[("Interpretation (labelled):  ",True),("I read al-Fatiha's profile as ordinary for a short sūra — its high richness is length, not a special signal. The real structure in the corpus is the grammar footprint, not composition.",False)])
d.save(os.path.join(WK,"Biology_Worked_Example.docx")); print("biology worked example saved")

d=new_doc("Two Books · Biology — Quick Reference (1 page)")
TITLE(d,"Two Books · Biology — Quick Reference (1 page)","The genome lens at a glance. Keep this beside the app.")
H(d,"The app in 4 steps",size=13)
bullet(d,"Open Two Books → Biology. Pick the tab (base composition, codon usage, di-codon, complexity, Markov).")
bullet(d,"Read each number AGAINST sūra size; run the shuffle null for the structural tests.")
bullet(d,"Keep the genuine signals (di-codon bias, H₀→H₁) separate from the confounds (composition, richness).")
bullet(d,"Record one fact + one labelled interpretation.")
H(d,"The measures",size=13)
bullet(d,[("Base composition",True),(" — per-letter frequency; dominated by common letters.",False)])
bullet(d,[("Codon usage / Zipf",True),(" — root-frequency skew; slope ≈ −1.56.",False)])
bullet(d,[("Di-codon bias",True),(" — adjacent-pair structure; p ≈ 0.005 (a GENUINE signal).",False)])
bullet(d,[("Lexical richness",True),(" — distinct ÷ total roots; falls with length.",False)])
bullet(d,[("Conditional entropy",True),(" — H₀ 4.086 → H₁ 3.525 bits = real short-range memory.",False)])
H(d,"Read honestly",size=13)
bullet(d,"DO read composition and richness against sūra LENGTH.")
bullet(d,"DON'T read base composition as a hidden cipher.")
bullet(d,"DON'T call a length-driven richness a stylistic choice.")
H(d,"Anchor numbers (al-Fatiha)",size=13)
bullet(d,"top letter "+fat["top_letter"]+" = %.2f%% of %d letters · richness %s (%d roots / %d tokens)."%(fat["top_pct"],fat["total_letters"],fat["richness"],fat["unique_roots"],fat["root_tokens"]))
H(d,"Honest spine",size=13)
P(d,"A measurement frame, not a design claim: composition is set by common letters and length; the genuine signal is the grammar footprint (di-codon bias + entropy drop). No hidden code.",size=10)
d.save(os.path.join(WK,"Biology_Quick_Reference.docx")); print("biology quick-ref saved")

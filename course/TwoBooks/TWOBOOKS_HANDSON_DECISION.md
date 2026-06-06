# Two Books — Hands-on Kits · DECISION DOC (for sign-off)

Per COURSE_STANDARDS §1 (spec → approve → build once → verify once). Nothing is
built until this is approved. Goal: give students **hands-on app work** on the
three new v1.3 pages, in the exact WeekN format (App-and-Plot Guide · Exercise ·
Answer Key). App: https://quranproject-quran-root-explorer.hf.space/

## Scope

Three self-contained hands-on kits, one per new page:

| Kit | App page (Two Books group) | Member task (the "hands-on") |
|-----|----------------------------|------------------------------|
| **A. Disjoint Letters** | 🔠 Disjoint Letters | each member tests ONE disjoint letter for a "letter-frequency code" |
| **B. Signal** | 📡 Signal | each member tests ONE root for bursty vs even spacing |
| **C. Biology** | 🧬 Biology | each member profiles ONE sūra's base/codon composition |

Each kit = 3 .docx, mirroring Week 2 exactly:
- `*_App_and_Plot_Guide.docx` — Part A live walkthrough · Part B the key skill · Part C cross-check rule.
- `*_Exercise.docx` — Part 1 by-hand computation · Part 2 in-app investigation · per-member table (12 members) · "what to submit."
- `*_Exercise_Answer_Key.docx` — all values computed from Book6 + teaching point.

## Standards adherence (locked)

- **Numbers:** the ONLY source is Book6 via the app's own kernel `twobooks_stats.py`
  (so the kit and the live app cannot disagree). Every value reproducible.
- **No fabrication / honest verdicts:** these pages test "is there a hidden code?"
  and mostly answer NO. The kits teach that honest negative, with permutation
  p-values and the length/frequency confound stated plainly (matches the app).
- **Arabic:** w:cs complex-script font on every run; verify with the w:cs sweep.
  Build the .docx via Python (NOT the Write tool — it truncates Arabic docx, §7).
- **Figures:** "computed from Book6," English titles, shaped Arabic on labels only.
- **Scope:** each kit teaches only its page's idea; cross-refs are labeled bridges.

## Build order (one at a time, validated)

1. Build **Kit A (Disjoint Letters)** Guide → you approve → Exercise + Key.
2. Verify (cs-sweep, numbers vs the bank, render to PDF and eyeball).
3. Then replicate for **Kit B (Signal)** and **Kit C (Biology)**.

---

## Kit A — Disjoint Letters (detailed; the template-setter)

**Concept taught:** the muqaṭṭaʿāt are a POSITIONAL pointer, not a letter-frequency
code. The hands-on lets each member try to find a code for their letter and
discover (collectively) that it isn't there.

**Part A — walkthrough (worked on ق, Sūrat Qāf):** open the app → Two Books →
Disjoint Letters → 🔤 Sequence → Alphabet & letter density. Pick ق. Read its
density rank across the 114 sūras, then run the bearer-enrichment test.
Real anchors (computed from Book6, will appear live):
- ق density rank of Sūra 50 (Qāf) = **111 / 114** (high — the famous lead).
- ق bearer-enrichment **p ≈ 0.10** → NOT significant at 5%. The single most
  suggestive letter still fails the test.

**Part B — the key skill:** read a permutation p-value. p = the fraction of random
same-size sūra sets whose mean letter-density is ≥ the bearer sūras'. Small p =
unusual; here almost every letter is unremarkable.

**Part C — cross-check rule:** one computed fact (rank + p from the app) + one
labeled interpretation; never claim a "code" the p-value doesn't license.

**Exercise — per-member assignment (12 of the 14 disjoint letters):**
Part 1 (by hand): given a sūra's count of your letter and its total letters,
compute the letter's density (×100). Part 2 (in app): read your letter's density
rank and run the enrichment test; report p and verdict.

**Answer-key data bank (computed from Book6, enrichment vs 20,000 random subsets):**

| # | letter | # bearer sūras | bearer-mean density | enrichment p | verdict |
|---|--------|----------------|---------------------|--------------|---------|
| 1 | ا | 13 | 0.1802 | 0.69 | n.s. |
| 2 | ل | 13 | 0.1177 | 0.24 | n.s. |
| 3 | م | 17 | 0.0840 | **0.018** | enriched (but م is the commonest letter — a frequency artifact) |
| 4 | ح | 7 | 0.0125 | 0.67 | n.s. |
| 5 | ر | 6 | 0.0373 | 0.79 | n.s. |
| 6 | س | 5 | 0.0166 | 0.78 | n.s. |
| 7 | ص | 3 | 0.0076 | 0.43 | n.s. |
| 8 | ط | 4 | 0.0049 | 0.33 | n.s. |
| 9 | ع | 2 | 0.0286 | 0.39 | n.s. |
| 10 | ق | 2 | 0.0269 | 0.10 | borderline, n.s. |
| 11 | ه | 2 | 0.0465 | 0.67 | n.s. |
| 12 | ي | 2 | 0.0810 | 0.23 | n.s. |
| (ك, ن: single-bearer, optional spares) | | | | | |

**Teaching point:** 13 of 14 disjoint letters show NO density enrichment in their
own sūras; the one "hit" (م) is the most frequent Arabic letter overall, so its
result is a frequency artifact, not a code. The class collectively reproduces the
app's verdict: a pointer, not a cipher.

---

## Kit B — Signal (sketch; finalized after A is approved)

**Concept:** does a root cluster in bursts or spread evenly through the text?
**Walkthrough:** Signal → Root recurrence; read the Fano factor (variance/mean of
gaps) and the dispersion p vs a Poisson null. **Exercise:** each member gets a root,
computes a mean gap by hand (Part 1) and reads its Fano + p in the app (Part 2).
**Bank:** per-root Fano + dispersion p from Book6.

## Kit C — Biology (sketch; finalized after A is approved)

**Concept:** the genome lens — base (letter) and codon (root) composition of a sūra.
**Walkthrough:** Biology → Base composition + Codon usage (Zipf). **Exercise:** each
member gets a sūra, computes a base proportion by hand (Part 1) and reads its
composition + lexical richness in the app (Part 2). **Bank:** per-sūra composition
+ richness from Book6.

---

## Sign-off questions

1. Approve this scope + the Disjoint-Letters detail, and I build Kit A's Guide first?
2. Cohort size — is it still **12 members** (matches Week 2)?
3. Where should the kits live — a new `TwoBooks/<topic>/handson/` folder, or
   weekNN-style folders continuing the sequence (e.g., week11+)?

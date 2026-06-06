# CROSS-IMPACT — propagate every discovery across all modalities (living doc)

**Standing practice (user-mandated):** whenever something is discovered, works in practice, or moves the
objective, READ IT BACK across the whole modality set — both explored and planned — and record (a) what it
RE-INTERPRETS, (b) what it asks us to RE-RUN, (c) what new test it OPENS. Update this file at every find.
Discipline unchanged (DESIGN_STANCE gates); this is about not letting findings stay siloed.

**NOTHING IS FINAL (user-mandated, stronger form):** treat NO verdict — positive OR null — as closed.
Every "final" result is provisional and must be RE-EVALUATED whenever another modality yields a relevant
insight. Cross-reference continuously: a null in one lens may be a signal relocated to another's grain; a
positive may be a generic effect another lens exposes. Re-open finals on purpose, not only on accident.

Legend: ⟳ re-run · ↻ re-interpret · ✦ opens new test.

---

## D1 — Multimodal FUSION is the signature (no single axis; AUC ≈0.94) [#35]
- ↻ Every NULL modality (phonosemantics #38, iltifāt #40, wazn #41, discourse-sequencing #44, syntax #45/#47,
  field-dynamics #46) is "null *standalone*" — its FUSION contribution is a separate question.
- ⟳ **Re-run fusion including the NEW positives as features**: muqaṭṭaʿāt position/root-cohesion, canonical-
  order coherence (#57), recurrence-variation profile (#43). Does AUC rise above 0.94? (Grain mismatch —
  sūra-level vs window-level — must be handled; do a sūra-level fusion variant.)
- ✦ A "fusion contribution" score per lens (drop-one-out AUC) to rank lenses by marginal value, not p-value.

## D2 — VARIED RECURRENCE is the strongest axis; = self-interpretation [#42/#43]
- ↻ Refrain (#33), rings (#31–32), discourse-inventory (#44) are facets of one repetition family; recurrence
  is the one measured at the right grain.
- ✦ Field RECURRENCE (not sequencing) untested: #46 tested field *sequencing* (null) — does a semantic field
  RE-CUR across distant passages like a narrative does? Re-open #46 as recurrence, not transition.
- ⟳ Sharpen with edit-distance / Kendall (DoE E3) — quantify re-expression vs copying.

## D3 — MUQAṬṬAʿĀT = position + root-cohesion + Book-theme (divinely-rooted) [#50–56]
- ✦ The root-space-cohesion test generalizes: apply it to OTHER a-priori sūra groups — Meccan/Medinan, the
  seven long (al-sabʿ al-ṭiwāl), the Musabbiḥāt, the Ḥawāmīm beyond muqaṭṭaʿāt — is grouping-cohesion special
  to the disjoint letters or general to named groups? (Distinguishes "letters" from "any traditional set".)
- ↻ Confirms the "pointer" idea (signal-geometry §8) at root grain.
- **✓ DONE (#59): cohesion is NOT special.** Other named groups cohere as much or more (al-sabʿ al-ṭiwāl
  cos 0.78 z=+5.4; Medinan z=+5.4) → the muqaṭṭaʿāt CONTENT-cohesion (#53/#54) is a general grouping/register
  effect; DOWN-WEIGHTED. Position pointer (#50/#51) + half-alphabet stay distinctive. Nuance: letter-group >
  several meaning-defined groups. LESSON: a positive can be a generic property — always test it against
  other a-priori groupings before claiming specialness.

## D4 — REARRANGEMENT / ORDERING is first-class; āyah-final-word stream [DoE]
- ↻ Rhyme/fāṣila (#34–37) is the SOUND of the verse-end; the fāṣila ROOT/CONCEPT stream (m2) is its MEANING
  in sequence — Lens 3 × Lens 12 × Lens 16 fuse at the verse-end.
- ✦ Re-examine #57/#58 with order-aware methods (Kendall, Mantel) and the fāṣila-concept ordering.
- ⟳ Re-run #46 field-sequencing using the fāṣila-concept stream as the unit (verse-ends may chain where bodies don't).

## D5 — DIVINE-ROOTEDNESS control (rasm/roots, not ḥarakāt) [DESIGN_STANCE]
- ↻ Recited/#49 deprioritized; prosody #39 (consonantal proxy) was already rasm-ok; all other lenses rasm-based.
- ✦ Flag any future step that needs vocalization; prefer rasm/root/position reformulations.

## D6 — EDIT-DISTANCE / order-sensitivity (cosine is order-blind) [IDEA §7]
- ⟳ Any cosine/TF-IDF result (#46, #53, #54, #57, #58, recurrence) can be re-checked with an order-aware
  metric: does adding order change the verdict? Especially #53/#57 (cohesion) — is it bag-of-roots or sequenced?

## D7 — LENGTH / REGISTER-LOCALITY confound (recurs across #53/#54/#57/#58)
- ⟳ Retroactive control: any adjacency/cohesion claim needs a length/register-matched null (the Meccan-only
  null in #54 is the template). Re-audit #57 with a register-matched null (currently length-band only).
- ↻ Tempered reading of #58 (chronology interlocks more) flows from this.

## D8 — GRAIN matters; a null is "wrong scale," not "absence" [#42 word vs passage; telescope rule]
- ✦ Re-test the NULL modalities at other grains/formulations before calling them dead: phonosemantics at
  root-pair grain; field-dynamics as recurrence (D2); syntax via dependency *relation-type* profile (not just depth).
- ↻ Reframes every null entry in EVIDENCE as scale-specific, not final.

---

## Priority back-propagation queue (concrete)
1. **Sūra-level FUSION re-run** with new positives (D1) — does the divinely-rooted signature integrate?
2. **Field RECURRENCE** re-open of #46 (D2/D8) — fields as recurring, not sequenced.
3. **Group-cohesion generalization** (D3) — is muqaṭṭaʿāt cohesion special vs other named groups?
4. **fāṣila-concept stream** (D4 = DoE E2) — meaning chaining at verse-ends.
5. **Register-matched re-audit of #57** (D7).

## Status
Living doc. Started this session. Update at every discovery; mirror priority items into DESIGN_OF_EXPERIMENTS.md.

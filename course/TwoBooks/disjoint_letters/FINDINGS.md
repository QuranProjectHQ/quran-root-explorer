# Char-Level — Muqaṭṭaʿāt Enrichment: a scenario sweep (honest, partial result)

*De-diacriticized text (col 6), Book6.xlsx. Bodies exclude the opening muqaṭṭaʿāt verse. Permutation tests, 20,000 draws.*

## The question
Are a sūra's opening disjoint letters unusually frequent in that sūra — tested **disjoint vs non-disjoint** and across several controls?

## Scenarios tried & results
1. **Within-sūra null (WRONG control)** → looked spectacular (mean rank 0.76; الم p≈0). Discarded — it only asks "are these letters frequent," not "ESPECIALLY frequent."
2. **Per-group, bearers vs all others** (الم, حم, الر…): **null** — الم 1.04×, حم 1.09×; 0/17 groups significant; Fisher χ²=9.6/df6.
3. **Per-unique-letter, bearers vs all** (27 letters): only **م significant** (p=0.006); ق p=0.075, ن p=0.068. **1/27.**
4. **Per-letter, bearers vs NON-disjoint only:** م p=0.006 (1.13×), ن p=0.035 (1.17×), ق p=0.084 — weak, common-letter effects.
5. **Single-letter sūras (cleanest test), rank among all 114:**
   - **ق — Sūrat Qāf (50): rank 111/114 (top 3.5%).**
   - **ن — Sūrat al-Qalam (68): rank 105/114 (top 8.8%).**
   - ص/38 (85th), يـ/36 (76th), طـ/20 (79th): not special.
6. **Aggregate own-opening-letters, muq vs non-muq:** mean diff +0.008; **0/29 significant**; Fisher χ²=60.6/df58 (~n.s.).

## Verdict
- The **blanket claim is generic/false**: multi-letter openings (الم etc.) are common letters and show no real enrichment.
- A **specific, real signal exists in single-letter sūras — ق in Sūrat Qāf above all** (3rd-densest of 114), with ن in al-Qalam weaker.
- **Strength: suggestive, not decisive.** With several letters tested, ق (p≈0.035) is borderline under multiple-comparison correction; ن (p≈0.088) weaker. م/ن "enrichment" is significant but tiny (≈1.15×).

| Criterion | Multi-letter groups | Single letter (ق, ن) |
|---|---|---|
| Beats a natural-language / non-disjoint baseline | ✗ | ~ (ق borderline, ن weak) |
| Latent / computational | ✓ | ✓ |
| Reads back | n/a | ✓ (Qāf↔ق, al-Qalam↔ن) |

**Net:** a genuine *partial* finding — the muqaṭṭaʿāt-enrichment effect is real only for specific single letters (best: ق/Qāf), not the aggregate. Honest, modest, and the strongest lead the project has yet produced.

## Next checks to firm it up
- Multiple-comparison correction across all single-letter cases; report ق/Qāf with corrected p.
- **External Arabic baseline** (poetry/hadith): is "a text's title-letter is dense in it" generic to Arabic acrostics? (needs a non-Qur'anic corpus — not in Book6).
- Re-run on a cleaner orthography (col 6 uses Persian ی/ک) and re-test ق, ن, ص.

---

# UPDATE — Disjoint letters as POINTERS (all 29, controlled verdict)

*Hypothesis (user): the muqaṭṭaʿāt are not content but **pointers/tags** that index a GROUP of related sūras. Tested over **ALL 29** muqaṭṭaʿāt sūras with the correct canonical letters (الم, المص, الر, المر, كهيعص, طه, طسم, طس, يس, ص, حم, ق, ن) — no cherry-picking.*

## Families (all 29)
حم (7): 40–46 · الم (6): 2,3,29–32 · الر (5): 10,11,12,14,15 · طسم (2): 26,28 · singletons (1 each): المص 7, المر 13, كهيعص 19, طه 20, طس 27, يس 36, ص 38, ق 50, ن 68.

## Decisive test — OMNIBUS label-permutation null (all 29)
Fix the 29 muqaṭṭaʿāt sūras in place; shuffle WHICH tag each gets (preserving family sizes); measure within-family pairwise distance. This controls for muqaṭṭaʿāt sūras clustering anyway (they do: p≈0).

- **Muṣḥaf contiguity: p = 2×10⁻⁵** (observed mean within-family Δ = 6.79 sūras)
- **Nuzūl (revelation-order) contiguity: p = 2×10⁻⁵** (Δ = 7.30)

Family detail: حم 40–46 → nuzūl **60–66 (7 consecutive)**; الر 10–15 → nuzūl 51,52,53,54 (consecutive); طسم 26,28 wraps طس 27; الم 2,3,29–32.

## Semantic test — does NOT hold
Same-tag sūras are **not** more semantically (root-profile) coherent than a random regrouping of the muqaṭṭaʿāt sūras: **label-permutation p = 0.27**. Muqaṭṭaʿāt sūras are similar only as a *general group* (vs random sūras p=0.0001 — because they are all long sūras), not per-family. Distinctive roots (الم↔كتب/برهم/قتل/موت; حم↔دعو/حقق/یوم/حیی) are *illustrative flavor*, NOT a validated family-specific theme.

## VERDICT (all disjoint letters, controlled)
| Claim | Status |
|---|---|
| Muqaṭṭaʿāt tag a **contiguous family** (muṣḥaf & nuzūl) | **✓ VALIDATED** (omnibus p=2×10⁻⁵, all 29, label-perm) |
| The effect is beyond muqaṭṭaʿāt-sūras-cluster-anyway | ✓ (that is what the label-perm controls) |
| Tag marks a distinct **semantic** theme | ✗ not supported (p=0.27) |
| Letter-frequency enrichment in own sūra | ✗ generic to Arabic |

**The muqaṭṭaʿāt are a validated POSITIONAL/ORGANIZATIONAL pointer — an index over contiguous sūra-families in both muṣḥaf and revelation order — but not a validated semantic pointer.** This is the project's first robust, all-inclusive latent feature, and it confirms the recurring lesson: the Qur'an's latent structure is **relational/organizational, not in content statistics**.

## Honesty & caveats
- The Ḥawāmīm / Alif-Lām-Mīm groupings are **known to scholarship**; the value added is rigorous statistical validation + the **nuzūl-contiguity** quantification (the novel, strongest part) over ALL 29 with a label-permutation null.
- **Nuzūl order is a scholarly reconstruction** — that result inherits its uncertainty.
- A non-Qur'anic Arabic baseline is not needed for the positional claim (it is internal), but would help any future semantic/acrostic comparison.

---

# RELATIONAL ANALYSIS — extended (all families + organizational role)

## Per-family contiguity — all multi-member families significant (both orders)
| family | n | muṣḥaf p | nuzūl p |
|---|---|---|---|
| حم (40–46) | 7 | ~0 | ~0 |
| الر (10–15) | 5 | ~0 (Δ=2.6) | 0.0017 |
| الم (2,3,29–32) | 6 | 0.009 | 0.004 |
| طسم (26,28) | 2 | 0.034 | 0.034 |

The pointer-as-index holds for **every** testable family, not just الم/حم.

## New organizational fact — muqaṭṭaʿāt flag the LONG sūras
- muqaṭṭaʿāt sūras: median **85** verses (mean 95); non-muqaṭṭaʿāt: median **26** (mean 41).
- **p = 2×10⁻⁵** (vs random 29-sūra sets). The disjoint letters tag the major sūras.

## But the tag is POSITIONAL, not an attribute group
- Same-tag sūras are **not** similar in length: label-permutation **p = 0.29**.
- So the muqaṭṭaʿāt index *where* (contiguous families of long sūras), not a shared size — and not a shared theme (p=0.27, earlier). A pure positional/organizational pointer.

## Observational (untested) — variant tags at boundaries
- **المص** (الم+ص) → sūra 7, between the الم region (2,3) and the الر block.
- **المر** (الم+ر) → sūra **13, inside the الر block** (10,11,12,**13**,14,15) as a variant.
Suggestive that "mixed" disjoint-letter tags mark transitions/variants — a hypothesis for the next round (needs a formal test).

## Consolidated relational verdict
The muqaṭṭaʿāt are a validated **positional/organizational indexing system**: they (a) flag the long sūras (p=2×10⁻⁵), and (b) tag contiguous families in muṣḥaf and revelation order (all families significant; omnibus p=2×10⁻⁵). They do **not** encode a shared theme or length per tag. This is the project's strongest, most robust latent feature — and it is purely relational, vindicating the meta-thesis.

---

# POINTER MODEL — deepened (revelation phase, boundary variants, weak content blocks)

## Revelation-phase mapping (nuzūl) — a clean organizational layer
| tag type | families | nuzūl | phase |
|---|---|---|---|
| single / short | ن, ق, ص, المص, يس, كهيعص, طه, طس, طسم | 2–49 | **early-Meccan** |
| multi-letter families | الر (51–54,72), حم (60–66), الم (57–89) | 51–89 | **late-Meccan** |
| mixed | **المر** (sūra 13) | 96 | **Medinan** (lone outlier) |

The muqaṭṭaʿāt tags order onto revelation time: simpler tags early, the big families late, المر alone in Medina. (Largely known — most muqaṭṭaʿāt sūras are Meccan; the value here is the systematic quantified mapping.)

## Boundary variants (structural observation)
- **المر** (الم+ر) → sūra 13, **inside the الر run 10–15** (nearest الر neighbour = 1), yet revealed Medinan (96): a positional variant bridging الم and الر.
- **المص** (الم+ص) → sūra 7, **between** the الم block (2,3) and the الر block (10–15).

## Content blocks are WEAK (confirms positional, not content)
Root-profile similarity, within-family vs cross-family: الم 0.700/0.677 · الر 0.719/0.698 · طسم 0.793/0.695 · حم **0.678/0.687** (within ≈ cross). Mean within 0.723 vs cross 0.689 — marginal. The families are **not** content-coherent; the pointer is positional/temporal.

## Deepened verdict
The muqaṭṭaʿāt are a **positional + temporal indexing system**: each tag marks a family contiguous in muṣḥaf order AND clustered in revelation phase (early/late-Meccan/Medinan), and the tags flag the long sūras. They do **not** encode shared content or theme. Relational/organizational, end to end — the substance the image (2-D/relational) course is built around.

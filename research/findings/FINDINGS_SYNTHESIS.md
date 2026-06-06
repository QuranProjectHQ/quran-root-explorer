# FINDINGS SYNTHESIS — the coherent, consistent digest to draw from

Single source of truth for *what we have learned*, organized by verdict class. Stays in lockstep with
`EVIDENCE.md` (raw numbers), `SIX_LENSES_PAPER.md` (narrative, 17 lenses), `COVERAGE_MAP.html` (coverage),
`DESIGN_STANCE.md` (controls). Update this whenever a finding lands or is revised. Data-driven, no overclaim:
every entry = measurement + boundary.

State: 17 lenses + rearrangement experiments (E1–E4) + cross-impact re-opens (D2/D3); coverage ~72%.

---

## 0. Thesis (one paragraph)
The Qur'an's measurable distinctiveness is **structured RETURN at multiple scales** — not ornament,
sound-iconicity, syntactic depth, or local flow. Long-range *varied passage-recurrence* is the central axis;
at the verse-end this concentrates as a *fāṣila system* (repeated, content-fitted attribute-endings) with
*rhyme persistence*; the style isolates only as a *conjunction* (sustained rhyme + no meter + recurrence);
and one *sui-generis, divinely-rooted* layer — the muqaṭṭaʿāt *positional* pointer + *half-alphabet* — sits
outside the stylistic axes. Falsifiable summary: **locally the Qur'an is *less* continuous than ordinary
prose (self-contained āyāt); at long range it *returns* to itself more.** Architecture of return.

---

## 1. DISTINCTIVES (cross-text, gated)
| # | Lens / finding | Measure | Result | Boundary |
|---|---|---|---|---|
| #42/#43 | **Varied long-range recurrence** (Lens 9) | passage re-similarity tail, word-shuffle-controlled, verbatim-excluded | **~+3σ vs ordinary** | shared *in kind* with poetry (+2σ); Qur'an maximises it |
| #61 | …re-expression quantified (E3) | edit-distance + Kendall on recurrence pairs | cos ~0.68 but edit-sim ~0.27 | "same matter, re-sequenced," not copying |
| #34–37 | **Rhyme persistence** (Lens 3) | dominant-fāṣila share over a window | **+1.7σ vs sajʿ** | presence (rhyme itself) is shared with sajʿ |
| #62/#63 | **Fāṣila system** (Lens 17) | ending-word repetition; ending→body content-fit | repeat ≥3× share **0.28 > sajʿ 0.04**; fit **z≈+12** | repetition is cross-text; the content-fit is Qur'an-internal |
| #35 | **Fusion cell** (Lens 5) | classifier over all axes; rhyme×(non-)meter | **AUC ≈0.94**; pair 0.92 > 0.76/0.84 | only the *conjunction* separates; single axes don't |
| #50/#51 | **Muqaṭṭaʿāt POSITION + half-alphabet** (Lens 15) | 14/28 letters; canonical contiguity | exact 14/28; **Moran's I +0.54**, p<10⁻⁴, robust to nuzūl | *sui generis* (no other-Arabic baseline); POSITION/CARDINALITY only |
| #64 | …muqaṭṭaʿāt LETTER-COMBINATORICS (network) | letter co-occurrence graph | designed topology: hubs م/ا/ل, isolate ن, family-communities {الر},{حم-cluster},{كهيعص} | descriptive; content NOT letter-organized (Q≈0, z=1.73) — confirms #56 in network view |

## 2. INTERNAL-ONLY / DOWN-WEIGHTED (real vs shuffle, NOT cross-text distinctive)
| # | Finding | Why down-weighted |
|---|---|---|
| #53/#54 → #59 | Muqaṭṭaʿāt content-cohesion (root-space) | a GENERAL grouping effect — the seven long cohere more (cos 0.78); other traditional groups cohere too |
| #55 | Muqaṭṭaʿāt over-express the "Book" theme | internal anchor of the cohesion; not shown distinctive vs comparators |
| #57 / E1 / E4 | Canonical-order coherence (Lens 16) | internally real, but ordinary prose is MORE locally coherent (E1-cmp ratio 1.82 > 1.50); position-tracks-content is general |
| #58 | Sūra-junction interlock (tanāsub al-suwar) | real but modest; nuzūl interlocks *more* — not canonical-specific |

## 3. NULL / register-level (swept, defensible negatives)
Lens 1 repetition as a *bulk rate* (~+1σ) · Lens 2 rings (null) / refrain (local, ~9 sūras) · Lens 4
phonosemantics (null) · Lens 6 prosody at text level (null) · Lens 7 iltifāt (null vs prose; referent-blind)
· Lens 8 wazn (register; also register at the fāṣila, ≈sajʿ) · Lens 10 discourse *sequencing* (null;
move-*inventory* +2.4σ is register-level) · Lens 11 shallow syntax (register; wāw-parataxis +1.9σ, sajʿ
exceeds) · Lens 13 dependency-syntax with real parser (Qur'an *simpler* than prose) · Lens 12 lexical-semantic
field dynamics (sequencing null; field-*recurrence* D2 also null) · #48 directional sub-unit (Qur'an-null).

## 4. BLOCKED / DEPRIORITIZED
Lens 14 recited/phonological — instrument built, Qur'an-internal rhythm real (isochrony; weight-alternation),
but **DATA-BLOCKED** (no vocalized comparators) and **DEPRIORITIZED** (ḥarakāt = human artifact). Deep
dependency-syntax beyond depth, and referent-aware iltifāt, remain parser/coref-blocked.

---

## 5. The rearrangement program (how we probe order)
Ordering mechanisms: linear index · āyah-final word (fāṣila-concept) stream · rhyme-class · root
first-occurrence · frequency-rank. Methods: edit-distance/SW · LCS · Kendall/inversion · genome-rearrangement
· DTW · optimal transport · permutation entropy · Moran/Geary · Mantel · block-permutation sensitivity.
Key results: E1 coherence length ~few āyāt (order lives at the fine scale); E4 Mantel canonical r=+0.325 >
nuzūl +0.290 (global grouping > chronology); #60 the fāṣila caps its OWN verse, doesn't chain to the next.
Nulls always at the same scale + allowed-practice reorderings (nuzūl/Nöldeke) reported alongside. (DESIGN_OF_EXPERIMENTS.md)
D1 (fusion, window grain, Qur'an vs ordinary): dominated by rhyme-persistence (AUC 0.86; fused 0.875, no
synergy) — the survivors live at DIFFERENT grains, so single-grain statistical fusion can't combine them;
the real fusion is this conceptual synthesis + the #35 cell (vs sajʿ AUC 0.96).

## 6. Controls & practices (LOCKED — DESIGN_STANCE.md)
- Positive-control-first; G10 invariance gate (equal-N, ≥2 tokenizations, same-language baseline, null).
- Telescope rule: absence of evidence ≠ evidence of absence (buys *search*, never a *claim*).
- Divine-rootedness: study rasm/roots/words/structure/canonical order; deprioritize ḥarakāt + human groupings.
- Voice: data-driven only, no overclaim, no miracle-tone.
- Cross-impact propagation: nothing is final; re-evaluate every verdict as other modalities teach us.
- Rearrangement built into every experiment.
- Keep the paper (SIX_LENSES_PAPER.md) live at every finding.

## 7. Frontier (largest first)
Recited/phonological (data-blocked, largest region; deprioritized as ḥarakāt) · deep dependency-syntax &
referent-aware iltifāt (tooling-blocked) · D1 statistical FUSION of the survivors (capstone, pending) ·
extend the muqaṭṭaʿāt/rasm positional thread (the sui-generis divine layer).

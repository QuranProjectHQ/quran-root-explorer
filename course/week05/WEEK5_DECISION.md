# Week 5 — Decision Doc (approve before building)

_Concept: Lift & tiers — make co-occurrence rigorous (pair; mode = find). Lock scope + outline + measures + banks first. This is the payoff of Week 4; the next axis (direction / asymmetry) is Week 6. Every value computed from Book6._

## A. Locked components carried from Weeks 1–4
8-beat skeleton; fact-vs-labeled-interpretation; **control before concluding** (the spine); Book6 sole numbers; verify (cs-sweep + scope-grep + English-only figure titles + render); **dense 15-slide deck**; **figures shaped-Arabic, English titles**; **week self-contained** (build/ + xlsx + decision). Targets: ~3,500-word notes, 8 modules, 15 slides, 8 figures, analogies, no fluff.

## B. The concept (the rigorous payoff of Week 4)
Week 4 controlled co-occurrence by frequency (a simple ratio). But two problems remain: (1) roots cluster in LONG ayahs, so even the ratio is inflated; (2) a high ratio on thin support — or a big raw count — can still be chance. Week 5 fixes both:
- **Lift** = observed ÷ expected under a **length-aware null** (corrects for the long-ayah clustering).
- **Significance** = a **Monte-Carlo** p-value: shuffle roots across ayahs thousands of times (preserving ayah lengths and root frequencies) and ask how often chance matches the observed overlap.
- **Tiers** = combine lift + significance + support into a verdict: structural / borderline / spurious.
- **Calibration** = check the tier thresholds against known pairs (real bonds land Tier 1; generic pairs land Tier 3).

## C. Concept TESTED against Book6 — and the "unlearn"
- **Length-aware null deflates every lift** (roots do cluster in long ayahs): صلو↔زكو ×34.6 (Week-4 simple) → **×23.6** length-aware — still strong.
- **Monte-Carlo separates real from spurious — even at large raw counts:**
  - Tier 1 (p<0.001): صلو↔زكو ×23.6 · كيل↔وزن ×93.5 · عهد↔نقض ×65.6 · سجد↔ركع ×31.5 · قرض↔حسن ×20.6 · جنن↔نهر ×8.9.
  - Tier 3 spurious: **قول↔شيء — 113 shared ayahs, lift ×0.8, p ≈ 0.99** (both ubiquitous → pure chance); علم↔رحم 36 shared, ×0.7; صلو↔ءله 44 shared, p ≈ 0.065 (fails).
- **THE UNLEARN:** a big shared count is not a bond. قول and شيء share 113 ayahs and it means nothing; صلو and زكو share 28 and it is structural. Counting is not the same as significance.

## D. Scope tightrope
- **Week 5 (this week):** lift (length-aware null), Monte-Carlo significance, tiers, calibration — the rigorous verdict on a PAIR.
- **Week 6:** direction — P(A|B) vs P(B|A), asymmetry, network hubs. Named here only as a preview.
We teach the null + p-value + tiers as "the app computes them; we read and interpret them," at the no-stats level (intuition + analogy), not the full mathematics.

## E. Measures & thresholds (lock once)
- joint(A,B) = shared ayahs.
- length-aware expected (global long-ayah correction) → **lift** = joint ÷ expected.
- **Monte-Carlo p** = fraction of length-preserving shuffles with overlap ≥ observed (≥2,000 trials).
- **Tiers:**  Tier 1 structural = lift ≥ 3 AND p < 0.001 AND joint ≥ 5;  Tier 2 borderline = p < 0.05 but modest lift or thin support;  Tier 3 spurious = p ≥ 0.05 OR lift < 2.
- **Calibration set:** known-real (صلو↔زكو, كيل↔وزن) must be Tier 1; known-generic (قول↔شيء, علم↔رحم) must be Tier 3.

## F. Banks
12-pair assignment bank spanning the tiers (members compute lift + p and ASSIGN the tier):
Tier 1: صلو↔زكو, كيل↔وزن, عهد↔نقض, سجد↔ركع, قرض↔حسن, جنن↔نهر · Tier 2/3: عبد↔رزق (borderline), صلو↔ءله, علم↔رحم, قول↔شيء, نفس↔بصر, صلو↔ءمن (spurious). Worked pair: **صلو↔زكو**; cautionary case: **قول↔شيء**.

## G. Proposed module outline (8 beats each, ~45 min)
- M1 Opening & recap — Week 4 ranked bonds; today we JUDGE them: is a bond real?
- M2 Two leftover problems — long-ayah inflation; big counts that mean nothing.
- M3 The length-aware null — correct for roots clustering in long ayahs (lift deflates).
- M4 Monte-Carlo significance — shuffle thousands of times; how often does chance match?
- M5 The tiers — structural / borderline / spurious; the rule.
- M6 The headline & unlearn — قول↔شيء (113 shared) is spurious; صلو↔زكو (28) is structural.
- M7 Calibration & limits — benchmark the tiers; still no direction (Week 6); significance ≠ meaning.
- M8 Fact vs interpretation, wrap & bridge to Week 6 (asymmetry & networks).

## H. Figures (8, English titles, shaped Arabic)
1. The two leftover problems (long ayah + big count). 2. Length-aware null: lift deflates (صلو↔زكو ×34.6→×23.6). 3. Monte-Carlo: observed vs a null histogram. 4. The tier ladder (3 tiers, criteria). 5. The unlearn: قول↔شيء big-but-spurious vs صلو↔زكو small-but-structural. 6. The 12-pair calibration table (lift, p, tier). 7. A real-vs-spurious scatter (lift vs −log p, tiers colored). 8. Worked pair صلو↔زكو verdict card.

## I. Deliverables (self-contained in week05/)
data bank (json + xlsx) → 8 figures (week05/figs) → lecture notes (~3,500w) → worked example → app guide → exercise+key → quiz+key → dense deck → instructor script → quick-ref → further-study → build/ scripts. Verify once per batch.

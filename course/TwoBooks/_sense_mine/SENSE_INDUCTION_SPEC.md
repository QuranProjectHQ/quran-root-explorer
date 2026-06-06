# Sense-Induction Sub-Project — Method Spec & Validation Plan (for sign-off)

**Goal.** Produce the "sense" charts (polysemy %, senses-per-root, sense-preserving %,
within-vs-across-field sharing) **data-driven from Book6 only** — no hand-picked lexica, no
anyone's bias. Senses are *induced* from how each root's surface forms and co-occurring roots
actually pattern in the corpus.

**Why it's a sub-project, not a figure swap.** The pilot (task #66) proved a naive method is an
artifact: per-occurrence clustering made 89% of roots "polysemous" and ranked the *most frequent*
roots (ءله, علم, رحم) as most polysemous — frequency leaking in, not meaning. A credible result
needs a frequency-matched null and validation. That is real compute + method work.

## Method (documented, reproducible, seeded)

1. **Co-occurrence model.** Within-āyah root co-occurrence → PPMI vectors. Down-weight
   corpus-ubiquitous roots (drop the top-K most frequent from *context*; K documented) so the
   distributional "stop-word" effect (ءله/كون/قول dominating every neighbour list) is removed.
2. **Surface-form gate (§14a).** Every root is first sense-verified at the surface-form level
   (نار≠نور, ملائكة≠ملك …) before any clustering, so a "sense" is never a polysemy artifact of a
   mislabelled root.
3. **Per-root sense induction.** For each root (≥ MIN_OCC occurrences), build one context vector
   per occurrence; cluster by cosine (deterministic greedy, threshold COS_THR; both documented).
   Raw #clusters is the *candidate* sense count.
4. **THE FIX — frequency-matched null.** For a root with n occurrences, resample n contexts from
   the corpus-wide context pool, cluster, repeat (≥ NULL_DRAWS). **Polysemy score = observed
   clusters minus the null mean** (or a permutation p). A root is "genuinely polysemous" only if it
   clusters *more than its own frequency predicts*. This removes the frequency artifact.
5. **Derived charts**, each null-controlled: senses-per-root distribution; % polysemous (excess>null);
   sense-preserving vs changing (context-overlap of a root's surface forms vs null); within-vs-across
   field sharing (field = data-derived co-occurrence community, not a hand list).

## Validation plan (must pass before publishing any sense chart)

- **Frequency control:** plot polysemy score vs occurrence count — it must be ~flat (no upward
  trend). If frequent roots still score highest, the null isn't working; do not ship.
- **Face validity:** a small held-out set of *known* polysemous roots (e.g. عين eye/spring,
  بيت house/verse, امة nation/time) should score high; *known* monosemous roots should score low.
  This is a sanity check on the method, not a tuning target.
- **Parameter sensitivity:** report results at 2–3 values of COS_THR and K; conclusions must be
  stable across them, or the chart is labelled "indicative only."
- **Compute budget:** the null over ~560 roots × NULL_DRAWS exceeds the 45 s interactive limit, so
  run **chunked** (batch roots, cache co-occurrence, persist partials to JSON) — a background-style
  multi-pass build, not one live call.

## Outputs & honest labelling

Every sense chart is labelled **"data-mined (distributional), Book6, null-controlled, seed=N, COS_THR=…, K=…"**
and carries the standing caveat: *distributional sense induction is a heuristic proxy with documented
parameters — it removes hand-picked bias, but it is a method, not an oracle.* Charts that fail the
frequency-control or sensitivity checks are dropped, not shipped.

## Effort estimate

- Kernel + null + caching: moderate build.
- Validation runs (frequency control, face validity, sensitivity): the gating step.
- Figure generation + embedding into modules 07/08/09: small, once validated.
- **Recommendation:** build + validate first; only embed charts that pass. If validation fails,
  the honest outcome is to *not* have these charts rather than ship an artifact.

---

## VALIDATION RESULT (2026-06-03) — METHOD DID NOT PASS; charts NOT built

Built the kernel (PPMI co-occurrence, ubiquity down-weighting, greedy clustering) with the
frequency-matched null(n) curve, and ran the gates on a labelled set:

| root | polysemy-excess (obs − null) | expectation |
|---|---|---|
| عين eye/spring | +5.1 | high ✓ |
| خلق create/character | +5.0 | high ✓ |
| صبر patience (monosemous) | +4.1 | LOW ✗ |
| شكر gratitude (monosemous) | +3.9 | LOW ✗ |
| بيت house/verse | +1.9 | high (weak) |
| رحم mercy | −10.0 | occurrence-cap artifact |

**Face-validity gate FAILED:** monosemous صبر/شكر score as high as polysemous عين/خلق. The
frequency-null removed the *frequency* artifact, but the method still measures **contextual
diversity, not word-sense polysemy** — a single-sense word used across many situations clusters
into many "senses." The occurrence cap also distorts high-frequency roots.

**Decision (per this spec's own rule):** do NOT ship polysemy-% / senses-per-root /
sense-preserving charts from this method. A valid measure needs a sense-annotated lexicon, which
Book6 (text only) does not contain. Tuning parameters until صبر "looks monosemous" would be
result-driven bias and is explicitly refused. The sense charts remain **out of scope** unless an
external sense resource is added.

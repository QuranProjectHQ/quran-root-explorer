# Week 2 — Decision Doc (approve before any document is built)

_Concept: Distribution & Concentration. Goal: lock scope + outline + measures + banks FIRST (the Week 1 5× lesson), then build lecture notes → verify → dependents. No scope leak. Every number computed from Book6._

## A. Locked components carried from Week 1 (no rebuild)
- **8-beat module skeleton** (`LECTURE_MODULE_TEMPLATE.md`): every module has what · why · how · what-we-get · why-it-matters · in-the-data · takeaway · bridge.
- **Dual discipline:** computed fact vs labeled interpretation; report normalized measures.
- **Engine/Book6 is the only source of numbers;** verify with the cs-sweep + scope-grep + PDF-render protocol; write Arabic-heavy files via bash heredoc (Edit/Write truncate them in this folder).
- **docx/pptx build patterns** from Week 1 (Arial cs on every run, page footer; deck template palette + left accent bar).
- **No scope leak:** Week 2 teaches only distribution/concentration; partners/co-occurrence/lift/motifs are Weeks 3–5 and appear only as a labeled bridge.

## B. Concept suitability — TESTED against Book6 (this is why these concepts work)
- **Breadth (# of 114 surahs):** real range — عسر 9, رشد 9 (narrow) … كفر 77, علم 85, ءله 86 (broad).
- **Concentration (Gini / top-3 share):** real range — رشد Gini 0.945 / top-3 57.9% (concentrated) vs كفر Gini 0.689 (spread). Clean contrast pair: **رشد (concentrated) vs كفر (spread).**
- **Home surah, raw vs size-normalized — the HEADLINE / UNLEARN:** of the **50 most frequent roots, 30 have al-Baqara as their raw busiest surah; after size-normalization, 0 do.** The longest surah (286 ayahs) masquerades as everything's home. Example: **ظلم raw home = al-Baqara (2); normalized home = Ibrahim (14).**
- **Support floor (small-sample reliability):** without a floor, rare roots get spurious "homes" in tiny surahs — عسر → surah 94 (2 hits / 8 ayahs = 250/1k), صبر → surah 103 (1 hit / 3 ayahs = 333/1k). Floor (count ≥ 3 AND surah ≥ 10 ayahs) removes these; for very rare roots (عسر) **no** surah qualifies → honest "insufficient support."

**Diversity vs Week 1:** new tools — spread/breadth, inequality (Lorenz/Gini), small-sample reliability. The recurring "normalize before concluding" is the intended course spine, not repetition.

## C. CRITICAL REVIEW — trim the planned scope
The earlier handoff listed: density per surah + home surah + support floor + Gini + top-3 + breadth + density heatmap + revelation-order overlay. **That is too many tools for one 45-min, no-stats session** (Week 1's exact failure mode was over-broad scope).
**Recommended lean set (4 ideas, 1 unlearn):**
1. Breadth (how many surahs).
2. Concentration — top-3 share (intuition) + Gini via a Lorenz-curve picture (one-number summary, computed by the app, not hand-calculated).
3. Size-normalized home surah + support floor (carries the unlearn).
4. Unlearn: the al-Baqara length confound (30/50 → 0/50).
**Cut from core:** revelation-order overlay (caveat-only mention); density heatmap kept as ONE illustrative figure, not a measure students compute.

## D. Proposed module outline (8-beat skeleton, ~45 min, no scope leak)
- M0 Opening & recap (0–3): Week 1 = how much; today = where / how spread.
- M1 What distribution & concentration are (3–9).
- M2 Breadth — in how many surahs (9–14): عسر 9 vs كفر 77.
- M3 Concentration — Lorenz, Gini, top-3 share (14–22): رشد vs كفر.
- M4 The home surah, size-normalized (22–29): ظلم raw al-Baqara → norm Ibrahim.
- M5 Headline & unlearn (29–34): 30/50 → 0/50 al-Baqara confound.
- M6 The support floor — small-sample reliability (34–39): عسر→94 spurious; "insufficient support."
- M7 Advantages, limits & what distribution loses (39–43): concentration ≠ importance; still no relationships (Wk 3+).
- M8 Fact vs interpretation, wrap & bridge (43–47): bridge to Week 3 — partners & forms.

## E. Measures & thresholds (lock once)
- breadth = # distinct surahs (of 114).
- top-3 share = % of a root's ayah-hits in its 3 busiest surahs.
- Gini = standard Gini of per-surah ayah-counts across all 114 surahs (incl. zeros); computed by engine/app.
- home (raw) = surah with most ayah-hits.
- home (size-true) = argmax of (root tokens in surah ÷ surah TOTAL root-tokens × 1000) — **per 1,000 root-tokens, NOT per ayah** (ayahs vary in length); floor: count ≥ 3 AND surah ≥ 30 root-tokens; if none qualify → "insufficient support." See `NORMALIZATION_STANDARD.md` (locked).
- revelation order = NOT core; one-line caveat only.

## F. Banks
- Reuse the Week-1 root set (spine + companions) — all validated above.
- Worked example: **ظلم** (continuity with Week 1).
- Contrast roots: **رشد (concentrated) vs كفر (spread)**; support-floor demo: **عسر, صبر**.
- Per-member assignment bank: reuse Week-1 12-member root assignments (each member now profiles the DISTRIBUTION of their root).

## G. Screenshots to capture (you snap in the app → upload → I insert)
1. Per-Root Profile → "Ayah hits per surah" bar chart for **ظلم** (shows the al-Baqara spike).
2. Any app view of surah spread / normalized prevalence / home surah (to confirm exact screen — we'll check the app together).
3. A concentrated root (**رشد**) "ayah hits per surah" for visual contrast with ظلم/كفر.

## H. Build order after sign-off (each verified before the next depends on it)
engine/data bank for the chosen roots → figures (Lorenz/concentration, breadth, normalized-home; reuse seeded fig2/fig3 if they fit) → **lecture notes (approve)** → worked example → app guide → exercise+key → quiz+key → deck → instructor script → quick-ref → further-study. Verify once per batch.

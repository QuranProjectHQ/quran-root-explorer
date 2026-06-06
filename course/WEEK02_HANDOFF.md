# Week 1 → Week 2 Handoff & Lessons Learned

_Date: 2026-05-29. Purpose: close Week 1 honestly and make Week 2 fast and high-quality._

---

## Note 1 — What we did, what we didn't, and why it cost ~5× the time

### What we delivered (Week 1, frequency-only)
- A data spine that works: `engine.py` (imports the app's own modules; single source of numbers), `answer_bank.*`.
- 11 student/instructor docs + a slide deck, all single-spaced, page-numbered, Arabic-correct, values reproducible from Book6.
- Real, data-driven figures (frequency gallery, themed-root ladder, al-Fatiha worked example) and **real app screenshots** for the how-to.
- Two normalizations done right: **per 1,000 ayahs** and **per 1,000 roots** (size-true), including the ظلم↔هدي ranking flip.
- Clean folder structure with v1 archived and Week 2 seeded.

### What we did NOT do up front — the time sinks
1. **Didn't lock scope to the syllabus first.** The syllabus already said Wk1 = Frequency, Wk2 = Distribution & concentration. We built Wk1 as *frequency + density*, then had to **re-scope nine components** back to frequency-only. This single miss caused the largest rework.
2. **Didn't agree the lecture outline before writing prose.** We wrote full lecture notes, then rebuilt them as v2 against a revised outline. Writing twice.
3. **Didn't lock the measurement methodology before producing.** "Per 1,000 roots" (the size-true rate) was missing initially and had to be retrofitted into every component after the fact.
4. **Verified with the wrong oracle.** We "verified" Word docs by rendering in LibreOffice, which auto-substitutes fonts and **hid the Arabic complex-script (`w:cs`) bug** that broke in real Word. Caught late, fixed everywhere.
5. **Built breadth before validating one component.** Many deliverables were produced, then a single upstream decision (scope, normalization, outline) forced edits across all of them.
6. **Tooling friction we rediscovered repeatedly:** Write/Edit truncates Arabic-heavy files (must use bash heredoc); browser screenshots can't be saved to disk; `kaleido` needs the legacy 0.2.1; open Word/PowerPoint **locks** files mid-build; a build-script output-name collision **clobbered** the canonical lecture notes once.

### The pattern
Reactive, iterate-then-fix instead of **spec → approve → build once → verify once**. Most rework traced to four decisions that should have been settled before any document was generated: **scope, outline, measures/normalization, verification method.**

---

## Note 2 — How to run Week 2 to cut time and raise quality

### Decide these FOUR things before building anything (get explicit sign-off)
1. **Scope:** Week 2 = Distribution & Concentration only. Measures: per-surah density, size-normalized **home surah + support floor**, **Gini**, **top-3 share**, **breadth (of 114)**, density heatmap; revelation-order overlay **indicative only**. (No motifs/partners — those are Wk4–5.)
2. **Outline:** agree the section-by-section lecture outline (with minute markers) BEFORE writing prose. Mirror the v2 structure: foundation → method → data → limits → discipline → bridge.
3. **Measures & thresholds:** lock support-floor thresholds (min_count, min_surah_size), Gini definition, and how revelation order is flagged — once, in the engine.
4. **Banks:** pick the Week-2 root set and the per-member assignment bank up front (reuse the Wk1 12-root bank if it fits).

### Build order (dependency-first, each verified before the next depends on it)
1. **Engine helpers** for Wk2 measures (add to `engine.py`): they already exist for most (`single_profile`, `home_surah`, `gini`) — add any missing as named functions so every doc draws identical numbers.
2. **Answer/data bank** for the chosen roots (one JSON, like `wk1_keys.json`).
3. **Figures** from real data (reuse `gen_freq_*` patterns; fig2/fig3 already seeded in `week02/`).
4. **Lecture notes** (against the approved outline) → then everything else inherits its framing.
5. Worked example → app guide → exercise+key → quiz+key → deck → instructor script → quick-ref → further-study. **Reuse the course-wide rubric** (`Reading_Rubric.docx`) as-is.

### Reuse what already works (don't rebuild)
- `outputs/docbuild/build.js` — the docx engine: single-space styles, page-number footer, `table()`, `fig()`, bullets, and the **font-on-every-run fix** (Arabic `w:cs`). Keep using it.
- The pptx deck template (palette, `fit()`, `motif()`, dual-rate slide pattern).
- The kaleido 0.2.1 path for app-chart exports; the Chrome flow for live screenshots.
- `engine.py` as the ONLY source of numbers.

### Verification protocol (do once, at the end of each batch — not ad hoc)
- **Values:** spot-check against `engine.py`.
- **Arabic:** run the `w:cs` sweep (unpack each docx, assert 0 Arabic runs without `cs`). LibreOffice rendering is NOT sufficient proof for Word.
- **Scope:** grep extracted text for out-of-scope terms (e.g., for Wk2, ensure no stray frequency-only framing; for forward refs keep them intentional).
- **Render:** convert to PDF/JPG and eyeball figures, tables, page counts.

### Process guardrails that would have saved the 5×
- One decision doc approved before generation (scope + outline + measures + banks).
- Build the **lecture notes first**, get it approved, THEN generate dependents.
- **Distinct output filenames per builder** and a fixed run order to avoid clobbering; or one consolidated build script.
- Ask the user to **close Word/PowerPoint** before any regeneration batch (file locks).
- Prefer **bash heredoc** for any Arabic-heavy file creation.

---

## Pick-up checklist for Week 2 (state right now)
- Seeded in `week02/`: `Week2_Lecture_Notes_DRAFT.docx`, `Week2_Slides_DRAFT.pptx`, `fig2_density.png`, `fig3_concentration.png`.
- Engine already supports: density per surah, `home_surah` (with floor), `gini`, `top3_share`, `n_surahs`, dual rates.
- First action next session: **approve the four decisions above**, then build engine bank → figures → lecture notes → dependents, verifying once per batch.

---

## Note 4 — LOCKED normalization standard (2026-05-30)
- **Normalize density to per 1,000 ROOT-TOKENS at every level — never by ayah-count or surah-count.** Containers (ayahs, surahs) vary in size; only root-tokens are size-true. Spec: `NORMALIZATION_STANDARD.md`.
- Surah "home" uses root tokens ÷ surah root-tokens × 1,000; floor = count ≥ 3 AND surah ≥ 30 root-tokens, else "insufficient support."
- Evidence: ṣabr home = al-Baqara (raw) → al-Kahf (per-ayah) → at-Tur (per-roots); only per-roots is correct. Headline: raw al-Baqara 30/50 → 0/50 normalized.

---

## Note 5 — Master standards doc (2026-05-30)
All locked lessons are consolidated in **`COURSE_STANDARDS.md`** (read first). New rule added this session: **Figures must show actual Arabic (roots/forms/surahs), shaped via arabic_reshaper + python-bidi, DejaVu Sans — never transliteration-only, never isolated letters; always view the PNG before embedding.**

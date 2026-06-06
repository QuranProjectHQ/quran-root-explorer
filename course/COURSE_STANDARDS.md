# COURSE STANDARDS — Lessons Learned, Locked (read first)

_Living document. Every oversight we hit becomes a permanent rule here so it never recurs. Last updated 2026-05-30._

## 1. Process (the Week-1 5× lesson)
**spec → approve → build once → verify once.** Before building any week: test concepts against Book6, write a decision doc (scope + outline + measures + banks), get explicit sign-off. Build the **lecture notes first**, approve, then generate dependents. Never build breadth before one component is validated.

## 2. Lecture structure
Every lecture = modules; **every module carries the 8 beats**: what it is · why · how · what we get · why it matters · in the data · takeaway · bridge. Spec: `LECTURE_MODULE_TEMPLATE.md`. Beat 6 (real Book6 data) is mandatory in every module.

## 3. Normalization (size is the recurring confound)
**Normalize density to per 1,000 ROOT-TOKENS at every level — never by ayah-count or surah-count.** Containers vary in size. Surah home = root-tokens-in-surah ÷ surah total root-tokens × 1,000; support floor = count ≥ 3 AND surah ≥ 30 root-tokens, else "insufficient support." Spec: `NORMALIZATION_STANDARD.md`.

## 4. Scope discipline (no leak)
Teach only the week's concept. Later-week terms (partners, co-occurrence, lift, motifs…) appear **only** as a labeled bridge/preview, never taught early. Verify with a scope grep each batch.

## 5. Numbers
Book6 / `engine.py` is the **only** source of numbers. Conform shared constants across all docs (e.g., 51,044 ayah-tokens vs the engine's 51,024 — use the engine's). Every value reproducible; spot-check each batch.

## 6. Arabic in Word documents
Set the complex-script font (`w:cs`) on **every run** (font-on-every-run). **Verify with the w:cs sweep** (unpack docx, assert 0 Arabic runs without cs). LibreOffice rendering auto-substitutes fonts and **hides** the bug — it is NOT sufficient proof.

## 7. File writing in this workspace
The Edit/Write tools **truncate** Arabic-heavy and special-character files (and corrupt packed XML). **Write such files via bash heredoc / Python**, not Edit/Write. Re-validate well-formedness after any XML edit.

## 8. Slide decks
Build decks **fresh with python-pptx** — editing an existing .pptx's XML truncates tails and corrupts `presentation.xml`. Set the cs typeface on every run. QA by rendering to image and eyeballing for overflow/overlap.

## 8b. Slide deck density (locked this session)
15 slides; **body 18–20pt, titles 30pt** (bigger than the old 14–15pt). Pack **8–12 substantive bullets** per content slide (≈2× the old ~5) with analogies and real data — **fill the slide vertically**; no large empty lower half. Figure slides put the image on one side and packed bullets on the other. No fluff/filler. Always render and check no text overflows the slide.

## 9. Figures — Arabic (locked 2026-05-30)
- Figures show the **actual Arabic** roots / forms / surah names — never transliteration-only, never isolated/unjoined letters.
- Render Arabic with **`arabic_reshaper` + `python-bidi`** (`get_display(reshape(s))`) so letters join and read right-to-left; font **DejaVu Sans** (it carries the Arabic glyphs). Helper lives in `/tmp/figcommon.py` pattern (`ar()`, full 114 `SUR` Arabic surah-name map).
- Transliteration + English gloss belong in the **figure caption / legend** (for accessibility), not as a replacement for the Arabic.
- Always **view the rendered PNG** before embedding — confirm Arabic is connected and correctly ordered.

## 9b. Figures & RTL prose — two traps locked this session (Week 3)
- **Horizontal-bar label alignment:** place each value label at the SAME y-position/order as its bar. A reversed text loop (e.g. iterating `vals[::-1]`) silently puts the wrong number on each bar — it looks plausible and is easy to miss. **Always view the rendered PNG and check the longest bar carries the largest number.**
- **Bidi-safe prose & captions:** never put a number immediately after an Arabic word in inline prose or a caption (e.g. "آمن 41%, مؤمنين 16.5%"). Right-to-left reordering scrambles such Arabic-word + number lists. Put Arabic-adjacent numbers in **figures or tables** (cells isolate them); in prose keep Arabic as isolated words inside Latin sentences, and reference the figure for the numbers.

- **Figure titles are English-only — NO Arabic characters.** Arabic mixed into a title (especially with punctuation like "/" or a second Arabic word) reorders under bidi and scrambles. Arabic belongs only on axis tick labels and data-point labels, as isolated single tokens. Legends/cards/annotations must not mix an Arabic word with adjacent Latin text or numbers.

## 9c. Each week is self-contained (locked this session)
Every `weekNN/` folder holds everything needed to use AND reproduce that week, with nothing in scratch:
- **Deliverables:** lecture notes, instructor script, slide deck, worked example, app & plot guide, exercise + key, quiz + key, quick reference, further study.
- **Data:** the data bank as JSON *and* an instructor Excel (`WeekNN_Data_Bank.xlsx`).
- **Figures:** in the week folder (`weekNN/figs/`), all English-titled with shaped-Arabic labels.
- **Build provenance:** `weekNN/build/` with the figure-generation and document-build scripts plus a copy of `figcommon.py`, so the week regenerates from its own folder.
- **Decision doc:** `WEEKNN_DECISION.md`.
Shared, course-wide assets stay at the repo root and are *referenced, not duplicated*: the `Book6.xlsx` corpus, `engine.py`, the `SYLLABUS`, and the standards files (`COURSE_STANDARDS.md`, `NORMALIZATION_STANDARD.md`, `LECTURE_MODULE_TEMPLATE.md`).

## 10. Verification protocol (run once per batch, not ad hoc)
cs-sweep (Arabic) · scope grep · normalization grep (no per-ayah-as-size-true) · number consistency vs the bank · render to PDF/JPG and **eyeball figures/tables/Arabic** · clean temp files · present files. For high-stakes weeks, verify with a subagent.

## 11. App screenshots
If live browser capture is unavailable/denied, generate **app-faithful figures from Book6** (the same corpus the app analyzes) and label them "computed from Book6," not "screenshot."

---
### Companion specs
`LECTURE_MODULE_TEMPLATE.md` · `NORMALIZATION_STANDARD.md` · `WEEK02_HANDOFF.md` (Notes 1–4) · per-week `WEEKnn_DECISION.md`.


## 12. Slide canvas-fill standard (LOCKED 2026-05-31)
Slides must FILL the 13.33×7.5 canvas — no white voids. Build each content slide as vertically-tiled ZONES that tile top→bottom with ≤0.25in gaps: a tinted panel for each text block, a colored (navy/teal) band for the key takeaway, images sized to span their zone. Never leave a large empty band. Fonts: body ≥18pt, labels ≥16pt, takeaway/conclusion ≥21pt; AND figure/chart fonts ≥16pt (titles ≥18) so they read when embedded at ~0.8 scale. Verify by rendering to JPG and eyeballing for both voids and legibility.

### 12a. Diagrams vs. data-figures — density amendment (LOCKED 2026-06-03)
The "charts are editable shapes, never images" rule (§15) is REFINED, not repealed, for
Two Books companion decks. Two visual categories now coexist:
- **Diagrams & categorical charts** — STAY editable pptx shapes (`diagrams.py` boxes/arrows;
  `ebar`/`finding2` shape-bars). Use these for ladders, pipelines, audits, and genuinely
  categorical comparisons of a FEW values.
- **Data-figures** — MAY be embedded high-resolution images (matplotlib PNG, ≥150 dpi) when
  the content is a dense distribution that shape-bars cannot carry: occurrence rasters,
  multi-lag autocorrelation curves, full power spectra, scalogram heatmaps, Zipf curves,
  scatter-with-trend, histograms. Each data-figure MUST be (a) generated by a checked-in
  `gen_figs.py` that computes live from `Book6.xlsx` with a fixed seed (fully reproducible),
  (b) labelled in English / transliteration (no unshaped Arabic in matplotlib), and
  (c) sized to fill its slide zone with ≥16pt figure fonts (§12).
- **Anti-pattern to retire:** a slide whose only content is a 2-bar comparison. Either fold it
  into a denser multi-series chart, replace it with a data-figure, or demote it to a sentence.
- Decks must still meet §16a (≥20 slides, ≥half visual). Data-figures count as visuals.

### 14a. Concept = sense-verified SURFACE FORMS, never a raw root (LOCKED 2026-06-03)
A "concept" figure/count MUST be computed from the root's **sense-bearing surface forms**, not the
raw root token-count, because Arabic roots are polysemous and a raw root MIXES concepts. Verified
conflations in Book6 that this rule exists to prevent:
- **نور** = light (نور/منير) **vs** نار = FIRE — raw root is mostly fire, not light.
- **ملك** = sovereign/king (ملك/ملوك) **vs** ملائكة = ANGELS — raw root is ~half angels.
- **علم** = knowledge (علم/عليم/يعلم) **vs** عالمين = the WORLDS — raw root inflates knowledge with cosmos.
- **قوم** = people (قوم/أقوام) **vs** قيامة/مستقيم/أقام = standing/resurrection/establish.
- **حسب** = reckoning (حساب/حسيب) **vs** يحسب/تحسب = supposing.
- **جنن** = garden (جنة/جنات) **vs** الجن = jinn **vs** مجنون = madness.
Procedure (data-driven, reproducible, no hidden bias): for every concept-root, **print its surface-form
inventory from Book6**, assign each form to a sense by its transparent string (نار→fire, نور→light),
then count āyahs containing only the INCLUDED forms. Report the included/excluded forms in the build
script so the choice is auditable. **Balance breadth and depth:** breadth = many concepts across many
domains; depth = each concept verified at the surface-form level. A broad spectrum of *unverified* roots
is worse than a smaller spectrum of *verified* concepts. Applies to all concept-spectrum figures
(modules 08, 15, and any virtue/eschatology/divine-attribute spectra).

## 13. "A Closer Look" — recurring digression (LOCKED 2026-05-31)
One per week, numbered #1–#10. English title ONLY (no Arabic in titles; Arabic appears only inside shaped images/charts; NO transliteration in prose — use English glosses). Fixed 4-beat structure:
  1. THE CLAIM — a popular/intuitive reading, motivated by the week's measure.
  2. THE TEST — put it to Book6 with THAT week's tool; statistically valid (significance-tested), no eyeballing, no cherry-picking (use the full pre-committed set).
  3. THE VERDICT — scoped to the evidence; issue only what the data licenses and explicitly DECLINE sweeping claims (Week-9 discipline).
  4. LESSON #N — one transferable thinking-principle.
The ten Lessons accumulate into the Week-10 synthesis. Each digression binds to its week's measure (Wk1 frequency, Wk2 distribution/concentration, …) so it never re-runs a prior week. The positive-vs-vice question may recur as a SPINE, but each week must interrogate it with a new lens.

VERSE CITATION RULE (LOCKED): do NOT put verse translations or full verses on slides — they waste space. Cite the ADDRESS (surah-name surah:ayah) and, only where directly warranted, a SHORT Arabic snippet (a few shaped words). Members look up full text/translation themselves. Use the freed space for robust data content.


## 14. Concept-field rule for claims/verdicts (LOCKED 2026-05-31)
When a Closer Look (or any claim) tests a CONCEPT (virtue, vice, success, failure, mercy, etc.), do NOT rest it on a single literal root. Use a PRE-COMMITTED, transparent lexical FIELD (the union of the concept's roots), and report the test on the field. Single rare words (دسس=1, خيب=5) produce false ratios; fields are robust. Always significance-test the field comparison (binomial / Mann-Whitney). Example: 'success vs failure' is ~8× by single words but ~1.1× (n.s.) by field.

SURFACE-FORM RULE (LOCKED): anchor analysis on the ROOT, but do NOT bypass surface forms where senses diverge. When a root is polysemous, filter to the sense-bearing forms before counting a concept: e.g. زكو → soul-purification forms only (drop زكاة, the alms-tax); فجر → vice forms (فجور/فاجر), not dawn (الفجر); نجو → salvation, not نجوى (private talk); جبّار → the Divine-Name sense, not 'tyrant'. Report which forms were kept. (Worked: virtue/vice 5.6×→6.6× and purify/corrupt 1.4×→0.8× after form-filtering.)

## 15. Special Topics — LOCKED layout & chart standard (2026-05-30)
Special Topics live in their own dir (`SpecialTopics/`), separate decks + separate peer-review docx, built by `SpecialTopics/build/st_slides.py` (single source of layout). Locked rules:
- **Full-canvas fill, always.** Content band 1.18–7.28"; panels reach the bottom edge. Appendix snippets are distributed into EQUAL vertical slots so there is never an empty bottom.
- **Back-of-room fonts.** Body ≥16pt, panel headers 17–18, titles 19–21, chart titles 14, value labels 11.5, category labels 12.5.
- **Charts are EDITABLE pptx shapes** (bars = rectangles, every title/value/category label = a text box) — never images. English chart titles; Arabic only as shaped, editable axis labels; per-bar colors supported. ≥2 visuals per finding slide; short titles/labels.
- **Appendix** shows vocalized input snippets (col 11), ≥5 words; sample when data is plentiful, all when few.
- No redundant/old files in the dir — latest versions only.


### 15a. Empty-space lock — AUTO-FILL ENGINE (final)
`st_slides.panel()` now auto-scales font size (binary search) so each panel's text block fills ≥93% of the panel height; appendix snippets scale to their slot. Panels already tile the full content band (1.18–7.28"). Net: every slide self-fills — no manual font tuning, no empty bottoms, ever. Charts expand into any remaining band.

### 15b. Appendix — BALANCED CARD GRID (final)
The appendix flattens every available snippet into colored cards (coloured by category, tagged ref·category) and distributes them EVENLY across 1–3 columns, each column tiling the full content band. No empty or sparse columns are possible; cards auto-scale to their slot. Always supply all available snippets — the grid fills itself.


## 16. THE TWO BOOKS — lecture series spec (locked)
Two revelations of one Author: عالم التدوين (the WORD, قول الله = the Qur'an / Scripture) and عالم التكوين (the ACT, فعل الله = the Universe / Creation). Same source (Allah); primary addressee the human (insān); jinn deferred to a future lecture. Both are āyāt.
- Every lecture: **≥ 2 data-chart slides with real distributions from BOTH domains** (the Qur'an, computed from Book6, AND the partner science) — e.g. frequency/Zipf spectra, length distributions, composition bias, fidelity/degeneracy. **≥ half the slides are visuals** — editable pptx diagrams (boxes/arrows/connectors via `diagrams.py`) + rich data charts (editable shape-bars), short labels/titles, readable from the back, all self-filling.
- The cross-discipline parallel is a LABELLED analogy, audited stage by stage (✓ Supported · ✗ Breaks · ~ Silent-but-surmisable), with an explicit "not a scientific miracle / not evidence" disclaimer. Qur'anic data computed from Book6.
- Lectures live in `TwoBooks/<name>/` with deck + instructor script + their own `build/`.

### 16a. Companion lecture decks — slide-count & visual lock (LOCKED 2026-06-03)
Applies to every Two Books *companion* deck built from an 8-beat lecture-notes doc
(`<page>/lecture/*_Lecture_Slides.pptx`), inherited from the module-deck norm (20–21 slides):
- **≥ 20 slides per deck.** Title + framing/analogy-ladder diagrams + null-model diagram +
  one slide per module + stage-by-stage audit + disclaimer + quick-reference.
- **≥ half the slides are visuals** — editable shape-charts (`ebar`/`finding2`) and editable
  diagrams (`diagrams.py`: `fbox`/`harrow`/`vdash`/`band`/`matgrid`/`chain`/`sigrow`). Never images.
- **≥ 2 both-domain data-chart slides**: a real Book6 distribution beside the partner-science
  reference (DSP for Signal: Poisson Fano=1, white-noise vs AR(1) autocorrelation, 1/f spectra;
  genomics for Biology: 4 bases/64 codons/20 AA, codon-usage bias, per-base conditional entropy).
  Partner numbers are mainstream and shown in round form, clearly labelled as reference.
- **Audit slide** rates the analogy stage by stage (✓ Supported · ✗ Breaks · ~ Silent) and a
  **disclaimer slide** states "not a scientific miracle / not evidence."
- Build via the shared engine `_handson_build/build_lecture_slides.py` is deprecated for these;
  use a per-deck `build/build_deck.py` that inlines the bank values and the chart/diagram calls.
- Verify per batch: assert slide count ≥20 and visual-slide ratio ≥0.5 programmatically, `a:cs`
  sweep on Arabic runs, PDF render eyeball.

## 17. SPECIAL TOPICS — full-deck standard (LOCKED 2026-06-03)
Every `SpecialTopics/SpecialTopic_*.pptx` is upgraded from the old 4-slide micro-format to a full
deck, same bar as §16a companion decks:
- **≥ 20 slides**, deep-dive and comprehensive; **no fluff/filler slide** — every slide carries
  content (data, verse, diagram, or audit), never a spacer.
- **≥ 50% of slides are visuals** — dense editable shape-charts and/or embedded reproducible
  data-figures (matplotlib from Book6, §12a). At least 2 dense data-figures per deck.
- **Every Qur'an number/verse computed or quoted from Book6 by address;** concepts use sense-verified
  surface forms (§14a). Honest framing: present, audited ✓/✗/~, never adjudicate theology.
- **Each deck ships with a Quiz + Answer Key** (.docx): ~10–13 questions, rotated A–D answer
  positions, one-line explanations, every value reproducible from Book6.
- Verify per deck: ≥20 slides, ≥50% visual, cs-clean Arabic, render-eyeball, key A–D balanced.

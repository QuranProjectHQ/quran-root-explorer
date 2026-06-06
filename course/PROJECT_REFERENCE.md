# RootCourse — Master Build Reference (LIVING)

_Single re-loadable operating manual. If a fresh session reads only this + `COURSE_STANDARDS.md`, it can continue the course consistently. Update this at the end of every week. Last updated: 2026-05-30 (COURSE COMPLETE & FINALIZED — all 10 weeks finalized/signed-off. Final end-to-end audit passed: 102 docx with 0 missing Arabic w:cs; 10 valid 15-slide decks; 0 Arabic figure-titles; every week self-contained (build scripts, data bank, decision doc, figures); all values reproducible from Book6. Finalization pass on Wks 6–10 confirmed 8 modules × 8 beats each, full deliverable sets, scope discipline, and headline-value consistency. Fixes this session: rebuilt 3 corrupted decks (wk5/6/9), fixed wk9 sea/land suptitle + wk2 stale figure titles to English-only, reconstructed a truncated SYLLABUS tail.)._

---

## 1. Mission & context
Build a 10-week, flipped, data-driven course that teaches members to investigate the Qur'an's ~1,700 triliteral roots across 6,236 ayahs using the *Quran Root Explorer* app (https://quranproject-quran-root-explorer.hf.space/), and to read the measurements honestly. Course thesis (the spine): **separate computed fact from labeled interpretation, and CONTROL before you conclude.** Every week produces a finding, an understanding, and a *labeled* interpretation; several weeks require unlearning a folk assumption the corpus disagrees with.

Single source of all numbers: **Book6.xlsx** (the corpus) — and `engine.py` when the app modules are available. Never assert a value not computed from Book6.

## 2. The locked PROCESS (this prevented ~5× rework)
**spec → approve → build once → verify once.** For each week, in order:
1. **Test concepts against Book6 first** — find the real finding / "unlearn" before writing anything.
2. **Write a decision doc** `weekNN/WEEKNN_DECISION.md` (scope · outline · measures · banks · figures · screenshots) and get explicit sign-off.
3. **Build the lecture notes first** (the master), verify, then generate dependents.
4. **Verify once per batch** (not ad hoc).
Never build breadth before one component is validated. Reading an output-format skill before research is done is a mistake.

## 3. Per-week deliverable spec (locked depth, from Week 3 on)
- **Lecture notes:** ~3,500 words, **8 modules**, each carrying the **8 beats** (what it is · why · how · what we get · why it matters · in the data · takeaway · bridge). Use analogies. No fluff/filler — every sentence earns its place. Beat 6 ("in the data") mandatory.
- **Deck:** **15 slides**, body **18–20pt** / titles **30pt**; **8–12 substantive bullets per content slide** (2× density); use analogies; **fill the slide vertically** (efficient use of space — no large empty bottom); figure slides pair the image with packed bullets; no fluff.
- **Figures:** **8**, English-only titles, shaped Arabic on axes/data only.
- Plus: instructor script (~1,300–1,700 spoken words), worked example, app guide, exercise + answer key, quiz (14 Q) + key, quick reference, further study, **Excel data bank**.
- **Self-contained** in `weekNN/`: deliverables + data bank (JSON + xlsx) + `figs/` + `build/` (scripts + `figcommon.py` + `BUILD_README.md`) + decision doc. Shared assets (Book6, engine, syllabus, standards) stay at root, referenced not duplicated (`COURSE_STANDARDS.md` §9c).
- New themed **root set each week**, distinct from prior weeks; reuse the 12-member assignment-bank pattern.

## 4. Data methods (compute from Book6.xlsx)
Columns (0-indexed; data starts row index 8): 5=surah#, 6=ayah#, 7=surah name, **8=roots (space-sep)**, **9=word-forms (aligned 1:1 to col 8)**, 10=tokenized text, 12=revelation order.
- **Persian letterform gotcha:** corpus uses ی/ک; normalize with `norm()` (ی→ي, ک→ك, hamza variants→ء) before matching. Forms (col 9) similarly need ی→ي, ک→ك for display.
- **Frequency:** doc-freq = ayahs containing root; term-freq = token count. **Size-true rate = per 1,000 ROOT-TOKENS** (term-freq ÷ ~51,024). Never normalize by ayah/surah COUNT — containers vary in size (`NORMALIZATION_STANDARD.md`).
- **Distribution:** breadth = #surahs; Gini/top-3 of per-surah counts; **home surah = root-tokens-in-surah ÷ surah total root-tokens × 1000**; support floor = count ≥ 3 AND surah ≥ 30 root-tokens.
- **Forms:** align col 8 ↔ col 9; tally surface forms; group by pattern family (verb/participle/masdar/intensive).
- **Co-occurrence:** joint(A,B)=ayahs with both; expected=freq(A)·freq(B)/N; ratio=joint/expected ("× over chance"); length-controlled z available. Min joint ≥ 5 to report.

## 5. Build toolchain (reuse, don't reinvent)
- **`figcommon.py`** — `ar()` = arabic_reshaper + python-bidi (shaped, RTL); DejaVu Sans; colors (NAVY 1E2761, TEAL 0E9D8C, RED A23B3B, AMBER B8860B, GREY); full 114 `SUR` Arabic surah-name map; `load()` reads Book6 (auto-locates).
- **docx:** python-docx; set `w:cs` font on **every** run (font-on-every-run); page-number footer; build via **bash heredoc** (Edit/Write truncate Arabic/XML in this workspace).
- **pptx:** build **fresh** with python-pptx (editing existing pptx XML truncates); cs typeface on every run; left accent bar; Georgia titles / Calibri body.
- **xlsx:** openpyxl; Arial; bold header fill; freeze header; computed values are facts (no formulas needed) — note "computed from Book6."
- **Verify renders:** LibreOffice → PDF → pdftoppm → **view the JPG** (LibreOffice render is NOT proof of Word's `w:cs`, but it IS how we catch figure/layout/bidi issues).

## 6. Standards digest (full text in COURSE_STANDARDS.md)
1 process · 2 8-beat skeleton · 3 per-1,000-root-tokens normalization · 4 no scope leak (later-week terms only as bridge/preview) · 5 Book6 sole numbers · 6 Arabic `w:cs` every run + cs-sweep · 7 heredoc for Arabic files · 8 decks fresh in python-pptx · **9 figures: actual shaped Arabic, never transliteration-only/isolated** · **9b: English-only figure titles; no Arabic-word+number lists in prose (bidi scramble); horizontal-bar labels aligned to bars** · **9c: each week self-contained** · 10 verify-once-per-batch · 11 app-faithful figures from Book6 if browser denied.

## 7. Pitfalls & fixes (hard-won)
| Pitfall | Fix |
|---|---|
| Built before locking scope/normalization → 5× rework | decision-doc + sign-off first |
| Ayah-count normalization (ayahs vary in size) | per-1,000 ROOT-TOKENS at every level |
| Arabic broke in real Word (LibreOffice hid it) | `w:cs` on every run + cs-sweep |
| Edit/Write truncated Arabic & corrupted pptx XML | bash heredoc / python; rebuild decks fresh |
| Matplotlib Arabic isolated/reversed; or transliteration-only | `ar()` reshape+bidi; actual Arabic on axes |
| Arabic embedded in figure TITLE scrambled (e.g. فعيل/فعّال) | English-only titles; Arabic only as isolated axis labels |
| Horizontal-bar value labels reversed (vals[::-1]) | align labels to bar y-order; view the PNG |
| Arabic-word+number lists in prose scrambled | numbers live in figures/tables; prose Arabic = isolated words |
| Const drift (51,024 vs 51,044 tokens) | conform to engine value across all docs |

## 8. Course map & accumulated findings (the "unlearns")
| Wk | Concept | Worked root | The finding / unlearn | Status |
|----|---------|-------------|------------------------|--------|
| 1 | Frequency | ظلم | ظلم named ~12× عدل — corpus names the violation over the ideal; + per-1k-roots is size-true (ظلم↔هدي flip) | ✅ final |
| 2 | Distribution & concentration | ظلم/صبر | Length confound: raw busiest surah = al-Baqara for 30/50 top roots → 0/50 once size-true (per root-tokens); ص بر home: al-Baqara→al-Kahf→at-Tur | ✅ final |
| 3 | Partners & forms | ءمن | Faith is 61% a VERB (an act), not the noun إيمان; Divine Names = intensive pattern; polysemy ك-ث-ر → كوثر (praise) vs تكاثر (blame); antonyms are partners (ءمن↔كفر) | ✅ final |
| 4 | Co-occurrence | صلو | Frequency confound: raw says قوم/God; controlled, it is زكو (×34.6) — prayer & charity (half of zakat ayahs sit with prayer) | ✅ final |
| 5 | Lift & tiers | صلو↔زكو | Rigour: length-aware null + Monte-Carlo p + tiers. UNLEARN: a big shared count is not a bond — قول↔شيء (113 shared) is spurious; صلو↔زكو (28) is structural | ✅ final |
| 6 | Asymmetry & networks | عدن→جنن | Direction: P(garden\|Eden)=100% but P(Eden\|garden)=6% — the specific implies the general; network hub صلح (degree 5) | ✅ final |
| 7 | Motifs (intro) | شمس·قمر·نجم | 3-root motif vs length-aware triple-null. UNLEARN 1: count ranks backwards — sky·earth·between (34×→6.5×) weaker than sun·moon·star (3×→3,721×). UNLEARN 2: a motif ≠ its pairs — open triangle جبل·موه·شجر (strong pairs, trio=0) | ✅ final |
| 8 | Motifs & significance | رسل·بشر·نذر | Significance vs SUPPORT + stability (jackknife) + multiple testing. UNLEARN: a higher lift is NOT stronger — نبء·تلو·حقق (22×, 2 verses) collapses on leave-one-out; رسل·بشر·نذر (25×, 11 verses) is robust. ~817M triples → ~817k false "structural" at p<0.001 | ✅ final |
| 9 | Interpretation discipline | الدنيا/الآخرة | Audit a reading: Supported / Contradicted / Underdetermined. UNLEARN: a true number can be a false claim — "الدنيا=الآخرة=115" is form-true (115=115) but root-false (133 vs 250, cherry-picked unit). Supported: حيي↔موت 17×; underdetermined: شكر/كفر 1.4×. Failure-mode map ties every prior week to a bad-reading it catches | ✅ final |
| 10 | Capstone | غفر | Full pipeline end-to-end on one unseen root: غفر (forgiveness) — 202 ayahs; home Sūrat Nūḥ; dominant form غفور = intensive Divine Name; cluster sin/repentance/mercy; sin→forgiveness 51% vs 9%; غفر·توب·رحم robust (55×,18v) vs غفر·ذنب·توب fragile; audit "always with mercy?"=45% (assoc, not "always"). SYNTHESIS: no single number is a portrait, only the pipeline is. + capstone assignment + rubric (12-root member bank) | ✅ final |

## 9. Critical-review discipline (always on)
Each week, ask: (a) is the finding *discovered from data*, not template-filled? (b) is this week's control a *new* confound, not a rerun? (c) does the escalation genuinely sharpen the prior week? (d) every figure earns its place with a finding, or it's cut. (e) flag any deliberately-rough method as scaffolding the next week sharpens.

## 10. Status (course complete & finalized)
All ten weeks finalized and signed off (2026-05-30). Final end-to-end audit passed: 102 docx, 0 missing Arabic w:cs; 10 valid 15-slide decks; 0 Arabic figure-titles; every week self-contained (build/ + data bank + decision doc + figures); all values reproducible from Book6.

**Workspace caution (this environment):** in-place rewrites of Arabic-heavy `.md` files via `sed -i` or a single very large `Edit` can truncate the file at an ~8–16 KB boundary (hit twice: SYLLABUS.md, PROJECT_REFERENCE.md). Prefer Python read-modify-write, or small targeted `Edit` calls, for these files; re-check byte length after editing.

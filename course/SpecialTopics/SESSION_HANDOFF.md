# Session Handoff — Special Topics (read me first next session)

_Last updated: end of this session. Everything below is current and verified._

## 1. Status — DONE

All **27 Special Topics** are complete, each with a full 5-piece kit:
**deck (.pptx) + quiz (.docx) + answer key (.docx) + instructor script (.docx) + App & Plot Guide (.docx)**.

- 25 W-series: `W01_bashir_nadhir`, `W01_who_addressed`, `W02_mushaf_vs_revelation`, `W02_surah_ayah_units`,
  `W03_act_vs_state`, `W03_din_islam_quran`, `W03_mukhlis`, `W04_light_darkness`, `W04_wealth_children`,
  `W05_name_pairs_lift`, `W06_darkness_to_light`, `W07_local_regional_global`, `W07_signs_nature_scripture`,
  `W08_hypocrite_syndrome`, `W09_equity_economic`, `W09_equity_inheritance`, `W09_equity_judicial`,
  `W09_equity_social`, `W09_istinsakh_genomics`, `W09_naskh_abrogation`, `W09_shafaa_intercession`,
  `W09_sword_or_peace`, `W10_divine_names`, `W10_ghaffar_vs_tawwab`, `W10_ghafr_forms`.
- 2 earlier: `Hapax_OnceOnly`, `Quran_Challenges`.

Every deck: **20 slides, 7 embedded Book6 figures + diagrams (>=50% visual), 0 missing cs=Arial fonts**.
Every quiz: 13 questions, answers rotated A/B/C/D, with a separate answer key.
Files live in `RootCourse/SpecialTopics/` (filenames: `SpecialTopic_<slug>_<Deck|Quiz|Quiz_Answer_Key|Instructor_Script|App_and_Plot_Guide>`).
Plus a series-overview `SpecialTopics_App_and_Plot_Guide.docx`.

Verification was done with the auditor in `wbuild/wbase.py:verify()` and a LibreOffice render-and-eyeball pass over the W-decks (no overflow/voids; captions auto-fit).

## 2. Build system (everything regenerates from Book6)

Working dir: `RootCourse/SpecialTopics/wbuild/`
- `wk.py` — **the kernel.** Loads `RootCourse/Book6.xlsx`, normalizes (Persian->Arabic letter folding),
  exposes `ac(root)`, `cooccur(a,b)`, `lift(a,b)`, `tokfreq`, surface-form helpers, and matplotlib figure
  builders (`fig_freqbarh/groupbar/suradist/timeline/liftscatter/donut`). Figures -> `SpecialTopics/figs_w/`. Fixed seed=7.
- `wbase.py` — `standard_deck(spec)` builds the locked 20-slide template; `build_quiz(...)`; `verify(path)`;
  the shared `st_slides`/`diagrams` colour + layout constants. Imports `st_slides.py` + `diagrams.py` (copied here).
- `build_b1*.py … build_b3*.py` — the per-batch deck builders (each defines `spec` dicts + computes figures live).
- `build_scripts.py` — generates instructor scripts by reading each deck (`make_script(pptx)`).
- `build_guides_each.py` — generates the **per-lecture** App & Plot Guides from each deck.
- `build_guide.py` — the combined series-overview guide.
- `append_sshot_section.py` — appends the Special Topics table to `RootCourse/SCREENSHOT_CAPTURE_GUIDE.md`.
- `hapax_build/` — the Hapax + Challenges builders (`build_hapax.py`, `build_challenges.py`, `gen_figs_chal.py`, `build_quiz_*.py`). Note: build_challenges.py uses module-level Arabic string constants `A_*`.

To rebuild a deck: `cd wbuild && python3 build_b<N>.py`. To rebuild all figures: the build scripts call `wk` inline.

## 3. Data discipline (non-negotiable — the user cares deeply about this)

- **No fabrication.** Every number a figure shows is recomputed live from Book6. Where a documented legacy
  number couldn't be cleanly reproduced (hand-tagged senses), I computed a defensible quantity and labelled it
  precisely rather than carry an unverified figure.
- **§14a surface-form rule:** a concept = its sense-bearing surface forms, NOT the raw root, when the root is
  polysemous. E.g. light counts surface `نور` (noun, ~36 ayat) NOT root نور (174, includes fire نار);
  sword topic sense-filters قتل (killing) vs قاتل/قتال (combat); mukhlis splits by company not voice.
- **Honest spine:** decks PRESENT structure; the theological reading is labelled and never adjudicated.
- Standards are locked in `RootCourse/COURSE_STANDARDS.md`: §12a (reproducible data-figures as images),
  §14a (concept = sense-verified surface forms), §16a (companion decks >=20 slides, >=half visual),
  §17 (Special Topics full standard: 20+ slides, quiz+key).

## 4. Verified key numbers (reproduce exactly — sanity anchors)

name-pair lifts 3.2/9.0/13.8/13.9x · naskh root = 4 occurrences · shafaa = 26 · literal "sword" = 0 ·
mushaf<->revelation corr = -0.41, position<->length = -0.75 · hypocrite trio = 3 verses · signs-root = 353 ·
mal/awlad 80/80 shared 16 · "light always singular / darkness always plural" with 0 exceptions ·
din+islam shared 7, din/islam+Qur'an = 0 · ghafr+rahma 91, +sin 19, +garden 9.

## 5. GOTCHAS (cost me time — avoid next session)

- **The Write tool truncates Arabic-heavy Python files** (~8KB cutoff mid-multibyte). Write/edit Arabic-heavy
  build files via `bash` heredoc (`cat > f <<'PYEOF' … PYEOF`), NOT the Write tool.
- **bash `-c "…"` command-substitutes backticks** inside your string. When writing markdown with backticks via
  python, use a **`.py` file** (Write tool is fine for ASCII) then run it — don't inline backtick-markdown in `python3 -c "…"`.
- Figure colour args must be **wk.py hex** (e.g. `wk.TEAL`), not the pptx `RGBColor` from wbase — they're different objects.
- Proper-name roots in Book6 are abjad-style: Moses = `وسي` (136), Pharaoh = `فرعن` (74), Abraham = `برهم` (69),
  mankind = `ءنس` (342), Jesus = `عسي`. Don't search `موسي` (=0).
- Vocatives in the tokenized column appear as `يا اي ها ال <group>` (split, Persian letters); normalize first.
- docx cs-font is the `w:cs` **attribute** on rFonts (set via `setcs`), NOT a `<cs>` child — verify with the
  wordprocessingml namespace, not drawingml (a pptx-namespace check gives false "missing").

## 6. OPEN / OPTIONAL (next session candidates)

- **Screenshots:** none captured yet — they're a to-do. `RootCourse/SCREENSHOT_CAPTURE_GUIDE.md` now has a
  SPECIAL TOPICS (27) table (headline figure + first verse + suggested `SpecialTopics/shots/<slug>/` folder).
  User was asked whether to create the 27 empty `shots/<slug>/` folders — **awaiting answer.**
- Optional: extend the verbatim verse galleries (some topics have few snippet verses in `build/snip_*.json`).
- Sense-charts (polysemy %) remain **out of scope** — the induction method failed face-validity
  (see `_sense_mine/SENSE_INDUCTION_SPEC.md`); do NOT revive without an external sense-annotated lexicon.

## 7. App (separate from course material)

The Quran Root Explorer app is in `Downloads/Quran_Root_Explorer_Web_v1.2/`, v1.3 live on Hugging Face
(`quranproject-quran-root-explorer.hf.space`). Pages in `state.py:NAV_SECTIONS`. The Signal FFT-caption fix
is already deployed (commit 931fea2). **Course material does NOT get deployed** — only the app does, via
`deploy_git.py` / `.\deploy.bat` (PowerShell). Nothing app-side is pending.

# week02 — build provenance

Run from the repo root (RootCourse). The shared corpus `Book6.xlsx` and standards live at the root; figcommon.py locates Book6 automatically.

Order:
1. `python3 week02/build/gen_figs.py`            → regenerates figures into `week02/figs/` (Week 2: into `week02/` + `week02/shots/`)
2. `python3 week02/build/build_data_bank_xlsx.py` → rebuilds `Week02_Data_Bank.xlsx` from the JSON banks
3. `python3 week02/build/build_notes.py`         → rebuilds the lecture notes
4. (Week 2) build_worked_exercise.py, build_quiz_quickref_further.py, build_appguide.py, build_deck.py, build_script.py

Standards: English-only figure titles; Arabic only as isolated shaped axis/data labels; per-1,000-root-tokens normalization; w:cs on every Arabic run. See ../../COURSE_STANDARDS.md.

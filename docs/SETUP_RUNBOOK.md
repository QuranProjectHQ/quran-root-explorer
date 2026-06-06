# SETUP RUNBOOK — publishing the project, start to finish

*The complete, ordered sequence of steps to take the project from local folders to a public,
self-contained, secured GitHub home with a free live app. ✅ = done, ▶ = current, ☐ = remaining.
Kept for reference and succession (see SUCCESSION.md). Last updated 2026-06-06.*

---

## Part A — GitHub foundation
1. ✅ **Create a GitHub account** (owner login) — username `Ayoub-Torkian`, email `torkiangm2@gmail.com`. (github.com/signup)
2. ✅ **Create a free Organization** — `QuranProjectHQ` (the self-contained, public home). (github.com/account/organizations/new)
3. ✅ **Transfer the repo into the org** — moved `Ayoub-Torkian/QuranProject` → `QuranProjectHQ` (lossless; from repo Settings → Danger Zone → Transfer).
4. ✅ **Rename the repo** to `quran-root-explorer` → home is `github.com/QuranProjectHQ/quran-root-explorer` (Settings → General → Repository name).
5. ✅ **Turn on security** (Settings → Code security & analysis): Dependency graph, Dependabot alerts, Secret scanning + Push protection, CodeQL code scanning, Private vulnerability reporting.
6. ✅ **Branch protection** ruleset `protect-main` (Settings → Rules): target `main`, Restrict deletions + Block force pushes. (Require-pull-request left off until a co-maintainer is added.)
7. ✅ **Clone to your computer** with GitHub Desktop → landed at `…\OneDrive\Documents\GitHub\quran-root-explorer` (this is now your **canonical local working copy**).
8. ✅ **Copy the organized project into the clone** (app, research, data, course, docs, license/governance files) — done for you.
9. ✅ **Commit + Push** (1762 files) → the project is **live and public**.

## Part B — Live app on free hosting (Streamlit Community Cloud)
10. ✅ **Sign in to Streamlit Community Cloud** (share.streamlit.io) with GitHub; authorized access to the `QuranProjectHQ` org.
11. ✅ **Create the app** pointing at `QuranProjectHQ/quran-root-explorer`, branch `main`, main file `app/app.py` (use share.streamlit.io/deploy, *not* a template).
12. ✅ **Fixed truncated files** — 6 app files (`app.py`, `state.py`, 4 pages) were silently truncated in the old working folder; recovered complete versions from the Hugging Face git history, verified they compile, kept the `../data` patch.
13. ▶ **Commit + Push the fixes** → Streamlit auto-redeploys → app starts. *(You are here.)*
14. ☐ **Confirm the app runs**; if PDF/PNG *export* errors on Chromium, add a one-line `app/packages.txt` containing `chromium` and re-push (one-time fix).
15. ☐ **(Optional) add app secrets** in Streamlit (Settings → Secrets): `ADMIN_PASSWORD`, `HF_TOKEN`, etc. — only needed to enable the analytics mirror and the password-protected Usage page. The app runs fine without them.

## Part C — Remaining project steps
16. ☐ **Back up via Google Drive for Desktop** — set it to *Mirror* the canonical clone (see `docs/BACKUP_AND_SYNC.md`). Keeps an organized, always-current Drive copy automatically.
17. ☐ **Merge the Google Drive material** — the foundational PDF + 10 research articles into `research/papers/` (plan in `docs/DRIVE_CATALOG.md`), then Drive can be retired.
18. ☐ **Reconstruct 5 truncated research/course scripts** (`iltifat_tagger`, `intratext_lock`, `intratext_variation`, `wavelet_prelim`, a course figure-builder) — not in the HF backup, so rebuild or flag.
19. ☐ **Add a co-owner to the organization** (Org → People → invite → role Owner) — the key succession safety net (see `SUCCESSION.md`).
20. ☐ **Retire the `Downloads\QuranProject` staging folder** (it did its job) so there's only one place you edit — the clone.
21. ☐ **Continue the research** from the next-candidates list (network-first muqaṭṭaʿāt/rasm thread), landing findings in `research/`.
22. ☐ **Later: retire Hugging Face** once the GitHub→Streamlit app is proven stable (then revoke the HF token). Until then, dual-maintain both.

## The standing rule
Edit in **one place only** — the canonical clone. Everything else (GitHub, Drive, USB) only *receives*. Commit + push at the end of each session; that is your backup.

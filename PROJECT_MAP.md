# PROJECT MAP — everything, A to Z

*The single front door to the whole project: what exists, where it lives, and where to start. If you
read one file first, read this. (For continuity if anything happens to the founder, see `SUCCESSION.md`.)*

*Updated 2026-06-06.*

---

## 1. What this project is
A free, open, public-domain study of the structure of the Qur'an — an **interactive app** to read and
probe it, and a **research record** of what is and isn't measurably distinctive, reported honestly
(statistic + null + comparator, no overclaiming). Mission & spirit: `VISION.md`.

## 2. Where everything lives (the three homes)
| Home | Holds | Link |
|---|---|---|
| **GitHub repo** (source of truth) | Code, research write-ups, docs, index | https://github.com/QuranProjectHQ/quran-root-explorer |
| **Live app** (free hosting) | The running application | https://quranprojecthq-quran-root-explorer-appapp-dlobjl.streamlit.app/ |
| **Live app (mirror)** | Same app on Hugging Face (during transition) | Space `QuranProjectHQ/quran-root-explorer` |
| **Google Drive archive** (~3 GB) | Academic papers + source datasets (too big for Git) | https://drive.google.com/drive/folders/1Iz34p_uD7tAL7To8HaVGPFoCJYpp3fPc |
| **Local working copy** | Your editable clone (the one place you edit) | `…\OneDrive\Documents\GitHub\quran-root-explorer` |

## 3. Repository layout
```
quran-root-explorer/
├── README.md              ← start here (overview + live-app link)
├── PROJECT_MAP.md         ← this file (the A-to-Z index)
├── VISION.md              ← mission, the "oneness" spirit
├── SUCCESSION.md          ← how anyone can continue the project
├── LICENSE · NOTICE       ← CC0 / public domain + scope
├── SOURCES.md             ← credit for every third-party input
├── CONTRIBUTING.md · SECURITY.md · CODE_OF_CONDUCT.md  ← how to take part, safely
│
├── app/                   ← the application (deploys live) — entry: app/app.py
│   ├── pages/             ← the ~25 app pages
│   └── README.md          ← run-it-locally notes
├── research/
│   ├── papers/            ← write-ups + ARCHIVE_INDEX.md (links to the Drive papers)
│   ├── findings/          ← FINDINGS_SYNTHESIS, EVIDENCE, results (the verdicts)
│   ├── method/            ← DESIGN_STANCE, DESIGN_OF_EXPERIMENTS, etc. (the locked rules)
│   ├── handoffs/          ← HANDOFF_MASTERY (research "start here") + roadmaps
│   ├── experiments/       ← the analysis scripts (incl. sequence_tests/)
│   └── coverage/          ← COVERAGE_MAP.html
├── data/                  ← reference datasets the app uses (Book6.xlsx, etc.)
├── course/                ← the teaching course (syllabus, weekly lectures, figures)
├── docs/                  ← plans & runbooks (see §4)
└── deploy/                ← deploy scripts (no secrets)
```

## 4. Document index (where to look for what)
- **Get oriented:** `README.md` → this `PROJECT_MAP.md` → `VISION.md`
- **Continue/inherit the project:** `SUCCESSION.md`
- **The plan & how it was built:** `docs/PROJECT_ORGANIZATION_PLAN.md`, `docs/SETUP_RUNBOOK.md`
- **Backups & syncing:** `docs/BACKUP_AND_SYNC.md`
- **The Drive archive (papers + data):** `research/papers/ARCHIVE_INDEX.md`, `docs/DRIVE_CATALOG.md`
- **The research itself:** `research/findings/FINDINGS_SYNTHESIS.md` (digest), `research/handoffs/HANDOFF_MASTERY.md` (what's next)
- **Credits & licensing:** `SOURCES.md`, `NOTICE`, `LICENSE`
- **Contributing & safety:** `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`

## 5. The research ↔ app ↔ papers connection
The ~18 academic papers in the Drive archive are the formal write-ups of the same investigations the
app lets you explore interactively and the `research/` folder records as findings. The mapping is in
`research/papers/ARCHIVE_INDEX.md` (each paper → its app page).

## 6. Status (as of 2026-06-06)
**Done:** public org repo · organized into the layout above · security (secret/push/CodeQL/Dependabot) ·
branch-protected · CC0 license + credits + vision + succession · live app on Streamlit (free) + HF mirror ·
truncated app files recovered · Drive archive catalogued and indexed.

**Pending (tracked):**
- Physical de-duplication of the Drive archive (same papers appear in multiple Drive sub-folders) and
  cleanup of leftover local folders — *deferred:* needs the sandbox (currently out of scratch space) or
  manual tidying; the **organization/index is complete**, the physical move is the remainder.
- Make the Drive folder public ("Anyone with link → Viewer").
- Rebuild 5 truncated research scripts (`research/experiments/…`).
- Merge selected small final-PDFs into the repo if desired (data stays in Drive).
- Add an org co-owner (succession) · install Drive-for-Desktop backup · retire HF when stable.
- Continue the research (next candidates in `research/handoffs/HANDOFF_MASTERY.md`).

## 7. The one rule
Edit in **one place only** — the local clone. Everything else (GitHub, Drive, USB) only *receives*.
Commit + push at the end of each session; that is your backup.

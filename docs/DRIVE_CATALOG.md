# GOOGLE DRIVE CATALOG — what's in the Drive folder, and the merge plan

*Snapshot of the shared Drive folder
(`https://drive.google.com/drive/folders/1Iz34p_uD7tAL7To8HaVGPFoCJYpp3fPc`) so nothing is lost
before Drive is retired. Cataloged 2026-06-06. Owner: torkiangm@gmail.com. Status of each item:
**MERGE** (unique, bring into repo) · **CHECK** (inspect before deciding) · **DUP** (already in repo).*

---

## Top level
| Item | Type | Status | Proposed repo destination |
|---|---|---|---|
| `QuranMiningFinalComplete.pdf` (34 MB) | PDF book/thesis (Persian) — foundational data-mining work across surah/ayah/word/letter scales, muqaṭṭaʿāt, bioinformatics | **MERGE** | `research/papers/` (or a `research/foundational/` subfolder) |
| `مقالات` (Articles) | Folder | **MERGE** (see below) | `research/papers/articles/` |
| `Presentation July 2025` | Folder | **CHECK** — returned empty via API; verify in the Drive UI | `course/` or `docs/presentations/` if it has content |

## مقالات → مستندات و داده‌های پشتیبان (Articles → Documentation & supporting data)
Ten dated research articles (Iranian calendar; ≈ Gregorian in parentheses). Each is its own folder,
likely containing a manuscript plus supporting data/figures — **each needs individual cataloging at
merge time.** All status **MERGE** → `research/papers/articles/<slug>/`.

| # | Title (Persian) | Topic (English) | Date ≈ |
|---|---|---|---|
| 1 | مقاله تحلیل فضایی مرداد ۱۴۰۴ | Spatial analysis | Aug 2025 |
| 2 | مقاله مکی مدنی تیر ۱۴۰۴ | Meccan vs. Medinan | Jul 2025 |
| 3 | مقاله روش‌شناسی تعبیه بافتار در تحلیل مفاهیم خرداد ۱۴۰۴ | Methodology: context-embedding in concept analysis | Jun 2025 |
| 4 | مقاله مشابهت یابی گراف اردیبهشت ۱۴۰۴ | Graph similarity-finding | May 2025 |
| 5 | مقاله بررسی تطبیقی فروردین ۱۴۰۴ | Comparative study | Mar–Apr 2025 |
| 6 | مقاله شبیه سازی روند نزول داده های قرآنی اسفند ۱۴۰۳ | Simulating the revelation sequence of Qur'anic data | Feb–Mar 2025 |
| 7 | مقاله مکان نگاری | Location/spatial mapping | 2025 |
| 8 | مقاله خطاب‌های قرآن - انسان | The Qur'an's address to humankind | Dec 2024 |
| 9 | مقاله دنیا و آخرت | This world and the hereafter | Dec 2024 |
| 10 | مقاله شماره آیه مفاهیم | Ayah-number / concepts | Nov 2024 |

## Merge procedure (when we run it)
1. Recurse into each article folder; list every file (manuscript, data, figures) with size/type.
2. Compare against what's already in the repo (`research/`, `data/`) — flag any **DUP**.
3. For unique items, copy into `research/papers/articles/<dated-slug>/`, keeping the date in the name.
4. Note the language (these are Persian) so the repo README can point readers to them appropriately.
5. Re-verify counts (files in Drive == files merged + flagged) before Drive is retired.
6. Credit/provenance: confirm these are the owner's own work (assumed yes) and record in `SOURCES.md`.

## Retirement gate
Drive is **not** retired until: every item above is either merged or consciously dropped, the counts
reconcile, and the result has been pushed to GitHub and mirrored. Even then, keep Drive as a cold
archive for a grace period (see `BACKUP_AND_SYNC.md`).

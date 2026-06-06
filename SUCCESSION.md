# SUCCESSION & CONTINUITY — so the project never stops

*Purpose: if the founder becomes unavailable for any reason, anyone trusted can pick this up and
continue without confusion or pause. This is the "will" of the project. It is kept **up to date at
all times** — every structural change updates this file. It contains **no passwords** (those travel
by a secure channel, see §6); it is safe to share publicly.*

*Last updated: 2026-06-06.*

---

## 1. What this project is (for someone arriving cold)
A free, open, public-domain study of the structure of the Qur'an, in two halves: an **interactive
app** (read the text and test ideas about its structure) and a **research record** (what has and has
*not* been found, with honest statistics and nulls — never overclaiming). It is meant as a gift to
all of humanity: free to use, free to copy, free to build upon. Read, in order: this file → `README.md`
→ `VISION.md` → `docs/PROJECT_ORGANIZATION_PLAN.md` → `research/handoffs/HANDOFF_MASTERY.md`.

## 2. Where everything lives (the whole map)
- **Canonical home:** the public GitHub repository (organization: *to be created* — `QuranProject`).
  This is the single source of truth: app, research, data, course, docs.
- **Local mirror:** a clone of that repo on the founder's computer
  (`Downloads/QuranProject/quran-root-explorer`). Identical to GitHub; kept in sync with Git.
- **Live app (current):** Hugging Face Space `QuranProject/quran-root-explorer` (kept running during
  transition).
- **Live app (target):** Streamlit Community Cloud, deploying directly from the GitHub repo (free).
- **Course material:** `course/` (originated in the `RootCourse` folder).
- **Supplementary archive:** a Google Drive folder being folded into the repo (see the merge plan).

## 3. How to take over — step by step
1. **Get access** to the GitHub organization (you should already be an Owner — see §5; if not, use the
   recovery path in §6).
2. **Clone the repo** with GitHub Desktop (Code → Open with GitHub Desktop) — that gives you the full
   project and its entire history on your machine.
3. **Read the orientation chain** in §1. The research state and "what to do next" always live in
   `research/handoffs/HANDOFF_MASTERY.md` (the "START HERE" block).
4. **Run the app locally:** open a terminal in `app/`, `pip install -r requirements.txt`, then
   `streamlit run app.py`. It loads the data from `../data/Book6.xlsx` automatically.
5. **Make changes the safe way:** edit in your clone, commit with a clear message, push. The live app
   redeploys automatically. Never commit secrets (the `.gitignore` blocks them).
6. **Keep the record honest:** when a finding changes, update the matching files in `research/` in the
   same commit — the discipline that keeps the project trustworthy (see `CONTRIBUTING.md`).

## 4. How to keep it alive (maintenance)
- Approve community pull requests only after review and passing automated checks (`SECURITY.md`).
- Keep the maintainer team small and trusted; never merge what you don't understand.
- Renew nothing costly — the whole stack is intentionally **free** (GitHub, Streamlit Cloud).
- Tag stable releases so the public app runs vetted versions.

## 5. The single most important continuity action — DO THIS FIRST
**Add at least one trusted co-owner to the GitHub organization now.** A project with one owner dies
if that owner is locked out. Two owners means it can always be recovered and continued. In GitHub:
Organization → People → invite the trusted person → set role **Owner**. This one step is the
difference between a project that survives and one that doesn't.

## 6. Credentials — handled securely, NOT written here
This file deliberately contains **no passwords or tokens.** To hand over access safely:
- Put account logins (GitHub, the project email, Hugging Face, Streamlit Cloud) in a **password
  manager** (e.g. Bitwarden, 1Password) and set up its **emergency-access / legacy** feature, naming
  your successor. They receive access automatically if you're unavailable.
- *Or* seal a printed credential sheet with a trusted person or lawyer.
- Because there are **two org owners** (§5), the successor can in most cases take over through GitHub's
  normal ownership without needing any password at all — that's the safety net.

## 7. What to send the successor, and when
**Now / at your earliest convenience (all safe, no secrets):**
- The GitHub repo link (everything is public and self-explanatory).
- This `SUCCESSION.md`, the `README.md`, and `VISION.md`.
- An invitation making them an **Owner** of the GitHub organization (§5).

**Set up now, delivered automatically only if needed:**
- Password-manager emergency access (§6) — so logins reach them without being exposed today.

**A short note to include:** "If I'm ever unavailable, you have everything you need in the GitHub
repository. Start with SUCCESSION.md. The project is free and public; please keep it that way and keep
it honest."

## 8. Keeping this current
This file is updated whenever the structure, hosting, owners, or where-things-live change. The founder
(and the assistant helping maintain the project) treat it as a living document, not a one-time note.

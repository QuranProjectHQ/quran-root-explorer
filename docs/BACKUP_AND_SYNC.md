# BACKUP & SYNC — keeping the project safe and in one place

*How the project's copies are organized so they protect each other instead of drifting apart. The
governing rule is simple and absolute: **edit in exactly ONE place; every other copy only receives.***

---

## The copies and their roles (3-2-1, exceeded on purpose)

| Copy | Role | How it updates | Edit here? |
|---|---|---|---|
| **Local computer drive** (`Downloads/QuranProject/…`) | The working copy / clone | You work here | ✅ ONLY here |
| **GitHub** (once the org exists) | Source of truth + off-site, versioned history | `git push` from local | ❌ push only |
| **Google Drive** | Second off-site cloud copy | Auto-sync from local (Drive for Desktop) | ❌ never |
| **USB / external SSD** | On-site snapshot on a different medium | Occasional manual copy | ❌ never |

This is 4 copies, 3 media, 2 off-site — stronger than the standard "3-2-1" rule (3 copies, 2 media,
1 off-site). The extra copies especially protect the material GitHub does **not** store (large
binaries, the 34 MB foundational PDF, datasets excluded from Git).

**The one rule that makes redundancy safe:** never edit directly in Drive, on the USB, or on GitHub's
web editor. Always edit in the local clone and let the change flow outward (push to GitHub, auto-sync
to Drive, periodic copy to USB). Editing in two places is how copies silently diverge — the exact
clutter problem this whole reorganization is fixing.

**During transition (before GitHub exists):** the local clone is the source of truth; Drive + USB are
its backups. **After GitHub is live:** GitHub becomes the source of truth and the local folder is its
clone. You may relax to three copies later, but keeping all four is fine.

---

## (A) Google Drive for Desktop — the right way to get an organized, always-current Drive copy

Do **not** hand-upload the folder through a connector — that creates a second copy that goes stale.
Instead, let Google Drive for Desktop mirror the local folder automatically:

1. Download **Google Drive for Desktop** from `https://www.google.com/drive/download/` and install it.
2. Sign in with your project Google account.
3. Open Drive for Desktop → **Preferences** (gear icon) → **Google Drive** tab.
4. Under **My Drive syncing options**, choose **"Mirror files"** (keeps a full copy both on your
   computer and in the cloud — best for backup).
5. Click **"Add folder"** and select `C:\Users\<you>\Downloads\QuranProject`.
6. Apply/Save. Drive now keeps an organized, complete, automatically up-to-date copy of the whole
   `QuranProject` folder in the cloud — including binaries — with zero manual effort.

Because you still edit only in the local folder, this obeys the one rule: Drive just mirrors.

*(Alternative if you prefer not to install anything: a one-time manual drag-drop upload of the folder
to Drive gives you a copy, but it will NOT stay current — you'd have to re-upload after every change.
Drive for Desktop is strongly preferred.)*

---

## (B) USB / external SSD snapshot — occasional, manual

A point-in-time copy on a physical drive protects against cloud-account problems and ransomware.
- Every so often (e.g., monthly, or before any big change), copy the whole `QuranProject` folder to
  the external drive. Label it with the date (e.g., `QuranProject_2026-06-06`).
- Keep the **two most recent** snapshots; delete older ones to avoid pile-up.
- This is the only copy that's fully manual — that's fine; it's your offline safety net.

---

## (C) GitHub — automatic off-site versioned backup (once live)
- `git push` after each working session. That single habit backs up everything tracked, with full
  history (you can recover any past state, not just the latest).
- Tag stable releases so you can always return to a known-good version.
- Remember: secrets and ignored files are **not** on GitHub by design — that's what (A) and (B) cover.

---

## Quick checklist
- [ ] Edit only in the local `QuranProject` folder.
- [ ] Drive for Desktop set to **Mirror** the folder (A).
- [ ] Occasional dated USB/SSD snapshot (B).
- [ ] `git push` each session once GitHub is live (C).
- [ ] Credentials in a password manager (never in any of these copies).

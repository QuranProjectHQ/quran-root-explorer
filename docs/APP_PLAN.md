# APP PLAN — the app is the MAIN INSTRUMENT (co-priority with research)

**Mandate (user):** the app is not a side-deliverable. It is the primary tool for users to
**(1) READ** the Qur'an, **(2) TEST** different ideas/lenses live, **(3) give FEEDBACK** on novel
ideas, and **(4) report BUGS**. Research findings only matter if users can read, probe, and
challenge them in the app. This file keeps app design explicitly in scope as research progresses.

## Principle: the app is an EVIDENCE INSTRUMENT, not a claims engine
Every lens shown in the app displays — always — its **statistic + null + equal-N + comparator +
gate verdict**. No "miracle" claims; honest nulls are shown as first-class results (most modalities
ARE null — that is the finding). This mirrors the locked methodology (`DESIGN_STANCE.md`).

## The organizing model (already agreed): MODALITY × SCALE, on a shared index
- **Scales** (how we read): 🧭 Position · 🔤 Sequence (char) · 🧩 Semantic (root/word). Shipped in v1.3.
- **Modalities** (what we test): the 12 lenses + the signal-geometry/positional-directional lenses.
- **Fusion unit = the āyah** (the "sign"): click one āyah/passage → see it read through every
  available lens at once, each with its null. This is the app's hero interaction.

## Four surfaces to build
1. **Reader** — read the Qur'an (exists in part via root explorer); make the āyah the clickable hero.
2. **Lens Lab** — one card per modality/idea. Each card: short claim, live run on a chosen
   passage/corpus, the statistic vs its null, equal-N + comparator, GATE verdict (pass/null), and a
   link to the EVIDENCE entry. Surfaces #42 (the one distinctive) prominently; shows the rest as
   honest nulls. Reuses `sequence_tests/*` detectors (each runs in ~2s).
3. **Feedback loop** — per-lens 👍/👎 + free-text note; a "propose a new lens/idea" form. Captured to
   a local store (e.g. `feedback/feedback.jsonl`) for us to review and turn into new modalities.
4. **Bug report** — a always-visible "report a bug" widget logging page + state + user note to
   `feedback/bugs.jsonl`.

## Phasing (realistic, incremental — NOT a stop-the-world overhaul)
- **v1.4 (next app release, incremental):**
  - Add **Feedback** + **Bug report** widgets (cheap, high value, unblocks user signal immediately).
  - Add a first **Lens Lab** page: render the 12 modality verdicts from EVIDENCE/COVERAGE as cards;
    make 2–3 fast lenses runnable live (recurrence #42, rhyme persistence, field-dynamics #46).
  - Embed/link `COVERAGE_MAP.html` as the "where we are" view.
  - Finish the shipped Two Books 🔜 items (alt-chronology robustness, spatial autocorrelation).
- **v2.0 (re-spine, scheduled, not yet):** reorganize nav around MODALITY × SCALE; the āyah-hero
  fusion view; every lens live and interactive. Two Books folds in as the three scales.

## How current research ideas map to app surfaces (keep this current)
- #42 intratextual recurrence (DISTINCTIVE) → Lens Lab flagship card + āyah-hero "where else does
  this passage recur" view.
- Signal-geometry / pointer (`IDEA_SIGNALS_GEOMETRY.md`) → Position-scale lenses; wavelet/locality
  demos (record: largely #33, no credit — show as an honest null demo).
- Positional/directional sub-unit lens → an āyah-internal visualizer (sub-unit spectrum char→root→
  morph; R→L default, reverse toggle).
- Masking/filtering toolkit → a "mask/filter" control on the āyah-hero view (include only Meccan /
  narrative / a field; project out a known axis) — makes the methodology tangible to users.

## Open decisions (ask the user when we start building)
- v1.4 scope: feedback+bug only first, or feedback+bug + first Lens Lab page together?
- Feedback storage: local file (private) vs a shared collector (multi-user)?
- Which 2–3 lenses to make live first in Lens Lab?

## Information architecture — the growing-nav problem (user-flagged, IN SCOPE, postponed to v2.0)
The flat nav list is long and getting longer (now ~25 pages + Feedback). This is the core reason the
re-spine is needed, NOT a cosmetic tweak. Target structure when we do it:
- **Top level = the three SCALES** (🧭 Position · 🔤 Sequence · 🧩 Semantic) — the categories we already
  have in Two Books — promoted to the app's primary axis.
- **Within each scale = the relevant MODALITIES/lenses**, each a card (claim · live run · null · gate).
- Collapse today's ~25 ad-hoc pages into this MODALITY × SCALE grid; Reader + Lens Lab + Feedback are
  cross-cutting, not more list items.
- Decision deferred deliberately: finalize the lens set first (research is still adding/retiring lenses),
  so the IA is designed once around the true, stable set rather than reorganized repeatedly.
DO NOT start the re-spine until the research sweep is at a stable stopping point. Until then, new pages
go into the existing groups (as Feedback did).

## Status
RECORDED as co-priority; IIA redesign POSTPONED to v2.0 by user decision (research first). v1.4 feedback +
bug widgets SHIPPED this session (feedback.py, pages/21_Feedback_and_Bugs.py, sidebar hook in state.py).
Next app step (when research reaches a stable point): the MODALITY × SCALE re-spine above, then Lens Lab.

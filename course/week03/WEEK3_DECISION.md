# Week 3 — Decision Doc (approve before any document is built)

_Concept: Partners & Forms (single root; mode = reproduce). Lock scope + outline + measures + banks FIRST. No scope leak into Wk4 (co-occurrence mechanics) or Wk5 (lift/null/tiers). Every value computed from Book6._

## A. Locked components carried from Weeks 1–2
8-beat module skeleton; computed-fact-vs-labeled-interpretation; **size/frequency control before concluding** (the course spine); engine/Book6 as the only numbers; verify with cs-sweep + scope-grep + render; bash-heredoc for Arabic files; no scope leak.

## B. Concepts TESTED against Book6 (why these work)
- **Morphological forms — fully reproducible** (Book6 col8 roots align 1:1 with col9 word-forms, 0% misalignment; matches the Week-1 app numbers exactly).
  - ẓulm (ظلم): 17 surface forms — ظالمين 28.9% (active participle, "the wrongdoers"), ظلم 24.4%, يظلم 11.4%, ظالمون 10.5%, **ظلمات 7.3% ("darknesses" — a polysemy split)**.
  - ṣabr (صبر): صبر 27.2%, **اصبر 24.3% (imperative — "be patient!")**, صابرين 14.6%. Forms reveal grammatical mood.
  - Form counts vary: عدل 6 forms vs كفر 20 — morphological richness differs by root.
- **Partners — reproducible & match the bank** (عدل↔قسط strongest; ظلم↔نفس = "wronging oneself"). The app reports a length-controlled significant-partners list.

## C. The “unlearn” (Week-3-appropriate, from FORMS not partners)
A root's most frequent *face* is often not its bare form: the commonest form of ظ-ل-م is **ظالمين, "the wrongdoers" (the agents)** — not the abstract act — and the same root also yields **ظلمات, "darkness."** One root, many faces: forms expose agency, mood, and polysemy that the root layer (Week 1) deliberately hid.

## D. CRITICAL REVIEW — the scope tightrope (most important decision)
The syllabus splits this material across three weeks:
- **Wk3 (this week):** *list* a root's length-controlled significant partners + its morphological forms — **reproduce**.
- **Wk4:** which root shares the MOST ayahs, and **why raw counts mislead** — find.
- **Wk5:** compute **lift**, apply the **length-aware null**, assign **tiers** — find.

Therefore Week 3 = **forms in depth + partners read descriptively.** We may *say* the app's partner list "is already frequency/length-controlled (mechanism in Weeks 4–5)" as a labeled preview, but we do **not** demonstrate raw-vs-controlled co-occurrence (that is Wk4's signature) and do **not** teach lift/null/tiers (Wk5). Forms carry the analytical depth; partners are introduced, not dissected.

**Diversity vs Wk1–2:** new lenses — Arabic root-and-pattern **morphology** and **relationships between roots**. Genuinely distinct from frequency and distribution.

## E. Proposed module outline (8-beat skeleton, ~45 min, no scope leak)
- M0 Opening & recap (0–3): Wk1 how much, Wk2 where; today a root's COMPANY — forms (internal) + partners (external).
- M1 Root vs form — the pattern system (3–9): one root → many forms; callback to Wk1 tokenization (we collapsed forms to count; now we re-open them).
- M2 Reading a form distribution (9–16): ẓulm's 17 forms; the donut; dominant form ظالمين.
- M3 What forms reveal — agency, mood, polysemy (16–23): participles (agents), imperative صبر→اصبر, polysemy ظلم/ظلمات. **The unlearn.**
- M4 Partners — a root's external company (23–30): roots co-occur; read the app's significant-partners list; عدل↔قسط, ظلم↔نفس.
- M5 Reading partners honestly (30–36): the list is already length-controlled (why/how = Wk4–5, labeled preview); significant ≠ meaningful; a partner is a lead, not a verdict.
- M6 Advantages, limits & what this loses (36–41): forms reveal grammar the root hides; partners reveal company; but forms ≠ meaning, and a partner ≠ direction or cause (Wk4–6).
- M7 Fact vs interpretation, wrap & bridge (41–47): two-sentence form; bridge to Wk4 (which root shares the MOST ayahs, and why raw counts mislead).

## F. Measures & thresholds (lock once)
- Form distribution = share of a root's tokens by surface form (col9 forms aligned to col8 roots), reported as % with raw counts; "N distinct forms."
- Partner list = the app's length-controlled significant partners (read-only this week); we report the partner root, joint count, and the app's significance flag — **not** lift/null math (Wk5).
- No new normalization; the size-true/per-1,000-roots standard from `NORMALIZATION_STANDARD.md` still governs any density mention.

## G. Banks
- Reuse the Week-1/2 root set + per-member assignments. Worked example: **ẓulm** (continuity — its forms incl. the polysemy split). Contrast roots for forms: **صبر** (imperative), **عدل** (few forms). Partner exemplars: عدل↔قسط, ظلم↔نفس.

## H. Screenshots to capture (you snap → upload → I insert)
1. App **Surface-forms** view (donut/list) for ẓulm — the 17 forms with %.
2. App **partners / co-occurring roots** panel for a root (عدل or ظلم) — the significant-partners list.
3. (Optional) a root with few forms (عدل) for contrast.

## I. Build order after sign-off
data bank (forms + partners) → figures (form-distribution bar, a partners figure) → **lecture notes (approve)** → worked example → app guide → exercise+key → quiz+key → deck → instructor script → quick-ref → further-study. Verify once per batch.

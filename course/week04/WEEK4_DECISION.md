# Week 4 — Decision Doc (approve before building)

_Concept: Co-occurrence as a measure (pair; mode = find). Lock scope + outline + measures + banks first. No scope leak into Week 5 (the formal length-aware null, Monte-Carlo, lift tiers). Every value computed from Book6._

## A. Locked components carried from Weeks 1–3
8-beat module skeleton; computed-fact-vs-labeled-interpretation; **control before concluding** (the course spine); Book6 as the only numbers; verify with cs-sweep + scope-grep + figure-title check + render; **figures English-titled with shaped Arabic** (`COURSE_STANDARDS.md` §9–9b); bash-heredoc for Arabic files; **week self-contained** (§9c). Deliverables target ~3,500-word lecture notes, 8 modules, 15 slides, 8 figures, no fluff.

## B. The concept (genuinely new vs Weeks 1–3)
Weeks 1–3 measured one root at a time (how much / where / its forms & partners). Week 4 is the first **pair** measure and the first **find** task: given a target root, **which other root shares the most ayahs with it — and why the raw shared-ayah count misleads.**

## C. Concept TESTED against Book6 — and the "unlearn"
Worked target **صلو (prayer)**:
- **Raw** shared-ayah count crowns قوم (52) and ءله (44) — but those win only because they are everywhere (freq 597 and 1879).
- **Controlled for frequency** (observed vs expected-by-chance), the real bond is **زكو (zakat): 28 shared ayahs, ×34.6 more than chance** — half of all zakat verses sit beside prayer (أقيموا الصلاة وآتوا الزكاة).
This is the exact analogue of Week 2's length confound, now a **frequency confound**: a frequent candidate shares ayahs with everything; control for that and the true companion appears.
Other tested cases (robust): كيل↔وزن (×137, honest weights & measures), عهد↔نقض (covenant & breaking, ×96), سجد↔ركع (×46), جنن↔عدن (×32), قرض↔حسن (×30, قرضًا حسنًا), نهر↔تحت (×49, rivers beneath).

## D. Scope tightrope (critical)
- **Week 4 (this week):** the find-task + the idea of **observed vs expected-by-chance** (a first, frequency-based control) → which candidate shares the MOST, and why raw counts mislead.
- **Week 5:** upgrade the control to the **length-aware null**, validate by **Monte-Carlo**, and assign **lift tiers**.
So Week 4 teaches observed-vs-expected and the ratio conceptually ("× more than chance"); it does **not** present the formal lift definition, the null model, or tier labels — those are Week 5, named only as a labeled preview.

## E. New themed root set — "Devotion & social duty: the acts and their bonds" (distinct from Wk1–3)
Worked target: **صلو**. 12-member assignment bank (target → its controlled top partner):
صلو→زكو · زكو→صلو · كيل→وزن · جنن→عدن · حسب→سرع · نفق→رزق · يتم→سكن (orphan & needy) · عهد→نقض · سجد→ركع · نهر→تحت · شفع→نفع · قرض→حسن. Each member is given a target + a slate of candidate roots and must **find** which candidate shares the most, raw vs controlled.

## F. Proposed module outline (8 beats each, ~45 min, no Wk5 leak)
- M1 Opening & recap — one root → pairs; the new question: which two roots share ayahs?
- M2 Co-occurrence: counting shared ayahs (the joint count) — صلو ∩ زكو.
- M3 Why the raw count misleads — the frequency confound (قوم/ءله win by being everywhere).
- M4 The fix: observed vs expected-by-chance — "× more than you'd expect."
- M5 The headline & unlearn — صلو's true companion is زكو, not قوم/ءله.
- M6 Reading a candidate slate (the find-task) — rank raw vs controlled; second case كيل↔وزن.
- M7 Advantages, limits & what co-occurrence still can't say — direction/cause (Wk6); the rigorous null & tiers (Wk5).
- M8 Fact vs interpretation, wrap & bridge to Week 5 (lift, the length-aware null, tiers).

## G. Measures & thresholds (lock once)
- joint(A,B) = ayahs containing both roots.
- expected(A,B) = freq(A)·freq(B)/6236 (independence baseline).
- ratio = joint/expected ("× more than chance") — the Week-4 control. Min support: joint ≥ 5 to report a ratio.
- Week 5 will replace `expected` with the length-aware null and add tiers. (Per `NORMALIZATION_STANDARD.md` discipline: control before concluding.)

## H. Figures (8, English-titled, shaped Arabic)
1. Two roots sharing ayahs — صلو ∩ زكو overlap. 2. صلو candidates by RAW joint (قوم/ءله win). 3. صلو candidates by CONTROLLED ratio (زكو wins). 4. Raw-vs-controlled flip (the unlearn). 5. Why raw misleads — a frequent candidate's chance overlap. 6. كيل↔وزن honest-measures case (×137). 7. The paradise cluster جنن↔عدن/تحت/نهر. 8. A worked find-slate: raw rank vs controlled rank for one target.

## I. Deliverables (self-contained in week04/)
lecture notes (~3,500 words, 8 modules) → figures (week04/figs) → worked example → app guide → exercise+key → quiz+key → deck (15 slides) → instructor script → quick-ref → further-study → Excel data bank → build/ scripts. Verify once per batch.

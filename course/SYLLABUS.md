# From Frequency to Structure
### A Data-Driven Exploration of Qur'anic Roots
**Course syllabus — 10 weeks, flipped format**

---

## Course description

This course teaches members to investigate the Qur'an's vocabulary the way an analyst would: by measuring how its ~1,700 three-letter roots behave across all 6,236 ayahs of the corpus, and learning to read those measurements honestly. Using the *Quran Root Explorer* web app as a laboratory, members move from the simplest question — how often a root appears — up to the deepest the data supports: which roots cluster into recurring structural patterns.

The course is built on one discipline: **separate what the data computes from what we interpret.** Every week produces a finding, an understanding, and an interpretation — with the interpretation always *labeled* as interpretation, never disguised as a fact. Several weeks will require members to *unlearn* a traditional, folkloric, or simplistic assumption when the corpus disagrees with it — and the corpus disagrees more often than expected.

## Prerequisites

Familiarity with the Qur'an and a web browser. No statistics or programming background is assumed; every measurement is introduced in plain language before it is used.

## Course-level outcomes

By the end, each member can:

1. Operate every analytical page of the app without guidance.
2. Correctly read frequency, distribution/concentration, partner, co-occurrence, lift, tier, network, and motif outputs — with their normalizations.
3. Write a defensible two-sentence reading: one sentence of computed fact, one of labeled interpretation.
4. Judge whether a result is structurally real or an artifact of corpus size, ayah length, or rarity.
5. Independently investigate a root, pair, or set they were never shown, and present a defensible finding with individual and social relevance.

## The data-driven contract

This course makes no claim it has not computed and tested against Book6. Specifically:

- **Natural units only** — the root, the ayah, the surah. No invented divisions.
- **Legitimate orderings only** — canonical (mushaf) order is intrinsic and used freely; revelation order is an external, surah-coarse *indicative* overlay, flagged as such and never a core claim. The Meccan/Medinan binary is **not** used as a core measure.
- **Normalization everywhere** — frequencies as rates, distribution corrected for surah size with a support floor, co-occurrence and motifs cleared by a length-preserving null cross-checked analytically and by Monte-Carlo.
- **Interpretation is always labeled** — reasoned readings are welcome every week, but never presented as computed fact.

## Per-session objectives

| Wk | Concept | By the end of the session, the member can… | Unit | Mode |
|----|---------|--------------------------------------------|------|------|
| 1 | Frequency | retrieve a root's ayah-frequency and express it as a rate; give a first interpretation | single root | reproduce |
| 2 | Distribution & concentration | read a root's surah spread, concentration (Gini/top-3), and size-normalized home surah | single root | reproduce |
| 3 | Partners & forms | list a root's length-controlled significant partners and its morphological forms | single root | reproduce |
| 4 | Co-occurrence | determine which candidate root shares the most ayahs with a target, and why raw counts mislead | pair | find |
| 5 | Lift & tiers | compute a pair's lift, apply the length-aware null, assign the tier, benchmark on Calibration | pair | find |
| 6 | Asymmetry & networks | distinguish P(A\|B) from P(B\|A); identify the hub of a themed set | cluster | find |
| 7 | Motifs (intro) | read a 3-root motif and judge whether it beats a length-aware expectation | triple | judge |
| 8 | Motifs & significance | defend whether a motif is structural, separating significance from support | triple | judge |
| 9 | Interpretation discipline | distinguish a computed fact from an interpretive overlay and audit an overlay against the data | meta | judge |
| 10 | Capstone & synthesis | investigate an unseen root/set through the full pipeline and synthesize the term's findings | any | investigate |

## Detailed session outlines

_Expanded as each week is finalized and signed off. Each finalized lecture runs the course's locked eight-beat module skeleton (what it is · why we do it · how it's done · what we get · why it matters · in the data · takeaway · bridge — see `LECTURE_MODULE_TEMPLATE.md`)._

### Week 1 — Frequency  ✅ finalized
A 45-minute lecture in nine modules; single root; mode = reproduce.

0. **Opening & course frame** — measuring as reproducible counting; the one rule (computed fact vs labeled interpretation).
1. **What frequency analysis is** — the bag-of-words tradition; presence is a signal of emphasis, not importance.
2. **Tokenization & preprocessing** — root reduction (كَتَبَ/يَكْتُبُ/كِتاب → كتب), letter/diacritic normalization, function-word drop; once-per-ayah (document frequency); 51,024 root-tokens.
3. **Normalization to a rate** — per 1,000 ayahs and the size-true per 1,000 roots; the ظلم↔هدي ranking flip (46.5 vs 43.0 per-ayah; 6.17 vs 6.19 per-root).
4. **The Qur'anic data — reading it** — the themed-root ladder; live retrieval of كفر (465 ayahs, the most-named) and عسر (12, the rarest); predict-then-check on ease vs hardship (يسر 40 vs عسر 12, ~3.3×).
5. **The headline finding & the "unlearn"** — ظلم 290 vs عدل 24, about 12× more; the corpus names the violation far more than the ideal.
6. **Frequency as a vector** *(preview)* — the vector-space model as the foundation of how machines read text; embeddings/skip-gram named as further-study only, never asserted against Book6.
7. **Advantages, disadvantages & limits** — objective/scalable/comparable vs the loss of stance, speaker, polysemy, syntax, and relationships.
8. **Fact vs. interpretation — the discipline & wrap** — the two-sentence form; bridge to Week 2.

**Deliverables (signed off):** lecture notes (v3), instructor script (v3), 19-slide deck (incl. a vector-space slide), worked example (al-Fatiha), app & plot guide, exercise + answer key, quiz (14 Q) + key, quick reference, further study. All values reproducible from Book6; Arabic complex-script verified.

### Week 2 — Distribution & Concentration  ✅ finalized
A 45-minute lecture in nine modules; single root; mode = reproduce.

0. **Opening & recap** — frequency told us how much; today, where a root sits and how evenly it spreads.
1. **What distribution & concentration are** — spread across the 114 surahs vs inequality of that spread.
2. **Breadth** — in how many of the 114 surahs (عسر 9 vs كفر 77); reach is not predicted by frequency.
3. **Concentration** — Lorenz curve, Gini (0 even → 1 all in one), top-3 share (رشد 0.95 concentrated vs كفر 0.69 spread).
4. **The home surah — normalize by ROOT-TOKENS, not ayahs** — the surah with most raw hits is usually just the longest; dividing by ayah-count is still confounded because ayahs vary in length. ظلم: raw al-Baqara → size-true home إبراهيم (15.8 per 1,000 root-tokens).
5. **Headline & the "unlearn"** — raw busiest surah = al-Baqara for 30 of the top-50 roots → 0/50 after size-true normalization; and per-ayah ≠ per-roots (صبر: al-Baqara → al-Kahf → at-Tur).
6. **The support floor** — trust a home only if count ≥ 3 AND surah ≥ 30 root-tokens, else "insufficient support" (عسر has no reliable home).
7. **Advantages, limits & what distribution loses** — geography, yes; importance and relationships, no.
8. **Fact vs. interpretation, wrap & bridge** — two-sentence form; bridge to Week 3 (partners & forms).

**Deliverables (signed off):** lecture notes, instructor script, 15-slide deck, worked example (home surah by hand), app & plot guide, exercise + key, quiz (14 Q) + key, quick reference, further study. **Locked this week:** size-true normalization = per 1,000 root-tokens (`NORMALIZATION_STANDARD.md`); figures render shaped Arabic (`COURSE_STANDARDS.md` §9).

### Week 3 — Partners & Forms  ✅ finalized
A 45-minute lecture in eight modules (each at full depth); single root; mode = reproduce. Worked root: ءمن (believe). New themed root set (faith / perception / Divine-Name vocabulary), distinct from Weeks 1–2.

1. **The root-and-pattern system (الجذر والوزن)** — a 3-consonant root poured into a pattern (wazn) → many words; root = metal, pattern = mould (ك-ت-ب → كاتب, مكتوب, كِتاب, يكتب, كُتِب).
2. **Reading a form distribution** — ءمن's 27 forms across 879 tokens; dominant form = the verb آمن (41%).
3. **Pattern families & the "unlearn"** — verb / participle / masdar; faith is overwhelmingly a VERB (61%), not the abstract noun إيمان — grammar encodes theology.
4. **The intensive forms & the Divine Names** — فعيل/فعّال intensives: رحيم, سميع, بصير, غفور, حكيم — one pattern over many roots.
5. **Polysemy by shared root** — ءمن → faith / security; كتب → book / decree; and the valence split ك-ث-ر → كوثر (blessed abundance, 108:1) vs تكاثر (blameworthy rivalry, 102:1).
6. **Partners — a root's external company** — collocation; ءمن travels with صلح / عمل (faith + works).
7. **Reading partners honestly — antonyms as partners** — significant ≠ meaningful; ءمن ↔ كفر (126 ayahs); mutual pairs رحم↔غفر, سمع↔بصر.
8. **Fact vs. interpretation, wrap & bridge** — two-sentence form; bridge to Week 4 (co-occurrence as a measure).

**Deliverables (signed off):** lecture notes (v2, ~3,000 words), instructor script, 15-slide deck, worked example, app & forms guide, exercise + key, quiz (14 Q) + key, quick reference, further study, Excel data bank. **Locked:** figures English-titled with shaped Arabic (`COURSE_STANDARDS.md` §9, §9b); each week self-contained (§9c).

### Week 4 — Co-occurrence  ✅ finalized
A 45-minute lecture in eight modules; pair; mode = find. Worked target: صلو (prayer). New themed root set ("devotion & social duty"), distinct from Weeks 1–3.

1. **From one root to a pair** — the first PAIR measure and first FIND task: which root shares the most ayahs with a target?
2. **Counting shared ayahs (the joint count)** — the overlap of two roots; صلو ∩ زكو = 28.
3. **Why the raw count misleads — the frequency confound** — a frequent root (God, 1,879 ayahs) shares ayahs with almost everything; the "celebrity in every photo."
4. **The fix — observed vs expected-by-chance** — expected = freq(A)·freq(B)/6,236; ratio = × over chance.
5. **The headline & the "unlearn"** — raw says قوم/God; controlled, prayer's true companion is زكو (×34.6) — half of all zakat ayahs sit with prayer (أقيموا الصلاة وآتوا الزكاة).
6. **The find-task** — rank a candidate slate by × over chance (support floor: joint ≥ 5); the raw list is a decoy. Second case: كيل↔وزن (×137).
7. **Advantages, limits & what co-occurrence can't say** — direction (Week 6), the rigorous null & tiers (Week 5), association ≠ cause.
8. **Fact vs. interpretation, wrap & bridge** — two-sentence form; bridge to Week 5 (lift & tiers).

**Deliverables (signed off):** lecture notes (~3,300 words), instructor script, 15-slide deck (dense), worked example, app & co-occurrence guide, exercise + key, quiz (14 Q) + key, quick reference, further study, Excel data bank. **Locked:** observed-vs-expected control (a first, frequency-based control sharpened in Week 5); English-titled shaped-Arabic figures; dense-slide standard.

### Week 5 — Lift & Tiers  ✅ finalized
A 45-minute lecture in eight modules; pair; mode = find/judge. Worked pair: صلو ↔ زكو. Reuses Week-4 pairs (judged rigorously) plus spurious cases.

1. **From ranking to judging** — Week 4 ranked bonds; today we deliver a VERDICT: is a bond real?
2. **Two problems Week 4 left** — long-ayah inflation; big shared counts that are chance.
3. **The length-aware null** — a fairer baseline (the golf-handicap); lift = observed ÷ length-aware expected; every lift deflates a little (صلو↔زكو ×34.6→×23.6).
4. **Monte-Carlo significance** — reshuffle the seating 3,000× (preserving ayah lengths + root frequencies); p = how often chance matches.
5. **The tiers** — structural (lift≥3 AND p<0.001 AND joint≥5) / borderline / spurious.
6. **The headline & "unlearn"** — a big shared count is NOT a bond: قول↔شيء (113 shared) is spurious; صلو↔زكو (28) is structural.
7. **Calibration & limits** — benchmark tiers on known pairs; still no DIRECTION (Week 6); significance ≠ meaning.
8. **Fact vs. interpretation, wrap & bridge** — two-sentence form; bridge to Week 6 (asymmetry & networks).

**Deliverables (signed off):** lecture notes (~3,200 words), instructor script, 15-slide dense deck, worked example, app & tiers guide, exercise + key, quiz (14 Q) + key, quick reference, further study, Excel data bank. **Locked:** length-aware null + Monte-Carlo + tiers; English-titled shaped-Arabic figures; dense-slide standard.

### Week 6 — Asymmetry & Networks  ✅ finalized
A 45-minute lecture in eight modules; pair → cluster; mode = find. Worked pair: عدن → جنن. Worked network: the "deeds & the reckoning" cluster (hub صلح).

1. **Opening & recap** — Week 5 judged WHETHER a bond is real; today, WHICH WAY it points and how bonds assemble into a map.
2. **Co-occurrence is symmetric** — one shared count, faced both ways; a handshake, not a phone call.
3. **Conditional probability** — P(A|B) vs P(B|A); the gap is the direction (the squares-and-rectangles logic).
4. **The headline & "unlearn"** — عدن always implies جنن (100%); a garden is rarely Eden (6%). The specific implies the general.
5. **From pairs to a network** — roots = nodes, Tier-1 bonds = edges, degree; single bonds are sentences, the network is the paragraph.
6. **The hub of a themed set** — صلح (righteous works) is the hub of "deeds & the reckoning," degree 5 (the airport/keystone).
7. **Reading networks honestly** — a hub is central, not most important; direction ≠ cause; the map depends on the threshold.
8. **Fact vs. interpretation, wrap & bridge** — two-sentence form; bridge to Weeks 7–8 (motifs).

**Deliverables (finalized):** lecture notes (~3,000 words), instructor script, 15-slide dense deck, worked example, app & networks guide, exercise + key, quiz + key, quick reference, further study, Excel data bank (4 sheets), 8 figures incl. the network graph, build scripts. **Decision doc:** `week06/WEEK6_DECISION.md`.

### Week 7 — Motifs (intro)  ✅ finalized
A 45-minute lecture in eight modules; triple; mode = judge. Worked motif: شمس · قمر · نجم (sun · moon · star). Fresh cosmology/natural-signs root family.

1. **From the edge to the triangle** — the unit becomes the triple; the smallest pattern big enough to show a scene.
2. **What a motif is** — three roots in one ayah; the three-sieve intersection (celestial trio in 7:54, 16:12, 22:18).
3. **The length-aware triple null** — E as a product of three length weights; the penalty compounds across three roots.
4. **The headline & UNLEARN 1** — count ranks motifs backwards: sky·earth·between (34×→6.5×) vs sun·moon·star (3×→3,721×).
5. **Reading the verdict** — obs, E, adjusted lift, z, Monte-Carlo p; the tiers (reused from Week 5, for triples).
6. **UNLEARN 2 — a motif is not its pairs** — the open triangle جبل·موه·شجر (strong pairs, trio = 0); test the centre directly.
7. **Judging honestly** — structural vs borderline vs spurious; rare-but-real vs frequent-but-explainable; fact vs interpretation.
8. **Wrap & bridge** — to Week 8 (significance vs support).

**Deliverables (finalized):** lecture notes (~3,735 words), instructor script, 15-slide dense deck, worked example, app & motif guide, exercise + key, quiz + key, quick reference, further study, Excel data bank (4 sheets), 8 figures, build scripts. **Decision doc:** `week07/WEEK7_DECISION.md`.

### Week 8 — Motifs & Significance  ✅ finalized
A 45-minute lecture in eight modules; triple; mode = judge/defend. Worked pair: رسل · بشر · نذر (robust) vs نبء · تلو · حقق (fragile). Fresh messengers/revelation root family.

1. **From "is it real?" to "can I trust it?"** — interrogating the Week-7 verdict itself; output = a Trust label.
2. **Significance is not support** — two numbers a tier hides: lift (how far above chance) vs verses (how much evidence). The witnesses analogy.
3. **The fragile structural** — نبء·تلو·حقق: a 22× lift built on 2 verses; a tower on a single flagstone.
4. **The jackknife & the "unlearn"** — remove one verse and re-judge; a higher lift is NOT a stronger result (Jenga: bedrock stands, sandcastle falls).
5. **What the p-value already knew** — the Monte-Carlo p is partly a support meter; fewer verses → weaker p.
6. **Multiple testing** — ~817M possible triples; ~817k false "structural" at p<0.001; the Texas-sharpshooter trap; call your shot.
7. **Defending a verdict** — the Trust label (Robust / Fragile / Spurious); the bank's ratio is itself a finding; fact vs interpretation.
8. **Wrap & bridge** — to Week 9 (interpretation discipline).

**Deliverables (finalized):** lecture notes (~3,525 words), instructor script, 15-slide dense deck, worked example, app & trust guide, exercise + key, quiz + key, quick reference, further study, Excel data bank (4 sheets), 8 figures, build scripts. **Decision doc:** `week08/WEEK8_DECISION.md`.

### Week 9 — Interpretation Discipline  ✅ finalized
A 45-minute lecture in eight modules; audit; mode = judge a reading. Worked cases: الدنيا/الآخرة (contradicted), حيي↔موت (supported), شكر/كفر (underdetermined). Fresh "claims & counting" root set.

1. **Turning the tools outward** — eight weeks produced facts; today we audit the READINGS people lay over the text.
2. **What an overlay is** — an interpretive claim; the three verdicts (Supported / Contradicted / Underdetermined); the referee with instant replay.
3. **Fix the rule before you look** — the unit problem returns; one fair counting rule, pre-committed, applied to both sides.
4. **The headline & "unlearn"** — الدنيا = الآخرة = 115 is form-true (115=115) but root-false (دنو 133 vs ءخر 250); a true number, a false claim.
5. **The failure-mode catalogue** — cherry-picked unit (Wk1), polysemy (Wk3), normalization (Wk2), non-significant co-occurrence (Wk4–5), multiple testing (Wk8); each mapped to the tool that catches it.
6. **A reading the data SUPPORTS** — life ↔ death (حيي/موت), 65 verses, lift 17×.
7. **An UNDERDETERMINED reading** — gratitude vs disbelief (شكر/كفر), lift 1.36×; the honest "we can't tell."
8. **Wrap & bridge** — the auditor's two-column discipline; bridge to Week 10 (the capstone).

**Deliverables (finalized):** lecture notes (~3,376 words), instructor script, 15-slide dense deck, worked example, app & audit guide, exercise + key, quiz + key, quick reference, further study, Excel data bank (4 sheets), 8 figures, build scripts. **Decision doc:** `week09/WEEK9_DECISION.md`.

### Week 10 — Capstone  ✅ finalized
A 45-minute lecture in eight modules; any root; mode = investigate. Worked root: غفر (forgiveness), carried through all nine stages. Fresh root; no new measure — integration and application.

1. **Nine instruments, one pipeline** — the weeks revealed as stages of one method; meet غفر, an unseen root.
2. **Frequency & distribution** — 202 ayahs, 4.44/1k; breadth 56/114, size-true home Sūrat Nūḥ — common and spread.
3. **Forms — the Divine Name in the grammar** — غفور, the فعول intensive ("the Oft-Forgiving"); استغفر, Form X "seek forgiveness."
4. **Partners & lift** — the sin–repentance–mercy cluster, all structural (by length-aware lift, never raw count).
5. **Direction & networks** — sin → forgiveness (51% vs 9%): wrongdoing summons the answer of forgiveness.
6. **Motifs & trust** — غفر·توب·رحم robust (55×, 18 verses, survives jackknife) vs غفر·ذنب·توب fragile (collapses).
7. **The audit** — "forgiveness is always paired with mercy"? 45% — supported as association, contradicted as "always."
8. **Synthesis & your capstone** — no single number is a portrait, only the pipeline is; investigate your own unseen root.

**Deliverables (finalized):** lecture notes (~3,000 words), instructor script, 15-slide dense deck, worked example (the full غفر pipeline), **capstone assignment + rubric** (12-root member bank), app & pipeline guide, exercise + key, quiz + key, quick reference, further study, Excel data bank (5 sheets), 8 figures, build scripts. **Decision doc:** `week10/WEEK10_DECISION.md`.

---

_All ten weeks FINALIZED and signed off. Every week is self-contained (build scripts + data bank + decision doc + 8 shaped-Arabic figures + dense 15-slide deck + full document set), and every value is reproducible from Book6._

## Required materials

- *Quran Root Explorer* — https://quranproject-quran-root-explorer.hf.space/
- The Book6 corpus (provided; the app uses it directly)
- A Google account (for quizzes)

## Weekly structure (≤ 3 hours total)

Each week is flipped: members watch/read the lecture material and complete a short pre-class exercise before meeting.

- **Lecture (≈45 min):** eight modules, each carrying the eight beats (what it is · why · how · what we get · why it matters · in the data · takeaway · bridge).
- **Pre-class exercise (≈30–45 min):** each member is assigned one root/pair/motif/claim from the week's bank; submitted the night before — it gates the debrief.
- **Debrief & worked example (≈45 min):** the assigned items are compared; the worked example is walked through against the app and the data bank.
- **Quiz (≈15 min):** short check on the week's concepts.

## Assessment & weights

- Weekly pre-class exercises — 40%
- Weekly quizzes — 25%
- Participation in the debrief — 10%
- Capstone (Week 10): full pipeline on an unseen root, defended number by number — 25%

## Grading scale

A (90–100) · B (80–89) · C (70–79) · D (60–69) · F (< 60). Every claim in graded work must separate computed fact from labeled interpretation; unlabeled interpretation presented as fact is the single most penalized error.

## Policies

- **Fact vs. interpretation:** reasoned readings are welcome every week, but never presented as computed fact.
- **Reproducibility:** every number must be reproducible from Book6 via the app or the course engine.
- **Control before you conclude:** raw counts are a starting point, never a verdict; normalize and control for the week's confound first.
- **Honesty of verdicts:** "the data cannot decide" (underdetermined) is a legitimate and expected answer.
- **Academic integrity:** standard institutional policies on collaboration and attribution apply.

## Course self-evaluation

At the end of the course, members audit one widely-circulated interpretive claim about the Qur'an end-to-end, using the full pipeline, and present a defensible verdict (Supported / Contradicted / Underdetermined) with its failure mode — the capstone demonstration that the course's literacy has been internalized.

## Source of all course data

All numbers in this course are computed from the **Book6** corpus (the same data the *Quran Root Explorer* app uses): 6,236 ayahs, ~1,700 triliteral roots. The course engine imports the app's own modules so every figure is reproducible and byte-identical to what members see in the app.

# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from _dochelper import newdoc,P,H,bullet,ACCENT,TEAL,GREY
OUT=os.path.abspath(os.path.join(HERE,".."))
TT={1:"Introduction — the pointer hypothesis",2:"The Method — the label-permutation null",3:"The Data & the Root Anchor",
4:"Contiguity I — Book Order (muṣḥaf)",5:"Contiguity II — Revelation Order (nuzūl)",6:"Per-Family Deep Dive",
7:"The Long-Sūra Flag",8:"Revelation-Phase Mapping",9:"Permutation Tests in Depth",10:"Multiple Comparisons & FDR",
11:"Effect Size, Power & the Scale Rule",12:"Bootstrap & Confidence",13:"What It Is NOT — No Shared Theme",
14:"What It Is NOT — No Frequency Code",15:"The Single-Letter Leads (ق, ن)",16:"Boundary Variants & the Graph View",17:"Synthesis — the Pointer Model"}
def E(goal,tasks,quiz,app): return dict(goal=goal,tasks=tasks,quiz=quiz,app=app)
K={
1:E("introduce the disjoint letters and the falsifiable hypothesis that they are POINTERS — tags that group and place sūras, not content to decode.",
 [("List the four multi-member families and their sūras.","حمٓ (40–46), الٓمٓ (2,3,29–32), الٓرٓ (10–15), طسٓمٓ (26,28)."),
  ("State the pointer hypothesis in one sentence.","A disjoint-letter opening is a tag that groups a family of related sūras and marks where they sit, without describing their content."),
  ("Why is 'what do they mean?' the wrong question?","It treats the letters as a content code; a millennium of that failed. 'What do they organize?' is testable."),
  ("What does a pointer predict that a content code does not?","Grouping/contiguity, possibly magnitude marking, and crucially NO shared theme."),
  ("Give the library analogy and its prediction.","A call number groups/places a book without summarizing it — so same-tag sūras should cluster but NOT share content.")],
 [("How many sūras open with disjoint letters?","29."),("Name the four multi-member families.","حمٓ, الٓمٓ, الٓرٓ, طسٓمٓ."),
  ("Pointer vs content code — one line.","A pointer references/groups; a code describes. The letters behave like pointers."),
  ("Why organization not content here?","The signal study showed verse content is generic to Arabic; only organization survived."),
  ("What is the anchor unit?","The root (ریشه)."),("One thing the course will NOT claim.","A hidden code, number-miracle, or secret meaning.")],
 ["Enter a disjoint-letter sūra (e.g. 40); see its family.","View the family on muṣḥaf and nuzūl timelines.","Note the حمٓ block (40–46).","Preview the label-permutation null."]),
2:E("install the testing discipline: why the label-permutation null (not a random-chapter baseline) is decisive, and how the frequency claim is a false positive.",
 [("Why is a random-chapter baseline misleading?","Muqaṭṭaʿāt sūras cluster anyway (mostly Meccan, long), so any grouping looks clustered."),
  ("Describe the label-permutation null.","Freeze the 29 sūras; shuffle only which tag each gets; ask if the real tagging groups better than random relabeling."),
  ("Tell the frequency false-positive story.","Within-chapter, الٓمٓ letters rank top (p≤0.001); cross-chapter, no more frequent than elsewhere (0/29). ا,ل,م are just common."),
  ("State the general lesson.","Beat NORMAL, not just random; the cross-chapter/natural-language baseline is mandatory."),
  ("Why correct for many tests?","Tags × orderings × statistics is a large search; some sparkle by luck. Use FDR; declare tests first.")],
 [("The decisive null is?","Label-permutation over the 29 fixed sūras."),("Why not random chapters?","They cluster anyway; conflates background with tag effect."),
  ("Frequency claim within vs cross?","Within p≤0.001 (illusory); cross 0/29 (refuted)."),("Why is ا,ل,م frequent everywhere?","They are the commonest Arabic letters."),
  ("Beat random or beat normal?","Beat normal."),("A method that can say no is?","Trustworthy when it says yes.")],
 ["Toggle random-chapter vs label-permutation null.","Set 50,000 draws.","Run the frequency test within- then cross-chapter.","Watch the false positive collapse."]),
3:E("build and verify the data object: Book6.xlsx, the root anchor, and the 29-sūra family table — before any test.",
 [("Name the Book6 columns the course uses.","Sūra # (col 6), āyah # (col 7), name (8), ROOT (9), revelation order (13)."),
  ("Why anchor on the root?","The triliteral root carries the most meaning per token; surface forms/diacritics are complementary channels."),
  ("How is sūra length computed?","Max āyah number per sūra."),
  ("Why verify before validating?","A wrong family list or anchor would poison every downstream p-value."),
  ("Is a root id a number you can average?","No — it is nominal (a label); compare profiles by overlap/cosine, not by averaging ids.")],
 [("Data source?","Book6.xlsx (114 sūras, 6,236 āyāt)."),("The anchor?","The root (col 9)."),("How many muqaṭṭaʿāt sūras?","29."),
  ("Families vs singletons?","4 multi-member families + 9 singletons."),("Root id level of measurement?","Nominal."),("First step before testing?","Verify the family table and counts.")],
 ["Load Book6.xlsx.","Build root profiles.","Group the 29 into families.","Verify counts vs canonical openings."]),
4:E("present the first half of the core result: same-tag sūras cluster in book (muṣḥaf) order, p≈2×10⁻⁵.",
 [("State the muṣḥaf contiguity result.","Within-family mean distance Δ=6.79 vs null mean ≈19; label-permutation p≈2×10⁻⁵."),
  ("Define the statistic.","Average sūra-number gap over all same-tag pairs; small = tightly grouped."),
  ("Give the Ḥawāmīm in book order.","Sūras 40–46 — an unbroken block."),
  ("Are all families significant?","Yes: ḤM ~0, ALR ~0, ALM 0.009, ṬSM 0.034."),
  ("Why not a random-chapter baseline?","It conflates the tag with background clustering; use label-permutation.")],
 [("Observed Δ (muṣḥaf)?","6.79 sūras."),("p-value?","≈2×10⁻⁵."),("Ḥawāmīm sūras?","40–46."),
  ("ALM structure?","2,3 early + 29–32 run."),("Statistic?","Within-family mean pairwise distance."),("All four families significant?","Yes.")],
 ["Compute within-family muṣḥaf distance.","Shuffle labels 50,000×.","Read the p-value tail.","Inspect the ḤM block."]),
5:E("present the second half of the core result: contiguity also holds in revelation (nuzūl) order, p≈2×10⁻⁵.",
 [("State the revelation-order result.","Within-family Δ=7.30 vs null mean ≈19; p≈2×10⁻⁵, independent of book order."),
  ("Give the Ḥawāmīm in revelation order.","Slots 60–66 — seven consecutive."),
  ("Why do two orderings matter?","Independent confirmation; a pattern in both is far harder to explain away."),
  ("Per-family nuzūl p-values?","ALM 0.004, ALR 0.0017, ḤM ~0, ṬSM 0.034."),
  ("What caveat attaches to nuzūl?","Revelation order is a reconstruction; the claim inherits its uncertainty (the muṣḥaf result does not).")],
 [("Observed Δ (nuzūl)?","7.30."),("p-value?","≈2×10⁻⁵."),("Ḥawāmīm nuzūl slots?","60–66."),
  ("ALR nuzūl?","51–54 (consecutive)."),("Why two orders?","Independent confirmation."),("nuzūl caveat?","It is a scholarly reconstruction.")],
 ["Recompute distance in nuzūl order.","Run the same null.","Compare muṣḥaf vs nuzūl.","See ḤM 60–66."]),
6:E("test every family individually, in both orders, with per-family nulls and a drop-one robustness check — no cherry-picking.",
 [("Why test each family separately?","To rule out a single family driving the omnibus; all four pass individually."),
  ("Per-family verdict?","ḤM, ALM, ALR, ṬSM all significant in both orders."),
  ("What is the drop-one check?","Remove any one sūra and recompute; the distance barely changes — no family rides on one member."),
  ("Why can't singletons be tested?","Size 1 → no internal pairs → no clustering statistic."),
  ("Which family is weakest, and is that a problem?","ṬSM (size 2, p=0.034) — still significant; the result does not depend on it.")],
 [("How many families tested?","Four multi-member."),("All significant both orders?","Yes."),("Drop-one effect?","Negligible."),
  ("Singletons testable?","No (size 1)."),("Weakest family?","ṬSM (p=0.034)."),("ḤM size?","7.")],
 ["Pick a family.","Run its size-matched null.","Check both orders.","Run the drop-one check."]),
7:E("show the long-sūra flag: muqaṭṭaʿāt mark the long sūras (median 85 vs 26, p≈2×10⁻⁵) — but length is not a per-tag attribute.",
 [("State the length result.","Median 85 vs 26 verses (means 95 vs 41); random-set null p≈2×10⁻⁵."),
  ("Group property or per-tag?","A group property; same-tag sūras are NOT length-matched (label-permutation p≈0.29)."),
  ("Name long tagged sūras.","al-Baqarah (2, الٓمٓ, 286), Āl ʿImrān (3, الٓمٓ, 200), al-Aʿrāf (7, الٓمٓصٓ, 206)."),
  ("Why does flagging long sūras matter?","The longest sūras hold most of the corpus's verses — the tag marks the book's pillars."),
  ("State the magnitude plainly.","A 3.3× median ratio — a large, interpretable effect.")],
 [("Median lengths?","85 vs 26."),("Long-flag p?","≈2×10⁻⁵."),("Per-tag length similarity p?","≈0.29 (none)."),
  ("Length: set or per-tag?","Set property only."),("A long الٓمٓ sūra?","al-Baqarah (286 āyāt)."),("Median ratio?","≈3.3×.")],
 ["Compare disjoint vs other lengths.","Test the group difference vs random sets.","Test a per-tag length (it fails).","List the longest sūras."]),
8:E("show the third organizational layer: tags map onto revelation phase (simple early, families late, المر Medinan).",
 [("Describe the phase mapping.","Single/short tags early-Meccan; multi-letter families late-Meccan; mixed المر alone Medinan."),
  ("Where do mixed tags sit?","المص (7) between ALM and ALR; المر (13) inside the ALR run."),
  ("Mean nuzūl by tag type?","≈25 (single/short) → ≈70 (families) → 96 (mixed)."),
  ("Is this novel?","Mostly known (most muqaṭṭaʿāt are Meccan); the value is the systematic, quantified mapping."),
  ("How should phase order be read?","As an organizational regularity consistent with the pointer model — not an encoded message.")],
 [("Phase of single/short tags?","Early-Meccan."),("Phase of families?","Late-Meccan."),("المر phase?","Medinan (lone)."),
  ("Mean nuzūl of families ≈?","~70."),("Boundary variant inside الر?","المر (13)."),("Novel part?","The quantified mapping.")],
 ["Color families by phase.","Map tag type → phase.","Spot the المر outlier.","Plot length vs revelation order."]),
9:E("explain the engine: exchangeability, the null distribution, and why freeze-and-shuffle isolates the tag — the method that can say no.",
 [("What does exchangeability assume?","Under H₀ the tag labels are interchangeable, so every relabeling is equally likely."),
  ("Why permutation, not a formula?","It builds the null from the data — no distributional assumption, exact by construction."),
  ("Why shuffle labels, not chapters?","To control background clustering and test the SPECIFIC tag effect."),
  ("Why report a converged p-value?","A p-value is an estimate with error; sample enough (≈50,000) that the conclusion is stable."),
  ("Why is the test falsifiable?","The same machinery refuted the frequency (0/29) and theme (0.27) claims — it can reject.")],
 [("Core assumption?","Exchangeability of labels."),("Shuffle what?","Labels, among the fixed 29."),("Statistic?","Within-family mean distance."),
  ("How many draws?","≈50,000."),("p = ?","Tail fraction at least as clustered."),("Falsifiable because?","It rejected the content claims.")],
 ["Fix the statistic.","Permute labels only.","Repeat 50,000×.","Read the tail."]),
10:E("control for multiple comparisons: the look-elsewhere effect, FDR (Benjamini–Hochberg), and Bonferroni — what survives.",
 [("What is the look-elsewhere effect?","Testing many things guarantees some pass by chance."),
  ("What does Benjamini–Hochberg control?","The false-discovery rate; compare ranked p to k/m·α."),
  ("FWER vs FDR?","FWER = P(any false positive), strict (Bonferroni); FDR = expected fraction of false discoveries, for screening."),
  ("What survives correction?","Muṣḥaf & revelation contiguity (p≈2×10⁻⁵) and the long-sūra flag — even under Bonferroni."),
  ("What fails after correction?","The frequency code (0/29), the theme (0.27); single-letter ق becomes borderline.")],
 [("Look-elsewhere effect?","Many tests → lucky positives."),("BH controls?","FDR."),("Strictest correction?","Bonferroni."),
  ("Contiguity survives?","Yes, even Bonferroni."),("Frequency claim?","Fails (0/29)."),("ق after correction?","Borderline.")],
 ["Count the tests.","Rank the p-values.","Apply BH and Bonferroni.","See which survive."]),
11:E("go beyond p-values: effect size (how big), power (could we detect), and the scale rule (stability with n).",
 [("Effect size of contiguity?","Observed distance is many null-SDs below the chance mean — large."),
  ("Why report effect size?","A tiny effect can be 'significant' with enough data; magnitude tells importance."),
  ("How does power depend on family size?","Bigger families are easier to confirm; the smallest are marginal."),
  ("Why can't singletons be tested?","Size 1 → zero internal pairs → no statistic; we flag them."),
  ("State the scale rule.","Estimates and p-values stabilize as n grows; small samples give noisy numbers.")],
 [("Effect size magnitude?","Many null-SDs (large)."),("p vs importance?","Different questions."),("Power grows with?","Family size."),
  ("Singletons testable?","No."),("Scale rule?","Stability rises with n."),("Why pool all 29?","More stable than single-family tests.")],
 ["Measure effect in null-SDs.","Simulate power by family size.","Watch SE shrink with n.","See why singletons are flagged."]),
12:E("quantify uncertainty: the bootstrap resamples family members to give confidence intervals that exclude the null.",
 [("What does the bootstrap do?","Resamples family members with replacement and recomputes the statistic to estimate uncertainty."),
  ("Permutation vs bootstrap?","Permutation → p-value (is it chance?); bootstrap → interval (how precise?)."),
  ("What does the CI show here?","The 95% interval for within-family distance lies entirely below the null region."),
  ("Why resample with replacement?","To mimic drawing fresh samples from the same population."),
  ("Do the two methods agree?","Yes — significant and precisely, stably estimated.")],
 [("Bootstrap gives?","A confidence interval."),("Permutation gives?","A p-value."),("CI vs null?","Excludes the null region."),
  ("Resample how?","With replacement."),("Agreement?","Both confirm the effect."),("Report estimate with?","An interval.")],
 ["Resample members with replacement.","Recompute the statistic.","Read the 95% interval.","Compare to the null."]),
13:E("confirm a predicted negative: same-tag sūras share no theme (root similarity within ≈ cross, p≈0.27).",
 [("State the content result.","Within-family root similarity ≈ cross-family; label-permutation p≈0.27."),
  ("Why is a predicted negative strong?","A pointer should NOT describe; no content link is the model confirmed."),
  ("Overall within vs cross cosine?","0.723 vs 0.689 — a whisker, reproducible by random regrouping."),
  ("Are distinctive roots a theme?","No — كتب, قتل, موت are illustrative flavor, not a validated theme."),
  ("Header vs theme?","Many sūras open on 'the Book' (a header), but bodies do not cluster by tag.")],
 [("Content-link p?","≈0.27 (none)."),("Within vs cross cosine?","0.723 vs 0.689."),("Distinctive roots?","Flavor, not theme."),
  ("Why is a negative informative?","It is the pointer model's prediction confirmed."),("Header = theme?","No."),("Verdict?","No per-tag theme.")],
 ["Build root profiles.","Compare within vs cross similarity.","Run the label-permutation null.","Read p≈0.27."]),
14:E("dissect the frequency false positive: spectacular within-chapter, zero under the cross-chapter baseline (0/29).",
 [("Recount the frequency refutation.","Within-chapter p≤0.001 (illusory); cross-chapter 0/29; Fisher χ²=60.6/df58 (n.s.)."),
  ("Why does the within-null mislead?","It only asks whether common letters are common."),
  ("What is the right question?","Are the letters MORE frequent than in OTHER sūras? Answer: no."),
  ("Which letter barely passes per-letter?","Only م (mim), at ~1.13× — a common-letter effect."),
  ("State the portable lesson.","Beat NORMAL, not just random; the baseline dissolves the false positive.")],
 [("Within-chapter p?","≤0.001 (illusory)."),("Cross-chapter result?","0/29 significant."),("Fisher omnibus?","χ²=60.6/df58 (n.s.)."),
  ("Only letter to pass?","م, barely."),("Why ا,ل,م frequent?","Commonest Arabic letters."),("Lesson?","Beat normal, not just random.")],
 ["Run the within-chapter test (looks great).","Switch to cross-chapter baseline.","Watch enrichment fall to ~1.0×.","Check the Fisher omnibus."]),
15:E("present the one honest content lead: single-letter ق (Sūrat Qāf) ranks 111/114 — real but borderline after correction.",
 [("State the single-letter result.","ق in Sūrat Qāf ranks 111/114 in its own letter (top 3.5%); ن in al-Qalam 105/114."),
  ("Why are single letters the cleanest test?","One letter = one hypothesis, with no multi-letter common-letter confound."),
  ("What happens after correction?","ق's p (≈0.035 raw) becomes borderline; held as a hypothesis, not asserted."),
  ("Do the families show this?","No — any real letter effect is single-letter only, not in the families."),
  ("What would settle it?","An external Arabic acrostic baseline and a cleaner-orthography re-run.")],
 [("ق rank?","111/114 (top 3.5%)."),("ن rank?","105/114."),("ق raw p?","≈0.035."),
  ("After correction?","Borderline."),("Cleanest test why?","No common-letter confound."),("To confirm?","External Arabic baseline.")],
 ["Rank each single-letter sūra by its letter's density.","Apply multiple-comparison correction.","Inspect Sūrat Qāf (50:1).","Consider the external baseline."]),
16:E("two forward threads: boundary variants (المص, المر) and the sūra-family network — a bridge to the corpus-graph course.",
 [("Where do mixed tags sit?","المص (7) between ALM and ALR; المر (13) inside the ALR run — at family boundaries."),
  ("What is the boundary-variant hypothesis?","Mixed tags may mark transitions/variants — a structural observation, not yet tested."),
  ("What does the family network look like?","Four tight cliques (families) plus nine isolated singletons; block-diagonal adjacency."),
  ("What does high modularity mean?","Tag-defined communities are far more separated than a random partition (≈0.62 vs ≈0.08)."),
  ("Why a graph view?","Reframing sūras as nodes and shared structure as edges is the productive next object.")],
 [("المص position?","Sūra 7 (between ALM and ALR)."),("المر position?","Sūra 13 (inside ALR)."),("Network structure?","Cliques + isolates."),
  ("Modularity (tag vs random)?","≈0.62 vs ≈0.08."),("Boundary variants — status?","Hypothesis, not tested."),("Next object?","The corpus graph.")],
 ["Build the same-tag network.","Measure modularity.","Locate المص and المر bridges.","Sketch added edge types."]),
17:E("state the validated pointer model, separate new from known, and chart next steps.",
 [("State the pointer model in one sentence.","A disjoint-letter opening is a pointer tagging a family of sūras coherent in position and time and flagged as long, while carrying no shared content."),
  ("List the affirmations and denials.","Affirm: muṣḥaf contiguity, nuzūl contiguity, long-sūra flag, family integrity. Deny: shared theme (0.27), shared length per tag (0.29), frequency code (0/29)."),
  ("Separate new from known.","Known: the families, mostly Meccan/long. New: label-permutation validation, quantified nuzūl-contiguity, long-sūra flag — over all 29."),
  ("How does this fit the program?","Biology (order), signal (refrains), disjoint letters (contiguity) → latent structure is relational, not content."),
  ("Name the top next steps.","External Arabic baseline for single letters; formal boundary-variant test; the 2-D corpus-graph view.")],
 [("Pointer model, one line?","Tags that group sūras by position/time, flag length, no content."),("Affirmations?","muṣḥaf + nuzūl contiguity, long flag, family integrity."),
  ("Denials?","No theme (0.27), no per-tag length (0.29), no frequency code (0/29)."),("Program conclusion?","Latent structure is relational."),
  ("Biggest limitation?","No external Arabic baseline."),("Next step?","External corpus; boundary variants; graph view.")],
 ["Run the full model on a family.","Contiguity + length + phase.","Content + frequency (null).","Export the validated summary."]),
}
def kit(lec):
    pfx="%02d"%lec; t=TT[lec]; k=K[lec]
    d=newdoc("Disjoint Letters · L%d · Instructor Script"%lec)
    P(d,[("Disjoint Letters — Lecture %d: %s"%(lec,t),True)],size=19,color=ACCENT,after=2)
    P(d,[("Instructor Script · 17-lecture course · root anchor · label-permutation discipline",True)],size=12,color=TEAL,after=6)
    P(d,[("Goal: ",True),(k["goal"],False)],after=8)
    H(d,"0:00–0:25  The idea & framing"); P(d,"Open on the lecture's question and the program context (content failed; test organization). Anchor on the root; all figures from Book6.xlsx.")
    H(d,"0:25–1:00  The core content"); P(d,"Develop the main result with the actual sūras and the relevant charts. Worked anchor where apt: the Ḥawāmīm (حمٓ 40–46, revealed 60–66).")
    H(d,"1:10–1:55  Validation & negatives"); P(d,"Beat the right null, beat the baseline, and report predicted negatives as carefully as positives. Demo the app live.")
    H(d,"2:35–3:00  Audit, discussion & takeaway"); P(d,"Close with ✓/✗/~, the discussion questions, and the takeaway. State new-vs-known honestly.")
    P(d,[("Provenance: ",True),("all figures from Book6.xlsx (6,236 āyāt; 29 muqaṭṭaʿāt sūras); label-permutation null, 50,000 permutations, fixed seed.",False)],color=ACCENT,before=6)
    d.save(os.path.join(OUT,pfx+"_Instructor_Script.docx"))
    d=newdoc("Disjoint Letters · L%d · Exercise"%lec); P(d,[("Lecture %d — Exercise"%lec,True)],size=19,color=ACCENT,after=2); P(d,[(t,True)],size=12,color=TEAL,after=6)
    for i,(q,a) in enumerate(k["tasks"],1): H(d,"Task %d"%i); P(d,q)
    H(d,"Reflection"); P(d,"In 3–4 sentences: what does this lecture's result show, and how would you prove it is real (null, baseline, read-back)?")
    d.save(os.path.join(OUT,pfx+"_Exercise.docx"))
    d=newdoc("Disjoint Letters · L%d · Exercise — Answer Key"%lec); P(d,[("Lecture %d — Exercise · Answer Key"%lec,True)],size=19,color=ACCENT,after=2)
    for i,(q,a) in enumerate(k["tasks"],1): H(d,"Task %d"%i); P(d,a)
    d.save(os.path.join(OUT,pfx+"_Exercise_Answer_Key.docx"))
    d=newdoc("Disjoint Letters · L%d · Quiz"%lec); P(d,[("Lecture %d — Quiz"%lec,True)],size=19,color=ACCENT,after=2); P(d,[(t,True)],size=12,color=TEAL,after=6)
    for i,(q,a) in enumerate(k["quiz"],1): P(d,"%d. %s"%(i,q),after=6)
    d.save(os.path.join(OUT,pfx+"_Quiz.docx"))
    d=newdoc("Disjoint Letters · L%d · Quiz — Answer Key"%lec); P(d,[("Lecture %d — Quiz · Answer Key"%lec,True)],size=19,color=ACCENT,after=2)
    for i,(q,a) in enumerate(k["quiz"],1): P(d,[("%d. "%i,True),(a,False)],after=6)
    d.save(os.path.join(OUT,pfx+"_Quiz_Answer_Key.docx"))
    d=newdoc("Disjoint Letters · L%d · App & Plot Guide"%lec); P(d,[("Lecture %d — App & Plot Guide"%lec,True)],size=19,color=ACCENT,after=2); P(d,[("Using the pointer explorer",True)],size=12,color=TEAL,after=6)
    H(d,"Live app tasks")
    for b in k["app"]: bullet(d,b)
    P(d,[("Tip: ",True),("examples illustrate; always validate against the label-permutation null and read results back to the actual sūras.",False)],color=ACCENT,before=6)
    d.save(os.path.join(OUT,pfx+"_App_and_Plot_Guide.docx"))
    return 6
tot=sum(kit(l) for l in range(1,18)); print("DL kit docx:",tot)

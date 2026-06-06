# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from _dochelper import newdoc,P,H,bullet,ACCENT,TEAL,GREY
OUT=os.path.abspath(os.path.join(HERE,".."))
FN={1:"01_Introduction_DL",2:"02_Method_DL",3:"03_Contiguity_DL",4:"04_Long_and_Phase_DL",5:"05_Not_Content_DL",6:"06_Synthesis_DL"}
TT={1:"Introduction — the pointer hypothesis",2:"The Method — the label-permutation null",3:"Contiguity — the core result",4:"Long-Sūra Flag & Revelation Phase",5:"What It Is NOT — content & the false positive",6:"Synthesis — the pointer model"}
K={
1:dict(goal="introduce the disjoint letters and the falsifiable hypothesis that they are POINTERS — tags that group and place sūras, not content to decode.",
 tasks=[("List the four multi-member disjoint-letter families and their sūra numbers.","حمٓ (40–46), الٓمٓ (2,3,29–32), الٓرٓ (10–15), طسٓمٓ (26,28)."),
  ("State the pointer hypothesis in one sentence.","A disjoint-letter opening is a reference/tag that groups a family of related sūras and marks where they sit, without describing their content."),
  ("Why is 'what do they mean?' the wrong question?","It treats the letters as a content code; a thousand years of that has not resolved them. 'What do they organize?' is testable and does."),
  ("What does a pointer predict that a content code does not?","Grouping (contiguity), possibly magnitude marking, and crucially NO shared theme."),
  ("Give the library analogy and what it predicts.","A call number groups and places a book without summarizing it — so same-tag sūras should cluster but NOT share content.")],
 quiz=[("How many sūras open with disjoint letters?","29."),("Name the four multi-member families.","حمٓ, الٓمٓ, الٓرٓ, طسٓمٓ."),
  ("Pointer vs content code — one line.","A pointer references/groups; a code describes. The letters behave like pointers."),
  ("Why look at organization not content here?","The signal study showed verse content is generic to Arabic; only organization survived."),
  ("What is the anchor unit?","The root (ریشه)."),
  ("One thing the course will NOT claim.","A hidden code, number-miracle, or secret meaning.")],
 app=["Enter a disjoint-letter sūra (e.g. 40); see its family.","View the family on muṣḥaf and nuzūl timelines.","Note the حمٓ block (40–46).","Preview the label-permutation null."]),
2:dict(goal="install the testing discipline: why the label-permutation null (not a random-chapter baseline) is decisive, and how the famous frequency claim is a false positive.",
 tasks=[("Why is a random-chapter baseline misleading here?","Muqaṭṭaʿāt sūras cluster anyway (mostly Meccan, long), so any grouping of them looks clustered."),
  ("Describe the label-permutation null.","Freeze the 29 sūras; shuffle only which tag each gets; ask if the real tagging groups better than random relabeling."),
  ("Tell the frequency false-positive story.","Within-chapter, الٓمٓ letters rank top (p≤0.001); cross-chapter, they are no more frequent than in other chapters (0/29). ا,ل,م are just common."),
  ("State the general lesson.","Beat NORMAL, not just random; the cross-chapter/natural-language baseline is mandatory."),
  ("Why correct for many tests?","Tags × orderings × statistics is a large search; some sparkle by luck. Use FDR; declare tests first.")],
 quiz=[("The decisive null is?","Label-permutation over the 29 fixed sūras."),("Why not random chapters?","They cluster anyway; that conflates background with the tag effect."),
  ("Frequency claim: within vs cross result?","Within p≤0.001 (illusory); cross 0/29 (refuted)."),
  ("Why is ا,ل,م frequent everywhere?","They are the commonest Arabic letters."),
  ("Beat random or beat normal?","Beat normal."),("A method that can say no is?","Trustworthy when it says yes.")],
 app=["Toggle random-chapter vs label-permutation null.","Set 50,000 draws.","Run the frequency test within- then cross-chapter.","Watch the false positive collapse."]),
3:dict(goal="present the core validated result: same-tag sūras are contiguous in muṣḥaf AND revelation order at p=2×10⁻⁵.",
 tasks=[("State the contiguity result and its null.","Specific tag predicts contiguity in muṣḥaf and nuzūl order, p=2×10⁻⁵, under the label-permutation null."),
  ("Give the Ḥawāmīm in both orderings.","حمٓ = sūras 40–46 (muṣḥaf); revealed slots 60–66 (seven consecutive)."),
  ("Why do two independent orderings matter?","Agreement in book-order and revelation-order (independent) makes the result robust."),
  ("Quote per-family p-values.","حمٓ, الٓرٓ p≈0; الٓمٓ 0.009/0.004; طسٓمٓ 0.034."),
  ("What caveat attaches to the nuzūl result?","Revelation order is a reconstruction; the nuzūl claim inherits its uncertainty (the muṣḥaf result does not).")],
 quiz=[("Contiguity p-value (both orders)?","2×10⁻⁵."),("Ḥawāmīm muṣḥaf sūras?","40–46."),("Ḥawāmīm nuzūl slots?","60–66 (consecutive)."),
  ("الٓرٓ sūras?","10–15."),("Why label-permutation?","To isolate the specific-tag effect from background clustering."),
  ("Two orderings give?","Two independent confirmations.")],
 app=["Pick حمٓ; see 40–46 and 60–66.","Shuffle tags; watch clustering dissolve.","Check each family's p.","Compare muṣḥaf vs nuzūl."]),
4:dict(goal="show the two further organizational layers: the tags flag the long sūras, and tag-type tracks revelation phase.",
 tasks=[("State the long-sūra result.","Disjoint-letter sūras median 85 verses vs 26 (means 95 vs 41), p=2×10⁻⁵."),
  ("Is length a per-tag or set property?","A set property; same-tag sūras are NOT length-matched (label-permutation p=0.29)."),
  ("Describe the revelation-phase mapping.","Single/short tags early-Meccan; big families late-Meccan; الٓمٓرٓ the lone Medinan."),
  ("Where do the mixed tags sit?","الٓمٓرٓ inside the الٓرٓ block (sūra 13); الٓمٓصٓ between الٓمٓ and الٓرٓ (sūra 7)."),
  ("How strong is tag-complexity vs time?","Spearman ρ=0.33, p=0.08 — suggestive, not significant.")],
 quiz=[("Median length: disjoint vs rest?","85 vs 26."),("Long-sūra p-value?","2×10⁻⁵."),("Per-tag length similarity p?","0.29 (none)."),
  ("الٓمٓرٓ phase?","Medinan (lone)."),("Boundary variants?","الٓمٓرٓ inside الٓرٓ; الٓمٓصٓ between."),("Tag-complexity vs time?","ρ=0.33, p=0.08.")],
 app=["Compare disjoint vs other lengths.","Color families by revelation phase.","Check per-tag length spread.","See الٓمٓرٓ inside الٓرٓ."]),
5:dict(goal="confirm the model by its predicted negatives: no shared content (p=0.27) and the refuted frequency claim (0/29).",
 tasks=[("State the content result.","Same-tag sūras are not more root-similar than a random regrouping: label-permutation p=0.27."),
  ("Why is a predicted negative strong evidence?","A pointer should NOT describe; finding no content link is the model's prediction confirmed."),
  ("Distinguish shared opening from shared theme.","Many open on the Book (a header), but their bodies do not cluster by tag (header ≠ theme)."),
  ("Recount the frequency refutation.","Within-chapter p≤0.001 (illusory); cross-chapter 0/29, mean diff +0.02 (refuted)."),
  ("State the portable lesson.","Beat NORMAL, not just random; the cross-chapter baseline dissolves the false positive.")],
 quiz=[("Content-link p?","0.27 (none)."),("Within vs cross cosine?","≈0.72 ≈ 0.69."),("Frequency claim cross-chapter?","0/29 significant."),
  ("Shared opening = shared theme?","No."),("Why is a negative informative?","It is the pointer model's prediction confirmed."),("Beat random or normal?","Normal.")],
 app=["Group by tag; check content cluster (fails).","Run frequency within- then cross-chapter.","Watch 0/29.","Compare header vs body similarity."]),
6:dict(goal="state the validated pointer model formally, separate new from known, and chart next steps.",
 tasks=[("State the pointer model in one sentence.","A disjoint-letter opening is a pointer tagging a family of sūras coherent in position, time, and magnitude, while carrying no shared content."),
  ("List the four affirmations and the denials.","Affirm: muṣḥaf contiguity, nuzūl contiguity, long-sūra flag, family integrity. Deny: shared content, frequency code."),
  ("Separate new from known.","Known: the families, mostly-Meccan, mostly-long. New: label-permutation validation, nuzūl quantification, frequency refutation, the pointer framing."),
  ("How does this fit the wider program?","Biology (shared grammar), signal (content generic), disjoint letters (organization real) → latent structure is relational."),
  ("Name the top next step.","Acquire an external Arabic corpus to test whether the grouping is unusual.")],
 quiz=[("Pointer model, one line?","Tags that group sūras by position/time/magnitude, no content."),("Four affirmations?","muṣḥaf + nuzūl contiguity, long flag, family integrity."),
  ("Two denials?","No shared content (0.27); no frequency code (0/29)."),("Program conclusion?","Latent structure is relational, not content."),
  ("Biggest limitation?","No external Arabic baseline."),("Next step?","External corpus; then boundary variants.")],
 app=["Run the full model on a family.","Contiguity + length + phase.","Content + frequency (null).","Export the validated summary."]),
}
def kit(lec):
    pfx="%02d"%lec; t=TT[lec]; k=K[lec]
    d=newdoc("Disjoint Letters · L%d · Instructor Script"%lec)
    P(d,[("Disjoint Letters — Lecture %d: %s"%(lec,t),True)],size=19,color=ACCENT,after=2)
    P(d,[("Instructor Script · focused unit · root anchor · label-permutation discipline",True)],size=12,color=TEAL,after=6)
    P(d,[("Goal: ",True),(k["goal"],False)],after=8)
    H(d,"0:00–0:25  The idea & framing"); P(d,"Open on the pointer hypothesis and the program context (content failed; test organization). Anchor on the root; figures from Book6.xlsx.")
    H(d,"0:25–1:00  The core content"); P(d,"Develop the lecture's main result with the actual sūras and the label-permutation null. Worked anchor: the Ḥawāmīm (حمٓ 40–46, revealed 60–66).")
    H(d,"1:10–1:55  Validation & negatives"); P(d,"Beat the right null, beat the baseline, and report the predicted negatives as carefully as the positives. Demo the app live.")
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
tot=sum(kit(l) for l in range(1,7)); print("DL kit docx:",tot)

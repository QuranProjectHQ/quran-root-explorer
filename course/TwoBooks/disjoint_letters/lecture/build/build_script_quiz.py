# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor
ACCENT=RGBColor(0x1F,0x4E,0x79); GREY=RGBColor(0x55,0x55,0x55); CUE=RGBColor(0x8A,0x4B,0x08)

# ============ INSTRUCTOR SCRIPT ============
d=new_doc("Two Books · Disjoint Letters — Instructor Script (v1)")
P(d,[("Two Books · Disjoint Letters — Instructor Lecture Script",True)],size=18,after=2,color=ACCENT)
P(d,"Spoken script, ~35 minutes, mapped to the 20-slide deck and the eight 8-beat modules. Honest spine throughout: the disjoint letters mark a contiguous block of longer, compositionally distinct suras - a positional and organizational pointer that survives the nulls and FDR - while the folkloric cipher claims do not. Every value from Book6; permutation nulls and Benjamini-Hochberg correction throughout. Arrow lines are delivery cues; time markers are cumulative.",size=9.5,after=8,color=GREY)
def marker(t,title): P(d,[(t+"  ",True),(title,True)],size=12,before=10,after=3,color=ACCENT)
def cue(t): P(d,[("> "+t,False)],size=9.5,after=3,color=CUE)
def say(t): P(d,t,size=11,after=5)

marker("0:00","Opening · what the disjoint letters are")
cue("Slides 1-3.")
say("Twenty-nine of the 114 suras open with detached letters - alif-lam-mim, alif-lam-ra, ha-mim, ta-sin-mim - recited one letter at a time. Popular accounts treat them as a hidden cipher. We will do something more disciplined: we will state a falsifiable thesis - that they act as a positional and organizational pointer to a distinct block of suras - and we will test it, alongside the cipher claims, against the corpus. Here is where we land, stated up front: a real geometric signal survives - contiguity, size, composition - while the famous code claims do not. The workbench has three scales: position, sequence, and semantic - where the marked suras sit, how their letters behave, how their roots behave.")

marker("4:00","Method · permutation nulls and FDR")
cue("Slides 4-5. This is the discipline that makes the rest trustworthy.")
say("Two tools. The permutation null: we re-tag 29 random suras thousands of times and rebuild each statistic, so we know what chance alone produces. And Benjamini-Hochberg correction: because we run a whole battery of tests, some will cross p below 0.05 by luck - FDR correction controls that across the battery. This matters enormously here, because a single uncorrected borderline p is exactly how folklore manufactures a miracle. So every result today is reported with its FDR-corrected status, never a lone p.")

marker("8:00","Module 1-2 · the tag, and contiguity")
cue("Slides 6-7.")
say("We tag each sura muqattaat-bearing or not - 29 against 85 - a clean two-group test. The first and strongest question is geometric: do the marked suras cluster together in the order? We measure their contiguity and compare to thousands of random tags of the same size - and we do it in TWO independent orderings, the mushaf order and the revelation, or nuzul, order. The result: contiguity is significant at p about 0.0005 in BOTH orderings. A signal that holds in two independent arrangements is very hard to dismiss as an artefact of one. The marked suras genuinely form a contiguous block.")

marker("13:00","Module 3 · per-family contiguity")
cue("Slide 8.")
say("Does the clustering hold at the family level - the alif-lam-mim family, the ha-mim family, and so on - not just in aggregate? We repeat the contiguity test within each family. Every family is significantly contiguous: ha-mim and alif-lam-ra at about 0.0005, alif-lam-mim at 0.006, ta-sin-mim at 0.035. So the geometry is family-structured, not one lucky run of adjacent suras.")

marker("17:00","Module 4 · the suras are longer")
cue("Slide 9.")
say("Contiguous in position - but are they also distinct in size? Compare the median length of the 29 marked suras to the other 85. The marked suras run about 85 ayahs at the median, against about 26 for the rest - markedly longer. A structural marker that coincides with a structural property like scale is independent evidence the tag points at something real in the architecture.")

marker("21:00","Module 5 · the code claims fail")
cue("Slides 10-11. Predict, then reveal.")
say("Now the attractive claims, the ones honesty requires us to test. First, the famous one: that Surat Qaf, sura 50, is saturated with the letter qaf. Its qaf density is 3.76% - and crucially, that ranks it 111th of 114 suras, not first. Against a permutation null the elevation is p about 0.10 - not significant. The story is appealing and the data simply does not support it. Likewise the thematic-coding claim comes in at p equals 0.049 - borderline, and it does NOT survive FDR - and an embedding-similarity claim sits at about 0.10. None of the cipher claims survive. This is the unlearn: the letters are not a decoded code.")

marker("26:00","Module 6-7 · what IS different - information theory")
cue("Slides 12-13.")
say("So if not a cipher, what IS different about these suras? At the letter scale, the letter-entropy of the marked group differs from the rest at p about 0.002 - they are compositionally distinct, not merely longer. And the distinction persists up a level: at the root scale, root-entropy differs at about 0.0005 and lexical richness at about 0.0005. So the marked suras are a genuinely distinct class at both the letter and the root scale - a multi-scale structural signal, exactly what a real organizational marker should leave behind.")

marker("31:00","Module 8 · synthesis, audit, disclaimer")
cue("Slides 14-18.")
say("Pull it together. What survives the nulls and FDR: contiguity in two orderings, per-family clustering, the size gap of 85 to 26, and compositional distinctness at both letter and root scale. What fails: Qaf saturation, thematic coding, embedding similarity. The whole-battery slide shows it in one picture - six green bars above the line, three red below. The honest reading: al-Muqattaat are a validated positional and organizational pointer to a distinct block of suras - not a letter cipher.")
cue("Slide 16 - say verbatim.")
say("The disclaimer, plainly: the disjoint letters are not a decoded cipher; contiguity is not theology; a borderline uncorrected p is not a finding. We do not claim to know WHY the letters are there - only what measurable structure the tag does and does not predict. The workbench separates a real geometric signal from folklore, with a null behind every answer and FDR across the battery - judged by reproducibility, never offered as proof of intent.")

marker("34:00","Close")
cue("Slides 17-20.")
say("Quick reference is on slide 17 - the terms and the live Book6 numbers. To close: tag the 29 suras and the geometry appears - they cluster, they are longer, they are compositionally distinct - while the cipher claims fall away. A pointer, not a code. Next in the series, Signal and Biology read the same corpus as an ordered signal and a genome; the FDR Summary then collects every Two Books test into one corrected dashboard. See you there.")
d.save(os.path.join(WK,"DisjointLetters_Instructor_Script.docx"))
print("DL script saved | words:",sum(len(p.text.split()) for p in d.paragraphs))

# ============ QUIZ + KEY (rotated) ============
d=new_doc("Two Books · Disjoint Letters — Quiz")
TITLE(d,"Two Books · Disjoint Letters — Quiz",
      "13 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise. Every value is reproducible live from Book6. (Paste into Google Forms.)")
QQ=[
("1.  al-Muqattaat are:","the disjoint letters that open 29 suras",["a list of 29 prophets","the longest 29 suras","a group of root families"],"the detached letters (alif-lam-mim, etc.) opening 29 of the 114 suras."),
("2.  This lecture treats the disjoint letters as:","a positional/organizational pointer to be tested",["a decoded cipher","a proven miracle","random decoration"],"a falsifiable pointer thesis, tested against permutation nulls - not assumed to be a code."),
("3.  The contiguity test asks whether the marked suras:","cluster together in the order, more than chance",["are the most frequent","contain the letter qaf","are all Meccan"],"contiguity = clustering of the 29 tagged suras vs random tags of the same size."),
("4.  Contiguity is significant (p ~ 0.0005) in:","BOTH the mushaf and the nuzul (revelation) orders",["only the mushaf order","only the nuzul order","neither order"],"holding in two independent orderings makes an artefact explanation very hard."),
("5.  Per-family contiguity (HM, ALR, ALM, TSM) shows:","every family clusters significantly",["no family clusters","only HM clusters","families are random"],"HM and ALR ~0.0005, ALM 0.006, TSM 0.035 - all significant."),
("6.  The median length of muqattaat suras vs the rest is about:","85 vs 26 ayahs (they are longer)",["26 vs 85 (they are shorter)","equal","there is no difference"],"marked suras median ~85 ayahs vs ~26 - markedly longer."),
("7.  In Surat Qaf (50), the letter qaf has density 3.76% and ranks:","111th of 114 - and is NOT significant (p ~ 0.10)",["1st - highly significant","50th - borderline","2nd - significant"],"the famous saturation claim fails: rank 111, p ~ 0.10."),
("8.  The thematic-coding claim (p = 0.049) is:","borderline and NOT significant after FDR",["strongly significant","exactly zero","not tested"],"a lone borderline p; Benjamini-Hochberg correction demotes it."),
("9.  Benjamini-Hochberg correction is used because:","running many tests yields chance hits we must control",["it raises every p-value","the app requires it","it proves the cipher"],"FDR controls false discoveries across the battery - the guard against manufactured miracles."),
("10.  The letter-entropy of muqattaat suras differs from the rest at:","p ~ 0.002 (compositionally distinct)",["p ~ 0.5 (no difference)","p = 1.0","it was not measured"],"p ~ 0.002: the marked suras differ in letter information, not only length."),
("11.  At the root scale, the marked suras differ in:","root-entropy AND lexical richness (both ~0.0005)",["neither measure","only richness","only entropy"],"root-entropy ~0.0005 and richness ~0.0005 - the distinction persists up a scale."),
("12.  The overall verdict of the workbench is:","a validated positional/organizational pointer, not a cipher",["a confirmed hidden code","no signal at all","a thematic encoding"],"geometry + size + composition survive; the cipher claims fail."),
("13.  Which statement is LICENSED by the analysis?","the marked suras cluster, are longer, and are compositionally distinct",["the letters encode secret meanings","Surat Qaf is saturated with qaf","the letters predict revelation dates"],"only the survived findings are licensed; the cipher claims are not."),
]
KEY=[]
for qi,(stem,correct,distr,expl) in enumerate(QQ):
    pos=qi%4; opts=list(distr); opts.insert(pos,correct)
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
    KEY.append((str(qi+1),string.ascii_uppercase[pos],expl))
d.save(os.path.join(WK,"DisjointLetters_Quiz.docx")); print("DL quiz saved")

d=new_doc("Two Books · Disjoint Letters — Quiz Answer Key (instructor)")
TITLE(d,"Two Books · Disjoint Letters — Quiz Answer Key (instructor)","One point each, 13 total. Every value reproducible live from Book6.")
H(d,"Answers")
for n,a,ex in KEY: P(d,[(f"{n}.  {a}  ",True),("- "+ex,False)],size=10,after=2)
H(d,"Grading notes")
bullet(d,"Q7, Q8, Q9 are the core 'folklore guard' checks - they confirm the student did NOT accept the cipher claims or a lone borderline p.")
bullet(d,"Q4 (two orderings) and Q10/Q11 (multi-scale composition) verify the genuine, survived findings.")
d.save(os.path.join(WK,"DisjointLetters_Quiz_Answer_Key.docx")); print("DL key saved | letters:",[a for _,a,_ in KEY])

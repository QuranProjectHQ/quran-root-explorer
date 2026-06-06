# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor
ACCENT=RGBColor(0x1F,0x4E,0x79); GREY=RGBColor(0x55,0x55,0x55); CUE=RGBColor(0x8A,0x4B,0x08)

# ===== INSTRUCTOR SCRIPT =====
d=new_doc("Two Books · FDR Summary — Instructor Script (v1)")
P(d,[("Two Books · FDR Summary — Instructor Lecture Script (capstone)",True)],size=18,after=2,color=ACCENT)
P(d,"Spoken script, ~30 minutes, mapped to the 20-slide deck and the eight 8-beat modules. This is the capstone of the Two Books series. Honest spine: under one Benjamini-Hochberg correction across one representative test per domain, 6 of 8 survive 5% FDR - the cross-domain structure is robust - while the borderline shared-theme claim drops out. Crucial caveat: FDR controls for MULTIPLICITY, not the sura-length confound. Every q-value re-runs live on the page. Arrow lines are delivery cues; time markers are cumulative.",size=9.5,after=8,color=GREY)
def marker(t,title): P(d,[(t+"  ",True),(title,True)],size=12,before=10,after=3,color=ACCENT)
def cue(t): P(d,[("> "+t,False)],size=9.5,after=3,color=CUE)
def say(t): P(d,t,size=11,after=5)

marker("0:00","Opening · why a cross-domain summary")
cue("Slides 1-2.")
say("This is the capstone. Across the series we ran many permutation tests - on the disjoint letters, on the corpus as a signal, on the corpus as a genome. The danger now is obvious: if you report only the smallest p from a large pile, you will almost always find one under 0.05, even when nothing is there. So we do the disciplined thing - we gather one representative test from each domain and correct them ALL together, in a single Benjamini-Hochberg pass. The pipeline is simple: each page contributes one test, the shared kernel assembles the eight p-values, one correction runs, and the dashboard reports q-values and survivors.")

marker("4:00","Module 2 · the multiplicity problem")
cue("Slide 3.")
say("Here is the problem in one line. At a 5% threshold, one null test in twenty passes by chance. Run eight, and the chance of at least one false hit climbs far above five percent. That is precisely how folklore manufactures a miracle - run enough comparisons and report the lucky one. Our own battery contains the textbook trap: the shared-theme test lands at p equals 0.049, just under the line. Multiplicity tells us to distrust that until it is corrected.")

marker("8:00","Module 3 · Benjamini-Hochberg")
cue("Slides 4-5.")
say("The fix is Benjamini-Hochberg, which controls the false-discovery rate - the expected fraction of our 'discoveries' that are actually null. Mechanically: rank the m p-values from small to large; the i-th passes if it is below i over m times alpha; the q-value is the smallest alpha at which a test still passes. FDR is the right tool for an exploratory battery - less brutal than Bonferroni, but still a real guard. Look at the ranking slide: ranks one through six sit above their thresholds and pass; rank seven, the theme test, falls below and fails. With eight tests at alpha 0.05, a raw p of 0.0005 becomes a q of 0.0010, while p equals 0.049 becomes q equals 0.056 - now just over the line.")

marker("13:00","Module 4 · the battery")
cue("Slides 6-7.")
say("Now the battery itself - one representative test per domain, eight in all. Position contributes contiguity in two orderings plus a shared-length test; Semantic contributes a shared-theme test and a root-entropy special; Sequence a letter-entropy special; Signal the length autocorrelation; Biology the di-codon adjacency. One well-chosen test per domain, so the correction never double-counts near-identical tests. The raw p-values: contiguity in both orderings, root-entropy, and length autocorrelation all at 0.0005; letter-entropy at 0.002; di-codon at 0.005; shared theme at 0.049; shared length at 0.289.")

marker("17:00","Module 5-6 · survivors and casualties")
cue("Slides 8-10. This is the heart of it.")
say("Apply the correction. Six of eight survive a five percent false-discovery rate: contiguity in both orderings at q 0.0010 each, length autocorrelation at 0.0010, root-entropy at 0.0010, letter-entropy at 0.0032, and di-codon adjacency at 0.0067. One survivor from every domain. And two drop out - and the casualties are the most instructive part. Shared theme: p 0.049 read alone looks like a finding, but q 0.056 in the battery is just over the line, so it is NOT a discovery. Shared length, at p 0.289, was never close. The correction did exactly its job - it demoted the borderline claim that, uncorrected, folklore would have promoted.")
cue("Slide 10 - the anatomy of the borderline. Say it slowly.")
say("Read alone, p equals 0.049 is under 0.05 and looks significant. Read in the battery, q equals 0.056 is over the line and is not a discovery. Same number, honest reading changes once you account for the other seven tests.")

marker("23:00","Module 7 · cross-domain reading")
cue("Slides 11-12.")
say("Step back. The six survivors span two INDEPENDENT orderings - the mushaf order and the revelation order both give significant contiguity - and all three pages plus the Signal and Biology structure tests. Structure that holds across independent readings and across domains is far harder to explain away than any single result. That is the real strength of the capstone: it is not one striking p, it is a coherent, multi-domain pattern that survives one joint correction.")

marker("27:00","Module 8 · synthesis, audit, disclaimer")
cue("Slides 13-14.")
say("The verdict: under one Benjamini-Hochberg correction the Two Books structure is robust - six of eight, one per domain, all q at or below 0.0067 - while the borderline theme claim is correctly excluded. And the caveat that keeps us honest, stated plainly: FDR controls for MULTIPLICITY, not for the sura-length confound that several of these tests share. Surviving the correction means a result is reproducible - it does NOT make it a proof of design or intent.")
cue("Slide 14 - say verbatim.")
say("So we do not claim a miracle. We claim something smaller and sturdier: read together and corrected for multiplicity, the corpus shows real, reproducible, multi-domain structure - and we have flagged exactly what the method cannot rule out.")

marker("30:00","Close")
cue("Slides 15-16.")
say("Quick reference is on slide 15. To close: this is where the Two Books series lands - one corrected dashboard, six robust discoveries, the borderline claim set aside, and every q-value reproducible live on the Global FDR page. Anyone can re-run the whole battery from Book6 and get these same numbers. That is the discipline the whole project was built for.")
d.save(os.path.join(WK,"FDR_Summary_Instructor_Script.docx"))
print("FDR script saved | words:",sum(len(p.text.split()) for p in d.paragraphs))

# ===== QUIZ + KEY =====
d=new_doc("Two Books · FDR Summary — Quiz")
TITLE(d,"Two Books · FDR Summary — Quiz",
      "13 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise. Every value is reproducible live from Book6. (Paste into Google Forms.)")
QQ=[
("1.  The FDR Summary page exists to:","correct one representative test per domain TOGETHER",["run new permutation tests","rank suras by length","replace the other pages"],"it gathers one test per domain and applies a single correction across all of them."),
("2.  The multiplicity problem is that:","running many tests yields some small p's by chance",["p-values are always wrong","the corpus is too small","permutation is biased"],"at alpha 0.05, ~1 in 20 null tests passes by luck; a battery inflates false positives."),
("3.  Benjamini-Hochberg controls:","the false-discovery rate across the battery",["the sura-length confound","the sample size","the permutation count"],"BH controls the expected fraction of 'discoveries' that are actually null."),
("4.  A q-value is:","the smallest alpha at which a test still passes",["the raw p-value","the number of tests","the effect size"],"q is the BH-adjusted threshold, directly comparable to 5%."),
("5.  The battery contains how many representative tests?","8",["3","14","50"],"one representative test per domain, 8 in total."),
("6.  How many survive a 5% false-discovery rate?","6 of 8",["8 of 8","2 of 8","0 of 8"],"6 survive (q <= 0.0067); 2 fail."),
("7.  The shared-theme test has raw p = 0.049. After BH correction its q is:","0.056 - it does NOT survive",["0.0010 - survives","0.049 - unchanged","0.005 - survives"],"q = 0.056 > 0.05: the borderline claim drops out once multiplicity is controlled."),
("8.  Which is the clearest demonstration that the correction works?","the borderline theme claim (p 0.049) is demoted",["all tests survive","no tests survive","the p-values change sign"],"a borderline raw p failing after correction is the guard doing its job."),
("9.  The survivors include contiguity in:","BOTH the mushaf and nuzul orderings",["only the mushaf ordering","only the nuzul ordering","neither"],"both orderings survive at q 0.0010 - the strongest, two-reading signal."),
("10.  Shared length per tag (p = 0.289) is:","never close to significant",["a strong discovery","borderline","exactly 0.05"],"p = 0.289 is well inside the null; it fails clearly."),
("11.  The crucial caveat about FDR is that it does NOT:","correct for the sura-length confound",["control multiplicity","produce q-values","rank the tests"],"FDR controls multiplicity only; the shared length confound is a separate issue."),
("12.  Surviving 5% FDR means a result is:","reproducible - not a proof of intent",["proof of design","a miracle","caused by length"],"survival = reproducible structure, never evidence of purpose."),
("13.  The survivors span:","every Two Books domain (Position, Sequence, Semantic, Signal, Biology)",["only Position","only Biology","only Signal"],"one survivor from each domain - the cross-domain robustness."),
]
KEY=[]
for qi,(stem,correct,distr,expl) in enumerate(QQ):
    pos=qi%4; opts=list(distr); opts.insert(pos,correct)
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
    KEY.append((str(qi+1),string.ascii_uppercase[pos],expl))
d.save(os.path.join(WK,"FDR_Summary_Quiz.docx")); print("FDR quiz saved")

d=new_doc("Two Books · FDR Summary — Quiz Answer Key (instructor)")
TITLE(d,"Two Books · FDR Summary — Quiz Answer Key (instructor)","One point each, 13 total. Every value reproducible live from Book6.")
H(d,"Answers")
for n,a,ex in KEY: P(d,[(f"{n}.  {a}  ",True),("- "+ex,False)],size=10,after=2)
H(d,"Grading notes")
bullet(d,"Q7 and Q8 are the core 'correction-works' checks; Q11 and Q12 are the caveat checks (multiplicity != confound; survival != proof).")
bullet(d,"Q6, Q9, Q13 verify the headline result and its cross-domain spread.")
d.save(os.path.join(WK,"FDR_Summary_Quiz_Answer_Key.docx")); print("FDR key saved | letters:",[a for _,a,_ in KEY])

# ===== WORKED EXAMPLE =====
d=new_doc("Two Books · FDR Summary — Worked Example")
TITLE(d,"Two Books · FDR Summary — Worked Example: correcting the battery by hand",
      "The eight tests, ranked and corrected step by step, with live Book6 numbers. The skill: read a q-value, not a raw p, and see why p = 0.049 is not a discovery.")
H(d,"Step 1 — Collect the battery (raw p, ascending)",size=13)
table(d,[["rank i","test","raw p"],
         ["1","Contiguity · muṣḥaf","0.0005"],
         ["2","Contiguity · nuzūl","0.0005"],
         ["3","Length autocorrelation","0.0005"],
         ["4","Root-entropy","0.0005"],
         ["5","Letter-entropy","0.002"],
         ["6","Di-codon adjacency","0.005"],
         ["7","Shared theme","0.049"],
         ["8","Shared length","0.289"]])
H(d,"Step 2 — The BH threshold for each rank: (i / m) × α, with m = 8, α = 0.05",size=13)
bullet(d,"rank 6 threshold = (6/8)×0.05 = 0.0375 — di-codon p 0.005 < 0.0375 → passes.")
bullet(d,"rank 7 threshold = (7/8)×0.05 = 0.0438 — shared theme p 0.049 > 0.0438 → FAILS.")
bullet(d,"rank 8 threshold = (8/8)×0.05 = 0.05 — shared length p 0.289 ≫ 0.05 → fails.")
H(d,"Step 3 — Read the q-values",size=13)
table(d,[["test","raw p","BH q","5% FDR"],
         ["Contiguity · muṣḥaf","0.0005","0.0010","✓"],
         ["Contiguity · nuzūl","0.0005","0.0010","✓"],
         ["Length autocorrelation","0.0005","0.0010","✓"],
         ["Root-entropy","0.0005","0.0010","✓"],
         ["Letter-entropy","0.002","0.0032","✓"],
         ["Di-codon adjacency","0.005","0.0067","✓"],
         ["Shared theme","0.049","0.056","✗"],
         ["Shared length","0.289","0.289","✗"]])
H(d,"Step 4 — Report: one fact + one labelled reading",size=13)
P(d,[("Fact:  ",True),("of 8 representative tests, 6 survive a 5% false-discovery rate (q ≤ 0.0067), one from every domain; shared theme fails (p 0.049 → q 0.056) and shared length fails (p 0.289).",False)])
P(d,[("Interpretation (labelled):  ",True),("I read the corpus as showing robust, reproducible, multi-domain structure; the borderline theme claim is set aside. FDR fixes multiplicity, not the length confound — this is reproducibility, not proof of intent.",False)])
d.save(os.path.join(WK,"FDR_Summary_Worked_Example.docx")); print("FDR worked example saved")

# ===== QUICK REFERENCE =====
d=new_doc("Two Books · FDR Summary — Quick Reference (1 page)")
TITLE(d,"Two Books · FDR Summary — Quick Reference (1 page)","The capstone dashboard at a glance. Keep this beside the app.")
H(d,"The app in 3 steps",size=13)
bullet(d,"Open Two Books → 📋 Global FDR. Click 'Run the full battery + BH-FDR'.")
bullet(d,"Read the q-value column (not the raw p) against the 5% line.")
bullet(d,"Note the survivor count and which domain each survivor comes from.")
H(d,"The method",size=13)
bullet(d,[("Multiplicity",True),(" — running many tests inflates false positives.",False)])
bullet(d,[("False-discovery rate",True),(" — expected fraction of 'discoveries' that are null.",False)])
bullet(d,[("Benjamini–Hochberg",True),(" — rank p's; the i-th passes if p < (i/m)×α.",False)])
bullet(d,[("q-value",True),(" — smallest α at which a test still passes; compare to 0.05.",False)])
H(d,"Read honestly",size=13)
bullet(d,"DO read q-values, never a lone raw p from a battery.")
bullet(d,"DON'T promote a borderline result (theme p 0.049 → q 0.056 fails).")
bullet(d,"DON'T treat FDR as a fix for the sūra-length confound, or survival as proof.")
H(d,"Anchor numbers",size=13)
bullet(d,"8 tests · 6 survive 5% FDR · survivors q ≤ 0.0067 · contiguity 0.0005 → q 0.0010 (both orderings) · theme 0.049 → q 0.056 (fails) · length 0.289 (fails).")
H(d,"Honest spine",size=13)
P(d,"One correction across all domains: robust, multi-domain, reproducible structure; the borderline theme claim excluded. FDR controls multiplicity, not the length confound — never proof of intent.",size=10)
d.save(os.path.join(WK,"FDR_Summary_Quick_Reference.docx")); print("FDR quick-ref saved")

# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK

def mod(d,n,title,beats):
    H(d,f"Module {n} — {title}",size=13)
    for lbl,txt in beats: P(d,[(lbl+": ",True),(txt,False)],size=10.5)

d=new_doc("Two Books · FDR Summary — Lecture Notes")
TITLE(d,"Two Books · FDR Summary — Lecture Notes",
      "The capstone: one Benjamini-Hochberg correction across one representative permutation test from "
      "every Two Books domain, so no single p-value is read in isolation. Every module carries the eight "
      "beats; beat 6 is a real Book6 number. Honest spine: after correction the cross-domain structure is "
      "robust - 6 of 8 tests survive 5% FDR - while the borderline shared-theme claim correctly drops out. "
      "Crucial caveat: FDR controls for MULTIPLICITY, not for the sura-length confound.")

mod(d,1,"Frame - why a cross-domain summary",[
 ("What it is","a single dashboard that gathers one representative test from each Two Books domain - Disjoint Letters, Signal, Biology - and corrects them together."),
 ("Why we do it","because reporting the best p from a large battery is exactly how a chance result is mistaken for a discovery; the summary refuses to read any p alone."),
 ("How it's done","collect the battery, then apply one Benjamini-Hochberg correction across ALL of them at once."),
 ("What we get","a q-value per test and a single count of how many survive a 5% false-discovery rate."),
 ("Why it matters","it turns a pile of separate claims into one disciplined verdict the whole series can stand on."),
 ("In the data","the battery holds 8 representative tests spanning Position, Sequence, Semantic, Signal and Biology - all computed live from Book6."),
 ("Takeaway","the capstone reads the whole Two Books battery together, never one p at a time."),
 ("Bridge","first, the problem the correction solves: multiplicity."),
])

mod(d,2,"The multiplicity problem",[
 ("What it is","the fact that running many independent tests produces some small p-values by chance alone."),
 ("Why we do it","to see why an uncorrected 0.05 threshold is unsafe across a battery."),
 ("How it's done","reason it through: at a 5% threshold, 1 in 20 null tests will 'pass' by luck; run 8 and the chance of at least one false hit is far above 5%."),
 ("What we get","an appreciation that the more tests we run, the more guard we need."),
 ("Why it matters","without a correction, a series with many tests can always manufacture a 'finding' - the engine of pseudo-miracles."),
 ("In the data","our battery runs 8 tests; the shared-theme test lands at p = 0.049 - the textbook borderline result that multiplicity should make us distrust."),
 ("Takeaway","run enough tests and chance alone will hand you a significant p; correction is not optional."),
 ("Bridge","the correction we use is Benjamini-Hochberg."),
])

mod(d,3,"Benjamini-Hochberg - how FDR works",[
 ("What it is","a procedure that controls the false-discovery rate - the expected fraction of 'discoveries' that are actually null."),
 ("Why we do it","FDR is the right control for an exploratory battery: it is less brutal than Bonferroni yet still guards against multiplicity."),
 ("How it's done","rank the m p-values ascending; the i-th passes if it is below (i/m) x alpha; the q-value is the smallest alpha at which a test still passes."),
 ("What we get","a q-value for every test, directly comparable to the 5% threshold."),
 ("Why it matters","q-values let us read the whole battery on one honest scale, instead of a raw p that ignores the others."),
 ("In the data","with 8 tests at alpha = 0.05, a raw p of 0.0005 becomes q = 0.0010, while the borderline p = 0.049 becomes q = 0.056 - now just over the line."),
 ("Takeaway","BH-FDR converts each raw p into a q-value that already accounts for the whole battery."),
 ("Bridge","now meet the battery itself."),
])

mod(d,4,"The battery - one test per domain",[
 ("What it is","the eight representative tests: contiguity in two orderings, shared length and shared theme per tag, letter- and root-entropy specials, length autocorrelation, and di-codon adjacency."),
 ("Why we do it","one well-chosen test per domain keeps the correction honest - it does not double-count near-identical tests."),
 ("How it's done","each test compares an observed statistic to a permutation null and returns one p; the page assembles them through the shared stats kernel."),
 ("What we get","eight raw p-values spanning Position (Disjoint Letters), Sequence, Semantic, Signal and Biology."),
 ("Why it matters","spanning every domain means the corrected verdict speaks for the whole Two Books project, not one page."),
 ("In the data","raw p's: contiguity mushaf 0.0005, contiguity nuzul 0.0005, length autocorrelation 0.0005, root-entropy 0.0005, letter-entropy 0.002, di-codon 0.005, shared theme 0.049, shared length 0.289."),
 ("Takeaway","the battery is one representative, permutation-tested claim from each domain."),
 ("Bridge","apply BH-FDR and see who survives."),
])

mod(d,5,"The survivors",[
 ("What it is","the tests that clear the 5% false-discovery rate after correction."),
 ("Why we do it","to state what the whole series robustly supports."),
 ("How it's done","read each q-value against 0.05; keep those at or below it."),
 ("What we get","the corrected list of discoveries."),
 ("Why it matters","these are the claims that survive the strictest cross-domain test we apply - the backbone of the project."),
 ("In the data","6 of 8 survive: contiguity in both orderings (q 0.0010 each), length autocorrelation (q 0.0010), root-entropy (q 0.0010), letter-entropy (q 0.0032), and di-codon adjacency (q 0.0067)."),
 ("Takeaway","six discoveries survive 5% FDR, one from every Two Books domain."),
 ("Bridge","and two do not - the casualties are just as instructive."),
])

mod(d,6,"The casualties",[
 ("What it is","the tests that fail once multiplicity is controlled."),
 ("Why we do it","because what DROPS OUT is the clearest demonstration that the correction is working."),
 ("How it's done","the same q-vs-0.05 reading, now landing above the line."),
 ("What we get","an honest record of claims we decline to keep."),
 ("Why it matters","a borderline raw p that fails after correction is exactly the kind of claim folklore would have promoted - and we do not."),
 ("In the data","shared theme per tag: p = 0.049 -> q = 0.056, just over the line, so NOT a discovery; shared length per tag: p = 0.289, never close. Both correctly drop out."),
 ("Takeaway","the borderline theme claim does not survive FDR - the correction does its job."),
 ("Bridge","step back: what does the surviving set say across domains?"),
])

mod(d,7,"Cross-domain reading",[
 ("What it is","the interpretation of the six survivors taken together."),
 ("Why we do it","to read the project as a whole rather than page by page."),
 ("How it's done","note that the survivors span two independent orderings (contiguity) and all three pages (Position, Sequence, Semantic + the Signal and Biology structure tests)."),
 ("What we get","a single, multi-domain statement of what the corpus robustly shows."),
 ("Why it matters","structure that survives across independent readings and domains is far harder to explain away than any single result."),
 ("In the data","survivors come from Position (contiguity, two orderings), Signal (length autocorrelation), Sequence (letter-entropy), Semantic (root-entropy), and Biology (di-codon) - every domain represented."),
 ("Takeaway","the corpus shows robust, multi-domain structure - geometric, compositional, and sequential - that survives one joint correction."),
 ("Bridge","the synthesis states the caveat that keeps this honest."),
])

mod(d,8,"Synthesis - one corrected dashboard",[
 ("What it is","the combined verdict of the whole Two Books series under one Benjamini-Hochberg correction."),
 ("Why we do it","to state plainly what the project licenses - and the one thing FDR does NOT fix."),
 ("How it's done","report the survivor count and q-values, then name the limit of the method."),
 ("What we get","one defensible sentence: robust cross-domain structure, with the borderline theme claim correctly excluded."),
 ("Why it matters","it inoculates the whole series against both over-reading and a false sense of proof."),
 ("In the data","6 of 8 survive 5% FDR (q <= 0.0067); theme fails (q 0.056); CRUCIAL CAVEAT - FDR controls for MULTIPLICITY, not for the sura-length confound, and a surviving test is reproducible, not a miracle."),
 ("Takeaway","under one honest correction the Two Books structure is robust across domains - a reproducible finding, never a proof of intent."),
 ("Bridge","this closes the Two Books series; the live page lets anyone re-run the whole battery and reproduce every q-value."),
])

out=os.path.join(WK,"FDR_Summary_Lecture_Notes.docx")
d.save(out); print("FDR notes built:",out)

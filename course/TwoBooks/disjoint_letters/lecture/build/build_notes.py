# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
TB=json.load(open(os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json"),encoding="utf-8"))

def mod(d,n,title,beats):
    H(d,f"Module {n} — {title}",size=13)
    for lbl,txt in beats:
        P(d,[(lbl+": ",True),(txt,False)],size=10.5)

d=new_doc("Disjoint Letters — Lecture Notes")
TITLE(d,"Two Books · Disjoint Letters — Lecture Notes",
      "Reading al-Muqattaat (the disjoint letters that open 29 suras) as a positional pointer and "
      "organizational marker - not a hidden code. Every module carries the eight beats; beat 6 is a real "
      "Book6 number computed by the app's engine. Honest spine: a validated geometric signal "
      "(contiguity + size + composition) survives the nulls and FDR, while the folkloric code claims do "
      "not. Permutation nulls + Benjamini-Hochberg correction throughout; no miracle claims.")

mod(d,1,"Frame - the disjoint letters as a pointer",[
 ("What it is","al-Muqattaat are the detached letters (e.g. الم, الر, حم) that open 29 of the 114 suras, recited letter by letter."),
 ("Why we do it","popular accounts treat them as a cipher; we instead test a falsifiable thesis - that they act as a POSITIONAL/organizational pointer to a distinct block of suras - against the corpus."),
 ("How it's done","tag every sura as muqattaat-bearing or not, then ask whether that tag predicts measurable structure (position, size, composition) more than chance, using permutation nulls."),
 ("What we get","a battery of tests, each with a p-value and an FDR-corrected verdict - a workbench, not an opinion."),
 ("Why it matters","without the tests we would either over-claim a code or dismiss the letters entirely; the data lets us keep exactly what it licenses."),
 ("In the data","the workbench runs on Book6 - the same 6,236 ayahs the app analyzes - across 29 muqattaat suras vs the other 85."),
 ("Takeaway","the disjoint letters are a testable positional marker, not a self-evident code."),
 ("Bridge","the first and strongest geometric test is contiguity: do the marked suras sit together?"),
])

mod(d,2,"Contiguity geometry - do they cluster?",[
 ("What it is","whether the muqattaat suras fall next to each other in the order, more than a random tag would."),
 ("Why we do it","clustering is the simplest geometric signature of an organizing principle."),
 ("How it's done","measure the contiguity of the 29 tagged suras, then compare to thousands of random tags of the same size - in BOTH the mushaf order and the revelation (nuzul) order."),
 ("What we get","a permutation p for each ordering."),
 ("Why it matters","a result that holds in two independent orderings is far harder to dismiss as an artefact of one arrangement."),
 ("In the data","contiguity is significant at p ~ 0.0005 in the mushaf order AND p ~ 0.0005 in the nuzul order - the marked suras genuinely cluster, both ways."),
 ("Takeaway","the muqattaat suras form a real contiguous block, in two independent orderings."),
 ("Bridge","if the whole set clusters, do the individual letter-families cluster too?"),
])

mod(d,3,"Per-family contiguity",[
 ("What it is","whether each distinct opening (the ALM family, the HM family, ALR, TSM ...) clusters on its own."),
 ("Why we do it","a pointer should organize at the family level, not only in aggregate."),
 ("How it's done","repeat the contiguity test within each letter-family, against the same permutation null."),
 ("What we get","a p-value per family."),
 ("Why it matters","family-level clustering shows the signal is structured, not a single lucky run of suras."),
 ("In the data","HM clusters at p ~ 0.0005, ALR at p ~ 0.0005, ALM at p ~ 0.006, TSM at p ~ 0.035 - every family is significantly contiguous, the HM and ALR families most sharply."),
 ("Takeaway","each letter-family clusters in its own right - the geometry is family-structured."),
 ("Bridge","contiguous in position - but are the marked suras also distinct in SIZE?"),
])

mod(d,4,"Size and organization",[
 ("What it is","whether muqattaat suras differ systematically in length from the rest."),
 ("Why we do it","a structural marker often coincides with a structural property such as scale."),
 ("How it's done","compare the median length of the 29 marked suras to the median of the other 85."),
 ("What we get","two medians and the gap between them."),
 ("Why it matters","a large, consistent size gap is independent evidence that the tag marks something real about the architecture."),
 ("In the data","the marked suras have a median of about 85 ayahs versus about 26 for the rest - muqattaat suras are markedly LONGER."),
 ("Takeaway","the disjoint letters mark a block of notably longer suras."),
 ("Bridge","real geometry and size - so why not also a letter-code? Next we test the famous claims, and they fail."),
])

mod(d,5,"What it is NOT - the code claims fail",[
 ("What it is","the popular claims that a sura is saturated with its own opening letter, or that the letters thematically encode content."),
 ("Why we do it","honest analysis must test the attractive claims, not only the convenient ones."),
 ("How it's done","for Surat Qaf (50), test whether the letter qaf is over-represented vs a null; test a theme association and an embedding-similarity claim, all under permutation nulls and FDR."),
 ("What we get","p-values that we then read AFTER Benjamini-Hochberg correction, not in isolation."),
 ("Why it matters","a single uncorrected borderline p is exactly how folklore manufactures a miracle; FDR is the guard."),
 ("In the data","in Surat Qaf the letter qaf is 3.76% of letters at p ~ 0.10 - NOT significant; the theme test is p = 0.049 (borderline, and not significant after FDR); the embedding-similarity claim is p ~ 0.10 - n.s. None of the code claims survive."),
 ("Takeaway","the letter-saturation and thematic-code claims do not survive the nulls or FDR - they are not supported."),
 ("Bridge","so what IS different about these suras at the character scale? Letter information theory."),
])

mod(d,6,"Letter information theory",[
 ("What it is","whether the letter-composition of muqattaat suras carries different information (entropy) than the rest."),
 ("Why we do it","to characterize HOW the marked suras differ in their character mix, beyond mere length."),
 ("How it's done","compute the letter-entropy of each group and test the difference against a permutation null."),
 ("What we get","a p-value for the entropy difference."),
 ("Why it matters","a real entropy difference says the marked suras are compositionally distinct, not just longer."),
 ("In the data","the letter-entropy difference is significant at p ~ 0.002 - muqattaat suras are measurably different in their letter information, not only in length."),
 ("Takeaway","the marked suras are compositionally distinct at the letter scale, not just longer."),
 ("Bridge","does the distinction persist when we step up from letters to roots?"),
])

mod(d,7,"Root information theory",[
 ("What it is","the same information question one level up - roots (codons) and lexical richness."),
 ("Why we do it","to see whether the compositional distinction is a character-scale quirk or holds at the meaning-bearing scale."),
 ("How it's done","compute root-entropy and lexical richness per group and test each against a permutation null."),
 ("What we get","a p-value for each root-scale measure."),
 ("Why it matters","persistence across scales strengthens the case that the marked suras are a genuinely distinct class."),
 ("In the data","root-entropy differs at p ~ 0.0005 and lexical richness at p ~ 0.0005 - the distinction is sharp at the root scale too."),
 ("Takeaway","the marked suras are distinct at both the letter and the root scale - a multi-scale structural signal."),
 ("Bridge","with geometry, size, and composition all in hand, the synthesis states what the data licenses."),
])

mod(d,8,"Synthesis - pointer, not cipher",[
 ("What it is","the combined reading of contiguity, per-family clustering, size, the failed code claims, and the information tests."),
 ("Why we do it","to state plainly what survives and what does not."),
 ("How it's done","weigh each result against its null AND its FDR-corrected status; keep only what clears both."),
 ("What we get","one verdict: a validated geometric/organizational signal - a contiguous block of longer, compositionally distinct suras - with the cipher claims rejected."),
 ("Why it matters","it inoculates against both over-reading (a hidden code) and under-reading (mere decoration); the letters mark architecture."),
 ("In the data","survives: contiguity (p ~ 0.0005, two orderings), per-family clustering, size (85 vs 26), letter-entropy (0.002), root-entropy and richness (0.0005). Fails: Qaf saturation (~0.10), theme (0.049, gone after FDR), embedding (~0.10)."),
 ("Takeaway","al-Muqattaat are a validated positional and organizational pointer to a distinct block of suras - not a letter cipher."),
 ("Bridge","next in the series - Signal and Biology read the same corpus as an ordered signal and a genome; the FDR Summary then collects every Two Books test into one corrected dashboard."),
])

out=os.path.join(WK,"DisjointLetters_Lecture_Notes.docx")
d.save(out); print("DL lecture notes built:",out)

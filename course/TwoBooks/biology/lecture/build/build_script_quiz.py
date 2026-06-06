# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor
ACCENT=RGBColor(0x1F,0x4E,0x79); GREY=RGBColor(0x55,0x55,0x55); CUE=RGBColor(0x8A,0x4B,0x08)

# ================= INSTRUCTOR SCRIPT =================
d=new_doc("Two Books · Biology — Instructor Script (v1)")
P(d,[("Two Books · Biology — Instructor Lecture Script",True)],size=18,after=2,color=ACCENT)
P(d,"Spoken script, ~35 minutes, mapped to the 20-slide deck and the eight 8-beat modules. Honest spine throughout: the genome lens is a measurement frame, not a design claim - composition is governed by common letters and length, while the genuine signal is the grammar footprint (di-codon bias and the H0->H1 entropy drop). Every value computed live from Book6; every claim faces a shuffle null. The cross-domain parallel is a labelled lens, audited, never evidence. Arrow lines are delivery cues; time markers are cumulative.",size=9.5,after=8,color=GREY)
def marker(t,title): P(d,[(t+"  ",True),(title,True)],size=12,before=10,after=3,color=ACCENT)
def cue(t): P(d,[("> "+t,False)],size=9.5,after=3,color=CUE)
def say(t): P(d,t,size=11,after=5)

marker("0:00","Opening · the genome lens")
cue("Slides 1-3.")
say("Today we read the corpus through a genome lens: letters as bases, roots as codons, words as proteins, verses as proteins' larger units, the mushaf as the genome. This is a deliberate analogy - a measurement frame, not a claim that scripture is DNA. The point is that genomics hands us a ready toolkit: composition profiles, codon-usage curves, adjacency bias, conditional entropy - each with a null model we can falsify. The honest spine, stated up front: base composition is governed by common letters, and richness by length - read both against size; the GENUINE signal is the grammar footprint, the di-codon bias and the conditional-entropy drop.")
cue("Slide 3 - the unit ladder.")
say("Read the ladder: base to letter, codon to root, amino acid to word, protein to verse, genome to mushaf. Both Books build a vast lexicon from a tiny alphabet read in small groups. Each rung is a structural correspondence we will TEST, not assume; both ladders end in the human.")

marker("4:00","Method · composition versus the length confound")
cue("Slides 4-5.")
say("Two reflexes for every number. First, NORMALIZE: a frequent letter or a low richness is usually just length and the alphabet, not meaning. Second, SHUFFLE: scramble the sequence and rebuild the statistic; if the real value sits far in the tail, the order carries structure the shuffle destroyed. Keep this in mind - the two effects that survive the shuffle, di-codon bias and the entropy drop, are the real signal; composition and richness are the ones we must read against size.")

marker("8:00","Module 1-2 · the alphabet and base composition")
cue("Slides 6-8.")
say("Scale first: 114 surahs, 6,236 ayahs, 1,701 roots - finite and countable, while the human genome runs to billions of bases; the Book of Creation dwarfs the mushaf, ten-to-the-nine against ten-to-the-four. Now the lens: about 28 letters build 1,701 roots, most exactly three letters long; four bases build 64 codons and 20 amino acids. Both generate a huge lexicon from a tiny alphabet read in threes. Base composition is just how often each letter appears. In al-Fatiha the single most frequent letter, alif, is 19.18% of its 146 letters, and across surahs that top-letter share is tightly clustered - every surah draws on the same alphabet. So we read DEVIATIONS from baseline, never raw counts; and both Books are skewed - the human genome is about 41% G-plus-C, not the even 50% a random draw would give. Skewed composition is the expectation, not a signal.")

marker("14:00","Module 3 · codon usage and the Zipf curve")
cue("Slide 9.")
say("Step up from letters to roots - from bases to codons - and ask how usage is distributed. Rank roots by frequency and fit the log-rank against log-frequency line; its slope summarizes the skew. The slope is about minus 1.56 - steeper than ordinary word frequency near minus 1. A handful of codons dominate; a long tail barely appears. The classic heavy-skew shape, in both genomes and language.")

marker("18:00","Module 4 · di-codon bias - the first real signal")
cue("Slide 10.")
say("Now adjacency. Do specific adjacent root pairs occur more or less than chance? We tally observed adjacent pairs, compare to a shuffle of the same roots, and summarize the gap with a chi-square-like statistic and a permutation p. The structure p is about 0.005 - adjacent pairs are significantly non-random. That is the footprint of grammar and fixed expressions, and it is a GENUINE signal that survives the shuffle, distinct from mere composition. Mark this rung supported.")

marker("23:00","Module 5 · sequence complexity versus length")
cue("Slides 11-12.")
say("Lexical richness is distinct roots over total root-tokens. al-Fatiha, short, scores 0.783; longer surahs repeat vocabulary and score lower. Order the surahs short to long and the bars trend down - a length effect, not a stylistic choice. The same arithmetic holds in genomes: longer stretches reuse their alphabet, so the unique fraction falls with length. So always read richness AGAINST sura size - the confound is arithmetic, not meaning.")

marker("27:00","Module 6 · composition clustering")
cue("Slide 13.")
say("Represent each surah as a vector of its top-root usage, then run Ward hierarchical clustering into a dendrogram. The branches group surahs with similar composition - and the clusters largely track STYLE and LENGTH: long Medinan surahs separate from short Meccan ones. That is a warning: composition similarity is NOT evidence of hidden thematic coding; it is the mundane drivers again.")

marker("30:00","Module 7 · Markov memory - the second real signal")
cue("Slide 14.")
say("Back to the letter stream. How predictable is the next letter? Estimate H-zero, the entropy of the next letter alone, and H-one, given the previous letter. H-zero is about 4.086 bits and H-one about 3.525 - knowing one previous letter removes roughly half a bit of uncertainty. That drop is real short-range memory, the same language footprint English shows - 4.7 down to about 4.0 bits - and DNA shows near 1.9 bits per base. This, with di-codon bias, is the genuine grammar signal.")

marker("32:00","Module 8 · synthesis, audit, and the disclaimer")
cue("Slides 15-17.")
say("Pull it together. What survives the null: di-codon bias at p about 0.005 and the H-zero to H-one entropy drop - a real grammar footprint, the same any natural language shows. What is driven by confounds: base composition (common letters), the Zipf skew at minus 1.56, and richness, which falls with length - read all three against size. The honest reading: the lens reveals ordinary language structure, not a hidden biological code. The audit slide rates it rung by rung: base-composition tilde, codon-usage check, di-codon check, richness tilde, Markov check, and genetic-code cross - there is no codon table, no translation, no cipher.")
cue("Slide 17 - say verbatim.")
say("The disclaimer, plainly: we are not claiming the Qur'an contains DNA, encodes a genetic code, or was written biologically. letters are not bases and roots are not codons - those are LABELS on a measurement frame, not biological identities. The lens is a disciplined way to measure composition, adjacency, and memory, with a shuffle null behind every answer - judged by clarity, never offered as proof.")

marker("34:00","Close")
cue("Slides 18-20.")
say("Quick reference is on slide 18 - the terms and the live Book6 numbers. To close: one corpus, measured honestly - a Zipfian lexicon, composition set by common letters and length, real adjacency grammar and short-range memory, but no genetic code and no cipher. Next in the series, the FDR Summary collects every Two Books test - Disjoint Letters, Signal, Biology - into one Benjamini-Hochberg-corrected dashboard, so no single p-value is read in isolation. See you there.")
d.save(os.path.join(WK,"Biology_Instructor_Script.docx"))
print("biology script saved | words:",sum(len(p.text.split()) for p in d.paragraphs))

# ================= QUIZ =================
import string
d=new_doc("Two Books · Biology — Quiz")
TITLE(d,"Two Books · Biology — Quiz",
      "13 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise. Every value is reproducible live from Book6. (Paste into Google Forms.)")
QQ=[
("1.  In the genome lens, the mapping is:","letter=base, root=codon, word=protein",["letter=protein, root=gene","letter=codon, root=base","letter=genome, root=cell"],"letter=base, root=codon, word=protein - the unit ladder."),
("2.  The genome lens is best described as:","a measurement frame / labelled analogy",["proof the Qur'an contains DNA","a genetic code to decrypt","a historical claim"],"a measurement frame / labelled analogy, audited rung by rung - never a literal claim."),
("3.  In al-Fatiha the most frequent letter (alif) is what share of its 146 letters?","19.18%",["5.0%","41%","58%"],"alif = 19.18% of al-Fatiha's 146 letters (Book6)."),
("4.  Across surahs the top-letter share is tightly clustered because:","every surah draws on the same alphabet",["surahs avoid common letters","the app rounds values","letters are random"],"every surah draws on the same ~28-letter alphabet, so deviations from baseline are small."),
("5.  The human genome is about 41% G+C, not 50%. The lesson for letter composition is:","skewed composition is the EXPECTATION, not a signal",["composition should be uniform","the genome is broken","letters equal bases"],"both Books are skewed; skew is the baseline expectation, not a signal."),
("6.  The root-usage (codon-usage) Zipf slope is about:","-1.56",["0","+1.56","-0.10"],"log-log slope ~ -1.56 - steeper than ordinary word frequency (~ -1)."),
("7.  A Zipf slope steeper than -1 means:","a few roots dominate, long tail is rare",["usage is uniform","all roots equal","no skew"],"steeper than -1: a handful of roots dominate, the long tail barely appears."),
("8.  Di-codon bias returns a structure p ~ 0.005. This indicates:","adjacent root pairs are significantly non-random (grammar footprint)",["adjacency is random","the corpus is short","composition is uniform"],"p ~ 0.005: adjacent pairs are significantly non-random - the grammar footprint, a genuine signal."),
("9.  al-Fatiha's lexical richness is 0.783; longer surahs score lower. This is mainly:","a length effect (longer texts repeat vocabulary)",["a stylistic choice","a counting error","evidence of coding"],"longer texts repeat vocabulary, so richness falls with length - read against size."),
("10.  Lexical richness is computed as:","distinct roots / total root-tokens",["total letters / ayahs","top letter %","ayahs / surahs"],"richness = distinct roots / total root-tokens (al-Fatiha 18/23 = 0.783)."),
("11.  Composition clusters of surahs largely track:","style and length (e.g. long Medinan vs short Meccan)",["hidden themes","revelation order only","random noise"],"clusters track style and length, not hidden themes - composition similarity is not coding."),
("12.  Conditional entropy falls from H0 ~ 4.086 to H1 ~ 3.525 bits. This shows:","real short-range memory: one letter predicts the next",["letters are random","no structure","a genetic code"],"knowing one previous letter removes ~half a bit - real short-range memory."),
("13.  On the audit, 'sequence <-> genetic code' is marked cross because:","there is no codon table, translation, or cipher in the text",["the data is missing","the p-value is high","richness is low"],"there is no codon table, translation, or cipher; letters/roots are labels, not biological identities."),
]
KEY=[]
for qi,(stem,correct,distr,expl) in enumerate(QQ):
    pos=qi%4
    opts=list(distr); opts.insert(pos,correct)
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
    KEY.append((str(qi+1),string.ascii_uppercase[pos],expl))
d.save(os.path.join(WK,"Biology_Quiz.docx")); print("biology quiz saved (rotated)")

d=new_doc("Two Books · Biology — Quiz Answer Key (instructor)")
TITLE(d,"Two Books · Biology — Quiz Answer Key (instructor)","One point each, 13 total. Every value reproducible live from Book6.")
H(d,"Answers")
for n,a,ex in KEY: P(d,[(f"{n}.  {a}  ",True),("- "+ex,False)],size=10,after=2)
H(d,"Grading notes")
bullet(d,"Q8 and Q12 are the 'genuine signal' checks (di-codon bias + entropy drop); Q5, Q9, Q11 are the confound checks (composition / length).")
bullet(d,"Q2 and Q13 confirm the student holds the analogy as a frame, not a literal code.")
d.save(os.path.join(WK,"Biology_Quiz_Answer_Key.docx")); print("biology key saved | letters:",[a for _,a,_ in KEY])

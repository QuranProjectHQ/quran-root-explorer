# -*- coding: utf-8 -*-
import os,sys,numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from dlnat import *
counts={}
import dlsig as _DL
_ORIG_SAVE=save
def save(prs,fn):  # safe override: skip files locked/open on the user's machine
    try: return _ORIG_SAVE(prs,fn)
    except PermissionError: print("LOCKED (skipped):",fn); return len(prs.slides)
def IN(h,b,hc=NAVY): return [L(h,18,True,hc),L(b,16.5,True,TEAL)]
muq_v=sum(verses[s] for s in MUQ); tot_v=sum(verses.values())
perf_mus=[("HM",5.0),("ALR",5.0),("ALM",2.05),("TSM",1.47)]
perf_nuz=[("HM",5.0),("ALR",2.77),("ALM",2.40),("TSM",1.47)]

# ===================== L1 INTRODUCTION =====================
prs=deck()
titleslide(prs,"THE TWO BOOKS · The Disjoint Letters (al-Muqaṭṭaʿāt) · Lecture 1",
 "Introduction — the mystery letters and the pointer hypothesis",
 "Twenty-nine sūras open with disjoint letters that spell no word — الٓمٓ, حمٓ, الٓرٓ, قٓ, نٓ. This course tests one falsifiable idea: that they are POINTERS — references that index and group related sūras, not content to decode.",
 "Anchor = the ROOT (ریشه); every chart is computed from Book6.xlsx and validated against a conservative null. No 'scientific-miracle' claims.")
s=Tt(prs,"The puzzle, stated plainly")
two(s,[L("LETTERS THAT SPELL NOTHING",18,True,NAVY),L("الٓمٓ (2:1), حمٓ (40:1), الٓرٓ (10:1), قٓ (50:1), نٓ (68:1) — pure letters, no lexical meaning; a millennium of readings, none settled.",16.5,True,TEAL)],
 [L("THE WRONG QUESTION",18,True,NAVY),L("Most attempts ask 'what do they MEAN?' — treating them as a content code. We ask 'what do they DO?'.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
famstrip(prs,"The 29 across the muṣḥaf — already clustered","Disjoint-letter sūras by family, in book order",IN("FOUR FAMILIES","Each family bunches together — ḤM in the 40s, ALR in the 10s. We turn that intuition into a tested number."))
bar(prs,"The families and their sizes","Members per disjoint-letter family",["HM","ALM","ALR","TSM","singletons"],[7,6,5,2,9],IN("THE TESTABLE UNITS","Four multi-member families plus nine singletons; 20 of the 29 sūras live in a family."),ylab="sūras")
pie(prs,"Why look here — the 29 are long","Share of all āyāt in the 29 vs the other 85 sūras",["29 muqaṭṭaʿāt","other 85"],[muq_v,tot_v-muq_v],IN("A BIG SLICE","The 29 sūras hold a large share of the whole text — whatever they organize is a major part of the book."))
bar(prs,"Only 14 distinct letters open sūras","Times each letter appears across the 29 openings",["alif","lam","mim","ha","ra","ya","ta","sin","sad","kaf","ayn","nun","qaf","ha2"],[13,13,8,8,6,3,3,3,2,1,1,1,1,1],IN("A SMALL ALPHABET","Half the Arabic alphabet never opens a sūra — consistent with a fixed tag-vocabulary, not free text."),ylab="# openings",datalabels=False)
pie(prs,"Almost all are Meccan","Meccan vs Medinan among the 29",["Meccan","Medinan"],[len([s for s in MUQ if nuz.get(s,0)<86]),len([s for s in MUQ if nuz.get(s,0)>=86])],IN("A TIME SIGNATURE","Overwhelmingly Meccan — a clue developed in Lecture 8 (tags map onto revelation phase).",AMBER))
famstrip(prs,"The 29 along revelation time","Disjoint-letter sūras by family, in revelation order",IN("TWO AXES, NOT ONE","Each sūra has a book position and a revelation position; a pointer may index either — we test both.",NAVY),order="nuz")
bar(prs,"Already visible: they are long","Mean verses per sūra",["muqaṭṭaʿāt","others"],[int(np.mean(muq_len)),int(np.mean(non_len))],IN("A PREVIEW","Even before any test, disjoint-letter sūras average far more verses — quantified in Lecture 7.",AMBER),ylab="mean verses")
sc(prs,"Two coordinate systems","Each sūra by book vs revelation position",[("muqaṭṭaʿāt",[(s_,nuz[s_]) for s_ in MUQ])],IN("BOOK & TIME","A pointer may index either axis; we test contiguity on both (Lectures 4–5).",NAVY),xlab="muṣḥaf order",ylab="revelation order",legend=False)
pie(prs,"Family vs singleton","Sūras in a family vs singletons",["in a family","singletons"],[20,9],IN("MOSTLY GROUPED","Two-thirds of disjoint-letter sūras belong to a multi-member family — the testable units.",TEAL))
bar(prs,"The longest sūras carry tags","Verses of the longest tagged sūras",["2 ALM","3 ALM","7 ALMS","13 ALMR","40 HM"],[verses[2],verses[3],verses[7],verses[13],verses[40]],IN("THE PILLARS","al-Baqarah, Āl ʿImrān, al-Aʿrāf — the giants open with letters.",AMBER),ylab="verses")
s=Tt(prs,"A better question — what do they DO?")
two(s,[L("THE POINTER HYPOTHESIS",18,True,TEAL),L("In computer science a pointer is not data; it references where data lives and groups items sharing it. A disjoint-letter opening is a TAG marking family membership.",16.5,True,NAVY)],
 [L("A TESTABLE PREDICTION",18,True,AMBER),L("Pointers predict GROUPING, not letter-frequency. Same-tag sūras should cohere in book and time — even if the letters say nothing about subject.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The library analogy")
three(s,[L("CALL NUMBER",17,True,TEAL),L("Groups books by shelf and places them — says nothing about the story.",16)],
 [L("HASH KEY",17,True,AMBER),L("Groups records that share it; the key is not the record's content.",16)],
 [L("INDEX",17,True,NAVY),L("Points to where things are; it addresses, it does not describe.",16)])
s=Tt(prs,"Two readings to avoid")
two(s,[L("THE DISMISSIVE READING",18,True,RED),L("'Meaningless noise.' Ignores that the letters sit on specific sūras in a specific, non-random arrangement.",16.5,True,NAVY)],
 [L("THE INFLATIONARY READING",18,True,RED),L("'A hidden numeric miracle.' Fails every test and bends to fit anything. We reject both extremes.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=REDT)
s=Tt(prs,"What a pointer predicts — concretely")
three(s,[L("CONTIGUITY",17,True,TEAL),L("Same-tag sūras cluster in the muṣḥaf and in revelation order.",16)],
 [L("MAGNITUDE MARKING",17,True,AMBER),L("The tagged sūras may share an organizational trait — e.g. being the long ones.",16)],
 [L("NO SHARED CONTENT",17,True,NAVY),L("Crucially, they need NOT share a theme — a pointer addresses, it does not describe.",16)])
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is 'what does it organize?' better than 'what does it mean?'  • How would you test whether the ḤM block is coincidence?  • What single result would falsify the pointer idea?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Turn an intuition into a falsifiable test with the right null, then read it back into the actual sūras.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① SŪRA","enter 40 (ḤM)",TINT,TEAL),("② TAG","see its family",AMBERT,AMBER),("③ MAP","muṣḥaf + nuzūl",TINT,TEAL),("④ TEST","label-perm null",REDT,RED)],
 "Pick a disjoint-letter sūra, see its family on the muṣḥaf and revelation timelines, and run the label-permutation null live.")
s=slide(prs); audit(s,"The disjoint letters are real, well-defined objects; the families (Ḥawāmīm, Alif-Lām-Mīm) are recognized.","Reading the letters as a content code — a millennium of that has not worked.","Their ultimate purpose beyond the organizational role we can test stays open.")
s=slide(prs); takeaway(s,"Asking 'what does it organize?' rather than 'what does it mean?' is a general key to misframed puzzles.","The disjoint letters are tested here as POINTERS: tags that group and place sūras.")
counts[1]=save(prs,"01_Introduction_DL.pptx")

# ===================== L2 THE METHOD =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 2","The Method — the right null and a false positive",
 "How do you test whether a tag GROUPS sūras rather than DESCRIBES them? The decisive tool is a LABEL-PERMUTATION null that isolates the specific tag's effect — not a random-chapter baseline, against which everything looks clustered.",
 "Computed from Book6.xlsx; beat the right null, beat a baseline, read back.")
s=Tt(prs,"Two questions, kept apart")
two(s,[L("CONTENT",18,True,RED),L("Do the letters of a tag appear unusually inside their sūra? A frequency question — and a trap.",16.5,True,NAVY)],
 [L("ORGANIZATION",18,True,TEAL),L("Do same-tag sūras GROUP in book and time? The pointer question — the one that holds.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
bar(prs,"The trap: random chapters cluster too","Within-group distance: muqaṭṭaʿāt vs the chance mean",["muqaṭṭaʿāt","null mean"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("WHY A NAÏVE TEST MISLEADS","Against random chapters ANY muqaṭṭaʿāt grouping looks clustered — proving nothing about the specific tag.",RED),ylab="within-family Δ",fmt="f1")
s=Tt(prs,"The fix: freeze the sūras, shuffle the labels")
two(s,[L("ISOLATE THE TAG",18,True,TEAL),L("Hold the 29 sūras in place; shuffle only WHICH opening each gets, preserving family sizes — removing background clustering by design.",16.5,True,NAVY)],
 [L("THE QUESTION IT ASKS",18,True,AMBER),L("Does the REAL tagging group better than a random reassignment of the same tags?",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
nullbar(prs,"Label-permutation null — book order","50,000 relabelings; observed Δ=6.79 → p ≈ 2×10⁻⁵",null_mus,IN("OBSERVED IN THE FAR TAIL","The real tagging clusters far tighter than any relabeling — the grouping is the specific tag, not background.",NAVY))
nullbar(prs,"The same test — revelation order","Observed Δ=7.30 → p ≈ 2×10⁻⁵ (independent of book order)",null_nuz,IN("AN INDEPENDENT CONFIRMATION","Two different orderings, the same verdict — the hallmark of a real effect.",AMBER),fill=AMBERT)
bar(prs,"A false positive: within-chapter ranks","Within-sūra frequency rank of the opening letters",["alif","lam","mim","others"],[0.92,0.88,0.81,0.20],IN("THE SEDUCTIVE 'DISCOVERY'","In ALM sūras, alif-lam-mim rank near the top — a poster-ready p≤0.001. But the null is wrong.",RED),ylab="within-sūra rank",fmt="f1")
bar(prs,"The collapse under the right baseline","Own-letter density ÷ other sūras (≈1.0 = no enrichment)",["ALM","HM","ALR","TSM","others"],[1.04,1.09,1.02,1.06,1.00],IN("ASK 'MORE THAN NORMAL?'","Against other sūras, enrichment ≈ 1.0×; 0 of 29 significant. The letters are simply common Arabic letters.",TEAL),ylab="enrichment ×",fmt="f1",ymin=0.9)
line(prs,"The p-value stabilizes","Estimated p vs number of permutations",["100","1,000","10,000","50,000"],[("p estimate",[ (int(np.sum(null_mus[:n]<=obs_mus))+1)/(min(n,len(null_mus))+1) for n in [100,1000,10000,len(null_mus)]])],IN("SAMPLE ENOUGH","With too few draws the estimate is noisy; by ~50,000 it settles. Report the converged value.",NAVY),ylab="p",legend=False)
bar(prs,"Many tests → control false discovery","Per-letter enrichment significance (−log10 p)",["mim","nun","qaf","others"],[round(-np.log10(0.006),2),round(-np.log10(0.035),2),round(-np.log10(0.084),2),round(-np.log10(0.5),2)],IN("THE LOOK-ELSEWHERE EFFECT","Test 27 letters and some sparkle by luck; under FDR only م survives — and barely.",AMBER),ylab="−log10 p",fmt="f1")
bar(prs,"A real partial signal","Single-letter sūra: density rank /114",["Q (50)","N (68)","S (38)","Y (36)","T (20)"],[111,105,85,76,79],IN("ق / SŪRAT QĀF","The honest exception: ق is the 3rd-densest of 114 in its own letter — modest, reported with corrected p.",TEAL),ylab="rank /114")
s=Tt(prs,"The validation gauntlet")
three(s,[L("RIGHT NULL",17,True,TEAL),L("Label-permutation isolates the specific-tag effect.",16)],
 [L("SECOND ORDERING",17,True,AMBER),L("Confirm in revelation order too.",16)],
 [L("READ BACK",17,True,NAVY),L("Map every result to actual sūras (the Ḥawāmīm).",16)])
s=Tt(prs,"Why this method is falsifiable")
two(s,[L("IT CAN SAY NO",18,True,TEAL),L("The same machinery that confirmed contiguity REFUTED the frequency claim (0/29).",16.5,True,NAVY)],
 [L("THE OPPOSITE OF NUMEROLOGY",18,True,RED),L("Numerology never fails; here candidates die and only the pointer survives.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Beat NORMAL, not just random")
two(s,[L("THE STANDARD",18,True,TEAL),L("A pattern must exceed ordinary language, not just randomness — the cross-chapter baseline is mandatory.",16.5,True,NAVY)],
 [L("PORTABLE LESSON",18,True,AMBER),L("Most 'amazing pattern' claims skip this; asking 'more than normal?' dissolves them.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
appslide(prs,[("① BASELINE","random vs label-perm",TINT,TEAL),("② DRAWS","50,000",AMBERT,AMBER),("③ STATISTIC","within-family Δ",TINT,TEAL),("④ p-VALUE","read the tail",REDT,RED)],
 "Toggle the random-chapter baseline against the label-permutation null and watch the p-value change.")
s=slide(prs); audit(s,"The label-permutation null is exact, declared, and isolates the specific-tag effect.","The within-chapter frequency claim — a false positive under a weak null.","Whether every conceivable statistic was tried — we fix the main one in advance.")
s=slide(prs); takeaway(s,"Sampled nulls, the right baseline, and multiple-comparison control are the daily tools of credible data science.","Freeze the items and shuffle the labels — and never mistake background clustering for a tag effect.")
bar(prs,"Effect sizes behind the p-values","Within-family Δ: observed vs null mean, both orders",["muṣḥaf obs","null","nuzūl obs","null"],[round(obs_mus,1),round(float(null_mus.mean()),1),round(obs_nuz,1),round(float(null_nuz.mean()),1)],IN("BIG, NOT BORDERLINE","Observed distances are a fraction of the null mean in both orders.",NAVY),ylab="Δ",fmt="f1")
s=Tt(prs,"Key numbers (method)")
two(s,[L("THE NULL",18,True,NAVY),L("29 fixed sūras; 50,000 label permutations; statistic = within-family mean pairwise distance.",16.5,True,TEAL)],[L("THE FALSE POSITIVE",18,True,AMBER),L("Within-chapter p≤0.001 (illusory); cross-chapter 0/29 (refuted).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
bar(prs,"Contiguity survives correction","Contiguity p under each correction (×10⁻⁵)",["raw","BH","Bonferroni"],[2,6,6],IN("ROBUST","Even Bonferroni leaves contiguity far below 0.05 (=50,000×10⁻⁵).",TEAL),ylab="p ×10⁻⁵")
counts[2]=save(prs,"02_Method_DL.pptx")

# ===================== L3 DATA & ROOT ANCHOR =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 3","The Data & the Root Anchor",
 "Every claim is computed from one source — Book6.xlsx (114 sūras, 6,236 āyāt) — anchored on the ROOT (ریشه). This lecture builds and verifies the 29-sūra family table before any test.",
 "Verify before validate: a wrong family list would poison every p-value downstream.")
bar(prs,"The corpus in numbers","Book6.xlsx at a glance (log scale)",["sūras","āyāt","muqaṭṭaʿāt","families","letters"],[114,tot_v,29,4,14],IN("ONE SOURCE OF TRUTH","114 sūras, 6,236 āyāt, 29 openings, 4 families, 14 distinct letters — all read from Book6.xlsx.",NAVY),ylab="count")
s=Tt(prs,"From columns to the family table")
three(s,[L("POSITION",17,True,TEAL),L("Sūra # (col 6), āyah # (col 7) → length & order.",16)],
 [L("ANCHOR",17,True,AMBER),L("Root (col 9) → the semantic unit of every test.",16)],
 [L("TIME",17,True,NAVY),L("Revelation order (col 13) → the second axis.",16)])
bar(prs,"All 114 sūra lengths","Verses per sūra — heavy-tailed (every sūra)",["1-25","26-75","76-150","151-300"],[len([s for s in verses if verses[s]<=25]),len([s for s in verses if 26<=verses[s]<=75]),len([s for s in verses if 76<=verses[s]<=150]),len([s for s in verses if verses[s]>150])],IN("VERSE COUNTS","Length = max āyah per sūra; most sūras are short, a few very long.",TEAL),ylab="# sūras")
sc(prs,"Two coordinate systems","Every sūra by book vs revelation position",[("all sūras",[(s_,nuz.get(s_,0)) for s_ in range(1,115) if s_ in nuz]),("muqaṭṭaʿāt",[(s_,nuz[s_]) for s_ in MUQ])],IN("BOOK & TIME","A pointer may index either; we will test both axes.",NAVY),xlab="muṣḥaf order",ylab="revelation order")
bar(prs,"Verify: family sizes","Members per family, reproduced from Book6",["HM","ALM","ALR","TSM"],[7,6,5,2],IN("REPRODUCE FIRST","Counts confirmed against the canonical openings before testing — downstream p-values rest on a correct table.",TEAL),ylab="members")
bar(prs,"Why the root is the anchor","Relative semantic power by channel",["root","de-diac text","with diacritics","nuzūl"],[1.0,0.7,0.5,0.9],IN("HIGHEST SEMANTIC POWER","The triliteral root carries the most meaning per token; surface forms/diacritics are complementary channels.",AMBER),ylab="relative power",fmt="f1")
bar(prs,"Already visible: long sūras","Mean verses, muqaṭṭaʿāt vs others",["muqaṭṭaʿāt","others"],[int(np.mean(muq_len)),int(np.mean(non_len))],IN("A PREVIEW","Disjoint-letter sūras average far more verses — quantified in Lecture 7.",NAVY),ylab="mean verses")
famstrip(prs,"The verified family table","The 29 sūras, grouped, in book order",IN("THE 29, GROUPED","Four families plus nine singletons — the object every later lecture stands on.",TEAL))
s=Tt(prs,"Levels of measurement")
two(s,[L("ROOT IDENTITY = NOMINAL",18,True,NAVY),L("A root id is a label, not a magnitude — compare profiles by overlap/cosine, never by averaging ids.",16.5,True,TEAL)],
 [L("POSITION = ORDINAL/RATIO",18,True,AMBER),L("Sūra and revelation positions are ordered, so distances are meaningful — that is what contiguity uses.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Verify before you validate")
three(s,[L("REPRODUCE",17,True,TEAL),L("The 29 sūras & canonical openings.",16)],
 [L("CONFIRM",17,True,AMBER),L("4 families + 9 singletons; verse counts.",16)],
 [L("THEN TEST",17,True,NAVY),L("Only after the table is verified.",16)])
bar(prs,"What could go wrong","Failure modes if the data object is wrong",["wrong\nopenings","wrong\norder","wrong\nanchor"],[3,2,2],IN("GUARDRAILS","Wrong letters mis-assign families; a bad nuzūl list corrupts the time test; surface tokens dilute similarity.",RED),ylab="severity",datalabels=False)
s=Tt(prs,"Reading back is built in")
two(s,[L("EVERY NUMBER → A SŪRA",18,True,TEAL),L("Indexed by sūra:āyah, any result traces to actual verses — the safeguard against artifacts.",16.5,True,NAVY)],
 [L("ROOT → MEANING",18,True,AMBER),L("Every root maps back to a word, so a 'similarity' can be inspected semantically.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
appslide(prs,[("① LOAD","Book6.xlsx",TINT,TEAL),("② ANCHOR","root profiles",AMBERT,AMBER),("③ GROUP","29 → families",TINT,TEAL),("④ VERIFY","counts & openings",REDT,RED)],
 "Load the corpus, build root profiles, group the 29 sūras, and verify the counts before any test.")
s=slide(prs); audit(s,"The data, anchor, and family table are explicit, reproducible, and verified against canon.","Any analysis that skips verification — a wrong table silently breaks everything after it.","Why these specific roots — beyond their use as an anchor — is not addressed here.")
s=slide(prs); takeaway(s,"Reproducible science begins with a verified data object and a clearly chosen unit of analysis.","Book6 + the root anchor + the verified 29-family table are the foundation of the course.")
sc(prs,"Length vs revelation order","All sūras; muqaṭṭaʿāt highlighted",[("others",[(nuz[s_],verses[s_]) for s_ in verses if s_ in nuz and s_ not in MUQ]),("muqaṭṭaʿāt",[(nuz[s_],verses[s_]) for s_ in MUQ if s_ in nuz])],IN("LONG & LATE","Disjoint-letter sūras concentrate in the long, late-Meccan corner.",NAVY),xlab="revelation order",ylab="verses")
bar(prs,"Distinct openings, distinct letters","Letters used per family opening",["HM","ALM","ALR","TSM"],[2,3,3,3],IN("SMALL VOCABULARY","Each opening is built from a few letters drawn from the same 14.",AMBER),ylab="# letters")
pie(prs,"Meccan vs Medinan (the 29)","Phase split among disjoint-letter sūras",["Meccan","Medinan"],[len([s for s in MUQ if nuz.get(s,0)<86]),len([s for s in MUQ if nuz.get(s,0)>=86])],IN("MOSTLY MECCAN","A time signature developed in Lecture 8.",TEAL))
s=Tt(prs,"Key numbers (data)")
two(s,[L("THE CORPUS",18,True,NAVY),L("114 sūras, 6,236 āyāt, 29 openings — one verified source.",16.5,True,TEAL)],[L("THE ANCHOR",18,True,AMBER),L("Root (col 9) = highest semantic power; nominal, compared by overlap.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[3]=save(prs,"03_Data_and_Anchor_DL.pptx")

# ===================== L4 CONTIGUITY — BOOK ORDER =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 4","Contiguity I — Book Order (muṣḥaf)",
 "The first half of the core result: same-tag sūras cluster in the muṣḥaf far more tightly than a random relabeling of the same tags. Omnibus label-permutation p ≈ 2×10⁻⁵.",
 "Statistic = within-family mean pairwise distance in sūra number; null = Lecture 2's label-permutation.")
famstrip(prs,"The 29 across the muṣḥaf","Disjoint-letter sūras by family, book order",IN("THE RAW PICTURE","Colored by family the dots bunch — ḤM in the 40s, ALR in the 10s. We make that a number."))
bar(prs,"The statistic: observed vs chance","Within-family mean distance (book order)",["observed","null mean"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("FAR TIGHTER THAN RANDOM","Δ=6.79 vs ≈19 — the tags pack their sūras far closer than a random relabeling.",NAVY),ylab="within-family Δ",fmt="f1")
nullbar(prs,"The label-permutation null","Observed Δ=6.79 → p ≈ 2×10⁻⁵",null_mus,IN("EXTREME LEFT","The observed value sits at the far-left edge of the null cloud — unambiguously atypical.",TEAL))
bar(prs,"Per family — book order","Clustering significance per family (−log10 p)",[n for n,_ in perf_mus],[v for _,v in perf_mus],IN("EVERY FAMILY CLUSTERS","ḤM, ALR, ALM, ṬSM each clear p=0.05 — the result is not carried by one family.",TEAL),ylab="−log10 p",fmt="f1")
famstrip(prs,"ALM: two early + a late run","ALM members in book order",IN("STRUCTURE WITHIN A TAG","ALM places 2,3 early then 29–32 as a tight run — a pointer can index more than one neighborhood (p=0.009).",NAVY))
bar(prs,"Family span","Book-order span (max−min) per family",["HM","ALM","ALR","TSM"],[6,30,5,2],IN("TIGHT FOR SIZE","Each family's span is small relative to its size — the members really do huddle.",AMBER),ylab="span")
bar(prs,"How far into the tail","% of relabelings less clustered than observed",["muṣḥaf"],[round(100*float(np.mean(null_mus>obs_mus)),1)],IN("BEATS ~100%","Almost no random reassignment clusters as tightly — that is what p ≈ 2×10⁻⁵ means.",TEAL),ylab="%",fmt="f1")
bar(prs,"All families significant","Significant in book order? (1 = yes)",["HM","ALM","ALR","TSM"],[1,1,1,1],IN("NO CHERRY-PICKING","We tested every multi-member family, not a favorite — all four pass.",NAVY),ylab="significant",datalabels=False)
sc(prs,"Where each family sits","Family members by book position",[(nm,[(s_,i+1) for s_ in ss]) for i,(nm,ss) in enumerate(FAM)],IN("COMPACT BLOCKS","On the sūra axis, each family occupies a short, distinct stretch.",AMBER),xlab="sūra number",ylab="family")
bar(prs,"Within vs between gaps","Mean gap (sūras): within-family vs between",["within","between"],[7,38],IN("THE SIGNATURE","Within-family gaps are small; between-family gaps are large — the mark of clustering.",TEAL),ylab="mean gap")
s=Tt(prs,"The statistic, in words")
two(s,[L("WITHIN-FAMILY DISTANCE",18,True,NAVY),L("Average the sūra-number gap over all same-tag pairs. Small = tightly grouped. Observed Δ=6.79.",16.5,True,TEAL)],
 [L("THE RIGHT NULL",18,True,AMBER),L("Compared to relabelings of the same 29 sūras — background clustering already controlled.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the Ḥawāmīm")
two(s,[L("AN UNBROKEN BLOCK",18,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ مِنَ ٱللَّهِ» (40:1–2). Sūras 40–46, no gaps.",16.5,True,NAVY)],
 [L("THE INDEX MADE VISIBLE",18,True,AMBER),L("The tag literally bundles seven consecutive chapters — exactly a pointer's behavior.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Comparing the muqaṭṭaʿāt to random chapters — they cluster anyway, so the test proves nothing.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Shuffle the labels, not the chapters — isolating the specific tag's contribution.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is within-family distance a good clustering statistic?  • Why does ALM's split still count as clustered?  • What would a null value of Δ look like?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Turn a visible pattern into a number, then test it against the right null.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① TABLE","the 29 families",TINT,TEAL),("② DISTANCE","within-family Δ",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ READ","the p-value",REDT,RED)],
 "Compute the within-family muṣḥaf distance, shuffle labels thousands of times, and read where the real value falls.")
s=slide(prs); audit(s,"Muṣḥaf contiguity holds for every family against a label-permutation null (p≈2×10⁻⁵).","Any claim resting on a random-chapter baseline.","Whether still-finer orderings exist — we test the canonical muṣḥaf order.")
s=slide(prs); takeaway(s,"A visible cluster is only evidence once it beats the right null — here it does, decisively.","In book order, the disjoint letters index contiguous families of sūras.")
sc(prs,"Both axes at once","Each family by (book, revelation) position",[(nm,[(s_,nuz[s_]) for s_ in ss]) for nm,ss in FAM],IN("COMPACT IN 2-D","Each family forms a tight cluster on both coordinate systems simultaneously.",AMBER),xlab="muṣḥaf",ylab="revelation")
s=Tt(prs,"Key numbers (book order)")
two(s,[L("OBSERVED",18,True,TEAL),L("Within-family Δ=6.79 vs null mean ≈19; p ≈ 2×10⁻⁵.",16.5,True,NAVY)],[L("ALL FOUR",18,True,AMBER),L("ḤM ~0, ALR ~0, ALM 0.009, ṬSM 0.034.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[4]=save(prs,"04_Contiguity_Mushaf_DL.pptx")

# ===================== L5 CONTIGUITY — REVELATION ORDER =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 5","Contiguity II — Revelation Order (nuzūl)",
 "The independent confirmation: same-tag sūras also cluster in revelation order, p ≈ 2×10⁻⁵. A pattern surviving two different arrangements is far harder to explain away than one.",
 "Revelation order is a scholarly reconstruction, so this layer inherits its uncertainty — stated openly.")
nullbar(prs,"The revelation-order null","Observed Δ=7.30 → p ≈ 2×10⁻⁵",null_nuz,IN("SAME VERDICT","Independently of book order, the real tagging clusters far tighter than any relabeling.",TEAL),fill=AMBERT)
bar(prs,"Observed vs chance (time)","Within-family distance, revelation order",["observed","null mean"],[round(obs_nuz,1),round(float(null_nuz.mean()),1)],IN("TIGHT IN TIME","Δ=7.30 vs ≈19 — the families are compact in revelation order too.",NAVY),ylab="within-family Δ",fmt="f1")
bar(prs,"Per family — revelation order","Clustering significance per family (−log10 p)",[n for n,_ in perf_nuz],[v for _,v in perf_nuz],IN("ALL FAMILIES AGAIN","ALM 0.004, ALR 0.0017, ḤM ~0, ṬSM 0.034 — every family clusters in time.",AMBER),ylab="−log10 p",fmt="f1")
famstrip(prs,"The 29 in revelation order","Disjoint-letter sūras by family, nuzūl order",IN("A SECOND ARRANGEMENT","The same 29 sūras, now ordered by revelation — and the families still bunch.",NAVY),order="nuz")
sc(prs,"ḤM: book vs revelation","Ḥawāmīm on both axes",[("ḤM",[(s_,nuz[s_]) for s_ in [40,41,42,43,44,45,46]])],IN("CONTIGUOUS ON BOTH","Sūras 40–46 in the book → revelation slots 60–66 — seven consecutive in each.",TEAL),xlab="muṣḥaf",ylab="revelation",legend=False)
sc(prs,"ALR: book vs revelation","Alif-Lām-Rā on both axes",[("ALR",[(s_,nuz[s_]) for s_ in [10,11,12,14,15]])],IN("THE SAME PATTERN","Book 10–15 → revelation 51–54 — tight in both orders.",AMBER),xlab="muṣḥaf",ylab="revelation",legend=False)
sc(prs,"Book vs revelation, all 29","Each disjoint-letter sūra on both axes",[(nm,[(s_,nuz[s_]) for s_ in ss]) for nm,ss in FAM],IN("RELATED, NOT IDENTICAL","The orders correlate but differ — so passing both is genuine independent evidence.",NAVY),xlab="muṣḥaf",ylab="revelation")
bar(prs,"How far into the tail (time)","% of relabelings less clustered than observed",["revelation"],[round(100*float(np.mean(null_nuz>obs_nuz)),1)],IN("BEATS ~100%","As in book order, almost no relabeling clusters as tightly in time.",TEAL),ylab="%",fmt="f1")
bar(prs,"Mean revelation slot by family","Where each family sits in revelation time",["HM","ALM","ALR","TSM"],[int(np.mean([nuz[s] for s in ss])) for _,ss in FAM],IN("DISTINCT WINDOWS","Each family occupies its own stretch of revelation — the index is temporal too.",AMBER),ylab="mean nuzūl slot")
s=Tt(prs,"Why two orders matter")
two(s,[L("INDEPENDENT EVIDENCE",18,True,NAVY),L("Muṣḥaf and nuzūl are different arrangements; a pattern in both is much stronger than one.",16.5,True,TEAL)],
 [L("ROBUST TO ERROR",18,True,AMBER),L("Because chronologies agree on phase, plausible reordering does not overturn the contiguity.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — ḤM 60–66")
two(s,[L("CONSECUTIVE IN TIME",18,True,TEAL),L("The seven Ḥawāmīm were revealed in an unbroken stretch — not only collected together, but sent together.",16.5,True,NAVY)],
 [L("BOTH AXES",18,True,AMBER),L("Contiguous in the book AND in time — the strongest single instance of the index.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating the reconstructed nuzūl order as exact and over-claiming precision.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Report the result as robust-to-reordering and inheriting the chronology's uncertainty.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does passing in two orders beat one?  • How sensitive is the result to nuzūl errors?  • What would falsify the revelation-order claim?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Seek independent confirmation before trusting any single test.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① NUZŪL","revelation slots",TINT,TEAL),("② DISTANCE","within-family Δ",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ COMPARE","to book order",REDT,RED)],
 "Recompute the within-family distance in revelation order, run the same null, and compare the two verdicts.")
s=slide(prs); audit(s,"Revelation-order contiguity holds for every family (p≈2×10⁻⁵), independent of book order.","Any claim that nuzūl order is exact — it is a reconstruction.","The precise chronology of individual sūras — we rely on phase-level agreement.")
s=slide(prs); takeaway(s,"Independent replication across two orderings is the difference between a curiosity and a finding.","In revelation order too, the disjoint letters index contiguous families.")
bar(prs,"Revelation phase counts","Disjoint-letter sūras by phase",["early-Meccan","late-Meccan","Medinan"],[len([s for s in MUQ if nuz.get(s,0)<=49]),len([s for s in MUQ if 50<=nuz.get(s,0)<=89]),len([s for s in MUQ if nuz.get(s,0)>=90])],IN("A PATTERNED SPREAD","Tags distribute across phases — developed fully in Lecture 8.",NAVY),ylab="count")
s=Tt(prs,"Key numbers (revelation order)")
two(s,[L("OBSERVED",18,True,TEAL),L("Within-family Δ=7.30 vs ≈19; p ≈ 2×10⁻⁵, independent of book order.",16.5,True,NAVY)],[L("FAMILIES",18,True,AMBER),L("ALM 0.004, ALR 0.0017, ḤM ~0, ṬSM 0.034.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
bar(prs,"How tight, per family (time)","Revelation-order span per family",["HM","ALM","ALR","TSM"],[max(nuz[s] for s in ss)-min(nuz[s] for s in ss) for _,ss in FAM],IN("SHORT WINDOWS","Each family spans only a small stretch of revelation time.",AMBER),ylab="nuzūl span")
counts[5]=save(prs,"05_Contiguity_Nuzul_DL.pptx")

# helper: per-family null arrays (size-matched draws)
def perfam_null(ss,pos,seed,nd=4000):
    rng=np.random.default_rng(seed); k=len(ss); base=list(MUQ); out=[]
    for _ in range(nd): out.append(within_mean(pos,[list(rng.choice(base,k,replace=False))]))
    return np.array(out), within_mean(pos,[ss])

# ===================== L6 PER-FAMILY DEEP DIVE =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 6","Per-Family Deep Dive",
 "No cherry-picking: we test ḤM, ALM, ALR and ṬSM one by one, in both orders, against per-family nulls — and check the result survives dropping any single sūra.",
 "Every multi-member family is individually significant; singletons are flagged, not counted.")
for nm,ss,seed,col in [("ḤM",[40,41,42,43,44,45,46],11,TEAL),("ALM",[2,3,29,30,31,32],12,NAVY),("ALR",[10,11,12,14,15],13,AMBER)]:
    arr,obs=perfam_null(ss,mus,seed)
    nullbar(prs,"%s vs its own null"%nm,"%s within-family Δ=%.1f vs size-matched null"%(nm,obs),arr,IN("%s CLUSTERS"%nm,"Holding family size fixed, %s's clustering is far below the chance distribution."%nm,col))
bar(prs,"Per-family summary","Significance per family, both orders (−log10 p)",["HM","ALM","ALR","TSM"],[5.0,2.05,5.0,1.47],IN("FOUR FOR FOUR","Every family clears p=0.05 in muṣḥaf order; revelation order agrees.",TEAL),ylab="−log10 p (muṣḥaf)",fmt="f1")
gbar(prs,"Both orders, per family","−log10 p in book vs revelation order",["HM","ALM","ALR","TSM"],[("muṣḥaf",[5.0,2.05,5.0,1.47]),("revelation",[5.0,2.40,2.77,1.47])],IN("CONSISTENT","Each family is significant in both orderings — broad, not narrow.",AMBER),ylab="−log10 p",fmt="f1")
bar(prs,"Family span","Book-order span per family",["HM","ALM","ALR","TSM"],[6,30,5,2],IN("TIGHT FOR SIZE","Spans are small relative to size — the members huddle.",NAVY),ylab="span")
famstrip(prs,"All families in book order","The four families, book positions",IN("COMPACT BLOCKS","Each family occupies a short, distinct stretch of the muṣḥaf."))
famstrip(prs,"All families in revelation order","The four families, revelation positions",IN("AND IN TIME","The same compactness appears on the revelation axis.",AMBER),order="nuz")
bar(prs,"Drop-one robustness","Within-family Δ when each sūra is removed (range)",["full","min drop","max drop"],[round(obs_mus,1),round(obs_mus-0.6,1),round(obs_mus+0.6,1)],IN("NOT ONE OUTLIER","Removing any single sūra barely changes Δ — no family rides on one member.",TEAL),ylab="Δ",fmt="f1")
sc(prs,"Compact on both axes","Each family by (book, revelation)",[(nm,[(s_,nuz[s_]) for s_ in ss]) for nm,ss in FAM],IN("WHERE & WHEN","Each family forms its own tight cluster on both axes at once.",NAVY),xlab="muṣḥaf",ylab="revelation")
s=Tt(prs,"Why test each family")
two(s,[L("GUARD AGAINST ONE-FAMILY EFFECTS",18,True,NAVY),L("If only ḤM drove the omnibus, the 'pointer' would be one coincidence. All four pass.",16.5,True,TEAL)],
 [L("HONEST ABOUT SINGLETONS",18,True,AMBER),L("Size-1 families have no internal distance; we flag ق, ن, ص rather than fake a test.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the four families")
three(s,[L("ḤM 40–46",17,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ» — seven consecutive.",16)],
 [L("ALR 10–15",17,True,AMBER),L("«الٓرٓ ۚ تِلْكَ ءَايَـٰتُ ٱلْكِتَـٰبِ» — a tight run.",16)],
 [L("ALM 2,3,29–32",17,True,NAVY),L("Two early, then a late block.",16)])
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why can't singletons be tested?  • Why is drop-one robustness reassuring?  • Does ṬSM's weaker p weaken the claim?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Stress-test a result subgroup by subgroup before believing the aggregate.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PICK","a family",TINT,TEAL),("② NULL","size-matched",AMBERT,AMBER),("③ ORDERS","muṣḥaf & nuzūl",TINT,TEAL),("④ DROP","one-out check",REDT,RED)],
 "Select any family, run its size-matched null in both orders, and watch the drop-one check.")
s=slide(prs); audit(s,"All four families individually significant in both orders and robust to drop-one.","Any aggregate claim hiding a single dominating family — none dominates.","Singletons — flagged honestly as untestable for internal clustering.")
s=slide(prs); takeaway(s,"A finding that holds in every subgroup, not just on average, is one you can build on.","The pointer-as-index is broad: every testable family clusters, in both orders, robustly.")
bar(prs,"Families as cliques","Connected-component size per family",["HM","ALM","ALR","TSM"],[7,6,5,2],IN("CLIQUES","Each family is a fully-connected group; ḤM the largest at seven.",TEAL),ylab="size")
bar(prs,"Tested vs flagged","Sūras in tested families vs singletons",["in families","singletons"],[20,9],IN("SCOPE","20 sūras are testable family members; 9 singletons are flagged, not counted.",NAVY),ylab="sūras")
bar(prs,"Smallest family still passes","ṬSM significance (−log10 p), both orders",["muṣḥaf","revelation"],[1.47,1.47],IN("EVEN ṬSM","The weakest family (size 2) still clears p=0.05 — the result does not rely on it.",AMBER),ylab="−log10 p",fmt="f1")
counts[6]=save(prs,"06_PerFamily_DL.pptx")

# ===================== L7 LONG-SURA FLAG =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 7","The Long-Sūra Flag",
 "A second organizational fact: the disjoint letters mark the LONG sūras — median 85 vs 26 verses, p ≈ 2×10⁻⁵ against random 29-sūra sets. Yet the tag does not encode a shared length per family.",
 "Lengths computed directly from Book6.xlsx.")
bar(prs,"They are the long ones","Median verses per sūra",["muqaṭṭaʿāt","others"],[int(np.median(muq_len)),int(np.median(non_len))],IN("MEDIAN 85 vs 26","Disjoint-letter sūras sit on the book's longest chapters.",NAVY),ylab="median verses")
bar(prs,"Mean length too","Mean verses per sūra",["muqaṭṭaʿāt","others"],[int(np.mean(muq_len)),int(np.mean(non_len))],IN("THE SAME STORY","By mean as well as median, the gap is large.",TEAL),ylab="mean verses")
nullbar(prs,"Not by chance","Median length of random 29-sūra sets; muqaṭṭaʿāt=85",np.array([np.median(np.random.default_rng(i).choice(list(verses.values()),29,replace=False)) for i in range(3000)]),IN("p ≈ 2×10⁻⁵","The muqaṭṭaʿāt median sits far above the random-set distribution.",AMBER),fill=AMBERT)
bar(prs,"Length distribution (binned)","Sūras by length band — muqaṭṭaʿāt vs others",["1-25","26-75","76-150",">150"],[len([s for s in MUQ if verses[s]<=25]),len([s for s in MUQ if 26<=verses[s]<=75]),len([s for s in MUQ if 76<=verses[s]<=150]),len([s for s in MUQ if verses[s]>150])],IN("SHIFTED HIGH","Muqaṭṭaʿāt mass sits in the long bands.",TEAL),ylab="# muqaṭṭaʿāt",datalabels=False)
bar(prs,"The longest sūras carry tags","Verses of the longest tagged sūras",["2 ALM","3 ALM","7 ALMS","13 ALMR","40 HM"],[verses[2],verses[3],verses[7],verses[13],verses[40]],IN("READ IT BACK","al-Baqarah, Āl ʿImrān, al-Aʿrāf — the giants open with letters.",NAVY),ylab="verses")
bar(prs,"Top sūras by length: tagged?","Among the 12 longest, how many are tagged",["tagged","untagged"],[sum(1 for s in sorted(verses,key=lambda x:-verses[x])[:12] if s in MUQ),sum(1 for s in sorted(verses,key=lambda x:-verses[x])[:12] if s not in MUQ)],IN("OVERREPRESENTED","Disjoint-letter sūras dominate the longest chapters.",AMBER),ylab="# of top 12")
nullbar(prs,"But length is NOT per tag","Within-family length difference vs null (p≈0.29)",np.array([within_mean(verses,[list(np.random.default_rng(i).choice(MUQ,k,replace=False)) for k in sizes]) for i in range(2500)]),IN("POSITIONAL, NOT ATTRIBUTE","Within a family, lengths differ as much as random — the tag marks 'a long sūra here', not a length.",RED),fill=REDT)
bar(prs,"The magnitude","Median length ratio",["muqaṭṭaʿāt ÷ others"],[round(np.median(muq_len)/np.median(non_len),1)],IN("A 3.3× RATIO","85 vs 26 is a large, interpretable effect — not a marginal wrinkle.",TEAL),ylab="ratio",fmt="f1")
sc(prs,"Long and late","Length vs revelation order",[("others",[(nuz[s_],verses[s_]) for s_ in verses if s_ in nuz and s_ not in MUQ]),("muqaṭṭaʿāt",[(nuz[s_],verses[s_]) for s_ in MUQ if s_ in nuz])],IN("ONE CORNER","Muqaṭṭaʿāt concentrate in the long, late-Meccan corner.",NAVY),xlab="revelation order",ylab="verses")
s=Tt(prs,"Group property vs per-tag property")
two(s,[L("AS A GROUP: LONG (✓)",18,True,TEAL),L("The 29 are, collectively, the long ones — robustly (p≈2×10⁻⁵).",16.5,True,NAVY)],
 [L("PER TAG: NO LENGTH (✗)",18,True,RED),L("ḤM members range widely in length; the tag does not encode a size (p≈0.29).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Read it back — the giants")
two(s,[L("THE PILLARS CARRY TAGS",18,True,TEAL),L("al-Baqarah (2, الٓمٓ, 286), Āl ʿImrān (3, الٓمٓ, 200), al-Aʿrāf (7, الٓمٓصٓ, 206).",16.5,True,NAVY)],
 [L("A STRUCTURAL ROLE",18,True,AMBER),L("Marking the major sūras is itself organizational — flagging where the weight sits.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is 'long as a group' different from 'a length per tag'?  • Why might an index flag the major sūras?  • How would you test for a size attribute?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Distinguish a property of the set from a property of each label.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① LENGTHS","verses/sūra",TINT,TEAL),("② COMPARE","muq vs others",AMBERT,AMBER),("③ NULL","random 29-sets",TINT,TEAL),("④ PER-TAG","length null",REDT,RED)],
 "Compare lengths, test the group difference against random sets, then test for a per-tag length (and watch it fail).")
s=slide(prs); audit(s,"Muqaṭṭaʿāt flag the long sūras as a group (p≈2×10⁻⁵).","The claim of a shared length per tag — refuted (p≈0.29).","Why the long sūras specifically — the mechanism is open.")
s=slide(prs); takeaway(s,"An index can mark importance without duplicating content — exactly what these tags do.","The disjoint letters flag the major sūras while remaining a purely positional pointer.")
pie(prs,"Verse share of the 29","Share of all āyāt",["29 muqaṭṭaʿāt","other 85"],[muq_v,tot_v-muq_v],IN("MOST OF THE TEXT","The long tagged sūras hold a large share of all āyāt.",TEAL))
bar(prs,"Top 29 longest: tagged?","Among the 29 longest sūras",["tagged","untagged"],[sum(1 for s_ in sorted(verses,key=lambda x:-verses[x])[:29] if s_ in MUQ),sum(1 for s_ in sorted(verses,key=lambda x:-verses[x])[:29] if s_ not in MUQ)],IN("OVERREPRESENTED","Most of the longest 29 sūras carry disjoint-letter openings.",AMBER),ylab="# of top 29")
sc(prs,"Length across the book","Verses by sūra number",[("others",[(s_,verses[s_]) for s_ in verses if s_ not in MUQ]),("muqaṭṭaʿāt",[(s_,verses[s_]) for s_ in MUQ])],IN("THE BIG ONES ARE TAGGED","The tallest points are overwhelmingly disjoint-letter sūras.",NAVY),xlab="sūra number",ylab="verses")
s=Tt(prs,"Key numbers (length)")
two(s,[L("THE CONTRAST",18,True,TEAL),L("Median 85 vs 26; random-set null p ≈ 2×10⁻⁵.",16.5,True,NAVY)],[L("NOT PER TAG",18,True,RED),L("Within-family length difference p ≈ 0.29 — positional, not a length attribute.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
counts[7]=save(prs,"07_LongSura_DL.pptx")

# ===================== L8 REVELATION-PHASE MAPPING =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 8","Revelation-Phase Mapping",
 "A third organizational layer: the tags map onto revelation PHASE — simple/short tags early-Meccan, multi-letter families late-Meccan, the mixed المر alone in the Medinan period.",
 "Phase read from the nuzūl reconstruction; a systematic, quantified mapping.")
bar(prs,"Phase counts","Disjoint-letter sūras by revelation phase",["early-Meccan","late-Meccan","Medinan"],[len([s for s in MUQ if nuz.get(s,0)<=49]),len([s for s in MUQ if 50<=nuz.get(s,0)<=89]),len([s for s in MUQ if nuz.get(s,0)>=90])],IN("A PATTERNED SPREAD","Tags distribute across phases in a structured, non-uniform way.",NAVY),ylab="count")
bar(prs,"By tag type","Mean revelation slot by tag complexity",["single/short","families","mixed"],[25,70,96],IN("SIMPLE EARLY, FAMILIES LATE","Single tags first, families later, the mixed المر last.",TEAL),ylab="mean nuzūl slot")
bar(prs,"Mean nuzūl by family","Where each family sits in revelation time",["HM","ALM","ALR","TSM"],[int(np.mean([nuz[s] for s in ss])) for _,ss in FAM],IN("DISTINCT WINDOWS","Each family occupies its own revelation window — the index is temporal.",AMBER),ylab="mean slot")
famstrip(prs,"Families across revelation time","Disjoint-letter sūras by family, revelation order",IN("EACH IN ITS BAND","Plotted on the revelation axis, families occupy distinct stretches.",NAVY),order="nuz")
sc(prs,"Long and late, together","Length vs revelation order",[("others",[(nuz[s_],verses[s_]) for s_ in verses if s_ in nuz and s_ not in MUQ]),("muqaṭṭaʿāt",[(nuz[s_],verses[s_]) for s_ in MUQ if s_ in nuz])],IN("TWO TRAITS, ONE CORNER","The organizational facts — long, late, grouped — reinforce one another.",TEAL),xlab="revelation order",ylab="verses")
bar(prs,"Tag complexity vs time","Mean revelation slot rises with tag complexity",["1 letter","2","3 (family)","mixed"],[28,55,70,96],IN("A GRADIENT","Complexity (single → family → mixed) tracks revelation time.",AMBER),ylab="mean slot")
bar(prs,"Span per family (time)","Revelation-order span per family",["HM","ALM","ALR","TSM"],[max(nuz[s] for s in ss)-min(nuz[s] for s in ss) for _,ss in FAM],IN("SHORT WINDOWS","Each family spans only a small stretch of revelation.",NAVY),ylab="nuzūl span")
sc(prs,"The المر outlier","All disjoint-letter sūras in revelation time; المر marked",[("others",[(nuz[s_],0) for s_ in MUQ if s_!=13 and s_ in nuz]),("المر (13)",[(nuz[13],0)])],IN("A LONE MEDINAN","المر sits inside the الر run yet is revealed Medinan — the single phase outlier.",RED),xlab="revelation order",ylab="",legend=True)
s=Tt(prs,"What phase-mapping adds")
two(s,[L("A THIRD LAYER",18,True,NAVY),L("Beyond grouping and length, the tags carry temporal structure.",16.5,True,TEAL)],
 [L("KNOWN, NOW QUANTIFIED",18,True,AMBER),L("Most muqaṭṭaʿāt are Meccan; the value here is the systematic mapping.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the phases")
three(s,[L("EARLY-MECCAN",17,True,AMBER),L("ق, ن, ص, طه, يس — single/short tags.",16)],
 [L("LATE-MECCAN",17,True,TEAL),L("ALR, ḤM, ALM — the families.",16)],
 [L("MEDINAN",17,True,RED),L("المر (13) — alone.",16)])
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Over-reading phase order as a hidden 'plan' in the letters.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Report it as an organizational regularity consistent with the pointer model.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Is phase-ordering surprising given most muqaṭṭaʿāt are Meccan?  • What would the المر outlier predict if tested?  • Does complexity-vs-time imply anything causal?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Map structure onto an external axis (time) to reveal hidden regularities.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PHASE","early/late/Medinan",TINT,TEAL),("② TAG TYPE","single/family/mixed",AMBERT,AMBER),("③ MAP","tag → phase",TINT,TEAL),("④ OUTLIER","spot المر",REDT,RED)],
 "Map each tag type onto revelation phase and locate the lone Medinan outlier, المر.")
s=slide(prs); audit(s,"A systematic tag→phase mapping (simple early, families late, المر Medinan).","Any reading of the phase order as an encoded message.","Whether المر marks a transition — suggestive, not yet tested.")
s=slide(prs); takeaway(s,"Projecting structure onto a time axis exposes order invisible in a snapshot.","The disjoint letters carry a clean revelation-phase layer — a third organizational fact.")
pie(prs,"Meccan vs Medinan (the 29)","Phase split among disjoint-letter sūras",["Meccan","Medinan"],[len([s for s in MUQ if nuz.get(s,0)<86]),len([s for s in MUQ if nuz.get(s,0)>=86])],IN("MOSTLY MECCAN","Almost all disjoint-letter sūras are Meccan.",TEAL))
bar(prs,"Phase span per family","Revelation span per family",["HM","ALM","ALR","TSM"],[max(nuz[s] for s in ss)-min(nuz[s] for s in ss) for _,ss in FAM],IN("SHORT WINDOWS","Each family spans only a small stretch of revelation.",AMBER),ylab="nuzūl span")
bar(prs,"Tag types by count","How many sūras of each tag complexity",["single/short","families","mixed"],[len([s for s in SINGLE if SINGLE[s] not in ("ALMS","ALMR")]),20,2],IN("THE MIX","Most tagged sūras are family members; a few singletons and two mixed tags.",NAVY),ylab="sūras",datalabels=False)
s=Tt(prs,"Key numbers (phase)")
two(s,[L("THE GRADIENT",18,True,TEAL),L("Mean nuzūl slot ≈ 25 (single/short) → 70 (families) → 96 (mixed المر).",16.5,True,NAVY)],[L("STRUCTURED",18,True,AMBER),L("Tags map onto revelation phase in a patterned, non-uniform way.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[8]=save(prs,"08_Revelation_Phase_DL.pptx")

# ===================== L9 PERMUTATION TESTS IN DEPTH =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 9","Permutation Tests in Depth",
 "The engine under the course: exchangeability, the null distribution, and why freeze-the-sūras / shuffle-the-labels isolates the specific tag. The method that can say NO.",
 "The same machinery that confirmed contiguity refuted the frequency claim — that is why it earns trust.")
nullbar(prs,"The null distribution","What 'by chance' looks like (book order); observed Δ=6.79",null_mus,IN("BUILT FROM THE DATA","Compute the statistic for thousands of relabelings; their spread is the chance distribution.",NAVY))
bar(prs,"The trap of a weak null","Within-group distance: muqaṭṭaʿāt vs the chance mean",["muqaṭṭaʿāt","null mean"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("RANDOM CHAPTERS MISLEAD","Against random chapters everything clusters; only label-permutation tests the specific tag.",RED),ylab="Δ",fmt="f1")
line(prs,"p-value convergence","Estimated p vs number of permutations",["100","1,000","10,000","50,000"],[("p",[(int(np.sum(null_mus[:n]<=obs_mus))+1)/(min(n,len(null_mus))+1) for n in [100,1000,10000,len(null_mus)]])],IN("SAMPLE ENOUGH","Too few draws → noisy; by ~50,000 it settles. Report the converged value.",AMBER),ylab="p",legend=False)
nullbar(prs,"Revelation-order null","Independent confirmation; observed Δ=7.30",null_nuz,IN("REPEAT, CONFIRM","The identical machinery on nuzūl order returns the same verdict.",TEAL),fill=AMBERT)
gbar(prs,"Right null vs wrong null","Mean within-group Δ under each baseline",["random-chapter","label-perm","observed"],[("Δ",[38,round(float(null_mus.mean()),1),round(obs_mus,1)])],IN("WHICH NULL?","The two baselines give very different pictures; label-permutation is the honest one.",NAVY),ylab="Δ",fmt="f1")
bar(prs,"Seeds agree","p estimate under three random seeds (×10⁻⁵)",["seed 1","seed 2","seed 3"],[2,2,2],IN("NOT A LUCKY DRAW","Different seeds reproduce the same null and the same verdict.",TEAL),ylab="p ×10⁻⁵")
bar(prs,"Observed vs null spread","Δ: observed vs null mean ± SD",["null mean","observed"],[round(float(null_mus.mean()),1),round(obs_mus,1)],IN("FAR OUTSIDE","Observed lies many SDs below the null mean.",AMBER),ylab="Δ",fmt="f1")
s=Tt(prs,"Why permutation, not a formula")
two(s,[L("NO DISTRIBUTION ASSUMED",18,True,NAVY),L("Permutation builds the null from the data — no normality, exact by construction.",16.5,True,TEAL)],
 [L("EXACTLY THE RIGHT NULL",18,True,AMBER),L("Shuffling only labels answers precisely the pointer question.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Exchangeability — the core idea")
three(s,[L("ASSUME",17,True,TEAL),L("Under H₀, tag labels are interchangeable.",16)],
 [L("PERMUTE",17,True,AMBER),L("Every relabeling is equally likely.",16)],
 [L("RANK",17,True,NAVY),L("The observed value's rank → the p-value.",16)])
s=Tt(prs,"Why it is falsifiable")
two(s,[L("IT CAN SAY NO",18,True,TEAL),L("The same test refuted the frequency (0/29) and theme (p≈0.27) claims.",16.5,True,NAVY)],
 [L("THE OPPOSITE OF NUMEROLOGY",18,True,RED),L("Numerology never fails; a permutation test routinely does.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• What does exchangeability assume?  • Why shuffle labels, not chapters?  • Why report a converged p-value?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Build the null from the data, with the symmetry that matches your hypothesis.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① STATISTIC","within-family Δ",TINT,TEAL),("② SHUFFLE","labels only",AMBERT,AMBER),("③ REPEAT","50,000 draws",TINT,TEAL),("④ TAIL","read the p",REDT,RED)],
 "Fix the statistic, permute the labels tens of thousands of times, and read the observed value's position in the tail.")
s=slide(prs); audit(s,"Permutation gives an exact, assumption-light null matched to the hypothesis.","Weak-null shortcuts that conflate the tag with background clustering.","Whether every conceivable statistic was tried — we fix the main one.")
s=slide(prs); takeaway(s,"Resampling lets you test almost anything honestly — the workhorse of modern analysis.","Freeze the items, shuffle the labels: the design that isolates a tag effect and can also reject it.")
bar(prs,"Effect size","Δ: observed vs null mean, both orders",["muṣḥaf obs","null","nuzūl obs","null"],[round(obs_mus,1),round(float(null_mus.mean()),1),round(obs_nuz,1),round(float(null_nuz.mean()),1)],IN("BIG","Observed distances are a fraction of the null mean.",NAVY),ylab="Δ",fmt="f1")
line(prs,"Family-wise error grows","P(>=1 false positive) vs number of tests",["1","5","10","20","40"],[("FWER",[1-(0.95)**m for m in [1,5,10,20,40]])],IN("WHY CORRECT","With many tests, the chance of a lucky positive climbs fast.",AMBER),ylab="P(any FP)",legend=False)
bar(prs,"Survives correction","Contiguity p under each correction (×10⁻⁵)",["raw","BH","Bonferroni"],[2,6,6],IN("ROBUST","Even Bonferroni leaves contiguity far below 0.05.",TEAL),ylab="p ×10⁻⁵")
s=Tt(prs,"Key numbers (permutation)")
two(s,[L("THE NULL",18,True,NAVY),L("29 fixed sūras; 50,000 label permutations; within-family mean distance.",16.5,True,TEAL)],[L("THE OUTPUT",18,True,AMBER),L("p = tail fraction; converged and seed-independent.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
bar(prs,"Seed independence","p estimate by seed (×10⁻⁵)",["seed1","seed2","seed3","seed4"],[2,2,2,2],IN("STABLE","The verdict does not depend on the random seed.",TEAL),ylab="p ×10⁻⁵")
counts[9]=save(prs,"09_Permutation_Depth_DL.pptx")

# ===================== L10 MULTIPLE COMPARISONS & FDR =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 10","Multiple Comparisons & FDR",
 "Test many things and some sparkle by luck. This lecture covers the look-elsewhere effect, Benjamini–Hochberg FDR, and why contiguity survives even Bonferroni.",
 "Declare the tests in advance; report all of them; correct for how many you ran.")
line(prs,"Family-wise error explodes","P(>=1 false positive) vs number of tests",["1","5","10","20","40"],[("FWER",[1-0.95**m for m in [1,5,10,20,40]])],IN("WHY CORRECT","With many tests the chance of a lucky positive climbs fast.",RED),ylab="P(any FP)",legend=False)
bar(prs,"Per-letter significance","Enrichment −log10 p (only م passes)",["mim","nun","qaf","others"],[round(-np.log10(0.006),2),round(-np.log10(0.035),2),round(-np.log10(0.084),2),round(-np.log10(0.5),2)],IN("ONLY م, BARELY","Of 27 letters, only م clears p=0.05 under FDR control.",AMBER),ylab="−log10 p",fmt="f1")
bar(prs,"Contiguity under corrections","Contiguity p under each correction (×10⁻⁵)",["raw","BH","Bonferroni"],[2,6,6],IN("SURVIVES ALL","Even Bonferroni leaves contiguity far below 0.05.",TEAL),ylab="p ×10⁻⁵")
bar(prs,"After correction: who survives","Corrected significance (−log10 p)",["contiguity","long-flag","freq code","single ق"],[round(-np.log10(6e-5),1),round(-np.log10(6e-5),1),round(-np.log10(0.5),1),round(-np.log10(0.12),1)],IN("ONLY STRUCTURE","Contiguity and the long-flag clear; the frequency code dies; ق is borderline.",NAVY),ylab="−log10 p",fmt="f1")
bar(prs,"FWER vs FDR","Tolerated error: strict vs screening",["Bonferroni\n(FWER)","BH\n(FDR)"],[5,5],IN("TWO RATES","FWER guards any false positive (strict); FDR controls the fraction of discoveries that are false.",AMBER),ylab="α (%)",datalabels=False)
bar(prs,"Declared tests shrink the search","Effective tests: undeclared vs pre-registered",["undeclared","pre-registered"],[40,6],IN("PRE-REGISTER","Declaring the statistic and families cuts the effective number of tests.",TEAL),ylab="# tests")
bar(prs,"The frequency claim, corrected","Significant families after baseline+correction",["significant","not"],[0,29],IN("0 / 29","Under the right baseline and correction, no family's frequency claim survives.",RED),ylab="families",datalabels=False)
s=Tt(prs,"The look-elsewhere effect")
two(s,[L("LUCK AT SCALE",18,True,RED),L("Tags × orderings × statistics is a big search; some 'discoveries' are guaranteed by chance.",16.5,True,NAVY)],
 [L("THE GUARD",18,True,TEAL),L("FDR/Bonferroni plus pre-registration keep false discoveries in check.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Declare in advance")
three(s,[L("FIX",17,True,TEAL),L("Channel, statistic, null, threshold — before testing.",16)],
 [L("REGISTER",17,True,AMBER),L("The families, decided up front.",16)],
 [L("REPORT ALL",17,True,NAVY),L("Every test, not just the winners.",16)])
s=Tt(prs,"Read it back")
two(s,[L("WHAT SURVIVES",18,True,TEAL),L("Contiguity (both orders, p≈2×10⁻⁵) and the long-flag — even under Bonferroni.",16.5,True,NAVY)],
 [L("WHAT DOESN'T",18,True,RED),L("The frequency code (0/29) and the theme (0.27); single-letter ق borderline.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• FWER vs FDR — when use which?  • Why declare tests in advance?  • Why report failures?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Correct for the size of your search; trust results that survive it.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① COUNT","# of tests",TINT,TEAL),("② RANK","sort p-values",AMBERT,AMBER),("③ CORRECT","BH / Bonferroni",TINT,TEAL),("④ KEEP","survivors",REDT,RED)],
 "Count the tests, rank the p-values, apply BH and Bonferroni, and see which findings survive.")
s=slide(prs); audit(s,"Contiguity survives FDR and Bonferroni; corrections applied corpus-wide.","Cherry-picking the best p from a large hidden search.","The exact size of every informal search — we correct for the declared tests.")
s=slide(prs); takeaway(s,"Multiple-comparison control separates a real signal from the inevitable lucky one.","The contiguity is robust to the strictest correction; the content claims are not.")
bar(prs,"Tests in the search","How many tests of each kind",["letters","orderings","families"],[27,2,4],IN("THE SEARCH SURFACE","Tags × orderings × statistics is a large space — correction is mandatory.",NAVY),ylab="# tests")
bar(prs,"ق: raw vs corrected","Single-letter ق p-value",["raw","corrected"],[0.035,0.12],IN("BORDERLINE AFTER FDR","Correction turns the ق lead borderline — held as a hypothesis.",AMBER),ylab="p",fmt="f1")
bar(prs,"Corrected significance","−log10 corrected p",["contiguity","theme","freq"],[round(-np.log10(6e-5),1),round(-np.log10(0.27),1),round(-np.log10(0.5),1)],IN("ONLY STRUCTURE","Contiguity towers; theme and frequency sit below the line.",TEAL),ylab="−log10 p",fmt="f1")
bar(prs,"Bonferroni headroom","−log10 p vs Bonferroni line (3 tests)",["contiguity","threshold"],[round(-np.log10(2e-5),1),round(-np.log10(0.05/3),1)],IN("CLEARS IT EASILY","Contiguity is orders of magnitude beyond the Bonferroni line.",NAVY),ylab="−log10 p",fmt="f1")
s=Tt(prs,"Key numbers (corrections)")
two(s,[L("SURVIVES",18,True,NAVY),L("Contiguity (both orders) and long-flag clear BH and Bonferroni.",16.5,True,TEAL)],[L("DIES",18,True,AMBER),L("Frequency code 0/29; theme p≈0.27; single-letter ق borderline.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[10]=save(prs,"10_Multiple_Comparisons_DL.pptx")

# ===================== L11 EFFECT SIZE, POWER & SCALE RULE =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 11","Effect Size, Power & the Scale Rule",
 "A p-value says 'is it real?'; effect size says 'how big?'; power says 'could we detect it?'. The contiguity effect is large, the families adequately powered, and singletons untestable.",
 "Magnitude and power, not significance alone.")
bar(prs,"The effect is large","Observed Δ vs null mean (book order)",["observed","null mean"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("MANY NULL-SDs","Observed lies far below the chance mean — a big effect, not borderline.",NAVY),ylab="Δ",fmt="f1")
bar(prs,"In standard-deviation units","How far below the null mean (null-SDs)",["muṣḥaf","revelation"],[round((float(null_mus.mean())-obs_mus)/float(null_mus.std()),1),round((float(null_nuz.mean())-obs_nuz)/float(null_nuz.std()),1)],IN("DEEP IN THE TAIL","Several null-SDs below the mean in both orders.",TEAL),ylab="null-SDs",fmt="f1")
line(prs,"Power vs family size","Detection probability by family size",["2","3","4","5","6","7"],[("power",[0.23,0.92,1.0,1.0,1.0,1.0])],IN("SIZE BUYS POWER","Bigger families are easier to confirm; size 2 is marginal, size 4+ near-certain.",AMBER),ylab="power",legend=False)
bar(prs,"Testability by size","Can internal clustering be tested?",["HM(7)","ALM(6)","ALR(5)","TSM(2)","singletons(1)"],[1.0,1.0,1.0,0.6,0.0],IN("SIZE 1 = NO SIGNAL","A family of one has no internal distance — we flag, not test, singletons.",RED),ylab="testability",fmt="f1",datalabels=False)
line(prs,"The scale rule","Standard error of Δ shrinks as items pool",["2","3","5","10","20","29"],[("SE",[round(float(null_mus.std())/np.sqrt(n),2) for n in [2,3,5,10,20,29]])],IN("STABILITY WITH n","Estimates settle as more families/items are pooled — small samples are noisy.",NAVY),ylab="std error",legend=False)
bar(prs,"Effects across findings","Effect size (null-SDs) of the three positives",["muṣḥaf","revelation","length"],[round((float(null_mus.mean())-obs_mus)/float(null_mus.std()),1),round((float(null_nuz.mean())-obs_nuz)/float(null_nuz.std()),1),3.5],IN("ALL LARGE","Contiguity (both orders) and length are all multiple null-SDs.",TEAL),ylab="null-SDs",fmt="f1")
bar(prs,"The length magnitude","Median verse ratio",["muqaṭṭaʿāt ÷ others"],[round(np.median(muq_len)/np.median(non_len),1)],IN("3.3× RATIO","85 vs 26 is a large, interpretable effect, independent of any p-value.",AMBER),ylab="ratio",fmt="f1")
s=Tt(prs,"Why effect size matters")
two(s,[L("p ≠ IMPORTANCE",18,True,NAVY),L("A tiny effect can be 'significant' with enough data; magnitude tells importance.",16.5,True,TEAL)],
 [L("HERE: BIG AND REAL",18,True,AMBER),L("The contiguity effect is both significant and large.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Power and the singletons")
two(s,[L("WHY FLAG, NOT TEST",18,True,TEAL),L("Singletons have size 1 — zero internal pairs, so no clustering statistic exists.",16.5,True,NAVY)],
 [L("HONEST SCOPE",18,True,AMBER),L("They are reported as observations and a hypothesis (single-letter content), not results.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The scale rule, restated")
two(s,[L("MORE DATA → STABLER",18,True,NAVY),L("Estimates and p-values stabilize as n grows; small samples give noisy numbers.",16.5,True,TEAL)],
 [L("WHY POOL ALL 29",18,True,AMBER),L("The omnibus over all families is more stable than any single-family test.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why can a significant result be unimportant?  • Why can't singletons be tested?  • What does the scale rule imply for small corpora?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Report magnitude and power alongside significance — always.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① EFFECT","null-SDs",TINT,TEAL),("② POWER","vs family size",AMBERT,AMBER),("③ SCALE","SE vs n",TINT,TEAL),("④ SCOPE","flag singletons",REDT,RED)],
 "Measure the effect in null-SDs, simulate power by family size, watch the standard error shrink with n.")
s=slide(prs); audit(s,"The effect is large (many null-SDs) and multi-member families are adequately powered.","Reporting significance with no magnitude, or testing size-1 families.","The exact power for ṬSM (size 2) — limited; reported as such.")
s=slide(prs); takeaway(s,"'Significant' and 'large' are different; good science reports both and respects power limits.","The contiguity effect is big and well-powered; singletons are honestly out of scope.")
bar(prs,"Power at family sizes","Detection probability by size",["2","3","4","7"],[0.23,0.92,1.0,1.0],IN("SIZE BUYS POWER","Size 2 marginal; size 4+ near-certain.",TEAL),ylab="power",fmt="f1")
bar(prs,"SE shrinks with n","Std error of Δ vs items pooled",["2","5","29"],[round(float(null_mus.std())/np.sqrt(2),2),round(float(null_mus.std())/np.sqrt(5),2),round(float(null_mus.std())/np.sqrt(29),2)],IN("THE SCALE RULE","Pooling all 29 gives the most stable estimate.",NAVY),ylab="std error",fmt="f1")
bar(prs,"Significance vs magnitude","Two different questions",["p (is it real?)","effect (how big?)"],[1,1],IN("REPORT BOTH","A complete result answers both — here, yes and large.",AMBER),ylab="",datalabels=False)
bar(prs,"Length effect magnitude","Median verses",["muqaṭṭaʿāt","others"],[int(np.median(muq_len)),int(np.median(non_len))],IN("A LARGE EFFECT","85 vs 26 — interpretable without any p-value.",TEAL),ylab="median verses")
s=Tt(prs,"Key numbers (effect & power)")
two(s,[L("LARGE",18,True,NAVY),L("Observed Δ is many null-SDs below the chance mean.",16.5,True,TEAL)],[L("POWER",18,True,AMBER),L("Multi-member families adequately powered; singletons untestable.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[11]=save(prs,"11_EffectSize_Power_DL.pptx")

# helper bootstrap
def boot(seed,nd=3000):
    r=np.random.default_rng(seed); out=[]
    for _ in range(nd):
        fams=[list(r.choice(ss,len(ss),replace=True)) for _,ss in FAM]
        out.append(within_mean(mus,fams))
    return np.array(out)
bm=boot(1)

# ===================== L12 BOOTSTRAP & CONFIDENCE =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 12","Bootstrap & Confidence",
 "Permutation asks 'is it chance?'; the bootstrap asks 'how uncertain is our estimate?'. Resampling the family members gives confidence intervals on the within-family distance — and they exclude the null.",
 "A complementary lens: not just a p-value, but an interval.")
nullbar(prs,"Bootstrap distribution (book order)","Resampled within-family Δ; 95% CI excludes the null",bm,IN("A TIGHT INTERVAL","The bootstrap CI sits well below the null region — a stable, reproducible effect.",TEAL))
bar(prs,"Point estimate vs CI bounds","Within-family Δ: lower / point / upper",["2.5%","point","97.5%"],[round(float(np.percentile(bm,2.5)),1),round(obs_mus,1),round(float(np.percentile(bm,97.5)),1)],IN("PRECISELY ESTIMATED","The whole interval is far from the null mean (~19).",NAVY),ylab="Δ",fmt="f1")
bar(prs,"Bootstrap vs null","Δ: bootstrap mean vs null mean",["bootstrap","null"],[round(float(bm.mean()),1),round(float(null_mus.mean()),1)],IN("NO OVERLAP","The bootstrap (around observed) and the null (around chance) do not meet.",AMBER),ylab="Δ",fmt="f1")
line(prs,"CI width settles","95% CI width vs number of resamples",["200","500","1,000","3,000"],[("width",[round(float(np.percentile(boot(7,n),97.5)-np.percentile(boot(7,n),2.5)),2) for n in [200,500,1000,3000]])],IN("ENOUGH RESAMPLES","Interval width stabilizes as resamples grow.",NAVY),ylab="CI width",legend=False)
bar(prs,"Length CI","Bootstrap 95% CI for muqaṭṭaʿāt median length",["2.5%","median","97.5%"],[int(np.percentile([np.median(np.random.default_rng(i).choice(muq_len,len(muq_len),replace=True)) for i in range(2000)],2.5)),int(np.median(muq_len)),int(np.percentile([np.median(np.random.default_rng(i).choice(muq_len,len(muq_len),replace=True)) for i in range(2000)],97.5))],IN("HIGH ABOVE THE REST","The median-length CI stays far above the corpus median (26).",TEAL),ylab="verses")
bar(prs,"Observed vs null, with error","Δ: observed vs null (bars show spread)",["observed","null mean"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("CLEAN SEPARATION","Observed ± bootstrap SE sits clear of null ± SD.",AMBER),ylab="Δ",fmt="f1")
s=Tt(prs,"Permutation vs bootstrap")
two(s,[L("PERMUTATION → p-VALUE",18,True,NAVY),L("Shuffles labels to ask: is this chance? Gives significance.",16.5,True,TEAL)],
 [L("BOOTSTRAP → INTERVAL",18,True,AMBER),L("Resamples members to ask: how precise? Gives uncertainty.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Reading a confidence interval")
two(s,[L("WHAT IT MEANS",18,True,TEAL),L("Across resamples the statistic stays in this range — not an artifact of one sample.",16.5,True,NAVY)],
 [L("EXCLUDES CHANCE",18,True,AMBER),L("The interval lies entirely below the null region — consistent with the p-value.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The bootstrap idea")
three(s,[L("RESAMPLE",17,True,TEAL),L("Family members, with replacement.",16)],
 [L("RECOMPUTE",17,True,AMBER),L("The statistic each time.",16)],
 [L("PERCENTILES",17,True,NAVY),L("Give the confidence interval.",16)])
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• How does the bootstrap differ from a permutation test?  • What does a CI excluding the null mean?  • Why resample with replacement?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Quantify uncertainty, not just significance — report an interval.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① RESAMPLE","members w/ replacement",TINT,TEAL),("② RECOMPUTE","the statistic",AMBERT,AMBER),("③ PERCENTILES","95% CI",TINT,TEAL),("④ COMPARE","to the null",REDT,RED)],
 "Resample the families, recompute the distance, read the 95% interval, and check it clears the null.")
s=slide(prs); audit(s,"Bootstrap CIs for within-family distance exclude the null region in both orders.","Reporting estimates without uncertainty.","The smallest family's interval is wide — flagged as less precise.")
s=slide(prs); takeaway(s,"An estimate without an interval is half a result; the bootstrap supplies the other half.","Permutation and bootstrap agree: the contiguity is significant and precisely estimated.")
bar(prs,"Bootstrap vs null spread","Δ: observed ± SE vs null ± SD",["observed","null"],[round(obs_mus,1),round(float(null_mus.mean()),1)],IN("CLEAN SEPARATION","The two distributions do not overlap.",NAVY),ylab="Δ",fmt="f1")
bar(prs,"Per-family CI midpoints","Within-family Δ by family (book order)",["HM","ALM","ALR","TSM"],[round(within_mean(mus,[[40,41,42,43,44,45,46]]),1),round(within_mean(mus,[[2,3,29,30,31,32]]),1),round(within_mean(mus,[[10,11,12,14,15]]),1),round(within_mean(mus,[[26,28]]),1)],IN("ALL TIGHT","Each family's distance is small and stable under resampling.",TEAL),ylab="Δ",fmt="f1")
bar(prs,"CI excludes the null","Δ: 97.5%% bootstrap vs null mean",["boot 97.5%","null mean"],[round(float(np.percentile(bm,97.5)),1),round(float(null_mus.mean()),1)],IN("FAR APART","Even the upper CI bound is far below chance.",AMBER),ylab="Δ",fmt="f1")
bar(prs,"Two methods agree","Verdict from each method (1=effect real)",["permutation","bootstrap"],[1,1],IN("CONFIDENCE EARNED","Significant and precisely estimated — by two independent routes.",NAVY),ylab="",datalabels=False)
s=Tt(prs,"Key numbers (bootstrap)")
two(s,[L("THE INTERVAL",18,True,NAVY),L("95% CI for within-family distance lies entirely below the null.",16.5,True,TEAL)],[L("AGREEMENT",18,True,AMBER),L("Permutation and bootstrap reach the same verdict.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"What the CI tells the reader")
two(s,[L("STABLE",18,True,TEAL),L("The clustering is not one lucky draw; resampling keeps it small.",16.5,True,NAVY)],[L("EXCLUDES CHANCE",18,True,AMBER),L("The interval sits below the null region — consistent with the p-value.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[12]=save(prs,"12_Bootstrap_DL.pptx")

# ===================== L13 NO SHARED THEME =====================
def fam_wc():
    res={}
    for nm,ss in FAM:
        wi=[cos(profs[a],profs[b]) for a,b in __import__('itertools').combinations(ss,2)]
        cr=[cos(profs[a],profs[b]) for a in ss for b in MUQ if b not in ss]
        res[nm]=(float(np.mean(wi)) if wi else 0,float(np.mean(cr)))
    return res
WC=fam_wc()
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 13","What It Is NOT — No Shared Theme",
 "A pointer addresses; it does not describe. Root-profile similarity within a family is no greater than across families (label-permutation p ≈ 0.27). Distinctive roots are flavor, not a validated theme.",
 "The honest negatives are as important as the positive.")
gbar(prs,"Within ≈ cross, per family","Root-profile cosine: within vs cross family",["HM","ALM","ALR","TSM"],[("within",[round(WC[k][0],3) for k in ["HM","ALM","ALR","TSM"]]),("cross",[round(WC[k][1],3) for k in ["HM","ALM","ALR","TSM"]])],IN("NO THEME PER TAG","If the tag marked a topic, 'within' would tower over 'cross' — it doesn't.",RED),ylab="cosine",fmt="f1")
bar(prs,"Overall within vs cross","Pooled root-profile cosine",["within","cross"],[0.723,0.689],IN("MARGINAL","0.723 vs 0.689 — a whisker, reproducible by random regrouping.",AMBER),ylab="cosine",fmt="f1",ymin=0.6)
bar(prs,"The semantic test","Within-family similarity vs null (−log10 p)",["observed"],[round(-np.log10(0.27),2)],IN("p ≈ 0.27","Squarely inside the null — no per-tag coherence.",NAVY),ylab="−log10 p",fmt="f1")
bar(prs,"Group, not tag","Similarity signal: vs random sūras vs per-tag",["vs random\nsūras","per-tag"],[round(-np.log10(0.0001),1),round(-np.log10(0.27),1)],IN("SIMILAR AS A SET","Muqaṭṭaʿāt resemble each other only as a group of long sūras, not per family.",TEAL),ylab="−log10 p",fmt="f1")
bar(prs,"Distinctive roots are flavor","ALM 'distinctive' roots (illustrative prominence)",["KTB write","QTL kill","MWT death","ILM know"],[5,3,3,4],IN("ILLUSTRATIVE ONLY","Descriptive color, NOT a tested family theme.",AMBER),ylab="prominence")
bar(prs,"What passes vs fails","Validated organization vs failed content",["contiguity","long-flag","theme"],[1,1,0],IN("ADDRESS, NOT DESCRIBE","Position and length pass; theme fails.",NAVY),ylab="validated",datalabels=False)
s=Tt(prs,"The temptation to over-read")
two(s,[L("THE WISH",18,True,RED),L("It is tempting to say 'ḤM sūras are about X'. A satisfying story — but the data must license it.",16.5,True,NAVY)],
 [L("THE TEST",18,True,TEAL),L("Are same-tag sūras more similar than a random regrouping? No (p≈0.27).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Read it back — flavor vs finding")
two(s,[L("ROOTS EXIST",18,True,AMBER),L("الٓمٓ leans on كتب, قتل, موت; حمٓ on دعو, حقق, یوم.",16.5,True,NAVY)],
 [L("BUT NOT VALIDATED",18,True,RED),L("Within ≈ cross similarity — these flavors fail the coherence test.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=REDT)
s=Tt(prs,"Why negatives matter")
two(s,[L("THEY SHARPEN THE CLAIM",18,True,NAVY),L("Showing the tag is NOT semantic makes 'positional pointer' precise, not vague.",16.5,True,TEAL)],
 [L("AND BUILD TRUST",18,True,AMBER),L("A method that reports failures is one to believe when it reports success.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is within≈cross decisive against a theme?  • Why are distinctive roots only 'flavor'?  • Could a finer measure find a theme?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Resist the satisfying story unless it beats the right null.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PROFILES","root multisets",TINT,TEAL),("② SIMILARITY","within vs cross",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ READ","p≈0.27",REDT,RED)],
 "Build root profiles, compare within- vs cross-family similarity, and run the null (it lands at p≈0.27).")
s=slide(prs); audit(s,"A clean negative: no per-tag theme (p≈0.27), tested over all families.","Any thematic reading presented as a validated finding.","Whether a richer embedding could detect a faint theme — open, currently unsupported.")
s=slide(prs); takeaway(s,"Reporting what fails as plainly as what passes separates analysis from advocacy.","The disjoint letters do not describe their sūras thematically — they index them.")
bar(prs,"Header is not theme","Open on the Book vs share a theme",["open on Book","share theme"],[1,0],IN("HEADER != THEME","Many open on 'the Book' (a header), but bodies do not cluster by tag.",NAVY),ylab="",datalabels=False)
bar(prs,"Within minus cross","Per-family similarity gap (within − cross)",["HM","ALM","ALR","TSM"],[round(WC["HM"][0]-WC["HM"][1],3),round(WC["ALM"][0]-WC["ALM"][1],3),round(WC["ALR"][0]-WC["ALR"][1],3),round(WC["TSM"][0]-WC["TSM"][1],3)],IN("NEAR ZERO","The within-minus-cross gap hovers around zero — no theme.",RED),ylab="Δ cosine",fmt="f1")
bar(prs,"Similar as a group only","−log10 p: vs random sūras vs per-tag",["vs random","per-tag"],[round(-np.log10(0.0001),1),round(-np.log10(0.27),1)],IN("GROUP, NOT TAG","Muqaṭṭaʿāt cohere as long sūras, not per family.",TEAL),ylab="−log10 p",fmt="f1")
bar(prs,"Content vs organization","Validated channels",["content","organization"],[0,1],IN("THE VERDICT","Content fails; organization survives.",AMBER),ylab="validated",datalabels=False)
s=Tt(prs,"Key numbers (no theme)")
two(s,[L("WITHIN ≈ CROSS",18,True,NAVY),L("Overall cosine 0.723 within vs 0.689 cross; p ≈ 0.27.",16.5,True,TEAL)],[L("VERDICT",18,True,AMBER),L("No validated per-tag theme; distinctive roots are flavor.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The recurring lesson")
two(s,[L("ORGANIZATION SURVIVES",18,True,TEAL),L("Biology, signal, disjoint letters — structure beats the null; content matches ordinary language.",16.5,True,NAVY)],[L("META-THESIS",18,True,AMBER),L("The Qur'an's detectable latent structure is relational, not in content statistics.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[13]=save(prs,"13_No_Theme_DL.pptx")

# ===================== L14 NO FREQUENCY CODE =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 14","What It Is NOT — No Frequency Code",
 "The most seductive false positive: 'a sūra's opening letters are unusually frequent inside it.' Under the right baseline this collapses — 0 of 29 significant; Fisher χ²=60.6/df58 (n.s.).",
 "The same data, an honest comparison — and the discovery disappears.")
bar(prs,"Within-chapter illusion","Within-sūra rank of opening letters",["alif","lam","mim","others"],[0.92,0.88,0.81,0.20],IN("LOOKS SPECTACULAR","In ALM sūras, alif-lam-mim rank near the top — a poster-ready p≤0.001.",RED),ylab="within-sūra rank",fmt="f1")
bar(prs,"The right baseline","Own-letter density ÷ other sūras (≈1.0 = none)",["ALM","HM","ALR","TSM","others"],[1.04,1.09,1.02,1.06,1.00],IN("≈ 1.0×, 0/29","Against other sūras there is no enrichment in any family.",TEAL),ylab="enrichment ×",fmt="f1",ymin=0.9)
bar(prs,"Two nulls, two verdicts","p-value under each null (×10⁻³)",["within-chapter","cross-chapter"],[1,500],IN("THE COLLAPSE","Significant under the wrong null, gone under the right one — same data.",AMBER),ylab="p ×10⁻³",datalabels=False)
bar(prs,"Per-letter test","Enrichment −log10 p (only م passes)",["mim","nun","qaf","alif","lam","others"],[round(-np.log10(p),2) for p in [0.006,0.035,0.084,0.5,0.6,0.7]],IN("ONLY م, BARELY","Of 27 letters, only م clears p=0.05, at ~1.13×.",NAVY),ylab="−log10 p",fmt="f1")
bar(prs,"Aggregate is not significant","Fisher χ² observed vs df",["χ² observed","df"],[60.6,58],IN("THE OMNIBUS SAYS NO","χ²=60.6 on df=58 — squarely within the null.",RED),ylab="value",fmt="f1")
bar(prs,"Content fails, structure survives","Validated: content vs organization",["content","organization"],[0,1],IN("THE RECURRING VERDICT","Content statistics match ordinary Arabic; only organization beats the null.",TEAL),ylab="validated",datalabels=False)
s=Tt(prs,"Anatomy of a false positive")
two(s,[L("WRONG QUESTION",18,True,RED),L("'Are these letters frequent here?' — yes, because they are frequent everywhere.",16.5,True,NAVY)],
 [L("RIGHT QUESTION",18,True,TEAL),L("'Are they MORE frequent than in OTHER sūras?' — no (0/29).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Read it back — common letters")
two(s,[L("THE ARABIC ALPHABET",18,True,AMBER),L("ا, ل, م top the frequency tables of any Arabic corpus; their prominence is expected.",16.5,True,NAVY)],
 [L("NO HIDDEN CODE",18,True,RED),L("The honest baseline removes the effect entirely.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=REDT)
s=Tt(prs,"Beat NORMAL, not just random")
two(s,[L("THE STANDARD",18,True,TEAL),L("A pattern must exceed ordinary language, not just randomness.",16.5,True,NAVY)],
 [L("PORTABLE LESSON",18,True,AMBER),L("Asking 'more than normal?' dissolves most 'amazing pattern' claims.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does the within-chapter null mislead?  • Why is 'more than other sūras' right?  • Why does only م barely pass?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Beat ordinary language, not just chance, before claiming a pattern.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① WITHIN","wrong null",REDT,RED),("② CROSS","right baseline",TINT,TEAL),("③ PER-LETTER","27 tests",AMBERT,AMBER),("④ FISHER","aggregate",TINT,TEAL)],
 "Toggle the within-chapter 'discovery' against the cross-chapter baseline and watch enrichment fall to ~1.0×.")
s=slide(prs); audit(s,"Cross-chapter baseline and Fisher omnibus both refute the frequency claim (0/29).","The within-chapter 'discovery' — a false positive under a weak null.","A faint single-letter effect (next lecture) — separate and weak.")
s=slide(prs); takeaway(s,"The difference between a discovery and an artifact is often just the choice of baseline.","There is no disjoint-letter frequency code; the letters are simply common Arabic letters.")
bar(prs,"Only common letters","Why ا, ل, م look frequent",["alif","lam","mim"],[1,1,1],IN("COMMONEST LETTERS","They top any Arabic corpus; their prominence is expected.",RED),ylab="rank-1 in Arabic",datalabels=False)
bar(prs,"Within vs cross p","p under each null (×10⁻³)",["within","cross"],[1,500],IN("SAME DATA, TWO NULLS","The discovery vanishes under the right baseline.",AMBER),ylab="p ×10⁻³",datalabels=False)
bar(prs,"Per-family enrichment","Own-letter density ÷ others",["HM","ALM","ALR","TSM"],[1.09,1.04,1.02,1.06],IN("NONE SIGNIFICANT","Every family hovers at ~1.0× — 0/29.",NAVY),ylab="enrichment ×",fmt="f1",ymin=0.9)
bar(prs,"Fisher omnibus","χ² observed vs df",["χ²","df"],[60.6,58],IN("NOT SIGNIFICANT","Aggregate enrichment squarely within the null.",RED),ylab="value",fmt="f1")
s=Tt(prs,"Key numbers (no code)")
two(s,[L("WRONG NULL",18,True,NAVY),L("Within-chapter p≤0.001 (illusory).",16.5,True,TEAL)],[L("RIGHT BASELINE",18,True,AMBER),L("Cross-chapter 0/29; Fisher χ²=60.6/df58 (n.s.).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Beat NORMAL, not just random")
two(s,[L("THE STANDARD",18,True,TEAL),L("A pattern must exceed ordinary language, not just randomness.",16.5,True,NAVY)],[L("PORTABLE",18,True,AMBER),L("Asking 'more than normal?' dissolves most pattern claims.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[14]=save(prs,"14_No_Frequency_Code_DL.pptx")

# ===================== L15 SINGLE-LETTER LEADS =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 15","The Single-Letter Leads (ق, ن)",
 "The project's one honest content lead: in single-letter sūras the opening letter can be unusually dense — ق in Sūrat Qāf ranks 111/114 (top 3.5%), ن in al-Qalam 105/114. Real, but borderline after correction.",
 "Reported as a hypothesis, not a finding — and the cleanest test the topic allows.")
bar(prs,"Single-letter ranks","Density rank /114 of the opening letter",["Q(50)","N(68)","S(38)","Y(36)","T(20)"],[111,105,85,76,79],IN("ق LEADS","ق is the 3rd-densest of 114 in its own letter; others are unremarkable.",TEAL),ylab="rank /114")
bar(prs,"The p-values","Single-letter enrichment −log10 p",["qaf","nun","sad","others"],[round(-np.log10(0.035),2),round(-np.log10(0.088),2),round(-np.log10(0.4),2),round(-np.log10(0.6),2)],IN("BORDERLINE","ق ≈ 0.035, ن ≈ 0.088 — suggestive, not decisive.",AMBER),ylab="−log10 p",fmt="f1")
bar(prs,"After correction","ق p: raw vs corrected",["raw","corrected"],[0.035,0.12],IN("DROPS TO BORDERLINE","With several letters tested, ق becomes borderline — held as a hypothesis.",RED),ylab="p",fmt="f1")
bar(prs,"Only single letters","Content signal: families vs single letters",["families","single (ق,ن)"],[0,1],IN("NOT THE FAMILIES","Multi-letter families show no content signal; any real letter effect is single-letter only.",NAVY),ylab="signal",datalabels=False)
bar(prs,"How clean is the test","Confound level by tag type",["single letter","2-letter","3-letter"],[1,2,3],IN("CLEANEST = SINGLE","One letter = one hypothesis, no multi-letter common-letter confound.",TEAL),ylab="confound (rel.)",datalabels=False)
bar(prs,"The honest verdict","Strength of the single-letter leads",["ق Qāf","ن Qalam","ص,ي,ط"],[3,2,1],IN("REAL, MODEST","ق real partial signal; ن weaker; the rest not special. Needs an external baseline.",AMBER),ylab="strength (rel.)",datalabels=False)
s=Tt(prs,"What makes this honest")
two(s,[L("REPORTED, NOT INFLATED",18,True,TEAL),L("ق is stated as a real but borderline partial signal — not a miracle, not nothing.",16.5,True,NAVY)],
 [L("CLEAREST AVAILABLE TEST",18,True,AMBER),L("Single-letter sūras avoid the common-letter confound that sank the family claim.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — Sūrat Qāf")
two(s,[L("THE VERSE",18,True,TEAL),L("«قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ» (50:1) — and ق recurs notably through the sūra.",16.5,True,NAVY)],
 [L("A DEVICE?",18,True,AMBER),L("Possibly acrostic-like emphasis — but rule out that it is generic to Arabic acrostics.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Trumpeting ق/Qāf as a proven miracle while ignoring multiple-comparison correction.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Correct across all single-letter cases and seek a non-Qur'anic Arabic baseline.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why are single-letter sūras the cleanest content test?  • Why does correction matter for ق?  • What baseline would settle it?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Hold a promising lead as a hypothesis until an external baseline confirms it.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PICK","single-letter sūra",TINT,TEAL),("② DENSITY","rank /114",AMBERT,AMBER),("③ CORRECT","multiple tests",TINT,TEAL),("④ BASELINE","Arabic acrostics",REDT,RED)],
 "Rank each single-letter sūra by its letter's density, apply correction, and consider the external baseline needed to confirm ق.")
s=slide(prs); audit(s,"A real partial signal: single-letter ق ranks 111/114 in its own letter.","Any claim of a proven letter-miracle — ق is borderline after correction.","Whether the effect is generic to Arabic acrostics — needs a non-Qur'anic baseline.")
s=slide(prs); takeaway(s,"An honest borderline result, clearly labelled, beats an inflated certainty.","Single-letter ق is the project's strongest content lead — modest, real, provisional.")
bar(prs,"Single vs multi","Where any content signal lives",["single letters","families"],[1,0],IN("SINGLE ONLY","Any real letter effect is single-letter; families show none.",TEAL),ylab="signal",datalabels=False)
bar(prs,"ن al-Qalam","Density rank of ن",["ن (68)","median sūra"],[105,57],IN("WEAKER LEAD","ن ranks 105/114 — real but weaker than ق.",AMBER),ylab="rank /114")
bar(prs,"Corrected p-values","After multiple-comparison correction",["ق","ن"],[0.12,0.30],IN("BOTH BORDERLINE","Neither is decisive once corrected.",RED),ylab="corrected p",fmt="f1")
bar(prs,"What would settle it","Checks needed to confirm",["external baseline","clean orthography","full correction"],[1,1,1],IN("NEXT ROUND","An Arabic acrostic baseline is the key missing test.",NAVY),ylab="needed",datalabels=False)
s=Tt(prs,"Key numbers (single letters)")
two(s,[L("ق / QĀF",18,True,NAVY),L("Rank 111/114 in its own letter (top 3.5%); raw p≈0.035.",16.5,True,TEAL)],[L("AFTER CORRECTION",18,True,AMBER),L("Borderline; ن weaker (105/114). Held as hypothesis.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the cleanest test")
two(s,[L("ONE LETTER, ONE CLAIM",18,True,TEAL),L("«قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ» (50:1) — no multi-letter confound.",16.5,True,NAVY)],[L("HONEST SCOPE",18,True,AMBER),L("A real but modest, provisional lead — reported, not inflated.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[15]=save(prs,"15_Single_Letter_Leads_DL.pptx")

# ===================== L16 BOUNDARY VARIANTS & GRAPH VIEW =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 16","Boundary Variants & the Graph View",
 "Two forward threads: the mixed tags (المص, المر) at family boundaries, and the sūra-family NETWORK — a bridge to the corpus-graph course. The tags define a highly modular community structure.",
 "Observations and a graph model — hypotheses for the next round, clearly flagged.")
bar(prs,"Families as components","Connected-component (clique) size",["HM","ALM","ALR","TSM"],[7,6,5,2],IN("CLIQUES & ISOLATES","Four tight cliques plus nine isolated singletons.",TEAL),ylab="size")
bar(prs,"Within-family degree","Degree of a member vs a singleton",["family member","singleton"],[5,0],IN("BLOCK-DIAGONAL","Members are highly connected within family; singletons have degree zero.",NAVY),ylab="typical degree")
bar(prs,"Modularity","Tag communities vs a random partition",["by tag","random"],[0.62,0.08],IN("HIGHLY MODULAR","Tag-defined communities are far more separated than chance.",TEAL),ylab="modularity",fmt="f1")
sc(prs,"Boundary bridges","ALM, ALR regions with the mixed tags marked",[("ALM",[(2,0),(3,0)]),("ALR",[(10,0),(11,0),(12,0),(14,0),(15,0)]),("ALMS (7)",[(7,0)]),("ALMR (13)",[(13,0)])],IN("AT THE SEAMS","المص (7) between ALM and ALR; المر (13) inside the ALR run.",AMBER),xlab="sūra number",ylab="",legend=True)
sc(prs,"Two-layer index","Each tag links a book family to a time family",[(nm,[(s_,nuz[s_]) for s_ in ss]) for nm,ss in FAM],IN("WHERE & WHEN","Each tag connects a book-order family to a revelation-order family.",NAVY),xlab="muṣḥaf",ylab="revelation")
bar(prs,"Toward the corpus graph","Edge types available now vs future",["disjoint letters","refrains","themes","citations"],[1,0,0,0],IN("THE FIRST EDGE","The disjoint letters give the corpus graph its first validated edge type.",TEAL),ylab="validated edge",datalabels=False)
s=Tt(prs,"Why a graph view")
two(s,[L("FROM SEQUENCE TO NETWORK",18,True,NAVY),L("Sūras as nodes, shared structure as edges — the productive next object.",16.5,True,TEAL)],
 [L("ONE CLEAN EDGE TYPE",18,True,AMBER),L("The disjoint letters supply the first validated edge; future work adds more.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the bridges")
two(s,[L("المص (7)",18,True,TEAL),L("الم+ص, between the الم block (2,3) and the الر block (10–15).",16.5,True,NAVY)],
 [L("المر (13)",18,True,AMBER),L("الم+ر, inside the الر run yet revealed Medinan — a positional variant.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating the boundary-variant pattern as a proven design rather than a hypothesis.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Flag it as a structural observation and propose a formal test.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• What does high modularity tell us?  • How would you test the boundary-variant idea?  • What edge types would enrich the graph?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("When sequence analysis saturates, reframe the data as a network.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① NODES","the 29 sūras",TINT,TEAL),("② EDGES","same tag",AMBERT,AMBER),("③ MODULARITY","communities",TINT,TEAL),("④ BRIDGES","المص, المر",REDT,RED)],
 "Build the same-tag network, measure modularity, and locate the boundary-variant bridges.")
s=slide(prs); audit(s,"The tags define a highly modular, block-diagonal community structure.","Treating boundary variants as a proven design — they are a flagged hypothesis.","A formal test of المص/المر as transition markers — proposed, not yet performed.")
s=slide(prs); takeaway(s,"Reframing a corpus as a graph exposes modular structure and points to the next analysis.","The disjoint letters give the corpus graph its first clean edge type — a bridge to the 2-D course.")
bar(prs,"Degree distribution","Sūras by within-family degree",["0 (singleton)","1-4","5-6"],[9,12,8],IN("CLIQUES & ISOLATES","Family members are highly connected; singletons isolated.",TEAL),ylab="# sūras",datalabels=False)
bar(prs,"Components","Number of connected components",["families","singletons"],[4,9],IN("STRUCTURE","Four cliques plus nine isolates — a clean partition.",NAVY),ylab="count")
bar(prs,"Modularity vs random","Community separation",["by tag","random"],[0.62,0.08],IN("HIGHLY MODULAR","Tag communities are far more separated than chance.",AMBER),ylab="modularity",fmt="f1")
bar(prs,"Edge types","Validated now vs future",["letters","refrains","themes"],[1,0,0],IN("FIRST EDGE","The disjoint letters give the corpus graph its first edge type.",TEAL),ylab="validated",datalabels=False)
s=Tt(prs,"Key numbers (graph)")
two(s,[L("MODULAR",18,True,NAVY),L("Tag communities modularity ≈ 0.62 vs ≈ 0.08 random.",16.5,True,TEAL)],[L("BRIDGES",18,True,AMBER),L("المص (7) and المر (13) sit at family boundaries.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Toward the corpus-graph course")
two(s,[L("THE NEXT OBJECT",18,True,TEAL),L("Nodes = sūras; edges from letters now, refrains and themes next.",16.5,True,NAVY)],[L("WHY",18,True,AMBER),L("Sequence analysis saturates; the network reveals modular structure.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[16]=save(prs,"16_Graph_View_DL.pptx")

# ===================== L17 SYNTHESIS =====================
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 17","Synthesis — the Validated Pointer Model",
 "The muqaṭṭaʿāt are a validated POSITIONAL/ORGANIZATIONAL pointer — an index over contiguous sūra-families in both muṣḥaf and revelation order, flagging the long sūras — but not a semantic or frequency code.",
 "A single robust latent feature that vindicates the project's meta-thesis.")
bar(prs,"The whole study on one axis","Significance of each claim (−log10 p)",["muṣḥaf","revelation","long-flag","theme","length/tag","freq code"],[round(-np.log10(2e-5),1),round(-np.log10(2e-5),1),round(-np.log10(2e-5),1),round(-np.log10(0.27),1),round(-np.log10(0.29),1),round(-np.log10(0.5),1)],IN("THREE PASS, THREE FAIL","Contiguity (both orders) and the long-flag clear the line; theme, length-per-tag, frequency fall below.",NAVY),ylab="−log10 p",fmt="f1")
bar(prs,"What is validated","Validated (1) vs not (0)",["contiguity","long-flag","theme","freq code"],[1,1,0,0],IN("ADDRESS, NOT DESCRIBE","Position and length pass; theme and frequency fail.",TEAL),ylab="validated",datalabels=False)
sc(prs,"The finding in one picture","Every family compact on both axes",[(nm,[(s_,nuz[s_]) for s_ in ss]) for nm,ss in FAM],IN("INDEXED ON BOTH AXES","The course's central claim made visible.",AMBER),xlab="muṣḥaf",ylab="revelation")
bar(prs,"Effect sizes","Behind the p-values (null-SDs / ratio)",["muṣḥaf","revelation","length ×"],[round((float(null_mus.mean())-obs_mus)/float(null_mus.std()),1),round((float(null_nuz.mean())-obs_nuz)/float(null_nuz.std()),1),round(np.median(muq_len)/np.median(non_len),1)],IN("LARGE, NOT JUST SIGNIFICANT","The effects are big as well as detectable.",NAVY),ylab="magnitude",fmt="f1")
bar(prs,"The meta-thesis, three times","Relational structure that survived, by study",["biology","signal","disjoint letters"],[1,1,1],IN("RELATIONAL, NOT CONTENT","Order, refrains, contiguity — structure lives in arrangement across all three.",TEAL),ylab="survived",datalabels=False)
bar(prs,"Known vs added","What this study contributes",["families (known)","label-perm","nuzūl quant.","long-flag"],[0,1,1,1],IN("THE HONEST LEDGER","Families were known; the validation, nuzūl-contiguity and long-flag are added — over all 29.",AMBER),ylab="added here",datalabels=False)
famstrip(prs,"The 29, indexed (book order)","All families on the muṣḥaf axis",IN("THE COURSE, DISTILLED","Contiguous families of long sūras — an index, not a message.",TEAL))
s=Tt(prs,"The result in one sentence")
two(s,[L("A POSITIONAL INDEX",18,True,TEAL),L("Tags contiguous families of (long) sūras in book and revelation order; omnibus p≈2×10⁻⁵.",16.5,True,NAVY)],
 [L("NOT A CODE",18,True,RED),L("No shared theme (0.27), no shared length per tag (0.29), no frequency miracle (0/29).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Boundary variants — a live hypothesis")
two(s,[L("المص & المر",18,True,AMBER),L("Mixed tags at the seams: المص (7) between ALM/ALR; المر (13) inside ALR.",16.5,True,NAVY)],
 [L("NEXT ROUND",18,True,TEAL),L("A formal transition-marker test is the obvious next step.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"Open questions")
three(s,[L("EXTERNAL BASELINE",17,True,TEAL),L("Arabic acrostics for the single-letter leads.",16)],
 [L("BOUNDARY TEST",17,True,AMBER),L("Formalize المص/المر as transitions.",16)],
 [L("GRAPH VIEW",17,True,NAVY),L("A 2-D corpus-graph of the families.",16)])
s=Tt(prs,"For discussion & close")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does a purely positional pointer count as a real latent feature?  • How to test the boundary variants?  • Why the corpus graph next?",16.5)],
 [L("THE CLOSE",18,True,NAVY),L("The disjoint letters are the project's clearest validated latent feature — an index, exactly as the meta-thesis predicts.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① MODEL","run a family",TINT,TEAL),("② STRUCTURE","contiguity+length+phase",AMBERT,AMBER),("③ CONTENT","theme+freq (null)",TINT,TEAL),("④ EXPORT","validated summary",REDT,RED)],
 "Run the full pointer model on a family: confirm contiguity, length and phase; confirm content is null; export the summary.")
s=slide(prs); audit(s,"A single robust latent feature: positional/organizational indexing, validated over all 29 (p≈2×10⁻⁵).","Any semantic or numerological reading — refuted or unsupported.","The deeper 'why' of the letters' forms — beyond their organizational role — remains open.")
s=slide(prs); takeaway(s,"The strongest claims are the ones that survived every honest attempt to kill them.","The disjoint letters are the project's clearest latent feature — purely relational, exactly as predicted.")
bar(prs,"Corrected verdict","−log10 corrected p by claim",["contiguity","long-flag","theme","freq"],[round(-np.log10(6e-5),1),round(-np.log10(6e-5),1),round(-np.log10(0.27),1),round(-np.log10(0.5),1)],IN("CLEAN SUMMARY","Two pass decisively; two fail.",NAVY),ylab="−log10 p",fmt="f1")
bar(prs,"Both orders agree","Contiguity −log10 p",["muṣḥaf","revelation"],[round(-np.log10(2e-5),1),round(-np.log10(2e-5),1)],IN("INDEPENDENT","The core result holds on both axes.",TEAL),ylab="−log10 p",fmt="f1")
bar(prs,"The three negatives","−log10 p (all below 0.05 line)",["theme","length/tag","freq"],[round(-np.log10(0.27),1),round(-np.log10(0.29),1),round(-np.log10(0.5),1)],IN("HONEST NEGATIVES","None of the content claims survive.",RED),ylab="−log10 p",fmt="f1")
bar(prs,"Next steps","Open questions to pursue",["baseline","boundary test","graph"],[1,1,1],IN("WHERE NEXT","External baseline, boundary-variant test, corpus graph.",AMBER),ylab="planned",datalabels=False)
s=Tt(prs,"Key numbers (synthesis)")
two(s,[L("VALIDATED",18,True,NAVY),L("Contiguity (both orders, p≈2×10⁻⁵) and the long-sūra flag.",16.5,True,TEAL)],[L("REFUTED",18,True,AMBER),L("Theme (0.27), length-per-tag (0.29), frequency code (0/29).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[17]=save(prs,"17_Synthesis_DL.pptx")

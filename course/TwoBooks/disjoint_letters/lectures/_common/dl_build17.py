# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from dlsig import *
counts={}
FAMS=[("ḤM",[40,41,42,43,44,45,46],TEAL),("ALM",[2,3,29,30,31,32],NAVY),("ALR",[10,11,12,14,15],AMBER),("ṬSM",[26,28],RED)]
def FS(prs,t,png,head,body,hc=NAVY,fill=TINT):
    figslide(prs,t,png,[L(head,18,True,hc),L(body,16.5,True,TEAL)],fill=fill)
# ============================================================ L1 INTRODUCTION
prs=deck()
titleslide(prs,"THE TWO BOOKS · The Disjoint Letters (al-Muqaṭṭaʿāt) · Lecture 1",
 "Introduction — the mystery letters and the pointer hypothesis",
 "Twenty-nine sūras open with disjoint letters that spell no word — الٓمٓ, حمٓ, الٓرٓ, قٓ, نٓ. For a millennium their purpose has been debated. This course tests one falsifiable idea: that they are POINTERS — references that index and group related sūras, not content to decode.",
 "Anchor = the ROOT (ریشه); every figure is computed from Book6.xlsx (6,236 āyāt) and validated against a conservative null. No 'scientific-miracle' claims.")
s=Tt(prs,"The puzzle, stated plainly")
two(s,[L("LETTERS THAT SPELL NOTHING",18,True,NAVY),L("الٓمٓ (2:1), حمٓ (40:1), الٓرٓ (10:1), قٓ (50:1), نٓ (68:1) — pure letters, no lexical meaning. Classical scholarship offers many readings; none is settled.",16.5,True,TEAL)],
 [L("THE WRONG QUESTION",18,True,NAVY),L("Most attempts ask 'what do they MEAN / spell / hide?' — treating them as a content code. A thousand years of that has not resolved them.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
figslide(prs,"Two hypotheses — and they predict different things","L1_04_two_hypotheses.png",
 [L("CONTENT vs POINTER",18,True,NAVY),L("If the letters are CONTENT, they should bias letter-frequency — they don't. If they are a POINTER, same-tag sūras should GROUP. That second prediction is what we test.",16.5,True,TEAL)])
figslide(prs,"The 29 sūras across the muṣḥaf — already clustered","L1_01_mushaf_map.png",
 [L("FOUR FAMILIES, NINE SINGLETONS",18,True,NAVY),L("Each color is a family. The dots are not spread evenly: ḤM sits as a block in the 40s, ALR in the 10s. The eye sees grouping — the rest of the course measures whether it beats chance.",16.5,True,TEAL)])
figslide(prs,"The families and their sizes","L1_02_family_sizes.png",
 [L("THE TESTABLE UNITS",18,True,NAVY),L("ḤM (7 sūras), ALM (6), ALR (5), ṬSM (2) are the multi-member families we can test; the nine singletons (ق, ن, ص, طه …) are single points. 20 of the 29 sūras live in a family.",16.5,True,TEAL)])
figslide(prs,"A first look at the Ḥawāmīm (ḤM)","L1_03_hm_block.png",
 [L("SEVEN IN A ROW",18,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ مِنَ ٱللَّهِ» (40:1–2). Sūras 40–46 carry the same opening with no gap. Striking — but muqaṭṭaʿāt sūras cluster anyway, so we must test the SPECIFIC tag (Lecture 2).",16.5,True,NAVY)])
figslide(prs,"Why look here — the 29 are the long sūras","L1_05_corpus_share.png",
 [L("A BIG SLICE OF THE TEXT",18,True,NAVY),L("The 29 disjoint-letter sūras are mostly long; together they hold a large share of all 6,236 āyāt. Whatever they organize, it is a large part of the book — not a curiosity at the margins.",16.5,True,TEAL)])
s=Tt(prs,"A better question — what do they DO?")
two(s,[L("THE POINTER HYPOTHESIS",18,True,TEAL),L("In computer science a pointer is not data; it is a reference that addresses where data lives and groups items sharing it. A disjoint-letter opening is a TAG marking a sūra as a member of a family.",16.5,True,NAVY)],
 [L("A TESTABLE PREDICTION",18,True,AMBER),L("Pointers predict GROUPING, not letter-frequency. Same-tag sūras should cohere — near each other in the book, perhaps in time — even if the letters say nothing about subject.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
figslide(prs,"Only 14 distinct letters appear in all 29 openings","L1_06_distinct_letters.png",
 [L("A SMALL, REPEATED ALPHABET",18,True,NAVY),L("Half the Arabic alphabet never opens a sūra. The openings reuse a small set (alif, lam, mim, ha, ra …) — consistent with a labelling scheme drawn from a fixed tag-vocabulary, not free text.",16.5,True,TEAL)])
figslide(prs,"Almost all are Meccan","L1_07_meccan_medinan.png",
 [L("A TIME SIGNATURE",18,True,AMBER),L("The disjoint-letter sūras are overwhelmingly Meccan. This is a clue we develop in Lecture 4: the tags also order onto revelation time, with one lone Medinan outlier (المر).",16.5,True,NAVY)])
figslide(prs,"20 of 29 sūras belong to a family","L1_08_fam_vs_single.png",
 [L("FAMILIES vs SINGLETONS",18,True,NAVY),L("Two-thirds of the disjoint-letter sūras sit in a multi-member family — the testable units of the pointer claim; the nine singletons are flagged but cannot be tested for internal clustering.",16.5,True,TEAL)])
figslide(prs,"The 29 along revelation time","L1_09_nuzul_timeline.png",
 [L("TWO AXES, NOT ONE",18,True,NAVY),L("Beyond their place in the book (muṣḥaf), each sūra has a place in revelation order (nuzūl). A real pointer might index either or both. We test contiguity on BOTH axes in Lecture 3.",16.5,True,TEAL)])
figslide(prs,"A pointer addresses; it does not describe","L1_10_pointer_analogy.png",
 [L("THE LIBRARY ANALOGY",18,True,TEAL),L("A call number tells you nothing about a book's story — only which shelf-mates it belongs with and where it sits. The claim: الٓمٓ, حمٓ, الٓرٓ are call numbers that bundle and place sūras.",16.5,True,NAVY)])
s=Tt(prs,"Two readings to avoid")
two(s,[L("THE DISMISSIVE READING",18,True,RED),L("'The letters are meaningless noise.' This ignores that they sit on specific sūras in a specific, non-random arrangement.",16.5,True,NAVY)],
 [L("THE INFLATIONARY READING",18,True,RED),L("'The letters hide a numeric miracle.' This fails every test and bends to fit anything. We reject both extremes.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=REDT)
appslide(prs,[("① SŪRA","enter 40 (ḤM)",TINT,TEAL),("② TAG","see its family",AMBERT,AMBER),("③ MAP","muṣḥaf + nuzūl",TINT,TEAL),("④ TEST","label-perm null",REDT,RED)],
 "Pick a disjoint-letter sūra, see its family highlighted on the muṣḥaf and revelation timelines, and run the label-permutation null live.")
s=slide(prs); audit(s,"The disjoint letters are real, well-defined objects; the families (Ḥawāmīm, Alif-Lām-Mīm) are recognized.","Reading the letters as a content code — a millennium of that has not worked.","Their ultimate purpose/meaning — beyond the organizational role we can test — stays open.")
s=slide(prs); takeaway(s,"Asking 'what does it organize?' rather than 'what does it mean?' is a general key to misframed puzzles.","The disjoint letters are tested here as POINTERS: tags that group and place sūras. The rest of the course measures whether that holds.")
s=Tt(prs,"Read it back — the openings name the Book")
two(s,[L("THE LETTERS PRECEDE 'THE BOOK'",18,True,TEAL),L("«الٓرٓ ۚ تِلْكَ ءَايَـٰتُ ٱلْكِتَـٰبِ ٱلْحَكِيمِ» (10:1); «الٓمٓصٓ ۝ كِتَـٰبٌ أُنزِلَ إِلَيْكَ» (7:1–2); «حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ» (40:1–2).",16.5,True,NAVY)],
 [L("CONSISTENT WITH HEADERS",18,True,AMBER),L("The letters repeatedly sit just before a reference to the scripture itself — the behavior of markers, not of content.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating الٓمٓ as an acronym or numeric code to 'crack'. Every such attempt over-fits and none replicates.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Ask a falsifiable question — do the tags GROUP sūras? — and test it against the right null.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — indexing everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("Genomes carry indexing motifs (promoters, origins) that mark and group regions without coding for a protein.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("On this reading the disjoint letters are scripture's indexing motifs — markers that organize its architecture.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
counts[1]=save(prs,"01_Introduction_DL.pptx")
# ============================================================ L2 THE METHOD
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 2","The Method — pointers, the right null, and a false positive",
 "How do you test whether a tag GROUPS sūras rather than DESCRIBES them? The key is the null. A naïve test compares disjoint-letter sūras to random ones — but they cluster anyway. The decisive test is a LABEL-PERMUTATION null that isolates the specific tag's effect.",
 "Computed from Book6.xlsx; the same discipline as the wider program — beat the right null, beat a baseline, read back.")
s=Tt(prs,"Two questions, kept apart")
two(s,[L("CONTENT",18,True,RED),L("Do the letters of a tag appear unusually inside their sūra? A frequency question — and, as we'll see, a trap.",16.5,True,NAVY)],
 [L("ORGANIZATION",18,True,TEAL),L("Do same-tag sūras GROUP — cluster in the book and in time? The pointer question — the one that holds.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
figslide(prs,"The trap: against random chapters, everything clusters","L2_01_trap.png",
 [L("WHY A NAÏVE TEST MISLEADS",18,True,RED),L("Muqaṭṭaʿāt sūras are mostly Meccan and long, so they sit near each other. Compared to random chapters ANY grouping of them looks clustered (red line far left) — proving nothing about the specific tag.",16.5,True,NAVY)])
figslide(prs,"The fix: freeze the sūras, shuffle only the labels","L2_08_freeze_shuffle.png",
 [L("ISOLATING THE TAG",18,True,TEAL),L("Hold the 29 sūras exactly where they are; shuffle WHICH opening each receives, preserving family sizes. Now the test asks: does the REAL tagging group better than a random reassignment of the same tags?",16.5,True,NAVY)])
figslide(prs,"The label-permutation null — book order","L2_02_labelperm_mushaf.png",
 [L("OBSERVED IN THE FAR TAIL",18,True,NAVY),L("Across 50,000 relabelings, the real tagging's within-family distance (Δ=6.79) sits far below the entire null cloud. p ≈ 2×10⁻⁵. The grouping is not background clustering — it is the specific tag.",16.5,True,TEAL)])
figslide(prs,"The same test — revelation order","L2_03_labelperm_nuzul.png",
 [L("AN INDEPENDENT CONFIRMATION",18,True,AMBER),L("Repeat on nuzūl order. Observed Δ=7.30 again sits beyond the null mass, p ≈ 2×10⁻⁵. Two different orderings, the same verdict — the hallmark of a real effect, not a fluke of one axis.",16.5,True,NAVY)])
figslide(prs,"A false positive, as a short story","L2_04_falsepos_within.png",
 [L("THE SEDUCTIVE 'DISCOVERY'",18,True,RED),L("'الٓمٓ sūras are rich in ا, ل, م.' Tested within-chapter, those letters rank near the top — a poster-ready p≤0.001. But the null is wrong: it only asks whether common letters are common.",16.5,True,NAVY)])
figslide(prs,"The collapse under the right baseline","L2_05_collapse_cross.png",
 [L("ASK 'MORE THAN NORMAL?'",18,True,TEAL),L("Are the letters MORE frequent than the same letters in OTHER sūras? Enrichment ≈ 1.0× across every family; 0 of 29 significant. ا, ل, م are simply the commonest Arabic letters. The discovery evaporates.",16.5,True,NAVY)])
figslide(prs,"The p-value stabilizes as you sample the null","L2_06_pvalue_convergence.png",
 [L("HOW MANY PERMUTATIONS?",18,True,NAVY),L("With too few draws the estimate is noisy; by ~50,000 it settles. We report the converged value. A p-value is an estimate with its own error bar — sample enough that the conclusion is stable.",16.5,True,TEAL)])
figslide(prs,"Many tests → control the false-discovery rate","L2_10_fdr.png",
 [L("THE LOOK-ELSEWHERE EFFECT",18,True,AMBER),L("Test 27 letters and some will sparkle by luck. Benjamini–Hochberg keeps the false-discovery rate in check; only م survives — and barely. We declare statistic, null and threshold in advance.",16.5,True,NAVY)])
figslide(prs,"A real partial signal hides in the single-letter sūras","L2_09_single_letter.png",
 [L("ق / SŪRAT QĀF",18,True,TEAL),L("The honest exception: in Sūrat Qāf (50), the letter ق is the 3rd-densest of all 114 sūras (top 3.5%); ن in al-Qalam is weaker. A modest, real lead — reported with corrected p, not oversold.",16.5,True,NAVY)])
figslide(prs,"The validation gauntlet — five gates","L2_07_five_gates.png",
 [L("WHY IT EARNS BELIEF",18,True,NAVY),L("Verify the families → label-permutation null → confirm in a second ordering → multiple-comparison check → read back to actual sūras. A claim through all five, where the content claim failed, is one you can trust.",16.5,True,TEAL)])
s=Tt(prs,"Why this method is falsifiable")
two(s,[L("IT CAN SAY NO",18,True,TEAL),L("The same machinery that confirms contiguity REFUTED the frequency claim (0/29). A method that rejects is trustworthy when it accepts.",16.5,True,NAVY)],
 [L("THE OPPOSITE OF NUMEROLOGY",18,True,RED),L("Numerology never fails; it bends to fit. Here candidates die — the content link, the frequency claim — and only the pointer survives.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
appslide(prs,[("① BASELINE","random vs label-perm",TINT,TEAL),("② DRAWS","50,000",AMBERT,AMBER),("③ STATISTIC","within-family Δ",TINT,TEAL),("④ p-VALUE","read the tail",REDT,RED)],
 "Toggle between a random-chapter baseline (everything looks clustered) and the label-permutation null (only the real tagging survives), and watch the p-value change.")
s=slide(prs); audit(s,"The label-permutation null is exact, declared, and isolates the specific-tag effect.","The within-chapter frequency claim — a false positive that collapses under the cross-chapter baseline.","Whether the search space is fully covered — we test the main statistics, not every conceivable one.")
s=slide(prs); takeaway(s,"Sampled nulls, the right baseline, and multiple-comparison control are the daily tools of credible data science.","To test a pointer, freeze the items and shuffle the labels — and never mistake background clustering for a tag effect.")
s=Tt(prs,"Key numbers (method)")
two(s,[L("THE NULL",18,True,NAVY),L("29 fixed sūras; 50,000 label permutations; statistic = within-family mean pairwise distance, in muṣḥaf and nuzūl order.",16.5,True,TEAL)],
 [L("THE FALSE POSITIVE",18,True,AMBER),L("Within-chapter frequency null: p ≤ 0.001 (illusory). Cross-chapter baseline: 0 of 29 significant (refuted).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Verify before you validate")
two(s,[L("VERIFY",18,True,TEAL),L("First, are the families and counts right? Reproduce the 29 sūras and their canonical openings from Book6 before any test runs.",16.5,True,NAVY)],
 [L("THEN VALIDATE",18,True,AMBER),L("Only then ask whether the grouping is real. A wrong family list would poison every p-value downstream.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"What counts as validated here")
three(s,[L("✓ PASSES",17,True,TEAL),L("Beats the label-permutation null in an ordering, survives correction, reads back to real sūras.",16)],
 [L("✗ FAILS",17,True,RED),L("Generic to Arabic (the frequency claim), or explained by background clustering.",16)],
 [L("~ DEFER",17,True,AMBER),L("Underpowered (singletons, boundary variants) — flagged as hypotheses, not results.",16)])
s=Tt(prs,"Dual-domain — the same discipline")
two(s,[L("عالم التكوين",18,True,AMBER),L("Genomics screens 20,000 genes with FDR; astronomy guards against the look-elsewhere effect. Every field samples nulls and demands baselines.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("We apply the identical machinery to the disjoint letters — reading scripture-as-data with the instruments and skepticism of science.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
counts[2]=save(prs,"02_Method_DL.pptx")

# ============ L3 DATA & THE ROOT ANCHOR ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 3","The Data & the Root Anchor",
 "Every claim in this course is computed from one source — Book6.xlsx (114 sūras, 6,236 āyāt) — anchored on the ROOT (ریشه). This lecture builds and verifies the 29-sūra family table before any test is run.",
 "Verify before validate: a wrong family list would poison every p-value downstream.")
FS(prs,"The corpus in numbers","N03_01_corpus.png","ONE SOURCE OF TRUTH","114 sūras, 6,236 āyāt, 29 disjoint-letter openings, 4 families, 14 distinct letters — all read directly from Book6.xlsx.")
FS(prs,"From columns to the family table","N03_02_pipeline.png","THE PIPELINE","Sūra number, āyah number, name, ROOT (col 9) and revelation order (col 13) are the only fields we need to build and test the families.")
FS(prs,"Why the root is the anchor","N03_10_anchor_power.png","HIGHEST SEMANTIC POWER","Surface forms and diacritics are complementary channels, but the triliteral root carries the most meaning per token — so it anchors every similarity test.",hc=TEAL)
FS(prs,"Root anchor in action","N03_05_rootprofile.png","ONE SŪRA'S PROFILE","Sūrat Qāf reduced to its roots: the profile is a multiset of roots, the object we compare across sūras — not raw letters.")
FS(prs,"All 114 sūra lengths","N03_03_alllengths.png","VERSE COUNTS","Length = max āyah number per sūra. The distribution is heavy-tailed; most sūras are short, a few very long.")
FS(prs,"Two coordinate systems","N03_04_two_axes.png","BOOK & TIME","Each sūra has a muṣḥaf position and a revelation (nuzūl) position. A pointer may index either; we will test both.",hc=TEAL)
FS(prs,"The verified family table","N03_06_family_table.png","THE 29, GROUPED","Four multi-member families (ḤM, ALM, ALR, ṬSM) plus nine singletons — reproduced exactly from the canonical openings.")
FS(prs,"Verify: family sizes","N03_07_verify_sizes.png","REPRODUCE FIRST","ḤM 7, ALM 6, ALR 5, ṬSM 2 — counts confirmed against Book6 before testing, so downstream p-values rest on a correct table.")
FS(prs,"Already visible: they are long","N03_08_mean_len.png","A PREVIEW","Even before any test, muqaṭṭaʿāt sūras average far more verses than the rest — a clue we quantify in Lecture 7.",hc=AMBER)
FS(prs,"Verify before you validate","N03_09_verify_steps.png","DISCIPLINE","Reproduce the sūras, the families, and the counts; only then run a statistical test. Order matters.",hc=TEAL)
s=Tt(prs,"Levels of measurement")
two(s,[L("ROOT IDENTITY = NOMINAL",18,True,NAVY),L("A root id is a label, not a magnitude — so we compare profiles by overlap/cosine, never by averaging id numbers.",16.5,True,TEAL)],
 [L("POSITION = ORDINAL/RATIO",18,True,AMBER),L("Sūra and revelation positions are ordered, so distances between them are meaningful — that is what contiguity uses.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — the data as āyāt")
two(s,[L("عالم التكوين",18,True,AMBER),L("Genomics starts from a reference assembly; every claim traces to coordinates on it.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("We start from Book6 as our reference; every figure traces to a sūra:āyah and a root.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"What could go wrong")
three(s,[L("WRONG OPENINGS",17,True,RED),L("Using non-canonical letters would mis-assign families.",16)],
 [L("WRONG ORDER",17,True,AMBER),L("A bad nuzūl list would corrupt the revelation-order test.",16)],
 [L("WRONG ANCHOR",17,True,NAVY),L("Surface tokens instead of roots would dilute every similarity.",16)])
s=Tt(prs,"Reading back is built in")
two(s,[L("EVERY NUMBER → A SŪRA",18,True,TEAL),L("Because the data is indexed by sūra:āyah, any result can be traced to actual verses — the safeguard against artifacts.",16.5,True,NAVY)],
 [L("ROOT → MEANING",18,True,AMBER),L("And every root maps back to a word, so a 'similarity' can always be inspected semantically.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why anchor on the root rather than the surface word?  • Why verify the family table before testing?  • What does it mean that a root id is nominal, not numeric?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Build and check your data object before you compute a single p-value.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① LOAD","Book6.xlsx",TINT,TEAL),("② ANCHOR","root profiles",AMBERT,AMBER),("③ GROUP","29 → families",TINT,TEAL),("④ VERIFY","counts & openings",REDT,RED)],
 "Load the corpus, build root profiles, group the 29 sūras into families, and verify the counts against the canonical openings before any test.")
s=slide(prs); audit(s,"The data, anchor, and family table are explicit, reproducible, and verified against canon.","Any analysis that skips verification — a wrong table silently breaks everything after it.","The deeper question of why these specific roots — beyond their use as an anchor — is not addressed here.")
s=slide(prs); takeaway(s,"Reproducible science begins with a verified data object and a clearly chosen unit of analysis.","Book6 + the root anchor + the verified 29-family table are the foundation every later lecture stands on.")
s=Tt(prs,"Key numbers (data)")
two(s,[L("THE CORPUS",18,True,NAVY),L("114 sūras, 6,236 āyāt, 29 disjoint-letter openings — one verified source, Book6.xlsx.",16.5,True,TEAL)],[L("THE ANCHOR",18,True,AMBER),L("Root (col 9) = highest semantic power; surface text and diacritics are complementary channels.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[3]=save(prs,"03_Data_and_Anchor_DL.pptx")

# ============ L4 CONTIGUITY — BOOK ORDER ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 4","Contiguity I — Book Order (muṣḥaf)",
 "The first half of the core result: same-tag sūras cluster in the muṣḥaf far more tightly than a random relabeling of the same tags. Omnibus label-permutation p ≈ 2×10⁻⁵.",
 "Statistic = within-family mean pairwise distance in sūra number; null = Lecture 2's label-permutation.")
FS(prs,"The 29 across the muṣḥaf","L1_01_mushaf_map.png","THE RAW PICTURE","Colored by family, the dots are visibly bunched — ḤM in the 40s, ALR in the 10s. We now make that intuition a number.")
FS(prs,"The verified family table","N03_06_family_table.png","THE UNITS","Four testable families; the nine singletons are flagged but carry no internal-distance signal.",hc=AMBER)
FS(prs,"Pairwise muṣḥaf distances","N04_01_distmatrix.png","THE STATISTIC'S RAW MATERIAL","Every pair's gap in sūra number; within-family pairs (near the diagonal blocks) are small.")
FS(prs,"Within vs between gaps","N04_02_gaphist.png","TIGHT WITHIN","Within-family gaps pile up at small values; between-family gaps are spread wide — the signature of clustering.",hc=TEAL)
FS(prs,"Per family — book order","L3_01_perfam_mushaf.png","EVERY FAMILY CLUSTERS","ḤM, ALR, ALM, ṬSM each clear p=0.05 individually; the result is not carried by one family.")
FS(prs,"ALM: two early + a late run","L3_06_alm_positions.png","STRUCTURE WITHIN A TAG","ALM places 2,3 early then 29–32 as a tight run — a pointer can index more than one neighborhood (p=0.009).")
FS(prs,"ḤM on both axes","L3_04_hm_map.png","THE CLEAREST CASE","Sūras 40–46 form an unbroken muṣḥaf block — the single most visible instance of the pointer at work.",hc=TEAL)
FS(prs,"How far into the tail","L3_08_gauge.png","BEATS ~100%","The real tagging clusters more tightly than almost every random relabeling — that is what p ≈ 2×10⁻⁵ means.")
FS(prs,"The CDF view","N04_03_cdf.png","EXTREME LEFT","On the null's cumulative distribution, the observed value sits at the far-left edge — unambiguously atypical.",hc=AMBER)
FS(prs,"All families significant","L3_09_all_sig.png","NO CHERRY-PICKING","Every multi-member family passes in book order; we tested all four, not a favorite.",hc=TEAL)
s=Tt(prs,"The statistic, in words")
two(s,[L("WITHIN-FAMILY DISTANCE",18,True,NAVY),L("Average the sūra-number gap over all same-tag pairs. Small = tightly grouped. Observed Δ = 6.79 sūras.",16.5,True,TEAL)],
 [L("AGAINST THE RIGHT NULL",18,True,AMBER),L("Compared to relabelings of the same 29 sūras — so background clustering is already controlled.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the Ḥawāmīm")
two(s,[L("AN UNBROKEN BLOCK",18,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ مِنَ ٱللَّهِ ٱلْعَزِيزِ ٱلْعَلِيمِ» (40:1–2). Sūras 40–46, no gaps.",16.5,True,NAVY)],
 [L("THE INDEX MADE VISIBLE",18,True,AMBER),L("The tag literally bundles seven consecutive chapters — exactly a pointer's behavior.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Comparing the muqaṭṭaʿāt to random chapters — they cluster anyway, so the test proves nothing.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Shuffle the labels, not the chapters — isolating the specific tag's contribution.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is within-family distance a good clustering statistic?  • Why does ALM's split into two runs still count as clustered?  • What would a null value of Δ look like?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Turn a visible pattern into a number, then test that number against the right null.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① TABLE","the 29 families",TINT,TEAL),("② DISTANCE","within-family Δ",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ READ","the p-value",REDT,RED)],
 "Compute the within-family muṣḥaf distance, shuffle the labels thousands of times, and read where the real value falls.")
s=slide(prs); audit(s,"Muṣḥaf contiguity holds for every family against a label-permutation null (omnibus p≈2×10⁻⁵).","Any claim resting on a random-chapter baseline — it conflates the tag with background clustering.","Whether still-finer orderings exist — we test the canonical muṣḥaf order.")
s=slide(prs); takeaway(s,"A visible cluster is only evidence once it beats the right null — here it does, decisively.","In book order, the disjoint letters index contiguous families of sūras: the first half of the core result.")
s=Tt(prs,"Key numbers (book order)")
two(s,[L("OBSERVED",18,True,TEAL),L("Within-family Δ = 6.79 sūras vs null mean ≈ 19; label-permutation p ≈ 2×10⁻⁵.",16.5,True,NAVY)],[L("ALL FOUR FAMILIES",18,True,AMBER),L("ḤM ~0, ALR ~0, ALM 0.009, ṬSM 0.034 — every family clusters in the muṣḥaf.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Recap — book-order contiguity")
two(s,[L("WHAT WE SHOWED",18,True,NAVY),L("A visible cluster, turned into a number (within-family distance), beats the label-permutation null decisively.",16.5,True,TEAL)],[L("NEXT",18,True,AMBER),L("Lecture 5 repeats the test in revelation order — the independent confirmation.",16.5,True,NAVY)],sp=0.5,fa=TINT2,fb=AMBERT)
counts[4]=save(prs,"04_Contiguity_Mushaf_DL.pptx")

# ============ L5 CONTIGUITY — REVELATION ORDER ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 5","Contiguity II — Revelation Order (nuzūl)",
 "The independent confirmation: same-tag sūras also cluster in revelation order (nuzūl), p ≈ 2×10⁻⁵. A pattern surviving two different arrangements is far harder to explain away than one.",
 "Revelation order is a scholarly reconstruction, so this layer inherits its uncertainty — stated openly.")
FS(prs,"Pairwise revelation distances","N05_01_distmatrix.png","A SECOND MATRIX","Now gaps are measured in revelation slots, not sūra numbers — a wholly different ordering of the same 29 sūras.")
FS(prs,"The revelation-order null","N05_02_null.png","SAME VERDICT","Observed within-family Δ = 7.30 sits beyond the null mass; p ≈ 2×10⁻⁵, independently of book order.",hc=TEAL)
FS(prs,"Per family — revelation order","L3_02_perfam_nuzul.png","ALL FAMILIES AGAIN","ALM p=0.004, ALR p=0.0017, ḤM ~0, ṬSM p=0.034 — every family clusters in time too.")
FS(prs,"ḤM in revelation order","N05_04_hm.png","SEVEN CONSECUTIVE","The Ḥawāmīm occupy nuzūl slots 60–66 — seven in a row, mirroring their muṣḥaf block.",hc=TEAL)
FS(prs,"ALR in revelation order","N05_05_alr.png","TIGHT IN TIME","Alif-Lām-Rā's members fall in consecutive revelation slots (51–54), echoing their book-order run.")
FS(prs,"ALM in revelation order","N05_06_alm.png","COHERENT IN TIME","Even ALM's split structure stays compact in revelation order — clustering is not a book-order artifact.",hc=AMBER)
FS(prs,"Book vs revelation, correlated","N05_03_corr.png","RELATED, NOT IDENTICAL","The two orders correlate but differ — so passing both is genuine independent evidence, not the same test twice.")
FS(prs,"The omnibus picture","L3_10_omnibus.png","ALL 29, ONE TEST","Pooled, both observed values land beyond the null — the project's first robust, all-inclusive latent feature.",hc=TEAL)
FS(prs,"A two-layer index","N16_07_twolayer.png","WHERE AND WHEN","Each tag connects a book-order family to a revelation-order family — an index over two coordinate systems at once.")
FS(prs,"Handle nuzūl with care","N05_07_caveat.png","AN HONEST CAVEAT","Revelation order is reconstructed; chronologies mostly agree on phase, and small reorderings barely move the families.",hc=AMBER)
s=Tt(prs,"Why two orders matter")
two(s,[L("INDEPENDENT EVIDENCE",18,True,NAVY),L("Muṣḥaf and nuzūl are different arrangements; a pattern in both is much stronger than a pattern in one.",16.5,True,TEAL)],
 [L("ROBUST TO ERROR",18,True,AMBER),L("Because chronologies agree on phase, plausible reordering does not overturn the contiguity.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — ḤM 60–66")
two(s,[L("CONSECUTIVE IN TIME",18,True,TEAL),L("The seven Ḥawāmīm were revealed in an unbroken stretch of revelation slots — not only collected together, but sent together.",16.5,True,NAVY)],
 [L("BOTH AXES",18,True,AMBER),L("Contiguous in the book AND in time — the strongest single instance of the index.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating the reconstructed nuzūl order as exact and over-claiming precision.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Report the result as robust-to-reordering and inheriting the chronology's uncertainty.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — time as an axis")
two(s,[L("عالم التكوين",18,True,AMBER),L("Developmental genes are co-expressed in time windows, not only co-located in the genome.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("Same-tag sūras are co-located in the book AND co-timed in revelation — a two-axis index.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does passing in two orders beat passing in one?  • How sensitive is the result to nuzūl errors?  • What would falsify the revelation-order claim?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Seek independent confirmation before trusting any single test.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① NUZŪL","revelation slots",TINT,TEAL),("② DISTANCE","within-family Δ",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ COMPARE","to book order",REDT,RED)],
 "Recompute the within-family distance in revelation order, run the same null, and compare the two independent verdicts.")
s=slide(prs); audit(s,"Revelation-order contiguity holds for every family (p≈2×10⁻⁵), independent of book order.","Any claim that nuzūl order is exact — it is a reconstruction, openly caveated.","The precise chronology of individual sūras — we rely on phase-level agreement.")
s=slide(prs); takeaway(s,"Independent replication across two orderings is the difference between a curiosity and a finding.","In revelation order too, the disjoint letters index contiguous families — the second half of the core result.")
s=Tt(prs,"Key numbers (revelation order)")
two(s,[L("OBSERVED",18,True,TEAL),L("Within-family Δ = 7.30 vs null mean ≈ 19; p ≈ 2×10⁻⁵, independent of book order.",16.5,True,NAVY)],[L("FAMILIES",18,True,AMBER),L("ALM 0.004, ALR 0.0017, ḤM ~0, ṬSM 0.034 — all cluster in time as well.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[5]=save(prs,"05_Contiguity_Nuzul_DL.pptx")

# ============ L6 PER-FAMILY DEEP DIVE ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 6","Per-Family Deep Dive",
 "No cherry-picking: we test ḤM, ALM, ALR and ṬSM one by one, in both orders, against per-family nulls — and check that the result survives dropping any single sūra.",
 "Every multi-member family is individually significant; singletons are flagged, not counted.")
FS(prs,"ḤM vs its own null","N06_01_hm_null.png","THE STRONGEST","Holding family size fixed, ḤM's clustering is essentially unreachable by chance.",hc=TEAL)
FS(prs,"ALM vs its own null","N06_02_alm_null.png","SPLIT BUT TIGHT","ALM's two-run structure still beats its per-family null (p≈0.009 muṣḥaf).")
FS(prs,"ALR vs its own null","N06_03_alr_null.png","CLEAN","Alif-Lām-Rā clusters far tighter than random size-5 sets of muqaṭṭaʿāt sūras.",hc=AMBER)
FS(prs,"Per-family summary","N06_04_perfam_summary.png","FOUR FOR FOUR","Every family clears p=0.05 in both muṣḥaf and revelation order — the result is broad, not narrow.",hc=TEAL)
FS(prs,"Family span","N06_05_span.png","TIGHT FOR SIZE","Each family's muṣḥaf span is small relative to its size — the members really do huddle.")
FS(prs,"ḤM detail","N06_06_hm_detail.png","40–46","The Ḥawāmīm block, up close: seven adjacent sūras with the same opening.",hc=TEAL)
FS(prs,"ALM detail","N06_07_alm_detail.png","TWO CLUSTERS","2,3 at the front, 29–32 mid-book — structured, not scattered.")
FS(prs,"ṬSM brackets ṬS","N06_08_tsm_detail.png","A NESTED VARIANT","ṬSM (26,28) sits on either side of the ṬS singleton (27) — a suggestive boundary pattern.",hc=AMBER)
FS(prs,"Compact on both axes","N06_09_2d.png","WHERE & WHEN","Plotted by (book, revelation), each family forms its own tight cluster simultaneously.",hc=TEAL)
FS(prs,"Drop-one robustness","N06_10_dropone.png","NOT ONE OUTLIER","Removing any single sūra barely changes the within-family distance — no family rides on one member.")
s=Tt(prs,"Why test each family")
two(s,[L("GUARD AGAINST ONE-FAMILY EFFECTS",18,True,NAVY),L("If only ḤM drove the omnibus, the 'pointer' would be a single coincidence. It doesn't — all four pass.",16.5,True,TEAL)],
 [L("HONEST ABOUT SINGLETONS",18,True,AMBER),L("Size-1 families have no internal distance; we flag ق, ن, ص … rather than pretend to test them.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the four families")
three(s,[L("ḤM 40–46",17,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ» — seven consecutive.",16)],
 [L("ALR 10–15",17,True,AMBER),L("«الٓرٓ ۚ تِلْكَ ءَايَـٰتُ ٱلْكِتَـٰبِ» — a tight run.",16)],
 [L("ALM 2,3,29–32",17,True,NAVY),L("Two early, then a late block.",16)])
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Reporting only the most spectacular family (ḤM) and ignoring the rest.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Pre-register all families and report every one — including the weaker ṬSM.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Robustness checks")
three(s,[L("PER-FAMILY NULL",17,True,TEAL),L("Each family beats its own size-matched null.",16)],
 [L("BOTH ORDERS",17,True,AMBER),L("muṣḥaf and revelation agree per family.",16)],
 [L("DROP-ONE",17,True,NAVY),L("No single sūra drives any family.",16)])
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why can't singletons be tested for clustering?  • Why is drop-one robustness reassuring?  • Does ṬSM's weaker p weaken the overall claim?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Stress-test a result subgroup by subgroup before believing the aggregate.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PICK","a family",TINT,TEAL),("② NULL","size-matched",AMBERT,AMBER),("③ ORDERS","muṣḥaf & nuzūl",TINT,TEAL),("④ DROP","one-out check",REDT,RED)],
 "Select any family, run its size-matched null in both orders, and watch the drop-one robustness check.")
s=slide(prs); audit(s,"All four multi-member families are individually significant in both orders and robust to drop-one.","Any aggregate claim that hides a single dominating family — here none dominates.","Singletons — flagged honestly as untestable for internal clustering.")
s=slide(prs); takeaway(s,"A finding that holds in every subgroup, not just on average, is one you can build a course on.","The pointer-as-index is broad: every testable family clusters, in both orders, robustly.")
s=Tt(prs,"Key numbers (per family)")
two(s,[L("BOTH ORDERS",18,True,NAVY),L("4 / 4 multi-member families significant in muṣḥaf AND revelation order.",16.5,True,TEAL)],[L("ROBUST",18,True,AMBER),L("Drop-one checks: no family relies on a single member.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[6]=save(prs,"06_PerFamily_DL.pptx")

# ============ L7 THE LONG-SURA FLAG ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 7","The Long-Sūra Flag",
 "A second organizational fact: the disjoint letters mark the LONG sūras — median 85 vs 26 verses, p ≈ 2×10⁻⁵ against random 29-sūra sets. Yet the tag does not encode a shared length per family.",
 "Lengths computed directly from Book6.xlsx (max āyah per sūra).")
FS(prs,"They are the long ones","L4_01_length_hist.png","MEDIAN 85 vs 26","The two length distributions barely overlap — disjoint-letter sūras sit on the book's longest chapters.")
FS(prs,"Not by chance","L4_02_length_null.png","p ≈ 2×10⁻⁵","Against 5,000 random 29-sūra sets, the muqaṭṭaʿāt median length is far out in the tail.",hc=TEAL)
FS(prs,"The contrast at a glance","L4_03_boxplot.png","TWO POPULATIONS","Side by side, the boxes hardly touch — a clean, reproducible marker.",hc=AMBER)
FS(prs,"Violin view","N07_01_violin.png","SHAPE, NOT JUST MEDIAN","The full distributions confirm it: muqaṭṭaʿāt mass sits high, others low.")
FS(prs,"Length CDFs","N07_02_cdf.png","SEPARATED CURVES","The cumulative curves are shifted apart across the whole range, not just at the median.",hc=TEAL)
FS(prs,"The longest are tagged","L4_08_top_long.png","READ IT BACK","Among the longest sūras, the teal (disjoint-letter) bars dominate — al-Baqarah, Āl ʿImrān, al-Aʿrāf.")
FS(prs,"Top-29 by length","N07_04_top29.png","OVERREPRESENTED","Of the 29 longest sūras, a large majority carry disjoint-letter openings.",hc=AMBER)
FS(prs,"Cumulative verse share","N07_03_cumshare.png","WHERE THE TEXT LIVES","The longest sūras hold most of the corpus's verses — so flagging them flags the bulk of the book.")
FS(prs,"But not shared per tag","L4_07_length_not_shared.png","POSITIONAL, NOT ATTRIBUTE","Within a family, lengths differ as much as random (p≈0.29) — the tag marks 'a long sūra here', not a length.",hc=RED)
FS(prs,"The magnitude","N11_10_lenmag.png","A 3.3× RATIO","Median 85 vs 26 is a large, plain effect — not a marginal statistical wrinkle.",hc=TEAL)
s=Tt(prs,"Group property vs per-tag property")
two(s,[L("AS A GROUP: LONG (✓)",18,True,TEAL),L("The 29 muqaṭṭaʿāt sūras are, collectively, the long ones — robustly (p≈2×10⁻⁵).",16.5,True,NAVY)],
 [L("PER TAG: NO LENGTH (✗)",18,True,RED),L("ḤM members range widely in length; the tag does not encode a specific size (p≈0.29).",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Read it back — the giants")
two(s,[L("THE PILLARS CARRY TAGS",18,True,TEAL),L("al-Baqarah (2, الٓمٓ, 286 āyāt), Āl ʿImrān (3, الٓمٓ, 200), al-Aʿrāf (7, الٓمٓصٓ, 206).",16.5,True,NAVY)],
 [L("A STRUCTURAL ROLE",18,True,AMBER),L("Marking the major sūras is itself organizational — flagging where the book's weight sits.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Concluding 'the tag means long sūra' — but members differ widely in length.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Separate a group property (long, as a set) from a per-label property (a length per tag — false).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is 'long as a group' different from 'a length per tag'?  • Why might an index flag the major sūras?  • How would you test for a size attribute?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Distinguish a property of the set from a property of each label — they need different nulls.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① LENGTHS","verses/sūra",TINT,TEAL),("② COMPARE","muq vs others",AMBERT,AMBER),("③ NULL","random 29-sets",TINT,TEAL),("④ PER-TAG","length null",REDT,RED)],
 "Compare muqaṭṭaʿāt vs non lengths, test the group difference against random sets, then test for a per-tag length (and watch it fail).")
s=slide(prs); audit(s,"Muqaṭṭaʿāt flag the long sūras as a group (p≈2×10⁻⁵).","The claim of a shared length per tag — refuted (p≈0.29).","Why the long sūras specifically — the mechanism is open; we report the association.")
s=slide(prs); takeaway(s,"An index can mark importance (size/position) without duplicating content — exactly what these tags do.","The disjoint letters flag the major sūras while remaining a purely positional pointer.")
s=Tt(prs,"Key numbers (length)")
two(s,[L("THE CONTRAST",18,True,TEAL),L("Median 85 vs 26 verses; random 29-sūra null p ≈ 2×10⁻⁵.",16.5,True,NAVY)],[L("NOT PER TAG",18,True,RED),L("Within-family length difference: p ≈ 0.29 — positional, not a length attribute.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Recap — the long-sūra flag")
two(s,[L("GROUP PROPERTY",18,True,NAVY),L("As a set, the 29 are the long sūras; this is robust and large (a 3.3× median ratio).",16.5,True,TEAL)],[L("STILL AN INDEX",18,True,AMBER),L("The tag marks importance/position, not a specific length per family.",16.5,True,NAVY)],sp=0.5,fa=TINT2,fb=AMBERT)
counts[7]=save(prs,"07_LongSura_DL.pptx")

# ============ L8 REVELATION-PHASE MAPPING ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 8","Revelation-Phase Mapping",
 "A third organizational layer: the tags map onto revelation PHASE — simple/short tags early-Meccan, the multi-letter families late-Meccan, and the mixed المر alone in the Medinan period.",
 "Phase read from the nuzūl reconstruction; a systematic, quantified mapping.")
FS(prs,"Phase counts","N08_01_phasecount.png","A PATTERNED SPREAD","The 29 sūras distribute across early-Meccan, late-Meccan and Medinan in a structured, non-uniform way.")
FS(prs,"By tag type","L4_04_phase_by_type.png","SIMPLE EARLY, FAMILIES LATE","Single/short tags appear first; the multi-letter families come later; the mixed المر last.",hc=TEAL)
FS(prs,"Families across phases","N08_02_bands.png","EACH IN ITS BAND","Plotted on the revelation axis with phase shading, families occupy distinct stretches.")
FS(prs,"Each family's window","N08_04_window.png","ORDERED IN TIME","Mean revelation slot differs by family — the index is temporal as well as positional.",hc=AMBER)
FS(prs,"Mean nuzūl by family","L4_05_mean_nuzul.png","DISTINCT WINDOWS","ḤM, ALM, ALR, ṬSM each cluster around their own revelation slot.")
FS(prs,"Long and late","N08_03_longlate.png","TWO TRAITS, ONE CORNER","Length vs revelation order: the muqaṭṭaʿāt concentrate in the long, late-Meccan corner.",hc=TEAL)
FS(prs,"Length vs nuzūl","L4_06_len_vs_nuzul.png","REINFORCING FACTS","The organizational facts — long, late, grouped — line up rather than conflict.")
FS(prs,"Complexity rises with time","N08_06_complexity.png","A GRADIENT","Tag complexity (single → family → mixed) tracks revelation time — a clean ordering.",hc=AMBER)
FS(prs,"The المر outlier","L4_10_almr_outlier.png","A LONE MEDINAN","المر (13) sits inside the الر run yet is revealed Medinan — the single phase outlier.",hc=RED)
FS(prs,"Outlier, isolated","N08_05_almr.png","ONE OF A KIND","On the revelation axis, المر stands apart from every other disjoint-letter sūra.")
s=Tt(prs,"What phase-mapping adds")
two(s,[L("A THIRD LAYER",18,True,NAVY),L("Beyond grouping and length, the tags carry temporal structure — the index orders onto revelation phase.",16.5,True,TEAL)],
 [L("LARGELY KNOWN, NOW QUANTIFIED",18,True,AMBER),L("Most muqaṭṭaʿāt are Meccan; the value here is the systematic, measured mapping.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the phases")
three(s,[L("EARLY-MECCAN",17,True,AMBER),L("ق, ن, ص, طه, يس — the single/short tags.",16)],
 [L("LATE-MECCAN",17,True,TEAL),L("ALR, ḤM, ALM — the families.",16)],
 [L("MEDINAN",17,True,RED),L("المر (13) — alone.",16)])
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Over-reading phase order as a hidden message or 'plan' in the letters.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Report it as an organizational regularity consistent with the pointer model — no more.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — timing marks")
two(s,[L("عالم التكوين",18,True,AMBER),L("Regulatory marks time gene expression to developmental windows.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("Disjoint-letter tags co-occur with revelation phase — a timing layer over the text.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Is phase-ordering surprising given most muqaṭṭaʿāt are Meccan?  • What would the المر outlier predict if tested?  • Does complexity-vs-time imply anything causal?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Map a structure onto an external axis (time) to reveal regularities the static view hides.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PHASE","early/late/Medinan",TINT,TEAL),("② TAG TYPE","single/family/mixed",AMBERT,AMBER),("③ MAP","tag → phase",TINT,TEAL),("④ OUTLIER","spot المر",REDT,RED)],
 "Map each tag type onto revelation phase and locate the lone Medinan outlier, المر.")
s=slide(prs); audit(s,"A systematic tag→phase mapping (simple early, families late, المر Medinan).","Any reading of the phase order as an encoded message — unsupported.","Whether المر marks a transition — suggestive, not yet formally tested.")
s=slide(prs); takeaway(s,"Projecting structure onto a time axis exposes order invisible in a single snapshot.","The disjoint letters carry a clean revelation-phase layer — a third organizational fact, all positional.")
s=Tt(prs,"Key numbers (phase)")
two(s,[L("THE GRADIENT",18,True,TEAL),L("Mean nuzūl slot ≈ 25 (single/short) → 70 (families) → 96 (mixed المر).",16.5,True,NAVY)],[L("STRUCTURED",18,True,AMBER),L("Tags map onto revelation phase in a patterned, non-uniform way.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[8]=save(prs,"08_Revelation_Phase_DL.pptx")

# ============ L9 PERMUTATION TESTS IN DEPTH ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 9","Permutation Tests in Depth",
 "The engine under the course: exchangeability, the null distribution, and why freeze-the-sūras / shuffle-the-labels isolates the specific tag's effect. The method that can say NO.",
 "Same machinery that confirmed contiguity refuted the frequency claim — that is why it earns trust.")
FS(prs,"Exchangeability","N09_01_exchange.png","THE CORE ASSUMPTION","Under the null, tag labels are interchangeable — so every relabeling is equally likely, and the observed rank gives a p-value.")
FS(prs,"The null distribution","N09_02_nulldist.png","WHAT 'BY CHANCE' LOOKS LIKE","Compute the statistic for thousands of relabelings; their spread is the chance distribution.",hc=TEAL)
FS(prs,"Freeze, then shuffle","L2_08_freeze_shuffle.png","ISOLATE THE TAG","Hold the 29 sūras in place; shuffle only which opening each gets — removing background clustering entirely.")
FS(prs,"The trap of a weak null","L2_01_trap.png","RANDOM CHAPTERS MISLEAD","Against random chapters everything clusters; only the label-permutation null tests the specific tag.",hc=RED)
FS(prs,"Which null? It matters","N09_05_nullchoice.png","RIGHT vs WRONG","The two nulls give very different pictures; the label-permutation one is the honest comparison.")
FS(prs,"Observed in the tail","L2_02_labelperm_mushaf.png","THE RESULT","The real tagging's Δ sits far below the whole null cloud — p ≈ 2×10⁻⁵.",hc=TEAL)
FS(prs,"Same across seeds","N09_03_seeds.png","NOT A LUCKY DRAW","Different random seeds reproduce the same null shape and the same verdict.")
FS(prs,"Convergence","N09_04_converge.png","SAMPLE ENOUGH","With too few permutations the p-value is noisy; by ~50,000 it settles.",hc=AMBER)
FS(prs,"p-value stability","L2_06_pvalue_convergence.png","REPORT THE CONVERGED VALUE","A p-value is an estimate with error; we report it once stable.")
FS(prs,"Revelation-order null","L2_03_labelperm_nuzul.png","REPEAT, CONFIRM","The identical machinery on nuzūl order returns the same p — independent confirmation.",hc=TEAL)
s=Tt(prs,"Why permutation, not a formula")
two(s,[L("NO DISTRIBUTION ASSUMED",18,True,NAVY),L("Permutation tests build the null from the data itself — no normality, no closed form, exact by construction.",16.5,True,TEAL)],
 [L("EXACTLY THE RIGHT NULL",18,True,AMBER),L("By shuffling only labels, the test answers precisely the pointer question.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The statistic and the tail")
two(s,[L("CHOOSE THE STATISTIC FIRST",18,True,TEAL),L("Within-family mean distance, fixed in advance — no fishing for the metric that looks best.",16.5,True,NAVY)],
 [L("READ THE TAIL",18,True,AMBER),L("p = fraction of relabelings at least as clustered as the real one.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Using a random-chapter baseline, where any muqaṭṭaʿāt grouping looks clustered.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Permute labels among the fixed 29 — controlling background clustering by design.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Why it is falsifiable")
two(s,[L("IT CAN SAY NO",18,True,TEAL),L("The same test that confirmed contiguity refuted the frequency claim (0/29) and the theme claim (p≈0.27).",16.5,True,NAVY)],
 [L("THE OPPOSITE OF NUMEROLOGY",18,True,RED),L("Numerology never fails; a permutation test routinely does — which is why its 'yes' means something.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• What does exchangeability assume?  • Why shuffle labels, not chapters?  • Why report a converged p-value?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Build the null from the data, with the symmetry that matches your hypothesis.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① STATISTIC","within-family Δ",TINT,TEAL),("② SHUFFLE","labels only",AMBERT,AMBER),("③ REPEAT","50,000 draws",TINT,TEAL),("④ TAIL","read the p",REDT,RED)],
 "Fix the statistic, permute the labels tens of thousands of times, and read the observed value's position in the tail.")
s=slide(prs); audit(s,"Permutation tests give an exact, assumption-light null matched to the pointer hypothesis.","Weak-null shortcuts (random chapters) that conflate the tag with background clustering.","Whether every conceivable statistic was tried — we fix the main one in advance.")
s=slide(prs); takeaway(s,"Resampling lets you test almost anything honestly — the workhorse of modern data analysis.","Freeze the items, shuffle the labels: the design that isolates a tag effect and can also reject it.")
s=Tt(prs,"Key numbers (permutation)")
two(s,[L("THE NULL",18,True,NAVY),L("29 fixed sūras; 50,000 label permutations; statistic = within-family mean pairwise distance.",16.5,True,TEAL)],[L("THE OUTPUT",18,True,AMBER),L("p = tail fraction; converged and seed-independent.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[9]=save(prs,"09_Permutation_Depth_DL.pptx")

# ============ L10 MULTIPLE COMPARISONS & FDR ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 10","Multiple Comparisons & FDR",
 "Test many things and some will sparkle by luck. This lecture covers the look-elsewhere effect, Benjamini–Hochberg FDR control, and why the contiguity result survives even the strict Bonferroni correction.",
 "Declare the tests in advance; report all of them; correct for how many you ran.")
FS(prs,"The look-elsewhere effect","N10_01_lookelse.png","LUCK AT SCALE","With 27 letters × several orderings × many statistics, some 'discoveries' are guaranteed by chance alone.")
FS(prs,"Benjamini–Hochberg","N10_02_bh.png","CONTROL THE FDR","Compare each ranked p to k/m·α; the BH line tells you which survive a controlled false-discovery rate.",hc=TEAL)
FS(prs,"FWER explodes","N10_04_fwer.png","WHY CORRECT","The chance of at least one false positive climbs fast with the number of tests.",hc=RED)
FS(prs,"Only م survives","N10_03_survive.png","HONEST PER-LETTER","Of the letters tested for enrichment, only م clears FDR control — and barely.")
FS(prs,"Declare in advance","N10_05_declare.png","CONFIRMATORY, NOT FISHED","Fix channel, statistic, null and threshold before testing; report every test, not just winners.",hc=TEAL)
FS(prs,"Survives Bonferroni","N10_06_bonferroni.png","THE STRICTEST TEST","Even dividing α by the number of tests, the contiguity p stays far below threshold.")
FS(prs,"All tests on one plot","N10_07_allbh.png","TWO STAND CLEAR","Plotting every p, the two contiguity results sit orders of magnitude below the BH line.",hc=AMBER)
FS(prs,"Under each correction","N10_08_corrections.png","ROBUST p","Raw, BH-adjusted, Bonferroni — contiguity remains significant under all three.",hc=TEAL)
FS(prs,"After correction","N10_09_after.png","ONLY CONTIGUITY IS CLEAN","The frequency claim dies; single-letter ق becomes borderline; contiguity alone is unambiguous.")
FS(prs,"Single-letter FDR","L2_10_fdr.png","THE LETTERS CASE","The per-letter enrichment search, corrected — most candidates fall away.",hc=AMBER)
s=Tt(prs,"The two error rates")
two(s,[L("FWER",18,True,NAVY),L("Probability of ANY false positive — strict (Bonferroni). Use when even one error is costly.",16.5,True,TEAL)],
 [L("FDR",18,True,AMBER),L("Expected fraction of discoveries that are false — less strict (BH). Use for screening many candidates.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Why pre-registration helps")
two(s,[L("SHRINK THE SEARCH",18,True,TEAL),L("Declaring the statistic and families in advance cuts the effective number of tests — fewer chances to fool yourself.",16.5,True,NAVY)],
 [L("REPORT NEGATIVES",18,True,AMBER),L("Publishing the failures (theme, frequency) keeps the correction honest.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Reporting the single best p from a large silent search — the classic false discovery.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Count every test performed and correct; a result that survives correction is trustworthy.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Read it back")
two(s,[L("WHAT SURVIVES",18,True,TEAL),L("Muṣḥaf & revelation contiguity (p≈2×10⁻⁵) clear even Bonferroni; the long-sūra flag too.",16.5,True,NAVY)],
 [L("WHAT DOESN'T",18,True,RED),L("The frequency code (0/29) and the theme (p≈0.27) fail outright; single-letter ق is borderline.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• FWER vs FDR — when use which?  • Why does declaring tests in advance matter?  • Why report failures?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Correct for the size of your search; trust results that survive it.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① COUNT","# of tests",TINT,TEAL),("② RANK","sort p-values",AMBERT,AMBER),("③ BH/Bonf","apply correction",TINT,TEAL),("④ KEEP","survivors",REDT,RED)],
 "Count the tests, rank the p-values, apply BH and Bonferroni, and see which findings survive.")
s=slide(prs); audit(s,"Contiguity survives FDR and Bonferroni; corrections are applied corpus-wide.","Cherry-picking the best p from a large hidden search.","The exact size of every informal search — we correct for the declared tests.")
s=slide(prs); takeaway(s,"Multiple-comparison control is what separates a real signal from the inevitable lucky one.","The disjoint-letter contiguity is robust to the strictest correction; the content claims are not.")
s=Tt(prs,"Key numbers (corrections)")
two(s,[L("SURVIVES",18,True,TEAL),L("Contiguity p ≈ 2×10⁻⁵ clears BH and Bonferroni for the declared tests.",16.5,True,NAVY)],[L("DIES",18,True,RED),L("Frequency code 0/29; theme p ≈ 0.27; single-letter ق borderline after correction.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
counts[10]=save(prs,"10_Multiple_Comparisons_DL.pptx")

# ============ L11 EFFECT SIZE, POWER & THE SCALE RULE ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 11","Effect Size, Power & the Scale Rule",
 "A p-value says 'is it real?'; effect size says 'how big?'; power says 'could we have detected it?'. Here we show the contiguity effect is large, the families adequately powered, and singletons untestable.",
 "Magnitude and power, not significance alone.")
FS(prs,"The effect is large","N11_01_effect.png","MANY NULL-SDs","The observed within-family distance lies several null standard deviations below the chance mean.")
FS(prs,"Deep in the tail","N11_02_sd.png","NOT MARGINAL","Observed sits far outside the null's ±1 SD band — a big effect, not a borderline one.",hc=TEAL)
FS(prs,"Power vs family size","N11_03_power.png","SIZE BUYS POWER","Simulated detection probability rises with family size — bigger families are easier to confirm.")
FS(prs,"Reaching 0.8 power","N11_07_power80.png","ADEQUATELY POWERED","Most multi-member families clear conventional power; only the smallest are marginal.",hc=AMBER)
FS(prs,"Singletons can't be tested","N11_04_testability.png","SIZE-1 = NO SIGNAL","A family of one has no internal distance — we flag ق, ن, ص rather than fake a test.",hc=RED)
FS(prs,"The scale rule","N11_05_scalerule.png","STABILITY WITH n","The standard error of the estimate shrinks as more families/items are pooled — estimates settle.")
FS(prs,"Effects across findings","N11_06_effects3.png","ALL LARGE","Muṣḥaf, revelation and length effects are all multiple null-SDs — consistently big.",hc=TEAL)
FS(prs,"Report both","N11_08_both.png","SIGNIFICANCE + MAGNITUDE","'Is it real?' and 'how big?' are different questions; a complete result answers both.")
FS(prs,"Observed vs null spread","N11_09_errbar.png","CLEANLY SEPARATED","Observed value with its uncertainty does not overlap the null's spread.",hc=AMBER)
FS(prs,"The length magnitude","N11_10_lenmag.png","3.3× MEDIAN","85 vs 26 verses is a large, interpretable effect, independent of any p-value.",hc=TEAL)
s=Tt(prs,"Why effect size matters")
two(s,[L("p ≠ IMPORTANCE",18,True,NAVY),L("A tiny effect can be 'significant' with enough data; a big effect can be missed with too little. Always report magnitude.",16.5,True,TEAL)],
 [L("HERE: BIG AND REAL",18,True,AMBER),L("The contiguity effect is both significant and large — the strongest kind of result.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Power and the singletons")
two(s,[L("WHY FLAG, NOT TEST",18,True,TEAL),L("Singletons (ق, ن, ص…) have size 1 — zero internal pairs, so no clustering statistic exists.",16.5,True,NAVY)],
 [L("HONEST SCOPE",18,True,AMBER),L("We report them as observations and a hypothesis (single-letter content), not as validated results.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The scale rule, restated")
two(s,[L("MORE DATA → STABLER",18,True,NAVY),L("Estimates and p-values stabilize as n grows; small samples give noisy, untrustworthy numbers.",16.5,True,TEAL)],
 [L("WHY WE POOL ALL 29",18,True,AMBER),L("The omnibus over all families is more stable than any single-family test.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Reporting a p-value with no effect size — or testing an underpowered singleton.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Always pair p with magnitude, and refuse tests the data can't support.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why can a significant result still be unimportant?  • Why can't singletons be tested?  • What does the scale rule imply for small corpora?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Report magnitude and power alongside significance — always.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① EFFECT","null-SDs",TINT,TEAL),("② POWER","vs family size",AMBERT,AMBER),("③ SCALE","SE vs n",TINT,TEAL),("④ SCOPE","flag singletons",REDT,RED)],
 "Measure the effect in null-SDs, simulate power by family size, watch the standard error shrink with n, and see why singletons are flagged.")
s=slide(prs); audit(s,"The effect is large (many null-SDs) and the multi-member families are adequately powered.","Reporting significance with no magnitude, or testing size-1 families.","The exact power for the smallest family (ṬSM) — limited; reported as such.")
s=slide(prs); takeaway(s,"'Significant' and 'large' are different; good science reports both and respects power limits.","The contiguity effect is big and well-powered; singletons are honestly out of testable scope.")
s=Tt(prs,"Key numbers (effect & power)")
two(s,[L("LARGE EFFECT",18,True,TEAL),L("Observed within-family distance is many null-SDs below the chance mean.",16.5,True,NAVY)],[L("POWER",18,True,AMBER),L("Multi-member families adequately powered; singletons (size 1) untestable.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[11]=save(prs,"11_EffectSize_Power_DL.pptx")

# ============ L12 BOOTSTRAP & CONFIDENCE ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 12","Bootstrap & Confidence",
 "Permutation tests ask 'is it chance?'; the bootstrap asks 'how uncertain is our estimate?'. Resampling the family members gives confidence intervals on the within-family distance — and they exclude the null region.",
 "A complementary lens: not just a p-value, but an interval.")
FS(prs,"The bootstrap idea","N12_03_idea.png","RESAMPLE WITH REPLACEMENT","Redraw family members, recompute the statistic; the spread of results is the sampling uncertainty.")
FS(prs,"CI — book order","N12_01_ci_mushaf.png","A TIGHT INTERVAL","The 95% bootstrap CI for the within-family distance sits well below the null region.",hc=TEAL)
FS(prs,"Stable across seeds","N12_02_ci_seed.png","NOT A FLUKE","Different resampling seeds give the same interval — the estimate is stable.")
FS(prs,"Per-family distributions","N12_04_perfam.png","EACH FAMILY TIGHT","Bootstrapping each family separately, all distributions stay small.",hc=AMBER)
FS(prs,"Forest plot","N12_05_forest.png","POINT ± CI","Per-family point estimates with their bootstrap intervals — all far from chance.",hc=TEAL)
FS(prs,"Length CI","N12_06_lenci.png","MEDIAN LENGTH INTERVAL","The bootstrap CI for muqaṭṭaʿāt median length stays high above the corpus median.")
FS(prs,"CI width settles","N12_07_ciwidth.png","ENOUGH RESAMPLES","Interval width stabilizes as resamples grow — report once stable.",hc=AMBER)
FS(prs,"Bootstrap vs null","N12_08_vsnull.png","NO OVERLAP","The bootstrap (around the observed) and the null (around chance) distributions do not overlap.",hc=TEAL)
FS(prs,"Observed vs null, with error","N12_09_compare.png","CLEAN SEPARATION","Observed ± bootstrap SE sits clear of null ± SD — significance and stability together.")
FS(prs,"What the CI tells us","N12_10_meaning.png","STABLE & REPRODUCIBLE","The clustering is not one lucky draw; resampling keeps it small and excludes the null.",hc=TEAL)
s=Tt(prs,"Permutation vs bootstrap")
two(s,[L("PERMUTATION → p-VALUE",18,True,NAVY),L("Shuffles labels to ask: is this chance? Gives the significance.",16.5,True,TEAL)],
 [L("BOOTSTRAP → INTERVAL",18,True,AMBER),L("Resamples members to ask: how precise is our estimate? Gives the uncertainty.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Reading a confidence interval")
two(s,[L("WHAT IT MEANS",18,True,TEAL),L("Across resamples, the statistic stays in this range — so the effect is not an artifact of one particular sample.",16.5,True,NAVY)],
 [L("EXCLUDES CHANCE",18,True,AMBER),L("The interval lies entirely below the null region — consistent with the permutation p-value.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Reporting a point estimate with no interval — hiding how (un)certain it is.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Pair every estimate with a bootstrap CI; let the reader see the precision.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Two lenses, one verdict")
two(s,[L("THEY AGREE",18,True,NAVY),L("Permutation says 'not chance'; bootstrap says 'precisely estimated and far from chance'. Same conclusion, two routes.",16.5,True,TEAL)],
 [L("CONFIDENCE EARNED",18,True,AMBER),L("Agreement across independent methods is what makes a result trustworthy.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• How does the bootstrap differ from a permutation test?  • What does a CI excluding the null mean?  • Why resample with replacement?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Quantify uncertainty, not just significance — report an interval.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① RESAMPLE","members w/ replacement",TINT,TEAL),("② RECOMPUTE","the statistic",AMBERT,AMBER),("③ PERCENTILES","95% CI",TINT,TEAL),("④ COMPARE","to the null",REDT,RED)],
 "Resample the families, recompute the distance, read the 95% interval, and check it clears the null region.")
s=slide(prs); audit(s,"Bootstrap CIs for the within-family distance exclude the null region in both orders.","Reporting estimates without uncertainty.","The smallest family's interval is wide — flagged as less precise.")
s=slide(prs); takeaway(s,"An estimate without an interval is half a result; the bootstrap supplies the other half.","Permutation and bootstrap agree: the contiguity is significant and precisely, stably estimated.")
s=Tt(prs,"Key numbers (bootstrap)")
two(s,[L("THE INTERVAL",18,True,TEAL),L("95% bootstrap CI for within-family distance sits entirely below the null region.",16.5,True,NAVY)],[L("AGREEMENT",18,True,AMBER),L("Permutation and bootstrap reach the same verdict by different routes.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[12]=save(prs,"12_Bootstrap_DL.pptx")

# ============ L13 NO SHARED THEME ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 13","What It Is NOT — No Shared Theme",
 "A pointer addresses; it does not describe. Root-profile similarity within a family is no greater than across families (label-permutation p ≈ 0.27). Distinctive roots are flavor, not a validated theme.",
 "The honest negatives are as important as the positive.")
FS(prs,"Within ≈ cross","N13_01_withincross.png","NO THEME PER TAG","For every family, within-family root similarity ≈ cross-family — no thematic cohesion by tag.",hc=RED)
FS(prs,"The semantic null","N13_02_semnull.png","p ≈ 0.27","Observed within-family similarity sits squarely inside the label-permutation null.")
FS(prs,"Overall within vs cross","N13_03_overall.png","0.723 vs 0.689","Pooled, the gap is a whisker — and a random regrouping produces it too.",hc=AMBER)
FS(prs,"Similarity heatmap","N13_04_heatmap.png","NO BLOCKS EMERGE","The 29×29 root-similarity map shows no family block structure — unlike the position matrices.")
FS(prs,"Distinctive roots are flavor","N13_05_flavor.png","ILLUSTRATIVE ONLY","الٓمٓ sūras feature كتب, قتل, موت — descriptive color, not a tested theme.",hc=AMBER)
FS(prs,"Group, not tag","N13_06_groupnottag.png","SIMILAR AS A SET","Muqaṭṭaʿāt resemble each other only as a general group of long sūras, not per family.")
FS(prs,"Within ≈ cross (per family)","L5_01_within_cross.png","BARS DON'T TOWER","If a tag marked a topic, teal would dwarf grey — it doesn't.",hc=RED)
FS(prs,"Semantic test fails","L5_02_semantic_null.png","MIDDLE OF THE CLOUD","The observed value is unremarkable under the null — no coherence.")
FS(prs,"Flavor, not finding","L5_07_distinctive_roots.png","DON'T OVER-READ","Distinctive roots are real but not a validated family theme.",hc=AMBER)
FS(prs,"Marginal overall","L5_08_overall_within_cross.png","A WHISKER APART","0.723 vs 0.689 — the kind of gap random regrouping also yields.",hc=TEAL)
s=Tt(prs,"The temptation to over-read")
two(s,[L("THE WISH",18,True,RED),L("It is tempting to say 'ḤM sūras are about X'. A satisfying story — but the data must license it.",16.5,True,NAVY)],
 [L("THE TEST",18,True,TEAL),L("Are same-tag sūras more similar than a random regrouping? Answer: no (p≈0.27).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Read it back — flavor vs finding")
two(s,[L("ROOTS EXIST",18,True,AMBER),L("الٓمٓ leans on كتب (write), قتل (kill), موت (death); حمٓ on دعو, حقق, یوم, حیی.",16.5,True,NAVY)],
 [L("BUT NOT VALIDATED",18,True,RED),L("Within-family ≈ cross-family similarity — these flavors fail the coherence test.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=REDT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Cherry-picking one striking root list and calling it the family's theme.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Test similarity against a label-permutation null over ALL families — here p≈0.27.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Why negatives matter")
two(s,[L("THEY SHARPEN THE CLAIM",18,True,NAVY),L("Showing the tag is NOT semantic is what makes 'positional pointer' precise rather than vague.",16.5,True,TEAL)],
 [L("AND BUILD TRUST",18,True,AMBER),L("A method that reports failures is one to believe when it reports success.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is within≈cross decisive against a theme?  • Why are distinctive roots only 'flavor'?  • Could a finer semantic measure find a theme?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Resist the satisfying story unless it beats the right null.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PROFILES","root multisets",TINT,TEAL),("② SIMILARITY","within vs cross",AMBERT,AMBER),("③ SHUFFLE","label-perm null",TINT,TEAL),("④ READ","p≈0.27",REDT,RED)],
 "Build root profiles, compare within- vs cross-family similarity, and run the label-permutation null (it lands at p≈0.27).")
s=slide(prs); audit(s,"A clean negative: no per-tag theme (p≈0.27), tested over all families.","Any thematic reading presented as a validated finding.","Whether a richer embedding could detect a faint theme — open, currently unsupported.")
s=slide(prs); takeaway(s,"Reporting what fails as plainly as what passes is what separates analysis from advocacy.","The disjoint letters do not describe their sūras thematically — they index them.")
s=Tt(prs,"Key numbers (no theme)")
two(s,[L("WITHIN ≈ CROSS",18,True,RED),L("Overall root cosine 0.723 within vs 0.689 cross; label-permutation p ≈ 0.27.",16.5,True,NAVY)],[L("VERDICT",18,True,TEAL),L("No validated per-tag theme; distinctive roots are illustrative flavor only.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
counts[13]=save(prs,"13_No_Theme_DL.pptx")

# ============ L14 NO FREQUENCY CODE ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 14","What It Is NOT — No Frequency Code",
 "The most seductive false positive: 'a sūra's opening letters are unusually frequent inside it.' Under the right baseline this collapses — 0 of 29 significant; Fisher χ²=60.6/df58, n.s. The letters are simply the commonest Arabic letters.",
 "The same data, an honest comparison — and the discovery disappears.")
FS(prs,"The seductive within-null","N14_01_within.png","LOOKS SPECTACULAR","Within الٓمٓ sūras, ا ل م rank near the top — a poster-ready p≤0.001.",hc=RED)
FS(prs,"The right baseline","N14_02_cross.png","≈ 1.0×, 0/29","Against OTHER sūras, own-letter density is ~1.0× — no enrichment in any family.",hc=TEAL)
FS(prs,"Two nulls, two verdicts","N14_03_twonulls.png","THE COLLAPSE","Significant under the wrong null, gone under the right one — same data.")
FS(prs,"Per-letter test","N14_04_perletter.png","ONLY م, BARELY","Of 27 letters vs non-disjoint sūras, only م clears p=0.05, at ~1.13×.",hc=AMBER)
FS(prs,"Aggregate is n.s.","N14_05_fisher.png","FISHER SAYS NO","Combining all sūras' own-letter densities: χ²=60.6/df58, squarely within the null.")
FS(prs,"Why it fails","N14_06_why.png","COMMON LETTERS","ا, ل, م are the commonest Arabic letters; any long text is 'rich' in them.",hc=RED)
FS(prs,"Within-chapter illusion","L2_04_falsepos_within.png","THE TRAP RESTATED","The within-chapter null asks only whether common letters are common.",hc=AMBER)
FS(prs,"Cross-chapter collapse","L2_05_collapse_cross.png","ASK 'MORE THAN NORMAL?'","Enrichment ≈ 1.0× across families; the effect evaporates.",hc=TEAL)
FS(prs,"Fisher omnibus","L5_09_fisher.png","NOT SIGNIFICANT","The aggregate enrichment test confirms: generic to Arabic.")
FS(prs,"Content fails, structure survives","L5_10_content_vs_org.png","THE RECURRING VERDICT","Content statistics match ordinary Arabic; only organization beats the null.",hc=TEAL)
s=Tt(prs,"Anatomy of a false positive")
two(s,[L("WRONG QUESTION",18,True,RED),L("'Are these letters frequent here?' — yes, because they are frequent everywhere.",16.5,True,NAVY)],
 [L("RIGHT QUESTION",18,True,TEAL),L("'Are they MORE frequent than in other sūras?' — no (0/29).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Read it back — common letters")
two(s,[L("THE ARABIC ALPHABET",18,True,AMBER),L("ا, ل, م top the frequency tables of any Arabic corpus; their prominence in الٓمٓ sūras is expected.",16.5,True,NAVY)],
 [L("NO HIDDEN CODE",18,True,RED),L("There is no letter-frequency miracle — the honest baseline removes it entirely.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=REDT)
s=Tt(prs,"Beat NORMAL, not just random")
two(s,[L("THE STANDARD",18,True,TEAL),L("A pattern must exceed not just randomness but ordinary language. The within-chapter null was too weak.",16.5,True,NAVY)],
 [L("PORTABLE LESSON",18,True,AMBER),L("Most 'amazing pattern' claims skip this step; asking 'more than normal?' dissolves them.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Publishing the within-chapter result — a textbook false positive.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Always compare to a natural-language baseline, not to randomness alone.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does the within-chapter null mislead?  • Why is 'more than other sūras' the right test?  • Why does only م barely pass?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Beat ordinary language, not just chance, before claiming a pattern.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① WITHIN","wrong null",REDT,RED),("② CROSS","right baseline",TINT,TEAL),("③ PER-LETTER","27 tests",AMBERT,AMBER),("④ FISHER","aggregate",TINT,TEAL)],
 "Toggle the within-chapter 'discovery' against the cross-chapter baseline and watch the enrichment fall to ~1.0×.")
s=slide(prs); audit(s,"Cross-chapter baseline and Fisher omnibus both refute the frequency claim (0/29).","The within-chapter 'discovery' — a false positive under a weak null.","A faint single-letter effect (next lecture) — separate and weak.")
s=slide(prs); takeaway(s,"The difference between a discovery and an artifact is often just the choice of baseline.","There is no disjoint-letter frequency code; the letters are simply common Arabic letters.")
s=Tt(prs,"Key numbers (no code)")
two(s,[L("WRONG NULL",18,True,RED),L("Within-chapter: ا ل م look top, p ≤ 0.001 — illusory.",16.5,True,NAVY)],[L("RIGHT BASELINE",18,True,TEAL),L("Cross-chapter: ≈ 1.0×, 0/29 significant; Fisher χ²=60.6/df58 (n.s.).",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
counts[14]=save(prs,"14_No_Frequency_Code_DL.pptx")

# ============ L15 THE SINGLE-LETTER LEADS ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 15","The Single-Letter Leads (ق, ن)",
 "The project's one honest content lead: in single-letter sūras, the opening letter can be unusually dense — ق in Sūrat Qāf ranks 111/114 (top 3.5%), ن in al-Qalam 105/114. Real, but borderline after correction.",
 "Reported as a hypothesis, not a finding — and the cleanest test the topic allows.")
FS(prs,"Single-letter ranks","N15_01_ranks.png","ق LEADS","Among single-letter sūras, ق is the 3rd-densest of all 114 in its own letter; others are unremarkable.",hc=TEAL)
FS(prs,"The p-values","N15_02_pvals.png","BORDERLINE","ق ≈ 0.035, ن ≈ 0.088 — suggestive, not decisive, before correction.",hc=AMBER)
FS(prs,"Qāf in the tail","N15_03_qaf_tail.png","EXTREME RIGHT","On the ق-density distribution across 114 sūras, Sūrat Qāf sits in the far-right tail.")
FS(prs,"Why single letters","N15_04_why.png","THE CLEANEST TEST","One letter = one clear hypothesis, with no multi-letter common-letter confound. «قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ».",hc=TEAL)
FS(prs,"After correction","N15_05_corrected.png","DROPS TO BORDERLINE","With several letters tested, ق's corrected p is borderline — held as a hypothesis, not asserted.",hc=AMBER)
FS(prs,"The honest verdict","N15_06_verdict.png","REAL, MODEST","ق real partial signal; ن weaker; ص, ي, ط not special; needs an external baseline.")
FS(prs,"Only single letters","N15_07_split.png","NOT THE FAMILIES","Multi-letter families show no content signal; any real letter effect is single-letter only.",hc=RED)
FS(prs,"Single-letter rank (corpus)","L5_05_single_rank.png","111/114","The cleanest content result in the whole project — and still modest.",hc=TEAL)
FS(prs,"The partial signal","L2_09_single_letter.png","ق ABOVE ALL","Qāf stands out; al-Qalam follows weakly; the rest are ordinary.")
FS(prs,"A lead for next round","N15_08_next.png","WHERE NEXT","Compare to Arabic acrostic poetry, re-run on cleaner orthography, correct across all single letters.",hc=AMBER)
s=Tt(prs,"What makes this honest")
two(s,[L("REPORTED, NOT INFLATED",18,True,TEAL),L("We state ق as a real but borderline partial signal — not a miracle, not nothing.",16.5,True,NAVY)],
 [L("CLEAREST AVAILABLE TEST",18,True,AMBER),L("Single-letter sūras avoid the common-letter confound that sank the family frequency claim.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — Sūrat Qāf")
two(s,[L("THE VERSE",18,True,TEAL),L("«قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ» (50:1) — and ق recurs notably through the sūra.",16.5,True,NAVY)],
 [L("A DEVICE?",18,True,AMBER),L("Possibly an acrostic-like emphasis — but we must rule out that this is generic to Arabic acrostics.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Trumpeting ق/Qāf as a proven miracle while ignoring multiple-comparison correction.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Correct across all single-letter cases and seek a non-Qur'anic Arabic baseline before claiming.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Why keep a borderline result")
two(s,[L("LEADS GUIDE WORK",18,True,NAVY),L("A modest, honest lead points the next round of analysis — without being oversold now.",16.5,True,TEAL)],
 [L("HONEST UNCERTAINTY",18,True,AMBER),L("Saying 'suggestive, needs a baseline' is more credible than a premature claim.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why are single-letter sūras the cleanest content test?  • Why does correction matter for ق?  • What baseline would settle it?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Hold a promising lead as a hypothesis until an external baseline confirms it.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① PICK","single-letter sūra",TINT,TEAL),("② DENSITY","rank /114",AMBERT,AMBER),("③ CORRECT","multiple tests",TINT,TEAL),("④ BASELINE","Arabic acrostics",REDT,RED)],
 "Rank each single-letter sūra by its letter's density, apply correction, and consider the external baseline needed to confirm ق.")
s=slide(prs); audit(s,"A real partial signal: single-letter ق ranks 111/114 in its own letter.","Any claim of a proven letter-miracle — ق is borderline after correction.","Whether the effect is generic to Arabic acrostics — needs a non-Qur'anic baseline.")
s=slide(prs); takeaway(s,"An honest borderline result, clearly labelled, is more valuable than an inflated certainty.","Single-letter ق is the project's strongest content lead — modest, real, and openly provisional.")
s=Tt(prs,"Key numbers (single letters)")
two(s,[L("ق / QĀF",18,True,TEAL),L("Rank 111/114 in its own letter (top 3.5%); raw p ≈ 0.035.",16.5,True,NAVY)],[L("AFTER CORRECTION",18,True,AMBER),L("Borderline; ن weaker (105/114); ص, ي, ط not special. Held as hypothesis.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[15]=save(prs,"15_Single_Letter_Leads_DL.pptx")

# ============ L16 BOUNDARY VARIANTS & THE GRAPH VIEW ============
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 16","Boundary Variants & the Graph View",
 "Two forward-looking threads: the mixed tags (المص, المر) that sit at family boundaries, and the sūra-family NETWORK — a bridge to the 2-D / corpus-graph course. The tags define a highly modular community structure.",
 "Observations and a graph model — hypotheses for the next round, clearly flagged.")
FS(prs,"The family network","N16_01_network.png","EDGES = SAME TAG","Drawing an edge between same-tag sūras yields four tight cliques and nine isolated singletons.",hc=TEAL)
FS(prs,"Degree distribution","N16_02_degree.png","CLIQUES & ISOLATES","Family members have high within-family degree; singletons have degree zero.")
FS(prs,"Adjacency matrix","N16_03_adjacency.png","BLOCK-DIAGONAL","The same-tag adjacency matrix is block-diagonal — the signature of clean communities.",hc=AMBER)
FS(prs,"Cliques","N16_04_cliques.png","CONNECTED COMPONENTS","Each family is a connected component; ḤM the largest at seven.",hc=TEAL)
FS(prs,"Modularity","N16_08_modularity.png","HIGHLY MODULAR","Tag-defined communities have far higher modularity than a random partition.")
FS(prs,"Boundary bridges","N16_05_bridges.png","المص & المر","Mixed tags sit at the seams: المص (7) between ALM and ALR; المر (13) inside the ALR run.",hc=AMBER)
FS(prs,"The hypothesis","N16_06_hypothesis.png","TRANSITION MARKERS?","Mixed tags may mark transitions/variants — a structural observation, not yet a tested claim.",hc=RED)
FS(prs,"Two-layer index","N16_07_twolayer.png","BOOK + TIME","Each tag links a book-order family to a revelation-order family — a two-layer graph.",hc=TEAL)
FS(prs,"Toward the corpus graph","N16_09_bridge.png","THE NEXT OBJECT","Nodes = sūras; the disjoint letters give one clean edge type; refrains and themes give more.")
FS(prs,"Community summary","N16_10_summary.png","CLEAN STRUCTURE","The muqaṭṭaʿāt define a clean community structure: contiguous, long, but not thematic.",hc=TEAL)
s=Tt(prs,"Why a graph view")
two(s,[L("FROM SEQUENCE TO NETWORK",18,True,NAVY),L("Treating sūras as nodes and shared structure as edges reframes the corpus as a graph — the productive object.",16.5,True,TEAL)],
 [L("ONE CLEAN EDGE TYPE",18,True,AMBER),L("The disjoint letters supply the first validated edge type; future work adds refrains, citations, themes.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the bridges")
two(s,[L("المص (7)",18,True,TEAL),L("الم+ص, sitting between the الم block (2,3) and the الر block (10–15).",16.5,True,NAVY)],
 [L("المر (13)",18,True,AMBER),L("الم+ر, inside the الر run yet revealed Medinan — a positional variant.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating the boundary-variant pattern as a proven design rather than a hypothesis.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Flag it as a structural observation and propose a formal test for the next round.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — networks")
two(s,[L("عالم التكوين",18,True,AMBER),L("Gene-regulatory and interaction networks reveal modules invisible in a linear genome.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The sūra-family network reveals the muqaṭṭaʿāt communities invisible in a flat reading.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• What does high modularity tell us?  • How would you test the boundary-variant idea?  • What edge types would enrich the graph?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("When sequence analysis saturates, reframe the data as a network.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
appslide(prs,[("① NODES","the 29 sūras",TINT,TEAL),("② EDGES","same tag",AMBERT,AMBER),("③ MODULARITY","communities",TINT,TEAL),("④ BRIDGES","المص, المر",REDT,RED)],
 "Build the same-tag network, measure its modularity, and locate the boundary-variant bridges.")
s=slide(prs); audit(s,"The tags define a highly modular, block-diagonal community structure.","Treating boundary variants as a proven design — they are a flagged hypothesis.","A formal test of المص/المر as transition markers — proposed, not yet performed.")
s=slide(prs); takeaway(s,"Reframing a corpus as a graph exposes modular structure and points to the next analysis.","The disjoint letters give the corpus graph its first clean edge type — and a bridge to the 2-D course.")
s=Tt(prs,"Key numbers (graph)")
two(s,[L("MODULAR",18,True,TEAL),L("Tag-defined communities: modularity ≈ 0.62 vs ≈ 0.08 for a random partition.",16.5,True,NAVY)],[L("BRIDGES",18,True,AMBER),L("المص (7) and المر (13) sit at family boundaries — a hypothesis for the next round.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
counts[16]=save(prs,"16_Graph_View_DL.pptx")
# ============================================================ L6 SYNTHESIS
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 17","Synthesis — the validated pointer model",
 "Putting it together: the muqaṭṭaʿāt are a validated POSITIONAL/ORGANIZATIONAL pointer — an index over contiguous sūra-families in both muṣḥaf and revelation order, flagging the long sūras — but not a semantic or frequency code.",
 "A single, robust, all-inclusive latent feature that vindicates the project's meta-thesis.")
s=Tt(prs,"The result in one sentence")
two(s,[L("A POSITIONAL INDEX",18,True,TEAL),L("The disjoint letters tag contiguous families of (long) sūras in book and revelation order. Validated over all 29 with a label-permutation null, omnibus p≈2×10⁻⁵.",16.5,True,NAVY)],
 [L("NOT A CODE",18,True,RED),L("They do not encode a shared theme (p≈0.27), a shared length (p≈0.29), or a letter-frequency miracle (0/29). Positional, not semantic.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
figslide(prs,"The whole study on one axis","L6_01_final_scores.png",
 [L("THREE PASS, THREE FAIL",18,True,NAVY),L("Contiguity (both orders) and the long-sūra flag clear the threshold by a wide margin; theme, length-per-tag, and the frequency code fall below it. The verdict, at a glance.",16.5,True,TEAL)])
figslide(prs,"The validated pointer model","L6_02_pointer_model.png",
 [L("WHAT A TAG DOES",18,True,TEAL),L("One disjoint-letter tag → a contiguous family in the muṣḥaf, a contiguous family in revelation order, all flagged as long sūras. An addressing system, not a description.",16.5,True,NAVY)])
figslide(prs,"The finding in one picture","L6_03_dual_map.png",
 [L("INDEXED ON BOTH AXES",18,True,AMBER),L("Every family is compact in book order (top) and revelation order (bottom) at once. This single image is the course's central claim made visible.",16.5,True,NAVY)])
figslide(prs,"Effect sizes behind the p-values","L6_07_effect_sizes.png",
 [L("NOT JUST SIGNIFICANT — LARGE",18,True,NAVY),L("Observed within-family distances are a fraction of the null mean; muqaṭṭaʿāt median length dwarfs the rest. The effects are big, not merely statistically detectable.",16.5,True,TEAL)])
figslide(prs,"Boundary variants — a live hypothesis","L6_05_boundary_variants.png",
 [L("المص AND المر",18,True,AMBER),L("Mixed tags sit at the seams: المص (7) between the ALM and ALR regions; المر (13) inside the الر run. Suggestive of transition-markers — the next round's formal test.",16.5,True,NAVY)])
figslide(prs,"Known to scholarship vs added here","L6_06_known_vs_added.png",
 [L("THE HONEST LEDGER",18,True,TEAL),L("The families themselves are anciently known. What this study adds: rigorous label-permutation validation, the quantified nuzūl-contiguity (the novel part), and the long-sūra flag — over all 29.",16.5,True,NAVY)])
figslide(prs,"The meta-thesis, a third time","L6_04_metathesis.png",
 [L("RELATIONAL, NOT CONTENT",18,True,NAVY),L("Biology (order), signal (refrains), disjoint letters (contiguity): the Qur'an's detectable latent structure lives in arrangement, not in local content statistics. Three independent studies, one lesson.",16.5,True,TEAL)])
figslide(prs,"A reproducible pipeline","L6_08_pipeline.png",
 [L("FROM DATA TO VERDICT",18,True,AMBER),L("Book6.xlsx → root anchor → families → label-permutation null → p-values → read back. Fixed seed, scripted tests; re-running reproduces every number in the course.",16.5,True,NAVY)])
figslide(prs,"Open questions","L6_09_future.png",
 [L("WHERE NEXT",18,True,TEAL),L("Formal tests of the boundary variants; an external Arabic acrostic baseline for the single-letter leads; a cleaner-orthography re-run for ق, ن, ص; and a 2-D corpus-graph view of the families.",16.5,True,NAVY)])
figslide(prs,"The one-line verdict","L6_10_verdict.png",
 [L("THE COURSE, DISTILLED",18,True,NAVY),L("The muqaṭṭaʿāt are a validated positional pointer: an index over contiguous sūra-families in muṣḥaf and revelation order — not a semantic code, not a frequency miracle.",16.5,True,TEAL)])
s=slide(prs); audit(s,"A single robust latent feature: positional/organizational indexing, validated over all 29 (p≈2×10⁻⁵).","Any semantic or numerological reading — refuted or unsupported by the controlled tests.","The deeper 'why' of the letters' specific forms — beyond their tested organizational role — remains open.")
s=slide(prs); takeaway(s,"The strongest claims are the ones that survived every honest attempt to kill them.","The disjoint letters are the project's clearest latent feature — purely relational, exactly as the meta-thesis predicts.")
s=Tt(prs,"Key numbers (synthesis)")
two(s,[L("VALIDATED",18,True,TEAL),L("Contiguity muṣḥaf & nuzūl (p≈2×10⁻⁵, all 29); long-sūra flag (p≈2×10⁻⁵). Robust, all-inclusive.",16.5,True,NAVY)],
 [L("REFUTED / UNSUPPORTED",18,True,RED),L("Shared theme (p≈0.27); shared length per tag (p≈0.29); letter-frequency code (0/29). Positional only.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Read it back — the model in verses")
two(s,[L("THE INDEX AT WORK",18,True,TEAL),L("«حمٓ» (40–46, nuzūl 60–66) and «الٓرٓ» (10–15, nuzūl 51–54) — each tag bundles a contiguous family of long sūras.",16.5,True,NAVY)],
 [L("NOT A MESSAGE",18,True,AMBER),L("«قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ» (50:1): even the lone real letter-signal (ق) marks, it does not narrate.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"What is known vs added")
two(s,[L("KNOWN",18,True,GREY),L("The families themselves (Ḥawāmīm, Alif-Lām-Mīm) are anciently recognized in scholarship.",16.5,True,NAVY)],
 [L("ADDED HERE",18,True,TEAL),L("Rigorous label-permutation validation, the quantified nuzūl-contiguity (novel), and the long-sūra flag — over all 29.",16.5,True,NAVY)],sp=0.5,fa=TINT2,fb=TINT)
s=Tt(prs,"The meta-thesis, restated")
two(s,[L("RELATIONAL, NOT CONTENT",18,True,NAVY),L("Biology (order p<0.003), signal (refrains 8.8×), disjoint letters (contiguity p≈2×10⁻⁵): structure lives in arrangement.",16.5,True,TEAL)],
 [L("WHY IT MATTERS",18,True,AMBER),L("It tells us where to look next: the productive object is the sūra-sequence / corpus graph, not local token statistics.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Letting a strong positional result tempt a semantic story. The data licenses the index — and only the index.",16.5,True,NAVY)],
 [L("THE DISCIPLINE",18,True,TEAL),L("Claim exactly what survived the tests: a validated positional/organizational pointer. Nothing more.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"For discussion & close")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does a purely positional pointer still count as a real latent feature?  • How would you formally test the boundary variants?  • Where should the project look next — and why the corpus graph?",16.5)],
 [L("THE CLOSE",18,True,NAVY),L("The disjoint letters are the project's clearest validated latent feature: an index, not a message — exactly what the meta-thesis predicts.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
counts[17]=save(prs,"17_Synthesis_DL.pptx")
print("DL 17 lectures:",{k:counts[k] for k in sorted(counts)})

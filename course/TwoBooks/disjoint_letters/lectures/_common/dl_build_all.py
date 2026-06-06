# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from dlsig import *
counts={}
FAMS=[("ḤM",[40,41,42,43,44,45,46],TEAL),("ALM",[2,3,29,30,31,32],NAVY),("ALR",[10,11,12,14,15],AMBER),("ṬSM",[26,28],RED)]

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

# ============================================================ L3 CONTIGUITY
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 3","Contiguity — the core result, in both orders",
 "The central finding: same-tag sūras are contiguous — they cluster in the muṣḥaf and in revelation order, beyond what background clustering explains. Every testable family is significant; the omnibus p ≈ 2×10⁻⁵.",
 "All values computed from Book6.xlsx with the label-permutation null of Lecture 2.")
s=Tt(prs,"The claim in one sentence")
two(s,[L("CONTIGUITY",18,True,TEAL),L("If the disjoint letters are an index, same-tag sūras should sit together. They do — and not by the background tendency of muqaṭṭaʿāt sūras to cluster.",16.5,True,NAVY)],
 [L("TWO ORDERS",18,True,AMBER),L("We test both the book order (muṣḥaf) and the revelation order (nuzūl). Passing both is far stronger than passing one.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
figslide(prs,"Observed clustering vs chance — both orders","L3_03_obs_vs_null.png",
 [L("FAR TIGHTER THAN RANDOM",18,True,NAVY),L("In both muṣḥaf and revelation order, the real within-family distance is a fraction of the null mean. The tags pack their sūras far closer together than a random relabeling would.",16.5,True,TEAL)])
figslide(prs,"Per family — book order","L3_01_perfam_mushaf.png",
 [L("EVERY FAMILY CLUSTERS",18,True,TEAL),L("ḤM, ALR, ALM, ṬSM each clear the p=0.05 line in muṣḥaf order. The pointer-as-index is not carried by one spectacular family — it holds across all of them.",16.5,True,NAVY)])
figslide(prs,"Per family — revelation order","L3_02_perfam_nuzul.png",
 [L("AND AGAIN IN TIME",18,True,AMBER),L("The same families also cluster in nuzūl order. ALM: p=0.004; ALR: p=0.0017; ḤM: ~0; ṬSM: p=0.034. Two independent orderings, four families, one consistent verdict.",16.5,True,NAVY)])
figslide(prs,"ḤM: book 40–46 → revelation 60–66","L3_04_hm_map.png",
 [L("CONTIGUOUS ON BOTH AXES",18,True,TEAL),L("The seven Ḥawāmīm are an unbroken block in the book AND seven consecutive slots in revelation order. The clearest single picture of the pointer at work.",16.5,True,NAVY)])
figslide(prs,"ALR: book 10–15 → revelation 51–54","L3_05_alr_map.png",
 [L("THE SAME PATTERN AGAIN",18,True,AMBER),L("Alif-Lām-Rā is tight in both orders too. «الٓرٓ ۚ تِلْكَ ءَايَـٰتُ ٱلْكِتَـٰبِ ٱلْحَكِيمِ» (10:1). Different family, different letters — identical organizational behavior.",16.5,True,NAVY)])
figslide(prs,"ALM: two early + a late run","L3_06_alm_positions.png",
 [L("STRUCTURE, NOT A SINGLE BLOB",18,True,NAVY),L("ALM places 2 and 3 early, then 29–32 as a tight run. A pointer can index more than one neighborhood; what matters is that the members are close, which the null confirms (p=0.009 muṣḥaf).",16.5,True,TEAL)])
figslide(prs,"Both axes at once","L3_07_scatter_2d.png",
 [L("COMPACT IN 2-D",18,True,TEAL),L("Plot each sūra by (book order, revelation order). Each family forms a tight cluster rather than scattering — the index is consistent across both coordinate systems simultaneously.",16.5,True,NAVY)])
figslide(prs,"How far into the tail?","L3_08_gauge.png",
 [L("BEATS ~100% OF RELABELINGS",18,True,NAVY),L("Almost no random reassignment of the same tags clusters as tightly as the real one — in either order. That is what p ≈ 2×10⁻⁵ means in plain terms.",16.5,True,TEAL)])
figslide(prs,"The omnibus picture","L3_10_omnibus.png",
 [L("ALL 29, ONE TEST",18,True,AMBER),L("Pooling every family into one statistic, both observed values land beyond the null mass. This is the project's first robust, all-inclusive latent feature — and it is purely relational.",16.5,True,NAVY)])
figslide(prs,"4 / 4 families significant in both orders","L3_09_all_sig.png",
 [L("NO CHERRY-PICKING",18,True,TEAL),L("We tested every multi-member family, not a favorite. All four pass in both orderings. Singletons can't be tested for internal clustering — we flag them, we don't count them.",16.5,True,NAVY)])
s=slide(prs); audit(s,"Contiguity in muṣḥaf and nuzūl, every family, against a label-permutation null (omnibus p≈2×10⁻⁵).","Any claim that one family alone drives the result — all four are individually significant.","Whether revelation order itself is exact — it is a scholarly reconstruction, so that layer inherits its uncertainty.")
s=slide(prs); takeaway(s,"A result that repeats across two independent orderings and every subgroup is the kind you can build on.","The disjoint letters index contiguous families of sūras in both book and revelation order — the validated core of the course.")
s=Tt(prs,"Key numbers (contiguity)")
two(s,[L("MUṢḤAF",18,True,TEAL),L("Observed within-family Δ = 6.79 sūras vs null mean ≈ 19; label-permutation p ≈ 2×10⁻⁵.",16.5,True,NAVY)],
 [L("REVELATION",18,True,AMBER),L("Observed Δ = 7.30 vs null mean ≈ 19; p ≈ 2×10⁻⁵. All four families significant individually.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the Ḥawāmīm")
two(s,[L("BOOK ORDER",18,True,TEAL),L("«حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ مِنَ ٱللَّهِ ٱلْعَزِيزِ ٱلْعَلِيمِ» (40:1–2). Sūras 40,41,42,43,44,45,46 — an unbroken block.",16.5,True,NAVY)],
 [L("REVELATION ORDER",18,True,AMBER),L("The same seven occupy nuzūl slots 60–66 — seven consecutive. Contiguous on BOTH axes at once.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("'The Ḥawāmīm cluster!' shouted against a random-chapter baseline conflates the tag with background clustering.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("The label-permutation null makes the claim about the SPECIFIC tag, not muqaṭṭaʿāt sūras in general.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Why two orders matter")
two(s,[L("INDEPENDENT EVIDENCE",18,True,NAVY),L("Muṣḥaf order and revelation order are different arrangements. A pattern surviving both is far harder to explain away than one.",16.5,True,TEAL)],
 [L("A CAVEAT",18,True,AMBER),L("Nuzūl order is a scholarly reconstruction, so the revelation-order layer inherits its uncertainty — stated openly.",16.5,True,NAVY)],sp=0.5,fa=TINT2,fb=AMBERT)
s=Tt(prs,"Dual-domain — clustered indices")
two(s,[L("عالم التكوين",18,True,AMBER),L("Functionally related genes often sit in clustered operons/loci — co-located so they are co-regulated.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("Same-tag sūras are co-located in both book and revelation order — a scriptural analogue of clustered loci.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is passing in two orderings stronger than one?  • How would mis-stated nuzūl order affect the result?  • Could a single family drive the omnibus? (No — all four pass.)",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Seek independent confirmations of the same claim before trusting it.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
counts[3]=save(prs,"03_Contiguity_DL.pptx")

# ============================================================ L4 LONG & PHASE
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 4","Long sūras & revelation phase — what else the tag flags",
 "Beyond grouping, the disjoint letters carry two more organizational facts: they flag the LONG sūras (median 85 vs 26 verses, p≈2×10⁻⁵), and they map onto revelation PHASE (simple tags early, families late, المر alone in Medina).",
 "Lengths and nuzūl slots computed directly from Book6.xlsx.")
s=Tt(prs,"A second organizational fact")
two(s,[L("THEY FLAG THE MAJOR SŪRAS",18,True,TEAL),L("Disjoint-letter sūras are not a random size sample — they are the long ones. The tag marks the architectural pillars of the book.",16.5,True,NAVY)],
 [L("STILL POSITIONAL",18,True,AMBER),L("But the tag does not mark a SHARED length per family. It indexes WHERE, not an attribute. We show both facts with the data.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
figslide(prs,"Disjoint-letter sūras are the long ones","L4_01_length_hist.png",
 [L("MEDIAN 85 vs 26",18,True,NAVY),L("The length distributions barely overlap: muqaṭṭaʿāt sūras pile up at high verse counts, the rest at low. The opening letters sit on the book's longest chapters.",16.5,True,TEAL)])
figslide(prs,"Not by chance","L4_02_length_null.png",
 [L("p ≈ 2×10⁻⁵",18,True,TEAL),L("Draw 5,000 random 29-sūra sets; the muqaṭṭaʿāt median length sits far above almost all of them. Flagging the long sūras is a real organizational fact, not an accident of sampling.",16.5,True,NAVY)])
figslide(prs,"The contrast at a glance","L4_03_boxplot.png",
 [L("TWO POPULATIONS",18,True,AMBER),L("Side by side, the boxes hardly touch. Whatever else the disjoint letters do, they reliably co-occur with length — a clean, reproducible marker.",16.5,True,NAVY)])
figslide(prs,"The longest sūras are nearly all tagged","L4_08_top_long.png",
 [L("READ IT BACK",18,True,NAVY),L("List the twelve longest sūras: the teal bars (disjoint-letter) dominate. al-Baqarah (2, الم), Āl ʿImrān (3, الم), al-Aʿrāf (7, المص) — the giants carry openings.",16.5,True,TEAL)])
figslide(prs,"But length is NOT shared per tag","L4_07_length_not_shared.png",
 [L("POSITIONAL, NOT ATTRIBUTE",18,True,RED),L("Within a family, member lengths differ as much as random (label-perm p≈0.29). So the tag says 'I am a long sūra in this neighborhood' — it does not encode a specific length. A pure index.",16.5,True,NAVY)])
figslide(prs,"Revelation phase by tag type","L4_04_phase_by_type.png",
 [L("SIMPLE EARLY, FAMILIES LATE",18,True,TEAL),L("Single/short tags (ق, ن, ص …) cluster early-Meccan; the multi-letter families (ALR, ḤM, ALM) come late-Meccan; the mixed المر stands alone in the Medinan period.",16.5,True,NAVY)])
figslide(prs,"Each family has its own revelation window","L4_05_mean_nuzul.png",
 [L("ORDERED IN TIME",18,True,AMBER),L("Mean nuzūl slot rises ḤM → ALM with each family occupying a distinct stretch of revelation. The index is temporal as well as positional.",16.5,True,NAVY)])
figslide(prs,"Long and late, together","L4_06_len_vs_nuzul.png",
 [L("TWO TRAITS, ONE CORNER",18,True,NAVY),L("Plot length against revelation order: the muqaṭṭaʿāt sūras concentrate in the long, late-Meccan corner. The organizational facts reinforce one another.",16.5,True,TEAL)])
figslide(prs,"Mapped onto revelation phases","L4_09_phase_bands.png",
 [L("THREE BANDS",18,True,TEAL),L("Early-Meccan, late-Meccan, Medinan: the disjoint-letter sūras distribute across the phases in a patterned, not uniform, way — a clean organizational layer over revelation time.",16.5,True,NAVY)])
figslide(prs,"A boundary variant: المر","L4_10_almr_outlier.png",
 [L("A HYPOTHESIS FOR NEXT ROUND",18,True,AMBER),L("المر (sūra 13) sits inside the الر run 10–15 yet is revealed Medinan — a lone outlier. Mixed tags at boundaries may mark transitions; an observation we flag, not yet a tested claim.",16.5,True,NAVY)])
s=slide(prs); audit(s,"Disjoint letters flag the long sūras (p≈2×10⁻⁵) and order onto revelation phase.","Any claim that the tag encodes a specific shared length — it does not (p≈0.29).","Whether boundary variants (المص, المر) mark transitions — suggestive, not yet formally tested.")
s=slide(prs); takeaway(s,"A good index marks WHERE and WHEN without duplicating the content — exactly what these tags do.","The disjoint letters flag the major sūras and map onto revelation phase, while staying purely positional.")
s=Tt(prs,"Key numbers (long & phase)")
two(s,[L("LENGTH",18,True,TEAL),L("Muqaṭṭaʿāt sūras: median 85 verses (mean 95); others: median 26 (mean 41). Random-set null p ≈ 2×10⁻⁵.",16.5,True,NAVY)],
 [L("NOT PER-TAG",18,True,AMBER),L("Within-family length difference: label-permutation p ≈ 0.29 — the tag does not encode a shared length.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Read it back — the giants")
two(s,[L("THE LONGEST CARRY TAGS",18,True,TEAL),L("al-Baqarah (2, الٓمٓ, 286 āyāt), Āl ʿImrān (3, الٓمٓ, 200), al-Aʿrāf (7, الٓمٓصٓ, 206), al-Anʿām/an-Nisāʾ neighbors — the architectural pillars open with letters.",16.5,True,NAVY)],
 [L("A STRUCTURAL ROLE",18,True,AMBER),L("Marking the major sūras is itself an organizational act — flagging where the weight of the Book sits.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("'The tag means long sūra.' But members of one family differ widely in length (p≈0.29) — length is not the message.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Separate 'muqaṭṭaʿāt sūras are long' (true, as a group) from 'each tag encodes a length' (false). Positional, not attribute.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Revelation phase, in words")
three(s,[L("EARLY-MECCAN",17,True,AMBER),L("Single/short tags — ق, ن, ص, طه, يس — appear first.",16)],
 [L("LATE-MECCAN",17,True,TEAL),L("The multi-letter families — ALR, ḤM, ALM — come later.",16)],
 [L("MEDINAN",17,True,RED),L("المر (sūra 13) stands alone in the Medinan period.",16)])
s=Tt(prs,"Dual-domain — size & timing markers")
two(s,[L("عالم التكوين",18,True,AMBER),L("Large genes and developmentally-timed loci are flagged by regulatory marks that say where/when, not what.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The disjoint letters flag the long sūras and a revelation phase — where and when, not what.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does 'long as a group' differ from 'a length per tag'?  • What would the المر outlier predict if tested?  • Is phase-ordering surprising given most muqaṭṭaʿāt are Meccan?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Distinguish a group property from a per-label property — they need different tests.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
counts[4]=save(prs,"04_Long_and_Phase_DL.pptx")

# ============================================================ L5 NOT CONTENT
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 5","What it is NOT — the honest negatives",
 "A pointer addresses; it does not describe. We show, with the data, that the disjoint letters do NOT mark a shared theme, a shared length, or a letter-frequency code. The honest negatives are as important as the positive.",
 "Root-profile similarities and enrichment tests computed from Book6.xlsx.")
s=Tt(prs,"The temptation to over-read")
two(s,[L("THE WISH",18,True,RED),L("It is tempting to say 'ḤM sūras are about X' or 'الم encodes a theme'. A satisfying story — but the data must license it.",16.5,True,NAVY)],
 [L("THE TEST",18,True,TEAL),L("Are same-tag sūras more similar in root-profile than a random regrouping of the muqaṭṭaʿāt sūras? That is the honest question.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
figslide(prs,"Within ≈ cross: families are not content-coherent","L5_01_within_cross.png",
 [L("NO THEME PER TAG",18,True,RED),L("For every family, within-family root similarity is about the same as cross-family. If the tag marked a topic, the teal bars would tower over the grey — they don't.",16.5,True,NAVY)])
figslide(prs,"The semantic test fails","L5_02_semantic_null.png",
 [L("p ≈ 0.27",18,True,NAVY),L("Under the label-permutation null, the observed within-family similarity sits right in the middle of the cloud. Same-tag sūras are no more thematically coherent than a random regrouping.",16.5,True,TEAL)])
figslide(prs,"Overall, within ≈ cross","L5_08_overall_within_cross.png",
 [L("MARGINAL, NOT A THEME",18,True,AMBER),L("Pooled: within-family cosine 0.723 vs cross 0.689. A whisker apart — and that whisker is what a random regrouping also produces. Muqaṭṭaʿāt sūras resemble each other only as a general group of long sūras.",16.5,True,NAVY)])
figslide(prs,"The frequency claim: two nulls, two verdicts","L5_03_freq_two_nulls.png",
 [L("WRONG NULL vs RIGHT BASELINE",18,True,RED),L("Within-chapter, the opening letters look 'significant' (p≈0.001). Against the cross-chapter baseline the effect is gone. The same data, an honest comparison — and the discovery disappears.",16.5,True,NAVY)])
figslide(prs,"Per-letter enrichment: only م passes","L5_04_perletter.png",
 [L("AND ONLY BARELY",18,True,TEAL),L("Of 27 letters tested against non-disjoint sūras, only م (mim) clears p=0.05, at a tiny ~1.13× effect; ن and ق are weaker. These are common-letter effects, not a code.",16.5,True,NAVY)])
figslide(prs,"The one honest positive","L5_05_single_rank.png",
 [L("SINGLE-LETTER ق",18,True,TEAL),L("The cleanest test is a single-letter sūra. ق in Sūrat Qāf ranks 111/114 in its own letter; ن in al-Qalam 105/114. A real but modest, borderline-after-correction signal — reported, not inflated.",16.5,True,NAVY)])
figslide(prs,"Aggregate enrichment is not significant","L5_09_fisher.png",
 [L("THE OMNIBUS SAYS NO",18,True,NAVY),L("Combine all sūras' own-opening-letter densities (Fisher χ²=60.6, df=58): squarely within the null. The blanket 'letters are dense in their sūra' claim is generic to Arabic.",16.5,True,TEAL)])
figslide(prs,"Distinctive roots are flavor, not finding","L5_07_distinctive_roots.png",
 [L("ILLUSTRATIVE ONLY",18,True,AMBER),L("Yes, الم sūras feature كتب, برهم, قتل, موت. But these are descriptive color, NOT a validated family-specific theme — the semantic test (p≈0.27) already told us so.",16.5,True,NAVY)])
figslide(prs,"What the tag is — and is not","L5_06_scorecard.png",
 [L("THREE YES, THREE NO",18,True,NAVY),L("Contiguity (muṣḥaf, revelation) and the long-sūra flag pass. Shared theme, shared length, and a letter-frequency code all fail. The pointer is positional/organizational — full stop.",16.5,True,TEAL)])
figslide(prs,"The recurring verdict","L5_10_content_vs_org.png",
 [L("ORGANIZATION SURVIVES",18,True,TEAL),L("Across biology, signal, and now the disjoint letters: content statistics match ordinary language, while organizational structure beats the null. The meta-thesis, confirmed a third time.",16.5,True,NAVY)])
s=slide(prs); audit(s,"Clean negatives: no shared theme (p≈0.27), no shared length (p≈0.29), no frequency code (0/29).","Any thematic reading of a family as a validated finding — it is illustrative only.","The single-letter ق lead — real and intriguing, but borderline after correction; held as a hypothesis.")
s=slide(prs); takeaway(s,"Reporting what FAILS as plainly as what passes is what separates analysis from advocacy.","The disjoint letters do not describe their sūras; they index them. The negatives sharpen the positive.")
s=Tt(prs,"Key numbers (negatives)")
two(s,[L("NO THEME, NO LENGTH",18,True,RED),L("Semantic coherence per tag: label-permutation p ≈ 0.27. Shared length per tag: p ≈ 0.29. Neither holds.",16.5,True,NAVY)],
 [L("NO FREQUENCY CODE",18,True,AMBER),L("Aggregate own-letter enrichment: 0/29 significant; Fisher χ²=60.6/df58 (n.s.). Only م barely passes per-letter.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=AMBERT)
s=Tt(prs,"Read it back — flavor, not finding")
two(s,[L("DISTINCTIVE ROOTS EXIST",18,True,AMBER),L("الٓمٓ sūras feature كتب (write), برهم?, قتل (kill), موت (death); حمٓ leans on دعو, حقق, یوم, حیی.",16.5,True,NAVY)],
 [L("BUT NOT VALIDATED",18,True,RED),L("Within-family root similarity ≈ cross-family (0.723 vs 0.689). These flavors are illustrative, not a tested theme.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=REDT)
s=Tt(prs,"The honest exception")
two(s,[L("SINGLE-LETTER ق",18,True,TEAL),L("In Sūrat Qāf (50), «قٓ ۚ وَٱلْقُرْءَانِ ٱلْمَجِيدِ», the letter ق is the 3rd-densest of all 114 sūras — a real partial signal.",16.5,True,NAVY)],
 [L("HELD AS HYPOTHESIS",18,True,AMBER),L("With several letters tested, ق is borderline after correction; ن (al-Qalam) is weaker. Reported, not inflated.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Cherry-picking one striking root list and calling it the family's 'theme'. Confirmation bias dressed as discovery.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Test similarity against a label-permutation null over ALL families. Here it returns p≈0.27 — no theme.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — address vs content")
two(s,[L("عالم التكوين",18,True,AMBER),L("A genomic address (locus tag) tells you WHERE a gene sits, not what protein it makes.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("A disjoint-letter tag tells you which family a sūra belongs to and where — not its subject.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why are the negatives (no theme, no length, no code) essential to the final claim?  • Why is single-letter ق the cleanest content test?  • What would a non-Qur'anic Arabic baseline add?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Let a method that can say NO tell you what your pattern is NOT — that is what makes the surviving claim credible.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
counts[5]=save(prs,"05_Not_Content_DL.pptx")

# ============================================================ L6 SYNTHESIS
prs=deck()
titleslide(prs,"THE DISJOINT LETTERS · Lecture 6","Synthesis — the validated pointer model",
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
counts[6]=save(prs,"06_Synthesis_DL.pptx")

print("DECK SLIDE COUNTS:",{k:counts[k] for k in sorted(counts)})

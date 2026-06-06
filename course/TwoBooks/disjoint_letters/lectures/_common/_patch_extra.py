# inserts 6 real content slides before each lecture's save() call
f="dl_build_all.py"; s=open(f,encoding="utf-8").read()
EX={
1:'''s=Tt(prs,"Key facts (Lecture 1)")
three(s,[L("29 SŪRAS",17,True,TEAL),L("Exactly 29 sūras open with disjoint letters — 4 multi-member families + 9 singletons.",16)],
 [L("14 LETTERS",17,True,AMBER),L("Only 14 distinct letters ever appear; half the alphabet never opens a sūra.",16)],
 [L("ONE HYPOTHESIS",17,True,NAVY),L("They are pointers — tags that index and group sūras, tested over all 29.",16)])
s=Tt(prs,"Read it back — the openings name the Book")
two(s,[L("THE LETTERS PRECEDE 'THE BOOK'",18,True,TEAL),L("«الٓرٓ ۚ تِلْكَ ءَايَـٰتُ ٱلْكِتَـٰبِ ٱلْحَكِيمِ» (10:1); «الٓمٓصٓ ۝ كِتَـٰبٌ أُنزِلَ إِلَيْكَ» (7:1–2); «حمٓ ۝ تَنزِيلُ ٱلْكِتَـٰبِ» (40:1–2).",16.5,True,NAVY)],
 [L("CONSISTENT WITH HEADERS",18,True,AMBER),L("The letters repeatedly sit just before a reference to the scripture itself — the behavior of markers, not of content.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"A common pitfall")
two(s,[L("THE PITFALL",18,True,RED),L("Treating الٓمٓ as an acronym or numeric code to 'crack'. Every such attempt over-fits and none replicates.",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("Ask a falsifiable question — do the tags GROUP sūras? — and test it against the right null.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — indexing everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("Genomes carry indexing motifs (promoters, origins) that mark and group regions without coding for a protein.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("On this reading the disjoint letters are scripture's indexing motifs — markers that organize its architecture.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why is 'what does it organize?' a better question than 'what does it mean?'  • How would you test whether the ḤM block is coincidence?  • What single result would falsify the pointer idea?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Turn an intuition into a falsifiable test with the right null, then read the result back into the actual sūras.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
s=Tt(prs,"Where we go next")
three(s,[L("L2 METHOD",17,True,TEAL),L("The label-permutation null that isolates the tag effect.",16)],
 [L("L3 CONTIGUITY",17,True,AMBER),L("The core result in both muṣḥaf and revelation order.",16)],
 [L("L4–L6",17,True,NAVY),L("Long-sūra flag, the honest negatives, and the pointer model.",16)])
''',
2:'''s=Tt(prs,"Key numbers (method)")
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
s=Tt(prs,"Reproducibility")
three(s,[L("DATA",17,True,TEAL),L("Book6.xlsx; canonical muqaṭṭaʿāt; root anchor. Every figure traces to a rule.",16)],
 [L("CODE",17,True,AMBER),L("Permutation tests scripted; fixed seed; re-run reproduces the p-value.",16)],
 [L("HONESTY",17,True,NAVY),L("Negatives (content, frequency) reported as plainly as positives.",16)])
s=Tt(prs,"For discussion")
two(s,[L("QUESTIONS",18,True,AMBER),L("• Why does a random-chapter baseline mislead here?  • What exactly does freezing positions control for?  • Why report the converged p-value, not the first estimate?",16.5)],
 [L("THE HABIT",18,True,NAVY),L("Pick the null that isolates the claim — then make it work hard to fail.",16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT2)
''',
3:'''s=Tt(prs,"Key numbers (contiguity)")
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
''',
4:'''s=Tt(prs,"Key numbers (long & phase)")
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
''',
5:'''s=Tt(prs,"Key numbers (negatives)")
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
''',
6:'''s=Tt(prs,"Key numbers (synthesis)")
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
'''
}
import re
for n,block in EX.items():
    anchor=f'counts[{n}]=save(prs,'
    i=s.find(anchor)
    assert i!=-1, f"anchor {n} not found"
    s=s[:i]+block+s[i:]
open(f,"w",encoding="utf-8").write(s)
print("patched; figslides:",s.count("figslide(prs"))

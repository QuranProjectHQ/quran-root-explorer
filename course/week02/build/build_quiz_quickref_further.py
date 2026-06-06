# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c","/tmp/wk2common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK

# ============ QUIZ ============
d=new_doc("Week 2 — Quiz (Distribution & Concentration)")
TITLE(d,"Week 2 — Quiz: Distribution & Concentration",
      "14 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise. (Paste into Google Forms.)")
Q=[
("1.  A root's “breadth” is:",["how many times it occurs in total","how many of the 114 surahs it appears in","how many ayahs are in its home surah","its rank by frequency"]),
("2.  Root A appears in 9 surahs, Root B in 77. Compared on breadth, Root B is:",["narrower","broader","equal","cannot tell"]),
("3.  The Gini coefficient of a root's spread runs from 0 to 1, where 1 means:",["perfectly even across surahs","all occurrences pooled in one surah","the root is rare","the root is frequent"]),
("4.  “Top-3 share” of 58% means:",["the root is in 58 surahs","58% of its occurrences fall in its 3 busiest surahs","its Gini is 0.58","it appears 58 times"]),
("5.  Why is a root's raw busiest surah usually a poor “home”?",["surahs are all the same size","the busiest surah is usually just the longest one (e.g. al-Baqara)","raw counts are random","the app is biased"]),
("6.  Dividing a root's hits by the surah's AYAH count is still not size-true because:",["ayahs are all equal length","ayahs vary in length, so a per-ayah rate is still confounded","the app forbids it","ayahs have no roots"]),
("7.  The size-true denominator for within-surah density is:",["the number of ayahs in the surah","the surah's total ROOT-TOKENS","114 surahs","6,236 ayahs"]),
("8.  A root occurs 9 times in Ibrahim (568 root-tokens). Its prevalence per 1,000 root-tokens is about:",["1.6","9","15.8","56.8"]),
("9.  Of the 50 most frequent roots, al-Baqara is the raw busiest surah for 30 — after size-true normalization that number becomes:",["30","15","5","0"]),
("10.  The support floor (count ≥ 3 and surah ≥ 30 root-tokens) exists to:",["speed up the app","stop a tiny surah from faking a sky-high density","rank surahs by length","remove function words"]),
("11.  ʿusr (عسر) is reported as having “no reliable home surah” because:",["it never occurs","every surah it appears in fails the support floor","it is only in al-Baqara","it has no root"]),
("12.  For ṣabr (صبر): raw busiest = al-Baqara, per-ayah leader = al-Kahf, per-root-tokens home = at-Tur. The size-true home is:",["al-Baqara","al-Kahf","at-Tur","all three"]),
("13.  On a Lorenz curve, a line that bows farther from the diagonal means the root is:",["more evenly spread","more concentrated","more frequent","broader"]),
("14.  A root spread across 77 surahs (low Gini) tells you it is a pervasive theme. It does NOT tell you:",["that it is broad","that it is important or central","its breadth","its concentration"]),
]
import string
for stem,opts in Q:
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts):
        P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
d.save(os.path.join(WK,"Week2_Quiz.docx")); print("quiz saved")

# ============ QUIZ ANSWER KEY ============
d=new_doc("Week 2 — Quiz Answer Key (instructor)")
TITLE(d,"Week 2 — Quiz Answer Key (instructor)","One point each, 14 total. Values reproducible from Book6.")
H(d,"Answers")
ans=[("1","B","breadth = number of distinct surahs containing the root."),
("2","B","77 surahs > 9 surahs → broader."),
("3","B","Gini 1 = all occurrences in a single surah (maximal concentration)."),
("4","B","top-3 share = % of occurrences in the 3 busiest surahs."),
("5","B","the raw busiest surah is usually just the longest (al-Baqara, 286 ayahs)."),
("6","B","ayahs vary in length, so per-ayah density is still confounded by size."),
("7","B","size-true density divides by the surah's total ROOT-TOKENS."),
("8","C","9 ÷ 568 × 1,000 = 15.8 per 1,000 root-tokens."),
("9","D","0 — normalizing for size dethrones al-Baqara entirely (30/50 → 0/50)."),
("10","B","the floor stops a tiny surah from faking a high density off 1–2 tokens."),
("11","B","every surah ʿusr appears in fails the floor → insufficient support."),
("12","C","at-Tur — only the per-root-tokens answer is size-true."),
("13","B","a deeper bow = more unequal spread = more concentrated."),
("14","B","spread/breadth is not importance; distribution does not rank centrality."),
]
for n,a,ex in ans: P(d,[(f"{n}.  {a}  ",True),("— "+ex,False)],size=10,after=2)
H(d,"Grading")
bullet(d,"Best 8 of 10 weekly quizzes count toward the 20% quiz component.")
bullet(d,"Q8/Q9/Q12 are the size-true-normalization checks — they confirm the student grasped per-root-tokens, not per-ayah or raw.")
d.save(os.path.join(WK,"Week2_Quiz_Answer_Key.docx")); print("quiz key saved")

# ============ QUICK REFERENCE ============
d=new_doc("Week 2 — Quick Reference (1 page)")
TITLE(d,"Week 2 — Quick Reference (1 page)","Distribution & concentration at a glance. Keep this beside the app.")
H(d,"The app in 4 steps",size=13)
bullet(d,"Analyze your root → open the Per-Root Profile / distribution view.")
bullet(d,"Read: breadth (# of 114 surahs), the per-surah chart, top-3 share, Gini.")
bullet(d,"Find the home surah — but size-true (per root-tokens), not raw, not per-ayah.")
bullet(d,"Screenshot the distribution chart + write one fact + one interpretation.")
H(d,"The measures",size=13)
bullet(d,[("Breadth",True),(" = number of the 114 surahs the root appears in (reach).",False)])
bullet(d,[("Concentration",True),(" = top-3 share (intuitive) and Gini 0→1 (0 even, 1 all in one surah).",False)])
bullet(d,[("Size-true home",True),(" = max of (root-tokens in surah ÷ surah's total root-tokens × 1,000).",False)])
bullet(d,[("Support floor",True),(" = count ≥ 3 AND surah ≥ 30 root-tokens, else “insufficient support.”",False)])
H(d,"Read honestly",size=13)
bullet(d,"DO normalize density by ROOT-TOKENS — never by ayah-count, never raw.")
bullet(d,"DON'T call the raw busiest surah the home (it's usually just the longest).")
bullet(d,"DON'T trust a home that fails the support floor.")
H(d,"Why per-ayah is not enough",size=13)
P(d,"Ayahs vary in length, so hits ÷ ayahs is still confounded. ṣabr: raw → al-Baqara, per-ayah → al-Kahf, per-roots → at-Tur. Only per-roots is size-true.",size=10)
H(d,"Anchor numbers (example: ظلم)",size=13)
bullet(d,"breadth 59 surahs · top-3 share 21.7% · Gini 0.74 · size-true home Ibrahim 15.8 / 1k root-tokens (raw busiest al-Baqara, by length only).")
H(d,"What's next (preview)",size=13)
P(d,"Distribution says WHERE a root lives; Week 3 asks WHO WITH — its partners and morphological forms.",size=10)
d.save(os.path.join(WK,"Week2_Quick_Reference.docx")); print("quick ref saved")

# ============ FURTHER STUDY ============
d=new_doc("Week 2 — Further Study & Research")
TITLE(d,"Week 2 — Further Study & Research","Optional extensions for the curious. Stay data-driven: normalize, then claim.")
H(d,"Extend the method",size=13)
bullet(d,"Take five roots and compare their per-AYAH home vs per-ROOT-TOKENS home — for how many do they disagree, and why?")
bullet(d,"Rank a set of roots by breadth, then by Gini — which roots are broad-but-even vs narrow-but-pooled?")
bullet(d,"For a rare root, find where the support floor first fails — how little data is too little?")
H(d,"Questions worth investigating",size=13)
bullet(d,"Does a root's size-true home surah match the surah's traditional theme — or surprise you?")
bullet(d,"Why does al-Baqara dominate raw counts for so many roots, and what does that say about reading by raw frequency?")
bullet(d,"Is a highly concentrated root (high Gini) more or less central than a spread one — or is concentration simply not importance?")
H(d,"Individual & social relevance",size=13)
bullet(d,"Track one root that matters to you to its size-true home surah; read that surah and ask why the density peaks there.")
bullet(d,"A community can be read by where its key terms cluster — does concentration vs spread change how a theme is taught?")
H(d,"A caveat to hold lightly",size=13)
P(d,"Revelation order is an external, surah-coarse overlay — interesting to glance at, but it is indicative only and never a core claim in this course.",size=10)
H(d,"Read more",size=13)
bullet(d,"The Gini coefficient and the Lorenz curve (measuring inequality of a distribution).")
bullet(d,"Document-term matrices and per-document term density in corpus linguistics.")
bullet(d,"Why size normalization matters whenever you compare counts across containers of different sizes.")
d.save(os.path.join(WK,"Week2_Further_Study.docx")); print("further study saved")
print("SET 2 DONE")

# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c","/tmp/wk4common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week04"

d=new_doc("Week 4 — Quiz (Co-occurrence)")
TITLE(d,"Week 4 — Quiz: Co-occurrence","14 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise.")
Q=[
("1.  The co-occurrence (joint count) of two roots is:",["how often each appears alone","the number of ayahs containing BOTH roots","their combined frequency","the longer root's frequency"]),
("2.  Prayer (صلو) shares 52 ayahs with قوم but only 28 with زكو. On the RAW count, the “closest” companion is:",["زكو","قوم","they tie","neither"]),
("3.  Why is the raw shared-ayah count a poor measure of a bond?",["it is too small","a very frequent root shares ayahs with almost everything","it ignores surahs","it is random"]),
("4.  The expected overlap of two roots by chance is computed as:",["freq(A) + freq(B)","freq(A) × freq(B) ÷ 6,236","freq(A) ÷ freq(B)","6,236 ÷ freq(A)"]),
("5.  ءله (God) shares 44 ayahs with prayer; the expected-by-chance is about 27. The ratio ≈ 1.6 means the bond is:",["very strong","about what chance predicts (weak)","negative","impossible"]),
("6.  زكو shares 28 ayahs with prayer against an expectation under 1 — a ratio of ×34.6. This means:",["a chance overlap","a strong, real bond far above chance","an error","zakat is frequent"]),
("7.  Once you control for frequency, prayer's TRUE closest companion is:",["قوم (establish)","ءله (God)","زكو (zakat)","ءتي (give)"]),
("8.  Why does zakat lose the RAW contest but win the CONTROLLED one?",["it is mis-spelled","it is rare overall, so its few ayahs are almost all with prayer","it is frequent","it is Meccan"]),
("9.  Before trusting a ratio, we require a minimum of how many shared ayahs?",["1","at least 5","100","none"]),
("10.  Co-occurrence is symmetric: it tells you two roots travel together but NOT:",["how often","which one leads the other","where they appear","their forms"]),
("11.  Our Week-4 control divides out frequency but still ignores:",["the alphabet","ayah length (longer ayahs co-occur more)","the surah name","the root"]),
("12.  كيل (measure) and وزن (weight) share only 6 ayahs but at ×137 over chance. This bond is:",["weak / accidental","strong and specific (honest scales)","a frequent-root artefact","unmeasurable"]),
("13.  Two roots can co-occur a lot because the text praises them together OR because it:",["never mentions them","contrasts them (association ≠ agreement)","is too short","repeats itself"]),
("14.  To find a target's true companion, you should rank candidates by:",["raw shared count","× over chance (controlled)","alphabetical order","frequency"]),
]
for stem,opts in Q:
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
d.save(os.path.join(WK,"Week4_Quiz.docx")); print("quiz saved")

d=new_doc("Week 4 — Quiz Answer Key (instructor)")
TITLE(d,"Week 4 — Quiz Answer Key (instructor)","One point each, 14 total. Values reproducible from Book6.")
ans=[("1","B","joint count = ayahs containing both roots."),("2","B","قوم has the highest raw joint (52)."),
("3","B","a frequent root shares ayahs with nearly everything — the frequency confound."),
("4","B","expected = freq(A)·freq(B)/6,236 (independence)."),("5","B","ratio ≈ 1.6 ≈ chance → a weak/ないbond."),
("6","B","×34.6 over chance → a strong, real bond."),("7","C","زكو (zakat) — controlled winner."),
("8","B","zakat is rare overall, so its few ayahs concentrate with prayer."),
("9","B","require joint ≥ 5 (small-sample caution)."),("10","B","symmetric — no direction (that is Week 6)."),
("11","B","it ignores ayah length (Week 5's length-aware null fixes this)."),
("12","B","strong, specific — the honest-scales warning (المطففين)."),
("13","B","association ≠ agreement — antonyms co-occur too."),("14","B","rank by × over chance, not raw count."),
]
H(d,"Answers")
for n,a,ex in ans: P(d,[(f"{n}.  {a}  ",True),("— "+ex,False)],size=10,after=2)
H(d,"Grading")
bullet(d,"Best 8 of 10 weekly quizzes count toward the 20% quiz component.")
bullet(d,"Q5/Q6/Q7/Q8 are the anchors (observed-vs-expected and the flip).")
d.save(os.path.join(WK,"Week4_Quiz_Answer_Key.docx")); print("quiz key saved")

d=new_doc("Week 4 — Quick Reference (1 page)")
TITLE(d,"Week 4 — Quick Reference (1 page)","Co-occurrence at a glance. Rank by surprise, not by size.")
H(d,"The measure",size=13)
bullet(d,[("Joint count",True),(" = ayahs containing BOTH roots.",False)])
bullet(d,[("Expected (chance)",True),(" = freq(A) × freq(B) ÷ 6,236.",False)])
bullet(d,[("Ratio",True),(" = observed ÷ expected = “× more than chance.” Report only if joint ≥ 5.",False)])
H(d,"Why raw counts mislead",size=13)
bullet(d,"A very frequent root (God, say, establish) shares ayahs with almost everything — fame, not friendship.")
bullet(d,"The celebrity is in every photo; the rare guest in half your photos is the real friend.")
H(d,"The find-task",size=13)
bullet(d,"Rank candidates by × over chance; read the top; the raw list is a decoy.")
H(d,"Anchor (worked target صلو)",size=13)
bullet(d,"raw winner قوم (52) → controlled winner زكو (×34.6): half of all zakat ayahs sit with prayer.")
H(d,"Limits (what it can't say yet)",size=13)
bullet(d,"Our control ignores ayah length (Week 5: length-aware null + tiers).")
bullet(d,"Co-occurrence is symmetric — no direction (Week 6).  Association ≠ cause or agreement.")
H(d,"Two-sentence reading",size=13)
bullet(d,"Sentence 1 = fact (a controlled ratio). Sentence 2 = labeled interpretation.")
d.save(os.path.join(WK,"Week4_Quick_Reference.docx")); print("quick ref saved")

d=new_doc("Week 4 — Further Study & Research")
TITLE(d,"Week 4 — Further Study & Research","Optional extensions. Control, then claim.")
H(d,"Extend the method",size=13)
bullet(d,"Take a target and rank its candidates both ways — how often does the controlled winner differ from the raw winner?")
bullet(d,"Find a pair with a huge ratio but tiny support (e.g. joint = 5) — why is the support floor important?")
bullet(d,"Pick a theme (the marketplace, the afterlife) and map its internal bonds by × over chance.")
H(d,"Questions worth investigating",size=13)
bullet(d,"Which famous Qur'anic pairings (prayer–zakat, measure–weight) does the controlled measure recover — and which does it not?")
bullet(d,"When is a high ratio meaningful, and when is it two rare roots that happen to share one passage?")
bullet(d,"Does controlling for ayah length (a preview of Week 5) change any of your answers?")
H(d,"Read more",size=13)
bullet(d,"Pointwise mutual information (PMI) and association measures in corpus linguistics.")
bullet(d,"Observed vs expected counts; the chi-square intuition.")
bullet(d,"Collocation extraction and why frequency must be controlled.")
d.save(os.path.join(WK,"Week4_Further_Study.docx")); print("further study saved")
print("SET 2 DONE")

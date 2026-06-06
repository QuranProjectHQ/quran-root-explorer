# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c","/tmp/wk3common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week03"

# QUIZ
d=new_doc("Week 3 — Quiz (Partners & Forms)")
TITLE(d,"Week 3 — Quiz: Partners & Forms","14 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise.")
Q=[
("1.  In the Arabic root-and-pattern system, the three-consonant root carries the core meaning and the pattern (wazn) carries:",["nothing","the grammatical role (agent, act, etc.)","the surah number","the frequency"]),
("2.  كاتب, مكتوب, and كتاب all come from ك-ت-ب. The pattern is what makes them mean, respectively:",["book, writer, written","writer, written, a book","decree, book, writer","all the same"]),
("3.  ءمن's single most common surface form is آمن, a verb. This means faith is most often named as:",["an abstract noun","an act (something done)","a place","a person"]),
("4.  A “masdar” form (e.g. إيمان) names:",["the doer","the abstract act itself","the object","the place"]),
("5.  An active participle (فاعل pattern, e.g. مؤمن) names:",["the act","the agent / doer","the time","the tool"]),
("6.  Divine Names such as رحيم, سميع, بصير, غفور share which morphological pattern type?",["the verb","the masdar","the intensive adjective (فعيل/فعّال)","the plural"]),
("7.  ءمن branches into faith AND a second sense. Which form carries that second sense, “security”?",["إيمان","مؤمن","أمن","آمن"]),
("8.  كوثر (blessed abundance) and تكاثر (blameworthy rivalry) are both forms of ك-ث-ر. They show one root split by:",["frequency","opposite moral valence","surah length","spelling only"]),
("9.  A root's “partners” are the roots that:",["sound similar","co-occur with it in the same ayah more than chance","share its pattern","are its antonyms only"]),
("10.  The app's partner list is “length-controlled” so that:",["short roots win","very frequent roots don't appear as partners just by chance","only Meccan roots show","the list is alphabetical"]),
("11.  ءمن's strongest specific partner is صلح. This shows faith most often travels with:",["disbelief","righteous works","travel","silence"]),
("12.  ءمن co-occurs heavily with its opposite, كفر. This illustrates that:",["the data is wrong","antonyms can be close partners (opposites are defined together)","كفر means faith","they never appear together"]),
("13.  A partner can be statistically significant yet still not be:",["frequent","meaningful, aligned, or causal","Arabic","a root"]),
("14.  A root with many distinct surface forms (e.g. ءمن, 27) is one that the Qur'an:",["never uses","deploys across many grammatical roles","uses only once","mispells"]),
]
for stem,opts in Q:
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
d.save(os.path.join(WK,"Week3_Quiz.docx")); print("quiz saved")

# QUIZ KEY
d=new_doc("Week 3 — Quiz Answer Key (instructor)")
TITLE(d,"Week 3 — Quiz Answer Key (instructor)","One point each, 14 total. Values reproducible from Book6.")
ans=[("1","B","the pattern carries the grammatical role; the root carries core meaning."),
("2","B","فاعل→writer (agent), مفعول→written (object), فِعال→a book."),
("3","B","the top form آمن is a verb — faith is most often an act."),
("4","B","a masdar names the abstract act itself (إيمان = faith)."),
("5","B","the active participle (فاعل) names the agent/doer (مؤمن = believer)."),
("6","C","رحيم/سميع/بصير/غفور are intensive adjectives (فعيل/فعّال) — the Divine-Name pattern."),
("7","C","أمن carries the “security/safety” sense of the root."),
("8","B","same root ك-ث-ر, opposite moral valence: كوثر praise vs تكاثر blame."),
("9","B","partners co-occur in the same ayah more often than chance."),
("10","B","length/frequency control stops ubiquitous roots from appearing as spurious partners."),
("11","B","صلح (righteous deeds) — faith travels with works (آمنوا وعملوا الصالحات)."),
("12","B","antonyms can be close partners — opposites are defined together."),
("13","B","significance is not meaning, alignment, or cause."),
("14","B","many forms = a root deployed across many grammatical roles."),
]
H(d,"Answers")
for n,a,ex in ans: P(d,[(f"{n}.  {a}  ",True),("— "+ex,False)],size=10,after=2)
H(d,"Grading")
bullet(d,"Best 8 of 10 weekly quizzes count toward the 20% quiz component.")
bullet(d,"Q3/Q6/Q8/Q12 are the conceptual anchors (faith-as-verb, the Divine-Name pattern, valence polysemy, antonyms-as-partners).")
d.save(os.path.join(WK,"Week3_Quiz_Answer_Key.docx")); print("quiz key saved")

# QUICK REFERENCE
d=new_doc("Week 3 — Quick Reference (1 page)")
TITLE(d,"Week 3 — Quick Reference (1 page)","Partners & forms at a glance. The root says WHAT; the pattern says HOW.")
H(d,"Pattern families (read the dominant form)",size=13)
bullet(d,[("Verb",True),(" (آمن، يؤمن، اعبد) — the act / mood (perfect, imperfect, imperative).",False)])
bullet(d,[("Active participle فاعل",True),(" (مؤمن، ظالم، شاهد) — the agent / doer.",False)])
bullet(d,[("Masdar",True),(" (إيمان، شهادة، حكمة) — the abstract act itself.",False)])
bullet(d,[("Intensive فعيل/فعّال",True),(" (رحيم، سميع، بصير، غفور) — an attribute; many Divine Names.",False)])
H(d,"Forms — how to read",size=13)
bullet(d,"List the surface forms and their shares; name the dominant pattern.")
bullet(d,"Watch for polysemy: one root can split by sense (ءمن → faith / security) or even by moral valence (ك-ث-ر → كوثر praise / تكاثر blame).")
H(d,"Partners — how to read",size=13)
bullet(d,"Partners = roots that co-occur in the same ayah more than chance (the app's list is length-controlled).")
bullet(d,"Significant ≠ meaningful. A partner is a lead, not a verdict. Antonyms can be partners (ءمن ↔ كفر).")
H(d,"Two-sentence reading",size=13)
bullet(d,"Sentence 1 = computed fact (a form share or a partner's significance).")
bullet(d,"Sentence 2 = labeled interpretation (“I read this as …”).")
H(d,"Anchor (worked root ءمن)",size=13)
bullet(d,"27 forms · 879 tokens · 61% verb (faith is an act) · top partner صلح (z 14) · antonym partner كفر.")
H(d,"What's next (preview)",size=13)
P(d,"This week: which roots travel together (descriptively). Week 4: which root shares the MOST ayahs, and why raw counts mislead.",size=10)
d.save(os.path.join(WK,"Week3_Quick_Reference.docx")); print("quick ref saved")

# FURTHER STUDY
d=new_doc("Week 3 — Further Study & Research")
TITLE(d,"Week 3 — Further Study & Research","Optional extensions for the curious. Stay data-driven: tally, then claim.")
H(d,"Extend the method",size=13)
bullet(d,"Compare the form distributions of two roots — which is verb-dominant (an act) and which is participle- or attribute-dominant?")
bullet(d,"Map the intensive (فعيل/فعّال) form of ten roots — how many function as Divine Names?")
bullet(d,"Find a root whose forms split by sense or valence (like ءمن or ك-ث-ر) — how does the form disambiguate?")
H(d,"Questions worth investigating",size=13)
bullet(d,"Does a root's dominant pattern (verb vs noun) track how the Qur'an frames the concept — as action or as essence?")
bullet(d,"Which roots are each other's mutual top partner (e.g. رحم↔غفر, سمع↔بصر), and what does that pairing express?")
bullet(d,"When is a significant partner meaningful, and when is it just two common roots sharing space?")
H(d,"Read more",size=13)
bullet(d,"Arabic root-and-pattern (templatic) morphology — the wazn system.")
bullet(d,"Active vs passive participle, masdar, and the intensive (مبالغة) patterns.")
bullet(d,"Collocation and distributional semantics — “a word is known by the company it keeps.”")
d.save(os.path.join(WK,"Week3_Further_Study.docx")); print("further study saved")
print("SET 2 DONE")

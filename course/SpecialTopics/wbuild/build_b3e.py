# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
EQ=json.load(open(SB+"snip_equity.json",encoding="utf-8"))
def gle(key,refs):
    d={e["ref"]:e for e in EQ[key]}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
AT=[("cross","Not a proof","the text's data is computed; the equity verdict is interpretive."),
    ("cross","No raw mixing","forms/senses separated; registers kept apart (course rule).")]

# ============ EQUITY - SOCIAL / SPIRITUAL ============
nzawj=ac('زوج'); nnafs=ac('نفس'); ntaqwa=ac('وقي'); nwomen=ac('نسو'); namanu=ac('ءمن')
fig_groupbar("eqs_parity.png","Parity stated in origin, reward, relation (from the cited verses)",["same origin\n(49:13, 4:1)","same reward\n(33:35, 3:195)","mutual guardians\n(9:71)"],[("",[wk.TEAL,wk.AMBER,wk.NAVY],[1,1,1])],ylabel="parity stated (each = 1)")
fig_groupbar("eqs_3335.png","33:35 - ten virtues, matched for men AND women",["men's virtues listed","women's virtues listed"],[("",[wk.TEAL,wk.AMBER],[10,10])],ylabel="virtues (from 33:35)")
fig_freqbarh("eqs_vocab.png","The vocabulary of shared standing",["soul/self (nafs)","pair/spouse (zawj)","faith (amanu)","piety (taqwa)","women (nisa)"],[nnafs,nzawj,namanu,ntaqwa,nwomen],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY,wk.LT],xlabel="ayat containing the root")
fig_groupbar("eqs_reward.png","'I waste not the work of any worker - male or female' (3:195)",["the reward formula 'male or female'"],[("approx. occurrences",[wk.TEAL],[4])],ylabel="times")
fig_suradist("eqs_nafs_sura.png","Where 'soul/self' (one origin) falls","نفس")
fig_suradist("eqs_zawj_sura.png","Where 'pair/spouse' falls, sura by sura","زوج")
fig_groupbar("eqs_registers.png","Keep registers apart: moral standing vs role",["moral/spiritual parity (stated)","role/legal differentiation (other verses)"],[("",[wk.TEAL,wk.GREY],[1,1])],ylabel="distinct questions")
spec=dict(slug="W09_equity_social",sub="women & men: social/spiritual, Week 9",
 main="Women & men - social & spiritual standing",
 headline="Parity stated in origin, reward and relation - kept apart from role",
 intro1="Are women and men equal in moral and spiritual standing - in origin, reward, and mutual relation? We read the verses on creation, reward, and mutual standing at face value, marking where parity is STATED vs interpreted, and keeping moral standing apart from role/legal differentiation.",
 intro2="Verse content is quoted from Book6; the 'ten matched virtues' and 'male or female' formulas are what the cited verses state.",
 qhead="The claim to test",qbody="Are women and men equal in moral/spiritual standing - in origin, reward, and relation?",
 mhead="The method",mpts=["read the verses on creation, reward, mutual standing at face value",
   "mark where parity is STATED vs interpreted",
   "keep moral standing apart from role/legal differentiation (separate question)"],
 figs=[
  dict(t="Parity stated in three registers",png="eqs_parity.png",cf=TINT,
    cap="In the data (from the cited verses) - parity is stated in origin (49:13, 4:1), reward (33:35, 3:195) and mutual relation (9:71). Three explicit statements."),
  dict(t="33:35 - ten virtues, matched",png="eqs_3335.png",
    cap="In the data (33:35) - the verse pairs TEN virtues for men and women identically, promising the same forgiveness and reward - parity made explicit."),
  dict(t="The vocabulary of shared standing",png="eqs_vocab.png",cf=TINT,
    cap=f"In the data - soul/self ({nnafs}), pair/spouse ({nzawj}), faith ({namanu}) and piety ({ntaqwa}) frame a standing ranked by taqwa, not sex (49:13)."),
  dict(t="'Male or female' - the reward formula",png="eqs_reward.png",
    cap="In the data - 'I will not waste the work of any worker among you, male or female' (3:195) - the reward formula recurs, tying outcome to deeds, not sex."),
  dict(t="'Soul/self' across the corpus",png="eqs_nafs_sura.png",cf=TINT,
    cap="In the data - the 'one soul' origin (4:1) sits in a root spread across the corpus - shared human origin."),
  dict(t="'Pair/spouse' across the corpus",png="eqs_zawj_sura.png",
    cap="In the data - the pair/spouse root names the reciprocal relation - 'created for you mates' - throughout the corpus."),
  dict(t="Two distinct questions",png="eqs_registers.png",cf=TINT,
    cap="In the data - moral/spiritual parity (stated) and role/legal differentiation (other verses) are SEPARATE questions; we do not collapse one into the other."),
 ],
 gal1=dict(title="Same origin; same reward",items=gle("social",["49:13","4:1"]) or [("49:13","خَلَقْنَاكُم مِّن ذَكَرٍ وَأُنثَىٰ","We created you from a male and a female")],fill=TINT,hc=TEAL),
 gal2=dict(title="Same reward; mutual guardianship",items=gle("social",["33:35","3:195","9:71"]) or [("9:71","الْمُؤْمِنُونَ وَالْمُؤْمِنَاتُ بَعْضُهُمْ أَوْلِيَاءُ بَعْضٍ","believing men and women are guardians of one another")],fill=AMBERT,hc=AMBER),
 v1=("Same origin","'created you from a male and a female' (49:13) and 'from one soul' (4:1); rank is by taqwa, not sex."),
 v2=("Same reward","33:35 pairs ten virtues identically; 'I will not waste the work of any worker, male or female' (3:195)."),
 v3=("Mutual guardianship","'the believing men and women are guardians (awliya) of one another' (9:71) - a reciprocal relation, not one-way."),
 deep=("Symmetric in standing",
   "Computed datum: in origin, moral agency and reward the text states parity explicitly and repeatedly - 33:35's ten matched pairs, the 'male or female' reward formula, reciprocal guardianship (9:71). On the face of the text, spiritual and moral standing is symmetric. Role and legal differentiations (other verses) are a distinct question, not this one."),
 deep_extra=["Face-value parity in origin and reward is a strong textual datum; whether social ROLES are 'equal' is contested and separate."],
 crit1=("Roles are a separate question",
   "face-value parity in origin and reward is strong; whether social ROLES are 'equal' is contested and not decided by these verses."),
 crit2=("Keep registers apart",
   "we keep moral standing and role distinct rather than collapse one into the other - they are answered by different verses."),
 audit=[("check","Parity verses cited","origin 49:13/4:1, reward 33:35/3:195, relation 9:71."),
   ("check","33:35 matched","ten virtues paired identically."),
   ("tilde","Roles separate","moral standing != role/legal question.")]+AT,
 method=("parity verses; shared-standing vocabulary","what each verse states; root fields","parity bars, 33:35 bars, vocabulary bars, sura maps"),
 take=("Symmetric in standing",
   ["In origin (49:13, 4:1), reward (33:35, 3:195) and relation (9:71) the text states parity explicitly and repeatedly.",
    "On the face of the text, spiritual and moral standing is symmetric - ranked by taqwa, not sex.",
    "Role/legal differentiation is a separate question; we keep the registers apart. Presented from the text."]),
 qr1=("The verses",f"origin 49:13, 4:1 - reward 33:35 (10 virtues), 3:195 - relation 9:71; vocabulary: soul {nnafs}, pair {nzawj}."),
 qr2=("The shape","moral/spiritual standing is symmetric (origin, reward, relation); role/legal differentiation is a distinct, interpretive question."),
 syn=("Three registers of parity",
   [("Origin","one soul / male and female"),("Reward","'male or female', ten virtues"),("Relation","mutual guardianship")],
   "Symmetric in standing","ranked by taqwa not sex; role is a separate question kept apart."),
 quiz=("Special Topic - Women & Men: Social & Spiritual Standing (Week 9)",[
  ("1.  49:13 grounds human rank in:","taqwa (God-consciousness), not sex",["wealth","lineage","gender"],"'created from a male and a female ... the noblest is the most God-conscious.'"),
  ("2.  33:35 pairs how many virtues for men and women?","ten, identically matched",["none","two","one hundred"],"the same forgiveness and reward promised."),
  ("3.  3:195's reward formula is:","'I waste not the work of any worker, male or female'",["men only","women only","the wealthy only"],"outcome tied to deeds, not sex."),
  ("4.  9:71 describes believing men and women as:","guardians (awliya) of one another",["unrelated","ranked","separate"],"a reciprocal relation."),
  ("5.  4:1 grounds humanity in:","one soul",["two souls","many gods","the dust only"],"shared origin."),
  ("6.  Moral/spiritual parity and role/legal differentiation are:","two distinct questions",["the same question","contradictory","both undecidable"],"answered by different verses."),
  ("7.  The computed datum is:","parity stated in origin, reward, relation",["total role-equality","total inequality","nothing"],"explicit and repeated."),
  ("8.  Whether social ROLES are 'equal' is:","contested and separate from these verses",["settled by 33:35","proven equal","proven unequal"],"a distinct question."),
  ("9.  'Ranked by taqwa, not sex' comes from:","49:13",["4:11","2:282","110:3"],"the nobility criterion."),
  ("10.  The reward formula recurs to tie outcome to:","deeds, not gender",["wealth","lineage","sex"],"'male or female.'"),
  ("11.  We avoid:","collapsing moral standing into role",["citing verses","counting roots","reading 33:35"],"keep registers apart."),
  ("12.  The honest verdict is:","symmetric in moral/spiritual standing",["asymmetric everywhere","identical in all roles","unknowable"],"face-value parity stated."),
  ("13.  These findings are:","the text's data, role-question scoped out",["a ruling on roles","disproof","unrelated to Book6"],"we report and scope."),
 ]),
)
standard_deck(spec)
print("done equity_social")

# ============ EQUITY - INHERITANCE ============
ninh=ac('ورث'); nwomen=ac('نسو')
fig_groupbar("eqi_fixed.png","A fixed right, then case-specific shares (from the cited verses)",["women inherit\n(fixed, 4:7)","2:1 child case\n(4:11)","equal cases\n(4:12)"],[("",[wk.TEAL,wk.AMBER,wk.RED],[1,1,1])],ylabel="established (each = 1)")
fig_groupbar("eqi_ratio.png","The ratio is case-specific, not a blanket 'half'",["son vs daughter (4:11)","uterine siblings (4:12)"],[("share ratio (M:F)",[wk.AMBER,wk.TEAL],[2.0,1.0])],ylabel="male : female share",fmt="{:.1f}")
fig_freqbarh("eqi_verses.png","The inheritance verses (the full schedule)",["4:7 women's right","4:11 children","4:12 spouses/siblings","4:176 kalala"],[1,1,1,1],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY],xlabel="each a distinct configuration")
fig_suradist("eqi_sura.png","Where the inheritance-root falls (sura 4 core)","ورث")
fig_groupbar("eqi_cherry.png","Two opposite cherry-picks",["quote only 4:11 (2:1)","quote only 4:12 (equal)"],[("each is a half-truth",[wk.RED,wk.RED],[1,1])],ylabel="cherry-pick")
fig_groupbar("eqi_maint.png","The interpretive crux: ratio paired with maintenance duty",["male's larger share (4:11)","male's exclusive maintenance duty"],[("the equity debate turns here",[wk.AMBER,wk.TEAL],[1,1])],ylabel="paired in the readings")
fig_freqbarh("eqi_field.png","Inheritance vocabulary",["inheritance-root (warth)","women (nisa)","inheritance . women co-occur"],[ninh,nwomen,cooccur('ورث','نسو')],[wk.TEAL,wk.AMBER,wk.NAVY],xlabel="ayat")
spec=dict(slug="W09_equity_inheritance",sub="women & men: inheritance, Week 9",
 main="Women & men - inheritance",
 headline="A fixed right, with case-specific shares - not a blanket 'half'",
 intro1="'The Qur'an gives women half.' Is the famous 2:1 the whole picture, or one case among several? We read the inheritance verses (4:7, 4:11, 4:12, 4:176) and report the actual shares by heir-CONFIGURATION, separating the fixed datum from the equity verdict.",
 intro2="Verse content is quoted from Book6; the shares are what the cited verses specify - the 2:1 holds in the child case but not universally.",
 qhead="The claim to test",qbody="Is '2:1, women get half' the whole inheritance picture - or one configuration among several?",
 mhead="The method",mpts=["read the inheritance verses; report shares by heir-CONFIGURATION",
   "show where 2:1 holds (4:11) and where shares are equal (4:12)",
   "separate the fixed schedule from the equity verdict"],
 figs=[
  dict(t="A fixed right, then case-specific shares",png="eqi_fixed.png",cf=TINT,
    cap="In the data (from the cited verses) - 4:7 fixes women's right to inherit; 4:11 gives the 2:1 child case; 4:12 has equal cases. A schedule, not a single ratio."),
  dict(t="The ratio is case-specific",png="eqi_ratio.png",
    cap="In the data - in the parents->children case (4:11) a son gets the share of two daughters (2:1); uterine siblings (4:12) inherit EQUALLY (1:1). The ratio varies by configuration."),
  dict(t="The full schedule",png="eqi_verses.png",cf=TINT,
    cap="In the data - four verses (4:7, 4:11, 4:12, 4:176) specify shares for distinct configurations - the honest datum is the FULL schedule, not one verse."),
  dict(t="The inheritance-root across the corpus",png="eqi_sura.png",
    cap="In the data - the inheritance-root concentrates in sura 4 (an-Nisa) - the legislative core."),
  dict(t="Two opposite cherry-picks",png="eqi_cherry.png",cf=TINT,
    cap="In the data - quoting only 4:11's 2:1 is a cherry-pick; quoting only the equal cases (4:12) is the opposite cherry-pick. Both distort the schedule."),
  dict(t="The interpretive crux",png="eqi_maint.png",
    cap="In the data - the equity debate turns on pairing the male's larger share (4:11) with his exclusive maintenance duty: net-parity readings vs unequal readings. The numbers alone do not decide."),
  dict(t="Inheritance vocabulary",png="eqi_field.png",cf=TINT,
    cap=f"In the data - the inheritance-root ({ninh}) and 'women' ({nwomen}) co-occur ({cooccur('ورث','نسو')}); 4:7 fixes the right where custom once bypassed women."),
 ],
 gal1=dict(title="Women inherit - fixed (4:7); the 2:1 child case (4:11)",items=gle("inherit",["4:7","4:11"]) or [("4:11","لِلذَّكَرِ مِثْلُ حَظِّ الْأُنثَيَيْنِ","for the male, the like of the share of two females")],fill=TINT,hc=TEAL),
 gal2=dict(title="Not always 2:1 - equal cases (4:12, 4:176)",items=gle("inherit",["4:12","4:176"]) or [("4:12","فَهُمْ شُرَكَاءُ فِي الثُّلُثِ","they share equally in a third")],fill=AMBERT,hc=AMBER),
 v1=("Women inherit - a fixed right (4:7)","where custom once bypassed them, 4:7 guarantees women a defined share of parents' and kin's estate - enforceable."),
 v2=("The 2:1 case (4:11)","in the parents->children case, a son receives the share of two daughters; this specific configuration is the one most quoted."),
 v3=("Not always 2:1 (4:12)","shares vary by configuration: uterine siblings inherit equally; some parent and spouse shares match - case-specific, not a blanket 'half.'"),
 deep=("A fixed schedule, an interpreted equity",
   "Computed datum: the corpus FIXES women's inheritance as an enforceable right (4:7) and specifies shares that vary by heir - the well-known 2:1 holds in the child case (4:11) but not universally (uterine siblings equal, 4:12). Whether the scheme is 'equitable' is the interpretive crux: readings that pair the male's larger share with his exclusive maintenance duty argue net-parity; others read it as unequal. The numbers alone do not decide."),
 deep_extra=["Quoting only 4:11's 2:1 is a cherry-pick; quoting only the equal cases is the opposite cherry-pick."],
 crit1=("Both cherry-picks distort",
   "quoting only 2:1 (4:11) or only the equal cases (4:12) misrepresents a schedule that varies by configuration."),
 crit2=("The verdict turns on the frame",
   "the honest datum is the FULL schedule plus the maintenance asymmetry; the equity verdict turns on the interpretive frame, not the count."),
 audit=[("check","Right fixed","4:7 guarantees women's inheritance."),
   ("check","Schedule varies","2:1 in the child case (4:11), equal in others (4:12)."),
   ("tilde","'Equitable?' is interpretive","turns on the maintenance pairing, not the count.")]+AT,
 method=("inheritance verses; share configurations","shares by heir-configuration; the full schedule","schedule bars, ratio bars, sura map"),
 take=("A fixed schedule, an interpreted equity",
   ["The corpus fixes women's inheritance as an enforceable right (4:7) and specifies shares that VARY by configuration.",
    "The famous 2:1 holds in the child case (4:11) but not universally (uterine siblings equal, 4:12).",
    "Whether the scheme is 'equitable' turns on the interpretive frame (maintenance asymmetry), not the count. Presented from the text."]),
 qr1=("The verses",f"4:7 fixed right - 4:11 2:1 child case - 4:12 equal cases - 4:176 kalala; inheritance-root {ninh} ayat."),
 qr2=("The shape","a fixed right with case-specific shares (2:1 not universal); the equity verdict turns on the interpretive frame, not the count."),
 syn=("Right fixed, ratio varies",
   [("4:7","women's inheritance fixed"),("4:11","2:1 in the child case"),("4:12","equal in other cases")],
   "A schedule, not a slogan","'women get half' is one configuration; the equity verdict turns on the frame, not the count."),
 quiz=("Special Topic - Women & Men: Inheritance (Week 9)",[
  ("1.  4:7 establishes that women:","have a fixed right to inherit",["inherit nothing","inherit only from mothers","inherit half always"],"a defined, enforceable share."),
  ("2.  The famous 2:1 ratio is from:","4:11 (the parents->children case)",["4:7","4:12","2:282"],"a son gets the share of two daughters."),
  ("3.  4:12 (uterine siblings) gives shares that are:","equal (1:1)",["2:1","3:1","zero"],"not always 2:1."),
  ("4.  The honest datum is:","the FULL schedule, not one verse",["only 4:11","only 4:12","none"],"shares vary by configuration."),
  ("5.  Quoting only 4:11's 2:1 is:","a cherry-pick",["the whole truth","fair","impossible"],"it ignores the equal cases."),
  ("6.  Quoting only the equal cases is:","the opposite cherry-pick",["the whole truth","fair","required"],"it ignores 4:11."),
  ("7.  The equity verdict turns on:","pairing the share with the maintenance duty (the frame)",["the count alone","4:7 alone","rhyme"],"net-parity vs unequal readings."),
  ("8.  The 2:1 ratio is:","case-specific, not a blanket 'half'",["universal","never true","forbidden"],"it holds in the child case only."),
  ("9.  The inheritance verses cluster in:","sura 4 (an-Nisa)",["sura 108","sura 1","the disjoint letters"],"the legislative core."),
  ("10.  Whether the scheme is 'equitable' is:","interpretive, not settled by the numbers",["settled by 4:11","proven equal","proven unequal"],"it turns on the frame."),
  ("11.  4:7's significance is that it:","fixes the right where custom once bypassed women",["abolishes inheritance","gives women everything","is symbolic"],"an enforceable guarantee."),
  ("12.  The honest verdict is:","a fixed schedule, an interpreted equity",["women get half, full stop","total equality","no rights"],"datum vs frame-dependent verdict."),
  ("13.  These findings are:","the text's schedule, with the equity-verdict scoped",["a ruling","disproof","unrelated to Book6"],"we report the schedule and scope the verdict."),
 ]),
)
standard_deck(spec)
print("done equity_inheritance")

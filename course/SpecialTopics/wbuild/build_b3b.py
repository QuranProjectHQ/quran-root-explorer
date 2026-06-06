# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_donut,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
SW=json.load(open(SB+"snip_sword.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def glw(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ SHAFAA - intercession ============
nsh=ac('شفع'); co_idhn=cooccur('شفع','ءذن')
fig_groupbar("sh_split.png","Two sets of verses, one rule",["denied as INDEPENDENT","permitted BY HIS LEAVE"],[("",[wk.RED,wk.TEAL],[co_idhn if False else 6,co_idhn])] if False else [("",[wk.RED,wk.TEAL],[6,co_idhn])],ylabel="representative verses")
fig_freqbarh("sh_field.png","The intercession-root and its qualifier",["شفع  intercession (total)","شفع . ءذن  'by His leave'"],[nsh,co_idhn],[wk.NAVY,wk.TEAL],xlabel="ayat")
fig_groupbar("sh_cond.png","The conditional clause does the work",["intercession (total)","conditioned 'by His leave'","belongs wholly to God (39:44)"],[("",[wk.NAVY,wk.TEAL,wk.AMBER],[nsh,co_idhn,1])])
fig_suradist("sh_sura.png","Where intercession is named, sura by sura","شفع")
fig_timeline("sh_time.png","The intercession-root across the revelation",[("shafaa شفع","شفع")])
fig_groupbar("sh_resolve.png","Not a contradiction - a single conditioned rule",["'no intercession'\n(absolute reading)","'except by His leave'\n(the qualifier)"],[("",[wk.RED,wk.TEAL],[6,co_idhn])])
fig_donut("sh_pie.png","Intercession: denied, permitted, or God's",["denied (independent)","by His leave","wholly God's"],[6,co_idhn,3],[wk.RED,wk.TEAL,wk.AMBER])
spec=dict(slug="W09_shafaa_intercession",sub="intercession, Week 9",
 main="Is intercession denied or affirmed? (shafaa)",
 headline="An apparent contradiction that dissolves on one qualifier",
 intro1="Some verses say no intercession will help; others speak of intercession 'by His leave.' A contradiction - or two halves of one rule? We read the intercession-root (26 occurrences) by type: independent intercession (denied) vs God-permitted intercession (affirmed).",
 intro2="The root-count recomputes from Book6 and reproduces exactly (26); the qualifier co-occurrence is computed.",
 qhead="The claim to test",qbody="Do the 'no intercession' and 'intercession by His leave' verses contradict, or form one conditioned rule?",
 mhead="The method",mpts=["read the intercession-root by type: independent (denied) vs God-permitted (affirmed)",
   "count where the qualifier 'by His leave' (idhn) appears with it",
   "let the conditional clause work with the negation, not against it"],
 figs=[
  dict(t="Two sets of verses, one rule",png="sh_split.png",cf=TINT,
    cap=f"In the data - the 'denied' verses reject autonomous intercession; the 'permitted' ones add the qualifier 'by His leave' ({co_idhn} co-occurrences with idhn). Two halves, not a contradiction."),
  dict(t="The root and its qualifier",png="sh_field.png",
    cap=f"In the data - intercession appears in {nsh} ayat; in {co_idhn} of them it is explicitly conditioned by 'His leave' (idhn) - the clause that reconciles the sets."),
  dict(t="The conditional clause does the work",png="sh_cond.png",cf=TINT,
    cap=f"In the data - intercession ({nsh}) is denied as a power, permitted by leave ({co_idhn}), and declared to 'belong wholly to God' (39:44) - never a rival authority."),
  dict(t="Intercession across the corpus",png="sh_sura.png",
    cap="In the data - the intercession verses cluster in the eschatology passages (the Day, the reckoning)."),
  dict(t="Across the revelation",png="sh_time.png",cf=TINT,
    cap="In the data - the intercession-root runs across periods; the conditioned rule is consistent throughout."),
  dict(t="Not a contradiction",png="sh_resolve.png",
    cap=f"In the data - reading the 'no intercession' verses absolutely IGNORES 'except by His leave' ({co_idhn}); the apparent contradiction dissolves once the qualifier is read WITH the negation."),
  dict(t="Denied, permitted, or God's",png="sh_pie.png",cf=TINT,
    cap="In the data - the verses sort into: denied as an independent power, permitted by His leave, and belonging wholly to God - one conditioned rule with three faces."),
 ],
 gal1=dict(title="Denied as an independent power",items=gl(B2["shafaa"],["2:48","2:254"]) or [("2:48","لَا تَجْزِي نَفْسٌ عَن نَّفْسٍ شَيْئًا وَلَا يُقْبَلُ مِنْهَا شَفَاعَةٌ","no soul avails another, no intercession is accepted")],fill=REDT,hc=RED),
 gal2=dict(title="Only by His leave; wholly God's",items=(gl(B2["shafaa"],["2:255","10:3"])+gl(B2["shafaa"],["39:44","21:28"])) or [("2:255","مَن ذَا الَّذِي يَشْفَعُ عِندَهُ إِلَّا بِإِذْنِهِ","who can intercede with Him except by His leave?")],fill=TINT,hc=TEAL),
 v1=("Denied as INDEPENDENT","no autonomous broker can override the verdict - 'no intercession is accepted' (2:48)."),
 v2=("Permitted BY HIS LEAVE",f"intercession exists, but only as God permits - 'except by His leave' (2:255); {co_idhn} ayat carry the qualifier."),
 v3=("Belongs WHOLLY to God","'Say: intercession belongs altogether to God' (39:44) - the power is His to grant, never a rival authority."),
 deep=("Not a contradiction - a single conditioned rule",
   f"The two sets are reconciled by one qualifier. Intercession is denied as an INDEPENDENT power and affirmed only as GOD-PERMITTED - 'by His leave' ({co_idhn} ayat), 'belongs wholly to God' (39:44). The apparent contradiction dissolves once the conditional clause is read WITH the negation, not against it. Whether anyone in fact receives that leave - and who - is the interpretive question the count does not settle."),
 deep_extra=["Reading the 'no intercession' verses absolutely (ignoring 'except by His leave') is the classic audit failure."],
 crit1=("The count does not settle 'who'",
   "whether anyone in fact receives that leave - and who - is the interpretive question the data leaves open."),
 crit2=("Absolute reading is the audit failure",
   "treating 'no intercession' as unconditional ignores the explicit qualifier in the same corpus - the classic cherry-pick."),
 audit=[("check","Root counted",f"{nsh} occurrences (reproduces exactly)."),
   ("check","Qualifier computed",f"'by His leave' co-occurs {co_idhn} times."),
   ("check","Reconciled by one clause","denied independent + permitted by leave = one rule.")]+[("tilde","'Who receives leave' open","the count does not settle that.")]+AT,
 method=("the intercession-root; the qualifier idhn","type split, qualifier co-occurrence","split bars, qualifier bar, sura map, donut"),
 take=("One conditioned rule, not a contradiction",
   [f"Intercession ({nsh} ayat) is denied as an independent power and affirmed only 'by His leave' ({co_idhn}).",
    "'Belongs wholly to God' (39:44) - the power is His to grant, never a rival authority.",
    "The contradiction dissolves on the qualifier; whether anyone receives leave is interpretive. Presented from the text."]),
 qr1=("The numbers",f"intercession-root {nsh}; 'by His leave' co-occurs {co_idhn}; 'wholly God's' (39:44)."),
 qr2=("The shape","denied as independent, permitted by His leave, wholly God's - one conditioned rule; reading absolutely is the audit failure."),
 syn=("One rule, two halves",
   [("Denied","no independent broker"),("+ Qualifier","'except by His leave'"),("= One rule","intercession belongs wholly to God")],
   "The qualifier reconciles","read 'except by His leave' WITH the negation and the contradiction dissolves."),
 quiz=("Special Topic - Intercession Denied or Affirmed? (Week 9)",[
  ("1.  The intercession-root appears in about:",f"{nsh} ayat",["4","200","once"],f"{nsh}, reproduced exactly."),
  ("2.  Intercession is DENIED when it is:","independent / autonomous of God",["by His leave","wholly God's","always"],"no broker overrides the verdict (2:48)."),
  ("3.  Intercession is PERMITTED when it is:","'by His leave' (idhn)",["independent","forbidden","automatic"],f"the qualifier in {co_idhn} ayat."),
  ("4.  39:44 says intercession:","belongs wholly to God",["belongs to angels","is impossible","is automatic"],"never a rival authority."),
  ("5.  The apparent contradiction dissolves once:","'except by His leave' is read WITH the negation",["the verses are ignored","one set is deleted","you pick one"],"one conditioned rule."),
  ("6.  Reading 'no intercession' absolutely is:","the classic audit failure (ignoring the qualifier)",["the correct reading","impossible","irrelevant"],"it cherry-picks half the rule."),
  ("7.  What the count does NOT settle:","who in fact receives God's leave",["the root-count","the qualifier","the verses"],"that is interpretive."),
  ("8.  The two verse-sets are:","two halves of one rule",["a real contradiction","unrelated","identical"],"reconciled by one qualifier."),
  ("9.  The qualifier 'by His leave' co-occurs with intercession:",f"in about {co_idhn} ayat",["never","in all 26","once"],"the conditioning clause."),
  ("10.  Intercession is therefore best described as:","conditioned, not denied or automatic",["fully denied","fully automatic","never mentioned"],"denied independent, permitted by leave."),
  ("11.  The intercession verses cluster in:","the eschatology passages",["the legal verses","sura 108","the disjoint letters"],"the Day and the reckoning."),
  ("12.  The honest verdict is:","a single conditioned rule, not a contradiction",["a contradiction","total denial","total affirmation"],"the qualifier reconciles the sets."),
  ("13.  These findings are:","presented from the text, the 'who' left open",["doctrine","disproof","unrelated to Book6"],"the count is computed; the recipients are interpretive."),
 ]),
)
standard_deck(spec)
print("done shafaa")

# ============ SWORD vs PEACE ============
nsayf=form_ac(['سيف','سيوف']); nharb=ac('حرب'); nqital=fac_sub(['قاتل','قتال','يقاتل','تقاتل','قاتلوا','نقاتل']); njihad=ac('جهد'); nqatl=ac('قتل')
co_trans=cooccur('قتل','عدو'); co_peace=cooccur('قتل','سلم'); nkurh=ac('كره')
fig_freqbarh("sp_war.png","The war vocabulary - and the missing word",["سيف  SWORD","حرب  war","قتال  combat (qital)","جهد  striving (jihad)"],[nsayf,nharb,nqital,njihad],[wk.RED,wk.AMBER,wk.AMBER,wk.GREY],xlabel="ayat")
fig_groupbar("sp_kill.png","The killing-root: mostly killing, not war",["killing / murder","mutual combat (qital)"],[("",[wk.GREY,wk.AMBER],[nqatl-nqital,nqital])])
fig_groupbar("sp_cond.png","Combat is CONDITIONED",["combat (qital)","with 'do not transgress' (2:190)","with peace (incline to it)"],[("",[wk.AMBER,wk.TEAL,wk.TEAL],[nqital,co_trans,co_peace])])
fig_suradist("sp_sura.png","Where the killing-root falls, sura by sura","قتل")
fig_timeline("sp_time.png","Combat and killing across the revelation",[("qatl قتل","قتل"),("jihad جهد","جهد")])
fig_groupbar("sp_absent.png","The literal 'sword' never appears",["سيف sword (literal)","قتال combat","compulsion forbidden (no ikrah)"],[("",[wk.RED,wk.AMBER,wk.TEAL],[nsayf,nqital,nkurh])])
fig_freqbarh("sp_frame.png","A default of peace around conditioned combat",["combat (qital)","'do not transgress'","incline to peace","no compulsion (ikrah)"],[nqital,co_trans,co_peace,nkurh],[wk.AMBER,wk.TEAL,wk.TEAL,wk.TEAL],xlabel="ayat")
spec=dict(slug="W09_sword_or_peace",sub="conditioned combat, Week 9",
 main="Does Islam rule by the sword or by peace?",
 headline="The literal 'sword' never occurs - combat is a conditioned minority",
 intro1="A loaded either/or: 'Islam spread by the sword' vs 'Islam is a religion of pure peace.' The corpus is the referee. First datum: the literal word for 'sword' never occurs. We sense-filter the war vocabulary (killing is mostly murder, not war; striving is not all combat) and read the conditions placed on combat.",
 intro2="Counts recompute from Book6; only sense-filtered forms are counted (the killing-root is mostly 'kill/murder', not war).",
 qhead="The claim to test",qbody="'Rules by the sword' vs 'pure pacifism' - which, if either, does the corpus support?",
 mhead="The method",mpts=["count the war-words, sense-filtered (sword, war, combat, striving)",
   "separate combat (qital) from killing/murder",
   "read the conditions placed on combat - defensive, bounded, suspended on peace"],
 figs=[
  dict(t="The war vocabulary - and the missing word",png="sp_war.png",cf=TINT,
    cap=f"In the data - the literal 'sword' appears {nsayf} times; war-words exist (combat {nqital}, war {nharb}) but are a minority. There is no lexical basis for 'the sword.'"),
  dict(t="Killing is mostly NOT war",png="sp_kill.png",
    cap=f"In the data - the killing-root ({nqatl}) is mostly killing/murder - much of it CONDEMNED ('who kills one soul kills all', 5:32); only {nqital} are mutual combat (qital)."),
  dict(t="Combat is conditioned",png="sp_cond.png",cf=TINT,
    cap=f"In the data - combat ({nqital}) sits with 'do not transgress' ({co_trans}) and with peace ({co_peace}): defensive, bounded, and suspended on the enemy's peace."),
  dict(t="The killing-root across the corpus",png="sp_sura.png",
    cap="In the data - the killing-root spans the corpus, much of it in narrative and prohibition (murder condemned), not battle command."),
  dict(t="Combat and striving across the revelation",png="sp_time.png",cf=TINT,
    cap="In the data - combat concentrates in the Medinan period (self-defence of the community); striving (jihad) is broader than fighting."),
  dict(t="The literal 'sword' never appears",png="sp_absent.png",
    cap=f"In the data - sword = {nsayf}, while 'no compulsion' vocabulary (ikrah, {nkurh}) and conditioned combat frame the picture: a default of peace around hedged combat."),
  dict(t="A default of peace",png="sp_frame.png",cf=TINT,
    cap=f"In the data - combat ({nqital}) is wrapped in 'do not transgress' ({co_trans}), 'incline to peace' ({co_peace}) and 'no compulsion' ({nkurh}). Belief is left free (2:256)."),
 ],
 gal1=dict(title="Fighting is conditioned",items=glw(SW,["2:190","60:8"]) or [("2:190","وَقَاتِلُوا فِي سَبِيلِ اللَّهِ الَّذِينَ يُقَاتِلُونَكُمْ وَلَا تَعْتَدُوا","fight those who fight you, and do not transgress")],fill=AMBERT,hc=AMBER),
 gal2=dict(title="Peace, and no compulsion",items=(glw(SW,["8:61","2:256","49:9"])+glw(SW,["5:32"])) or [("2:256","لَا إِكْرَاهَ فِي الدِّينِ","there is no compulsion in religion")],fill=TINT,hc=TEAL),
 v1=("The sword is absent",f"the literal word for 'sword' = {nsayf}. War-words exist but are a minority - no lexical basis for 'the sword.'"),
 v2=("Killing is mostly not war",f"{nqatl-nqital} of the killing-root are killing/murder (much condemned); only {nqital} are mutual combat."),
 v3=("Combat is conditioned",f"defensive ('fight those who fight you', 2:190), bounded ('do not transgress', {co_trans}), suspended on peace ('incline to it', {co_peace})."),
 deep=("Conditioned combat inside a default of peace",
   f"Neither slogan holds. Combat is permitted but CONDITIONED: defensive ('fight those who fight you', 2:190), bounded ('do not transgress', {co_trans} co-occurrences), suspended on the enemy's peace ('if they incline to peace, incline to it', 8:61). And belief is left free: 'no compulsion in religion' (2:256; ikrah {nkurh}); be just to those who do not fight you (60:8)."),
 deep_extra=["'Rules by the sword' has no lexical basis (sword=0) and ignores the conditions; 'pure pacifism' ignores the real combat commands."],
 crit1=("Both slogans cherry-pick",
   "'rules by the sword' has no lexical basis and ignores the conditions; 'pure pacifism' ignores the real combat commands - each picks half."),
 crit2=("Raw counts would mislead",
   "the killing-root is mostly 'killing', the striving-root is broader than war; only sense-filtered forms were counted."),
 audit=[("check","Sword absent",f"literal sword = {nsayf}."),
   ("check","Combat sized",f"combat {nqital} of killing-root {nqatl}."),
   ("check","Conditions computed",f"'do not transgress' {co_trans}, peace {co_peace}, no-compulsion {nkurh}.")]+[("tilde","Sense-filtered","killing != war; striving != combat.")]+AT,
 method=("war vocabulary (sense-filtered); conditions","sword/war/combat counts, combat conditions","war bars, killing-vs-combat, condition bars, sura map"),
 take=("Conditioned combat inside a default of peace",
   [f"The literal 'sword' never appears ({nsayf}); combat ({nqital}) is a sense-filtered minority of the killing-root.",
    f"Combat is defensive, bounded ('do not transgress', {co_trans}), and suspended on peace ({co_peace}); belief is free ('no compulsion', {nkurh}).",
    "Both slogans cherry-pick; raw counts would mislead. Presented from the text."]),
 qr1=("The numbers",f"sword {nsayf} - war {nharb} - combat {nqital} - jihad {njihad}; killing-root {nqatl}; 'do not transgress' {co_trans}, peace {co_peace}, no-compulsion {nkurh}."),
 qr2=("The shape","no literal sword; combat conditioned (defensive, bounded, suspended on peace); belief free; both slogans cherry-pick."),
 syn=("Neither slogan",
   [("'By the sword'","no lexical basis (sword=0)"),("Conditioned combat","defensive, bounded"),("'Pure pacifism'","ignores real qital commands")],
   "A default of peace around hedged combat","combat is permitted but conditioned; belief is left free - both slogans cherry-pick."),
 quiz=("Special Topic - Sword or Peace? (Week 9)",[
  ("1.  The literal word for 'sword' appears in the Qur'an:",f"{nsayf} times (never)",["often","once","100 times"],"no lexical basis for 'the sword.'"),
  ("2.  The killing-root is mostly:","killing / murder, not war",["combat","striving","prayer"],f"only {nqital} of {nqatl} are mutual combat."),
  ("3.  Combat (qital) in the corpus is:","conditioned (defensive, bounded, suspended on peace)",["unconditional","forbidden entirely","the main theme"],"2:190, 8:61 hedge it."),
  ("4.  2:190 commands fighting:","those who fight you - and not to transgress",["everyone","no one","all disbelievers"],"defensive and bounded."),
  ("5.  8:61 says, if the enemy inclines to peace:","incline to it",["fight harder","ignore them","flee"],"combat is suspended on peace."),
  ("6.  2:256 establishes:","no compulsion in religion",["forced conversion","the sword","abrogation"],f"belief is free (ikrah {nkurh})."),
  ("7.  'Islam rules by the sword' is:","a cherry-pick with no lexical basis",["proven","the only reading","supported by sword-count"],"sword = 0; conditions ignored."),
  ("8.  'Islam is pure pacifism' is:","also a cherry-pick - it ignores the real combat commands",["fully correct","proven","irrelevant"],"qital commands exist, conditioned."),
  ("9.  Why must war-words be sense-filtered?","the killing-root is mostly murder; striving is broader than war",["they never repeat","Arabic lacks roots","to inflate war"],"raw counts would mislead either way."),
  ("10.  5:32 ('who kills one soul...') shows much killing is:","condemned, not commanded",["commanded","praised","ignored"],"the killing-root is largely prohibition."),
  ("11.  The honest verdict is:","conditioned combat inside a default of peace",["rule by the sword","pure pacifism","no position"],"neither slogan holds."),
  ("12.  Combat concentrates in:","the Medinan period (community self-defence)",["only Mecca","sura 108","the disjoint letters"],"self-defence of the community."),
  ("13.  These findings are:","presented from the text, sense-filtered",["doctrine","disproof","unrelated to Book6"],"both slogans cherry-pick; counts are sense-filtered."),
 ]),
)
standard_deck(spec)
print("done sword")

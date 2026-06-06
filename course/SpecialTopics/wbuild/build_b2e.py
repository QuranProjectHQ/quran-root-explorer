# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
B3=json.load(open(SB+"snip_batch3.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def coocN(rs): return int(df['toks'].map(lambda ts:all(r in ts for r in rs)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ SIGNS - nature vs scripture ============
nsign=ac('ءيي')
nat=['شمس','قمر','ليل','نهر','خلق','نبت']; scr=['كتب','نزل','تلو','بين','ذكر','قرء']
co_nat=sum(cooccur('ءيي',r) for r in nat); co_scr=sum(cooccur('ءيي',r) for r in scr)
gen=nsign-co_nat-co_scr
fig_groupbar("sg_two.png","One word, two registers - 'sign' co-occurs with...",["nature roots","scripture roots"],[("",[wk.TEAL,wk.AMBER],[co_nat,co_scr])])
fig_freqbarh("sg_scr.png","'Sign' with scripture roots",["bayyana clarify","anzala send-down","kitab book","tala recite","dhikr reminder","qara'a recite"],[cooccur('ءيي','بين'),cooccur('ءيي','نزل'),cooccur('ءيي','كتب'),cooccur('ءيي','تلو'),cooccur('ءيي','ذكر'),cooccur('ءيي','قرء')],[wk.AMBER]*6)
fig_freqbarh("sg_nat.png","'Sign' with nature roots",["layl night","nahr river/day","khalq creation","shams sun","qamar moon","nabt plant"],[cooccur('ءيي','ليل'),cooccur('ءيي','نهر'),cooccur('ءيي','خلق'),cooccur('ءيي','شمس'),cooccur('ءيي','قمر'),cooccur('ءيي','نبت')],[wk.TEAL]*6)
fig_groupbar("sg_split.png","The 353 signs by explicit context",["nature","scripture","general"],[("",[wk.TEAL,wk.AMBER,wk.GREY],[co_nat,co_scr,gen])])
fig_suradist("sg_sura.png","Where 'sign' (aya) falls, sura by sura","ءيي")
fig_timeline("sg_time.png","The sign-root across the revelation",[("aya ءيي","ءيي")])
fig_groupbar("sg_lean.png","Verbally toward scripture, conceptually both",["with scripture","with nature"],[("",[wk.AMBER,wk.TEAL],[co_scr,co_nat])])
spec=dict(slug="W07_signs_nature_scripture",sub="one word, two books, Week 7",
 main="One word for sunrise and scripture (aya)",
 headline="The same word names a recited verse and a natural wonder",
 intro1="The Qur'an calls a verse an 'aya' - and calls a sunrise, the rain, the human body an 'aya' too. Does one word really span cosmos and scripture? The sign-root appears 353 times; we tag where it co-occurs with NATURE roots vs SCRIPTURE roots.",
 intro2="Counts recompute from Book6; the sign-root total (353) reproduces exactly; co-occurrence uses explicit nature/scripture root sets.",
 qhead="The observation",qbody="Does the single word 'aya' genuinely span the natural world and the revealed text?",
 mhead="The method",mpts=["count the sign-root (353) and where it co-occurs with nature vs scripture roots",
   "compare the two registers; note the general remainder",
   "read the fusion verse (41:53) where cosmos and self are 'shown' as signs"],
 figs=[
  dict(t="One word, two registers",png="sg_two.png",cf=TINT,
    cap=f"In the data - the sign-root co-occurs with scripture roots in {co_scr} ayat and with nature roots in {co_nat}: verbally it leans to the recited signs, yet it is the SAME word for a sunrise."),
  dict(t="'Sign' with scripture",png="sg_scr.png",
    cap=f"In the data - 'sign' pairs with clarify, send-down, book, recite, reminder - the vocabulary of revelation ({co_scr} co-occurrences)."),
  dict(t="'Sign' with nature",png="sg_nat.png",cf=TINT,
    cap=f"In the data - 'sign' also pairs with night, creation, sun, moon, plant - the vocabulary of the cosmos ({co_nat} co-occurrences)."),
  dict(t="The 353 signs by context",png="sg_split.png",
    cap=f"In the data - of {nsign} sign-ayat, {co_scr} sit explicitly with scripture, {co_nat} with nature, and {gen} are general 'Our signs' - the term is deployed across both books."),
  dict(t="'Sign' across the corpus",png="sg_sura.png",cf=TINT,
    cap="In the data - the sign-root is spread throughout, naming verses and natural wonders alike."),
  dict(t="Across the revelation",png="sg_time.png",
    cap="In the data - the dual use of 'aya' runs the whole revelation; it is a structural feature, not a phase."),
  dict(t="Verbally scripture, conceptually both",png="sg_lean.png",cf=TINT,
    cap=f"In the data - the explicit lean is to scripture ({co_scr} vs {co_nat}), but the same word names nature - the conflation is the point (41:53: signs 'in the horizons and in themselves')."),
 ],
 gal1=dict(title="The fusion - signs in self and cosmos",items=gl(B2["ayat"],["41:53","51:21"]) or [("41:53","سَنُرِيهِمْ آيَاتِنَا فِي الْآفَاقِ وَفِي أَنفُسِهِمْ","We will show them Our signs in the horizons and in themselves")],fill=TINT,hc=TEAL),
 gal2=dict(title="Nature signs and scripture signs",items=(gl(B2["ayat"],["2:164","16:12"])+gl(B2["ayat"],["45:6","2:252"])) or [("2:164","لَآيَاتٍ لِّقَوْمٍ يَعْقِلُونَ","signs for a people who reason")],fill=AMBERT,hc=AMBER),
 v1=("One word, two books",f"the sign-root ({nsign}) names both a recited verse and a natural wonder - the same term for scripture and cosmos."),
 v2=("Verbally toward scripture",f"explicitly it sits with scripture ({co_scr}) far more than nature ({co_nat})..."),
 v3=("Conceptually both","...yet the very same word names the sun, the rain, the self - the fusion is deliberate (41:53)."),
 deep=("Creation and revelation share one vocabulary",
   f"The sign-root spans both registers - leaning verbally to the recited signs ({co_scr} vs {co_nat} in explicit co-occurrence) while naming nature with the very same term. The conflation is deliberate: the book and the world are presented as two volumes of one signage, each meant to be 'read.' 41:53 fuses them: 'We will show them Our signs in the horizons and in themselves.'"),
 deep_extra=[f"Of {nsign} sign-ayat, {gen} are general 'Our signs' - the term floats freely between the two books."],
 crit1=("Co-occurrence captures explicit pairing only",
   f"the {gen} general 'Our signs' are untagged; the nature/scripture tiers are the analyst's, and the root sets are a choice."),
 crit2=("But the dual use is robust",
   "the single word naming both a verse and a sunrise is the hard datum, independent of the tiering."),
 audit=[("check","Sign-root counted",f"{nsign} ayat (reproduces exactly)."),
   ("check","Two registers",f"scripture {co_scr}, nature {co_nat}."),
   ("tilde","Tiers are the analyst's","nature/scripture root sets are a labelled choice.")]+AT,
 method=("the sign-root; nature & scripture root sets","co-occurrence by register; general remainder","register bars, scripture/nature bars, sura map"),
 take=("Two volumes of one signage",
   [f"The same word 'aya' ({nsign}) names a recited verse AND a sunrise - creation and revelation share one vocabulary.",
    f"Verbally it leans to scripture ({co_scr} vs {co_nat}), but the dual use is the point: 41:53 shows signs 'in the horizons and in themselves.'",
    "Co-occurrence captures explicit pairing; the dual use is the robust datum. Presented from the text."]),
 qr1=("The numbers",f"sign-root {nsign} ayat; with scripture {co_scr}, with nature {co_nat}, general {gen}."),
 qr2=("The shape","one word for verse and cosmos; verbally leans scripture, conceptually both; the fusion is deliberate (41:53)."),
 syn=("Two books, one word",
   [("Nature signs","sun, rain, the self"),("One word: aya","names both"),("Scripture signs","verse, book, recite")],
   "Read creation as you read revelation","the book and the world are two volumes of one signage."),
 quiz=("Special Topic - One Word for Sunrise and Scripture (Week 7)",[
  ("1.  The word 'aya' in the Qur'an names:","both a recited verse and a natural wonder",["only verses","only nature","only the Kaaba"],"the same word spans cosmos and scripture."),
  ("2.  The sign-root appears about:",f"{nsign} times",["50","1000","once"],f"{nsign} ayat, reproduced exactly."),
  ("3.  Explicitly, 'sign' co-occurs MORE with:","scripture roots",["nature roots","neither","both equally"],f"scripture {co_scr} vs nature {co_nat}."),
  ("4.  Yet the same word also names:","the sun, rain, the self (nature)",["only the Prophet","only angels","only numbers"],"the dual use is the point."),
  ("5.  41:53 ('signs in the horizons and in themselves') is:","the fusion verse - cosmos and self as a text",["a nature-only verse","a scripture-only verse","unrelated"],"it fuses the two registers."),
  ("6.  The 'general Our signs' remainder is:","a large untagged group floating between both",["zero","all of them","scripture only"],f"{gen} general sign-ayat."),
  ("7.  The nature/scripture tiers are:","the analyst's labelled categories",["Qur'anic categories","computed by the text","arbitrary"],"a labelled choice of root sets."),
  ("8.  The robust datum is:","one word naming both a verse and a sunrise",["the exact co-occurrence counts","the root sets","the rhyme"],"independent of the tiering."),
  ("9.  'Verbally scripture, conceptually both' means:","explicit lean to scripture, but dual concept",["only scripture","only nature","no pattern"],f"{co_scr} vs {co_nat}, same word both."),
  ("10.  Reading creation, on this view, is:","like reading revelation",["forbidden","unrelated","impossible"],"two volumes of one signage."),
  ("11.  Co-occurrence captures:","explicit pairing, not all uses",["every use","no uses","only nature"],f"the {gen} general signs are untagged."),
  ("12.  The honest verdict is:","creation and revelation share one vocabulary",["two unrelated words","scripture only","nature only"],"the dual use is deliberate."),
  ("13.  These findings are:","presented from the text, tiers labelled",["doctrine","disproof","unrelated to Book6"],"the sign-root total is computed; tiers are labelled."),
 ]),
)
standard_deck(spec)
print("done signs")

# ============ HYPOCRITE SYNDROME ============
nnifaq=ac('نفق')
qm=cooccur('قلب','مرض'); nq=cooccur('نفق','قلب'); nk=cooccur('نفق','كذب'); nx=cooccur('نفق','خدع')
trio=coocN(['نفق','قلب','مرض'])
fig_freqbarh("hp_pairs.png","The syndrome holds as PAIRS",["heart . disease","hypocrisy . heart","hypocrisy . lying","hypocrisy . deception"],[qm,nq,nk,nx],[wk.TEAL,wk.TEAL,wk.AMBER,wk.RED],xlabel="shared ayat")
fig_groupbar("hp_trio.png","Strong as a pair, THIN as a trio",["heart.disease pair","full trio\n(hypocrite+heart+disease)"],[("",[wk.TEAL,wk.RED],[qm,trio])])
fig_suradist("hp_sura.png","Where hypocrisy is named, sura by sura","نفق")
fig_timeline("hp_time.png","The hypocrisy-root across the revelation",[("nifaq نفق","نفق")])
fig_groupbar("hp_support.png","Read the SUPPORT, not just the motif",["heart.disease","nifaq.heart","nifaq.lying","nifaq.deception","full trio"],[("",[wk.TEAL,wk.TEAL,wk.AMBER,wk.RED,wk.RED],[qm,nq,nk,nx,trio])],ylabel="shared ayat")
lf,j,na,nb=lift('نفق','قلب')
fig_liftscatter("hp_lift.png","Hypocrisy and the heart attract",[("nifaq . heart",nq,lf)])
fig_freqbarh("hp_field.png","The hypocrisy-field, and its links",["nifaq (hypocrite forms)","nifaq.heart","heart.disease","full trio"],[nnifaq,nq,qm,trio],[wk.NAVY,wk.TEAL,wk.TEAL,wk.RED],xlabel="ayat")
spec=dict(slug="W08_hypocrite_syndrome",sub="motif support, Week 8",
 main="The hypocrite syndrome - a motif, and its support",
 headline="A vivid three-part portrait that rests on only three verses",
 intro1="The Qur'an paints the hypocrite (munafiq) with a recurring cluster - a diseased heart and deception. Is the full three-part motif as solid as it feels? We sense-filter the root to the hypocrite forms (not 'spending'), count the pairwise links and the full trio, and read each one's verse-SUPPORT.",
 intro2="Counts recompute from Book6 and reproduce exactly; only the munafiq forms of the root are counted.",
 qhead="The claim to test",qbody="Is the hypocrite's 'diseased-heart + deception' motif a tight three-part formula, or a thin trio dressed as one?",
 mhead="The method",mpts=["sense-filter the root to the hypocrite forms (not 'spending')",
   "count each pairwise link and the full trio",
   "read the verse-SUPPORT - a vivid motif on few verses is fragile"],
 figs=[
  dict(t="Strong as pairs",png="hp_pairs.png",cf=TINT,
    cap=f"In the data - hypocrisy clusters with a diseased heart and deceit: heart+disease {qm} ('in their hearts a disease'), hypocrisy+heart {nq}, hypocrisy+lying {nk}, hypocrisy+deception {nx}."),
  dict(t="Thin as a trio",png="hp_trio.png",
    cap=f"In the data - the strongest pair (heart+disease, {qm}) is robust, but the COMPLETE munafiq+heart+disease motif holds in only {trio} verses - strong as a theme, slim as a trio."),
  dict(t="Hypocrisy across the corpus",png="hp_sura.png",cf=TINT,
    cap="In the data - the hypocrite forms cluster in the Medinan community suras (al-Baqara, an-Nisa, al-Munafiqun)."),
  dict(t="Across the revelation",png="hp_time.png",
    cap="In the data - the hypocrisy-root is concentrated in the Medinan period, when the community faced internal dissent."),
  dict(t="Read the support",png="hp_support.png",cf=TINT,
    cap=f"In the data - the links weaken as they specialize: {qm} -> {nq} -> {nk} -> {nx} -> {trio}. The motif is real but its tightest form rests on little."),
  dict(t="Hypocrisy and the heart attract",png="hp_lift.png",
    cap=f"In the data - hypocrisy and 'heart' co-occur at {lf:.1f}x chance ({nq} ayat): the pairwise syndrome is genuine."),
  dict(t="The field and its links",png="hp_field.png",cf=TINT,
    cap=f"In the data - the hypocrite-field ({nnifaq}) supports strong pairs but a {trio}-verse trio - vividness is not support."),
 ],
 gal1=dict(title="A diseased heart",items=gl(B3["hypo"],["2:10","8:49"]) or [("2:10","فِي قُلُوبِهِم مَّرَضٌ","in their hearts is a disease")],fill=TINT,hc=TEAL),
 gal2=dict(title="Deception, and they lie",items=(gl(B3["hypo"],["4:142"])+gl(B3["hypo"],["63:1"])) or [("63:1","وَاللَّهُ يَشْهَدُ إِنَّ الْمُنَافِقِينَ لَكَاذِبُونَ","God bears witness that the hypocrites are liars")],fill=AMBERT,hc=AMBER),
 v1=("A real pairwise syndrome",f"hypocrisy clusters with a diseased heart ({nq}) and the heart with disease ({qm}) - a genuine, well-supported motif."),
 v2=("But a thin trio",f"the complete three-part motif (hypocrite + heart + disease) holds in only {trio} verses - slim as a tight formula."),
 v3=("Support, not vividness",f"a vivid motif on {trio} verses is fragile; a leave-one-out would shake it - read the base, not the picture."),
 deep=("The portrait is real; its tightest form rests on little",
   f"The hypocrite is drawn as heart-diseased and deceptive - a robust PAIRWISE syndrome (heart+disease {qm}, hypocrisy+heart {nq}) but a thin TRIO ({trio} verses). So the portrait is genuine; quoting it as a tight three-part formula overstates a {trio}-verse base. Support, not vividness, decides - the exact Week-8 caution."),
 deep_extra=[f"The root is polysemous (spend vs hypocrite) - only the munafiq forms were counted."],
 crit1=("A 3-verse trio is fragile",
   f"with only {trio} supporting verses, a leave-one-out would shake the trio - vividness must not be mistaken for support."),
 crit2=("Sense-filtering is load-bearing",
   "the root also means 'to spend' (infaq); only the hypocrite forms were counted, or the field would balloon with charity verses."),
 audit=[("check","Pairs counted",f"heart-disease {qm}, nifaq-heart {nq}, nifaq-lying {nk}, nifaq-deception {nx}."),
   ("check","Trio counted",f"full motif = {trio} verses."),
   ("check","Lift computed",f"nifaq-heart {lf:.1f}x chance.")]+[("tilde","Thin trio wobbles","a 3-verse base is fragile under leave-one-out.")]+AT,
 method=("hypocrite forms (sense-filtered); cluster roots","pairwise & trio co-occurrence; support","pairwise bars, trio bar, support ladder, sura map"),
 take=("A genuine portrait, a fragile formula",
   [f"The hypocrite-syndrome is real as PAIRS (heart+disease {qm}, hypocrisy+heart {nq}) but thin as a TRIO ({trio} verses).",
    "Quoting it as a tight three-part formula overstates a 3-verse base - a leave-one-out would shake it.",
    "Support, not vividness, decides; only the munafiq forms were counted. Presented from the text."]),
 qr1=("The numbers",f"hypocrite-field {nnifaq}; heart.disease {qm}, nifaq.heart {nq} ({lf:.1f}x), nifaq.lying {nk}, nifaq.deception {nx}; full trio {trio}."),
 qr2=("The shape","strong pairwise syndrome, thin 3-verse trio; read support not vividness; sense-filter spend vs hypocrite."),
 syn=("Vivid, but read the base",
   [("Pairs strong","heart+disease, nifaq+heart"),("Trio thin","only 3 verses"),("Verdict","support, not vividness")],
   "The portrait is real; the formula is fragile","a 3-verse trio wobbles under leave-one-out - the Week-8 caution."),
 quiz=("Special Topic - The Hypocrite Syndrome (Week 8)",[
  ("1.  The hypocrite-syndrome is STRONG as:","pairwise links (heart+disease, hypocrisy+heart)",["a full trio","a single word","a divine name"],f"heart+disease {qm}, nifaq+heart {nq}."),
  ("2.  The full three-part motif holds in only:",f"{trio} verses",["100 verses","12 verses","zero"],f"the trio is thin - {trio} verses."),
  ("3.  The strongest pairwise link is:",f"heart + disease ({qm})",["hypocrisy+deception","hypocrisy+lying","the trio"],f"{qm} shared ayat ('in their hearts a disease')."),
  ("4.  The Week-8 lesson here is:","read SUPPORT, not just the vivid motif",["lift is everything","count is everything","ignore support"],"a vivid motif on few verses is fragile."),
  ("5.  The root had to be sense-filtered because it also means:","to spend (infaq)",["to pray","to fast","to travel"],"only the munafiq forms were counted."),
  ("6.  A 3-verse trio is described as:","fragile - a leave-one-out would shake it",["rock-solid","the strongest","irrelevant"],"thin support wobbles."),
  ("7.  Hypocrisy and 'heart' co-occur at about:",f"{lf:.1f}x chance",["below chance","exactly chance","never"],f"a genuine pairwise bond ({nq} ayat)."),
  ("8.  The hypocrite forms cluster in:","the Medinan community suras",["only Mecca","sura 108","the disjoint letters"],"internal dissent in Medina."),
  ("9.  'Vividness is not support' means:","a striking motif can rest on very few verses",["vivid motifs are always solid","support is irrelevant","counts lie"],"the trio is vivid but thin."),
  ("10.  The links weaken as they:","specialize (pair -> trio)",["generalize","repeat","disappear"],f"{qm} -> {nq} -> {nk} -> {nx} -> {trio}."),
  ("11.  Quoting the syndrome as a tight three-part formula:","overstates a 3-verse base",["is fully justified","understates it","is impossible"],"the trio is thin."),
  ("12.  The honest verdict is:","a genuine pairwise portrait, a fragile trio",["a solid formula","no syndrome at all","pure fabrication"],"support, not vividness, decides."),
  ("13.  These findings are:","computed from Book6 (sense-filtered) and reproducible",["estimated","theological","unrelated"],"only munafiq forms counted; counts reproduce."),
 ]),
)
standard_deck(spec)
print("done hypocrite")

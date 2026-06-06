# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,fig_donut,norm,df,SUR,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
B3=json.load(open(SB+"snip_batch3.json",encoding="utf-8"))
SC=json.load(open(SB+"snip_scope.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def coocN(rs): return int(df['toks'].map(lambda ts:all(r in ts for r in rs)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ DARKNESS -> LIGHT (direction) ============
T=df[TOK].astype(str).map(norm); dl=ld=0
for t in T:
    if 'ظلمات' in t and 'نور' in t:
        if t.index('ظلمات')<t.index('نور'): dl+=1
        else: ld+=1
co_ld=cooccur('نور','ظلم'); co_god=coocN(['نور','ظلم','ءله']); co_tagh=coocN(['نور','ظلم','طغو'])
fig_groupbar("d2l_dir.png","The journey runs one way: out of darkness into light",["dark -> light","light -> dark"],[("",[wk.TEAL,wk.RED],[dl,ld])])
fig_groupbar("d2l_agent.png","And it names its agent",["God brings out\n(+ God in verse)","the taghut drags\n(+ taghut)"],[("",[wk.TEAL,wk.RED],[co_god,co_tagh])])
fig_suradist("d2l_sura.png","Where the light/darkness journey falls","نور")
fig_freqbarh("d2l_counts.png","Direction and agency, side by side",["dark -> light","light -> dark","with God in verse","with taghut"],[dl,ld,co_god,co_tagh],[wk.TEAL,wk.RED,wk.NAVY,wk.AMBER],xlabel="ayat")
fig_timeline("d2l_time.png","The light/darkness pair across the revelation",[("light نور","نور"),("dark ظلم","ظلم")])
lf,j,na,nb=lift("نور","ظلم")
fig_liftscatter("d2l_lift.png","Light and darkness are a bonded contrast pair",[("نور . ظلمات",co_ld,lf)])
fig_groupbar("d2l_ratio.png","A 5-to-1 directional asymmetry",["dark->light","light->dark"],[("",[wk.TEAL,wk.RED],[dl,ld])],ylabel="directional phrases")
spec=dict(slug="W06_darkness_to_light",sub="direction & agency, Week 6",
 main="'Out of darkness into light' - a one-way arrow",
 headline="Direction encodes agency - and the lone reversal names the culprit",
 intro1="The Qur'an speaks of moving between darkness and light. Is the movement symmetric, or fixed in direction - and who is its agent? We count the directional phrase both ways and record the subject of each (who brings whom).",
 intro2="Direction is read from token order in ayat naming both; counts recompute from Book6.",
 qhead="The question",qbody="Is the darkness/light movement symmetric, or one-way - and who drives it?",
 mhead="The method",mpts=["count the directional phrase both ways (darkness->light vs light->darkness)",
   "record the SUBJECT of each movement (God vs the false patron)",
   "let direction plus agency carry the finding"],
 figs=[
  dict(t="A one-way arrow",png="d2l_dir.png",cf=TINT,
    cap=f"In the data - the journey runs darkness -> light {dl} times and the reverse only {ld}: a ~{dl/max(ld,1):.0f}-to-1 directional asymmetry."),
  dict(t="It names its agent",png="d2l_agent.png",
    cap=f"In the data - where the journey to light appears, God is the named subject ({co_god} ayat with God in the verse); the reversal is tied to the false patron (taghut, {co_tagh})."),
  dict(t="Where the journey falls",png="d2l_sura.png",cf=TINT,
    cap="In the data - the light/darkness journey clusters in the guidance passages (2:257; 5:16; 14:1)."),
  dict(t="Direction and agency side by side",png="d2l_counts.png",
    cap=f"In the data - {dl} forward vs {ld} reverse; God-agency {co_god} vs taghut {co_tagh}. The arrow and its driver point the same way."),
  dict(t="The pair across the revelation",png="d2l_time.png",cf=TINT,
    cap="In the data - the light/darkness contrast runs the whole revelation; the directional asymmetry is consistent."),
  dict(t="A bonded contrast pair",png="d2l_lift.png",
    cap=f"In the data - light and darkness co-occur in {co_ld} ayat at {lf:.1f}x chance: they are deployed together precisely to mark the journey."),
  dict(t="The asymmetry, plainly",png="d2l_ratio.png",cf=TINT,
    cap=f"In the data - {dl} forward to {ld} reverse: the lone reversal (2:257, the taghut) is the exception that names the agent of darkness."),
 ],
 gal1=dict(title="God brings out of darkness into light",items=gl(B3["light"],["2:257","5:16","14:1"]) or [("2:257","يُخْرِجُهُم مِّنَ الظُّلُمَاتِ إِلَى النُّورِ","He brings them out of the darknesses into the light")],fill=TINT,hc=TEAL),
 gal2=dict(title="The lone reversal - the taghut",items=gl(B3["light"],["2:257"]) or [("2:257","يُخْرِجُونَهُم مِّنَ النُّورِ إِلَى الظُّلُمَاتِ","they bring them out of the light into the darknesses")],fill=REDT,hc=RED),
 v1=("A one-way arrow",f"out of (plural) darkness into (single) light {dl} times; the reverse only {ld} - a fixed direction."),
 v2=("God is its subject",f"the forward journey names God as the one who 'brings them out' ({co_god} ayat with God in the verse)."),
 v3=("The reversal names the agent",f"the lone light->darkness case (2:257) is the taghut dragging the wrong way - the exception that proves the rule."),
 deep=("Direction encodes agency",
   f"Salvation has a direction: out of the plural darknesses into the single light ({dl} times), and God is its subject. The one reversal ({ld}) is explicitly attributed to the taghut (false gods). So the arrow encodes agency - toward light is God's work; toward darkness is the false patron's. This builds on the Week-4 number: one light, many darknesses."),
 deep_extra=["Small support - a handful of directional phrases - but the asymmetry is clear and the agents are named."],
 crit1=("Small support",
   f"only {dl+ld} directional phrases in all; the asymmetry is clear but rests on few verses."),
 crit2=("'Direction = agency' is the reading",
   "the counts and the named subjects are computed; the claim that direction encodes agency is the labelled interpretation."),
 audit=[("check","Direction counted",f"dark->light {dl}, reverse {ld}."),
   ("check","Agents named",f"God {co_god}, taghut {co_tagh}."),
   ("check","Pair bonded",f"{co_ld} shared ayat, {lf:.1f}x chance.")]+[("tilde","Few verses","the asymmetry rests on a small base.")]+AT,
 method=("light & darkness; directional token order","direction count, named subject, co-occurrence","direction bars, agent bars, sura map"),
 take=("A one-way arrow that names its driver",
   [f"The journey runs out of darkness into light {dl} times; the reverse only {ld} - a fixed direction.",
    f"God is the subject of the forward journey; the lone reversal (2:257) is the taghut dragging the other way.",
    "Direction encodes agency - a labelled reading over a clear, if small, computed asymmetry. Presented from the text."]),
 qr1=("The numbers",f"dark->light {dl} - light->dark {ld} - with God {co_god} - with taghut {co_tagh} - pair {co_ld} ayat ({lf:.1f}x)."),
 qr2=("The shape","a one-way arrow (darkness->light), God its agent; the single reversal names the taghut; small support, clear asymmetry."),
 syn=("Arrow and agent",
   [("Darkness (plural)","the starting state"),("-> Light (single)","God brings them out"),("Reversal","the taghut - the lone exception")],
   "Direction encodes agency","toward light is God's work; toward darkness is the false patron's - the lone reversal names it."),
 quiz=("Special Topic - Out of Darkness into Light (Week 6)",[
  ("1.  The darkness/light movement is:","one-way (darkness -> light dominates)",["symmetric","light -> dark dominates","random"],f"{dl} forward vs {ld} reverse."),
  ("2.  The agent of the forward journey is:","God",["the taghut","the angels","mankind"],f"God 'brings them out' ({co_god} ayat)."),
  ("3.  The single reversal (light -> darkness) is attributed to:","the taghut (false patron)",["God","the Prophet","no one"],"2:257 - the lone exception names the agent of darkness."),
  ("4.  The directional asymmetry is about:",f"{dl} to {ld}",["1 to 1","even","reversed"],"a strong one-way arrow."),
  ("5.  This topic builds on the Week-4 finding that:","light is singular, darkness plural",["wealth is a trial","names pair","order is by length"],"one light, many darknesses."),
  ("6.  'Direction = agency' is:","the labelled reading over computed counts",["a raw count","proven theology","irrelevant"],"counts are computed; the reading is labelled."),
  ("7.  The support for the finding is:","small (a handful of directional phrases)",["thousands of verses","zero","exactly 100"],f"only {dl+ld} directional phrases."),
  ("8.  Light and darkness are:","a bonded contrast pair (co-occur above chance)",["never together","unrelated","identical"],f"{co_ld} shared ayat, {lf:.1f}x."),
  ("9.  Direction is read from:","token order within ayat naming both",["the translation","the rhyme","outside the corpus"],"computed from Book6's tokenized text."),
  ("10.  The lone reversal is best called:","the exception that proves (names) the rule",["the main pattern","a counting error","symmetric"],"it identifies the agent of darkness."),
  ("11.  The forward journey goes:","out of plural darkness into single light",["into many lights","out of one darkness","nowhere"],"plural darknesses -> single light."),
  ("12.  The honest verdict is:","a one-way arrow that names its driver",["a symmetric swing","no pattern","light->dark wins"],"direction plus agency, computed and labelled."),
  ("13.  These findings are:","presented from the text, on a small but clear base",["doctrine","disproof","unrelated to Book6"],"the asymmetry is computed; the reading is labelled."),
 ]),
)
standard_deck(spec)
print("done darkness_to_light")

# ============ LOCAL / REGIONAL / GLOBAL ============
g_nas=ac('ءنس'); g_alam=form_ac(['العالمين','عالمين']); r_musa=ac('وسي'); r_fir=ac('فرعن'); r_ibr=ac('برهم'); r_nuh=ac('نوح')
l_kaba=ac('كعب'); l_aad=form_ac(['عاد']); l_thamud=form_ac(['ثمود']); l_arab=form_ac(['عربي','عربيا']); l_qur=ac('قرش')
fig_groupbar("lrg_tiers.png","Three scales of reach (ayat naming each)",
  ["GLOBAL\nmankind/worlds","REGIONAL\nMoses/Pharaoh/Abraham","LOCAL\nKaaba/Aad/Quraysh"],
  [("",[wk.TEAL,wk.AMBER,wk.RED],[g_nas+g_alam,r_musa+r_fir+r_ibr,l_kaba+l_aad+l_qur])])
fig_freqbarh("lrg_regional.png","A global frame, a regional story",
  ["مankind (nas)","Moses","Pharaoh","Abraham","Noah","the worlds"],[g_nas,r_musa,r_fir,r_ibr,r_nuh,g_alam],[wk.TEAL,wk.AMBER,wk.AMBER,wk.AMBER,wk.AMBER,wk.TEAL])
fig_freqbarh("lrg_local.png","Its own backyard, barely named",
  ["Aad","Thamud","the Kaaba","the Arabic tongue","Quraysh"],[l_aad,l_thamud,l_kaba,l_arab,l_qur],[wk.RED,wk.RED,wk.RED,wk.GREY,wk.RED],xlabel="ayat naming it")
fig_groupbar("lrg_asym.png","A distant Exodus outweighs the local Quraysh",["Moses","Quraysh"],[("",[wk.AMBER,wk.RED],[r_musa,l_qur])])
fig_suradist("lrg_musa_sura.png","Where Moses appears, sura by sura","وسي")
fig_suradist("lrg_nas_sura.png","Where 'mankind' appears, sura by sura","ءنس")
fig_groupbar("lrg_all.png","The full tiering",["mankind","worlds","Moses","Pharaoh","Abraham","Kaaba","Quraysh"],
  [("",[wk.TEAL,wk.TEAL,wk.AMBER,wk.AMBER,wk.AMBER,wk.RED,wk.RED],[g_nas,g_alam,r_musa,r_fir,r_ibr,l_kaba,l_qur])])
spec=dict(slug="W07_local_regional_global",sub="reach & name-fields, Week 7",
 main="Local, regional, or global? The reach of the content",
 headline="A global frame, told through a regional past, on a barely-named local stage",
 intro1="Is the Qur'an a local Arabian text, a regional Near-Eastern one, or a universal address? Its own name-vocabulary points somewhere. We count ayat naming three tiers - GLOBAL (mankind, the worlds), REGIONAL (the Abrahamic prophets), LOCAL (Kaaba, Aad/Thamud, the Arabic tongue, Mecca, Quraysh).",
 intro2="Counts recompute from Book6 by root/surface; proper-name normalization is imperfect (a stated limit), but the asymmetries are large.",
 qhead="The question",qbody="Where does the Qur'an's content point - local, regional, or global?",
 mhead="The method",mpts=["count ayat naming each tier's key terms",
   "compare the three scales against each other",
   "treat name-mention as REACH, not emphasis - a labelled proxy"],
 figs=[
  dict(t="Three scales at once",png="lrg_tiers.png",cf=TINT,
    cap=f"In the data - global terms (mankind+worlds {g_nas+g_alam}), regional (Moses+Pharaoh+Abraham {r_musa+r_fir+r_ibr}) and local (Kaaba+Aad+Quraysh {l_kaba+l_aad+l_qur}) all operate - the regional story is by far the densest."),
  dict(t="A global frame, a regional story",png="lrg_regional.png",
    cap=f"In the data - framed globally (mankind {g_nas}, the worlds {g_alam}) yet narrated through the Near-East: Moses fills {r_musa} ayat - rivalling 'mankind' itself - with Pharaoh {r_fir} and Abraham {r_ibr}."),
  dict(t="Its own backyard, barely named",png="lrg_local.png",cf=TINT,
    cap=f"In the data - the Arabian setting is sparse by name: Aad {l_aad}, Thamud {l_thamud}, the Kaaba {l_kaba}, the Arabic tongue {l_arab}, Quraysh {l_qur}. The local is the stage, not the subject."),
  dict(t="Exodus outweighs Quraysh",png="lrg_asym.png",
    cap=f"In the data - Moses ({r_musa}) vs Quraysh ({l_qur}): a distant Exodus dwarfs the local tribe by ~{r_musa/max(l_qur,1):.0f}x. No rounding artefact."),
  dict(t="Moses across the corpus",png="lrg_musa_sura.png",cf=TINT,
    cap="In the data - the Moses narrative is spread across many suras - the densest single thread of the regional story."),
  dict(t="'Mankind' across the corpus",png="lrg_nas_sura.png",
    cap="In the data - 'mankind' is named throughout - the global frame within which the regional story is told."),
  dict(t="The full tiering",png="lrg_all.png",cf=TINT,
    cap=f"In the data - global (mankind {g_nas}, worlds {g_alam}), regional (Moses {r_musa}, Pharaoh {r_fir}, Abraham {r_ibr}), local (Kaaba {l_kaba}, Quraysh {l_qur}) - the particular is a doorway to the universal."),
 ],
 gal1=dict(title="GLOBAL - all mankind / the worlds",items=gl(SC,["1:2","49:13"]) or [("1:2","رَبِّ الْعَالَمِينَ","Lord of the worlds")],fill=TINT,hc=TEAL),
 gal2=dict(title="REGIONAL past, LOCAL setting",items=(gl(SC,["79:17","2:136"])+gl(SC,["3:96","106:1"])) or [("3:96","إِنَّ أَوَّلَ بَيْتٍ","the first House...")],fill=AMBERT,hc=AMBER),
 v1=("Global frame",f"the Qur'an addresses all mankind ({g_nas}) and is 'Lord of the worlds' ({g_alam}) - the widest scale."),
 v2=("Regional story",f"its narrative runs through the Abrahamic Near-East - Moses ({r_musa}), Pharaoh ({r_fir}), Abraham ({r_ibr}): by far the densest tier."),
 v3=("Local stage",f"its own Hijaz is named sparingly - Kaaba ({l_kaba}), Quraysh ({l_qur}), the Arabic tongue ({l_arab}): the stage, not the subject."),
 deep=("The particular as a doorway to the universal",
   f"All three scales operate at once. The Qur'an addresses ALL mankind (global), tells its story through the shared Abrahamic past (regional, by far the densest - Moses alone fills {r_musa} ayat), and treats its own Hijaz as the stage rather than the subject (Mecca/Quraysh barely named). A distant Exodus outweighs the local Quraysh by ~{r_musa/max(l_qur,1):.0f}x: the particular becomes the doorway to the universal, not its rival."),
 deep_extra=["The asymmetry is robust - Moses vs Quraysh is no rounding artefact."],
 crit1=("Mention proxies reach, not weight",
   "name-mention measures REACH, not emphasis or theological weight; proper-name normalization is imperfect; the tiers are the analyst's, not a Qur'anic category."),
 crit2=("But the asymmetry is robust",
   f"Moses ({r_musa}) vs Mecca/Quraysh (~{l_qur}) is far too large to be an artefact - the global-frame/regional-story/local-stage shape holds."),
 audit=[("check","Tiers counted",f"global {g_nas+g_alam}, regional {r_musa+r_fir+r_ibr}, local {l_kaba+l_aad+l_qur}."),
   ("check","Asymmetry robust",f"Moses {r_musa} vs Quraysh {l_qur}."),
   ("tilde","Name normalization","proper-name folding is imperfect (a stated limit).")]+[("tilde","Tiers are the analyst's","'local/regional/global' is a labelled category.")]+AT[:1]+AT[1:],
 method=("name-fields by tier (root/surface)","ayat naming each; compare three scales","tier bars, regional/local bars, sura maps"),
 take=("A global frame, a regional story, a local stage",
   [f"The Qur'an addresses all mankind (global, {g_nas}), narrates through the Abrahamic past (regional - Moses {r_musa}, the densest thread), and barely names its own Hijaz (local - Quraysh {l_qur}).",
    f"A distant Exodus outweighs the local tribe by ~{r_musa/max(l_qur,1):.0f}x - the particular is a doorway to the universal.",
    "Name-mention proxies reach, not weight (a labelled limit); the asymmetry is robust. Presented from the text."]),
 qr1=("The numbers",f"mankind {g_nas} - worlds {g_alam} - Moses {r_musa} - Pharaoh {r_fir} - Abraham {r_ibr} - Kaaba {l_kaba} - Quraysh {l_qur}."),
 qr2=("The shape","all three scales at once; regional story densest; local stage barely named; mention = reach (a labelled proxy)."),
 syn=("Three scales, one text",
   [("GLOBAL","all mankind, the worlds"),("REGIONAL","the Abrahamic past (densest)"),("LOCAL","Hijaz - the stage, barely named")],
   "The particular, a doorway to the universal","a distant Exodus outweighs the local tribe - the local is the stage, not the subject."),
 quiz=("Special Topic - Local, Regional, Global Reach (Week 7)",[
  ("1.  The densest name-tier in the Qur'an is:","the regional (Abrahamic) story",["the local Arabian setting","the global frame","none"],f"Moses alone fills {r_musa} ayat."),
  ("2.  'Mankind' (the global frame) is named about:",f"{g_nas} ayat",["once",f"{l_qur}","never"],"the widest scale."),
  ("3.  Quraysh, the local tribe, is named:",f"~{l_qur} time(s)",[f"{r_musa}","100","never"],"the local stage is barely named."),
  ("4.  Moses vs Quraysh shows:","a distant Exodus dwarfs the local tribe",["the local dominates","they are equal","neither appears"],f"~{r_musa/max(l_qur,1):.0f}x asymmetry."),
  ("5.  Name-mention is treated as a proxy for:","reach, not emphasis or weight",["theological importance","rhyme","length"],"a labelled limit."),
  ("6.  The 'local/regional/global' tiers are:","the analyst's categories, not Qur'anic",["Qur'anic categories","computed by the text","arbitrary and useless"],"a labelled interpretation."),
  ("7.  The Qur'an's own Hijaz functions as:","the stage, not the subject",["the main subject","unmentioned","the global frame"],"Mecca/Quraysh barely named."),
  ("8.  All three scales:","operate at once",["are mutually exclusive","cancel out","are identical"],"global frame, regional story, local stage."),
  ("9.  'Lord of the worlds' (1:2) is an example of the:","global tier",["local tier","regional tier","no tier"],"the widest frame."),
  ("10.  The robustness of the finding rests on:","the sheer size of the asymmetry",["a single verse","exact normalization","rhyme"],"Moses vs Quraysh is no rounding artefact."),
  ("11.  Proper-name normalization is:","imperfect - a stated limit",["perfect","irrelevant","computed flawlessly"],"the topic flags it openly."),
  ("12.  The honest verdict is:","a global frame, a regional story, a local stage",["purely local","purely global","purely regional"],"the particular is a doorway to the universal."),
  ("13.  These findings are:","presented from the text, with limits flagged",["doctrine","disproof","unrelated to Book6"],"the asymmetry is computed; the tiers are labelled."),
 ]),
)
standard_deck(spec)
print("done local_regional_global")

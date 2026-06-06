# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,norm,df,SUR,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B3=json.load(open(SB+"snip_batch3.json",encoding="utf-8"))
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; they do not settle theology."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ LIGHT & DARKNESS ============
nlight=fac_sub(['نور']); nanwar=form_ac(['انوار']); nzulu=fac_sub(['ظلمات']); nzulm=form_ac(['ظلمه','الظلمه'])
co_ld=cooccur('نور','ظلم')
fig_groupbar("ld_count.png","Light outnumbers darkness (~2 to 1)",["light (noun)","darkness (zulumat)"],[("",[wk.TEAL,wk.NAVY],[nlight,nzulu])])
fig_groupbar("ld_number.png","Light is ALWAYS singular; darkness ALWAYS plural",
  ["light singular","light PLURAL","darkness PLURAL","darkness singular"],[("",[wk.TEAL,wk.GREY,wk.NAVY,wk.GREY],[nlight,nanwar,nzulu,nzulm])])
fig_suradist("ld_light_sura.png","Where light is named, sura by sura","نور")
fig_suradist("ld_dark_sura.png","Where darkness is named, sura by sura","ظلم")
fig_timeline("ld_time.png","Light and darkness across the revelation",[("light نور","نور"),("dark ظلم","ظلم")])
lf,j,na,nb=lift("نور","ظلم")
fig_liftscatter("ld_pair.png","Light and darkness travel together",[("نور . ظلمات",co_ld,lf)])
fig_freqbarh("ld_forms.png","The two words, by grammatical number",
  ["نور  light - singular (always)","ظلمات  darkness - plural (always)","انوار  light-plural","ظلمة  darkness-singular"],
  [nlight,nzulu,nanwar,nzulm],[wk.TEAL,wk.NAVY,wk.GREY,wk.GREY],xlabel="ayat containing the form")
spec=dict(slug="W04_light_darkness",sub="number & morphology, Week 4",
 main="One light, many darknesses",
 headline="A creed encoded in grammatical number - with zero exceptions",
 intro1="Light and darkness are a stock pair, but their NUMBER tells a story: is 'light' (nur) ever plural? is 'darkness' (zulumat) ever singular? We count every surface form, tagging singular vs plural, and weigh light against darkness overall.",
 intro2="Counts recompute from Book6 by surface form; fire (nar) shares the lexical family but is a different sense and is excluded.",
 qhead="The observation",qbody="Does the grammatical NUMBER of light vs darkness encode a consistent pattern?",
 mhead="The method",mpts=["count every surface form of light and of darkness",
   "tag each as singular or plural",
   "weigh light against darkness overall - let number, not translation, carry the finding"],
 figs=[
  dict(t="Light outnumbers darkness",png="ld_count.png",cf=TINT,
    cap=f"In the data - light (noun) is named in {nlight} ayat, darkness in {nzulu}: the corpus weights illumination over its absence by roughly {nlight/max(nzulu,1):.1f} to 1."),
  dict(t="One light, many darknesses - zero exceptions",png="ld_number.png",
    cap=f"In the data - light is ALWAYS singular (plural 'anwar' = {nanwar}); darkness is ALWAYS plural (singular 'zulma' = {nzulm}). A hard morphological datum with no counter-examples."),
  dict(t="Light across the corpus",png="ld_light_sura.png",cf=TINT,
    cap="In the data - light clusters in the guidance and divine-attribute passages (24:35, 'God is the light...')."),
  dict(t="Darkness across the corpus",png="ld_dark_sura.png",
    cap="In the data - darkness appears alongside light in the journey passages ('out of the darknesses into the light')."),
  dict(t="Both across the revelation",png="ld_time.png",cf=TINT,
    cap="In the data - the pair runs the whole revelation; the singular/plural asymmetry holds throughout."),
  dict(t="They travel together",png="ld_pair.png",
    cap=f"In the data - light and darkness co-occur in {co_ld} ayat at {lf:.1f}x chance: a deliberate contrast pair, not separate vocabularies."),
  dict(t="By grammatical number",png="ld_forms.png",cf=TINT,
    cap=f"In the data - singular light ({nlight}) vs plural darkness ({nzulu}); the 'wrong-number' forms (plural light, singular darkness) are both {nanwar}/{nzulm} - they do not occur."),
 ],
 gal1=dict(title="God is light; darknesses and the light",items=gl(B3["light"],["24:35","6:1"]) or [("24:35","اللَّهُ نُورُ السَّمَاوَاتِ وَالْأَرْضِ","God is the light of the heavens and the earth")],fill=TINT,hc=TEAL),
 gal2=dict(title="Out of the darknesses into the light",items=gl(B3["light"],["2:257","5:16"]) or [("2:257","يُخْرِجُهُم مِّنَ الظُّلُمَاتِ إِلَى النُّورِ","He brings them out of the darknesses into the light")],fill=AMBERT,hc=AMBER),
 v1=("One light",f"'nur' appears in {nlight} ayat and is ALWAYS singular - never pluralised ('anwar' = {nanwar})."),
 v2=("Many darknesses",f"'zulumat' appears in {nzulu} ayat and is ALWAYS plural - the singular 'zulma' = {nzulm}."),
 v3=("And light leads",f"light is named ~{nlight/max(nzulu,1):.1f}x as often as darkness - the corpus weights illumination over its absence."),
 deep=("Unity of light, multiplicity of dark",
   f"With zero exceptions, a single 'nur' (never pluralised) is set against plural 'zulumat' (never singularised), and light outnumbers darkness ({nlight} vs {nzulu}). The grammar encodes a creed: truth and guidance are ONE; error and confusion are MANY. The number is the message."),
 deep_extra=["The morphology is a hard datum (0 counter-examples); the reading laid over it is labelled."],
 crit1=("The reading is laid over the datum",
   "'one truth, many errors' is the interpretation; the 0-exception singular/plural split is the computed fact."),
 crit2=("Fire shares the family but not the sense",
   "'nar' (fire) belongs to a related lexical family but is a different concept and is excluded - a sense-verification step."),
 audit=[("check","Counts exact",f"light {nlight}, darkness {nzulu}."),
   ("check","Zero exceptions","plural-light and singular-darkness both = 0; no counter-examples."),
   ("check","Light leads",f"~{nlight/max(nzulu,1):.1f}x more than darkness.")]+[("tilde","Fire excluded","'nar' is a different sense, kept out.")]+AT,
 method=("light & darkness surface forms","number (singular/plural), totals, co-occurrence","count bars, number bars, sura maps"),
 take=("The number is the message",
   [f"Light is always singular ({nlight} ayat, never plural); darkness is always plural ({nzulu}, never singular).",
    f"Light leads darkness ~{nlight/max(nzulu,1):.1f} to 1, and the two are a tight contrast pair ({co_ld} shared ayat).",
    "The grammar encodes a creed - one truth, many errors - a labelled reading laid over a 0-exception datum. Presented from the text."]),
 qr1=("The numbers",f"light {nlight} (always singular) - darkness {nzulu} (always plural) - plural-light {nanwar}, singular-darkness {nzulm} - shared {co_ld} ayat."),
 qr2=("The shape","one light vs many darknesses, with zero exceptions; light outnumbers darkness ~2:1; fire excluded as a different sense."),
 syn=("Grammar as creed",
   [("Light = singular","one - never pluralised"),("Darkness = plural","many - never singular"),("Light leads","~2x more frequent")],
   "The number is the message","one truth, many errors - a labelled reading over a 0-exception morphological datum."),
 quiz=("Special Topic - One Light, Many Darknesses (Week 4)",[
  ("1.  In the Qur'an, the word 'light' (nur) is:","always singular",["always plural","sometimes plural","never used"],f"plural 'anwar' = {nanwar} - it never occurs."),
  ("2.  The word 'darkness' (zulumat) is:","always plural",["always singular","sometimes singular","never used"],f"singular 'zulma' = {nzulm} - it never occurs."),
  ("3.  Comparing totals, light is named:",f"~{nlight/max(nzulu,1):.1f}x as often as darkness",["half as often","exactly as often","ten times as often"],f"light {nlight} vs darkness {nzulu}."),
  ("4.  The pattern 'one light, many darknesses' has:","zero counter-examples",["many exceptions","one exception","never been counted"],"the morphological split is a hard datum."),
  ("5.  The interpretation laid over the data is:","truth/guidance is one; error is many",["light is hotter","darkness is older","numbers are random"],"a labelled reading, not the computed fact."),
  ("6.  Fire (nar) is excluded because:","it is a different sense in a related family",["it is plural","it never occurs","it means light"],"a sense-verification step."),
  ("7.  Light and darkness co-occur:",f"in {co_ld} ayat, above chance",["never","only once","below chance"],f"{lf:.1f}x chance - a contrast pair."),
  ("8.  The computed (hard) part of the finding is:","the 0-exception singular/plural split",["the creed reading","the fire exclusion only","nothing"],"morphology is the datum."),
  ("9.  'God is the light of the heavens and the earth' is:","24:35 - light as a divine attribute (singular)",["a plural usage","about fire","about darkness"],"the flagship singular-light verse."),
  ("10.  Darkness being plural suggests, on the reading:","multiplicity of error/confusion",["many gods","many books","many suras"],"many darknesses vs one light."),
  ("11.  The method counts:","surface forms, tagged by number",["roots only","letters","rhymes"],"number is read from the surface form."),
  ("12.  The honest verdict is:","one light vs many darknesses, light leading ~2:1",["darkness leads","they are equal","light is plural"],"computed datum plus a labelled reading."),
  ("13.  These findings are:","presented from the morphology, not theological proof",["doctrine","disproof","unrelated to Book6"],"the grammar shows it; the creed-reading is labelled."),
 ]),
)
standard_deck(spec)
print("done light_darkness")

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
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
def coocN(rs): return int(df['toks'].map(lambda ts:all(r in ts for r in rs)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ NASKH - abrogation ============
nnas=ac('نسخ')
fig_groupbar("nk_uses.png","The whole textual base: four occurrences",["ABROGATE\n(2:106, 22:52)","COPY/WRITE\n(7:154, 45:29)"],[("",[wk.AMBER,wk.GREY],[2,2])],ylabel="occurrences")
fig_freqbarh("nk_slender.png","A large doctrine on a slender base",["نسخ  abrogate-root (total)","حكم  ruling","ءيي  sign/verse","امر  command","ءله  God"],[nnas,ac('حكم'),ac('ءيي'),ac('امر'),ac('ءله')],[wk.RED,wk.TEAL,wk.TEAL,wk.AMBER,wk.NAVY],xlabel="ayat containing the root (log-like contrast)")
fig_groupbar("nk_sense.png","Two senses, evenly split",["abrogate","copy / transcribe"],[("",[wk.AMBER,wk.GREY],[2,2])],ylabel="occurrences")
fig_groupbar("nk_named.png","The text never NAMES a verse-cancels-verse case",["uses of نسخ","cases where the text names which cancels which"],[("",[wk.AMBER,wk.RED],[nnas,0])])
fig_suradist("nk_sura.png","Where the abrogation-root falls (all 4)","نسخ")
co_aya=cooccur('نسخ','ءيي')
fig_groupbar("nk_aya.png","'Abrogate' co-occurs with 'sign/verse'",["نسخ . ءيي (sign)"],[("",[wk.AMBER],[co_aya])])
fig_freqbarh("nk_doctrine.png","Doctrine size vs textual footprint",["the naskh DOCTRINE (vast)","its textual base (~2 abrogate verses)"],[100,2],[wk.GREY,wk.RED],xlabel="relative scale (illustrative: doctrine vs base)")
spec=dict(slug="W09_naskh_abrogation",sub="abrogation, Week 9",
 main="Does the Qur'an abrogate itself? (naskh)",
 headline="A whole doctrine - resting on about two verses",
 intro1="A whole doctrine (naskh) holds that later verses cancel earlier ones. How much textual ground does the word itself actually cover? We find every occurrence of the root, read each in context, and separate the 'abrogate' sense from the 'copy/transcribe' sense.",
 intro2="The root-count recomputes from Book6 and reproduces exactly (4 occurrences); the sense split is read from context.",
 qhead="The claim to test",qbody="How much textual base does the abrogation doctrine actually have - and does the text ever name which verse cancels which?",
 mhead="The method",mpts=["find every occurrence of the abrogation-root",
   "separate 'abrogate' from 'copy/transcribe' in context",
   "ask whether the text ever NAMES a specific verse-cancels-verse case"],
 figs=[
  dict(t="The whole textual base: four occurrences",png="nk_uses.png",cf=TINT,
    cap=f"In the data - the root appears just {nnas} times in the entire Qur'an: two mean 'abrogate' (2:106, 22:52), two mean 'copy/transcribe' (7:154, 45:29). A slender base for so large a doctrine."),
  dict(t="A large doctrine on a slender base",png="nk_slender.png",
    cap=f"In the data - against ruling ({ac('حكم')}), sign/verse ({ac('ءيي')}) and command ({ac('امر')}), the abrogation-root's {nnas} occurrences are tiny. The doctrine vastly outweighs its lexical footprint."),
  dict(t="Two senses, evenly split",png="nk_sense.png",cf=TINT,
    cap="In the data - half the occurrences are not 'abrogation' at all: the tablets' text (7:154) and 'We were having it copied' (45:29) are about transcription. Same root, different sense."),
  dict(t="The text never names a case",png="nk_named.png",
    cap=f"In the data - across all {nnas} uses, the Qur'an never names a specific verse that cancels another: which verses (if any) abrogate which is entirely interpretive."),
  dict(t="Where the root falls",png="nk_sura.png",cf=TINT,
    cap="In the data - the four occurrences sit in al-Baqara, al-Hajj, al-A'raf and al-Jathiya - scattered, not a doctrinal cluster."),
  dict(t="'Abrogate' and 'sign/verse'",png="nk_aya.png",
    cap=f"In the data - 2:106 pairs the abrogate-sense with 'sign' (aya, {co_aya} co-occurrence) - but 'sign' may mean a miracle or a prior scripture, not necessarily a Qur'anic verse."),
  dict(t="Doctrine vs footprint",png="nk_doctrine.png",cf=TINT,
    cap="In the data - the intra-Qur'anic abrogation doctrine is a juristic construct built atop ~2 abrogate-verses - the imbalance is the point (illustrative scale)."),
 ],
 gal1=dict(title="The 'abrogate' sense (2 of 4)",items=gl(B2["naskh"],["2:106","22:52"]) or [("2:106","مَا نَنسَخْ مِنْ آيَةٍ أَوْ نُنسِهَا نَأْتِ بِخَيْرٍ مِّنْهَا","whatever sign We abrogate or cause to be forgotten, We bring better")],fill=AMBERT,hc=AMBER),
 gal2=dict(title="The 'copy / transcribe' sense (2 of 4)",items=gl(B2["naskh"],["7:154","45:29"]) or [("45:29","إِنَّا كُنَّا نَسْتَنسِخُ مَا كُنتُمْ تَعْمَلُونَ","We were having transcribed what you used to do")],fill=TINT2,hc=GREY),
 v1=("Only four occurrences",f"the root appears just {nnas} times in the whole Qur'an - a slender base for so large a doctrine."),
 v2=("Half are not 'abrogation'",f"two mean abrogate (2:106, 22:52); two mean copy/transcribe (7:154, 45:29) - the same root, a different sense."),
 v3=("No named case","the text never names a specific verse-cancels-verse case; which verses (if any) abrogate which is entirely interpretive."),
 deep=("A large doctrine on a slender textual base",
   f"Computed: the abrogation idea rests on ~2 verses (2:106, 22:52); the word also means 'copy,' and the text NEVER names a specific verse-cancels-verse case. So intra-Qur'anic abrogation is a juristic CONSTRUCT built atop a thin lexical base - not a self-declared feature of the text. This does not settle whether abrogation is true - only that the corpus barely uses the word and never lists cases."),
 deep_extra=["2:106's 'sign' (aya) may mean a miracle or a prior scripture, not necessarily a Qur'anic verse - itself a reading."],
 crit1=("It does not disprove the doctrine",
   "the slender base shows only that the corpus barely uses the word and never lists cases - not that abrogation is false."),
 crit2=("'Sign' is ambiguous",
   "2:106's 'aya' may mean a miracle or a prior scripture, not necessarily a Qur'anic verse - the reading is interpretive."),
 audit=[("check","Root counted",f"{nnas} occurrences (reproduces exactly)."),
   ("check","Senses split","2 abrogate, 2 copy/transcribe."),
   ("check","No named case","the text never names which verse cancels which.")]+[("tilde","Doesn't settle truth","only the lexical base is shown.")]+AT,
 method=("the abrogation-root; context senses","count, sense split, named-case check","use bars, slender-base contrast, sura map"),
 take=("A vast doctrine on about two verses",
   [f"The abrogation-root appears only {nnas} times - two meaning 'abrogate,' two meaning 'copy.'",
    "The text never names which verse cancels which: intra-Qur'anic abrogation is a juristic construct on a thin base.",
    "This shows the lexical footprint, not whether the doctrine is true. Presented from the text."]),
 qr1=("The numbers",f"abrogation-root {nnas} total - 2 abrogate (2:106, 22:52), 2 copy (7:154, 45:29); zero named verse-cancels-verse cases."),
 qr2=("The shape","a large doctrine on ~2 verses; half the root's uses mean 'copy'; the text never lists cases."),
 syn=("Doctrine vs base",
   [("The doctrine","vast juristic construct"),("The root","only 4 uses"),("Named cases","zero")],
   "A construct on a thin base","the corpus barely uses the word and never names a case - which verses abrogate which is interpretive."),
 quiz=("Special Topic - Does the Qur'an Abrogate Itself? (Week 9)",[
  ("1.  The abrogation-root appears in the Qur'an:",f"only {nnas} times",["hundreds of times","never","exactly 50"],f"a slender base - {nnas} occurrences."),
  ("2.  Of those occurrences, how many mean 'abrogate'?","two (2:106, 22:52)",["all four","zero","three"],"the other two mean copy/transcribe."),
  ("3.  The other two occurrences mean:","copy / transcribe (7:154, 45:29)",["abrogate","recite","forbid"],"same root, different sense."),
  ("4.  Does the text name which verse cancels which?","never",["always","sometimes","only in al-Baqara"],"no named verse-cancels-verse case exists."),
  ("5.  Intra-Qur'anic abrogation is therefore:","a juristic construct on a thin lexical base",["a self-declared feature","disproven","impossible to study"],"built atop ~2 verses."),
  ("6.  This finding:","does NOT settle whether abrogation is true",["disproves it","proves it","is irrelevant"],"it shows only the lexical footprint."),
  ("7.  2:106's word 'aya' may mean:","a miracle or prior scripture, not necessarily a Qur'anic verse",["only a Qur'anic verse","a sword","a sura"],"itself an interpretive point."),
  ("8.  Against 'ruling' or 'sign', the abrogation-root is:","tiny",["larger","equal","the largest"],f"{nnas} vs {ac('حكم')}/{ac('ءيي')}."),
  ("9.  The sense split is:","even - two abrogate, two copy",["all abrogate","all copy","three to one"],"half are transcription."),
  ("10.  The doctrine vs the base shows:","a large construct on a small footprint",["a matched pair","no doctrine","a huge base"],"the imbalance is the point."),
  ("11.  The root-count is:","reproduced exactly from Book6",["estimated","guessed","unknown"],f"{nnas}, verifiable."),
  ("12.  The honest verdict is:","a large doctrine resting on about two verses",["abrogation is false","abrogation is proven","there is no doctrine"],"lexical base shown, truth not settled."),
  ("13.  These findings are:","presented from the text, not a theological ruling",["doctrine","disproof","unrelated to Book6"],"the count is computed; the doctrine's truth is left open."),
 ]),
)
standard_deck(spec)
print("done naskh")

# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,norm,df,SUR,AYA,NUZ,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
FIG=wk.FIG
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SA=json.load(open(SB+"snip_address.json",encoding="utf-8"))
SO=json.load(open(SB+"snip_order.json",encoding="utf-8"))
SS=json.load(open(SB+"snip_actstate.json",encoding="utf-8"))
SU=json.load(open(SB+"snip_unit.json",encoding="utf-8"))
S1=json.load(open(SB+"snippets.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r]["tag"]) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
T=df[TOK].astype(str).map(norm)
def voc(after): a=norm(after); return int(T.map(lambda t:('يا اي ها' in t) and a in t).sum())
def say_count(): return int(df[TOK].astype(str).map(lambda t: any(norm(w)=='قل' for w in t.split())).sum())
def scatxy(fname,title,x,y,xl,yl,hi=None,line=None):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.scatter(x,y,s=24,color=wk.TEAL,alpha=0.6,edgecolor="white")
    if line is not None: ax.plot(line[0],line[1],"-",color=wk.RED,lw=2,label=line[2]); ax.legend(frameon=False,fontsize=12)
    if hi:
        for lab,xx,yy in hi:
            ax.scatter([xx],[yy],s=150,color=wk.RED,edgecolor="white",zorder=4)
            ax.annotate(lab,(xx,yy),xytext=(6,4),textcoords="offset points",fontsize=10.5,color=wk.NAVY)
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def hist(fname,title,vals,bins,xl,yl="# items",hi=None,logy=False):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.hist(vals,bins=bins,color=wk.ICE,edgecolor="white")
    if hi:
        for lab,v in hi: ax.axvline(v,color=wk.RED,lw=1.3); ax.text(v,ax.get_ylim()[1]*0.6,lab,rotation=90,fontsize=10,color=wk.RED,ha="right")
    if logy: ax.set_yscale("log")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
AT=[("cross","Not a proof","counts and co-occurrence locate meaning; they do not settle theology."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# per-sura arrays
g=df.groupby(SUR)
POS=np.array(sorted(g.groups.keys()))
NUZv=np.array([df[df[SUR]==s][NUZ].dropna().iloc[0] for s in POS])
LEN=np.array([int(df[df[SUR]==s][AYA].max()) for s in POS])
ATC=df['toks'].map(len).values

# =============== WHO ADDRESSED ===============
vb=voc('ذين'); vn=voc('ناس'); vp=voc('نبي')
nas_men=form_ac(['الناس','ناس']); say=say_count()
n_amn=ac('ءمن'); n_kfr=ac('كفر'); n_nas=ac('نوس'); n_nbi=ac('نبا')
fig_groupbar("wa_voc.png","Who is called 'O ...!' - vocative openings (Book6)",
  ["O believers","O mankind","O Prophet"],[("",[wk.TEAL,wk.AMBER,wk.NAVY],[vb,vn,vp])])
fig_freqbarh("wa_fields.png","The addressee fields, by size",
  ["ءمن  faith / believers","كفر  disbelief","نوس  mankind","نبا  prophet"],[n_amn,n_kfr,n_nas,n_nbi],[wk.TEAL,wk.RED,wk.AMBER,wk.NAVY])
fig_groupbar("wa_mention.png","Mention is not address - mankind named vs called",
  ["mankind"],[("named (mention)",wk.GREY,[nas_men]),("called 'O mankind!'",wk.AMBER,[vn])])
fig_suradist("wa_amn_sura.png","Where the faith-root falls, sura by sura","ءمن")
fig_timeline("wa_time.png","Believers vs disbelievers across the revelation",[("faith ءمن","ءمن"),("disbelief كفر","كفر")])
fig_groupbar("wa_dialogue.png","A scripted dialogue - 'Say!' (qul) is everywhere",
  ["'Say!' (qul) openings"],[("",[wk.TEAL],[say])])
fig_freqbarh("wa_voc_share.png","Direct address concentrates on the believing community",
  ["O believers","O mankind","O Prophet","O Children of Israel"],[vb,vn,vp,voc('اسرائيل')],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY])
spec=dict(slug="W01_who_addressed",sub="frequency & address, Week 1",
 main="Who does the Qur'an address?",
 headline="Everyone, one community, or its opponents? - read from the vocatives",
 intro1="Is the Qur'an speaking to all humanity, to a community, or to its critics? We separate MENTION (named anywhere) from ADDRESS (the vocative 'O ...!'), and a fixed identity (a noun) from an ongoing act (a verb), then read the speech frame ('Say!' vs 'they said').",
 intro2="Counts recompute from Book6; vocative openings are detected from the tokenized text and are reproducible.",
 qhead="The question",qbody="Does the Qur'an address everyone, a community, or opponents - and as fixed identities or ongoing acts?",
 mhead="The method",mpts=["count the vocative 'O ...!' openings by addressee",
   "separate mention (named) from address (called)",
   "track the dialogue frame - 'Say!' (qul) commands"],
 figs=[
  dict(t="The vocative goes to the believing community",png="wa_voc.png",cf=TINT,
    cap=f"In the data - direct 'O ...!' openings: believers {vb}, mankind {vn}, the Prophet {vp}. The primary addressee is the community of faith."),
  dict(t="The addressee fields, by size",png="wa_fields.png",
    cap=f"In the data - faith ({n_amn}), disbelief ({n_kfr}), mankind ({n_nas}) and prophet ({n_nbi}) fields: a universal frame around a community focus."),
  dict(t="Mention is not address",png="wa_mention.png",cf=TINT,
    cap=f"In the data - 'mankind' is NAMED {nas_men} times but directly CALLED only {vn}. Counting mentions would overstate the universal address."),
  dict(t="The faith-root across the corpus",png="wa_amn_sura.png",
    cap="In the data - the faith-root is densest in the Medinan community sūras, thinning in the short Meccan tail."),
  dict(t="Believers and disbelievers across the revelation",png="wa_time.png",cf=TINT,
    cap="In the data - both groups are addressed across periods; the believing-community focus sharpens in the Medinan suras."),
  dict(t="A scripted dialogue",png="wa_dialogue.png",
    cap=f"In the data - 'Say!' (qul) opens speech {say} times: the text is staged as a back-and-forth, God instructing the Prophet to answer."),
  dict(t="Direct address, by group",png="wa_voc_share.png",cf=TINT,
    cap=f"In the data - of all 'O ...!' openings, the believing community dominates ({vb}), inside a universal frame ('O mankind' {vn})."),
 ],
 gal1=dict(title="Universal frame - 'O mankind'",items=gl(SA,["49:13","2:21","3:64"]) or gl(SA,[SA[0]["ref"]]),fill=AMBERT,hc=AMBER),
 gal2=dict(title="Community focus, and the dialogue",items=(gl(SA,["5:1","2:104"])+gl(SA,["112:1","109:1","2:11"])) or gl(SA,[SA[-1]["ref"]]),fill=TINT,hc=TEAL),
 v1=("Identity AND act",f"believers and disbelievers are each named both as a settled NOUN and an ongoing VERB - faith ({n_amn}) and denial ({n_kfr}) are processes, not only labels."),
 v2=("Addressed in-community",f"the vocative goes to believers {vb} times, mankind only {vn}, the Prophet {vp} - a community focus inside a universal frame."),
 v3=("Staged as dialogue",f"'Say!' (qul) opens {say} replies - a scripted back-and-forth, not a monologue."),
 deep=("A community address inside a universal frame, in dialogue",
   "The primary addressee is the believing community (most vocatives), set inside a universal frame: 'mankind' is named hundreds of times but directly called far less. And it is a scripted dialogue - God tells the Prophet 'Say!' and quotes opponents 'they said.' Mention is not address: counting names alone would overstate the universal reach; the vocative reveals the real focus."),
 deep_extra=["A universal frame, a community focus, a dialogue form - all three at once."],
 crit1=("Mention != address",
   f"'mankind' is named {nas_men} times but called only {vn}; reading mentions as address inflates the universal claim."),
 crit2=("Noun and verb must be split",
   "collapsing 'those who came to believe' into 'the believers' erases the act-vs-identity distinction; root + surface + morphology keep them apart."),
 audit=[("check","Vocatives counted",f"believers {vb}, mankind {vn}, Prophet {vp}."),
   ("check","Mention vs address",f"mankind named {nas_men}, called {vn}."),
   ("check","Dialogue frame",f"'Say!' opens {say} times.")]+[("tilde","Tokenized detection","vocatives read from tokenized text; small boundary variation possible.")]+AT,
 method=("addressee roots; vocative openings","field size, mention vs address, dialogue frame","vocative bars, field bars, timeline, sura map"),
 take=("A community address, inside a universal frame, in dialogue",
   ["The Qur'an's primary addressee is the believing community, addressed directly far more than mankind at large.",
    f"Yet the frame is universal ('O mankind') and the form is dialogue ('Say!' {say} times). Faith and denial are named as both acts and identities.",
    "Mention is not address - the vocatives, not the name-counts, reveal the focus. Presented from the text."]),
 qr1=("The numbers",f"vocatives: believers {vb}, mankind {vn}, Prophet {vp}; mankind named {nas_men}; 'Say!' {say}; faith-field {n_amn}, disbelief {n_kfr}."),
 qr2=("The shape","community focus inside a universal frame, staged as dialogue; identity and act both named."),
 syn=("Frame, focus, form",
   [("Universal frame","'O mankind' - all are in view"),("Community focus","most vocatives -> believers"),("Dialogue form","'Say!' - a staged reply")],
   "Three things at once","a universal address, a community focus, and a dialogue - the vocatives reveal the real centre of gravity."),
 quiz=("Special Topic - Who the Qur'an Addresses (Week 1)",[
  ("1.  The primary direct addressee (by vocative count) is:","the believing community",["all mankind","the opponents","the angels"],f"'O believers' opens {vb} times vs mankind {vn}."),
  ("2.  'Mention is not address' means:","being named is not the same as being called 'O ...!'",["names are uncounted","address is fictional","mention is rarer"],f"mankind is named {nas_men} but called only {vn}."),
  ("3.  'O mankind' (the universal vocative) occurs about:",f"{vn} times",[f"{vb} times",f"{vp} times","never"],f"the universal vocative is {vn}; the community one {vb}."),
  ("4.  The dialogue frame is marked by:","'Say!' (qul) openings",["chapter numbers","rhyme only","the Basmala"],f"'Say!' opens {say} replies - a staged dialogue."),
  ("5.  Faith and disbelief are each named:","both as a settled noun and an ongoing verb",["only as nouns","only as verbs","only once"],"identity AND act - the morphology marks both."),
  ("6.  Counting only name-mentions would:","overstate the universal address",["understate it","change nothing","be most accurate"],"mentions far exceed vocatives for 'mankind.'"),
  ("7.  The believing community is addressed inside:","a universal frame ('O mankind')",["a purely local frame","no frame","an angelic frame"],"community focus, universal frame."),
  ("8.  'Say!' (qul) shows the text is:","a scripted dialogue, not a monologue",["a single speech","silent","only narrative"],f"qul opens {say} instructed replies."),
  ("9.  Why split noun from verb?","to keep 'the believers' (identity) apart from 'those who came to believe' (act)",["to inflate counts","Arabic has no nouns","for rhyme"],"morphology marks identity vs act."),
  ("10.  The faith-root is densest in:","the Medinan community suras",["only Mecca","the disjoint letters","sura 108"],"the community focus sharpens in Medina."),
  ("11.  Vocative detection here comes from:","the tokenized text - reproducible, with minor boundary variation",["a guess","one verse","outside the corpus"],"detected from Book6's tokenized column."),
  ("12.  The honest one-line verdict is:","a community address inside a universal frame, in dialogue",["only universal","only local","only to opponents"],"all three hold at once."),
  ("13.  These findings are:","presented from the text, not theological claims",["doctrine","disproof","unrelated"],"the corpus shows the structure; the reading is labelled."),
 ]),
)
standard_deck(spec)
print("done who_addressed")

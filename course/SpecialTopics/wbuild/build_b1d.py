# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df,SUR,AYA,NUZ,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
FIG=wk.FIG
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SO=json.load(open(SB+"snip_order.json",encoding="utf-8"))
SS=json.load(open(SB+"snip_actstate.json",encoding="utf-8"))
SU=json.load(open(SB+"snip_unit.json",encoding="utf-8"))
S1=json.load(open(SB+"snippets.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r]["tag"]) for r in refs if r in d]
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
def scatxy(fname,title,x,y,xl,yl,hi=None,line=None,corr=None):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.scatter(x,y,s=24,color=wk.TEAL,alpha=0.6,edgecolor="white")
    if line is not None: ax.plot(line[0],line[1],"-",color=wk.RED,lw=2,label=line[2]); ax.legend(frameon=False,fontsize=12)
    if hi:
        for lab,xx,yy in hi:
            ax.scatter([xx],[yy],s=150,color=wk.RED,edgecolor="white",zorder=4)
            ax.annotate(lab,(xx,yy),xytext=(6,4),textcoords="offset points",fontsize=10.5,color=wk.NAVY)
    if corr is not None: ax.text(0.02,0.96,corr,transform=ax.transAxes,fontsize=13,color=wk.NAVY,va="top",fontweight="bold")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def hist(fname,title,vals,bins,xl,yl="# items",hi=None,logy=False):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.hist(vals,bins=bins,color=wk.ICE,edgecolor="white")
    if hi:
        for lab,v in hi: ax.axvline(v,color=wk.RED,lw=1.3); ax.text(v,ax.get_ylim()[1]*0.55,lab,rotation=90,fontsize=10,color=wk.RED,ha="right")
    if logy: ax.set_yscale("log")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def barfull(fname,title,xs,ys,xl,yl,hi=None):
    fig,ax=plt.subplots(figsize=(11,4.8))
    cols=[wk.RED if (hi and s in hi) else wk.TEAL for s in xs]
    ax.bar(xs,ys,color=cols,width=0.9,edgecolor="none")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
AT=[("cross","Not a proof","counts locate structure; they do not settle theology or 'why'."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]
g=df.groupby(SUR); POS=np.array(sorted(g.groups.keys()))
NUZv=np.array([df[df[SUR]==s][NUZ].dropna().iloc[0] for s in POS])
LEN=np.array([int(df[df[SUR]==s][AYA].max()) for s in POS])
ATC=df['toks'].map(len).values
corr_pn=np.corrcoef(POS,NUZv)[0,1]; corr_pl=np.corrcoef(POS,LEN)[0,1]
QL=[LEN[(POS>=q*28.5+1)&(POS<(q+1)*28.5+1)].mean() for q in range(4)]

# =============== MUSHAF ORDER ===============
land=[("al-Fatiha",1,5),("al-Baqara",2,87),("al-Alaq",96,1),("al-Tawba",9,114)]
scatxy("mo_posnuz.png","Canonical position vs revelation order - no timeline",POS,NUZv,
  "mushaf position (1-114)","revelation order",hi=[(n,p,nz) for n,p,nz in land],corr=f"corr = {corr_pn:+.2f}")
scatxy("mo_poslen.png","Canonical position vs sura length - graded by size",POS,LEN,
  "mushaf position (1-114)","sura length (ayat)",corr=f"corr = {corr_pl:+.2f}")
fig_groupbar("mo_quarters.png","Average sura length falls across the mushaf quarters",
  ["Q1 (1-29)","Q2 (30-57)","Q3 (58-86)","Q4 (87-114)"],[("",[wk.NAVY,wk.TEAL,wk.LT,wk.GREY],[round(x) for x in QL])],ylabel="avg ayat")
fig_groupbar("mo_land.png","Landmark suras: position vs when revealed",
  [n for n,_,_ in land],[("mushaf #",wk.TEAL,[p for _,p,_ in land]),("revelation #",wk.AMBER,[nz for _,_,nz in land])])
barfull("mo_lenbypos.png","The whole mushaf, longest-first",POS,LEN,"mushaf position (1-114)","sura length (ayat)")
hist("mo_nuzbyq.png","Late mushaf positions hold the EARLY-revealed short suras",NUZv,np.arange(0,116,8),"revelation order","# suras")
scatxy("mo_lennuz.png","Length, not time, drives placement",NUZv,LEN,"revelation order","sura length (ayat)")
spec=dict(slug="W02_mushaf_vs_revelation",sub="distribution, Week 2",
 main="Why the Qur'an's order is not its revelation order",
 headline="A non-chronological arrangement - what rule governs it instead?",
 intro1="The Qur'an was revealed over ~23 years, but its written (mushaf) order is not chronological. Using the revelation-order index in Book6, we compare canonical position against timing and length to find the organizing rule.",
 intro2="Correlations and quarter-averages recompute from Book6; revelation rank is per-sura (narrated, not computed) - a stated limit.",
 qhead="The question",qbody="If not chronology, what rule sets the order of the 114 suras?",
 mhead="The method",mpts=["correlate canonical position with revelation order and with length",
   "bin the mushaf into quarters; read average length",
   "track landmark suras (first/last revealed) against their position"],
 figs=[
  dict(t="Position carries no chronology",png="mo_posnuz.png",cf=TINT,
    cap=f"In the data - canonical position vs revelation order correlates only {corr_pn:+.2f}: the arrangement is essentially non-chronological. al-Alaq (revealed 1st) sits at 96; al-Tawba (last) at 9."),
  dict(t="It is graded by length",png="mo_poslen.png",
    cap=f"In the data - position vs sura length correlates {corr_pl:+.2f}: a strong descending-length gradient. Length, not time, is the visible rule."),
  dict(t="Quarter by quarter, length falls",png="mo_quarters.png",cf=TINT,
    cap=f"In the data - average length drops {round(QL[0])} -> {round(QL[1])} -> {round(QL[2])} -> {round(QL[3])} ayat across the four mushaf quarters. The longest suras open; the shortest close."),
  dict(t="The first revealed becomes the 96th",png="mo_land.png",
    cap="In the data - al-Fatiha (#1) was revealed 5th; al-Baqara (#2) 87th; al-Alaq ('Read!', 1st revealed) sits at 96; al-Tawba (last) at 9. Position encodes no timeline."),
  dict(t="The whole mushaf, longest-first",png="mo_lenbypos.png",cf=TINT,
    cap="In the data - the length profile descends across the codex, with al-Fatiha the short opening exception. Longest-first is a tendency, not an absolute law."),
  dict(t="The early-revealed short suras cluster late",png="mo_nuzbyq.png",
    cap="In the data - the short, early-Meccan suras are gathered at the END of the codex - the opposite of chronological order."),
  dict(t="Length, not time, drives placement",png="mo_lennuz.png",cf=TINT,
    cap="In the data - length shows no clean trend with revelation order; the codex is sorted by size, and the timeline is scrambled within it."),
 ],
 gal1=dict(title="First and last revealed",items=gl(SO,["96:1","9:1"]) or gl(SO,[SO[0]["ref"]]),fill=AMBERT,hc=AMBER),
 gal2=dict(title="The opening of the codex, and short suras placed late",items=(gl(SO,["1:2","2:1"])+gl(SO,["108:1","110:1"])) or gl(SO,[SO[-1]["ref"]]),fill=TINT,hc=TEAL),
 v1=("Non-chronological",f"position vs revelation correlates only {corr_pn:+.2f} - the order is not a biography."),
 v2=("Graded by length",f"position vs length correlates {corr_pl:+.2f}; quarter averages fall {round(QL[0])} -> {round(QL[3])} ayat."),
 v3=("Thematic / liturgical","tradition holds the arrangement was prophet-directed and recitational - a structure, not a timeline (labelled, historical)."),
 deep=("A thematic order, not a timeline",
   f"The canonical order is essentially non-chronological (corr {corr_pn:+.2f}) and graded by descending length (corr {corr_pl:+.2f}), clustering the short early-Meccan suras at the very end. The data shows the SHAPE - longest-first; the REASON (a prophet-directed, liturgical arrangement) lies outside the text and is a narrated, historical claim, not a computed one."),
 deep_extra=["The codex maps WHAT the order is; it declines to compute WHY."],
 crit1=("Length is a tendency, not a law",
   "al-Fatiha is short yet first - an opening, not the longest. 'Longest-first' is strong but imperfect."),
 crit2=("Revelation order is narrated",
   "the timeline comes from sira and ahadith, only at the sura level (Meccan/Medinan verses mix within a sura) - so the chronology itself is an approximation."),
 audit=[("check","Correlations computed",f"position-revelation {corr_pn:+.2f}, position-length {corr_pl:+.2f}."),
   ("check","Quarter trend",f"avg length {round(QL[0])}->{round(QL[3])} ayat."),
   ("check","Landmarks placed","al-Alaq 1st->#96; al-Tawba last->#9.")]+[("tilde","Sura-level only","revelation rank is per-sura, narrated, not computed.")]+AT,
 method=("revelation-order index; sura lengths","correlations, quarter-averages, landmarks","scatter plots, quarter bars, length profile"),
 take=("A codex sorted by size, not by time",
   [f"The Qur'an's order is non-chronological (corr {corr_pn:+.2f}) and graded by descending length (corr {corr_pl:+.2f}).",
    "The first revealed sura sits at position 96; the last, at 9; the short early-Meccan suras are gathered at the end.",
    "We map WHAT the order is - longest-first - and decline to compute WHY (a narrated, liturgical reason). Presented from the data."]),
 qr1=("The numbers",f"position-revelation corr {corr_pn:+.2f}; position-length corr {corr_pl:+.2f}; quarter avg length {round(QL[0])}/{round(QL[1])}/{round(QL[2])}/{round(QL[3])}."),
 qr2=("The shape","graded by descending length; non-chronological; short early-Meccan suras placed last; reason is narrated, not computed."),
 syn=("What, not why",
   [("Revealed over ~23 yrs","a chronology exists"),("Codex sorts by length","longest-first gradient"),("Order is thematic","narrated, liturgical - outside the text")],
   "The data gives the shape","longest-first, non-chronological; the reason is a historical, narrated claim we do not compute."),
 quiz=("Special Topic - Mushaf vs Revelation Order (Week 2)",[
  ("1.  The Qur'an's written order is:","essentially non-chronological",["exactly chronological","reverse-chronological","random with no pattern"],f"position-revelation correlates only {corr_pn:+.2f}."),
  ("2.  The visible organizing rule is:","descending sura length",["date of revelation","alphabetical","number of letters"],f"position-length correlates {corr_pl:+.2f}."),
  ("3.  Average sura length across the four quarters:","falls steadily (long -> short)",["rises","stays flat","is random"],f"{round(QL[0])} -> {round(QL[3])} ayat."),
  ("4.  al-Alaq ('Read!'), revealed FIRST, sits at position:","96",["1","5","114"],"the first revealed is placed 96th - no chronology."),
  ("5.  al-Tawba, revealed LAST, sits at position:","9",["114","1","96"],"the last revealed is placed 9th."),
  ("6.  al-Fatiha is the exception because it is:","short yet placed first (an opening)",["the longest","revealed last","not a sura"],"longest-first is a tendency, not a law."),
  ("7.  The short early-Meccan suras are gathered:","at the END of the codex",["at the start","in the middle","evenly"],"the opposite of chronological order."),
  ("8.  The reason for the order is:","narrated / liturgical - outside the text",["computed from the data","alphabetical","unknown and uncheckable"],"tradition holds it prophet-directed; we map what, not why."),
  ("9.  Revelation rank in Book6 is given:","per sura, from narration (not computed)",["per ayah, computed","per letter","not at all"],"Meccan/Medinan verses can mix within a sura."),
  ("10.  The position-vs-length correlation is best called:","strong and negative (longer suras come first)",["weak and positive","exactly zero","perfectly 1.0"],f"corr {corr_pl:+.2f}."),
  ("11.  'Longest-first' is described as:","a strong tendency, not an absolute law",["an exact law","false","irrelevant"],"al-Fatiha breaks it as the opening."),
  ("12.  The honest verdict is:","a thematic order graded by length, not a timeline",["a strict diary","alphabetical","meaningless"],"shape computed; reason narrated."),
  ("13.  These findings are:","presented from the data; the 'why' is labelled historical",["proof of doctrine","disproof","unrelated to Book6"],"we compute what the order is, not why."),
 ]),
)
standard_deck(spec)
print("done mushaf_order")

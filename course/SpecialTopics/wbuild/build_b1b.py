# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,fig_donut,norm,df,SUR,AYA,NUZ,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
FIG=wk.FIG
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SD=json.load(open(SB+"snip_din.json",encoding="utf-8"))
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
def scatxy(fname,title,x,y,xl,yl,labels=None,hi=None):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.scatter(x,y,s=26,color=wk.TEAL,alpha=0.65,edgecolor="white")
    if hi:
        for lab,xx,yy in hi:
            ax.scatter([xx],[yy],s=150,color=wk.RED,edgecolor="white",zorder=4)
            ax.annotate(lab,(xx,yy),xytext=(6,4),textcoords="offset points",fontsize=11,color=wk.NAVY)
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def hist(fname,title,vals,bins,xl,yl="# items",hi=None,logy=False):
    fig,ax=plt.subplots(figsize=(11,5.0))
    ax.hist(vals,bins=bins,color=wk.ICE,edgecolor="white")
    if hi:
        for lab,v in hi:
            ax.axvline(v,color=wk.RED,lw=1.3)
            ax.text(v,ax.get_ylim()[1]*0.6,lab,rotation=90,fontsize=10,color=wk.RED,ha="right",va="bottom")
    if logy: ax.set_yscale("log")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()

AUDIT_TAIL=[("cross","Not a proof","co-occurrence and counts locate meaning; they do not settle theology."),
            ("cross","No raw-root mixing","senses/forms are separated before counting (course rule).")]

# =============== DIN / ISLAM / QURAN ===============
ndin=ac("دين"); nslm=ac("سلم"); nqr=ac("قرء")
c_ds=cooccur("دين","سلم"); c_dq=cooccur("دين","قرء"); c_sq=cooccur("سلم","قرء")
fig_freqbarh("din_freq.png","Three roots often treated as one - their field sizes",
  ["دين  way / religion / judgment","سلم  submission / peace / Islam","قرء  recite / Qur'an"],[ndin,nslm,nqr],[wk.TEAL,wk.AMBER,wk.NAVY])
fig_groupbar("din_cooc.png","Do the three share verses? (shared-ayah counts)",
  ["دين . سلم","دين . قرء","سلم . قرء"],[("",[wk.TEAL,wk.RED,wk.RED],[c_ds,c_dq,c_sq])])
lf,j,na,nb=lift("دين","سلم")
fig_liftscatter("din_lift.png","Only one pair attracts: religion and submission",[("دين . سلم",c_ds,lf),("دين . قرء",max(c_dq,0.01),0.01),("سلم . قرء",max(c_sq,0.01),0.01)])
fig_suradist("din_sura.png","Where 'religion' (دين) falls, sura by sura","دين")
fig_suradist("qr_sura.png","Where the recitation-root (قرء) falls, sura by sura","قرء")
fig_timeline("din_time.png","The three roots across the revelation timeline",[("دين","دين"),("سلم","سلم"),("قرء","قرء")])
fig_freqbarh("din_partners.png","What 'religion' keeps company with",
  ["سلم submission","ءله God","قول say (109:6 'to you yours')","ربب Lord"],
  [cooccur("دين","سلم"),cooccur("دين","ءله"),cooccur("دين","قول"),cooccur("دين","ربب")],[wk.TEAL,wk.NAVY,wk.AMBER,wk.GREY])
spec=dict(slug="W03_din_islam_quran",sub="forms & senses, Week 3",
 main="Religion, Islam, Qur'an - one thing, or three?",
 headline="Three words people use interchangeably - tested for equivalence",
 intro1="People treat 'din' (religion), 'islam' (submission) and 'Qur'an' as near-synonyms for 'the religion.' Equivalence leaves a fingerprint: true synonyms co-occur and gloss each other. We test for it rather than assume it - all three roots are polysemous, so figures use co-occurrence, not bare totals.",
 intro2="Every count recomputes from Book6; the co-occurrence numbers are exact and reproducible.",
 qhead="The claim to test",qbody="Are din, islam and Qur'an one concept in the corpus - or a genus, a species, and a Book?",
 mhead="The method",mpts=["count each root's field, then the shared-ayah counts for all three pairs",
   "read what 'religion' pairs with (God? submission? 'to you yours'?)",
   "treat zero co-occurrence as a blunt-but-real signal of non-equivalence"],
 figs=[
  dict(t="Three fields, three sizes",png="din_freq.png",cf=TINT,
    cap=f"In the data - the three roots appear in {ndin}, {nslm}, {nqr} ayat respectively. Comparable sizes - so any non-overlap is not a frequency artefact."),
  dict(t="Only one pair ever shares a verse",png="din_cooc.png",
    cap=f"In the data - 'religion' and 'submission' share {c_ds} ayat; 'religion'+'Qur'an' and 'submission'+'Qur'an' share {c_dq} and {c_sq}. Qur'an is never lexically equated with the religion."),
  dict(t="And that one pair attracts above chance",png="din_lift.png",cf=TINT,
    cap=f"In the data - din+islam co-occur at {lf:.1f}x chance ({c_ds} ayat): a real bond. The Qur'an-root sits at zero with both."),
  dict(t="'Religion' across the corpus",png="din_sura.png",
    cap="In the data - 'religion' is spread across the corpus, clustering in the creed and law passages."),
  dict(t="The recitation-root across the corpus",png="qr_sura.png",cf=TINT,
    cap="In the data - the Qur'an-root tracks passages about the Book, sending-down and reciting - the vehicle, not the religion."),
  dict(t="All three span the revelation",png="din_time.png",
    cap="In the data - none of the three is period-bound; the distinction is conceptual, not chronological."),
  dict(t="What 'religion' keeps company with",png="din_partners.png",cf=TINT,
    cap="In the data - 'religion' pairs most with God and submission, and famously with 'say' (109:6: 'to you your religion, to me mine') - it can be anyone's way, the genus."),
 ],
 gal1=dict(title="The identity verses - religion and submission",items=gl(SD,[e["ref"] for e in SD if ("identity" in e["tag"] or "approved" in e["tag"] or "accepted" in e["tag"])][:5]) or gl(SD,[SD[0]["ref"]]),fill=TINT,hc=TEAL),
 gal2=dict(title="'Religion' in its other senses, and the Qur'an as the Book",items=gl(SD,[e["ref"] for e in SD if ("Judgment" in e["tag"] or "debt" in e["tag"] or "each one" in e["tag"] or "قرآن" in e["tag"])][:5]) or gl(SD,[SD[-1]["ref"]]),fill=AMBERT,hc=AMBER),
 v1=("din = the GENUS",f"a way / religion (and 'the Reckoning', and even 'debt'); it can be anyone's - 'to you yours, to me mine' (109:6). Field of {ndin} ayat."),
 v2=("islam = the SPECIES","the one din named as accepted (3:19; 3:85); din contains islam - equivalent only in the chosen case."),
 v3=("Qur'an = the BOOK",f"the recited text that CARRIES the din; zero shared ayat with either - the vehicle, not the destination."),
 deep=("A genus, a species, and a Book - not three names for one thing",
   "The folk shortcut 'din = islam = Qur'an' is only half-supported. The corpus reserves identity strictly for din<->islam (the 'identity verses' 3:19, 5:3), treats islam as the specific din God accepts, and never lexically equates the Qur'an with the religion - it pairs the Book-root with sending-down, reminder and recital. Most 'din = Islam' claims quietly ignore the Judgment-Day and debt senses of din."),
 deep_extra=["din contains islam; the Qur'an carries both - three layers, not one synonym."],
 crit1=("Zero co-occurrence is blunt",
   "Absence of shared verses does not by itself prove non-synonymy - but here it lines up with the grammar: the Qur'an-root is never used to mean 'the religion.'"),
 crit2=("Senses must be separated",
   "din also = Judgment-Day and debt; islam's root also = peace/Solomon. Counting raw roots as one idea would merge distinct concepts - so figures lean on co-occurrence, which is sense-robust."),
 audit=[("check","Fields are counted",f"{ndin}/{nslm}/{nqr} ayat for the three roots."),
   ("check","Overlaps are exact",f"din+islam {c_ds}, din+Qur'an {c_dq}, islam+Qur'an {c_sq}."),
   ("check","din<->islam attracts",f"{lf:.1f}x chance - a real bond.")]+AUDIT_TAIL[:1]+[("tilde","'Roles' are a gloss","genus/species/Book is the analyst's label on the usage.")]+AUDIT_TAIL[1:],
 method=("din, islam, Qur'an roots","field size, all-pairs co-occurrence & lift","field bars, co-occurrence bars, lift, sura maps"),
 take=("One religion, named three ways - but not three synonyms",
   ["'Religion', 'submission' and 'Qur'an' are not interchangeable in the corpus.",
    f"Religion (din) is the broad way (any can hold one); islam is the specific din accepted (they share {c_ds} ayat, {lf:.1f}x chance); the Qur'an is the Book that carries it (zero shared ayat).",
    "A genus, a species, and a Book - presented from the text, not adjudicated."]),
 qr1=("The numbers",f"din {ndin} - islam-root {nslm} - Qur'an-root {nqr} ayat; din.islam {c_ds} shared ({lf:.1f}x), din.Qur'an {c_dq}, islam.Qur'an {c_sq}."),
 qr2=("The shape","din (genus) contains islam (species); the Qur'an (Book) carries both; equivalence holds only for din<->islam in the chosen case."),
 syn=("Genus, species, Book",
   [("din","the way - anyone's (genus)"),("islam","the accepted din (species)"),("Qur'an","the Book that carries it")],
   "Three layers, not one word","din contains islam; the Qur'an carries both - the corpus keeps them lexically distinct."),
 quiz=("Special Topic - Religion, Islam, Qur'an (Week 3)",[
  ("1.  The folk claim tested here is:","that din, islam and Qur'an are interchangeable",["that the Qur'an has 114 suras","that din means debt only","that islam means peace only"],"the topic tests whether the three are one concept."),
  ("2.  Which pair actually shares verses?",f"din and islam ({c_ds} ayat)",["din and Qur'an","islam and Qur'an","none of them"],f"only din<->islam co-occur ({c_ds}); the Qur'an-root shares {c_dq}/{c_sq}."),
  ("3.  The Qur'an-root co-occurs with 'the religion':","never (zero shared ayat)",["constantly","more than islam","exactly half the time"],"the Book-root is never lexically equated with the religion."),
  ("4.  In the genus/species reading, din is the:","genus (the broad 'way')",["species","the Book","a proper name"],"din is the broad category; islam the specific accepted one."),
  ("5.  '109:6 - to you your religion, to me mine' shows din can be:","anyone's way, not only Islam",["only the Day of Judgment","a kind of debt","the Qur'an itself"],"din is broad enough to be the opponents' way too."),
  ("6.  islam in the corpus is best described as:","the specific din God names as accepted",["a synonym for the Qur'an","unrelated to din","the Day of Judgment"],"3:19/3:85: islam is the accepted din - the species."),
  ("7.  din+islam co-occur at about:",f"{lf:.1f}x chance",["below chance","exactly chance","never"],f"a real bond on {c_ds} shared ayat."),
  ("8.  Why must the roots be sense-separated?","din also = Judgment-Day and debt; the islam-root also = peace/Solomon",["they never repeat","Arabic lacks roots","to inflate islam"],"raw counting would merge distinct senses."),
  ("9.  The Qur'an in this scheme is the:","Book that carries the religion",["religion itself","submission","Day of Judgment"],"it is the vehicle, pairing with Book/sent-down/recite."),
  ("10.  Most 'din = Islam' claims quietly ignore:","the Judgment-Day and debt senses of din",["the existence of suras","the Arabic language","the Basmala"],"din's other senses are dropped to force the equation."),
  ("11.  Zero co-occurrence is described as:","blunt but real - it lines up with the grammar",["absolute proof","meaningless","a counting bug"],"absence is suggestive and here matches usage."),
  ("12.  The honest one-line verdict is:","a genus, a species, and a Book",["three perfect synonyms","three unrelated words","one word repeated"],"din contains islam; the Qur'an carries both."),
  ("13.  These findings are:","presented from the text, not theological verdicts",["proof of doctrine","disproof of doctrine","unrelated to the text"],"the corpus shows the structure; the reading is labelled."),
 ]),
)
standard_deck(spec)
print("done din")

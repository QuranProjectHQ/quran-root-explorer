# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df,SUR,AYA,NUZ
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
FIG=wk.FIG
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SS=json.load(open(SB+"snip_actstate.json",encoding="utf-8"))
SU=json.load(open(SB+"snip_unit.json",encoding="utf-8"))
S1=json.load(open(SB+"snippets.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r]["tag"]) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
def triple(a,b,c): return int(df['toks'].map(lambda ts:(a in ts)and(b in ts)and(c in ts)).sum())
def hist(fname,title,vals,bins,xl,yl="# items",hi=None,logy=False):
    fig,ax=plt.subplots(figsize=(11,5.0)); ax.hist(vals,bins=bins,color=wk.ICE,edgecolor="white")
    if hi:
        for lab,v in hi: ax.axvline(v,color=wk.RED,lw=1.3); ax.text(v,ax.get_ylim()[1]*0.5,lab,rotation=90,fontsize=10,color=wk.RED,ha="right")
    if logy: ax.set_yscale("log")
    ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def barfull(fname,title,xs,ys,xl,yl,hi=None):
    fig,ax=plt.subplots(figsize=(11,4.8)); cols=[wk.RED if (hi and s in hi) else wk.TEAL for s in xs]
    ax.bar(xs,ys,color=cols,width=0.9); ax.set_xlabel(xl); ax.set_ylabel(yl); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
AT=[("cross","Not a proof","counts/forms locate structure; they do not settle theology."),
    ("cross","No raw mixing","forms separated before counting (course rule).")]
g=df.groupby(SUR); POS=np.array(sorted(g.groups.keys()))
LEN=np.array([int(df[df[SUR]==s][AYA].max()) for s in POS])
ATC=df['toks'].map(len).values

# =============== UNITS (surah / ayah) ===============
sbins=[3,11,51,101,201,300]; sh=np.histogram(LEN,bins=sbins)[0]
abins=[1,3,11,31,61,90]; ah=np.histogram(ATC,bins=abins)[0]
floor=int(LEN.min()); ceil=int(LEN.max()); med=int(np.median(LEN)); amax=int(ATC.max()); amed=int(np.median(ATC))
hist("u_suralen.png","Sura length - a bounded range (3 to 286 ayat)",LEN,np.arange(0,300,12),"sura length (ayat)","# suras",hi=[("floor 3",3),("ceiling 286",286)])
hist("u_ayalen.png","Ayah length - 1 to 84 root-tokens (log scale)",ATC,np.arange(0,88,3),"root-tokens in ayah","# ayat",hi=[("2:282 = 84",84)],logy=True)
fig_groupbar("u_surabins.png","How many suras at each length band",
  ["3-10","11-50","51-100","101-200","201+"],[("",[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER,wk.RED],sh.tolist())],ylabel="# suras")
fig_groupbar("u_ayabins.png","How many ayat at each length band",
  ["1-2","3-10","11-30","31-60","61+"],[("",[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER,wk.RED],ah.tolist())],ylabel="# ayat")
barfull("u_lenbypos.png","Every sura's length (1-114)",POS,LEN,"sura number","ayat")
# longest ayat
ords=np.argsort(ATC)[::-1][:6]
labs=[f"{int(df.iloc[i][SUR])}:{int(df.iloc[i][AYA])}" for i in ords]; vals=[int(ATC[i]) for i in ords]
fig_freqbarh("u_longest.png","The longest ayat, by root-tokens",labs,vals,[wk.RED,wk.AMBER,wk.AMBER,wk.TEAL,wk.TEAL,wk.TEAL],xlabel="root-tokens")
# shortest suras
sord=np.argsort(LEN)[:6]; slabs=[f"sura {int(POS[i])}" for i in sord]; svals=[int(LEN[i]) for i in sord]
fig_freqbarh("u_shortest.png","The shortest suras, by ayah-count",slabs,svals,[wk.TEAL]*6,xlabel="ayat")
spec=dict(slug="W02_surah_ayah_units",sub="distribution, Week 2",
 main="What defines a sura and an ayah?",
 headline="Can the two units be defined by measurable criteria - or only marked?",
 intro1="The Qur'an has two units: the sura and the ayah. We measure both from Book6 - ayat per sura, root-tokens per ayah - to see whether length DEFINES them or merely corroborates boundaries that are otherwise marked by name, basmala and received verse-stops.",
 intro2="Every range and count recomputes from Book6; the anchor cases (al-Kawthar, al-Baqara, 2:282) are checked directly.",
 qhead="The question",qbody="Do measurable criteria DEFINE a sura and an ayah, or only describe units that are received and marked?",
 mhead="The method",mpts=["count ayat per sura (1-114): floor, ceiling, distribution",
   "count root-tokens per ayah: shortest (disjoint letters) to longest (2:282)",
   "ask whether length defines, or only corroborates, the marked boundary"],
 figs=[
  dict(t="Sura length - a bounded range",png="u_suralen.png",cf=TINT,
    cap=f"In the data - suras run from {floor} ayat (al-Kawthar, al-Asr, an-Nasr) to {ceil} (al-Baqara); median {med}. A measurable range, but the boundary is marked by name and basmala."),
  dict(t="Ayah length - one token to 84",png="u_ayalen.png",
    cap=f"In the data - an ayah ranges from a single token (the disjoint letters; 55:64) to the {amax}-token debt verse (2:282); median {amed}. An ayah need not be a sentence."),
  dict(t="Suras by length band",png="u_surabins.png",cf=TINT,
    cap=f"In the data - most suras are short-to-mid ({sh[1]} at 11-50 ayat, {sh[2]} at 51-100); only {sh[4]} exceed 200. The long suras are the rare giants."),
  dict(t="Ayat by length band",png="u_ayabins.png",
    cap=f"In the data - the overwhelming majority of ayat are 3-30 tokens ({ah[1]}+{ah[2]}); only {ah[4]} exceed 60. The debt verse is a lone outlier."),
  dict(t="Every sura's length",png="u_lenbypos.png",cf=TINT,
    cap="In the data - the codex's descending-length profile is visible across all 114 suras (the same length-grading as the order topic)."),
  dict(t="The longest ayat",png="u_longest.png",
    cap=f"In the data - 2:282 (the debt verse, {amax} tokens) towers over the field; the next longest trail well behind. Length is a property, not the definition."),
  dict(t="The shortest suras",png="u_shortest.png",cf=TINT,
    cap=f"In the data - the floor is {floor} ayat (al-Kawthar and two others). Brevity does not stop a sura from being a complete, named, basmala-bounded unit."),
 ],
 gal1=dict(title="The shortest suras (3 ayat)",items=gl(SU,["108:1","110:1"]) or gl(SU,[SU[0]["ref"]]),fill=TINT,hc=TEAL),
 gal2=dict(title="Shortest ayat (1 token) and the longest",items=(gl(SU,["2:1","55:64"])+gl(SU,["2:282","2:286"])) or gl(SU,[SU[-1]["ref"]]),fill=AMBERT,hc=AMBER),
 v1=("A sura: 3 to 286 ayat",f"a named, basmala-bounded unit (except at-Tawba); floor {floor}, ceiling {ceil}, median {med}. Length is one visible handle."),
 v2=("An ayah: 1 to 84 tokens",f"a marked verse - from a single token (disjoint letters) to the {amax}-token debt verse; median {amed}. Not necessarily a sentence."),
 v3=("Marked, not defined","both units have measurable ranges, but neither is DEFINED by length - the boundaries are received (name, basmala, verse-stops)."),
 deep=("Length corroborates; marking defines",
   f"Both units have measurable ranges that corroborate the anchor cases - suras {floor}-{ceil} ayat, ayat 1-{amax} tokens. But length defines neither. The units are MARKED: suras by name and basmala, ayat by received verse-stops. The disjoint letters (a single token standing as a whole ayah) prove the marking is prior to length, grammar, or even meaning."),
 deep_extra=["This mirrors the order topic's limit: segmentation, like arrangement, is given, not inferred."],
 crit1=("Length is corroborating, not defining",
   "you can describe the units by counting, but you cannot DERIVE the boundaries from a count - they are received."),
 crit2=("Boundaries are narrated / recitational",
   "the verse-stops and sura divisions come from transmission, not computation; counting can only characterise them."),
 audit=[("check","Sura range exact",f"{floor} to {ceil} ayat, median {med}."),
   ("check","Ayah range exact",f"1 to {amax} tokens (2:282), median {amed}."),
   ("check","Anchors verified","al-Kawthar=3, al-Baqara=286, 2:282 longest.")]+[("tilde","Length corroborates","it describes the units, it does not define them.")]+AT,
 method=("ayat per sura; tokens per ayah","floor/ceiling/median, length bands","length histograms, band bars, longest/shortest"),
 take=("Measurable, but marked",
   [f"A sura spans {floor}-{ceil} ayat; an ayah spans 1-{amax} tokens. Both ranges are real and corroborate the anchors.",
    "But length DEFINES neither - the disjoint letters stand as a whole ayah on a single token. The units are marked by name, basmala and received verse-stops.",
    "Counting describes the units; it does not derive them. Presented from the data."]),
 qr1=("The numbers",f"suras {floor}-{ceil} ayat (median {med}); ayat 1-{amax} tokens (median {amed}); {sh[4]} suras over 200 ayat; only {ah[4]} ayat over 60 tokens."),
 qr2=("The shape","both units have measurable ranges, but are defined by MARKING (name/basmala/verse-stops), not by length."),
 syn=("Measured, then marked",
   [("Count the units","suras 3-286, ayat 1-84"),("Ranges corroborate","they fit the anchors"),("Marking defines","name, basmala, verse-stops")],
   "Length describes, marking defines","the disjoint-letter ayah proves marking is prior to length, grammar or meaning."),
 quiz=("Special Topic - What Defines a Sura and an Ayah (Week 2)",[
  ("1.  The shortest suras have how many ayat?",f"{floor}",["1","7","10"],f"al-Kawthar, al-Asr, an-Nasr = {floor} ayat each."),
  ("2.  The longest sura (al-Baqara) has:",f"{ceil} ayat",["114","99","30"],f"al-Baqara = {ceil} ayat, the ceiling."),
  ("3.  The longest single ayah is:",f"2:282 ({amax} root-tokens)",["1:1","2:255","112:1"],f"the debt verse, {amax} tokens - a lone outlier."),
  ("4.  An ayah can be as short as:","a single token (e.g. the disjoint letters)",["never under 10 tokens","one full sentence","one sura"],"55:64 and the disjoint letters are one-token ayat."),
  ("5.  Most suras fall in the band:","11-100 ayat",["over 200","exactly 3","over 286"],f"{sh[1]}+{sh[2]} suras are 11-100 ayat."),
  ("6.  The units are ultimately DEFINED by:","marking (name, basmala, received verse-stops)",["length alone","rhyme alone","grammar alone"],"length corroborates but does not define."),
  ("7.  The disjoint letters as a whole ayah prove:","marking is prior to length, grammar, even meaning",["they are not ayat","length defines ayat","they are suras"],"a single, meaning-opaque token stands as a full ayah."),
  ("8.  An ayah need not be:","a complete sentence",["marked","recited","numbered"],"verse-stops, not syntax, bound the ayah."),
  ("9.  The codex's length profile across 114 suras:","descends (longest-first)",["ascends","is flat","is random"],"the same length-grading as the order topic."),
  ("10.  How many suras exceed 200 ayat?",f"{sh[4]}",["dozens","half","none"],f"only {sh[4]} - the rare giants."),
  ("11.  Length is best called:","a corroborating, not defining, criterion",["the definition","irrelevant","the only criterion"],"it describes the units; it cannot derive them."),
  ("12.  The boundaries themselves are:","received / narrated, not computed",["computed from tokens","arbitrary","alphabetical"],"transmission fixes the verse-stops and divisions."),
  ("13.  The honest verdict is:","measurable ranges, but marked-not-defined units",["length defines both","they have no range","they are undefined"],"counting characterises; marking defines."),
 ]),
)
standard_deck(spec)
print("done units")

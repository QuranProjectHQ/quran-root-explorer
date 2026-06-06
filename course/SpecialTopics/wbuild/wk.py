# -*- coding: utf-8 -*-
"""Shared Book6 data + dense-figure kernel for the W-series Special Topics.
Every number a figure shows is recomputed here from Book6.xlsx. Fixed seed, reproducible."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from collections import Counter
SEED=7; rng=np.random.default_rng(SEED)
ROOT="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse"
FIG=os.path.join(ROOT,"SpecialTopics","figs_w"); os.makedirs(FIG,exist_ok=True)
BOOK6=os.path.join(ROOT,"Book6.xlsx")
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#6a6a6a"; ICE="#9fc0e8"; LT="#7ec8bf"
plt.rcParams.update({"font.size":15,"axes.titlesize":17,"axes.labelsize":14,"xtick.labelsize":13,
                     "ytick.labelsize":13,"figure.dpi":150,"axes.spines.top":False,"axes.spines.right":False,
                     "font.family":"DejaVu Sans"})
_raw=pd.read_excel(BOOK6,header=None)
_hdr=[i for i in range(15) if any("سوره" in str(v) for v in _raw.iloc[i]) and any("ریشه" in str(v) for v in _raw.iloc[i])][0]
df=pd.read_excel(BOOK6,header=_hdr)
ROO=[c for c in df.columns if str(c).strip()=="ریشه نحوی"][0]
SURF=[c for c in df.columns if "توکن ریشه" in str(c)][0]      # surface words (col 9)
TOK=[c for c in df.columns if "توکن شده" in str(c)]
TOK=TOK[0] if TOK else SURF
VOC=[c for c in df.columns if "حرکت" in str(c)]
VOC=VOC[0] if VOC else SURF
SUR=[c for c in df.columns if "سوره" in str(c) and "اسم" not in str(c)][0]
AYA=[c for c in df.columns if "آیه" in str(c)][0]
NUZ=[c for c in df.columns if "نزول" in str(c)][0]
df=df.dropna(subset=[SUR,AYA]).reset_index(drop=True)
for c in (ROO,SURF,TOK,VOC): df[c]=df[c].fillna("")
df[SUR]=df[SUR].astype(int); df[AYA]=df[AYA].astype(int)
df[NUZ]=pd.to_numeric(df[NUZ],errors="coerce")
TR={"ی":"ي","ک":"ك","ى":"ي","ة":"ه","أ":"ا","إ":"ا","آ":"ا","ؤ":"و","ئ":"ي"}
def norm(s): return "".join(TR.get(ch,ch) for ch in str(s))
df["toks"]=df[ROO].map(lambda s:[norm(x) for x in str(s).split()])
df["surf"]=df[SURF].map(lambda s:[norm(x) for x in str(s).split()])
_freq=Counter(t for ts in df["toks"] for t in ts)
NA=len(df)
MECCA_CUT=86  # revelation-order boundary (Medinan suras have nuzul order > ~86)

def ac(root):
    """# ayat whose normalized root-list contains `root`."""
    r=norm(root); return int(df["toks"].map(lambda ts:r in ts).sum())
def tokfreq(root): return _freq.get(norm(root),0)
def surf_ac(substr):
    """# ayat where any surface word contains the normalized substring."""
    sub=norm(substr); return int(df["surf"].map(lambda ws:any(sub in w for w in ws)).sum())
def cooccur(a,b):
    """# ayat containing both roots a and b."""
    a=norm(a); b=norm(b)
    return int(df["toks"].map(lambda ts:(a in ts) and (b in ts)).sum())
def lift(a,b):
    na=ac(a); nb=ac(b); j=cooccur(a,b)
    exp=na*nb/NA
    return (j/exp if exp>0 else 0.0), j, na, nb
def sura_counts(root):
    r=norm(root); out=Counter()
    for s,ts in zip(df[SUR],df["toks"]):
        if r in ts: out[s]+=1
    return out
def mecca_split(root):
    r=norm(root); m=0; d=0
    for n,ts in zip(df[NUZ],df["toks"]):
        if r in ts:
            if pd.isna(n): continue
            if n<=MECCA_CUT: m+=1
            else: d+=1
    return m,d

# ---------- generic figures ----------
def fig_freqbarh(fname,title,labels,values,colors=None,xlabel="ayat containing the root (Book6)"):
    colors=colors or [TEAL,NAVY,AMBER,RED,GREY,LT,ICE][:len(labels)]
    fig,ax=plt.subplots(figsize=(11,max(3.4,0.7*len(labels)+2.0)))
    ax.barh(range(len(labels)),values,color=colors,edgecolor="white")
    for i,v in enumerate(values):
        ax.text(v+max(values)*0.012,i,(f"{v:g}"),va="center",fontsize=12.5,fontweight="bold")
    ax.set_yticks(range(len(labels))); ax.set_yticklabels(labels,fontsize=13); ax.invert_yaxis()
    ax.set_xlabel(xlabel); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def fig_groupbar(fname,title,cats,series,ylabel="ayat",fmt="{:.0f}"):
    """series=[(name,color,[vals])]"""
    fig,ax=plt.subplots(figsize=(11,5.0)); n=len(cats); ns=len(series)
    x=np.arange(n); bw=0.8/ns
    for i,(nm,col,vs) in enumerate(series):
        b=ax.bar(x+i*bw-0.4+bw/2,vs,bw,label=nm,color=col,edgecolor="white")
        for xi,v in zip(x+i*bw-0.4+bw/2,vs): ax.text(xi,v+max(max(s[2]) for s in series)*0.012,fmt.format(v),ha="center",va="bottom",fontsize=11,fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(cats,fontsize=12.5); ax.set_ylabel(ylabel); ax.set_title(title)
    if any(nm for nm,_,_ in series): ax.legend(frameon=False,fontsize=12)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def fig_suradist(fname,title,root,highlight=None,xlabel="sura number"):
    sc=sura_counts(root); xs=list(range(1,115)); ys=[sc.get(s,0) for s in xs]
    fig,ax=plt.subplots(figsize=(11,4.8))
    cols=[RED if (highlight and s in highlight) else TEAL for s in xs]
    ax.bar(xs,ys,color=cols,edgecolor="none",width=0.9)
    ax.set_xlabel(xlabel); ax.set_ylabel("occurrences in sura"); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def fig_timeline(fname,title,roots_labels):
    """roots_labels=[(label,root)] -> Meccan vs Medinan stacked bars."""
    labs=[l for l,_ in roots_labels]; M=[]; D=[]
    for _,r in roots_labels:
        m,d=mecca_split(r); M.append(m); D.append(d)
    fig,ax=plt.subplots(figsize=(11,5.0)); x=np.arange(len(labs))
    ax.bar(x,M,color=TEAL,edgecolor="white",label="Meccan")
    ax.bar(x,D,bottom=M,color=AMBER,edgecolor="white",label="Medinan")
    for i in range(len(labs)):
        if M[i]: ax.text(i,M[i]/2,str(M[i]),ha="center",va="center",fontsize=10.5,color="white",fontweight="bold")
        if D[i]: ax.text(i,M[i]+D[i]/2,str(D[i]),ha="center",va="center",fontsize=10.5,color="white",fontweight="bold")
    ax.set_xticks(x); ax.set_xticklabels(labs,fontsize=12.5); ax.set_ylabel("ayat"); ax.set_title(title)
    ax.legend(frameon=False,fontsize=12)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def fig_liftscatter(fname,title,items):
    """items=[(label,count,lift)] -> count (x) vs lift (y) bubble."""
    fig,ax=plt.subplots(figsize=(11,5.0))
    for lab,c,lf in items:
        ax.scatter(c,lf,s=160,color=TEAL,edgecolor="white",zorder=3)
        ax.annotate(lab,(c,lf),xytext=(6,4),textcoords="offset points",fontsize=11.5,color=NAVY)
    ax.set_xlabel("shared-ayah count (support)"); ax.set_ylabel("lift (x over chance)")
    ax.axhline(1,color=GREY,ls="--",lw=1); ax.set_title(title)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()
def fig_donut(fname,title,labels,values,colors=None):
    colors=colors or [TEAL,AMBER,NAVY,RED,GREY][:len(labels)]
    fig,ax=plt.subplots(figsize=(7.5,5.2))
    w,_,_=ax.pie(values,labels=[f"{l}\n{v}" for l,v in zip(labels,values)],colors=colors,
                 autopct=lambda p:f"{p:.0f}%",pctdistance=0.78,wedgeprops=dict(width=0.42,edgecolor="white"),
                 textprops=dict(fontsize=12))
    ax.set_title(title); plt.tight_layout(); plt.savefig(os.path.join(FIG,fname)); plt.close()

if __name__=="__main__":
    print("Book6 rows:",NA,"| cols:",ROO,"|",SURF)
    for r in ["ءله","رحم","نور","ظلم","مثل","نفق","شفع","نسخ","علم","حكم","غفر"]:
        print(f"{r}: ac={ac(r)} tokfreq={tokfreq(r)}")

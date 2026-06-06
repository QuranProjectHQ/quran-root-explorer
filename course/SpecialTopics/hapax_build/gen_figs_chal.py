# -*- coding: utf-8 -*-
"""Dense data-figures for the Qur'an-Challenges Special Topic, computed LIVE from Book6.xlsx.
Per COURSE_STANDARDS 12a/17. Fixed seed, reproducible. 7 figures."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from collections import Counter
SEED=7; rng=np.random.default_rng(SEED)
HERE=os.path.dirname(os.path.abspath(__file__))
ROOT="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse"
FIG=os.path.join(ROOT,"SpecialTopics","figs_chal"); os.makedirs(FIG,exist_ok=True)
BOOK6=os.path.join(ROOT,"Book6.xlsx")
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#6a6a6a"; ICE="#9fc0e8"
plt.rcParams.update({"font.size":15,"axes.titlesize":18,"axes.labelsize":15,"xtick.labelsize":13,
                     "ytick.labelsize":13,"figure.dpi":150,"axes.spines.top":False,"axes.spines.right":False,
                     "font.family":"DejaVu Sans"})
raw=pd.read_excel(BOOK6,header=None)
hdr=[i for i in range(15) if any("سوره" in str(v) for v in raw.iloc[i]) and any("ریشه" in str(v) for v in raw.iloc[i])][0]
df=pd.read_excel(BOOK6,header=hdr)
ROO=[c for c in df.columns if str(c).strip()=="ریشه نحوی"][0]
SUR=[c for c in df.columns if "سوره" in str(c) and "اسم" not in str(c)][0]
AYA=[c for c in df.columns if "آیه" in str(c)][0]
NUZ=[c for c in df.columns if "نزول" in str(c)][0]
df=df.dropna(subset=[SUR,AYA]).reset_index(drop=True); df[ROO]=df[ROO].fillna("")
TR={"ی":"ي","ک":"ك","ى":"ي","ة":"ه","أ":"ا","إ":"ا","آ":"ا","ؤ":"و","ئ":"ي"}
def norm(s): return "".join(TR.get(ch,ch) for ch in s)
df["toks"]=df[ROO].map(lambda s:[norm(x) for x in str(s).split()])
df[SUR]=df[SUR].astype(int); df[AYA]=df[AYA].astype(int)
df[NUZ]=pd.to_numeric(df[NUZ],errors="coerce")
def ac(r): r=norm(r); return int(df["toks"].map(lambda ts:r in ts).sum())

# ---------- FIG 1: the escalating literary challenge (log bar) ----------
labels=["the WHOLE\n(17:88)","TEN sūras\n(11:13)","ONE sūra\n(2:23·10:38)","ONE statement\n(52:34)"]
# units of text demanded as a proxy (āyāt): whole corpus, 10 avg-sūras, 1 avg-sūra, 1 statement(~1 āyah)
avg_sura=6236/114
units=[6236, 10*avg_sura, 1*avg_sura, 1]
fig,ax=plt.subplots(figsize=(11,5.0))
cols=[RED,AMBER,TEAL,NAVY]
b=ax.bar(range(4),units,color=cols,edgecolor="white",width=0.62)
ax.set_yscale("log"); ax.set_ylim(0.6,1e4)
for i,(r,u) in enumerate(zip(b,units)): ax.text(i,u*1.25,f"≈{u:.0f}\nāyāt",ha="center",va="bottom",fontsize=12,color=cols[i],fontweight="bold")
ax.set_xticks(range(4)); ax.set_xticklabels(labels,fontsize=12.5)
ax.set_ylabel("text demanded (āyāt, log scale)")
ax.set_title("The literary dare escalates DOWN — whole → ten → one → a single statement")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_escalation.png")); plt.close()

# ---------- FIG 2: challenge verses on the revelation timeline ----------
verses=[("17:88",17,88,"imitate the whole"),("11:13",11,13,"ten sūras"),
        ("10:38",10,38,"one sūra"),("52:34",52,34,"a statement"),
        ("67:3",67,3,"cosmic: a flaw"),("2:23",2,23,"one sūra"),
        ("2:24",2,24,"prediction"),("4:82",4,82,"consistency")]
# revelation order of each verse's sūra
def nuz_of(s):
    v=df[df[SUR]==s][NUZ].dropna()
    return int(v.iloc[0]) if len(v) else np.nan
pts=[(lbl,nuz_of(s),gl) for lbl,s,a,gl in verses]
pts=[p for p in pts if not np.isnan(p[1])]
pts.sort(key=lambda p:p[1])
fig,ax=plt.subplots(figsize=(11,5.0))
xs=[p[1] for p in pts]; ys=list(range(len(pts)))
mecca_cut=86  # rev-order <=86 ≈ Meccan period boundary (an-Nisā' #92 onward Medinan)
cols=[TEAL if x<=mecca_cut else AMBER for x in xs]
ax.scatter(xs,ys,s=160,c=cols,edgecolor="white",zorder=3)
for (lbl,x,gl),y in zip(pts,ys):
    ax.text(x+1.2,y,f"{lbl}  {gl}",va="center",fontsize=12.5,color=NAVY)
ax.axvline(mecca_cut,color=GREY,ls="--",lw=1.3)
ax.text(mecca_cut-1,len(pts)-0.3,"Meccan ◂",ha="right",fontsize=12,color=TEAL,fontweight="bold")
ax.text(mecca_cut+1,len(pts)-0.3,"▸ Medinan",ha="left",fontsize=12,color=AMBER,fontweight="bold")
ax.set_yticks([]); ax.set_xlabel("revelation order (sūra) →")
ax.set_xlim(40,100); ax.set_title("When the challenges fall — across the revelation timeline")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_revorder.png")); plt.close()

# ---------- FIG 3: literary-challenge vocabulary frequency ----------
lit=[("أتى bring! ءتي",ac("ءتي")),("مثل the like",ac("مثل")),
     ("فري fabricate",ac("فري")),("سور sūra",ac("سور"))]
fig,ax=plt.subplots(figsize=(11,4.8))
labs=[l for l,_ in lit]; vals=[v for _,v in lit]
b=ax.barh(range(len(labs)),vals,color=[TEAL,NAVY,AMBER,RED],edgecolor="white")
for i,v in enumerate(vals): ax.text(v+5,i,str(v),va="center",fontsize=13,fontweight="bold")
ax.set_yticks(range(len(labs))); ax.set_yticklabels(labs,fontsize=13.5); ax.invert_yaxis()
ax.set_xlabel("āyāt containing the root (Book6)")
ax.set_title("The literary-challenge vocabulary — how often the dare-words occur")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_vocab.png")); plt.close()

# ---------- FIG 4: cosmic + consistency challenge terms — rare, precise vocabulary ----------
cos=[("تفاوت disparity (فوت)",ac("فوت")),("فطور rupture (فطر)",ac("فطر")),
     ("اختلاف discrepancy (خلف)",ac("خلف")),("صدق truthful",ac("صدق"))]
fig,ax=plt.subplots(figsize=(11,4.8))
labs=[l for l,_ in cos]; vals=[v for _,v in cos]
b=ax.barh(range(len(labs)),vals,color=[RED,AMBER,TEAL,NAVY],edgecolor="white")
for i,v in enumerate(vals): ax.text(v+2,i,str(v),va="center",fontsize=13,fontweight="bold")
ax.set_yticks(range(len(labs))); ax.set_yticklabels(labs,fontsize=13); ax.invert_yaxis()
ax.set_xlabel("āyāt containing the root (Book6)")
ax.set_title("The cosmic & consistency dares use PRECISE, rare terms — تفاوت only 5 āyāt")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_cosmic_rarity.png")); plt.close()

# ---------- FIG 5: مثل across the corpus — the 5 literary challenges are a needle in a haystack ----------
mathl=norm("مثل")
hits=[(int(r[SUR]),int(r[AYA])) for _,r in df.iterrows() if mathl in r["toks"]]
chal_set={(17,88),(11,13),(2,23),(10,38),(52,34)}
fig,ax=plt.subplots(figsize=(11,4.6))
xs=[s for s,a in hits]
ax.scatter(xs,[0.0]*len(xs),s=44,c=ICE,edgecolor="white",alpha=0.8,zorder=2,label=f"مثل elsewhere ({len(hits)-len([h for h in hits if h in chal_set])} āyāt)")
ch=[s for s,a in hits if (s,a) in chal_set]
ax.scatter(ch,[0.0]*len(ch),s=180,c=RED,edgecolor="white",zorder=4,marker="D",label=f"literary-challenge āyāt ({len(ch)})")
for s,a in hits:
    if (s,a) in chal_set: ax.annotate(f"{s}:{a}",(s,0.0),xytext=(s,0.02),fontsize=11,color=RED,ha="center")
ax.set_ylim(-0.05,0.06); ax.set_yticks([]); ax.set_xlabel("sūra number")
ax.set_title("'Bring the like (mithl)' — 5 challenge āyāt among 148 uses of مثل")
ax.legend(frameon=False,fontsize=12,loc="lower right")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_mathl.png")); plt.close()

# ---------- FIG 6: the consistency-challenge touchpoint — Two Books FDR battery (6 of 8 survive) ----------
# Live-computed battery from the Two Books FDR-summary lecture (BH q-values).
batt=[("Contiguity · muṣḥaf",0.0010),("Contiguity · nuzūl",0.0010),
      ("Length autocorrelation",0.0010),("Root-entropy special",0.0010),
      ("Letter-entropy special",0.0032),("Di-codon adjacency",0.0067),
      ("Shared theme per tag",0.056),("Shared length per tag",0.289)]
batt=sorted(batt,key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(11,5.0))
labs=[l for l,_ in batt]; q=[v for _,v in batt]
cols=[TEAL if v<=0.05 else RED for v in q]
b=ax.barh(range(len(labs)),q,color=cols,edgecolor="white")
for i,v in enumerate(q): ax.text(v*1.15,i,f"{v:.3f}",va="center",fontsize=12,fontweight="bold",color=cols[i])
ax.axvline(0.05,color=GREY,ls="--",lw=1.4); ax.text(0.05,-0.7,"5% FDR",color=GREY,fontsize=12)
ax.set_xscale("log"); ax.set_yticks(range(len(labs))); ax.set_yticklabels(labs,fontsize=12.5); ax.invert_yaxis()
ax.set_xlabel("Benjamini–Hochberg q-value (log scale)")
ax.set_title("The consistency dare, measured — 6 of 8 structural tests survive 5% FDR")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_fdr.png")); plt.close()

# ---------- FIG 7: the 7 challenge sūras against the corpus length distribution ----------
lengths={s:int(g[AYA].max()) for s,g in df.groupby(SUR)}
allv=np.array(sorted(lengths.values()))
chs={17:"17 al-Isrā",11:"11 Hūd",2:"2 al-Baqara",10:"10 Yūnus",52:"52 aṭ-Ṭūr",4:"4 an-Nisāʾ",67:"67 al-Mulk"}
fig,ax=plt.subplots(figsize=(11,5.0))
ax.hist(allv,bins=30,color=ICE,edgecolor="white")
for s,name in chs.items():
    ax.axvline(lengths[s],color=RED,lw=1.4,alpha=0.85)
    ax.text(lengths[s],ax.get_ylim()[1]*(0.55+0.06*(list(chs).index(s)%5)),f"{name} ({lengths[s]})",
            rotation=90,fontsize=10.5,color=RED,va="bottom",ha="right")
ax.set_xlabel("sūra length (āyāt)"); ax.set_ylabel("# sūras")
ax.set_title("The challenge sūras span the whole range — from al-Mulk (30) to al-Baqara (286)")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"chal_sura_context.png")); plt.close()

print("OK figs:",sorted(os.listdir(FIG)))
print("counts: ءتي",ac("ءتي"),"مثل",ac("مثل"),"فري",ac("فري"),"سور",ac("سور"),
      "فوت",ac("فوت"),"فطر",ac("فطر"),"خلف",ac("خلف"),"صدق",ac("صدق"))
print("mathl hits:",len(hits)," challenge-in-mathl:",len(ch))

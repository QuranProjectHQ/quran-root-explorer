# -*- coding: utf-8 -*-
"""Week 1 — fig1 (frequency) rebuilt STANDALONE from Book6 (no engine dep).
Panel 1A is a single-y-axis RANK SLOPEGRAPH (the per-ayah vs per-roots flip);
all fonts enlarged for readability."""
import os, collections, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper; from bidi.algorithm import get_display
HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.join(os.path.dirname(HERE),"Book6.xlsx")
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams.update({"font.family":"DejaVu Sans","axes.grid":True,"grid.alpha":0.3,
    "font.size":15,"axes.titlesize":17,"axes.labelsize":15,"xtick.labelsize":14,
    "ytick.labelsize":14,"legend.fontsize":13})
def ar(s): return get_display(arabic_reshaper.reshape(str(s)))
def norm(s):
    s=s.replace('ی','ي').replace('ﻯ','ي').replace('ک','ك')
    for h in 'ئؤأإآ': s=s.replace(h,'ء')
    return s
import openpyxl
ws=openpyxl.load_workbook(BOOK,read_only=True,data_only=True).active
SETS=[];SUR=[];IDX=collections.defaultdict(set);TF=collections.Counter();SURSIZE=collections.Counter()
for row in ws.iter_rows(min_row=9,values_only=True):
    if not row[8]: continue
    toks=[norm(t) for t in str(row[8]).split()]; j=len(SETS)
    SETS.append(set(toks)); s=int(row[5]); SUR.append(s); SURSIZE[s]+=1
    for t in toks: TF[t]+=1
    for t in set(toks): IDX[t].add(j)
N=len(SETS); TOT=sum(TF.values())
LEN=np.array([len(x) for x in SETS],float)
ROOTS=["ظلم","نفس","هدي","عدل"]; RC=dict(zip(ROOTS,["#d62728","#1f77b4","#ff7f0e","#2ca02c"]))
def df(r): return len(IDX[norm(r)])
def tf(r): return TF[norm(r)]
def rows(r): return IDX[norm(r)]
per_ay={r:df(r)/N*1000 for r in ROOTS}; per_rt={r:tf(r)/TOT*1000 for r in ROOTS}
def per_surah(r):
    c=collections.Counter(SUR[i] for i in rows(r)); s=sorted(c)
    freq=np.array([c[x] for x in s],float); size=np.array([SURSIZE[x] for x in s],float)
    return freq,size
FREQ={t:len(v) for t,v in IDX.items()}

fig,axs=plt.subplots(2,2,figsize=(16,9.6))
fig.suptitle(ar("الأسبوع ١ — جوانب التكرار: ما يكشفه وأين يضلّل")+
    "   (Week 1 — frequency: what it reveals & where it misleads)",fontsize=17,weight="bold")

# ---- 1A: single-y RANK SLOPEGRAPH (the flip) ----
ax=axs[0,0]
order_ay=sorted(ROOTS,key=lambda r:-per_ay[r]); order_rt=sorted(ROOTS,key=lambda r:-per_rt[r])
rank_ay={r:order_ay.index(r)+1 for r in ROOTS}; rank_rt={r:order_rt.index(r)+1 for r in ROOTS}
for r in ROOTS:
    ax.plot([0,1],[rank_ay[r],rank_rt[r]],"-o",lw=4,ms=12,color=RC[r],zorder=3)
    ax.text(-0.06,rank_ay[r],f"{ar(r)}  {per_ay[r]:.1f}",ha="right",va="center",fontsize=15,color=RC[r],weight="bold")
    ax.text(1.06,rank_rt[r],f"{per_rt[r]:.2f}  {ar(r)}",ha="left",va="center",fontsize=15,color=RC[r],weight="bold")
ax.set_xlim(-0.55,1.55); ax.set_ylim(4.6,0.4)
ax.set_yticks([1,2,3,4]); ax.set_yticklabels(["#1","#2","#3","#4"])
ax.set_xticks([0,1]); ax.set_xticklabels(["per 1,000 AYAHS","per 1,000 ROOTS\n(size-true)"],fontsize=15,weight="bold")
ax.set_ylabel("rank",fontsize=15); ax.grid(False)
ax.set_title("[norm] the size-true RANK FLIP (hudā overtakes ẓulm)",fontsize=16,weight="bold")
ax.annotate("",xy=(1,rank_rt["هدي"]),xytext=(0,rank_ay["هدي"]),
    arrowprops=dict(arrowstyle="->",color="#ff7f0e",lw=0,alpha=0))
ax.text(0.5,0.2,"per-ayah: ظلم #1  →  per-roots: هدي #1",ha="center",va="top",fontsize=13,
    color="#333",transform=ax.transAxes)

# ---- 1B length confound ----
ax=axs[0,1]
for r in ROOTS:
    freq,size=per_surah(r); ax.scatter(size,freq,s=34,alpha=.6,color=RC[r],label=ar(r))
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_title("[−] raw count rides on surah length"); ax.set_xlabel("surah size (ayahs, log)")
ax.set_ylabel("raw hits in surah (log)"); ax.legend()

# ---- 1C term vs ayah freq ----
ax=axs[1,0]; x=np.arange(4); w=.38
af=[df(r) for r in ROOTS]; tfr=[tf(r) for r in ROOTS]
ax.bar(x-w/2,af,w,label="ayah-frequency (once/ayah)",color="#4c72b0")
ax.bar(x+w/2,tfr,w,label="term-frequency (every token)",color="#dd8452")
for i,(a,t) in enumerate(zip(af,tfr)): ax.text(i+w/2,t,f"+{t-a}",ha="center",va="bottom",fontsize=14,weight="bold")
ax.set_xticks(x); ax.set_xticklabels([ar(r) for r in ROOTS],fontsize=16)
ax.set_title("[−] ayah-frequency hides repeats inside a verse"); ax.set_ylabel("count"); ax.legend()

# ---- 1D Zipf ----
ax=axs[1,1]
allf=np.array(sorted(FREQ.values(),reverse=True),float); rank=np.arange(1,len(allf)+1)
ax.loglog(rank,allf,color="#888",lw=1.6)
for r in ROOTS:
    fr=df(r); rk=int((allf>=fr).sum())
    ax.scatter(rk,fr,color=RC[r],s=90,zorder=3)
    ax.annotate(ar(r),(rk,fr),textcoords="offset points",xytext=(8,5),fontsize=15,color=RC[r],weight="bold")
ax.set_title(f"[ctx] frequency is long-tailed ({len(allf)} roots)")
ax.set_xlabel("rank (log)"); ax.set_ylabel("ayah-frequency (log)")
fig.tight_layout(rect=[0,0,1,0.94]); fig.savefig(os.path.join(HERE,"fig1_frequency.png"),dpi=130); plt.close(fig)
print("wrote fig1_frequency.png  | flip:",order_ay,"->",order_rt)

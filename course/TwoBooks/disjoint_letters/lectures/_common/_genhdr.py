import os, numpy as np, matplotlib, itertools
matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import openpyxl
from collections import Counter
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":15,
 "axes.titleweight":"bold","figure.dpi":150,"savefig.bbox":"tight","axes.edgecolor":"#556070",
 "axes.labelcolor":"#1E293B","text.color":"#1E293B","xtick.color":"#556070","ytick.color":"#556070"})
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#8A93A0"; ICE="#CADCFC"; LT="#7FCABD"
OUT="/sessions/stoic-cool-hawking/mnt/TwoBooks/disjoint_letters/lectures/figs_dl"
wb=openpyxl.load_workbook("/sessions/stoic-cool-hawking/mnt/RootCourse/Book6.xlsx",read_only=True,data_only=True)
ws=wb.active; vmax={}; nuz={}; roots={}
for r in ws.iter_rows(values_only=True):
    if r[5] is None or not isinstance(r[5],(int,float)): continue
    su=int(r[5]); ay=int(r[6]) if isinstance(r[6],(int,float)) else 0
    vmax[su]=max(vmax.get(su,0),ay)
    if r[12] is not None and su not in nuz:
        try: nuz[su]=int(r[12])
        except: pass
    if r[8]: roots.setdefault(su,[]).extend(str(r[8]).split())
verses=dict(vmax)
FAMS=[("HM",[40,41,42,43,44,45,46],TEAL),("ALM",[2,3,29,30,31,32],NAVY),("ALR",[10,11,12,14,15],AMBER),("TSM",[26,28],RED)]
SINGLE={7:"ALMS",13:"ALMR",19:"KHYAS",20:"TH",27:"TS",36:"YS",38:"S",50:"Q",68:"N"}
MUQ=sorted(sum([f[1] for f in FAMS],[])+list(SINGLE)); multi=[f[1] for f in FAMS]; sizes=[len(x) for x in multi]
famcol={}
for nm,ss,c in FAMS:
    for s in ss: famcol[s]=c
for s in SINGLE: famcol[s]=GREY
mus={s:s for s in range(1,115)}
def style(ax): ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False); ax.grid(axis="y",alpha=.25,lw=.8)
def save(fig,name): fig.savefig(os.path.join(OUT,name),facecolor="white"); plt.close(fig); print(name)
def within_mean(pos,fams):
    tot=0;n=0
    for ss in fams:
        ps=[pos[s] for s in ss if s in pos]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)): tot+=abs(ps[i]-ps[j]); n+=1
    return tot/n if n else 0
def lpnull(pos,seed=1,nd=8000):
    rng=np.random.default_rng(seed); out=[]; base=list(MUQ)
    for _ in range(nd):
        rng.shuffle(base); idx=0; fams=[]
        for k in sizes: fams.append(base[idx:idx+k]); idx+=k
        out.append(within_mean(pos,fams))
    return np.array(out)
profs={s:Counter(roots.get(s,[])) for s in MUQ}
def cos(a,b):
    import math; keys=set(a)|set(b); dot=sum(a[k]*b[k] for k in keys)
    na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0
obs_mus=within_mean(mus,multi); obs_nuz=within_mean(nuz,multi)
null_mus=lpnull(mus,1); null_nuz=lpnull(nuz,2)

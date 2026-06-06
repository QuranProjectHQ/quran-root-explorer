# -*- coding: utf-8 -*-
"""FDR Summary dense figure: the Benjamini-Hochberg staircase. Per §12a.
Sorted p-values vs the (i/m)*alpha line; the crossover marks the 6/8 survivors."""
import os, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
HERE=os.path.dirname(os.path.abspath(__file__)); LEC=os.path.dirname(HERE)
FIG=os.path.join(LEC,"figs"); os.makedirs(FIG,exist_ok=True)
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#6a6a6a"; ICE="#9fc0e8"
plt.rcParams.update({"font.size":15,"axes.titlesize":18,"axes.labelsize":15,"xtick.labelsize":12,
                     "ytick.labelsize":12,"figure.dpi":150,"axes.spines.top":False,"axes.spines.right":False,
                     "font.family":"DejaVu Sans"})
# the 8 representative tests, sorted ascending by p (labels short)
tests=[("contiguity·muṣḥaf",0.0005),("contiguity·nuzūl",0.0005),("length autocorr.",0.0005),
       ("root entropy",0.0005),("letter entropy",0.002),("di-codon adj.",0.005),
       ("shared theme",0.049),("shared length",0.289)]
tests=sorted(tests,key=lambda x:x[1])
ps=np.array([p for _,p in tests]); m=len(ps); alpha=0.05
ranks=np.arange(1,m+1); thr=ranks/m*alpha
# BH survivors: largest i with p_i <= (i/m)alpha; all ranks <= that survive
below=ps<=thr
kmax=np.max(np.where(below)[0])+1 if below.any() else 0
surv=ranks<=kmax
fig,ax=plt.subplots(figsize=(11,5.2))
ax.plot(ranks,thr,"--",color=GREY,lw=2,label="BH threshold  (i/m)·α,  α=0.05")
ax.scatter(ranks[surv],ps[surv],s=130,color=TEAL,zorder=5,label="survives 5% FDR")
ax.scatter(ranks[~surv],ps[~surv],s=130,color=RED,zorder=5,label="fails")
for i,(lab,p) in enumerate(tests):
    ax.annotate(lab,(ranks[i],ps[i]),xytext=(ranks[i],ps[i]+0.011),
                ha="center",fontsize=11,color=NAVY,rotation=0)
ax.axvline(kmax+0.5,color=AMBER,lw=1.5,ls=":")
ax.annotate(f"crossover after rank {kmax}\n→ {kmax} of {m} survive",(kmax+0.5,0.20),
            xytext=(kmax+0.7,0.20),color=AMBER,fontsize=13)
ax.set_xticks(ranks); ax.set_xlabel("rank i (p-values sorted ascending)")
ax.set_ylabel("p-value"); ax.set_ylim(-0.01,0.31)
ax.set_title("Benjamini–Hochberg staircase — 6 of 8 tests clear the line")
ax.legend(frameon=False,fontsize=12,loc="upper left")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"fdr_staircase.png")); plt.close()
print("FDR staircase written. survivors=%d/%d (kmax=%d)"%(surv.sum(),m,kmax))

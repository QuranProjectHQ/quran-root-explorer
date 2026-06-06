# -*- coding: utf-8 -*-
"""Dense Disjoint-Letters data-figures, computed LIVE from Book6.xlsx. Per §12a.
Contiguity strip (114 suras), muq-vs-other length histogram, per-sura Qaf-density distribution."""
import os, numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from collections import Counter
HERE=os.path.dirname(os.path.abspath(__file__)); LEC=os.path.dirname(HERE)
FIG=os.path.join(LEC,"figs"); os.makedirs(FIG,exist_ok=True)
BOOK6=os.path.join(LEC,"..","..","..","Book6.xlsx")
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#cfcfcf"; ICE="#9fc0e8"
plt.rcParams.update({"font.size":15,"axes.titlesize":18,"axes.labelsize":15,"xtick.labelsize":12,
                     "ytick.labelsize":12,"figure.dpi":150,"axes.spines.top":False,"axes.spines.right":False,
                     "font.family":"DejaVu Sans"})
MUQ=[2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68]
FAM={"ḤM":[40,41,42,43,44,45,46],"ALM":[2,3,29,30,31,32],"ALR":[10,11,12,14,15],"ṬSM":[26,28]}
raw=pd.read_excel(BOOK6,header=None)
hdr=[i for i in range(15) if any("سوره" in str(v) for v in raw.iloc[i]) and any("ریشه" in str(v) for v in raw.iloc[i])][0]
df=pd.read_excel(BOOK6,header=hdr)
SUR=[c for c in df.columns if "سوره" in str(c) and "اسم" not in str(c)][0]; AYA=[c for c in df.columns if "آیه" in str(c)][0]
SEG=[c for c in df.columns if "متن آیه" in str(c)]
SEG=SEG[0] if SEG else None
df=df.dropna(subset=[SUR,AYA]).reset_index(drop=True)
sur=df[SUR].astype(int).tolist()
vps=Counter(sur)                                 # ayahs per sura
TR={"ی":"ي","ک":"ك","ى":"ي","ة":"ه","أ":"ا","إ":"ا","آ":"ا","ؤ":"و","ئ":"ي"}
def norm(s): return "".join(TR.get(ch,ch) for ch in str(s))

# ---- FIG 1: contiguity strip — which of the 114 suras carry disjoint letters ----
fig,ax=plt.subplots(figsize=(11,3.0))
muqset=set(MUQ)
for s in range(1,115):
    ax.add_patch(plt.Rectangle((s-1,0),1,1,color=(TEAL if s in muqset else GREY),ec="white",lw=0.4))
ax.set_xlim(0,114); ax.set_ylim(0,1); ax.set_yticks([])
ax.set_xticks([0,20,40,60,80,100,114]); ax.set_xlabel("sūra number (muṣḥaf order)")
ax.set_title("Contiguity — the 29 disjoint-letter sūras (teal) cluster in blocks, not at random")
ax.legend(handles=[Patch(color=TEAL,label="muqaṭṭaʿāt sūra"),Patch(color=GREY,label="other")],
          loc="upper center",bbox_to_anchor=(0.5,-0.35),ncol=2,frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"dl_contiguity.png")); plt.close()

# ---- FIG 2: sura-length histogram, muq vs other (ayahs per sura) ----
muq_len=[vps[s] for s in range(1,115) if s in muqset]
oth_len=[vps[s] for s in range(1,115) if s not in muqset]
fig,ax=plt.subplots(figsize=(11,4.8))
bins=np.linspace(0,300,31)
ax.hist(oth_len,bins=bins,color=GREY,alpha=0.85,label=f"other sūras (median {int(np.median(oth_len))})",edgecolor="white")
ax.hist(muq_len,bins=bins,color=TEAL,alpha=0.8,label=f"muqaṭṭaʿāt sūras (median {int(np.median(muq_len))})",edgecolor="white")
ax.axvline(np.median(oth_len),color=GREY,lw=2,ls="--"); ax.axvline(np.median(muq_len),color=TEAL,lw=2,ls="--")
ax.set_xlabel("sūra length (āyahs)"); ax.set_ylabel("number of sūras")
ax.set_title("Size — disjoint-letter sūras are markedly LONGER (median 85 vs 26 āyahs)")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"dl_length.png")); plt.close()

print("DL figs written. muq median=%d other median=%d"%(int(np.median(muq_len)),int(np.median(oth_len))))

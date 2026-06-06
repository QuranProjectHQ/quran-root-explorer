# -*- coding: utf-8 -*-
"""al-Fatiha worked-example figure — FREQUENCY only (ayah vs term; within-ayah repeats)."""
import os, sys, collections
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE); sys.path.insert(0,ROOT)
import engine as E, analysis
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams["font.family"]="DejaVu Sans"; plt.rcParams["axes.grid"]=True; plt.rcParams["grid.alpha"]=0.3
def ar(s): return get_display(arabic_reshaper.reshape(str(s)))
df=E.C.df; sub=df[df[E.SUR_COL]==1]
ayah_tokens=[str(r['ریشه نحوی']).split() for _,r in sub.iterrows()]; ayahs=list(range(1,8))
tot=[len(t) for t in ayah_tokens]; dist=[len(set(t)) for t in ayah_tokens]
af=collections.Counter(); tf=collections.Counter()
for t in ayah_tokens:
    for x in set(t): af[x]+=1
    for x in t: tf[x]+=1
order=sorted(tf, key=lambda x:(-tf[x],-af[x]))
fig,axs=plt.subplots(1,2,figsize=(14.5,5.6))
fig.suptitle(ar("سورة الفاتحة — مثال محسوب يدويًا للتكرار")+"   (al-Fatiha — worked example: frequency)",fontsize=14,weight="bold")
# P1 root frequency ayah vs term
ax=axs[0]; xx=np.arange(len(order)); w=.38
ax.bar(xx-w/2,[af[r] for r in order],w,label="ayah-freq",color="#d62728")
ax.bar(xx+w/2,[tf[r] for r in order],w,label="term-freq",color="#dd8452")
ax.set_xticks(xx); ax.set_xticklabels([ar(r) for r in order],rotation=90,fontsize=8)
ax.set_title("root frequency in al-Fatiha (ayah vs term)"); ax.set_ylabel("count"); ax.legend(fontsize=9)
# P2 within-ayah repeats
ax=axs[1]; x=np.arange(7)
ax.bar(x-w/2,tot,w,label="total tokens",color="#1f77b4")
ax.bar(x+w/2,dist,w,label="distinct roots",color="#2ca02c")
ax.set_xticks(x); ax.set_xticklabels(ayahs)
ax.set_title("repeats within an ayah (gap = a root said twice)")
ax.set_xlabel("Ayah No"); ax.set_ylabel("count"); ax.legend(fontsize=9)
fig.tight_layout(rect=[0,0,1,0.94]); fig.savefig(os.path.join(HERE,"fig_fatiha.png"),dpi=124); plt.close(fig)
print("wrote fig_fatiha.png (frequency-only)")

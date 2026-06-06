# -*- coding: utf-8 -*-
"""Themed-root frequency ladder (per 1000 ayahs), colored by band. For Lecture Notes v2 §5."""
import os, sys
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE); sys.path.insert(0,ROOT)
import engine as E
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams["font.family"]="DejaVu Sans"; plt.rcParams["axes.grid"]=True; plt.rcParams["grid.alpha"]=0.3
def ar(s): return get_display(arabic_reshaper.reshape(str(s)))
ROOTS=["عدل","ظلم","قسط","نفس","عسر","يسر","صبر","رزق","شكر","هدي","ضلل","صرط","رشد"]
data=sorted([(r,E.rate_per_1k_ayahs(r),E.rate_per_1k_roots(r),E.f(r)) for r in ROOTS], key=lambda t:t[1])
def band(v): return "#1a6b54" if v>=25 else ("#c98a1b" if v>=5 else "#a23b3b")
fig,ax=plt.subplots(figsize=(11.5,7.2))
y=np.arange(len(data))
ax.barh(y,[d[1] for d in data],color=[band(d[1]) for d in data])
for i,d in enumerate(data):
    ax.text(d[1]+0.4,i,f"{d[1]:.1f}/1k ay  ·  {d[2]:.2f}/1k rt  (n={d[3]})",va="center",fontsize=9)
ax.set_yticks(y); ax.set_yticklabels([ar(d[0]) for d in data],fontsize=14)
ax.set_xlabel("rate per 1000 ayahs"); ax.set_xlim(0,60)
ax.set_title(ar("الأسبوع ١ — سلّم تكرار الجذور المواضيعية")+
             "   (Week 1 — themed-root frequency ladder)",fontsize=13,weight="bold")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color="#1a6b54",label="pervasive ≥25/1k"),
                   Patch(color="#c98a1b",label="mid 5–25/1k"),
                   Patch(color="#a23b3b",label="rare <5/1k")],loc="lower right",fontsize=10)
fig.tight_layout(); fig.savefig(os.path.join(HERE,"fig_freq_ladder.png"),dpi=124); plt.close(fig)
print("wrote fig_freq_ladder.png")

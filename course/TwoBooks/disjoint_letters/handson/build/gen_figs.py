# -*- coding: utf-8 -*-
import json, sys, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import arabic_reshaper
from bidi.algorithm import get_display
def ar(s): return get_display(arabic_reshaper.reshape(s))
plt.rcParams["font.family"]="DejaVu Sans"
sys.path.insert(0, "/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2")
import analysis as A, twobooks_stats as T
c=A.load_corpus("/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2/Book6.xlsx"); L,_=T.per_sura_letters_roots(c)
bank=json.load(open("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/disjoint_letters/handson/dl_data_bank.json",encoding="utf-8"))
def dens(s,ch):
    tot=sum(L[s].values()); return (L[s].get(ch,0)/tot) if tot else 0.0

# FIG 1 — ق density across 114 sūras, Sūra 50 highlighted
qd=[100*dens(s,"ق") for s in range(1,115)]
colors=["#E63946" if s==50 else "#9CA3AF" for s in range(1,115)]
fig,axx=plt.subplots(figsize=(9,3.2))
axx.bar(range(1,115),qd,color=colors,width=0.9)
axx.set_title("Density of the letter "+ar("ق")+" across the 114 suras (computed from Book6)",fontsize=12)
axx.set_xlabel("sura number",fontsize=11); axx.set_ylabel("% of letters that are "+ar("ق"),fontsize=11)
axx.annotate("Sura 50 (Qaf)\nrank "+str(bank["qaf"]["sura50_rank"])+"/114",
             xy=(50,qd[49]),xytext=(60,max(qd)*0.8),fontsize=10,color="#E63946",
             arrowprops=dict(arrowstyle="->",color="#E63946"))
fig.tight_layout(); fig.savefig("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/disjoint_letters/handson/figs/fig_qaf_density.png",dpi=150); plt.close(fig)

# FIG 2 — enrichment test across the 14 disjoint letters (only م crosses 0.05)
lets=bank["letters"]
labels=[ar(x["letter"]) for x in lets]; pv=[x["p"] for x in lets]
nlp=[-np.log10(max(p,1e-6)) for p in pv]
bar_colors=["#2A9D8F" if p<0.05 else "#9CA3AF" for p in pv]
fig,axx=plt.subplots(figsize=(9,3.4))
axx.bar(range(len(lets)),nlp,color=bar_colors,width=0.8)
axx.axhline(-np.log10(0.05),color="#E63946",ls="--",lw=1.3)
axx.text(len(lets)-1,-np.log10(0.05)+0.05,"p = 0.05",color="#E63946",ha="right",fontsize=9)
axx.set_xticks(range(len(lets))); axx.set_xticklabels(labels,fontsize=13)
axx.set_title("Does each disjoint letter carry a frequency code? (enrichment vs 20,000 random sura-sets)",fontsize=11)
axx.set_ylabel("-log10 p  (higher = more unusual)",fontsize=10)
fig.tight_layout(); fig.savefig("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/disjoint_letters/handson/figs/fig_letter_enrichment.png",dpi=150); plt.close(fig)
print("figures written:", bank["n_sig"], "letter(s) above the 0.05 line")

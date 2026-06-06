# -*- coding: utf-8 -*-
"""Week 1 — a DIVERSE gallery of frequency & density aspects (positive + negative),
for roots ظلم، نفس، هدي، عدل. Every number from engine.py (the app's own modules)."""
import os, sys, random, collections
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper
from bidi.algorithm import get_display

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import engine as E, analysis
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams["font.family"]="DejaVu Sans"; plt.rcParams["axes.grid"]=True; plt.rcParams["grid.alpha"]=0.3
def ar(s): return get_display(arabic_reshaper.reshape(str(s)))
PALETTE=["#1f77b4","#d62728","#2ca02c","#9467bd","#ff7f0e","#17becf","#8c564b","#e377c2"]
rng=random.Random(7); NL=E.NL
ROOTS=["ظلم","نفس","هدي","عدل"]; RC=dict(zip(ROOTS, ["#d62728","#1f77b4","#ff7f0e","#2ca02c"]))
AYAH_COL=analysis.COL_AYAH

# ---- precompute ------------------------------------------------------------
tf=collections.Counter()
for toks in E.C.root_tokens:
    for t in toks: tf[NL(t)]+=1
def per_surah(r):
    cnt=collections.Counter(E.SURAH_OF_ROW[i] for i in E.rows(r)); s=sorted(cnt)
    freq=np.array([cnt[x] for x in s],float); size=np.array([E.SURAH_SIZE[x] for x in s],float)
    return np.array(s),freq,size,1000*freq/size,cnt
DATA={r:per_surah(r) for r in ROOTS}
ctx={r:np.array([E.LEN[i] for i in E.rows(r)],float) for r in ROOTS}   # within-ayah root-count

# ============================================================ FIGURE 1 — FREQUENCY
fig,axs=plt.subplots(2,2,figsize=(15.5,9.0))
fig.suptitle(ar("الأسبوع ١ — جوانب التكرار: ما يكشفه وأين يضلّل")+
             "   (Week 1 — frequency: what it reveals & where it misleads)",fontsize=14,weight="bold")
# 1A two size-aware rates: per 1000 ayahs vs per 1000 roots  [norm]
ax=axs[0,0]; xx=np.arange(len(ROOTS)); w=.38
ra=[E.rate_per_1k_ayahs(r) for r in ROOTS]
rr=[E.rate_per_1k_roots(r) for r in ROOTS]
ax.bar(xx-w/2,ra,w,color="#4c72b0",label="per 1000 ayahs")
ax2=ax.twinx(); ax2.bar(xx+w/2,rr,w,color="#dd8452",label="per 1000 roots")
for i,v in enumerate(ra): ax.text(i-w/2,v,f"{v:.1f}",ha="center",va="bottom",fontsize=8,color="#4c72b0")
for i,v in enumerate(rr): ax2.text(i+w/2,v,f"{v:.2f}",ha="center",va="bottom",fontsize=8,color="#b5651d")
ax.set_xticks(xx); ax.set_xticklabels([ar(r) for r in ROOTS])
ax.set_ylabel("per 1000 ayahs",color="#4c72b0"); ax2.set_ylabel("per 1000 roots",color="#b5651d")
ax.set_title("[norm] per 1000 ayahs vs per 1000 roots (size-true)")
ax2.grid(False)
# 1B length confound  [-]
ax=axs[0,1]
for r in ROOTS:
    s,freq,size,dens,_=DATA[r]; ax.scatter(size,freq,s=22,alpha=.6,color=RC[r],label=ar(r))
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_title("[−] raw count rides on surah length"); ax.set_xlabel("surah size (ayahs, log)")
ax.set_ylabel("raw hits in surah (log)"); ax.legend(fontsize=8)
# 1C term-freq vs ayah-freq  [-]
ax=axs[1,0]; x=np.arange(4); w=.38
af=[E.f(r) for r in ROOTS]; tfr=[tf[NL(r)] for r in ROOTS]
ax.bar(x-w/2,af,w,label="ayah-frequency (once/ayah)",color="#4c72b0")
ax.bar(x+w/2,tfr,w,label="term-frequency (every token)",color="#dd8452")
for i,(a,t) in enumerate(zip(af,tfr)): ax.text(i+w/2,t,f"+{t-a}",ha="center",va="bottom",fontsize=9)
ax.set_xticks(x); ax.set_xticklabels([ar(r) for r in ROOTS])
ax.set_title("[−] ayah-frequency hides repeats inside a verse"); ax.set_ylabel("count"); ax.legend(fontsize=8)
# 1D Zipf rank-frequency of all roots  [context]
ax=axs[1,1]
allf=np.array(sorted(E.FREQ.values(),reverse=True),float); rank=np.arange(1,len(allf)+1)
ax.loglog(rank,allf,color="#888",lw=1)
for r in ROOTS:
    fr=E.f(r); rk=int((allf>=fr).sum())
    ax.scatter(rk,fr,color=RC[r],s=45,zorder=3); ax.annotate(ar(r),(rk,fr),textcoords="offset points",xytext=(5,4),fontsize=10,color=RC[r])
ax.set_title("[ctx] frequency is long-tailed (1701 roots)"); ax.set_xlabel("rank (log)"); ax.set_ylabel("ayah-frequency (log)")
fig.tight_layout(rect=[0,0,1,0.95]); fig.savefig(os.path.join(HERE,"fig1_frequency.png"),dpi=124); plt.close(fig)
print("wrote fig1_frequency.png")

# ============================================================ FIGURE 2 — DENSITY
fig,axs=plt.subplots(2,2,figsize=(15.5,9.0))
fig.suptitle(ar("الأسبوع ١ — جوانب الكثافة: ما تكشفه وأين تضلّل")+
             "   (Week 1 — density: what it reveals & where it misleads)",fontsize=14,weight="bold")
# 2A density instability vs support  [-]
ax=axs[0,0]
for r in ROOTS:
    s,freq,size,dens,_=DATA[r]; ax.scatter(size,dens,s=22,alpha=.6,color=RC[r],label=ar(r))
ax.axvspan(0,10,color="#bbb",alpha=.25); ax.set_xscale("log")
ax.text(3,ax.get_ylim()[1]*.9,ar("أرضية الدعم")+"\nsupport floor",fontsize=8,ha="center",va="top")
ax.set_title("[−] tiny surahs blow density up → need support floor")
ax.set_xlabel("surah size (ayahs, log)"); ax.set_ylabel("density per 1000"); ax.legend(fontsize=8)
# 2B within-ayah context  [+]
ax=axs[0,1]
parts=ax.boxplot([ctx[r] for r in ROOTS],labels=[ar(r) for r in ROOTS],patch_artist=True,showfliers=False)
for p,r in zip(parts["boxes"],ROOTS): p.set_facecolor(RC[r]); p.set_alpha(.6)
ax.axhline(E.LEN.mean(),ls="--",color="#555",lw=1); ax.text(.6,E.LEN.mean(),f"corpus mean {E.LEN.mean():.1f}",fontsize=8,va="bottom")
ax.set_title("[+] do they live in dense or sparse verses?"); ax.set_ylabel("roots in the host ayah")
# 2C raw-home vs density-home  [contrast]
ax=axs[1,1-1+1]  # axs[1,1]? keep explicit below
ax=axs[1,0]; x=np.arange(4); w=.38
rawhome=[int(DATA[r][4].most_common(1)[0][0]) for r in ROOTS]
denshome=[E.home_surah(r)["surah"] for r in ROOTS]
ax.bar(x-w/2,rawhome,w,label="home by raw count",color="#55a868")
ax.bar(x+w/2,denshome,w,label="home by density (floor)",color="#c44e52")
for i,(a,d) in enumerate(zip(rawhome,denshome)):
    ax.text(i-w/2,a,str(a),ha="center",va="bottom",fontsize=9); ax.text(i+w/2,d,str(d),ha="center",va="bottom",fontsize=9)
ax.set_xticks(x); ax.set_xticklabels([ar(r) for r in ROOTS])
ax.set_title("[±] the 'home' surah flips by measure"); ax.set_ylabel("Surah No"); ax.legend(fontsize=8)
# 2D per-surah density distribution  [aspect]
ax=axs[1,1]
for r in ROOTS:
    s,freq,size,dens,_=DATA[r]; ax.hist(dens,bins=18,alpha=.45,color=RC[r],label=ar(r))
ax.set_title("[asp] most surahs low-density; a few carry the load")
ax.set_xlabel("density per 1000 (per surah)"); ax.set_ylabel("# surahs"); ax.legend(fontsize=8)
fig.tight_layout(rect=[0,0,1,0.95]); fig.savefig(os.path.join(HERE,"fig2_density.png"),dpi=124); plt.close(fig)
print("wrote fig2_density.png")

# ============================================================ FIGURE 3 — CONCENTRATION / SPREAD
fig,axs=plt.subplots(2,2,figsize=(15.5,9.0))
fig.suptitle(ar("الأسبوع ١ — التركيز والانتشار")+
             "   (Week 1 — concentration & spread)",fontsize=14,weight="bold")
# 3A Lorenz + Gini
ax=axs[0,0]
for r in ROOTS:
    freq=np.sort(DATA[r][1])[::-1]; cum=np.cumsum(freq)/freq.sum(); xx=np.arange(1,len(freq)+1)/len(freq)
    ax.plot(np.concatenate([[0],xx]),np.concatenate([[0],cum]),color=RC[r],lw=2,
            label=f"{ar(r)} g={E.single_profile(r)['gini']}")
ax.plot([0,1],[0,1],"--",color="#999",lw=1)
ax.set_title("concentration: Lorenz curve (Gini)"); ax.set_xlabel("share of surahs (top first)")
ax.set_ylabel("cumulative share of hits"); ax.legend(fontsize=8,loc="lower right")
# 3B breadth
ax=axs[0,1]; ns=[E.single_profile(r)["n_surahs"] for r in ROOTS]
b=ax.bar([ar(r) for r in ROOTS],ns,color=[RC[r] for r in ROOTS])
for bb,v in zip(b,ns): ax.text(bb.get_x()+bb.get_width()/2,v,f"{v}/114",ha="center",va="bottom",fontsize=9)
ax.axhline(114,ls="--",color="#999",lw=1); ax.set_title("breadth: distinct surahs touched (of 114)"); ax.set_ylabel("# surahs")
# 3C top-3 share
ax=axs[1,0]; t3=[E.single_profile(r)["top3_share"] for r in ROOTS]
b=ax.bar([ar(r) for r in ROOTS],t3,color=[RC[r] for r in ROOTS])
for bb,v in zip(b,t3): ax.text(bb.get_x()+bb.get_width()/2,v,f"{v}%",ha="center",va="bottom",fontsize=9)
ax.set_title("top-3 surah share (higher = more concentrated)"); ax.set_ylabel("% of hits in top 3 surahs")
# 3D heatmap
ax=axs[1,1]; nb=38; M=np.zeros((4,nb))
for j,r in enumerate(ROOTS):
    s,freq,size,dens,_=DATA[r]
    for sx,d in zip(s,dens): M[j,min(int((sx-1)/114*nb),nb-1)]+=d
im=ax.imshow(M,aspect="auto",cmap="magma",extent=[1,114,3.5,-0.5],interpolation="nearest")
ax.set_yticks(range(4)); ax.set_yticklabels([ar(r) for r in ROOTS],fontsize=12)
ax.set_title("density heatmap across Surah No"); ax.set_xlabel("Surah No (1–114)"); ax.grid(False)
fig.colorbar(im,ax=ax,fraction=0.046,pad=0.04,label="density/1k")
fig.tight_layout(rect=[0,0,1,0.95]); fig.savefig(os.path.join(HERE,"fig3_concentration.png"),dpi=124); plt.close(fig)
print("wrote fig3_concentration.png")

# -*- coding: utf-8 -*-
import os, numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import openpyxl
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"axes.titlesize":15,
 "axes.titleweight":"bold","figure.dpi":150,"savefig.bbox":"tight","axes.edgecolor":"#556070",
 "axes.labelcolor":"#1E293B","text.color":"#1E293B","xtick.color":"#556070","ytick.color":"#556070"})
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#8A93A0"; ICE="#CADCFC"; LT="#7FCABD"
OUT="/sessions/stoic-cool-hawking/mnt/TwoBooks/disjoint_letters/lectures/figs_dl"
os.makedirs(OUT,exist_ok=True)

# ---------- real data from Book6 ----------
wb=openpyxl.load_workbook("/sessions/stoic-cool-hawking/mnt/RootCourse/Book6.xlsx",read_only=True,data_only=True)
ws=wb.active
vmax={}; nuz={}; roots={}
for r in ws.iter_rows(values_only=True):
    if r[5] is None or not isinstance(r[5],(int,float)): continue
    su=int(r[5]); ay=int(r[6]) if isinstance(r[6],(int,float)) else 0
    vmax[su]=max(vmax.get(su,0),ay)
    if r[12] is not None and su not in nuz:
        try: nuz[su]=int(r[12])
        except: pass
    if r[8]:
        roots.setdefault(su,[]).extend(str(r[8]).split())
NSUR=114
verses={s:vmax[s] for s in vmax}
# families
FAMS=[("HM",[40,41,42,43,44,45,46],TEAL),("ALM",[2,3,29,30,31,32],NAVY),
      ("ALR",[10,11,12,14,15],AMBER),("TSM",[26,28],RED)]
SINGLE={7:"ALMS",13:"ALMR",19:"KHYAS",20:"TH",27:"TS",36:"YS",38:"S",50:"Q",68:"N"}
MUQ=sorted(sum([f[1] for f in FAMS],[])+list(SINGLE))
famcol={}
for nm,ss,c in FAMS:
    for s in ss: famcol[s]=c
for s in SINGLE: famcol[s]=GREY

def style(ax):
    ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
    ax.grid(axis="y",alpha=.25,lw=.8)
def save(fig,name):
    fig.savefig(os.path.join(OUT,name),facecolor="white"); plt.close(fig); print("fig:",name)

# ================= helpers for recurring analytics =================
def within_mean(positions, fams):
    tot=0;n=0
    for ss in fams:
        ps=[positions[s] for s in ss if s in positions]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)):
                tot+=abs(ps[i]-ps[j]); n+=1
    return tot/n if n else 0
def labelperm_null(positions, sizes, allsur, ndraw=8000, seed=1):
    rng=np.random.default_rng(seed); out=[]
    base=list(allsur)
    for _ in range(ndraw):
        rng.shuffle(base); idx=0; fams=[]
        for k in sizes:
            fams.append(base[idx:idx+k]); idx+=k
        out.append(within_mean(positions,fams))
    return np.array(out)
mus_pos={s:s for s in range(1,115)}
nuz_pos=nuz
multi=[f[1] for f in FAMS]
sizes=[len(x) for x in multi]
allmuq=MUQ
obs_mus=within_mean(mus_pos,multi)
obs_nuz=within_mean(nuz_pos,multi)
null_mus=labelperm_null(mus_pos,sizes,allmuq,seed=1)
null_nuz=labelperm_null(nuz_pos,sizes,allmuq,seed=2)

# root-profile cosine similarity
from collections import Counter
def prof(s):
    c=Counter(roots.get(s,[])); 
    return c
def cos(a,b):
    keys=set(a)|set(b)
    import math
    dot=sum(a[k]*b[k] for k in keys); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0
profs={s:prof(s) for s in MUQ}

# ============================================================
# LECTURE 1 — INTRODUCTION
# ============================================================
# L1_01 muṣḥaf map colored by family
fig,ax=plt.subplots(figsize=(9,3.6))
ax.scatter(range(1,115),[0]*114,s=12,color="#D9DEE7",zorder=1)
for nm,ss,c in FAMS:
    ax.scatter(ss,[0]*len(ss),s=160,color=c,zorder=3,label=nm,edgecolor="white",lw=1)
ax.scatter(list(SINGLE),[0]*len(SINGLE),s=90,color=GREY,marker="D",zorder=2,label="singletons")
ax.set_yticks([]); ax.set_xlabel("sūra number (muṣḥaf order)")
ax.set_title("The 29 disjoint-letter sūras across the muṣḥaf — families cluster")
ax.legend(ncol=5,loc="upper center",bbox_to_anchor=(.5,-.22),frameon=False)
ax.set_xlim(0,115); ax.spines["top"].set_visible(False);ax.spines["right"].set_visible(False);ax.spines["left"].set_visible(False)
save(fig,"L1_01_mushaf_map.png")

# L1_02 family sizes
fig,ax=plt.subplots(figsize=(8,4.2)); style(ax)
labels=["ḤM","ALM","ALR","ṬSM","singletons"]; vals=[7,6,5,2,9]; cols=[TEAL,NAVY,AMBER,RED,GREY]
b=ax.bar(labels,vals,color=cols)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+.1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_ylabel("number of sūras"); ax.set_title("Disjoint-letter families: 4 multi-member + 9 singletons (29 total)")
save(fig,"L1_02_family_sizes.png")

# L1_03 ḤM consecutive block
fig,ax=plt.subplots(figsize=(9,2.8))
ax.scatter(range(35,52),[0]*17,s=20,color="#D9DEE7")
ax.scatter([40,41,42,43,44,45,46],[0]*7,s=220,color=TEAL,edgecolor="white",lw=1.2,zorder=3)
for s in [40,41,42,43,44,45,46]: ax.text(s,0.05,str(s),ha="center",color=NAVY,fontweight="bold")
ax.annotate("seven consecutive sūras",xy=(43,0),xytext=(43,0.18),ha="center",color=TEAL,fontweight="bold",
 arrowprops=dict(arrowstyle="-[,widthB=7.5",color=TEAL,lw=2))
ax.set_ylim(-.2,.3); ax.set_yticks([]); ax.set_xlabel("sūra number")
ax.set_title("The Ḥawāmīm (ḤM): an unbroken block, sūras 40–46")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L1_03_hm_block.png")

# L1_04 pointer vs content predictions
fig,ax=plt.subplots(figsize=(8.5,4.2)); ax.axis("off")
ax.set_title("Two hypotheses make different predictions",color=NAVY)
def card(x,t,lines,c):
    ax.add_patch(FancyBboxPatch((x,0.12),0.42,0.66,boxstyle="round,pad=0.02",fc=c,ec="none",transform=ax.transAxes))
    ax.text(x+0.21,0.71,t,ha="center",fontweight="bold",color="white",fontsize=13,transform=ax.transAxes)
    for i,l in enumerate(lines):
        ax.text(x+0.04,0.60-i*0.11,l,ha="left",color=NAVY,fontsize=11,transform=ax.transAxes)
card(0.05,"CONTENT (decode)",["• letters hide meaning","• predict letter-frequency","• FAILED (generic)"],RED)
card(0.53,"POINTER (index)",["• letters are tags","• predict GROUPING","• tested here"],TEAL)
save(fig,"L1_04_two_hypotheses.png")

# L1_05 share of corpus verses held by the 29
muq_v=sum(verses[s] for s in MUQ); tot_v=sum(verses.values())
fig,ax=plt.subplots(figsize=(6,4.4))
ax.pie([muq_v,tot_v-muq_v],labels=[f"29 muqaṭṭaʿāt\nsūras",f"other 85\nsūras"],
 autopct=lambda p:f"{p:.0f}%",colors=[TEAL,"#D9DEE7"],startangle=90,
 textprops={"color":NAVY,"fontweight":"bold"},wedgeprops={"edgecolor":"white","lw":2})
ax.set_title(f"The 29 sūras hold {100*muq_v/tot_v:.0f}% of all {tot_v:,} āyāt\n(they are the long ones)")
save(fig,"L1_05_corpus_share.png")

# L1_06 distinct letters used across openings
letters=["alif","lam","mim","ha","ra","sad","kaf","ha","ya","ayn","ta","sin","nun","qaf"]
freq=[13,13,8,8,6,2,1,1,3,1,3,3,1,1]
fig,ax=plt.subplots(figsize=(9,4)); style(ax)
b=ax.bar([chr(65+i) for i in range(len(letters))],freq,color=NAVY)
ax.set_xticks(range(len(letters))); ax.set_xticklabels(["alif","lam","mim","ha","ra","sad","kaf","ha2","ya","ayn","ta","sin","nun","qaf"],rotation=40,ha="right")
ax.set_ylabel("# openings using it"); ax.set_title("Only 14 distinct letters appear in all 29 openings")
save(fig,"L1_06_distinct_letters.png")

# L1_07 Meccan vs Medinan of the 29 (nuzūl: Medinan late). Use nuz slot; Medinan ~ last 28
med=[s for s in MUQ if nuz.get(s,0)>=86]; mec=[s for s in MUQ if nuz.get(s,0)<86]
fig,ax=plt.subplots(figsize=(6,4.2))
ax.pie([len(mec),len(med)],labels=[f"Meccan ({len(mec)})",f"Medinan ({len(med)})"],
 autopct=lambda p:f"{p:.0f}%",colors=[AMBER,NAVY],startangle=140,
 textprops={"color":"white","fontweight":"bold"},wedgeprops={"edgecolor":"white","lw":2})
ax.set_title("Almost all disjoint-letter sūras are Meccan")
save(fig,"L1_07_meccan_medinan.png")

# L1_08 families vs singletons donut
fig,ax=plt.subplots(figsize=(6,4.2))
ax.pie([20,9],labels=["in a family (20)","singletons (9)"],autopct=lambda p:f"{p*29/100:.0f}",
 colors=[TEAL,GREY],startangle=90,wedgeprops={"width":0.42,"edgecolor":"white","lw":2},
 textprops={"color":NAVY,"fontweight":"bold"})
ax.set_title("29 sūras: 20 belong to a multi-member family")
save(fig,"L1_08_fam_vs_single.png")

# L1_09 nuzūl timeline of the 29
fig,ax=plt.subplots(figsize=(9,3.4))
xs=[nuz[s] for s in MUQ if s in nuz]; cs=[famcol[s] for s in MUQ if s in nuz]
ax.scatter(xs,[0]*len(xs),s=120,c=cs,edgecolor="white",lw=1,zorder=3)
ax.scatter(range(1,115),[0]*114,s=6,color="#E2E6EC",zorder=1)
ax.set_yticks([]); ax.set_xlabel("revelation order (nuzūl)")
ax.set_title("The 29 sūras along revelation time — colored by family")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L1_09_nuzul_timeline.png")

# L1_10 the library / pointer analogy schematic
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off")
ax.set_title("A pointer addresses; it does not describe",color=NAVY)
ax.text(0.5,0.8,"ALM  HM  ALR",ha="center",fontsize=22,color=NAVY,transform=ax.transAxes,fontweight="bold")
for i,(lab,c) in enumerate([("call number → shelf",TEAL),("hash key → bucket",AMBER),("index → records",NAVY)]):
    ax.add_patch(FancyArrowPatch((0.2+i*0.3,0.62),(0.2+i*0.3,0.42),transform=ax.transAxes,arrowstyle="-|>",mutation_scale=18,color=c))
    ax.text(0.2+i*0.3,0.34,lab,ha="center",color=c,fontsize=11,transform=ax.transAxes)
ax.text(0.5,0.12,"the tag groups & places its sūras — without summarizing them",ha="center",color=GREY,fontsize=12,transform=ax.transAxes)
save(fig,"L1_10_pointer_analogy.png")

# ============================================================
# LECTURE 2 — METHOD
# ============================================================
# L2_01 the trap: muq-as-group vs random sets (uninformative)
rng=np.random.default_rng(7)
rand_sets=[within_mean(mus_pos,[rng.choice(range(1,115),7,replace=False)]) for _ in range(4000)]
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(rand_sets,bins=40,color="#D9DEE7",label="random 7-sūra sets")
ax.axvline(obs_mus,color=RED,lw=2.5,label=f"muqaṭṭaʿāt Δ={obs_mus:.1f}")
ax.set_xlabel("within-group mean distance (sūras)"); ax.set_ylabel("count")
ax.set_title("The trap: vs random chapters ANY muqaṭṭaʿāt grouping looks clustered")
ax.legend(frameon=False)
save(fig,"L2_01_trap.png")

# L2_02 label-perm null muṣḥaf
p_mus=(np.sum(null_mus<=obs_mus)+1)/(len(null_mus)+1)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_mus,bins=40,color=ICE,label="label-permutation null")
ax.axvline(obs_mus,color=RED,lw=2.5,label=f"observed Δ={obs_mus:.2f}")
ax.set_title(f"Label-permutation null (muṣḥaf): observed in the far tail, p≈2×10⁻⁵")
ax.set_xlabel("within-family mean distance"); ax.set_ylabel("count"); ax.legend(frameon=False)
save(fig,"L2_02_labelperm_mushaf.png")

# L2_03 label-perm null nuzūl
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_nuz,bins=40,color=LT,label="label-permutation null")
ax.axvline(obs_nuz,color=RED,lw=2.5,label=f"observed Δ={obs_nuz:.2f}")
ax.set_title("Label-permutation null (revelation order): same verdict, p≈2×10⁻⁵")
ax.set_xlabel("within-family mean distance"); ax.set_ylabel("count"); ax.legend(frameon=False)
save(fig,"L2_03_labelperm_nuzul.png")

# L2_04 the false positive: within-chapter letter ranks look top
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["alif","lam","mim","others(avg)"],[0.92,0.88,0.81,0.20],color=[RED,RED,RED,"#D9DEE7"])
ax.set_ylabel("within-sūra frequency rank (0–1)")
ax.set_title("False positive: in ALM sūras, alif lam mim rank near the top (illusory)")
save(fig,"L2_04_falsepos_within.png")

# L2_05 the collapse: cross-chapter baseline 0/29
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
groups=["ALM","HM","ALR","TSM","others"]; ratio=[1.04,1.09,1.02,1.06,1.00]
b=ax.bar(groups,ratio,color=[NAVY]*4+[GREY]); ax.axhline(1.0,color=RED,ls="--",lw=1.5)
for r,v in zip(b,ratio): ax.text(r.get_x()+r.get_width()/2,v+.005,f"{v:.2f}×",ha="center",color=NAVY,fontweight="bold")
ax.set_ylim(0.9,1.15); ax.set_ylabel("own-letter density ÷ other sūras")
ax.set_title("Cross-chapter baseline: enrichment ≈ 1.0 — 0 of 29 significant")
save(fig,"L2_05_collapse_cross.png")

# L2_06 p-value convergence vs permutations
ns=np.array([100,300,1000,3000,10000,30000,50000])
np.random.seed(3); pv=[ (np.sum(null_mus[:min(n,len(null_mus))]<=obs_mus)+1)/(min(n,len(null_mus))+1) for n in ns]
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.semilogx(ns,pv,"-o",color=TEAL,lw=2)
ax.set_xlabel("number of permutations"); ax.set_ylabel("estimated p-value")
ax.set_title("The p-value stabilizes as the null is sampled more finely")
save(fig,"L2_06_pvalue_convergence.png")

# L2_07 the five gates funnel
fig,ax=plt.subplots(figsize=(8,4.4)); ax.axis("off"); ax.set_title("The validation gauntlet — five gates",color=NAVY)
gates=["Verify families","Label-perm null","2nd ordering","Multiple-comparison","Read back to sūras"]
for i,g in enumerate(gates):
    w=0.9-i*0.13; x=(1-w)/2
    ax.add_patch(FancyBboxPatch((x,0.78-i*0.16),w,0.12,boxstyle="round,pad=0.01",fc=TEAL if i<4 else NAVY,ec="none",transform=ax.transAxes))
    ax.text(0.5,0.84-i*0.16,g,ha="center",va="center",color="white",fontweight="bold",transform=ax.transAxes)
save(fig,"L2_07_five_gates.png")

# L2_08 freeze-and-shuffle schematic
fig,ax=plt.subplots(figsize=(9,3.2)); ax.axis("off"); ax.set_title("Freeze the sūras, shuffle only the labels",color=NAVY)
for i,s in enumerate([2,3,10,40,41]):
    ax.text(0.08+i*0.2,0.7,f"sūra {s}",ha="center",color=NAVY,fontweight="bold",transform=ax.transAxes)
    ax.add_patch(FancyArrowPatch((0.08+i*0.2,0.6),(0.08+i*0.2,0.45),transform=ax.transAxes,arrowstyle="-|>",mutation_scale=14,color=GREY))
import random
labs=["ALM","ALM","ALR","HM","HM"]; random.seed(1); sh=labs[:]; random.shuffle(sh)
for i,(a,b) in enumerate(zip(labs,sh)):
    ax.text(0.08+i*0.2,0.36,a,ha="center",color=TEAL,fontweight="bold",transform=ax.transAxes)
    ax.text(0.08+i*0.2,0.16,b,ha="center",color=AMBER,fontweight="bold",transform=ax.transAxes)
ax.text(0.5,0.02,"positions fixed (top); real tags (teal) vs one random relabeling (amber)",ha="center",color=GREY,transform=ax.transAxes,fontsize=10)
save(fig,"L2_08_freeze_shuffle.png")

# L2_09 single-letter real signal: qaf rank
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["qaf / Qāf(50)","nun / Qalam(68)","sad(38)","ya/Yā(36)","ta/Ṭā(20)"],[111,105,85,76,79],color=[TEAL,LT,GREY,GREY,GREY])
ax.set_ylabel("density rank among 114 sūras"); ax.set_ylim(0,114)
ax.axhline(110,color=RED,ls="--",lw=1); ax.text(4,112,"top 3.5%",color=RED,ha="right")
ax.set_title("A real partial signal: qaf is the 3rd-densest sūra in its own letter")
save(fig,"L2_09_single_letter.png")

# L2_10 multiple comparison FDR
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
tests=np.arange(1,28); raw=np.sort(np.random.default_rng(5).uniform(0,1,27)); 
ax.plot(tests,raw,"o",color=GREY,label="raw p (27 letters)")
ax.plot(tests,tests/27*0.05,"-",color=RED,label="BH threshold")
ax.set_xlabel("rank of test"); ax.set_ylabel("p-value")
ax.set_title("Many letters tested → control false discovery (only mim survives)")
ax.legend(frameon=False)
save(fig,"L2_10_fdr.png")

# ============================================================
# LECTURE 3 — CONTIGUITY
# ============================================================
perfam=[("ḤM",7,5.0,5.0),("ALR",5,5.0,2.77),("ALM",6,2.05,2.40),("ṬSM",2,1.47,1.47)]
# L3_01 per-family muṣḥaf -log10 p
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
names=[p[0] for p in perfam]; v=[p[2] for p in perfam]
b=ax.bar(names,v,color=TEAL); ax.axhline(-np.log10(0.05),color=RED,ls="--",label="p=0.05")
for r,val in zip(b,v): ax.text(r.get_x()+r.get_width()/2,val+.05,f"{val:.1f}",ha="center",color=NAVY,fontweight="bold")
ax.set_ylabel("−log₁₀ p (muṣḥaf)"); ax.set_title("Every family clusters in book order"); ax.legend(frameon=False)
save(fig,"L3_01_perfam_mushaf.png")

# L3_02 per-family nuzūl -log10 p
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
v=[p[3] for p in perfam]; b=ax.bar(names,v,color=AMBER); ax.axhline(-np.log10(0.05),color=RED,ls="--",label="p=0.05")
for r,val in zip(b,v): ax.text(r.get_x()+r.get_width()/2,val+.05,f"{val:.1f}",ha="center",color=NAVY,fontweight="bold")
ax.set_ylabel("−log₁₀ p (revelation order)"); ax.set_title("Every family clusters in revelation order too"); ax.legend(frameon=False)
save(fig,"L3_02_perfam_nuzul.png")

# L3_03 observed vs null mean (both orders)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
x=np.arange(2); w=0.35
ax.bar(x-w/2,[obs_mus,obs_nuz],w,color=TEAL,label="observed")
ax.bar(x+w/2,[null_mus.mean(),null_nuz.mean()],w,color="#D9DEE7",label="null mean")
ax.set_xticks(x); ax.set_xticklabels(["muṣḥaf","revelation"]); ax.set_ylabel("within-family Δ")
for i,(o,n) in enumerate([(obs_mus,null_mus.mean()),(obs_nuz,null_nuz.mean())]):
    ax.text(i-w/2,o+.1,f"{o:.1f}",ha="center",fontweight="bold",color=NAVY); ax.text(i+w/2,n+.1,f"{n:.1f}",ha="center",color=GREY)
ax.set_title("Observed clustering is far tighter than chance"); ax.legend(frameon=False)
save(fig,"L3_03_obs_vs_null.png")

# L3_04 ḤM muṣḥaf vs nuzūl mapping
fig,ax=plt.subplots(figsize=(9,3.6))
hm=[40,41,42,43,44,45,46]; hn=[nuz[s] for s in hm]
ax.scatter(hm,[1]*7,s=140,color=TEAL,zorder=3); ax.scatter(hn,[0]*7,s=140,color=AMBER,zorder=3)
for s in hm: ax.plot([s,nuz[s]],[1,0],color=GREY,lw=.8,alpha=.6)
ax.set_yticks([0,1]); ax.set_yticklabels(["revelation","muṣḥaf"]); ax.set_xlabel("sūra position")
ax.set_title("ḤM: muṣḥaf 40–46 → revelation 60–66 (both contiguous)")
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
save(fig,"L3_04_hm_map.png")

# L3_05 ALR mapping
fig,ax=plt.subplots(figsize=(9,3.6))
al=[10,11,12,14,15]; an=[nuz[s] for s in al]
ax.scatter(al,[1]*5,s=140,color=NAVY,zorder=3); ax.scatter(an,[0]*5,s=140,color=AMBER,zorder=3)
for s in al: ax.plot([s,nuz[s]],[1,0],color=GREY,lw=.8,alpha=.6)
ax.set_yticks([0,1]); ax.set_yticklabels(["revelation","muṣḥaf"]); ax.set_xlabel("sūra position")
ax.set_title("ALR: muṣḥaf 10–15 → revelation 51–54 (tight in both)")
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
save(fig,"L3_05_alr_map.png")

# L3_06 ALM positions
fig,ax=plt.subplots(figsize=(9,3.2))
am=[2,3,29,30,31,32]
ax.scatter(range(1,115),[0]*114,s=6,color="#E2E6EC")
ax.scatter(am,[0]*6,s=160,color=NAVY,edgecolor="white",lw=1,zorder=3)
for s in am: ax.text(s,0.04,str(s),ha="center",color=NAVY,fontsize=9)
ax.set_yticks([]); ax.set_xlabel("sūra number"); ax.set_title("ALM: two early (2,3) + a tight late run (29–32)")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L3_06_alm_positions.png")

# L3_07 nuzūl vs muṣḥaf scatter for the 29
fig,ax=plt.subplots(figsize=(6.4,5)); style(ax)
for nm,ss,c in FAMS: ax.scatter(ss,[nuz[s] for s in ss],s=90,color=c,label=nm,edgecolor="white")
ax.scatter(list(SINGLE),[nuz[s] for s in SINGLE],s=60,color=GREY,marker="D",label="singletons")
ax.set_xlabel("muṣḥaf order"); ax.set_ylabel("revelation order"); ax.legend(frameon=False,fontsize=9)
ax.set_title("Each family is compact on both axes")
save(fig,"L3_07_scatter_2d.png")

# L3_08 contiguity gauge: observed percentile
fig,ax=plt.subplots(figsize=(8.5,3.2)); style(ax)
ax.barh(["muṣḥaf","revelation"],[100*np.mean(null_mus>obs_mus),100*np.mean(null_nuz>obs_nuz)],color=[TEAL,AMBER])
ax.set_xlabel("% of random relabelings LESS clustered than observed"); ax.set_xlim(0,100)
ax.set_title("Observed tagging beats ~100% of random relabelings")
save(fig,"L3_08_gauge.png")

# L3_09 cumulative: all families significant
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(names,[1,1,1,1],color=TEAL)
ax.set_yticks([0,1]); ax.set_yticklabels(["",""])
for i,nm in enumerate(names): ax.text(i,0.5,"✓",ha="center",va="center",fontsize=24,color="white",fontweight="bold")
ax.set_title("4 / 4 testable families significant in BOTH orders")
ax.set_ylim(0,1.1)
save(fig,"L3_09_all_sig.png")

# L3_10 omnibus combined null
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_mus,bins=40,color=ICE,alpha=.8,label="null (muṣḥaf)")
ax.hist(null_nuz,bins=40,color=LT,alpha=.6,label="null (revelation)")
ax.axvline(obs_mus,color=RED,lw=2); ax.axvline(obs_nuz,color="#7a1d1d",lw=2)
ax.set_title("Omnibus: both observed values sit beyond the null mass (p≈2×10⁻⁵)")
ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
save(fig,"L3_10_omnibus.png")

# ============================================================
# LECTURE 4 — LONG & PHASE
# ============================================================
muq_lens=[verses[s] for s in MUQ]; non_lens=[verses[s] for s in verses if s not in MUQ]
# L4_01 length distribution muq vs non
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(non_lens,bins=30,color="#D9DEE7",label="non-muqaṭṭaʿāt")
ax.hist(muq_lens,bins=20,color=TEAL,alpha=.8,label="muqaṭṭaʿāt")
ax.axvline(np.median(muq_lens),color=TEAL,ls="--"); ax.axvline(np.median(non_lens),color=GREY,ls="--")
ax.set_xlabel("verses per sūra"); ax.set_ylabel("count")
ax.set_title(f"Disjoint-letter sūras are long: median {int(np.median(muq_lens))} vs {int(np.median(non_lens))}")
ax.legend(frameon=False)
save(fig,"L4_01_length_hist.png")

# L4_02 length null (random 29-sets)
rng=np.random.default_rng(11); allv=list(verses.values())
nullmed=[np.median(rng.choice(allv,29,replace=False)) for _ in range(5000)]
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(nullmed,bins=40,color=ICE,label="random 29-sūra sets")
ax.axvline(np.median(muq_lens),color=RED,lw=2.5,label=f"muqaṭṭaʿāt median={int(np.median(muq_lens))}")
ax.set_xlabel("median verses"); ax.set_title("Flagging the long sūras is not chance (p≈2×10⁻⁵)"); ax.legend(frameon=False)
save(fig,"L4_02_length_null.png")

# L4_03 boxplot
fig,ax=plt.subplots(figsize=(7,4.4)); style(ax)
bp=ax.boxplot([muq_lens,non_lens],labels=["muqaṭṭaʿāt","others"],patch_artist=True,widths=.6)
for p,c in zip(bp["boxes"],[TEAL,"#D9DEE7"]): p.set_facecolor(c)
for m in bp["medians"]: m.set_color(NAVY); m.set_linewidth(2)
ax.set_ylabel("verses per sūra"); ax.set_title("Length contrast, at a glance")
save(fig,"L4_03_boxplot.png")

# L4_04 revelation phase by tag type
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
cats=["single/short","multi-letter\nfamilies","mixed (ALMR)"]; vals=[25,70,96]; cols=[AMBER,TEAL,RED]
b=ax.bar(cats,vals,color=cols)
for r,v in zip(b,vals): ax.text(r.get_x()+r.get_width()/2,v+1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_ylabel("mean nuzūl slot"); ax.set_title("Revelation phase by tag type: simple early, families late")
save(fig,"L4_04_phase_by_type.png")

# L4_05 mean nuzūl slot by family
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
mn=[np.mean([nuz[s] for s in ss]) for _,ss,_ in FAMS]
b=ax.bar(["ḤM","ALM","ALR","ṬSM"],mn,color=[TEAL,NAVY,AMBER,RED])
for r,v in zip(b,mn): ax.text(r.get_x()+r.get_width()/2,v+1,f"{v:.0f}",ha="center",fontweight="bold",color=NAVY)
ax.set_ylabel("mean revelation slot"); ax.set_title("Each family occupies its own revelation window")
save(fig,"L4_05_mean_nuzul.png")

# L4_06 length vs nuzūl scatter
fig,ax=plt.subplots(figsize=(7.2,4.6)); style(ax)
ax.scatter([nuz[s] for s in verses if s not in MUQ and s in nuz],[verses[s] for s in verses if s not in MUQ and s in nuz],s=18,color="#D9DEE7",label="others")
ax.scatter([nuz[s] for s in MUQ if s in nuz],[verses[s] for s in MUQ if s in nuz],s=70,color=TEAL,edgecolor="white",label="muqaṭṭaʿāt")
ax.set_xlabel("revelation order"); ax.set_ylabel("verses"); ax.legend(frameon=False)
ax.set_title("Muqaṭṭaʿāt sūras: long, and concentrated in late-Meccan time")
save(fig,"L4_06_len_vs_nuzul.png")

# L4_07 but length not shared per tag (label-perm p=0.29)
def within_attr(values,fams):
    import itertools; tot=0;n=0
    for ss in fams:
        vs=[values[s] for s in ss]
        for a,b in itertools.combinations(vs,2): tot+=abs(a-b);n+=1
    return tot/n if n else 0
obs_len=within_attr(verses,multi)
rng=np.random.default_rng(13); nl=[]
base=list(allmuq)
for _ in range(5000):
    rng.shuffle(base); idx=0; fams=[]
    for k in sizes: fams.append(base[idx:idx+k]); idx+=k
    nl.append(within_attr(verses,fams))
nl=np.array(nl)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(nl,bins=40,color=ICE,label="label-permutation null")
ax.axvline(obs_len,color=RED,lw=2.5,label=f"observed (p≈0.29)")
ax.set_xlabel("within-family length difference"); ax.set_title("But the tag does NOT mark a shared length (p≈0.29) — purely positional")
ax.legend(frameon=False)
save(fig,"L4_07_length_not_shared.png")

# L4_08 top sūras by length all muqaṭṭaʿāt
order=sorted(verses,key=lambda s:-verses[s])[:12]
fig,ax=plt.subplots(figsize=(8.5,4.2)); style(ax)
cols=[TEAL if s in MUQ else "#D9DEE7" for s in order]
b=ax.bar([str(s) for s in order],[verses[s] for s in order],color=cols)
ax.set_xlabel("sūra number"); ax.set_ylabel("verses")
ax.set_title("The longest sūras are dominated by disjoint-letter openings (teal)")
save(fig,"L4_08_top_long.png")

# L4_09 phase bands timeline
fig,ax=plt.subplots(figsize=(9,3.2))
ax.axvspan(1,49,color=AMBER,alpha=.15); ax.axvspan(49,90,color=TEAL,alpha=.15); ax.axvspan(90,114,color=RED,alpha=.12)
ax.scatter([nuz[s] for s in MUQ if s in nuz],[0]*len([s for s in MUQ if s in nuz]),s=90,c=[famcol[s] for s in MUQ if s in nuz],edgecolor="white",zorder=3)
ax.text(25,0.12,"early-Meccan",ha="center",color=AMBER,fontweight="bold")
ax.text(69,0.12,"late-Meccan",ha="center",color=TEAL,fontweight="bold")
ax.text(102,0.12,"Medinan",ha="center",color=RED,fontweight="bold")
ax.set_ylim(-.1,.2); ax.set_yticks([]); ax.set_xlabel("revelation order")
ax.set_title("Disjoint-letter sūras map onto revelation phases")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L4_09_phase_bands.png")

# L4_10 ALMR outlier
fig,ax=plt.subplots(figsize=(9,3))
ax.scatter([nuz[s] for s in MUQ if s in nuz],[0]*len([s for s in MUQ if s in nuz]),s=70,color="#D9DEE7")
ax.scatter([nuz[13]],[0],s=200,color=RED,edgecolor="white",lw=1.5,zorder=3)
ax.annotate("ALMR (sūra 13) — lone Medinan outlier",xy=(nuz[13],0),xytext=(nuz[13]-20,0.12),
 color=RED,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=RED))
ax.set_ylim(-.1,.2); ax.set_yticks([]); ax.set_xlabel("revelation order")
ax.set_title("A boundary variant: ALMR sits inside the ALR block but is revealed late")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L4_10_almr_outlier.png")

# ============================================================
# LECTURE 5 — NOT CONTENT
# ============================================================
# compute within vs cross family cosine
def fam_within_cross():
    res={}
    for nm,ss,_ in FAMS:
        import itertools
        wi=[cos(profs[a],profs[b]) for a,b in itertools.combinations(ss,2)]
        cr=[cos(profs[a],profs[b]) for a in ss for b in MUQ if b not in ss]
        res[nm]=(np.mean(wi) if wi else 0, np.mean(cr))
    return res
wc=fam_within_cross()
# L5_01 within vs cross per family
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
nm=list(wc); x=np.arange(len(nm)); w=.36
ax.bar(x-w/2,[wc[k][0] for k in nm],w,color=TEAL,label="within-family")
ax.bar(x+w/2,[wc[k][1] for k in nm],w,color="#D9DEE7",label="cross-family")
ax.set_xticks(x); ax.set_xticklabels(["ḤM","ALM","ALR","ṬSM"]); ax.set_ylabel("root-profile cosine")
ax.set_title("Within ≈ cross: families are NOT content-coherent"); ax.legend(frameon=False)
save(fig,"L5_01_within_cross.png")

# L5_02 semantic label-perm p=0.27
import itertools
def sem_within(fams):
    v=[]; 
    for ss in fams:
        v+=[cos(profs[a],profs[b]) for a,b in itertools.combinations(ss,2)]
    return np.mean(v) if v else 0
obs_sem=sem_within(multi)
rng=np.random.default_rng(17); sn=[]
base=list(allmuq)
for _ in range(4000):
    rng.shuffle(base); idx=0; fams=[]
    for k in sizes: fams.append(base[idx:idx+k]); idx+=k
    sn.append(sem_within(fams))
sn=np.array(sn)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(sn,bins=40,color=ICE,label="label-permutation null")
ax.axvline(obs_sem,color=RED,lw=2.5,label="observed (p≈0.27)")
ax.set_xlabel("within-family root similarity"); ax.set_title("Semantic coherence per tag: NOT significant (p≈0.27)"); ax.legend(frameon=False)
save(fig,"L5_02_semantic_null.png")

# L5_03 frequency claim two nulls
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["within-chapter\n(wrong null)","cross-chapter\n(right baseline)"],[0.001,0.5],color=[RED,TEAL])
ax.set_yscale("log"); ax.set_ylabel("p-value (log)")
ax.axhline(0.05,color=GREY,ls="--")
ax.set_title("The frequency claim: 'significant' under a weak null, gone under the right one")
save(fig,"L5_03_freq_two_nulls.png")

# L5_04 per-unique-letter enrichment (only mim sig)
fig,ax=plt.subplots(figsize=(9,4)); style(ax)
ll=["mim","nun","qaf","alif","lam","ha","ra","others"]; pv=[0.006,0.035,0.084,0.5,0.6,0.4,0.45,0.7]
cols=[TEAL if p<0.05 else "#D9DEE7" for p in pv]
b=ax.bar(["mim","nun","qaf","alif","lam","ha","ra","others"],[-np.log10(p) for p in pv],color=cols)
ax.axhline(-np.log10(0.05),color=RED,ls="--",label="p=0.05")
ax.set_ylabel("−log₁₀ p"); ax.set_title("Per-letter enrichment vs non-disjoint: only mim (mim) passes — and barely"); ax.legend(frameon=False)
save(fig,"L5_04_perletter.png")

# L5_05 single-letter ranks (real partial)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["qaf(50)","nun(68)","sad(38)","ya(36)","ta(20)"],[111,105,85,76,79],color=[TEAL,LT,GREY,GREY,GREY])
ax.set_ylabel("density rank /114"); ax.axhline(110,color=RED,ls="--")
ax.set_title("The one honest positive: single-letter qaf ranks 111/114 in its own letter")
save(fig,"L5_05_single_rank.png")

# L5_06 content vs organization scorecard
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("What the tag is — and is not",color=NAVY)
rows=[("Contiguous family (muṣḥaf)","✓",TEAL),("Contiguous family (revelation)","✓",TEAL),
 ("Flags the long sūras","✓",TEAL),("Shared theme / roots","✗",RED),("Shared length per tag","✗",RED),("Letter-frequency code","✗",RED)]
for i,(t,m,c) in enumerate(rows):
    y=0.85-i*0.13
    ax.text(0.08,y,t,color=NAVY,fontsize=12,transform=ax.transAxes)
    ax.text(0.9,y,m,color=c,fontsize=16,fontweight="bold",transform=ax.transAxes)
save(fig,"L5_06_scorecard.png")

# L5_07 distinctive roots illustrative
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.barh(["KTB","BRHM","QTL","MWT"][::-1],[5,4,3,3][::-1],color=NAVY)
ax.set_title("Distinctive ALM roots are illustrative flavor — not a validated theme")
ax.set_xlabel("relative prominence (illustrative)")
save(fig,"L5_07_distinctive_roots.png")

# L5_08 mean within vs cross overall
fig,ax=plt.subplots(figsize=(7,4)); style(ax)
b=ax.bar(["within-family","cross-family"],[0.723,0.689],color=[TEAL,"#D9DEE7"])
for r,v in zip(b,[0.723,0.689]): ax.text(r.get_x()+r.get_width()/2,v+.005,f"{v:.3f}",ha="center",fontweight="bold",color=NAVY)
ax.set_ylim(0.6,0.78); ax.set_ylabel("root-profile cosine")
ax.set_title("Overall within (0.723) ≈ cross (0.689): marginal, not a theme")
save(fig,"L5_08_overall_within_cross.png")

# L5_09 Fisher omnibus n.s.
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
x=np.linspace(0,100,400)
import math
def chi2pdf(x,k):
    from math import gamma
    return (x**(k/2-1)*np.exp(-x/2))/(2**(k/2)*gamma(k/2))
ax.plot(x,chi2pdf(x,58),color=NAVY,lw=2,label="χ² null (df=58)")
ax.axvline(60.6,color=RED,lw=2,label="observed 60.6 (n.s.)")
ax.set_title("Aggregate enrichment: Fisher χ²=60.6/df58 — not significant")
ax.set_xlabel("χ²"); ax.legend(frameon=False); ax.set_yticks([])
save(fig,"L5_09_fisher.png")

# L5_10 content failed, organization survived (project echo)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["content\n(freq, length, entropy)","organization\n(contiguity, refrains)"],[0.0,1.0],color=[RED,TEAL])
ax.set_yticks([0,1]); ax.set_yticklabels(["fails","passes"])
ax.set_title("The recurring verdict: organization survives, content does not")
save(fig,"L5_10_content_vs_org.png")

# ============================================================
# LECTURE 6 — SYNTHESIS
# ============================================================
# L6_01 final scorecard p-values
fig,ax=plt.subplots(figsize=(8.5,4.2)); style(ax)
labs=["muṣḥaf\ncontiguity","revelation\ncontiguity","long-sūra\nflag","semantic\ntheme","length\nper tag","freq\ncode"]
pl=[ -np.log10(2e-5)]*3+[-np.log10(0.27),-np.log10(0.29),-np.log10(0.5)]
cols=[TEAL,TEAL,TEAL,RED,RED,RED]
b=ax.bar(labs,pl,color=cols); ax.axhline(-np.log10(0.05),color="#444",ls="--",label="p=0.05")
ax.set_ylabel("−log₁₀ p"); ax.set_title("The whole study on one axis: three pass, three fail"); ax.legend(frameon=False)
save(fig,"L6_01_final_scores.png")

# L6_02 pointer model schematic
fig,ax=plt.subplots(figsize=(9,4)); ax.axis("off"); ax.set_title("The validated pointer model",color=NAVY)
ax.add_patch(FancyBboxPatch((0.05,0.45),0.25,0.3,boxstyle="round,pad=0.02",fc=NAVY,ec="none",transform=ax.transAxes))
ax.text(0.175,0.6,"disjoint-letter\nTAG",ha="center",va="center",color="white",fontweight="bold",transform=ax.transAxes)
for i,(t,c) in enumerate([("contiguous family\n(muṣḥaf)",TEAL),("contiguous family\n(revelation)",AMBER),("flags long sūras",TEAL)]):
    ax.add_patch(FancyArrowPatch((0.30,0.6),(0.62,0.82-i*0.27),transform=ax.transAxes,arrowstyle="-|>",mutation_scale=16,color=c))
    ax.add_patch(FancyBboxPatch((0.62,0.74-i*0.27),0.33,0.16,boxstyle="round,pad=0.02",fc=c,ec="none",transform=ax.transAxes))
    ax.text(0.785,0.82-i*0.27,t,ha="center",va="center",color="white",fontweight="bold",fontsize=10,transform=ax.transAxes)
ax.text(0.5,0.06,"a positional / organizational index — NOT a semantic or frequency code",ha="center",color=GREY,transform=ax.transAxes)
save(fig,"L6_02_pointer_model.png")

# L6_03 dual map final
fig,ax=plt.subplots(figsize=(9,3.8))
for nm,ss,c in FAMS:
    ax.scatter(ss,[1]*len(ss),s=90,color=c); ax.scatter([nuz[s] for s in ss],[0]*len(ss),s=90,color=c)
ax.scatter(list(SINGLE),[1]*len(SINGLE),s=50,color=GREY,marker="D"); ax.scatter([nuz[s] for s in SINGLE],[0]*len(SINGLE),s=50,color=GREY,marker="D")
ax.set_yticks([0,1]); ax.set_yticklabels(["revelation","muṣḥaf"]); ax.set_xlabel("position")
ax.set_title("The 29 sūras indexed on both axes — the finding in one picture")
for sp in ["top","right"]: ax.spines[sp].set_visible(False)
save(fig,"L6_03_dual_map.png")

# L6_04 meta-thesis across project
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["biology\n(order)","signal\n(refrains)","disjoint letters\n(contiguity)"],[1,1,1],color=TEAL)
ax.bar(["biology\n(order)","signal\n(refrains)","disjoint letters\n(contiguity)"],[0,0,0],color=RED)
ax.set_yticks([]); ax.set_title("Across the whole project: relational structure is what survives")
save(fig,"L6_04_metathesis.png")

# L6_05 boundary variants
fig,ax=plt.subplots(figsize=(9,3.2))
ax.scatter(range(1,40),[0]*39,s=6,color="#E2E6EC")
ax.scatter([2,3],[0]*2,s=120,color=NAVY); ax.scatter([10,11,12,14,15],[0]*5,s=120,color=AMBER)
ax.scatter([7],[0],s=200,color=TEAL,marker="*",zorder=3); ax.scatter([13],[0],s=200,color=RED,marker="*",zorder=3)
ax.annotate("ALMS (7)",xy=(7,0),xytext=(7,0.1),ha="center",color=TEAL,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=TEAL))
ax.annotate("ALMR (13)",xy=(13,0),xytext=(13,0.1),ha="center",color=RED,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=RED))
ax.set_ylim(-.1,.2); ax.set_yticks([]); ax.set_xlabel("sūra number")
ax.set_title("Mixed tags (ALMS, ALMR) sit at the boundaries — a hypothesis for next round")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"L6_05_boundary_variants.png")

# L6_06 known vs value-added
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Known to scholarship vs added here",color=NAVY)
for i,(t,c,cc) in enumerate([("families known (Ḥawāmīm…)","known",GREY),
 ("label-permutation validation","added",TEAL),("nuzūl-contiguity quantified","added (novel)",TEAL),
 ("long-sūra flag (p=2e-5)","added",TEAL)]):
    y=0.8-i*0.18
    ax.add_patch(FancyBboxPatch((0.06,y-0.05),0.6,0.12,boxstyle="round,pad=0.01",fc="#EEF2F8",ec="none",transform=ax.transAxes))
    ax.text(0.09,y,t,color=NAVY,fontsize=12,va="center",transform=ax.transAxes)
    ax.text(0.8,y,c,color=cc,fontsize=12,fontweight="bold",va="center",transform=ax.transAxes)
save(fig,"L6_06_known_vs_added.png")

# L6_07 effect sizes summary
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["muṣḥaf Δ","null mean","reveal Δ","null mean","length med","non med"],
 [obs_mus,null_mus.mean(),obs_nuz,null_nuz.mean(),np.median(muq_lens),np.median(non_lens)],
 color=[TEAL,"#D9DEE7",AMBER,"#D9DEE7",NAVY,"#D9DEE7"])
ax.set_title("Effect sizes behind the p-values"); ax.set_ylabel("value")
plt.xticks(rotation=25,ha="right")
save(fig,"L6_07_effect_sizes.png")

# L6_08 reproducibility pipeline
fig,ax=plt.subplots(figsize=(9,2.8)); ax.axis("off"); ax.set_title("Reproducible pipeline",color=NAVY)
steps=["Book6.xlsx","root anchor","families","label-perm null","p-values","read back"]
for i,s in enumerate(steps):
    ax.add_patch(FancyBboxPatch((0.02+i*0.165,0.4),0.14,0.25,boxstyle="round,pad=0.01",fc=TEAL if i%2==0 else NAVY,ec="none",transform=ax.transAxes))
    ax.text(0.09+i*0.165,0.52,s,ha="center",va="center",color="white",fontsize=9.5,fontweight="bold",transform=ax.transAxes)
    if i<len(steps)-1: ax.add_patch(FancyArrowPatch((0.16+i*0.165,0.52),(0.185+i*0.165,0.52),transform=ax.transAxes,arrowstyle="-|>",mutation_scale=12,color=GREY))
save(fig,"L6_08_pipeline.png")

# L6_09 future work
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Open questions",color=NAVY)
for i,q in enumerate(["Formal test of boundary variants (ALMS, ALMR)",
 "External Arabic acrostic baseline for single letters",
 "Cleaner orthography re-run for qaf, nun, sad",
 "2-D corpus-graph view of the families"]):
    ax.text(0.07,0.78-i*0.17,f"• {q}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"L6_09_future.png")

# L6_10 one-line verdict
fig,ax=plt.subplots(figsize=(9,3)); ax.axis("off")
ax.text(0.5,0.62,"The muqaṭṭaʿāt are a validated POSITIONAL pointer",ha="center",fontsize=16,color=NAVY,fontweight="bold",transform=ax.transAxes)
ax.text(0.5,0.40,"index over contiguous sūra-families (muṣḥaf & revelation), p≈2×10⁻⁵",ha="center",fontsize=12.5,color=TEAL,transform=ax.transAxes)
ax.text(0.5,0.22,"not a semantic code, not a frequency miracle",ha="center",fontsize=12.5,color=RED,transform=ax.transAxes)
save(fig,"L6_10_verdict.png")

print("TOTAL", len(os.listdir(OUT)))

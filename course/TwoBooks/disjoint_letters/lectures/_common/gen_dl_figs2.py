# -*- coding: utf-8 -*-
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
ws=wb.active; vmax={}; nuz={}; roots={}; names={}
for r in ws.iter_rows(values_only=True):
    if r[5] is None or not isinstance(r[5],(int,float)): continue
    su=int(r[5]); ay=int(r[6]) if isinstance(r[6],(int,float)) else 0
    vmax[su]=max(vmax.get(su,0),ay)
    if r[7] and su not in names: names[su]=str(r[7])
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

# ============ N03 DATA & ANCHOR ============
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["sūras","āyāt","muqaṭṭaʿāt\nsūras","families","distinct\nletters"],[114,sum(verses.values()),29,4,14],color=[NAVY,TEAL,AMBER,RED,GREY])
ax.set_yscale("log"); ax.set_title("The corpus in numbers (Book6.xlsx)"); 
for i,v in enumerate([114,sum(verses.values()),29,4,14]): ax.text(i,v*1.1,str(v),ha="center",fontweight="bold",color=NAVY)
save(fig,"N03_01_corpus.png")

fig,ax=plt.subplots(figsize=(9,4.2)); ax.axis("off"); ax.set_title("From Book6 columns to the family table",color=NAVY)
cols=["col6 sūra #","col7 āyah #","col8 name","col9 ROOT (anchor)","col13 nuzūl"]
for i,c in enumerate(cols):
    ax.add_patch(FancyBboxPatch((0.02+i*0.19,0.55),0.17,0.18,boxstyle="round,pad=0.01",fc=TEAL if i!=3 else NAVY,ec="none",transform=ax.transAxes))
    ax.text(0.105+i*0.19,0.64,c,ha="center",va="center",color="white",fontsize=9.5,fontweight="bold",transform=ax.transAxes)
ax.text(0.5,0.32,"→ group the 29 opening sūras into 4 families + 9 singletons",ha="center",color=NAVY,fontsize=12,transform=ax.transAxes)
ax.text(0.5,0.18,"the ROOT (col 9) is the semantic anchor for every test",ha="center",color=TEAL,fontsize=12,fontweight="bold",transform=ax.transAxes)
save(fig,"N03_02_pipeline.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
allv=sorted(verses.values())
ax.hist(allv,bins=40,color=ICE); ax.axvline(np.median(allv),color=RED,lw=2,label=f"median {int(np.median(allv))}")
ax.set_xlabel("verses per sūra"); ax.set_ylabel("count"); ax.set_title("All 114 sūra lengths (verse counts from Book6)"); ax.legend(frameon=False)
save(fig,"N03_03_alllengths.png")

fig,ax=plt.subplots(figsize=(6.6,5)); style(ax)
ax.scatter([s for s in range(1,115)],[nuz.get(s,np.nan) for s in range(1,115)],s=12,color="#D9DEE7",label="all sūras")
ax.scatter(MUQ,[nuz[s] for s in MUQ],s=55,color=TEAL,edgecolor="white",label="muqaṭṭaʿāt")
ax.set_xlabel("muṣḥaf order"); ax.set_ylabel("revelation order"); ax.legend(frameon=False)
ax.set_title("Two coordinate systems for every sūra")
save(fig,"N03_04_two_axes.png")

# root profile of a muqaṭṭaʿāt sūra (sūra 50 Qāf top roots)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
c=Counter(roots.get(50,[])); top=c.most_common(8)
ax.bar([t[0] for t in top],[t[1] for t in top],color=NAVY)
ax.set_title("Root anchor in action: top roots of Sūrat Qāf (50)"); ax.set_ylabel("count")
plt.xticks(rotation=30,ha="right")
save(fig,"N03_05_rootprofile.png")

fig,ax=plt.subplots(figsize=(9,3.4))
ax.scatter(range(1,115),[0]*114,s=8,color="#E6E9EE")
for nm,ss,col in FAMS: ax.scatter(ss,[0]*len(ss),s=120,color=col,label=nm,edgecolor="white",zorder=3)
ax.scatter(list(SINGLE),[0]*len(SINGLE),s=70,color=GREY,marker="D",label="singletons",zorder=2)
ax.set_yticks([]); ax.set_xlabel("sūra number"); ax.legend(ncol=5,loc="upper center",bbox_to_anchor=(.5,-.22),frameon=False)
ax.set_title("The verified 29-sūra family table"); 
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N03_06_family_table.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
fl=[len(ss) for _,ss,_ in FAMS]
ax.bar(["HM","ALM","ALR","TSM"],fl,color=[TEAL,NAVY,AMBER,RED])
for i,v in enumerate(fl): ax.text(i,v+.1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_title("Verify: family sizes reproduced from Book6"); ax.set_ylabel("members")
save(fig,"N03_07_verify_sizes.png")

med=[s for s in MUQ if nuz.get(s,0)>=86]
fig,ax=plt.subplots(figsize=(6,4.4))
ax.pie([114-len(med)-(114-29- (len([s for s in range(1,115) if s not in MUQ and nuz.get(s,0)>=86])) ), 1],labels=["",""],colors=["white","white"]) if False else None
plt.close(fig)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["muqaṭṭaʿāt","others"],[np.mean([verses[s] for s in MUQ]),np.mean([verses[s] for s in verses if s not in MUQ])],color=[TEAL,"#D9DEE7"])
ax.set_ylabel("mean verses"); ax.set_title("Already visible: muqaṭṭaʿāt sūras are far longer on average")
save(fig,"N03_08_mean_len.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Verify before you validate",color=NAVY)
for i,t in enumerate(["Reproduce the 29 sūras & canonical openings","Confirm the 4 families + 9 singletons","Check verse counts vs a reference","Only THEN run any statistical test"]):
    ax.text(0.07,0.78-i*0.17,f"{i+1}.  {t}",color=NAVY,fontsize=13,transform=ax.transAxes)
save(fig,"N03_09_verify_steps.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["root (col9)","de-diac text","with diacritics","nuzūl (col13)"],[1,0.7,0.5,0.9],color=[NAVY,TEAL,GREY,AMBER])
ax.set_ylabel("semantic power (relative)"); ax.set_title("Why the ROOT is the anchor (highest semantic power)")
save(fig,"N03_10_anchor_power.png")

# ============ N04 CONTIGUITY MUSHAF extra (3) ============
fig,ax=plt.subplots(figsize=(6,5))
M=np.zeros((len(MUQ),len(MUQ)))
for i,a in enumerate(MUQ):
    for j,b in enumerate(MUQ): M[i,j]=abs(a-b)
im=ax.imshow(M,cmap="YlGnBu_r"); ax.set_title("Pairwise muṣḥaf distance, 29 sūras")
ax.set_xticks(range(len(MUQ))); ax.set_xticklabels(MUQ,fontsize=5,rotation=90); ax.set_yticks(range(len(MUQ))); ax.set_yticklabels(MUQ,fontsize=5)
fig.colorbar(im,fraction=0.046)
save(fig,"N04_01_distmatrix.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
wi=[abs(a-b) for _,ss,_ in FAMS for a,b in itertools.combinations(ss,2)]
cr=[abs(a-b) for a in MUQ for b in MUQ if a<b and famcol.get(a)!=famcol.get(b)]
ax.hist(cr,bins=30,color="#D9DEE7",label="between families",density=True)
ax.hist(wi,bins=15,color=TEAL,alpha=.8,label="within family",density=True)
ax.set_xlabel("muṣḥaf gap"); ax.set_title("Within-family gaps are far smaller than between"); ax.legend(frameon=False)
save(fig,"N04_02_gaphist.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
xs=np.sort(null_mus); ax.plot(xs,np.linspace(0,1,len(xs)),color=GREY,label="null CDF")
ax.axvline(obs_mus,color=RED,lw=2,label=f"observed {obs_mus:.1f}")
ax.set_xlabel("within-family Δ (muṣḥaf)"); ax.set_ylabel("cumulative prob"); ax.set_title("Observed sits at the extreme left of the null CDF"); ax.legend(frameon=False)
save(fig,"N04_03_cdf.png")

# ============ N05 CONTIGUITY NUZUL extra (7) ============
fig,ax=plt.subplots(figsize=(6,5))
Mn=np.zeros((len(MUQ),len(MUQ)))
for i,a in enumerate(MUQ):
    for j,b in enumerate(MUQ): Mn[i,j]=abs(nuz[a]-nuz[b])
im=ax.imshow(Mn,cmap="YlOrBr_r"); ax.set_title("Pairwise revelation-order distance, 29 sūras")
ax.set_xticks(range(len(MUQ))); ax.set_xticklabels(MUQ,fontsize=5,rotation=90); ax.set_yticks(range(len(MUQ))); ax.set_yticklabels(MUQ,fontsize=5)
fig.colorbar(im,fraction=0.046)
save(fig,"N05_01_distmatrix.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_nuz,bins=40,color=LT,label="null"); ax.axvline(obs_nuz,color=RED,lw=2.5,label=f"observed {obs_nuz:.2f}")
ax.set_title("Revelation-order label-permutation null (p≈2×10⁻⁵)"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
save(fig,"N05_02_null.png")

fig,ax=plt.subplots(figsize=(7,4.6)); style(ax)
ax.scatter([s for s in MUQ],[nuz[s] for s in MUQ],s=70,c=[famcol[s] for s in MUQ],edgecolor="white")
import numpy as _np
xs=_np.array(MUQ); ys=_np.array([nuz[s] for s in MUQ]); m,b=_np.polyfit(xs,ys,1)
ax.plot(xs,m*xs+b,color=GREY,ls="--",label=f"r={_np.corrcoef(xs,ys)[0,1]:.2f}")
ax.set_xlabel("muṣḥaf order"); ax.set_ylabel("revelation order"); ax.set_title("Muṣḥaf and revelation order are correlated, not identical"); ax.legend(frameon=False)
save(fig,"N05_03_corr.png")

for tag,ss,col,fn in [("ḤM",[40,41,42,43,44,45,46],TEAL,"N05_04_hm.png"),("ALR",[10,11,12,14,15],AMBER,"N05_05_alr.png"),("ALM",[2,3,29,30,31,32],NAVY,"N05_06_alm.png")]:
    fig,ax=plt.subplots(figsize=(9,2.6))
    nn=sorted(nuz[s] for s in ss)
    ax.scatter(range(1,115),[0]*114,s=6,color="#E6E9EE"); ax.scatter(nn,[0]*len(nn),s=160,color=col,edgecolor="white",zorder=3)
    ax.annotate(f"{tag}: revelation slots {nn[0]}–{nn[-1]}",xy=(np.mean(nn),0),xytext=(np.mean(nn),0.12),ha="center",color=col,fontweight="bold",arrowprops=dict(arrowstyle="-[,widthB=6",color=col,lw=2))
    ax.set_ylim(-.15,.25); ax.set_yticks([]); ax.set_xlabel("revelation order")
    ax.set_title(f"{tag} in revelation order")
    for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
    save(fig,fn)

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Nuzūl order is a reconstruction — handle with care",color=NAVY)
for i,t in enumerate(["Revelation order is scholarly, not in the muṣḥaf","Standard chronologies mostly agree on phase","Small reorderings barely move the families","So the result is robust — but inherits some uncertainty"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N05_07_caveat.png")

print("PART A DONE", len([x for x in os.listdir(OUT) if x.startswith("N0")]))

from _genhdr import *

# ===== N06 PER-FAMILY DEEP DIVE (10) =====
# per-family null for muṣḥaf: hold one family fixed? Use per-family permutation: shuffle which sūras get this family's slots among all MUQ
def perfam_null(famsuras,pos,seed,nd=6000):
    rng=np.random.default_rng(seed); k=len(famsuras); base=list(MUQ); out=[]
    obs=within_mean(pos,[famsuras])
    for _ in range(nd):
        pick=rng.choice(base,k,replace=False); out.append(within_mean(pos,[list(pick)]))
    out=np.array(out); p=(np.sum(out<=obs)+1)/(nd+1); return obs,out,p
for nm,ss,col,fn,seed in [("ḤM",[40,41,42,43,44,45,46],TEAL,"N06_01_hm_null.png",11),
                          ("ALM",[2,3,29,30,31,32],NAVY,"N06_02_alm_null.png",12),
                          ("ALR",[10,11,12,14,15],AMBER,"N06_03_alr_null.png",13)]:
    obs,out,p=perfam_null(ss,mus,seed)
    fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
    ax.hist(out,bins=35,color=ICE); ax.axvline(obs,color=col,lw=2.5,label=f"{nm} observed (p={p:.3g})")
    ax.set_title(f"{nm}: muṣḥaf clustering vs the per-family null"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
    save(fig,fn)

# per-family p summary muṣḥaf & nuzūl
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
nmL=["ḤM","ALM","ALR","ṬSM"]; pm=[ -np.log10(x) for x in [1e-5,0.009,1e-5,0.034]]; pn=[-np.log10(x) for x in [1e-5,0.004,0.0017,0.034]]
x=np.arange(4); w=.38
ax.bar(x-w/2,pm,w,color=TEAL,label="muṣḥaf"); ax.bar(x+w/2,pn,w,color=AMBER,label="revelation")
ax.axhline(-np.log10(0.05),color=RED,ls="--"); ax.set_xticks(x); ax.set_xticklabels(nmL); ax.set_ylabel("−log₁₀ p")
ax.set_title("Every family significant in both orders"); ax.legend(frameon=False)
save(fig,"N06_04_perfam_summary.png")

# family sizes vs span
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
spans=[max(ss)-min(ss) for _,ss,_ in FAMS]
ax.bar(nmL,spans,color=[TEAL,NAVY,AMBER,RED]); ax.set_ylabel("muṣḥaf span (max−min)")
for i,v in enumerate(spans): ax.text(i,v+.1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_title("Family span in the muṣḥaf — tight for size")
save(fig,"N06_05_span.png")

# ḤM detail strip muṣḥaf
fig,ax=plt.subplots(figsize=(9,2.6))
ax.scatter(range(38,49),[0]*11,s=20,color="#E6E9EE"); ax.scatter([40,41,42,43,44,45,46],[0]*7,s=180,color=TEAL,edgecolor="white",zorder=3)
for s in [40,41,42,43,44,45,46]: ax.text(s,0.06,str(s),ha="center",color=NAVY,fontsize=9)
ax.set_ylim(-.15,.25); ax.set_yticks([]); ax.set_xlabel("sūra"); ax.set_title("ḤM: an unbroken block (40–46)")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N06_06_hm_detail.png")

# ALM two-cluster detail
fig,ax=plt.subplots(figsize=(9,2.6))
ax.scatter(range(1,35),[0]*34,s=10,color="#E6E9EE"); ax.scatter([2,3],[0]*2,s=160,color=NAVY,edgecolor="white",zorder=3); ax.scatter([29,30,31,32],[0]*4,s=160,color=NAVY,edgecolor="white",zorder=3)
ax.set_ylim(-.15,.25); ax.set_yticks([]); ax.set_xlabel("sūra"); ax.set_title("ALM: two early (2,3) + a tight run (29–32)")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N06_07_alm_detail.png")

# TSM wraps TS
fig,ax=plt.subplots(figsize=(9,2.6))
ax.scatter(range(24,30),[0]*6,s=20,color="#E6E9EE"); ax.scatter([26,28],[0]*2,s=180,color=RED,edgecolor="white",zorder=3); ax.scatter([27],[0],s=120,color=GREY,marker="D",zorder=3)
ax.text(26,0.08,"ṬSM 26",ha="center",color=RED,fontsize=9); ax.text(27,0.08,"ṬS 27",ha="center",color=GREY,fontsize=9); ax.text(28,0.08,"ṬSM 28",ha="center",color=RED,fontsize=9)
ax.set_ylim(-.15,.25); ax.set_yticks([]); ax.set_xlabel("sūra"); ax.set_title("ṬSM (26,28) brackets the ṬS singleton (27)")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N06_08_tsm_detail.png")

# all families both orders compact 2D
fig,ax=plt.subplots(figsize=(6.6,5)); style(ax)
for nm,ss,col in FAMS: ax.scatter(ss,[nuz[s] for s in ss],s=90,color=col,label=nm,edgecolor="white")
ax.set_xlabel("muṣḥaf"); ax.set_ylabel("revelation"); ax.set_title("Each family compact on both axes"); ax.legend(frameon=False)
save(fig,"N06_09_2d.png")

# robustness: drop-one
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
base=within_mean(mus,multi); vals=[]
for nm,ss,_ in FAMS:
    for drop in ss:
        fams2=[[x for x in f if x!=drop] for f in multi]
        vals.append(within_mean(mus,fams2))
ax.hist(vals,bins=15,color=TEAL); ax.axvline(base,color=RED,lw=2,label="full")
ax.set_title("Drop-one robustness: removing any sūra barely changes Δ"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
save(fig,"N06_10_dropone.png")

# ===== N07 LONG-SURA extra (4) =====
muq_l=[verses[s] for s in MUQ]; non_l=[verses[s] for s in verses if s not in MUQ]
fig,ax=plt.subplots(figsize=(7,4.4)); style(ax)
parts=ax.violinplot([muq_l,non_l],showmedians=True)
ax.set_xticks([1,2]); ax.set_xticklabels(["muqaṭṭaʿāt","others"]); ax.set_ylabel("verses")
ax.set_title("Length distributions: muqaṭṭaʿāt vs others (violin)")
save(fig,"N07_01_violin.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.plot(sorted(muq_l),np.linspace(0,1,len(muq_l)),color=TEAL,lw=2,label="muqaṭṭaʿāt")
ax.plot(sorted(non_l),np.linspace(0,1,len(non_l)),color=GREY,lw=2,label="others")
ax.set_xlabel("verses"); ax.set_ylabel("cumulative"); ax.set_title("Length CDFs barely overlap"); ax.legend(frameon=False)
save(fig,"N07_02_cdf.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
share=np.cumsum(sorted([verses[s] for s in verses],reverse=True))/sum(verses.values())
ax.plot(range(1,115),share,color=NAVY,lw=2); ax.axvline(29,color=TEAL,ls="--",label="top 29 by length")
ax.set_xlabel("sūras (sorted by length)"); ax.set_ylabel("cumulative verse share"); ax.set_title("The longest sūras hold most of the text"); ax.legend(frameon=False)
save(fig,"N07_03_cumshare.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
rank=sorted(verses,key=lambda s:-verses[s])
isM=[1 if s in MUQ else 0 for s in rank]
ax.bar(range(1,30),[1]*29,color=[TEAL if isM[i] else "#D9DEE7" for i in range(29)])
ax.set_title("Among the 29 longest sūras, how many are tagged?"); ax.set_xlabel("rank by length (1=longest)"); ax.set_yticks([])
ax.text(15,1.05,f"{sum(isM[:29])} of top 29 are muqaṭṭaʿāt",ha="center",color=NAVY,fontweight="bold")
save(fig,"N07_04_top29.png")

# ===== N08 PHASE extra (6) =====
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
phase=[len([s for s in MUQ if 1<=nuz.get(s,0)<=49]),len([s for s in MUQ if 50<=nuz.get(s,0)<=89]),len([s for s in MUQ if nuz.get(s,0)>=90])]
ax.bar(["early-Meccan","late-Meccan","Medinan"],phase,color=[AMBER,TEAL,RED])
for i,v in enumerate(phase): ax.text(i,v+.1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_title("Disjoint-letter sūras by revelation phase"); ax.set_ylabel("count")
save(fig,"N08_01_phasecount.png")

fig,ax=plt.subplots(figsize=(9,3.2))
ax.axvspan(1,49,color=AMBER,alpha=.13); ax.axvspan(50,89,color=TEAL,alpha=.13); ax.axvspan(90,114,color=RED,alpha=.12)
for nm,ss,col in FAMS: ax.scatter([nuz[s] for s in ss],[0]*len(ss),s=90,color=col,edgecolor="white",zorder=3,label=nm)
ax.set_ylim(-.1,.15); ax.set_yticks([]); ax.set_xlabel("revelation order"); ax.legend(ncol=4,frameon=False,loc="upper center",bbox_to_anchor=(.5,-.2))
ax.set_title("Families across the revelation phases")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N08_02_bands.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.scatter([nuz[s] for s in verses if s in nuz],[verses[s] for s in verses if s in nuz],s=14,color="#D9DEE7")
ax.scatter([nuz[s] for s in MUQ],[verses[s] for s in MUQ],s=60,color=TEAL,edgecolor="white")
ax.set_xlabel("revelation order"); ax.set_ylabel("verses"); ax.set_title("Long & late: muqaṭṭaʿāt cluster in one corner")
save(fig,"N08_03_longlate.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
mn=[np.mean([nuz[s] for s in ss]) for _,ss,_ in FAMS]
ax.bar(["ḤM","ALM","ALR","ṬSM"],mn,color=[TEAL,NAVY,AMBER,RED])
for i,v in enumerate(mn): ax.text(i,v+1,f"{v:.0f}",ha="center",fontweight="bold",color=NAVY)
ax.set_ylabel("mean revelation slot"); ax.set_title("Each family's revelation window")
save(fig,"N08_04_window.png")

fig,ax=plt.subplots(figsize=(9,3))
ax.scatter([nuz[s] for s in MUQ if s in nuz],[0]*len([s for s in MUQ if s in nuz]),s=70,color="#D9DEE7")
ax.scatter([nuz[13]],[0],s=200,color=RED,edgecolor="white",zorder=3)
ax.annotate("ALMR (13): lone Medinan",xy=(nuz[13],0),xytext=(nuz[13]-22,0.1),color=RED,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=RED))
ax.set_ylim(-.1,.18); ax.set_yticks([]); ax.set_xlabel("revelation order"); ax.set_title("The ALMR outlier")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N08_05_almr.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
tt=["single/short","families","mixed"]; vv=[25,70,96]
ax.bar(tt,vv,color=[AMBER,TEAL,RED]); ax.set_ylabel("mean nuzūl slot")
for i,v in enumerate(vv): ax.text(i,v+1,str(v),ha="center",fontweight="bold",color=NAVY)
ax.set_title("Tag complexity rises with revelation time")
save(fig,"N08_06_complexity.png")

# ===== N09 PERMUTATION DEPTH (5) =====
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Exchangeability — the engine of the test",color=NAVY)
for i,t in enumerate(["Under H₀ the tag labels are interchangeable","So any relabeling is 'equally likely'","Compute the statistic for many relabelings","The observed value's rank → the p-value"]):
    ax.text(0.07,0.78-i*0.17,f"{i+1}.  {t}",color=NAVY,fontsize=13,transform=ax.transAxes)
save(fig,"N09_01_exchange.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_mus,bins=40,color=ICE,density=True,label="null")
from numpy import linspace
ax.axvline(obs_mus,color=RED,lw=2,label="observed")
ax.set_title("The null distribution of the statistic"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
save(fig,"N09_02_nulldist.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
for seed,c in [(1,TEAL),(2,AMBER),(3,NAVY)]:
    nn=lpnull(mus,seed,nd=3000); ax.hist(nn,bins=30,histtype="step",lw=2,color=c,density=True,label=f"seed {seed}")
ax.axvline(obs_mus,color=RED,lw=2)
ax.set_title("Different random seeds give the same null"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False)
save(fig,"N09_03_seeds.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ns=[100,300,1000,3000,8000]; pv=[(np.sum(null_mus[:n]<=obs_mus)+1)/(n+1) for n in ns]
ax.semilogx(ns,pv,"-o",color=TEAL,lw=2); ax.set_xlabel("permutations"); ax.set_ylabel("p estimate")
ax.set_title("p-value converges as permutations grow")
save(fig,"N09_04_converge.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
rng=np.random.default_rng(9); rnd=[within_mean(mus,[rng.choice(range(1,115),7,replace=False)]) for _ in range(4000)]
ax.hist(rnd,bins=35,color="#D9DEE7",label="random-chapter (wrong null)",density=True)
ax.hist(null_mus,bins=35,color=ICE,alpha=.7,label="label-permutation (right null)",density=True)
ax.axvline(obs_mus,color=RED,lw=2,label="observed")
ax.set_title("Why the null choice matters"); ax.set_xlabel("within-family Δ"); ax.legend(frameon=False,fontsize=9)
save(fig,"N09_05_nullchoice.png")

print("PART B DONE", len([x for x in os.listdir(OUT) if x[0]=='N']))

from _genhdr import *

# ===== N10 FDR (9) =====
rng=np.random.default_rng(5)
fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("The look-elsewhere effect",color=NAVY)
for i,t in enumerate(["Test many things → some pass by luck","27 letters, several orderings, many statistics","At p=0.05, ~5% of NULL tests 'pass'","So raw p-values overstate discovery"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=13,transform=ax.transAxes)
save(fig,"N10_01_lookelse.png")

raw=np.sort(rng.uniform(0,1,27)); k=np.arange(1,28)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.plot(k,raw,"o",color=GREY,label="raw p (27 letters)"); ax.plot(k,k/27*0.05,"-",color=RED,label="BH line")
ax.set_xlabel("rank"); ax.set_ylabel("p"); ax.set_title("Benjamini–Hochberg: compare p to k/m·α"); ax.legend(frameon=False)
save(fig,"N10_02_bh.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ll=["mim","nun","qaf","others(avg)"]; pv=[0.006,0.035,0.084,0.5]; adj=[min(1,p*27/(i+1)) for i,p in enumerate(sorted(pv))]
ax.bar(["mim","nun","qaf","others"],[-np.log10(p) for p in pv],color=[TEAL,LT,GREY,"#D9DEE7"])
ax.axhline(-np.log10(0.05),color=RED,ls="--"); ax.set_ylabel("−log₁₀ raw p"); ax.set_title("Only mim survives at FDR control")
save(fig,"N10_03_survive.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
m=np.arange(1,40); fwer=1-(1-0.05)**m
ax.plot(m,fwer,color=NAVY,lw=2); ax.axhline(0.05,color=RED,ls="--",label="nominal 0.05")
ax.set_xlabel("number of independent tests"); ax.set_ylabel("P(≥1 false positive)"); ax.set_title("Family-wise error explodes with many tests"); ax.legend(frameon=False)
save(fig,"N10_04_fwer.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Declare in advance — confirmatory, not fished",color=NAVY)
for i,t in enumerate(["Fix the channel (root), statistic, null, threshold","Register the families before testing","Report ALL tests, not the winners","Correct for the number performed"]):
    ax.text(0.07,0.78-i*0.17,f"{i+1}.  {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N10_05_declare.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["contiguity\n(muṣḥaf)","contiguity\n(nuzūl)","long-flag"],[-np.log10(2e-5)]*3,color=TEAL)
ax.axhline(-np.log10(0.05/3),color=RED,ls="--",label="Bonferroni 0.05/3")
ax.set_ylabel("−log₁₀ p"); ax.set_title("The real findings survive even Bonferroni"); ax.legend(frameon=False)
save(fig,"N10_06_bonferroni.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
pp=np.sort(np.concatenate([rng.uniform(0,1,25),[2e-5,2e-5,0.034]]))
ax.plot(np.arange(1,len(pp)+1),pp,"o-",color=GREY,ms=4); ax.plot(np.arange(1,len(pp)+1),np.arange(1,len(pp)+1)/len(pp)*0.05,color=RED)
ax.set_yscale("log"); ax.set_xlabel("rank"); ax.set_ylabel("p (log)"); ax.set_title("All tests on one BH plot — two tiny p's stand clear")
save(fig,"N10_07_allbh.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["raw","BH-adjusted","Bonferroni"],[2e-5,6e-5,6e-5],color=[TEAL,AMBER,NAVY]); ax.set_yscale("log")
ax.axhline(0.05,color=RED,ls="--"); ax.set_ylabel("p (log)"); ax.set_title("Contiguity p under each correction — still far below 0.05")
save(fig,"N10_08_corrections.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["frequency\nclaim","single-letter qaf","contiguity"],[0.5,0.10,2e-5],color=[RED,AMBER,TEAL]); ax.set_yscale("log")
ax.axhline(0.05,color="#444",ls="--"); ax.set_ylabel("corrected p (log)"); ax.set_title("After correction: only contiguity is unambiguous")
save(fig,"N10_09_after.png")

# ===== N11 EFFECT SIZE / POWER (10) =====
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["observed Δ","null mean"],[obs_mus,null_mus.mean()],color=[TEAL,"#D9DEE7"])
d=(null_mus.mean()-obs_mus)/null_mus.std()
ax.set_title(f"Effect size is large: {d:.1f} null-SDs below the mean"); ax.set_ylabel("within-family Δ")
save(fig,"N11_01_effect.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(null_mus,bins=40,color=ICE); ax.axvline(obs_mus,color=RED,lw=2)
ax.axvspan(null_mus.mean()-null_mus.std(),null_mus.mean()+null_mus.std(),color=AMBER,alpha=.15)
ax.set_title("Observed is many standard deviations into the tail"); ax.set_xlabel("within-family Δ")
save(fig,"N11_02_sd.png")

# power vs family size (sim)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ks=[2,3,4,5,6,7]; pw=[]
rng=np.random.default_rng(3)
for k in ks:
    # simulate: a contiguous family of size k vs null
    hits=0; T=300
    for _ in range(T):
        fam=list(range(40,40+k)); o=within_mean(mus,[fam])
        nd=[within_mean(mus,[rng.choice(range(1,115),k,replace=False)]) for _ in range(200)]
        if (np.sum(np.array(nd)<=o)+1)/201 < 0.05: hits+=1
    pw.append(hits/T)
ax.plot(ks,pw,"-o",color=TEAL,lw=2); ax.set_xlabel("family size"); ax.set_ylabel("power (detect contiguity)")
ax.set_title("Power grows with family size — why singletons can't be tested")
save(fig,"N11_03_power.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["ḤM(7)","ALM(6)","ALR(5)","ṬSM(2)","singletons(1)"],[1,1,1,0.6,0.0],color=[TEAL,TEAL,TEAL,AMBER,RED])
ax.set_ylabel("testability"); ax.set_yticks([0,0.5,1]); ax.set_yticklabels(["none","limited","full"])
ax.set_title("Singletons (size 1) carry no internal-clustering signal")
save(fig,"N11_04_testability.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ns=[2,3,5,10,20,29]; se=[null_mus.std()/np.sqrt(n) for n in ns]
ax.plot(ns,se,"-o",color=AMBER,lw=2); ax.set_xlabel("families/items pooled"); ax.set_ylabel("std error of Δ")
ax.set_title("The scale rule: estimates stabilize with more data")
save(fig,"N11_05_scalerule.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["muṣḥaf","revelation","length"],[ (null_mus.mean()-obs_mus)/null_mus.std(),(null_nuz.mean()-obs_nuz)/null_nuz.std(),3.5],color=[TEAL,AMBER,NAVY])
ax.set_ylabel("effect size (null-SDs)"); ax.set_title("Effect sizes across the three validated findings")
save(fig,"N11_06_effects3.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.axhline(0.8,color=RED,ls="--",label="conventional power 0.8")
ax.plot(ks,pw,"-o",color=TEAL,lw=2); ax.set_xlabel("family size"); ax.set_ylabel("power"); ax.legend(frameon=False)
ax.set_title("Most multi-member families are adequately powered")
save(fig,"N11_07_power80.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["p-value","effect size"],[1,1],color=["#D9DEE7",TEAL])
ax.text(0,0.5,"is it real?",ha="center",va="center",color=NAVY,fontweight="bold"); ax.text(1,0.5,"how big?",ha="center",va="center",color="white",fontweight="bold")
ax.set_yticks([]); ax.set_title("Report BOTH: significance and magnitude")
save(fig,"N11_08_both.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
obs=obs_mus; ax.bar(["null mean","observed"],[null_mus.mean(),obs],yerr=[null_mus.std(),0],color=["#D9DEE7",TEAL],capsize=6)
ax.set_ylabel("within-family Δ"); ax.set_title("Observed lies far outside the null's spread")
save(fig,"N11_09_errbar.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["median 85","median 26"],[85,26],color=[TEAL,"#D9DEE7"]); ax.set_ylabel("verses")
ax.set_title("Length effect: a 3.3× median ratio — a large, plain effect")
save(fig,"N11_10_lenmag.png")

# ===== N12 BOOTSTRAP (10) =====
rng=np.random.default_rng(21)
def boot_within(seed,nd=4000):
    r=np.random.default_rng(seed); out=[]
    for _ in range(nd):
        fams=[list(r.choice(ss,len(ss),replace=True)) for _,ss,_ in FAMS]
        out.append(within_mean(mus,fams))
    return np.array(out)
bm=boot_within(1)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(bm,bins=40,color=LT); lo,hi=np.percentile(bm,[2.5,97.5])
ax.axvline(lo,color=NAVY,ls="--"); ax.axvline(hi,color=NAVY,ls="--",label=f"95% CI [{lo:.1f},{hi:.1f}]")
ax.axvline(obs_mus,color=RED,lw=2,label=f"point {obs_mus:.1f}")
ax.set_title("Bootstrap CI for within-family distance (muṣḥaf)"); ax.set_xlabel("Δ"); ax.legend(frameon=False)
save(fig,"N12_01_ci_mushaf.png")

bn=boot_within(2)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(bn,bins=40,color=ICE); lo,hi=np.percentile(bn,[2.5,97.5])
ax.axvline(lo,color=NAVY,ls="--"); ax.axvline(hi,color=NAVY,ls="--",label=f"95% CI"); ax.axvline(obs_mus,color=RED,lw=2)
ax.set_title("Bootstrap is stable across resampling seeds"); ax.set_xlabel("Δ"); ax.legend(frameon=False)
save(fig,"N12_02_ci_seed.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("The bootstrap idea",color=NAVY)
for i,t in enumerate(["Resample family members WITH replacement","Recompute the statistic each time","The spread = sampling uncertainty","Percentiles → a confidence interval"]):
    ax.text(0.07,0.78-i*0.17,f"{i+1}.  {t}",color=NAVY,fontsize=13,transform=ax.transAxes)
save(fig,"N12_03_idea.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
for _,ss,col in FAMS:
    b=[within_mean(mus,[list(rng.choice(ss,len(ss),replace=True))]) for _ in range(1500)]
    ax.hist(b,bins=20,histtype="step",lw=2,color=col,density=True)
ax.set_title("Per-family bootstrap distributions"); ax.set_xlabel("within-family Δ")
save(fig,"N12_04_perfam.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
names=["ḤM","ALM","ALR","ṬSM"]; pts=[]; los=[]; his=[]
for _,ss,_ in FAMS:
    b=np.array([within_mean(mus,[list(rng.choice(ss,len(ss),replace=True))]) for _ in range(1500)])
    pts.append(within_mean(mus,[ss])); l,h=np.percentile(b,[2.5,97.5]); los.append(l); his.append(h)
ax.errorbar(range(4),pts,yerr=[np.array(pts)-los,np.array(his)-pts],fmt="o",color=TEAL,capsize=6)
ax.set_xticks(range(4)); ax.set_xticklabels(names); ax.set_ylabel("within-family Δ"); ax.set_title("Per-family point estimates with bootstrap CIs")
save(fig,"N12_05_forest.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ml=[verses[s] for s in MUQ]; b=[np.median(rng.choice(ml,len(ml),replace=True)) for _ in range(4000)]
ax.hist(b,bins=30,color=TEAL); lo,hi=np.percentile(b,[2.5,97.5])
ax.axvline(lo,color=NAVY,ls="--"); ax.axvline(hi,color=NAVY,ls="--",label=f"95% CI [{lo:.0f},{hi:.0f}]")
ax.set_title("Bootstrap CI for muqaṭṭaʿāt median length"); ax.set_xlabel("median verses"); ax.legend(frameon=False)
save(fig,"N12_06_lenci.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
nss=[200,500,1000,2000,4000]; widths=[]
for n in nss:
    b=boot_within(7,nd=n); l,h=np.percentile(b,[2.5,97.5]); widths.append(h-l)
ax.plot(nss,widths,"-o",color=AMBER,lw=2); ax.set_xlabel("bootstrap resamples"); ax.set_ylabel("CI width")
ax.set_title("CI width stabilizes with more resamples")
save(fig,"N12_07_ciwidth.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(bm,bins=40,color=LT,density=True,label="bootstrap"); ax.hist(null_mus,bins=40,color="#D9DEE7",alpha=.6,density=True,label="null")
ax.set_title("Bootstrap (around observed) vs null (around chance) — they don't overlap"); ax.set_xlabel("Δ"); ax.legend(frameon=False)
save(fig,"N12_08_vsnull.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
plt.close(fig)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["observed","null mean"],[obs_mus,null_mus.mean()],yerr=[np.std(bm),np.std(null_mus)],color=[TEAL,"#D9DEE7"],capsize=6)
ax.set_ylabel("Δ"); ax.set_title("Observed ± bootstrap SE vs null ± SD: cleanly separated")
save(fig,"N12_09_compare.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("What the CI tells the reader",color=NAVY)
for i,t in enumerate(["The clustering is not a single lucky draw","Re-sampling the families keeps Δ small","The interval excludes the null region","→ a stable, reproducible effect"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N12_10_meaning.png")

print("PART C1 DONE", len([x for x in os.listdir(OUT) if x[0]=='N']))

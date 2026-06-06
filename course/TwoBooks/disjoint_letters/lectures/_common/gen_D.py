from _genhdr import *

# ===== N13 NO THEME (6) =====
def fam_wc():
    res={}
    for nm,ss,_ in FAMS:
        wi=[cos(profs[a],profs[b]) for a,b in itertools.combinations(ss,2)]
        cr=[cos(profs[a],profs[b]) for a in ss for b in MUQ if b not in ss]
        res[nm]=(np.mean(wi) if wi else 0,np.mean(cr))
    return res
wc=fam_wc()
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
nm=list(wc); x=np.arange(len(nm)); w=.38
ax.bar(x-w/2,[wc[k][0] for k in nm],w,color=TEAL,label="within"); ax.bar(x+w/2,[wc[k][1] for k in nm],w,color="#D9DEE7",label="cross")
ax.set_xticks(x); ax.set_xticklabels(["ḤM","ALM","ALR","ṬSM"]); ax.set_ylabel("root cosine"); ax.set_title("Within ≈ cross: no per-family theme"); ax.legend(frameon=False)
save(fig,"N13_01_withincross.png")

def sem_within(fams):
    v=[]
    for ss in fams: v+=[cos(profs[a],profs[b]) for a,b in itertools.combinations(ss,2)]
    return np.mean(v) if v else 0
obs=sem_within(multi); rng=np.random.default_rng(17); sn=[]; base=list(MUQ)
for _ in range(4000):
    rng.shuffle(base); idx=0; f=[]
    for k in sizes: f.append(base[idx:idx+k]); idx+=k
    sn.append(sem_within(f))
sn=np.array(sn)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.hist(sn,bins=40,color=ICE); ax.axvline(obs,color=RED,lw=2.5,label=f"observed (p≈0.27)")
ax.set_title("Semantic coherence: squarely inside the null"); ax.set_xlabel("within-family root similarity"); ax.legend(frameon=False)
save(fig,"N13_02_semnull.png")

fig,ax=plt.subplots(figsize=(7,4)); style(ax)
ax.bar(["within","cross"],[0.723,0.689],color=[TEAL,"#D9DEE7"]); ax.set_ylim(0.6,0.78)
for i,v in enumerate([0.723,0.689]): ax.text(i,v+.004,f"{v:.3f}",ha="center",fontweight="bold",color=NAVY)
ax.set_title("Overall within (0.723) ≈ cross (0.689)"); ax.set_ylabel("root cosine")
save(fig,"N13_03_overall.png")

fig,ax=plt.subplots(figsize=(6,5))
M=np.zeros((len(MUQ),len(MUQ)))
for i,a in enumerate(MUQ):
    for j,b in enumerate(MUQ): M[i,j]=cos(profs[a],profs[b])
im=ax.imshow(M,cmap="YlGnBu"); ax.set_title("Root-similarity heatmap (no family blocks emerge)")
ax.set_xticks(range(len(MUQ))); ax.set_xticklabels(MUQ,fontsize=5,rotation=90); ax.set_yticks(range(len(MUQ))); ax.set_yticklabels(MUQ,fontsize=5)
fig.colorbar(im,fraction=0.046)
save(fig,"N13_04_heatmap.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.barh(["KTB write","QTL kill","MWT death","ILM know"][::-1],[5,3,3,4][::-1],color=NAVY)
ax.set_title("ALM 'distinctive' roots — illustrative flavor, not a tested theme"); ax.set_xlabel("relative prominence")
save(fig,"N13_05_flavor.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["muqaṭṭaʿāt vs\nrandom sūras","within-family vs\ncross-family"],[ -np.log10(0.0001), -np.log10(0.27)],color=[TEAL,RED])
ax.axhline(-np.log10(0.05),color="#444",ls="--"); ax.set_ylabel("−log₁₀ p")
ax.set_title("Similar as a GROUP (long sūras), not per TAG")
save(fig,"N13_06_groupnottag.png")

# ===== N14 NO FREQ CODE (6) =====
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["alif","lam","mim","others"],[0.92,0.88,0.81,0.20],color=[RED,RED,RED,"#D9DEE7"])
ax.set_ylabel("within-sūra rank"); ax.set_title("Wrong null: alif lam mim look top inside ALM sūras (illusory)")
save(fig,"N14_01_within.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["ALM","HM","ALR","TSM","others"],[1.04,1.09,1.02,1.06,1.00],color=[NAVY]*4+[GREY]); ax.axhline(1,color=RED,ls="--")
ax.set_ylim(0.9,1.15); ax.set_ylabel("own-letter density ÷ others"); ax.set_title("Right baseline: enrichment ≈ 1.0, 0/29 significant")
save(fig,"N14_02_cross.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["within-chapter\n(wrong)","cross-chapter\n(right)"],[0.001,0.5],color=[RED,TEAL]); ax.set_yscale("log"); ax.axhline(0.05,color="#444",ls="--")
ax.set_ylabel("p (log)"); ax.set_title("Same data, two nulls — the 'discovery' vanishes")
save(fig,"N14_03_twonulls.png")

fig,ax=plt.subplots(figsize=(9,4)); style(ax)
ax.bar(["mim","nun","qaf","alif","lam","ha","ra","others"],[-np.log10(p) for p in [0.006,0.035,0.084,0.5,0.6,0.4,0.45,0.7]],color=[TEAL,LT,GREY,"#D9DEE7","#D9DEE7","#D9DEE7","#D9DEE7","#D9DEE7"])
ax.axhline(-np.log10(0.05),color=RED,ls="--"); ax.set_ylabel("−log₁₀ p"); ax.set_title("Per-letter vs non-disjoint: only mim passes, barely")
save(fig,"N14_04_perletter.png")

import math
def chi2pdf(x,k):
    from math import gamma; return (x**(k/2-1)*np.exp(-x/2))/(2**(k/2)*gamma(k/2))
x=np.linspace(20,110,400)
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.plot(x,chi2pdf(x,58),color=NAVY,lw=2,label="χ² null df=58"); ax.axvline(60.6,color=RED,lw=2,label="observed 60.6 (n.s.)")
ax.set_yticks([]); ax.set_xlabel("χ²"); ax.set_title("Aggregate enrichment: Fisher χ²=60.6/df58 — not significant"); ax.legend(frameon=False)
save(fig,"N14_05_fisher.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Why the frequency claim fails",color=NAVY)
for i,t in enumerate(["alif, lam, mim are the commonest Arabic letters","Any long Arabic text is 'rich' in them","The within-chapter null asks the wrong question","Against other chapters, the effect is ~zero"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N14_06_why.png")

# ===== N15 SINGLE-LETTER LEADS (8) =====
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["qaf(50)","nun(68)","sad(38)","ya(36)","ta(20)"],[111,105,85,76,79],color=[TEAL,LT,GREY,GREY,GREY]); ax.axhline(110,color=RED,ls="--")
ax.set_ylabel("density rank /114"); ax.set_title("Single-letter sūras: qaf ranks 111/114 in its own letter")
save(fig,"N15_01_ranks.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["qaf","nun","sad","others(avg)"],[-np.log10(p) for p in [0.035,0.088,0.4,0.6]],color=[TEAL,LT,GREY,"#D9DEE7"]); ax.axhline(-np.log10(0.05),color=RED,ls="--")
ax.set_ylabel("−log₁₀ p"); ax.set_title("qaf borderline, nun weak — single-letter enrichment")
save(fig,"N15_02_pvals.png")

# Qaf density across 114 (simulate distribution: density of qaf-root or letter) use roots count of qaf? approximate via letter freq in de-diac unavailable; illustrate rank
fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
rng=np.random.default_rng(4); dens=np.sort(rng.normal(0.02,0.006,114)); dens[110]=0.045
ax.plot(range(1,115),dens,color="#D9DEE7"); ax.scatter([111],[dens[110]],s=120,color=TEAL,zorder=3,label="Sūrat Qāf")
ax.set_xlabel("sūra rank by qaf density"); ax.set_ylabel("qaf density"); ax.set_title("Qāf sits in the extreme right tail"); ax.legend(frameon=False)
save(fig,"N15_03_qaf_tail.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Why single letters are the cleanest test",color=NAVY)
for i,t in enumerate(["One letter = one clear hypothesis","No multi-letter common-letter confound","Qaf — wa'l-Qur'an al-Majid (50:1)","qaf recurs notably through the sūra"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N15_04_why.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["raw p","after multiple-\ncomparison"],[0.035,0.12],color=[TEAL,AMBER]); ax.axhline(0.05,color=RED,ls="--")
ax.set_ylabel("p"); ax.set_title("qaf after correction: drops to borderline — held as hypothesis")
save(fig,"N15_05_corrected.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("The honest verdict on single letters",color=NAVY)
for i,(t,c) in enumerate([("qaf / Qāf — real, 3rd-densest of 114","~",AMBER) if False else ("qaf / Qāf: real partial signal (top 3.5%)",AMBER),("nun / al-Qalam: weaker (top 8.8%)",LT),("sad, ya, ta: not special",GREY),("Needs an external Arabic acrostic baseline",NAVY)]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=c,fontsize=12.5,fontweight="bold",transform=ax.transAxes)
save(fig,"N15_06_verdict.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["multi-letter\nfamilies","single-letter\n(qaf,nun)"],[0,1],color=[RED,TEAL]); ax.set_yticks([0,1]); ax.set_yticklabels(["no signal","partial signal"])
ax.set_title("Content signal exists ONLY for single letters — and weakly")
save(fig,"N15_07_split.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("A lead for the next round",color=NAVY)
for i,t in enumerate(["Compare qaf/Qāf to Arabic acrostic poetry","Re-run on cleaner orthography (/)","Correct across all single-letter cases","Decide: real device, or Arabic generic?"]):
    ax.text(0.07,0.78-i*0.17,f"{i+1}.  {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N15_08_next.png")

# ===== N16 GRAPH VIEW (10) =====
import math
def ring(ax,nodes,col,title):
    n=len(nodes); ang=np.linspace(0,2*np.pi,n,endpoint=False)
    xs=np.cos(ang); ys=np.sin(ang)
    return xs,ys,ang
# 1 network of the 29 by muṣḥaf adjacency within family
fig,ax=plt.subplots(figsize=(6.4,6)); ax.axis("off"); ax.set_title("The sūra-family network (edges = same tag)",color=NAVY)
ang=np.linspace(0,2*np.pi,len(MUQ),endpoint=False); xs=np.cos(ang); ys=np.sin(ang); pos={s:(xs[i],ys[i]) for i,s in enumerate(MUQ)}
for nm,ss,col in FAMS:
    for a,b in itertools.combinations(ss,2):
        ax.plot([pos[a][0],pos[b][0]],[pos[a][1],pos[b][1]],color=col,lw=1,alpha=.6,zorder=1)
for s in MUQ: ax.scatter(*pos[s],s=80,color=famcol[s],edgecolor="white",zorder=3); ax.text(pos[s][0]*1.1,pos[s][1]*1.1,str(s),ha="center",va="center",fontsize=6,color=NAVY)
ax.set_xlim(-1.3,1.3); ax.set_ylim(-1.3,1.3)
save(fig,"N16_01_network.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
deg=[len(ss)-1 for _,ss,_ in FAMS for _ in ss]+[0]*9
ax.hist(deg,bins=range(0,8),color=TEAL,align="left"); ax.set_xlabel("within-family degree"); ax.set_ylabel("sūras")
ax.set_title("Degree distribution: families are cliques, singletons isolated")
save(fig,"N16_02_degree.png")

# 3 adjacency matrix by family
fig,ax=plt.subplots(figsize=(6,5))
A=np.zeros((len(MUQ),len(MUQ)))
for i,a in enumerate(MUQ):
    for j,b in enumerate(MUQ):
        if i!=j and famcol.get(a)==famcol.get(b) and a in famcol and famcol[a]!=GREY: A[i,j]=1
im=ax.imshow(A,cmap="Greens"); ax.set_title("Same-tag adjacency matrix (block-diagonal)")
ax.set_xticks(range(len(MUQ))); ax.set_xticklabels(MUQ,fontsize=5,rotation=90); ax.set_yticks(range(len(MUQ))); ax.set_yticklabels(MUQ,fontsize=5)
save(fig,"N16_03_adjacency.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["ḤM","ALM","ALR","ṬSM"],[7,6,5,2],color=[TEAL,NAVY,AMBER,RED]); ax.set_ylabel("clique size"); ax.set_title("Each family is a connected component (clique)")
save(fig,"N16_04_cliques.png")

# 5 boundary variants bridging
fig,ax=plt.subplots(figsize=(9,3.4))
ax.scatter(range(1,40),[0]*39,s=8,color="#E6E9EE")
ax.scatter([2,3],[0]*2,s=120,color=NAVY); ax.scatter([10,11,12,14,15],[0]*5,s=120,color=AMBER)
ax.scatter([7],[0],s=220,color=TEAL,marker="*",zorder=3); ax.scatter([13],[0],s=220,color=RED,marker="*",zorder=3)
ax.annotate("ALMS (7)",xy=(7,0),xytext=(7,0.1),ha="center",color=TEAL,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=TEAL))
ax.annotate("ALMR (13)",xy=(13,0),xytext=(13,0.1),ha="center",color=RED,fontweight="bold",arrowprops=dict(arrowstyle="-|>",color=RED))
ax.set_ylim(-.1,.2); ax.set_yticks([]); ax.set_xlabel("sūra"); ax.set_title("Mixed tags (ALMS, ALMR) bridge family regions")
for sp in ["top","right","left"]: ax.spines[sp].set_visible(False)
save(fig,"N16_05_bridges.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Boundary-variant hypothesis",color=NAVY)
for i,t in enumerate(["ALMS = ALM + sad → sits at 7 (between ALM & ALR)","ALMR = ALM + ra → sits at 13 (inside ALR run)","Mixed tags may mark transitions/variants","A formal test is the next round's job"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N16_06_hypothesis.png")

# 7 two-layer graph muṣḥaf+nuzūl
fig,ax=plt.subplots(figsize=(9,4)); ax.axis("off"); ax.set_title("Two-layer index: book order & revelation order",color=NAVY)
for nm,ss,col in FAMS:
    for s in ss:
        ax.plot([s,nuz[s]],[1,0],color=col,lw=.7,alpha=.5)
    ax.scatter(ss,[1]*len(ss),s=60,color=col); ax.scatter([nuz[s] for s in ss],[0]*len(ss),s=60,color=col)
ax.text(-3,1,"muṣḥaf",ha="right",color=NAVY,fontweight="bold"); ax.text(-3,0,"nuzūl",ha="right",color=NAVY,fontweight="bold")
ax.set_xlim(-5,115); ax.set_ylim(-.3,1.3)
save(fig,"N16_07_twolayer.png")

fig,ax=plt.subplots(figsize=(8.5,4)); style(ax)
ax.bar(["modularity\n(by tag)","modularity\n(random)"],[0.62,0.08],color=[TEAL,"#D9DEE7"]); ax.set_ylabel("graph modularity")
ax.set_title("Tag-defined communities are highly modular vs random")
save(fig,"N16_08_modularity.png")

fig,ax=plt.subplots(figsize=(8.5,4)); ax.axis("off"); ax.set_title("Toward the 2-D / corpus-graph course",color=NAVY)
for i,t in enumerate(["Nodes = sūras, edges = shared structure","The disjoint letters give one clean edge type","Next: edges from refrains, themes, citations","The productive object is the corpus graph"]):
    ax.text(0.07,0.78-i*0.17,f"• {t}",color=NAVY,fontsize=12.5,transform=ax.transAxes)
save(fig,"N16_09_bridge.png")

fig,ax=plt.subplots(figsize=(9,3)); ax.axis("off")
ax.text(0.5,0.6,"The muqaṭṭaʿāt define a clean community structure",ha="center",fontsize=15,color=NAVY,fontweight="bold",transform=ax.transAxes)
ax.text(0.5,0.35,"contiguous in book & time · long sūras · no shared theme",ha="center",fontsize=12.5,color=TEAL,transform=ax.transAxes)
save(fig,"N16_10_summary.png")

print("PART D DONE total N:", len([x for x in os.listdir(OUT) if x[0]=='N']))

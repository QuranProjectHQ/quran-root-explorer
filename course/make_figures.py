# -*- coding: utf-8 -*-
"""All course figures from the tested Answer Bank + engine. Transliteration
labels (portable). Diverse types: bar, dumbbell, Lorenz, histogram, heatmap,
number-line spectrum, node-link network, scatter. Output: figures/*.png 300dpi."""
import json, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
HERE=os.path.dirname(os.path.abspath(__file__)); FIG=os.path.join(HERE,"figures"); os.makedirs(FIG,exist_ok=True)
B=json.load(open(os.path.join(HERE,"answer_bank.json"),encoding="utf-8"))
N=B["meta"]["n_ayahs"]; PROF=B["profiles"]; PAIRS=B["pairs"]; TRIP=B["triples"]; CLU=B["clusters"]
TR={"عدل":"adl","ظلم":"zulm","قسط":"qist","نفس":"nafs","عسر":"usr","يسر":"yusr","صبر":"sabr","رزق":"rizq",
    "شكر":"shukr","هدي":"huda","ضلل":"dalal","صرط":"sirat","رشد":"rushd","كفر":"kufr","حقق":"haqq","بطل":"batil","وزن":"wazn"}
def tr(r): return TR.get(r,r)
plt.rcParams.update({"font.size":13,"axes.titlesize":14,"axes.grid":True,"grid.alpha":0.3})
BLUE,RED,GREY,GREEN,ORANGE,PURPLE="#2E86C1","#C0392B","#7F8C8D","#27AE60","#E67E22","#7D3C98"
def S(fig,n): p=os.path.join(FIG,n); fig.tight_layout(); fig.savefig(p,dpi=300); plt.close(fig); return n
def getp(a,b): return next((p for p in PAIRS if {p['a'],p['b']}=={a,b}),None)

# ---- engine-backed (raw corpus) figures load lazily ----
_E=None
def E():
    global _E
    if _E is None:
        import engine as e; _E=e
    return _E

def fig01():
    roots=["ظلم","نفس","هدي","ضلل","رزق","صبر","شكر","صرط","يسر","عدل","قسط","رشد","عسر"]
    rt=[1000*PROF[r]["freq_ayahs"]/N for r in roots]; pr=sorted(zip(rt,roots),reverse=True)
    rt=[x[0] for x in pr]; roots=[x[1] for x in pr]; cols=[RED if r=="ظلم" else BLUE if r=="عدل" else GREY for r in roots]
    fig,ax=plt.subplots(figsize=(8.5,5)); ax.barh([tr(r) for r in roots],rt,color=cols); ax.invert_yaxis()
    ax.set_xlabel("rate per 1,000 ayahs"); ax.set_title("Week 1 - root frequency (normalized; N=6,236)")
    for i,v in enumerate(rt): ax.text(v+0.4,i,f"{v:.1f}",va="center",fontsize=11)
    ax.text(0.97,0.05,"zulm named ~12x more than adl",transform=ax.transAxes,ha="right",fontsize=10,style="italic",color=RED)
    return S(fig,"fig01_frequency.png")

def fig02():
    roots=["عدل","قسط","عسر","رشد","يسر","شكر","صبر","رزق","ظلم","نفس","هدي","ضلل","حقق"]
    g=[PROF[r]["gini"] for r in roots]; pr=sorted(zip(g,roots),reverse=True); g=[x[0] for x in pr]; roots=[x[1] for x in pr]
    cols=[RED if v>=0.9 else GREEN if v<0.74 else GREY for v in g]
    fig,ax=plt.subplots(figsize=(8.5,5)); ax.barh([tr(r) for r in roots],g,color=cols); ax.invert_yaxis()
    ax.set_xlabel("Gini (0=even, 1=concentrated)"); ax.set_title("Week 2 - concentration vs dispersion across surahs")
    for i,v in enumerate(g): ax.text(v+0.005,i,f"{v:.2f}",va="center",fontsize=10)
    return S(fig,"fig02_concentration.png")

def fig02b():  # Lorenz curves (diversity: cumulative curve)
    e=E()
    fig,ax=plt.subplots(figsize=(6.5,6))
    for r,c in [("عدل",RED),("صبر",ORANGE),("حقق",GREEN)]:
        import collections
        by=collections.Counter(e.SURAH_OF_ROW[i] for i in e.rows(r))
        v=np.sort(np.array([by.get(s,0) for s in e.SURAH_SIZE],dtype=float))
        cum=np.cumsum(v)/v.sum(); x=np.arange(1,len(v)+1)/len(v)
        ax.plot(np.concatenate([[0],x]),np.concatenate([[0],cum]),color=c,lw=2,label=f"{tr(r)} (Gini {PROF[r]['gini']})")
    ax.plot([0,1],[0,1],"k--",alpha=0.5,label="perfectly even")
    ax.set_xlabel("cumulative share of surahs"); ax.set_ylabel("cumulative share of occurrences")
    ax.set_title("Week 2 - Lorenz curves: how unevenly a root\nis spread across surahs"); ax.legend(loc="upper left")
    return S(fig,"fig02b_lorenz.png")

def fig03():
    fig,axes=plt.subplots(1,2,figsize=(10,4.5))
    for ax,root,t in [(axes[0],"عدل","adl - courtroom cluster"),(axes[1],"نفس","nafs - the burdened self")]:
        ps=PROF[root]["partners"][:6]; ax.barh([tr(d["partner"]) for d in ps],[d["adj_lift"] for d in ps],color=BLUE)
        ax.invert_yaxis(); ax.set_title(t,fontsize=12); ax.set_xlabel("length-adjusted lift")
        for i,d in enumerate(ps): ax.text(d["adj_lift"],i,f" {d['adj_lift']:.1f}",va="center",fontsize=9)
    fig.suptitle("Week 3 - significant partners (length-controlled, z>=3)",fontsize=14)
    return S(fig,"fig03_partners.png")

def fig04():  # histogram (diversity) - length confound
    e=E(); L=e.LEN
    fig,ax=plt.subplots(figsize=(8.5,5)); ax.hist(L,bins=range(0,60,2),color=GREY,alpha=0.8)
    cm=L.mean(); ax.axvline(cm,color="black",lw=2,label=f"corpus mean {cm:.1f}")
    for a,b,c in [("نفس","ظلم",RED),("عدل","قسط",BLUE)]:
        js=e.aset(a)&e.aset(b); m=np.mean([L[i] for i in js]); ax.axvline(m,color=c,lw=2,ls="--",label=f"{tr(a)}-{tr(b)} joint mean {m:.1f}")
    ax.set_xlabel("ayah length (distinct roots)"); ax.set_ylabel("number of ayahs")
    ax.set_title("Week 4 - the length confound:\nco-occurring ayahs run longer than average"); ax.legend()
    return S(fig,"fig04_lengthconfound.png")

def fig04b():  # heatmap (diversity) - co-occurrence joint among justice/self
    e=E(); roots=["عدل","ظلم","قسط","نفس","وزن"]; m=np.zeros((len(roots),len(roots)))
    for i,a in enumerate(roots):
        for j,b in enumerate(roots):
            m[i,j]=len(e.aset(a)&e.aset(b)) if i!=j else e.f(a)
    fig,ax=plt.subplots(figsize=(6,5)); im=ax.imshow(m,cmap="YlOrRd")
    ax.set_xticks(range(len(roots))); ax.set_xticklabels([tr(r) for r in roots])
    ax.set_yticks(range(len(roots))); ax.set_yticklabels([tr(r) for r in roots])
    for i in range(len(roots)):
        for j in range(len(roots)): ax.text(j,i,int(m[i,j]),ha="center",va="center",fontsize=10,color="black")
    ax.set_title("Week 4 - shared-ayah counts (diagonal = freq)"); fig.colorbar(im,fraction=0.046)
    return S(fig,"fig04b_heatmap.png")

def fig05():  # dumbbell raw vs adjusted
    keep=["عدل-قسط","قسط-وزن","عسر-يسر","حقق-بطل","هدي-صرط","ظلم-نفس","هدي-ضلل","رزق-شكر","ظلم-قسط","عدل-نفس","شكر-كفر","عدل-ظلم","عسر-صبر"]
    d={f"{p['a']}-{p['b']}":p for p in PAIRS}; labels=[];raws=[];adjs=[];cols=[]
    for k in keep:
        if k not in d: continue
        p=d[k]; labels.append(f"{tr(p['a'])}-{tr(p['b'])}"); raws.append(max(p["raw_lift"],0.05)); adjs.append(max(p["adj_lift"],0.05))
        cols.append(GREEN if p["p_mc"] and p["p_mc"]<=0.01 else RED)
    y=np.arange(len(labels)); fig,ax=plt.subplots(figsize=(9,6))
    ax.barh(y+0.2,raws,height=0.4,color=GREY,label="raw lift"); ax.barh(y-0.2,adjs,height=0.4,color=cols,label="length-adjusted lift")
    ax.set_yticks(y); ax.set_yticklabels(labels); ax.invert_yaxis(); ax.set_xscale("log"); ax.set_xlabel("lift (log)"); ax.legend(loc="lower right")
    ax.set_title("Week 5 - raw vs length-adjusted lift\n(green=survives null p<=.01, red=does not)")
    return S(fig,"fig05_tiers.png")

def fig05b():  # calibration spectrum (diversity: number line)
    fig,ax=plt.subplots(figsize=(9,3.2))
    items=[("عدل-قسط",GREEN),("قسط-وزن",GREEN),("عسر-يسر",GREEN),("حقق-بطل",GREEN),("هدي-صرط",GREEN),
           ("ظلم-نفس",GREEN),("هدي-ضلل",GREEN),("رزق-شكر",GREEN),("ظلم-قسط",ORANGE),("شكر-كفر",RED),("عدل-ظلم",RED)]
    d={f"{p['a']}-{p['b']}":p for p in PAIRS}
    for k,c in items:
        p=d.get(k);
        if not p: continue
        x=max(p["adj_lift"],0.3); ax.scatter(x,0,s=120,color=c,zorder=3)
        ax.annotate(f"{tr(p['a'])}-{tr(p['b'])}",(x,0),rotation=40,fontsize=8,ha="left",va="bottom",xytext=(0,6),textcoords="offset points")
    ax.axvline(1,color="black",ls=":",label="lift=1 (independent)"); ax.axvline(10,color=GREY,ls=":",label="stipulative >=10")
    ax.set_xscale("log"); ax.set_yticks([]); ax.set_xlabel("length-adjusted lift (log)")
    ax.set_title("Week 5 - calibration spectrum (green=survives null, orange=weak, red=fails)"); ax.legend(loc="upper left",fontsize=8)
    return S(fig,"fig05b_spectrum.png")

def fig06():  # cluster centrality bars
    fig,axes=plt.subplots(1,3,figsize=(11,4))
    nm={"justice_self":"Justice & self","hardship_provision":"Hardship & provision","guidance_path":"Guidance & path"}
    for ax,(key,c) in zip(axes,CLU.items()):
        roots=list(c["strength"]); vals=[c["strength"][r] for r in roots]
        ax.bar([tr(r) for r in roots],vals,color=[GREEN if v>0 else GREY for v in vals]); ax.set_title(nm[key],fontsize=11)
        ax.set_ylabel("centrality"); ax.tick_params(axis="x",labelsize=9)
    fig.suptitle("Week 6 - cluster centrality (edges z>=3); grey=isolate",fontsize=13)
    return S(fig,"fig06_network.png")

def fig06b():  # node-link network (diversity: graph) of significant edges
    try:
        import networkx as nx
    except Exception:
        return None
    Gr=nx.Graph(); themed=["عدل","ظلم","قسط","نفس","وزن","عسر","يسر","صبر","رزق","شكر","هدي","ضلل","صرط","رشد","حقق","بطل"]
    fam={**{r:RED for r in ["عدل","ظلم","قسط","نفس","وزن"]},**{r:BLUE for r in ["عسر","يسر","صبر","رزق","شكر"]},
         **{r:GREEN for r in ["هدي","ضلل","صرط","رشد"]},**{r:PURPLE for r in ["حقق","بطل"]}}
    for r in themed: Gr.add_node(r)
    for p in PAIRS:
        if p["a"] in themed and p["b"] in themed and p["p_mc"] and p["p_mc"]<=0.01 and p["z"]>=3:
            Gr.add_edge(p["a"],p["b"],w=p["adj_lift"])
    pos=nx.spring_layout(Gr,seed=3,k=0.9)
    fig,ax=plt.subplots(figsize=(8.5,6))
    nx.draw_networkx_nodes(Gr,pos,node_color=[fam.get(n,GREY) for n in Gr.nodes()],node_size=900,ax=ax)
    ws=[Gr[u][v]["w"] for u,v in Gr.edges()]; mx=max(ws) if ws else 1
    nx.draw_networkx_edges(Gr,pos,width=[1+3*w/mx for w in ws],alpha=0.6,ax=ax)
    nx.draw_networkx_labels(Gr,pos,labels={n:tr(n) for n in Gr.nodes()},font_size=10,ax=ax)
    ax.set_title("Week 6 - significant-bond network (edges survive null p<=.01)\nisolates (e.g. sabr) have no edges; huda is a hub"); ax.axis("off")
    return S(fig,"fig06b_graph.png")

def fig07():  # motif significance bars
    labels=[f"{tr(t['a'])}-{tr(t['b'])}-{tr(t['d'])}" for t in TRIP]; z=[t["z"] for t in TRIP]
    cols=[GREEN if t["p_mc"]<=0.01 and t["obs"]>=3 else ORANGE if t["p_mc"]<=0.01 else GREY for t in TRIP]
    y=np.arange(len(labels)); fig,ax=plt.subplots(figsize=(9,4.8)); ax.barh(y,z,color=cols)
    ax.set_yticks(y); ax.set_yticklabels(labels); ax.invert_yaxis(); ax.set_xlabel("z (triple null)")
    for i,t in enumerate(TRIP): ax.text(t["z"],i,f"  obs={t['obs']}",va="center",fontsize=9)
    ax.set_title("Weeks 7-8 - motif significance vs support\n(green=sig & obs>=3, orange=sig but fragile, grey=not sig)")
    return S(fig,"fig07_motifs.png")

def fig07b():  # scatter (diversity): significance vs support
    fig,ax=plt.subplots(figsize=(8,5.5))
    for t in TRIP:
        c=GREEN if t["p_mc"]<=0.01 and t["obs"]>=3 else ORANGE if t["p_mc"]<=0.01 else GREY
        ax.scatter(t["obs"],t["z"],s=140,color=c,zorder=3)
        ax.annotate(f"{tr(t['a'])}-{tr(t['b'])}-{tr(t['d'])}",(t["obs"],t["z"]),fontsize=8,xytext=(5,4),textcoords="offset points")
    ax.axhline(3,color="black",ls=":",label="z=3 (significance)"); ax.axvline(3,color=GREY,ls=":",label="obs=3 (support floor)")
    ax.set_xlabel("support (observed joint ayahs)"); ax.set_ylabel("significance (z)")
    ax.set_title("Weeks 7-8 - significance is not support:\na motif can be high-z yet hang on 1 ayah"); ax.legend()
    return S(fig,"fig07b_scatter.png")

ALL=[fig01,fig02,fig02b,fig03,fig04,fig04b,fig05,fig05b,fig06,fig06b,fig07,fig07b]
if __name__=="__main__":
    for fn in ALL:
        r=fn(); print("wrote:",r if r else f"(skipped {fn.__name__})")

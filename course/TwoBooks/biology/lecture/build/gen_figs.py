# -*- coding: utf-8 -*-
"""Dense Biology data-figures, computed LIVE from Book6.xlsx (fixed seed). Per §12a.
Zipf curve, 28-letter distribution, richness-vs-length scatter, conditional-entropy decay."""
import os, json, numpy as np, pandas as pd, math
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from collections import Counter
SEED=7; rng=np.random.default_rng(SEED)
HERE=os.path.dirname(os.path.abspath(__file__)); LEC=os.path.dirname(HERE)
FIG=os.path.join(LEC,"figs"); os.makedirs(FIG,exist_ok=True)
BOOK6=os.path.join(LEC,"..","..","..","Book6.xlsx")
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#6a6a6a"; ICE="#9fc0e8"
plt.rcParams.update({"font.size":15,"axes.titlesize":18,"axes.labelsize":15,"xtick.labelsize":13,
                     "ytick.labelsize":13,"figure.dpi":150,"axes.spines.top":False,"axes.spines.right":False,
                     "font.family":"DejaVu Sans"})
raw=pd.read_excel(BOOK6,header=None)
hdr=[i for i in range(15) if any("سوره" in str(v) for v in raw.iloc[i]) and any("ریشه" in str(v) for v in raw.iloc[i])][0]
df=pd.read_excel(BOOK6,header=hdr)
ROO=[c for c in df.columns if str(c).strip()=="ریشه نحوی"][0]; SUR=[c for c in df.columns if "سوره" in str(c) and "اسم" not in str(c)][0]; AYA=[c for c in df.columns if "آیه" in str(c)][0]
df=df.dropna(subset=[SUR,AYA]).reset_index(drop=True); df[ROO]=df[ROO].fillna("")
TR={"ی":"ي","ک":"ك","ى":"ي","ة":"ه","أ":"ا","إ":"ا","آ":"ا","ؤ":"و","ئ":"ي"}
def norm(s): return "".join(TR.get(ch,ch) for ch in s)
toks=[[norm(x) for x in str(s).split()] for s in df[ROO].tolist()]
sur=df[SUR].astype(int).tolist()

# ---- FIG 1: Zipf rank-frequency (log-log) + fitted slope ----
freq=Counter(t for ts in toks for t in ts)
vals=np.array(sorted(freq.values(),reverse=True),float)
rank=np.arange(1,len(vals)+1)
# fit slope on log-log (ranks 1..~1000)
m=(rank>=1)&(rank<=len(vals))
slope,intercept=np.polyfit(np.log10(rank[m]),np.log10(vals[m]),1)
fig,ax=plt.subplots(figsize=(11,5.0))
ax.loglog(rank,vals,".",color=TEAL,ms=4,alpha=0.6,label="roots (Book6)")
ax.loglog(rank,10**(intercept)*rank**slope,"-",color=RED,lw=2,label=f"fit slope = {slope:.2f}")
ax.set_xlabel("rank (most→least frequent root)"); ax.set_ylabel("frequency")
ax.set_title("Codon usage — the Zipf curve of root frequency")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"bio_zipf.png")); plt.close()

# ---- FIG 2: full letter (base) distribution ----
letters=Counter()
import re as _re
_isar=lambda ch: bool(_re.match(r"[\u0600-\u06FF]",ch))
for ts in toks:
    for t in ts:
        for ch in t:
            if _isar(ch): letters[ch]+=1
items=letters.most_common()
tot=sum(letters.values())
labs=[ch for ch,_ in items]; pct=[100*c/tot for _,c in items]
fig,ax=plt.subplots(figsize=(11,4.8))
ax.bar(range(len(labs)),pct,color=TEAL,edgecolor="white")
ax.set_xticks(range(len(labs))); ax.set_xticklabels(labs,fontsize=12)
ax.set_xlabel("letter (base) — by corpus frequency"); ax.set_ylabel("% of all root letters")
ax.set_title(f"Base composition — the full {len(labs)}-letter distribution (Book6)")
plt.tight_layout(); plt.savefig(os.path.join(FIG,"bio_letters.png")); plt.close()

# ---- FIG 3: richness vs length scatter (114 suras) + trend ----
bysur={}
for i,s in enumerate(sur): bysur.setdefault(s,[]).extend(toks[i])
S=sorted(bysur); length=np.array([len(bysur[s]) for s in S],float)
rich=np.array([len(set(bysur[s]))/max(1,len(bysur[s])) for s in S],float)
lr=np.log10(length); a,b=np.polyfit(lr,rich,1); corr=np.corrcoef(lr,rich)[0,1]
fig,ax=plt.subplots(figsize=(11,5.0))
ax.scatter(length,rich,s=28,color=TEAL,alpha=0.7,edgecolor="white")
xs=np.linspace(length.min(),length.max(),100)
ax.plot(xs,a*np.log10(xs)+b,"-",color=RED,lw=2,label=f"trend (r = {corr:+.2f})")
ax.set_xscale("log"); ax.set_xlabel("sūra length (root-tokens, log scale)"); ax.set_ylabel("lexical richness")
ax.set_title("Sequence complexity — richness falls with length (114 sūras)")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"bio_richness.png")); plt.close()

# ---- FIG 5: Markov conditional-entropy decay (uses the APP's normalize_letters + seg_tokens -> exact 4.086/3.525) ----
import sys as _sys, random as _random
_sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Downloads/Quran_Root_Explorer_Web_v1.2")
try:
    import analysis as _an
    _corp=_an.load_corpus(BOOK6); _nl=_an.normalize_letters
    def _gr(shuf=False,seed=7):
        _rng=_random.Random(seed); G={m:Counter() for m in (1,2,3,4)}
        for toks_ in _corp.seg_tokens:
            for tk in toks_:
                chars=[ch for ch in _nl(tk) if ch.strip()]
                if shuf: _rng.shuffle(chars)
                nt="".join(chars)
                for m in (1,2,3,4):
                    for i in range(len(nt)-m+1): G[m][nt[i:i+m]]+=1
        return G
    def _H(c):
        tot=sum(c); return -sum((v/tot)*math.log2(v/tot) for v in c if v>0) if tot>0 else 0
    def _cond(G):
        H={m:_H(G[m].values()) for m in G}; orders=[0]; vals=[H[1]]
        for m in (1,2,3): vals.append(H[m+1]-H[m]); orders.append(m)
        return orders,vals
    o,v=_cond(_gr(False)); _,vs=_cond(_gr(True))
    fig,ax=plt.subplots(figsize=(11,4.8))
    ax.plot(o,v,"-o",color=TEAL,lw=2.4,ms=9,label="observed (real words)")
    ax.plot(o,vs,"--o",color=GREY,lw=2,ms=7,label="letters shuffled within words")
    for k,h in zip(o,v): ax.annotate(("H%d = %.3f"%(k,h) if k<=1 else "%.3f"%h),(k,h),xytext=(k+0.06,h+0.13),color=NAVY,fontsize=12)
    ax.set_xticks(o); ax.set_xlabel("context length k (previous letters)")
    ax.set_ylabel("conditional entropy (bits / letter)")
    ax.set_title("Markov memory — H0 4.086 → H1 3.525; observed sits BELOW the shuffled baseline")
    ax.legend(frameon=False,fontsize=13)
    plt.tight_layout(); plt.savefig(os.path.join(FIG,"bio_markov.png")); plt.close()
    print("bio_markov: H0=%.3f cond1=%.3f"%(v[0],v[1]))
except Exception as _e:
    print("markov fig skipped:",type(_e).__name__,_e)

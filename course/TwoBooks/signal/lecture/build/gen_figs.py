# -*- coding: utf-8 -*-
"""Dense Signal data-figures, computed LIVE from Book6.xlsx (fixed seed). Per COURSE_STANDARDS 12a.
Outputs high-DPI PNGs to ../figs/. Transliteration labels (no unshaped Arabic in matplotlib)."""
import os, json, numpy as np, pandas as pd, math
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from collections import Counter
SEED=7; rng=np.random.default_rng(SEED)
HERE=os.path.dirname(os.path.abspath(__file__)); LEC=os.path.dirname(HERE)
FIG=os.path.join(LEC,"figs"); os.makedirs(FIG,exist_ok=True)
BOOK6=os.path.join(LEC,"..","..","..","Book6.xlsx")   # RootCourse/Book6.xlsx
NAVY="#1E2761"; TEAL="#0E9D8C"; AMBER="#B8860B"; RED="#A23B3B"; GREY="#6a6a6a"; ICE="#9fc0e8"
plt.rcParams.update({"font.size":15,"axes.titlesize":18,"axes.labelsize":15,
                     "xtick.labelsize":13,"ytick.labelsize":13,"figure.dpi":150,
                     "axes.spines.top":False,"axes.spines.right":False,"font.family":"DejaVu Sans"})

# ---- load corpus ----
raw=pd.read_excel(BOOK6,header=None)
hdr=[i for i in range(15) if any("سوره" in str(v) for v in raw.iloc[i]) and any("ریشه" in str(v) for v in raw.iloc[i])][0]
df=pd.read_excel(BOOK6,header=hdr)
ROO=[c for c in df.columns if str(c).strip()=="ریشه نحوی"][0]
SUR=[c for c in df.columns if "سوره" in str(c) and "اسم" not in str(c)][0]
AYA=[c for c in df.columns if "آیه" in str(c)][0]
df=df.dropna(subset=[SUR,AYA]).reset_index(drop=True); df[ROO]=df[ROO].fillna("")
TR={"ی":"ي","ک":"ك","ى":"ي","ة":"ه","أ":"ا","إ":"ا","آ":"ا","ؤ":"و","ئ":"ي"}
def norm(s): return "".join(TR.get(ch,ch) for ch in s)
toks=[set(norm(x) for x in str(s).split()) for s in df[ROO].tolist()]
sur=df[SUR].astype(int).tolist()
N=len(df)                                   # 6236 ayahs in mushaf order
bank=json.load(open(os.path.join(LEC,"..","handson","signal_data_bank.json"),encoding="utf-8"))
ROOTS=[(b["translit"],norm(b["root"]),b["fano"],b["p"]) for b in bank]

def shannon(counts):
    tot=sum(counts); 
    if tot<=0: return 0.0
    return -sum((c/tot)*math.log2(c/tot) for c in counts if c>0)

# =========================================================
# FIG 1 — occurrence raster: 12 roots across the 6,236-ayah reading order
# =========================================================
fig,ax=plt.subplots(figsize=(11,5.2))
for yi,(tr,r,fano,p) in enumerate(ROOTS):
    pos=[i for i,t in enumerate(toks) if r in t]
    ax.scatter(pos,[yi]*len(pos),marker="|",s=70,linewidths=0.7,
               color=TEAL if fano>1 else GREY,alpha=0.85)
    ax.text(N+60,yi,f"Fano {fano:.0f}",va="center",fontsize=11,color=NAVY)
ax.set_yticks(range(len(ROOTS))); ax.set_yticklabels([t for t,_,_,_ in ROOTS])
ax.set_xlim(0,N+700); ax.set_ylim(-0.6,len(ROOTS)-0.4)
ax.set_xlabel("ayah index in reading order (0 → 6,235)")
ax.set_title("Occurrence raster — every root arrives in CLUSTERS, not evenly (Book6)")
ax.invert_yaxis()
plt.tight_layout(); plt.savefig(os.path.join(FIG,"sig_raster.png")); plt.close()

# =========================================================
# FIG 2 — sūra-length multi-lag autocorrelation + permutation null band
# =========================================================
vps=Counter(sur); ser=np.array([vps.get(s,0) for s in range(1,115)],float)
sc=ser-ser.mean(); den=np.dot(sc,sc)
def acf(x,L):
    xc=x-x.mean(); d=np.dot(xc,xc) or 1.0
    return [np.dot(xc[:len(x)-k],xc[k:])/d for k in range(L+1)]
L=25; obs=acf(ser,L)
nd=2000; null=np.empty((nd,L+1))
for j in range(nd):
    null[j]=acf(rng.permutation(ser),L)
lo=np.percentile(null,2.5,0); hi=np.percentile(null,97.5,0)
fig,ax=plt.subplots(figsize=(11,5.0))
ax.fill_between(range(L+1),lo,hi,color=ICE,alpha=0.6,label="shuffled null (95%)")
ax.axhline(0,color=GREY,lw=1)
ax.plot(range(L+1),obs,"-o",color=TEAL,lw=2.2,ms=5,label="observed (muṣḥaf order)")
ax.annotate(f"lag-1 = +{obs[1]:.2f}",(1,obs[1]),xytext=(4,obs[1]+0.04),
            color=NAVY,fontsize=14,arrowprops=dict(arrowstyle="->",color=NAVY))
ax.set_xlabel("lag (sūras)"); ax.set_ylabel("autocorrelation")
ax.set_title("Sūra-length memory — autocorrelation vs the shuffled null")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"sig_autocorr.png")); plt.close()

# =========================================================
# FIG 3 — full FFT power spectrum of per-sūra letter-entropy + null threshold
# (letter-entropy per sūra from the segmented root text letters)
# =========================================================
# per-sūra letter entropy from the root column letters (proxy signal, same shape family)
seg_by_sur={}
for i in range(N):
    s=sur[i]; seg_by_sur.setdefault(s,Counter())
    for ch in str(df[ROO].iloc[i]):
        if ch.strip() and ch not in " ": seg_by_sur[s][norm(ch)]+=1
H=np.array([shannon(seg_by_sur.get(s,Counter()).values()) for s in range(1,115)],float)
Hd=H-H.mean()
power=np.abs(np.fft.rfft(Hd))**2
freqs=np.fft.rfftfreq(len(Hd),d=1.0)
# shuffle null for the per-frequency power
nd=2000; nullp=np.empty((nd,len(power)))
for j in range(nd):
    nullp[j]=np.abs(np.fft.rfft(rng.permutation(Hd)))**2
thr=np.percentile(nullp,95,0)
fig,ax=plt.subplots(figsize=(11,5.0))
ax.plot(freqs[1:],power[1:],"-",color=TEAL,lw=2,label="observed power")
ax.plot(freqs[1:],thr[1:],"--",color=RED,lw=1.6,label="shuffle 95% threshold")
pk=1+int(np.argmax(power[1:])); 
ax.scatter([freqs[pk]],[power[pk]],color=NAVY,zorder=5)
ax.annotate("peak at LOWEST frequency\n= slow trend, not a cycle",(freqs[pk],power[pk]),
            xytext=(freqs[pk]+0.08,power[pk]*0.8),color=NAVY,fontsize=13,
            arrowprops=dict(arrowstyle="->",color=NAVY))
ax.set_xlabel("frequency (cycles per sūra)"); ax.set_ylabel("power")
ax.set_title("Letter-entropy power spectrum — low-frequency peak beats the null")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"sig_spectrum.png")); plt.close()

# =========================================================
# FIG 4 — Ricker (mexican-hat) continuous-wavelet scalogram of the entropy signal
# =========================================================
def ricker(points,a):
    A=2/(math.sqrt(3*a)*math.pi**0.25); vec=np.arange(0,points)-(points-1.0)/2
    x2=(vec/a)**2; return A*(1-x2)*np.exp(-x2/2)
def cwt(sig,widths):
    out=np.empty((len(widths),len(sig)))
    for i,a in enumerate(widths):
        w=ricker(min(10*a,len(sig)),a); out[i]=np.convolve(sig,w,mode="same")
    return out
widths=np.arange(1,33)
scal=np.abs(cwt(Hd,widths))
fig,ax=plt.subplots(figsize=(11,4.8))
im=ax.imshow(scal,aspect="auto",cmap="viridis",extent=[0,114,widths[-1],widths[0]])
ax.set_xlabel("sūra position in reading order"); ax.set_ylabel("scale (≈ sūras)")
ax.set_title("Ricker scalogram — energy at COARSE scales, spread across the order",pad=10)
    fig.subplots_adjust(left=0.10,right=0.99,top=0.88)
cb=fig.colorbar(im,ax=ax,fraction=0.046,pad=0.02); cb.set_label("|coefficient|",fontsize=12)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"sig_scalogram.png")); plt.close()

# =========================================================
# FIG 5 — āyah-length distribution histogram + mean & CV
# =========================================================
ln=np.array([len(str(df[ROO].iloc[i]).split()) for i in range(N)],float)
cv=ln.std()/ln.mean()
fig,ax=plt.subplots(figsize=(11,4.8))
ax.hist(ln,bins=range(0,int(ln.max())+2),color=TEAL,alpha=0.85,edgecolor="white")
ax.axvline(ln.mean(),color=RED,lw=2,label=f"mean = {ln.mean():.1f} root-tokens")
ax.set_xlim(0,40)
ax.set_xlabel("root-tokens per āyah"); ax.set_ylabel("number of āyahs")
ax.set_title(f"Āyah-length distribution — wide, speech-like rhythm (CV = {cv:.2f})")
ax.legend(frameon=False,fontsize=13)
plt.tight_layout(); plt.savefig(os.path.join(FIG,"sig_ayahlen.png")); plt.close()

print("figures written to",FIG)
for f in sorted(os.listdir(FIG)): print("  ",f)
print(f"verify: lag-1={obs[1]:.3f} | CV={cv:.3f} | spectrum peak freq={freqs[pk]:.3f}")

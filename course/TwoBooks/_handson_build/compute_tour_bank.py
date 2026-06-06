# -*- coding: utf-8 -*-
import json, sys, math, numpy as np
from collections import Counter
sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2"); import analysis as A, twobooks_stats as T
c=A.load_corpus("/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2/Book6.xlsx"); N=len(c.df); L,R=T.per_sura_letters_roots(c)
mus={s:s for s in range(1,115)}; nuz={int(k):int(v) for k,v in c.rev_order_of_surah.items()}
def wm(pos,fams):
    tot=n=0
    for ss in fams:
        ps=[pos[s] for s in ss]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)): tot+=abs(ps[i]-ps[j]); n+=1
    return tot/n if n else 0
def pm(v):
    n=len(v); t=k=0
    for i in range(n):
        for j in range(i+1,n): t+=abs(v[i]-v[j]); k+=1
    return t/k if k else 0
def shuf_p(valfn, direction, nd=2000, seed=1):
    obs=wm(valfn,T.MUQ_MULTI); base=list(T.MUQ); rng=np.random.default_rng(seed); out=np.empty(nd)
    for kk in range(nd):
        rng.shuffle(base); idx=0; f=[]
        for sz in T.MUQ_SIZES: f.append(base[idx:idx+sz]); idx+=sz
        out[kk]=wm(valfn,f)
    return round(float((np.sum(out<=obs)+1)/(nd+1)) if direction=="less" else float((np.sum(out>=obs)+1)/(nd+1)),5)
contig_m=shuf_p(mus,"less"); contig_n=shuf_p(nuz,"less",seed=2)
verses={};su=c.df[A.COL_SURAH].astype(int).tolist();ay=c.df[A.COL_AYAH].astype(int).tolist()
for i in range(len(c.df)): verses[su[i]]=max(verses.get(su[i],0),ay[i])
lenmap={s:float(verses[s]) for s in range(1,115)}; length_tag=shuf_p(lenmap,"less",seed=3)
# theme cosine
profs={s:Counter(R[s]) for s in T.MUQ}
def cos(a,b):
    ks=set(a)|set(b); d=sum(a[k]*b[k] for k in ks); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return d/(na*nb) if na and nb else 0
def theme_w(fams):
    import itertools as it; v=[]
    for ss in fams: v+=[cos(profs[a],profs[b]) for a,b in it.combinations(ss,2)]
    return float(np.mean(v)) if v else 0
base=list(T.MUQ); rng=np.random.default_rng(17); out=np.empty(2000)
for kk in range(2000):
    rng.shuffle(base); idx=0; f=[]
    for sz in T.MUQ_SIZES: f.append(base[idx:idx+sz]); idx+=sz
    out[kk]=theme_w(f)
theme_p=round(float((np.sum(out>=theme_w(T.MUQ_MULTI))+1)/2001),4)
# per-family p (mushaf, random subsets)
def fam_p(mem,nd=2000,seed=7):
    obs=pm([mus[s] for s in mem]); rng=np.random.default_rng(seed); out=np.empty(nd)
    for j in range(nd):
        pk=rng.choice(range(1,115),size=len(mem),replace=False); out[j]=pm([int(x) for x in pk])
    return round(float((np.sum(out<=obs)+1)/(nd+1)),4)
perfam={nm:fam_p(mem) for nm,mem in T.MUQ_FAMILIES.items()}
# specials
def special(metric,direction,nd=2000,seed=11):
    allv={s:metric(s) for s in range(1,115)}; obs=np.mean([allv[s] for s in T.MUQ]); rng=np.random.default_rng(seed); out=np.empty(nd)
    for j in range(nd):
        pk=rng.choice(range(1,115),size=len(T.MUQ),replace=False); out[j]=np.mean([allv[int(x)] for x in pk])
    return round(float((np.sum(out>=obs)+1)/(nd+1)) if direction=="greater" else float((np.sum(out<=obs)+1)/(nd+1)),4)
le_p=special(lambda s:T.shannon_bits(L[s].values()),"greater")
re_p=special(lambda s:T.shannon_bits(Counter(R[s]).values()),"greater")
rich_p=special(lambda s:(len(set(R[s]))/len(R[s]) if R[s] else 0),"less")
# embedding
vocab=sorted({r for s in T.MUQ for r in profs[s]}); vi={r:i for i,r in enumerate(vocab)}
M=np.zeros((len(T.MUQ),len(vocab)))
for row,s in enumerate(T.MUQ):
    tot=sum(profs[s].values()) or 1
    for r,cnt in profs[s].items(): M[row,vi[r]]=cnt/tot
U,S,_=np.linalg.svd(M-M.mean(0),full_matrices=False); emb=U[:,:10]*S[:10]; pos={s:emb[i] for i,s in enumerate(T.MUQ)}
def cd(a,b):
    na=np.linalg.norm(a);nb=np.linalg.norm(b); return 1-(a@b/(na*nb)) if na and nb else 1
def ew(fams):
    d=[cd(pos[ss[i]],pos[ss[j]]) for ss in fams for i in range(len(ss)) for j in range(i+1,len(ss))]; return float(np.mean(d)) if d else 0
rng=np.random.default_rng(23); out=np.empty(2000); base=list(T.MUQ)
for t in range(2000):
    rng.shuffle(base); idx=0; f=[]
    for sz in T.MUQ_SIZES: f.append(base[idx:idx+sz]); idx+=sz
    out[t]=ew(f)
emb_p=round(float((np.sum(out<=ew(T.MUQ_MULTI))+1)/2001),4)
import statistics as stx
med_muq=int(stx.median([verses[s] for s in T.MUQ])); med_oth=int(stx.median([verses[s] for s in verses if s not in T.MUQ]))
# SIGNAL
ser=np.array([verses[s] for s in range(1,115)],float); sc=ser-ser.mean(); ac1=round(float(np.dot(sc[:-1],sc[1:])/np.dot(sc,sc)),3)
H=np.array([T.shannon_bits(L[s].values()) for s in range(1,115)]); Hd=H-H.mean(); peak=float((np.abs(np.fft.rfft(Hd))**2)[1:].max())
rng=np.random.default_rng(7); o=np.empty(2000); b=Hd.copy()
for j in range(2000): rng.shuffle(b); o[j]=float((np.abs(np.fft.rfft(b))**2)[1:].max())
fft_p=round(float((np.sum(o>=peak)+1)/2001),4)
def haar(x):
    x=x.astype(float).copy(); det=[]
    while len(x)>1:
        a=(x[0::2]+x[1::2])/np.sqrt(2); d=(x[0::2]-x[1::2])/np.sqrt(2); det.append(d); x=a
    return det
def lvl(s):
    v=np.asarray(s,float)-np.mean(s); n2=1<<int(np.ceil(np.log2(len(v)))); vp=np.zeros(n2); vp[:len(v)]=v
    return np.array([float(np.sum(d*d)) for d in haar(vp)])
en=lvl(H); scales=[2**(k+1) for k in range(len(en))]; rng=np.random.default_rng(11); nul=np.empty((2000,len(en)))
for j in range(2000): nul[j]=lvl(rng.permutation(H))
wav=[scales[k] for k in range(len(en)) if (np.sum(nul[:,k]>=en[k])+1)/2001<0.05]
al=np.array([len(t) for t in c.seg_tokens]); cv=round(float(al.std()/al.mean()),2)
# BIOLOGY
uni=Counter()
for toks in c.root_tokens:
    for t in toks: uni[t]+=1
ranked=uni.most_common(); ranks=np.arange(1,len(ranked)+1); fr=np.array([x[1] for x in ranked],float)
zipf=round(float(np.polyfit(np.log10(ranks),np.log10(fr),1)[0]),2)
g1=Counter(); g2=Counter()
for toks in c.seg_tokens:
    for t in toks:
        nt="".join(x for x in A.normalize_letters(t) if x.strip())
        for ch in nt: g1[ch]+=1
        for i in range(len(nt)-1): g2[nt[i:i+2]]+=1
H0=round(T.shannon_bits(g1.values()),3); cond1=round(T.shannon_bits(g2.values())-T.shannon_bits(g1.values()),3)
# di-codon (light: nd=200)
ar=[list(t) for t in c.root_tokens]; big=Counter()
for toks in ar:
    for x,y in zip(toks,toks[1:]): big[(x,y)]+=1
ntok=sum(uni.values()); common=set([r for r,_ in uni.most_common(150)])
def chi(bg):
    tot=0.0
    for (a,b),oo in bg.items():
        if a in common and b in common:
            ex=uni[a]*uni[b]/ntok
            if ex>0: tot+=(oo-ex)**2/ex
    return tot
obs=chi(big); flat=np.array([t for toks in ar for t in toks],dtype=object); lens=[len(t) for t in ar]
rng=np.random.default_rng(9); o=np.empty(200)
for j in range(200):
    perm=flat.copy(); rng.shuffle(perm); bg=Counter(); p0=0
    for Ln in lens:
        seg=perm[p0:p0+Ln]; p0+=Ln
        for x,y in zip(seg,seg[1:]): bg[(x,y)]+=1
    o[j]=chi(bg)
dicodon_p=round(float((np.sum(o>=obs)+1)/201),4)
bank=dict(contiguity_mushaf=contig_m,contiguity_nuzul=contig_n,theme_p=theme_p,length_tag_p=length_tag,
          letter_entropy_p=le_p,root_entropy_p=re_p,lexical_richness_p=rich_p,embedding_p=emb_p,
          perfam=perfam,median_muq=med_muq,median_other=med_oth,
          signal=dict(autocorr_lag1=ac1,fft_peak_p=fft_p,wavelet_sig_scales=wav,ayah_len_cv=cv),
          biology=dict(zipf_slope=zipf,markov_H0=H0,markov_cond1=cond1,dicodon_p=dicodon_p))
json.dump(bank,open("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/_handson_build/tour_bank.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("OK contig_m",contig_m,"perfam",perfam,"theme",theme_p,"len_tag",length_tag,"rich",rich_p,"emb",emb_p)
print("   signal ac1",ac1,"fft",fft_p,"wav",wav,"cv",cv,"| bio zipf",zipf,"H0",H0,"cond1",cond1,"dicodon",dicodon_p)

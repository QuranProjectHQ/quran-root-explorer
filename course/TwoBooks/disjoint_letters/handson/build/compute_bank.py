# -*- coding: utf-8 -*-
# Data bank for the Disjoint-Letters hands-on kit. Single source = the app's own
# kernel (twobooks_stats) over Book6, so kit and live app cannot disagree.
import json, sys, numpy as np
sys.path.insert(0, "/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2")
import analysis as A, twobooks_stats as T
c = A.load_corpus("/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2/Book6.xlsx")
L, _ = T.per_sura_letters_roots(c)
NAME = {int(c.df[A.COL_SURAH].iat[i]): str(c.df[A.COL_SURAH_NAME].iat[i]) for i in range(len(c.df))}
def dens(s, ch):
    tot = sum(L[s].values()); return (L[s].get(ch,0)/tot) if tot else 0.0
def enr(ch, nd=20000, seed=13):
    bearers = [s for s in T.MUQ if ch in T.LETTERS_OF[s]]
    d = {s: dens(s, ch) for s in range(1,115)}
    obs = float(np.mean([d[s] for s in bearers]))
    rng = np.random.default_rng(seed); out = np.empty(nd)
    for j in range(nd):
        pick = rng.choice(range(1,115), size=len(bearers), replace=False)
        out[j] = np.mean([d[int(x)] for x in pick])
    p = (np.sum(out >= obs) + 1)/(nd+1)
    # sample sūra for the by-hand part: the bearer with the highest density of ch
    samp = max(bearers, key=lambda s: d[s])
    tot = sum(L[samp].values())
    return dict(letter=ch, n_bearers=len(bearers), bearer_mean=round(obs,4), p=round(float(p),4),
                sample_sura=samp, sample_name=NAME[samp], sample_count=L[samp].get(ch,0),
                sample_total=tot, sample_density_pct=round(100*d[samp],2))
letters = [enr(ch) for ch in T.DISJOINT_LETTERS]
# qaf detail for the walkthrough
qd = {s: dens(s,"ق") for s in range(1,115)}
qaf = dict(sura50_rank=sorted(range(1,115), key=lambda s: qd[s]).index(50)+1,
           sura50_count=L[50].get("ق",0), sura50_total=sum(L[50].values()),
           sura50_density_pct=round(100*qd[50],2),
           p=[x for x in letters if x["letter"]=="ق"][0]["p"])
# contiguity p (mushaf) + medians, from the kernel battery logic
mus={s:s for s in range(1,115)}
def wm(pos,fams):
    tot=n=0
    for ss in fams:
        ps=[pos[s] for s in ss]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)): tot+=abs(ps[i]-ps[j]); n+=1
    return tot/n if n else 0
rng=np.random.default_rng(1); base=list(T.MUQ); out=np.empty(20000)
for k in range(20000):
    rng.shuffle(base); idx=0; f=[]
    for sz in T.MUQ_SIZES: f.append(base[idx:idx+sz]); idx+=sz
    out[k]=wm(mus,f)
contig_p=float((np.sum(out<=wm(mus,T.MUQ_MULTI))+1)/20001)
su=c.df[A.COL_SURAH].astype(int).tolist(); ay=c.df[A.COL_AYAH].astype(int).tolist()
V={}
for i in range(len(c.df)): V[su[i]]=max(V.get(su[i],0),ay[i])
import statistics as stx
med_muq=int(stx.median([V[s] for s in T.MUQ])); med_oth=int(stx.median([V[s] for s in V if s not in T.MUQ]))
bank=dict(letters=letters, qaf=qaf, contiguity_p_mushaf=contig_p, median_muq=med_muq, median_other=med_oth,
          n_sig=sum(1 for x in letters if x["p"]<0.05))
json.dump(bank, open("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/disjoint_letters/handson/dl_data_bank.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)
print("bank written. sig letters:", bank["n_sig"], "| qaf rank", qaf["sura50_rank"], "p", qaf["p"],
      "| contig_p", round(contig_p,6), "| medians", med_muq, med_oth)

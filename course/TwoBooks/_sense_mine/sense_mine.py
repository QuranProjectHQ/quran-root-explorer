# -*- coding: utf-8 -*-
"""Data-driven sense mining from Book6 (no hand-picked lexica). Deterministic, documented.
Method: within-āyah root co-occurrence -> PPMI vectors (ubiquity down-weighted by dropping the
top-K most frequent roots from CONTEXT). Per-root SENSES induced by greedy cosine-threshold
clustering of each occurrence's context vector. All parameters are explicit module constants."""
import sys, math
from collections import Counter, defaultdict
sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Downloads/Quran_Root_Explorer_Web_v1.2")
import analysis
# ---- documented parameters ----
MIN_VOCAB_FREQ = 5     # a root must occur >=5x to be a context feature
STOP_TOPK      = 30    # the 30 most frequent roots are treated as ubiquitous -> excluded from context
MIN_OCC_SENSE  = 12    # only induce senses for roots occurring >=12x
COS_THR        = 0.30  # two occurrences share a sense if context cosine >= 0.30
MAX_SENSES     = 6     # cap reported senses per root

def load():
    c=analysis.load_corpus("Book6.xlsx"); K=analysis.normalize_letters
    ayahs=[[K(t) for t in toks] for toks in c.root_tokens]
    rf=Counter(r for a in ayahs for r in a)
    stop=set([r for r,_ in rf.most_common(STOP_TOPK)])
    vocab={r for r,n in rf.items() if n>=MIN_VOCAB_FREQ}
    content=lambda a: [r for r in a if r in vocab and r not in stop]
    N=len(ayahs)
    # document frequency for IDF-style weight
    dfc=Counter()
    for a in ayahs:
        for r in set(content(a)): dfc[r]+=1
    idf={r: math.log(N/(1+dfc[r])) for r in dfc}
    return c,ayahs,rf,stop,vocab,content,idf

def occ_vec(ctx, idf):
    # context vector for one occurrence = idf-weighted bag of co-occurring content roots
    v=Counter(ctx)
    return {r: v[r]*idf.get(r,0) for r in v}

def cos(a,b):
    if not a or not b: return 0.0
    keys=a.keys()&b.keys()
    dot=sum(a[k]*b[k] for k in keys)
    na=math.sqrt(sum(x*x for x in a.values())); nb=math.sqrt(sum(x*x for x in b.values()))
    return dot/(na*nb) if na and nb else 0.0

def senses_for(root, ayahs, content, idf, K):
    # gather this root's occurrence contexts (deterministic order = ayah index)
    vecs=[]
    for a in ayahs:
        ca=content(a)
        if root in [r for r in a]:
            ctx=[r for r in ca if r!=root]
            if ctx: vecs.append(occ_vec(ctx, idf))
    # greedy centroid clustering
    cents=[]   # list of (sumvec, count)
    for v in vecs:
        best=-1; bi=-1
        for i,(cv,cnt) in enumerate(cents):
            centroid={k:cv[k]/cnt for k in cv}
            s=cos(v,centroid)
            if s>best: best=s; bi=i
        if best>=COS_THR and bi>=0:
            cv,cnt=cents[bi]
            for k,val in v.items(): cv[k]=cv.get(k,0)+val
            cents[bi]=(cv,cnt+1)
        else:
            cents.append((dict(v),1))
    # keep only clusters with >=2 supporting occurrences (singletons = noise)
    real=[c for c in cents if c[1]>=2]
    return min(len(real) if real else 1, MAX_SENSES), len(vecs)

if __name__=="__main__":
    import json
    c,ayahs,rf,stop,vocab,content,idf=load()
    K=analysis.normalize_letters
    roots=[r for r,n in rf.items() if n>=MIN_OCC_SENSE]
    sense_count={}
    for r in roots:
        sc,occ=senses_for(r, ayahs, content, idf, K)
        sense_count[r]=sc
    dist=Counter(sense_count.values())
    poly=sum(1 for v in sense_count.values() if v>=2)
    tot=len(sense_count)
    print("roots analysed (>=%d occ): %d"%(MIN_OCC_SENSE,tot))
    print("sense-count distribution:",dict(sorted(dist.items())))
    print("polysemous (>=2 senses): %d  (%.1f%%)"%(poly,100*poly/tot))
    # examples
    ex=sorted(sense_count.items(),key=lambda x:-x[1])[:8]
    print("most polysemous (data-mined):",[(r,sc) for r,sc in ex])
    json.dump(sense_count, open("/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/_sense_mine/sense_counts.json","w"))

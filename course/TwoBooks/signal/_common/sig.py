# -*- coding: utf-8 -*-
"""Shared builders for signal lectures 3-17. Root anchor. Real data from data.json."""
import os, sys, json, math
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from st_slides import *
from st_slides import _tb,_rect,_fill_panel
from diagrams import fbox,harrow,vdash,band,sigrow,matgrid,isocube,chain
from pptx.util import Inches,Pt
DATA=json.load(open(os.path.join(HERE,"data.json"),encoding="utf-8"))
ROOT=os.path.abspath(os.path.join(HERE,".."))

def two(s,A,B,sp=0.5,fa=TINT,fb=TINT2): two_stack(s,A,B,split=sp,fillA=fa,fillB=fb)
def three(s,A,B,C,f=(TINT,AMBERT,TINT2)): three_stack(s,A,B,C,fills=f)

def titleslide(prs,tag,headline,body1,body2):
    s=slide(prs)
    panel(s,0.42,1.05,12.5,1.5,TINT2,[L(tag,15,True,TEAL),L(headline,24,True,NAVY)],space=6)
    panel(s,0.42,2.85,12.5,4.35,TINT,[L(body1,16.5),L(body2,16,True,TEAL)],space=9)
    return s

def Tt(prs,t,sz=21):
    s=slide(prs); title(s,t,sz); return s

def line_signal(s,x,y,w,vals,col=TEAL,bh=2.1,labels=None,vmax=None):
    """editable bar 'waveform' for a root-signal."""
    vals=list(vals); n=len(vals); cw=w/n; vmax=vmax or (max(vals) if vals else 1); base=y+bh
    _rect(s,x,base,w,0.02,GREY)
    for i,v in enumerate(vals):
        h=0.06+(v/vmax)*(bh-0.3)
        b=s.shapes.add_shape(5,Inches(x+i*cw+cw*0.12),Inches(base-h),Inches(cw*0.76),Inches(h))
        b.fill.solid(); b.fill.fore_color.rgb=col; b.line.fill.background()
        if labels and i<len(labels):
            _tb(s,x+i*cw-0.05,base+0.05,cw+0.1,0.4,[(labels[i],14,True,NAVY)])

def audit(s,ok,bad,sil):
    title(s,"Audit — supported, broken, and silent")
    three(s,[L("✓ SUPPORTED",17,True,TEAL),L(ok,16)],
            [L("✗ BREAKS",17,True,RED),L(bad,16)],
            [L("~ SILENT",17,True,AMBER),L(sil,16)],f=(TINT,REDT,AMBERT))

def takeaway(s,rel,take):
    title(s,"Real-world relevance & takeaway")
    two(s,[L("REAL-WORLD RELEVANCE",18,True,NAVY),L(rel,17,True,TEAL)],
          [L("THE TAKEAWAY",18,True,AMBER),L(take,17,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)

def appslide(prs,steps,body):
    s=slide(prs); title(s,"The app — explore it live")
    band(s,0.42,1.2,12.5,0.4,TINT,"root anchor · real verse · live transform",TEAL)
    x=0.55; bw=2.98; aw=0.1
    for i,(t,sub,fl,ln) in enumerate(steps):
        fbox(s,x,1.9,bw,1.35,fl,t,sub,line=ln,tsz=15,ssz=11)
        if i<len(steps)-1: harrow(s,x+bw-0.02,2.45,aw+0.05,"",color=GREY)
        x+=bw+aw
    panel(s,0.42,4.65,12.5,2.55,TINT,[L("Hands on the data",18,True,NAVY),L(body,16.5,True,TEAL)],space=7)

def save(prs,folder,fname):
    out=os.path.join(ROOT,folder); 
    prs.save(os.path.join(out,fname))
    return len(prs.slides)

UNIT={3:"A · Foundations",4:"B · Signal in time",5:"B · Signal in time",6:"B · Signal in time",
 7:"B · Signal in time",8:"B · Signal in time",9:"C · In frequency",10:"C · In frequency",
 11:"C · In frequency",12:"D · Information & space",13:"D · Information & space",14:"D · Information & space",
 15:"E · Structure & synthesis",16:"E · Structure & synthesis",17:"E · Structure & synthesis"}
TITLES={3:"Vectorization Schemes",4:"The Waveform",5:"Sampling & Quantization",6:"Smoothing, Trend & Difference",
 7:"Convolution & LTI Systems",8:"Autocorrelation & Periodicity",9:"Fourier & the Spectrum",
 10:"Dominant Frequencies & Rhythm",11:"Filtering",12:"Energy, Norm & Entropy",13:"Distance & Similarity",
 14:"Embeddings",15:"Dimensionality Reduction (PCA)",16:"Clustering & the Spectrogram",17:"Synthesis & Capstone"}

def threads_block(prs,crit,latent,reorder,readback,baseline):
    s=Tt(prs,"Criteria — the amplitude is a measurement, not a label")
    two(s,[L("THE NUMBER MUST MEASURE",18,True,TEAL),L(crit,16.5,True,NAVY)],
          [L("ANCHOR = ROOT",18,True,AMBER),L("Computed over root-tokens (ریشه); root IDENTITY is nominal and is encoded before any arithmetic. Frequency/length are ratio-scale and safe.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
    s=Tt(prs,"The objective — the latent feature this surfaces")
    two(s,[L("WHAT WE ARE HUNTING",18,True,NAVY),L(latent,16.5,True,TEAL)],
          [L("VECTOR → TRANSFORM → FEATURE",18,True,NAVY),L("Digitize on the root, apply this lecture’s operation, and read out the hidden structure. The vector is the doorway; the latent feature is the room.",16.5)],sp=0.5,fa=TINT2,fb=TINT)
    s=Tt(prs,"Reordering — a declared tool, not a violation")
    two(s,[L("MANIPULATE TO REVEAL",18,True,TEAL),L(reorder,16.5,True,NAVY)],
          [L("THE ONE RULE",18,True,RED),L("Any structure found by searching reorderings/configurations must still beat a null — or it is an artifact, not a feature. The shuffle null is itself a reordering.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
    s=Tt(prs,"The anchor — read the feature back into the text")
    two(s,[L("INTERPRETIVE READ-BACK",18,True,TEAL),L(readback,16.5,True,NAVY)],
          [L("SEMANTIC vs FORMAL",18,True,AMBER),L("Meaning-claims answer to the roots/sense; form-claims answer to the text’s structure + a null. Map back to nothing and the number is numerology.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
    s=Tt(prs,"Validation — beat the null AND random Arabic")
    two(s,[L("NOT-RANDOM IS NOT ENOUGH",18,True,RED),L(baseline,16.5,True,NAVY)],
          [L("THE GAUNTLET",18,True,TEAL),L("verify → null → natural-language baseline → multiple-comparison correction → read-back. Most candidates die here; the survivors are real.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)

def roadmap_pos(prs,lec):
    s=Tt(prs,"Where this sits — the 17-lecture arc")
    band(s,0.42,1.2,12.5,0.4,TINT2,"five units · 17 lectures · root-anchored DSP on the āyah",NAVY)
    us=[("A · Foundations","1–3",TINT,TEAL),("B · in time","4–8",AMBERT,AMBER),("C · in frequency","9–11",TINT,TEAL),
        ("D · info & space","12–14",AMBERT,AMBER),("E · structure","15–17",TINT2,NAVY)]
    x=0.55; bw=2.42; aw=0.05
    for i,(t,sub,fl,ln) in enumerate(us):
        hi = (UNIT[lec].split(" ")[0]==t.split(" ")[0])
        fbox(s,x,1.9,bw,1.5,(REDT if hi else fl),t,sub+("  ← here" if hi else ""),line=(RED if hi else ln),tsz=13.5,ssz=10.5)
        if i<4: harrow(s,x+bw-0.03,2.5,aw+0.06,"",color=GREY)
        x+=bw+aw
    panel(s,0.42,4.75,12.5,2.45,TINT,[L("Lecture %d — %s  (Unit %s)"%(lec,TITLES[lec],UNIT[lec]),18,True,NAVY),
      L("Each lecture is one DSP idea on real root-vectors, building from the waveform to frequency, to information and distance, to structure. Same anchor, one object.",16.5,True,TEAL)],space=7)

def finish_block(prs,disc,synth,pit_wrong,pit_right):
    s=Tt(prs,"Synthesis & discussion")
    two(s,[L("FOR DISCUSSION",18,True,AMBER),L(disc,16.5)],
          [L("SYNTHESIS",18,True,NAVY),L(synth,16.5,True,TEAL)],sp=0.5,fa=AMBERT,fb=TINT)
    s=Tt(prs,"A common pitfall — and the fix")
    two(s,[L("THE PITFALL",18,True,RED),L(pit_wrong,16.5,True,NAVY)],
          [L("DO THIS INSTEAD",18,True,TEAL),L(pit_right,16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
def keyidea(prs,t,a,b):
    s=Tt(prs,t)
    two(s,[L("IN ONE LINE",18,True,NAVY),L(a,17,True,TEAL)],[L("CARRIES FORWARD",18,True,AMBER),L(b,16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)

NUM={
3:("Type-token ratio across the 114 sūras ranges 0.15 → 0.56 (median) → 1.00 — channel behaviour is not uniform; every sūra is processed.","Some sūras repeat roots heavily (low TTR), others never; the channel you pick must work across this whole range, not one verse."),
4:("Per-verse dynamic range (peak−trough of root frequency) across 6,139 verses: p10 = 118, median = 1,360, p90 = 2,839.","Most verses are spiky (one dominant root), some flat. The waveform vocabulary is read on all of them, not a favourite."),
5:("Verse-length quartiles (root-tokens) across 6,236 āyāt: 4 / 7 / 11 / 20 (Q1 / median / Q3 / p95).","Sampling resolution is set by length; three-quarters of verses have ≤11 roots — the corpus, not a long example, sets the regime."),
6:("Per-verse dynamic range across 6,139 verses (p10 118 · median 1,360 · p90 2,839) — the trend/detail split is computed on all.","Smoothing runs corpus-wide; the spread shows verses differ hugely in how much detail there is to remove."),
7:("Kernels are applied to every verse; verse lengths span 1 → 84 roots (quartiles 4 / 7 / 11 / 20).","A kernel must behave sensibly across the whole length range, not just on a chosen short sūra."),
8:("Of 114 sūras, 29 contain at least one exactly-repeated verse; 79 are long enough (≥20 verses) to test periodicity.","We scan every eligible sūra for periodicity, not only Ar-Raḥmān — its refrain is one of 29 repeat-bearing sūras."),
9:("79 of 114 sūras have ≥20 verses — the spectral-capable set; spectra are computed across all of them.","Ar-Raḥmān is one case; the Fourier method runs on every long sūra, with the scale rule enforced."),
10:("Rhythm (verse-length spectra) is read on all 79 long sūras; their lengths span widely.","Al-Fātiḥa illustrates; confident meter comes from the corpus of long sūras, not one short example."),
11:("Filtering is applied across the length range (quartiles 4 / 7 / 11 / 20); the debt verse (84) is the long extreme.","Cutoffs are tested across the whole corpus so a filter is never tuned to a single verse."),
12:("Per-sūra root entropy across all 114 sūras: 1.42 → 6.60 (median) → 7.93 bits.","Al-Qadr and Al-Kawthar are two points in this whole distribution; entropy is computed for every sūra."),
13:("Cosine similarity over 5,000 random length-matched verse pairs: median 0.51, 90th pct 0.88.","113 vs 114 is read against this whole-corpus distribution of pair-similarities, never in isolation."),
14:("Embeddings are learned from co-occurrence over all 51,044 root-tokens (1,702 distinct roots).","Neighbours of a root are judged within the full vocabulary, not a handful of hand-picked roots."),
15:("PCA is computed over all 114 sūras × 5 features; PC1 + PC2 explain 81% of the variance.","Every sūra is a point; the axes summarise the whole corpus, not selected sūras."),
16:("Clustering partitions all 114 sūras; 29 carry refrains and 79 are long — structure spans the corpus.","Clusters are formed from every sūra; none is excluded to make the picture tidy."),
17:("The capstone pipeline is validated on corpus-wide statistics (6,236 āyāt, 114 sūras) before any single-verse claim.","One verse is walked end-to-end for teaching; its claims are checked against the whole corpus."),
}
def corpus_slide(prs,lec):
    left,right=NUM[lec]
    s=Tt(prs,"Across the whole corpus — every āyah is a valid set")
    two(s,[L("WHOLE-CORPUS DISTRIBUTION",18,True,NAVY),L(left,16.5,True,TEAL)],
          [L("DIVERSITY BY DESIGN",18,True,AMBER),L(right,16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)

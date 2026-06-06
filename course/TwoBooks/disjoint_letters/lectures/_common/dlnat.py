# -*- coding: utf-8 -*-
"""Data + native-chart spec helpers for the 17-lecture DL course (editable charts)."""
import os,sys,numpy as np,itertools
from collections import Counter
import openpyxl
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from dlsig import *
import dlcharts as dc
# ---- data ----
wb=openpyxl.load_workbook("/sessions/stoic-cool-hawking/mnt/RootCourse/Book6.xlsx",read_only=True,data_only=True)
ws=wb.active; vmax={}; nuz={}; roots={}
for r in ws.iter_rows(values_only=True):
    if r[5] is None or not isinstance(r[5],(int,float)): continue
    su=int(r[5]); ay=int(r[6]) if isinstance(r[6],(int,float)) else 0
    vmax[su]=max(vmax.get(su,0),ay)
    if r[12] is not None and su not in nuz:
        try: nuz[su]=int(r[12])
        except: pass
    if r[8]: roots.setdefault(su,[]).extend(str(r[8]).split())
verses=dict(vmax)
FAM=[("HM",[40,41,42,43,44,45,46]),("ALM",[2,3,29,30,31,32]),("ALR",[10,11,12,14,15]),("TSM",[26,28])]
SINGLE={7:"ALMS",13:"ALMR",19:"KHYAS",20:"TH",27:"TS",36:"YS",38:"S",50:"Q",68:"N"}
MUQ=sorted(sum([f[1] for f in FAM],[])+list(SINGLE)); multi=[f[1] for f in FAM]; sizes=[len(x) for x in multi]
mus={s:s for s in range(1,115)}
famidx={}
for i,(nm,ss) in enumerate(FAM):
    for s in ss: famidx[s]=i
def within_mean(pos,fams):
    tot=0;n=0
    for ss in fams:
        ps=[pos[s] for s in ss if s in pos]
        for i in range(len(ps)):
            for j in range(i+1,len(ps)): tot+=abs(ps[i]-ps[j]); n+=1
    return tot/n if n else 0
def lpnull(pos,seed,nd=6000):
    rng=np.random.default_rng(seed); out=[]; base=list(MUQ)
    for _ in range(nd):
        rng.shuffle(base); idx=0; f=[]
        for k in sizes: f.append(base[idx:idx+k]); idx+=k
        out.append(within_mean(pos,f))
    return np.array(out)
profs={s:Counter(roots.get(s,[])) for s in MUQ}
def cos(a,b):
    import math; keys=set(a)|set(b); dot=sum(a[k]*b[k] for k in keys)
    na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0
obs_mus=within_mean(mus,multi); obs_nuz=within_mean(nuz,multi)
null_mus=lpnull(mus,1); null_nuz=lpnull(nuz,2)
muq_len=[verses[s] for s in MUQ]; non_len=[verses[s] for s in verses if s not in MUQ]

def hist_cols(arr,nbins=11):
    c,edges=np.histogram(arr,bins=nbins)
    cats=[f"{(edges[i]+edges[i+1])/2:.0f}" for i in range(len(c))]
    return cats,[int(x) for x in c]

# convenience wrappers ------------------------------------------------------
def bar(prs,ttl,ctitle,cats,vals,insight,ylab="",fmt="0",seriesname="value",ymax=None,ymin=None,fill=TINT,datalabels=True):
    dc.chart_slide(prs,ttl,"col",ctitle,cats,[(seriesname,vals)],insight,ylab=ylab,fmt=fmt,ymax=ymax,ymin=ymin,fill=fill,datalabels=datalabels,legend=False)
def gbar(prs,ttl,ctitle,cats,series,insight,ylab="",fmt="0",fill=TINT2):
    dc.chart_slide(prs,ttl,"col",ctitle,cats,series,insight,ylab=ylab,fmt=fmt,fill=fill,datalabels=True,legend=True)
def line(prs,ttl,ctitle,cats,series,insight,ylab="",fmt="0",fill=TINT,legend=None):
    dc.chart_slide(prs,ttl,"line",ctitle,cats,series,insight,ylab=ylab,fmt=fmt,fill=fill,datalabels=False,legend=legend)
def pie(prs,ttl,ctitle,cats,vals,insight,fill=TINT,pct=True):
    dc.chart_slide(prs,ttl,"pie",ctitle,cats,[("",vals)],insight,fmt=("pct" if pct else "0"),fill=fill)
def sc(prs,ttl,ctitle,series,insight,xlab="",ylab="",fill=TINT2,legend=True):
    dc.scatter_slide(prs,ttl,ctitle,series,insight,xlab=xlab,ylab=ylab,fill=fill,legend=legend)
def nullbar(prs,ttl,ctitle,arr,insight,fill=TINT):
    cats,counts=hist_cols(arr); bar(prs,ttl,ctitle,cats,counts,insight,ylab="count",seriesname="null",fill=fill,datalabels=False)
def famstrip(prs,ttl,ctitle,insight,order="mus",fill=TINT2):
    series=[]
    for i,(nm,ss) in enumerate(FAM):
        pts=[(mus[s] if order=="mus" else nuz[s], i+1) for s in ss]
        series.append((nm,pts))
    dc.scatter_slide(prs,ttl,ctitle,series,insight,xlab=("sūra number" if order=="mus" else "revelation order"),ylab="family",fill=fill,legend=True)

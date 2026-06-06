# -*- coding: utf-8 -*-
import importlib.util, os, numpy as np
import matplotlib.pyplot as plt
spec=importlib.util.spec_from_file_location("F","/tmp/figcommon.py"); F=importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
ar,surA,norm,NAVY,TEAL,RED,AMBER,GREY,PAL=F.ar,F.surA,F.norm,F.NAVY,F.TEAL,F.RED,F.AMBER,F.GREY,F.PAL
sa,stok,rsd,rst,form=F.load()
W2='week02'; W3='week03/shots'; SH='week02/shots'
def lorenz(v):
    xs=np.sort(np.array(v,float)); n=len(xs); cum=np.cumsum(xs)/xs.sum(); return np.arange(0,n+1)/n, np.concatenate([[0],cum])
def gini(full):
    xs=sorted(full); n=len(xs); tot=sum(xs); cum=sum(i*x for i,x in enumerate(xs,1)); return (2*cum)/(n*tot)-(n+1)/n
fig,axx=plt.subplots(figsize=(6.6,5.2))
axx.plot([0,1],[0,1],'--',color=GREY,label='perfectly even')
for rt,col in [('رشد',RED),('كفر',TEAL)]:
    full=[rsd[norm(rt)].get(s,0) for s in range(1,115)]; x,y=lorenz(full); ns=sum(1 for v in full if v>0)
    axx.plot(x,y,color=col,lw=2.4,label=f'{ar(rt)}  (Gini {gini(full):.2f} · {ns} surahs)')
axx.set_xlabel('cumulative share of the 114 surahs'); axx.set_ylabel("cumulative share of occurrences")
axx.set_title('Concentration (Lorenz)',fontsize=12,weight='bold',color=NAVY); axx.legend(fontsize=11,loc='upper left')
fig.tight_layout(); fig.savefig(f'{W2}/fig_concentration.png',dpi=150); plt.close(fig)

d=rsd[norm('ظلم')]; t=rst[norm('ظلم')]
raw=sorted(d.items(),key=lambda kv:-kv[1])[:6]; pr=sorted(((s,t[s]/stok[s]*1000) for s in t if t[s]>=3 and stok[s]>=30),key=lambda x:-x[1])[:6]
fig,(a1,a2)=plt.subplots(1,2,figsize=(11.5,4.4))
rr=raw[::-1]; c=[NAVY]*len(rr); c[-1]=RED
a1.barh([surA(s) for s,_ in rr],[v for _,v in rr],color=c); a1.invert_yaxis()
a1.set_title('Raw busiest surah (ayah-hits)',fontsize=11,weight='bold'); a1.set_xlabel('ayahs with the root')
for i,(s,v) in enumerate(rr): a1.text(v+0.4,i,str(v),va='center',fontsize=9)
pp=pr[::-1]; c2=[NAVY]*len(pp); c2[-1]=TEAL
a2.barh([surA(s) for s,_ in pp],[p for _,p in pp],color=c2); a2.invert_yaxis()
a2.set_title('Size-true home (per 1,000 root-tokens)',fontsize=11,weight='bold'); a2.set_xlabel('per 1,000 root-tokens')
for i,(s,p) in enumerate(pp): a2.text(p+0.2,i,f'{p:.1f}',va='center',fontsize=9)
fig.suptitle('Raw count crowns al-Baqara (the longest surah); size-true, the home is Ibrahim',fontsize=12.5,weight='bold',color=NAVY)
fig.tight_layout(rect=[0,0,1,0.93]); fig.savefig(f'{W2}/fig_home_flip.png',dpi=150); plt.close(fig)

d=rsd[norm('صبر')]; t=rst[norm('صبر')]
raw=sorted(d.items(),key=lambda kv:-kv[1])[:4]; pa=sorted(((s,d[s]/sa[s]*1000) for s in d if d[s]>=3 and sa[s]>=10),key=lambda x:-x[1])[:4]; pr=sorted(((s,t[s]/stok[s]*1000) for s in t if t[s]>=3 and stok[s]>=30),key=lambda x:-x[1])[:4]
fig,axes=plt.subplots(1,3,figsize=(13,4.3))
def panel(ax,data,wc,title,xl,fmt):
    dd=data[::-1]; cols=[NAVY]*len(dd); cols[-1]=wc
    ax.barh([surA(s) for s,_ in dd],[v for _,v in dd],color=cols); ax.invert_yaxis()
    ax.set_title(title,fontsize=10.5,weight='bold'); ax.set_xlabel(xl,fontsize=9)
    for i,(s,v) in enumerate(dd): ax.text(v*1.01,i,fmt(v),va='center',fontsize=8.5)
panel(axes[0],raw,RED,'1. Raw (ayah-hits)','ayahs',lambda v:f'{int(v)}')
panel(axes[1],pa,AMBER,'2. per AYAH','per 1k ayahs',lambda v:f'{int(round(v))}')
panel(axes[2],pr,TEAL,'3. per ROOT-TOKENS (size-true)','per 1k root-tokens',lambda v:f'{v:.1f}')
fig.suptitle('sabr: the home changes at every level — only per root-tokens is size-true',fontsize=12,weight='bold',color=NAVY)
fig.text(0.5,0.005,'Ayahs vary in length, so per-ayah is still confounded; only per ROOT-TOKENS is size-true.',ha='center',fontsize=9,color=GREY)
fig.tight_layout(rect=[0,0.05,1,0.93]); fig.savefig(f'{W2}/fig_normalization_levels.png',dpi=150); plt.close(fig)

t=rst[norm('عسر')]; items=sorted(((s,t[s],t[s]/stok[s]*1000,stok[s]) for s in t),key=lambda x:-x[2])
fig,ax=plt.subplots(figsize=(8.2,4.4))
labels=[surA(s)+f'  ({c}/{sz})' for s,c,p,sz in items]
cols=[(TEAL if (c>=3 and sz>=30) else RED) for s,c,p,sz in items]
ax.barh(labels[::-1],[p for s,c,p,sz in items][::-1],color=cols[::-1]); ax.invert_yaxis()
ax.set_xlabel('per 1,000 root-tokens of the surah')
ax.set_title('“Homes” are tiny-surah artifacts — all fail the support floor',fontsize=11.5,weight='bold',color=NAVY)
fig.text(0.5,0.005,'Red = fails floor (count < 3 or surah < 30 root-tokens) → no reliable home surah.',ha='center',fontsize=8.5,color=RED)
fig.tight_layout(rect=[0,0.05,1,1]); fig.savefig(f'{W2}/fig_support_floor.png',dpi=150); plt.close(fig)

d=rsd[norm('ظلم')]; counts=[d.get(s,0) for s in range(1,115)]
fig,ax=plt.subplots(figsize=(11,3.7))
ax.bar(range(1,115),counts,color=[RED if s==2 else NAVY for s in range(1,115)],width=0.85)
ax.set_xlabel('surah number (1–114)'); ax.set_ylabel('ayahs with the root')
ax.set_title('Ayah hits per surah — zulm  (290 ayahs / 59 surahs)',fontsize=12,weight='bold',color=NAVY)
ax.annotate(ar('البقرة')+' = 27\n(tallest only because it is the longest surah)',xy=(2,27),xytext=(14,24),fontsize=9,color=RED,arrowprops=dict(arrowstyle='->',color=RED))
ax.set_xlim(0,115); fig.tight_layout(); fig.savefig(f'{SH}/zulm_ayah_hits_per_surah.png',dpi=150); plt.close(fig)

fig,ax=plt.subplots(figsize=(7.2,3.4)); ax.axis('off')
ax.add_patch(plt.Rectangle((0,0),1,1,transform=ax.transAxes,fill=False,ec=NAVY,lw=1.5))
ax.text(0.5,0.92,'Per-Root Profile — '+ar('ظلم'),ha='center',va='top',fontsize=14,weight='bold',color=NAVY,transform=ax.transAxes)
rows=[('Ayah frequency','290 ayahs'),('Breadth','59 of 114 surahs'),('Percentile','98.6th (ubiquitous)'),('Concentration','top-3 21.7% · Gini 0.74'),('Raw busiest surah',ar('البقرة')+' (length artifact)'),('Size-true home',ar('إبراهيم')+' — 15.8 / 1,000 root-tokens')]
y=0.74
for k,v in rows:
    ax.text(0.06,y,k,ha='left',va='center',fontsize=10.5,color=GREY,transform=ax.transAxes)
    ax.text(0.58,y,v,ha='left',va='center',fontsize=10.5,weight='bold',color=NAVY,transform=ax.transAxes); y-=0.12
fig.tight_layout(); fig.savefig(f'{SH}/zulm_profile_card.png',dpi=150); plt.close(fig)

def donut(root,title,path,topn=6):
    fc=form[norm(root)]; tot=sum(fc.values()); top=fc.most_common(topn); other=tot-sum(c for _,c in top)
    labs=[f'{ar(f)}  {c/tot*100:.1f}%' for f,c in top]; sizes=[c for _,c in top]
    if other>0: labs.append(ar('أخرى')+f'  {other/tot*100:.1f}%'); sizes.append(other)
    fig,ax=plt.subplots(figsize=(7.0,5.0))
    ax.pie(sizes,labels=labs,startangle=90,counterclock=False,colors=[PAL[i%len(PAL)] for i in range(len(sizes))],wedgeprops=dict(width=0.42,edgecolor='white'),textprops=dict(fontsize=11))
    ax.set_title(title,fontsize=12.5,weight='bold',color=NAVY); fig.tight_layout(); fig.savefig(path,dpi=150); plt.close(fig)
donut('ظلم','Surface forms of '+ar('ظلم')+'  (17 forms · 315 tokens)',f'{W3}/forms_zulm.png')
donut('عدل','Surface forms of '+ar('عدل')+'  (only 6 forms)',f'{W3}/forms_adl.png')
parts=[('قسط',48.3),('قرب',9.7),('شهد',8.6),('ذوي',7.8),('وحد',6.0),('ءمر',4.7),('وقي',4.5),('ءخر',3.7)]
fig,ax=plt.subplots(figsize=(7.6,4.3)); pr=parts[::-1]; cols=[NAVY]*len(pr); cols[-1]=TEAL
ax.barh([ar(p[0]) for p in pr],[p[1] for p in pr],color=cols)
for i,(n,v) in enumerate(pr): ax.text(v+0.6,i,f'{v:.1f}×',va='center',fontsize=9)
ax.set_xlabel('length-controlled lift (× expected)')
ax.set_title('Significant partners of adl — qist (equity) leads',fontsize=12,weight='bold',color=NAVY)
ax.grid(axis='x',alpha=0.25)
fig.text(0.5,0.005,'List is frequency/length-controlled (mechanism = Weeks 4–5).',ha='center',fontsize=8.5,color=GREY)
fig.tight_layout(rect=[0,0.05,1,1]); fig.savefig(f'{W3}/partners_adl.png',dpi=150); plt.close(fig)
print('regenerated all figures with full surah names')

# -*- coding: utf-8 -*-
# Week 3 figures — run from anywhere; reads ../wk3_keys.json, writes ../figs/.
# Standard: English-only titles; Arabic only as isolated, shaped axis/data labels.
import importlib.util, json, os
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
HERE=os.path.dirname(os.path.abspath(__file__)); BASE=os.path.dirname(HERE)
spec=importlib.util.spec_from_file_location("F",os.path.join(HERE,"figcommon.py")); F=importlib.util.module_from_spec(spec); spec.loader.exec_module(F)
ar,NAVY,TEAL,RED,AMBER,GREY,PAL=F.ar,F.NAVY,F.TEAL,F.RED,F.AMBER,F.GREY,F.PAL
GREEN='#2C7A3F'
K=json.load(open(os.path.join(BASE,'wk3_keys.json'))); FD=os.path.join(BASE,'figs'); os.makedirs(FD,exist_ok=True)

fig,ax=plt.subplots(figsize=(9,5)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax.text(5,9.3,'One root + many patterns → many words',ha='center',fontsize=14,weight='bold',color=NAVY)
ax.add_patch(plt.Circle((5,5),1.05,color=NAVY)); ax.text(5,5,ar('ك ت ب'),ha='center',va='center',fontsize=22,color='white',weight='bold')
ax.text(5,3.65,'root: write',ha='center',fontsize=10,color=GREY)
for word,gl,x,y in [(ar('كاتب'),'writer (doer)',8.4,8),(ar('مكتوب'),'written (done-to)',9.2,5),(ar('كِتاب'),'a book',8.4,2),(ar('يكتب'),'he writes',1.6,2),(ar('كُتِب'),'was decreed',0.8,5),(ar('كتّاب'),'scribes',1.6,8)]:
    ax.annotate('',xy=(x,y),xytext=(5,5),arrowprops=dict(arrowstyle='-',color=TEAL,lw=1.4,alpha=0.6))
    ax.text(x,y+0.28,word,ha='center',fontsize=15,color=NAVY,weight='bold'); ax.text(x,y-0.32,gl,ha='center',fontsize=8.5,color=GREY)
fig.tight_layout(); fig.savefig(f'{FD}/fig_root_pattern.png',dpi=150); plt.close(fig)

amn=K['forms']['ءمن']; tot=sum(c for _,c in amn); top=amn[:6]; other=tot-sum(c for _,c in top)
labs=[f'{ar(f)}  {c/tot*100:.0f}%' for f,c in top]+[ar('أخرى')+f'  {other/tot*100:.0f}%']; sizes=[c for _,c in top]+[other]
fig,ax=plt.subplots(figsize=(7,5)); ax.pie(sizes,labels=labs,startangle=90,counterclock=False,colors=[PAL[i%len(PAL)] for i in range(len(sizes))],wedgeprops=dict(width=0.42,edgecolor='white'),textprops=dict(fontsize=11))
ax.set_title('Surface forms of the worked root (27 forms, 879 tokens)',fontsize=12,weight='bold',color=NAVY)
fig.tight_layout(); fig.savefig(f'{FD}/fig_amn_forms.png',dpi=150); plt.close(fig)

fam=K['amn_families']; order=['verb (the act)','participle (believers)','masdar (faith-noun)','security / trust']
arn={'verb (the act)':'الفعل','participle (believers)':'اسم الفاعل','masdar (faith-noun)':'المصدر','security / trust':'الأمن'}
vals=[fam[k][1] for k in order]; cols=[TEAL,NAVY,AMBER,RED]; ypos=list(range(4))[::-1]
fig,ax=plt.subplots(figsize=(8.6,4.5)); ax.barh(ypos,vals,color=cols)
ax.set_yticks(ypos); ax.set_yticklabels([ar(arn[k])+'  ·  '+k for k in order],fontsize=10.5)
for y,v in zip(ypos,vals): ax.text(v+0.7,y,f'{v:.0f}%',va='center',fontsize=11,weight='bold',color=NAVY)
ax.set_xlabel('share of the root’s tokens (%)'); ax.set_xlim(0,72)
ax.set_title('By pattern family: faith is overwhelmingly a VERB (an act)',fontsize=12,weight='bold',color=NAVY)
for sp in ('top','right'): ax.spines[sp].set_visible(False)
ax.grid(axis='x',alpha=0.25); fig.tight_layout(); fig.savefig(f'{FD}/fig_amn_patterns.png',dpi=150); plt.close(fig)

div=sorted(K['divine'],key=lambda x:-x[1]); attr={'رحيم':'the All-Merciful','حكيم':'the All-Wise','غفور':'the Oft-Forgiving','رحمن':'the Most Gracious','سميع':'the All-Hearing','بصير':'the All-Seeing'}
names=[d[0] for d in div]; counts=[d[1] for d in div]; ypos=list(range(len(div)))[::-1]
fig,ax=plt.subplots(figsize=(8.4,4.5)); ax.barh(ypos,counts,color=NAVY)
ax.set_yticks(ypos); ax.set_yticklabels([ar(n)+'   '+attr[n] for n in names],fontsize=11)
for y,c in zip(ypos,counts): ax.text(c+1.0,y,str(c),va='center',fontsize=10,weight='bold',color=NAVY)
ax.set_xlabel('occurrences'); ax.set_xlim(0,108); ax.set_title('Divine Names are intensive forms of these roots',fontsize=12,weight='bold',color=NAVY)
for sp in ('top','right'): ax.spines[sp].set_visible(False)
ax.grid(axis='x',alpha=0.25); fig.tight_layout(); fig.savefig(f'{FD}/fig_divine_names.png',dpi=150); plt.close(fig)

fig,ax=plt.subplots(figsize=(10,6.0)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax.text(5,9.55,'One root, divergent meanings — and even opposite moral valence',ha='center',fontsize=13.5,weight='bold',color=NAVY)
def rowf(root,y,left,right,lcol,rcol,tag=None):
    ax.add_patch(Ellipse((5,y),1.6,1.15,color=NAVY)); ax.text(5,y,ar(root),ha='center',va='center',fontsize=19,color='white',weight='bold')
    ax.annotate('',xy=(2.7,y),xytext=(4.15,y),arrowprops=dict(arrowstyle='->',color=lcol,lw=1.8)); ax.annotate('',xy=(7.3,y),xytext=(5.85,y),arrowprops=dict(arrowstyle='->',color=rcol,lw=1.8))
    ax.text(2.45,y+0.27,left[0],ha='right',fontsize=15,color=lcol,weight='bold'); ax.text(2.45,y-0.37,left[1],ha='right',fontsize=8.6,color=GREY)
    ax.text(7.55,y+0.27,right[0],ha='left',fontsize=15,color=rcol,weight='bold'); ax.text(7.55,y-0.37,right[1],ha='left',fontsize=8.6,color=GREY)
    if tag: ax.text(5,y-0.95,tag,ha='center',fontsize=8.5,style='italic',color=GREY)
rowf('كثر',7.7,(ar('كوثر'),'blessed abundance (108:1)'),(ar('تكاثر'),'rivalry in piling up (102:1)'),GREEN,RED,'opposite moral valence — praise vs blame')
rowf('ءمن',4.6,(ar('إيمان'),'faith / belief'),(ar('أمن'),'security / safety'),TEAL,RED,'two senses')
rowf('كتب',1.5,(ar('كِتاب'),'a book'),(ar('كُتِب'),'was decreed'),TEAL,RED,'two senses')
fig.tight_layout(); fig.savefig(f'{FD}/fig_polysemy.png',dpi=150); plt.close(fig)

nf=K['nforms']; items=sorted(nf.items(),key=lambda x:x[1])
fig,ax=plt.subplots(figsize=(8,4.6)); ax.barh([ar(r) for r,_ in items],[v for _,v in items],color=[TEAL if r=='ءمن' else NAVY for r,_ in items])
for i,(r,v) in enumerate(items): ax.text(v+0.2,i,str(v),va='center',fontsize=9)
ax.set_xlabel('number of distinct surface forms'); ax.set_title('Morphological richness varies by root',fontsize=12,weight='bold',color=NAVY)
fig.tight_layout(); fig.savefig(f'{FD}/fig_form_richness.png',dpi=150); plt.close(fig)

P=[p for p in K['partners_amn'] if p[0]!='ءله']
fig,ax=plt.subplots(figsize=(7.6,4.2)); pr=P[::-1]; cols=[NAVY]*len(pr); cols[-1]=TEAL
ax.barh([ar(p[0]) for p in pr],[p[3] for p in pr],color=cols)
for i,p in enumerate(pr): ax.text(p[3]+0.2,i,f'z={p[3]}',va='center',fontsize=9)
ax.set_xlabel('length-controlled significance (z)'); ax.set_title('Partners of the worked root: faith travels with works',fontsize=12,weight='bold',color=NAVY)
fig.text(0.5,0.005,'Frequency/length-controlled (mechanism = Weeks 4–5).',ha='center',fontsize=8.5,color=GREY)
fig.tight_layout(rect=[0,0.05,1,1]); fig.savefig(f'{FD}/fig_amn_partners.png',dpi=150); plt.close(fig)

ant=K['antonyms']
fig,ax=plt.subplots(figsize=(7.4,3.8)); ax.barh(list(range(len(ant)))[::-1],[j for a,b,j in ant],color=RED)
ax.set_yticks(list(range(len(ant)))[::-1]); ax.set_yticklabels([ar(a)+'  ↔  '+ar(b) for a,b,j in ant],fontsize=13)
for i,(a,b,j) in enumerate(ant): ax.text(j+1,len(ant)-1-i,str(j),va='center',fontsize=10)
ax.set_xlabel('ayahs where both roots co-occur'); ax.set_title('Antonyms are partners too — opposites defined together',fontsize=12,weight='bold',color=NAVY)
fig.tight_layout(); fig.savefig(f'{FD}/fig_antonym_partners.png',dpi=150); plt.close(fig)
print('Week 3 figures regenerated ->',FD)

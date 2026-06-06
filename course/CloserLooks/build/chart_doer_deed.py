# -*- coding: utf-8 -*-
"""Two-column 'doer + deed' chart for synthesis #10: inner (actor) vs outer (act) registers,
both substantial; deeds rest on an inner source. English title; Arabic only as isolated labels."""
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import matplotlib.font_manager as fm, numpy as np
import arabic_reshaper; from bidi.algorithm import get_display
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":19})
def ar(s): return get_display(arabic_reshaper.reshape(s))
NAVY="#1E2761"; TEAL="#0E9D8C"; RED="#A23B3B"; GREY="#9aa0a6"; AMBER="#B8860B"
FIG="/sessions/kind-compassionate-feynman/mnt/RootCourse/CloserLooks/figs"

inner=[("علم",728,"knowledge"),("نفس",270,"self"),("ذكر",264,"remembrance"),
       ("تقوى",237,"God-consciousness"),("حسن",177,"excellence"),("قلب",155,"heart"),
       ("نظر",115,"considered look"),("خلص",30,"sincerity")]
outer=[("عمل",313,"righteous deeds"),("صلو",90,"prayer"),("صبر",93,"patience"),
       ("نفق",86,"spending"),("زكو",56,"charity-purify")]

fig,axs=plt.subplots(1,2,figsize=(13.6,5.9),gridspec_kw={"width_ratios":[8,5]})
fig.suptitle("Goodness of the DOER and goodness of the DEED — both weighted; the act rests on an inner source",
             fontsize=20,weight="bold",color=NAVY,y=1.01)
def col(ax,data,c,head):
    cats=[ar(a)+"  "+g for a,v,g in data]; vals=[v for a,v,g in data]
    y=list(range(len(vals)))[::-1]
    ax.barh(y,vals,color=c,height=0.66)
    for yi,v in zip(y,vals): ax.text(v,yi,"  "+str(v),va="center",fontsize=19,weight="bold",color=NAVY)
    ax.set_yticks(y); ax.set_yticklabels(cats,fontsize=18)
    ax.set_xlim(0,max(vals)*1.18); ax.set_title(head,fontsize=19,weight="bold",color=c,pad=10)
    ax.set_xlabel("verses present (doc-freq, Book6)",fontsize=15)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
col(axs[0],inner,TEAL,"The inner register — the DOER")
col(axs[1],outer,NAVY,"The outer register — the DEED")
fig.tight_layout(rect=[0,0,1,0.95])
fig.savefig(FIG+"/cl10b_doer_deed.png",dpi=150,bbox_inches="tight"); print("saved cl10b_doer_deed.png")

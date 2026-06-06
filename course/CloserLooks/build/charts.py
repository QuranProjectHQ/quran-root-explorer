# -*- coding: utf-8 -*-
import os
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import arabic_reshaper; from bidi.algorithm import get_display
fm.fontManager.addfont("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":17})
def ar(s): return get_display(arabic_reshaper.reshape(s))
NAVY="#1E2761"; TEAL="#0E9D8C"; RED="#A23B3B"; GREY="#9aa0a6"; AMBER="#B8860B"
FIG="/sessions/kind-compassionate-feynman/mnt/RootCourse/CloserLooks/figs"
def save(fig,n): fig.savefig(os.path.join(FIG,n),dpi=150,bbox_inches="tight"); plt.close(fig); print("saved",n)
def vbar(name,cats,vals,cols,title,ylab,fmt="{:.0f}",ymaxf=1.18):
    fig,ax=plt.subplots(figsize=(11.5,5.0))
    ax.bar(range(len(vals)),vals,color=cols)
    for i,v in enumerate(vals): ax.text(i,v,fmt.format(v),ha="center",va="bottom",fontsize=18,weight="bold",color=NAVY)
    ax.set_xticks(range(len(cats))); ax.set_xticklabels(cats,fontsize=16)
    ax.set_ylabel(ylab,fontsize=16); ax.set_ylim(0,max(vals)*ymaxf)
    ax.set_title(title,fontsize=18,weight="bold",color=NAVY,pad=12)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    save(fig,name)
def hbar(name,cats,vals,cols,title,xlab,fmt="{:.1f}×",line=None):
    fig,ax=plt.subplots(figsize=(11.8,5.2)); y=range(len(vals))[::-1]
    ax.barh(list(y),vals,color=cols,height=0.62)
    for yi,v in zip(y,vals): ax.text(v,yi,"  "+fmt.format(v),va="center",fontsize=17,weight="bold",color=NAVY)
    ax.set_yticks(list(y)); ax.set_yticklabels(cats,fontsize=16)
    if line is not None: ax.axvline(line,color=GREY,ls="--",lw=1.5)
    ax.set_xlabel(xlab,fontsize=16); ax.set_xlim(0,max(vals)*1.2)
    ax.set_title(title,fontsize=18,weight="bold",color=NAVY,pad=12)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    save(fig,name)

# #3 God's names: mercy vs wrath vs punishment-theme
vbar("cl3_names.png",
 [ar("الرحمن، الغفور، الودود…")+"\nmercy NAMES", ar("المنتقم، الجبّار، القهّار")+"\nwrath NAMES", ar("عذاب")+"\npunishment (theme)"],
 [661,36,336],[TEAL,RED,GREY],
 "God’s NAMES skew to mercy (~18×) — but punishment is a frequent THEME","occurrences (Book6)")
# #4 al-Asr quartet: only faith+deeds recurs
hbar("cl4_asr.png",
 [ar("ءمن + عمل")+"  faith + deeds", ar("ءمن + حقق")+"  faith + truth", ar("عمل + صبر")+"  deeds + patience",
  ar("ءمن + صبر")+"  faith + patience", ar("ءنس + خسر")+"  human + loss"],
 [2.8,1.8,1.3,1.2,1.3],[TEAL,GREY,GREY,GREY,GREY],
 "Only faith + deeds recurs (101 verses); the al-ʿAsr fourfold does not","co-occurrence lift (× over chance)",line=3,fmt="{:.1f}×")
# #5 patience & prayer real
vbar("cl5_sabr_salat.png",
 [ar("صبر + صلو")+"\npatience + prayer", "chance\nbaseline"],
 [5.2,1.0],[TEAL,GREY],
 "Patience & prayer: a real bond — 5.2× over chance (7 verses)","co-occurrence lift (×)",fmt="{:.1f}×")
# #6 direction guidance/path
vbar("cl6_direction.png",
 ["P(guidance | path)\n"+ar("هدي | صرط"), "P(path | guidance)\n"+ar("صرط | هدي")],
 [53,9],[TEAL,RED],
 "Direction: the “path” is a path OF guidance — not the reverse","% of the other’s verses",fmt="{:.0f}%")
# #7 faith-deeds-reward motif
hbar("cl7_motif.png",
 [ar("ءمن · عمل · صلح")+"  faith·deeds·righteous", ar("ءمن · صلح · جنن")+"  faith·righteous·garden", ar("ءمن · عمل · جنن")+"  faith·deeds·garden"],
 [24.4,12.8,7.3],[TEAL,TEAL,TEAL],
 "The signature moral motif: faith + deeds + reward (70 verses for the core)","adjusted lift (× over a length-aware null)",line=10,fmt="{:.1f}×")
# #8 robust vs fragile
vbar("cl8_support.png",
 [ar("توب·غفر·رحم")+"\nrobust — 18 verses", ar("خشع·دعو·رغب")+"\nfragile — 1 verse (21:90)"],
 [55.4,575.9],[TEAL,RED],
 "A 576× motif on ONE verse is worthless; 55× on 18 verses is trustworthy","adjusted lift (×)  —  read with the verse-count!",fmt="{:.0f}×")
# #9 audit man/woman
vbar("cl9_audit.png",
 ["claimed\n“24 = 24”", ar("رجل")+"\nman (root)", ar("نسو")+"\nwoman (root)", ar("مرء")+"\nperson (root)"],
 [24,66,53,37],[GREY,TEAL,RED,AMBER],
 "“Man & woman, 24 each” is a cherry-picked form: roots give 66 vs 53","occurrences (Book6)")
print("ALL CL CHARTS DONE")

# ===== SERIES FRAME — ash-Shams 91:7-10 dichotomies =====
import numpy as np
def shams():
    fig,ax=plt.subplots(figsize=(12.2,5.6))
    pairs=[("تقوى\nvirtue",237,"فجور\nvice",21,"virtue / vice"),
           ("زكو\npurify",56,"دسس\ncorrupt",1,"purify / corrupt"),
           ("فلح\nsuccess",40,"خيب\nfailure",5,"success / failure")]
    x=np.arange(3); w=0.36
    pv=[p[1] for p in pairs]; nv=[p[3] for p in pairs]
    ax.bar(x-w/2,pv,w,color=TEAL,label="the soul’s POSITIVE pole")
    ax.bar(x+w/2,nv,w,color=RED,label="its opposite")
    for i in range(3):
        ax.text(x[i]-w/2,pv[i],f"{ar(pairs[i][0].split(chr(10))[0])}  {pv[i]}",ha="center",va="bottom",fontsize=15,weight="bold",color=TEAL)
        ax.text(x[i]+w/2,nv[i],f"{ar(pairs[i][2].split(chr(10))[0])}  {nv[i]}",ha="center",va="bottom",fontsize=15,weight="bold",color=RED)
    ax.set_xticks(x); ax.set_xticklabels([p[4] for p in pairs],fontsize=17,weight="bold")
    ax.set_ylabel("occurrences (Book6)",fontsize=16); ax.set_ylim(0,270)
    ax.legend(fontsize=14,loc="upper right")
    ax.set_title("Ash-Shams 91:7–10: the Qur’an names the soul’s virtue, purity & success far more than their opposites",fontsize=15.5,weight="bold",color=NAVY,pad=12)
    for sp in ["top","right"]: ax.spines[sp].set_visible(False)
    save(fig,"frame_shams.png")
shams()
print("FRAME CHART DONE")

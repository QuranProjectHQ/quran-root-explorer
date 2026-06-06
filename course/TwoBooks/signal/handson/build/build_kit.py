# -*- coding: utf-8 -*-
import importlib.util, os, json, sys, numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import arabic_reshaper; from bidi.algorithm import get_display
def ar(s): return get_display(arabic_reshaper.reshape(s))
plt.rcParams["font.family"]="DejaVu Sans"
spec=importlib.util.spec_from_file_location("c",os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
GREY=RGBColor(0x55,0x55,0x55)
sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2"); import analysis as A, twobooks_stats as T
corp=A.load_corpus("/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2/Book6.xlsx"); N=len(corp.df)
ROOTS=[("ظلم","zulm"),("نفس","nafs"),("هدي","huda"),("ضلل","dalal"),("رزق","rizq"),("صبر","sabr"),
       ("شكر","shukr"),("صرط","sirat"),("يسر","yusr"),("عدل","adl"),("قسط","qist"),("رشد","rushd")]
def disp(rt,nd=5000,seed=5):
    idx=sorted(corp.index_norm.get(A.normalize_letters(rt),[]))
    if len(idx)<3: return None
    gaps=np.diff(idx); fano=float(gaps.var()/gaps.mean()) if gaps.mean() else 0.0
    rng=np.random.default_rng(seed); out=np.empty(nd)
    for j in range(nd):
        pk=np.sort(rng.choice(N,size=len(idx),replace=False)); g=np.diff(pk)
        out[j]=g.var()/g.mean() if g.mean() else 0.0
    p=float((np.sum(out>=fano)+1)/(nd+1))
    verdict=("bursty/clustered" if fano>1.2 else "regular/even" if fano<0.8 else "~Poisson")
    return dict(root=rt,n=len(idx),mean_gap=round(float(gaps.mean()),1),fano=round(fano,2),p=round(p,4),
                verdict=verdict, first5=idx[:5])
bank=[dict(translit=tr, **disp(rt)) for rt,tr in ROOTS]
json.dump(bank,open(os.path.join(WK,"signal_data_bank.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

# FIGURE — Fano factor across the 12 roots
fig,axx=plt.subplots(figsize=(9,3.4))
cols=["#E63946" if b["fano"]>1.2 else "#2A9D8F" if b["fano"]<0.8 else "#9CA3AF" for b in bank]
axx.bar(range(len(bank)),[b["fano"] for b in bank],color=cols,width=0.8)
axx.axhline(1.0,color="#1D3557",ls="--",lw=1.2); axx.text(len(bank)-1,1.03,"Poisson (Fano=1)",ha="right",fontsize=9,color="#1D3557")
axx.set_xticks(range(len(bank))); axx.set_xticklabels([ar(b["root"]) for b in bank],fontsize=12)
axx.set_title("Burstiness of 12 roots — Fano factor of inter-occurrence gaps (computed from Book6)",fontsize=11)
axx.set_ylabel("Fano factor (>1 = bursty)",fontsize=10)
fig.tight_layout(); fig.savefig(os.path.join(WK,"figs","fig_fano.png"),dpi=150); plt.close(fig)

def figdoc(d,path,cap,w=6.4):
    if os.path.exists(path):
        d.add_picture(path,width=Inches(w)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)
ex=[b for b in bank if b["translit"]=="zulm"][0]  # walkthrough root

# GUIDE
d=new_doc("Signal — App & Test Guide")
TITLE(d,"Signal — Using the App & Reading the Tests",
      "A live walkthrough on one root (ẓulm), theme: does a root CLUSTER in bursts or spread evenly "
      "through the text? Numbers computed from Book6 by the app's engine. Honest rule: trust the Fano factor and its permutation p, not the eye.")
H(d,"Part A — Walkthrough: ẓulm, the dispersion way")
H(d,"1.  Open the recurrence tool",size=12)
bullet(d,[("App → Two Books → Signal → ",False),("🔁 Root recurrence",True),(". Pick your root from the list.",False)])
H(d,"2.  Read the dispersion metrics",size=12)
P(d,[("The app marks every āyah where the root occurs as a 1, else 0, and measures the gaps between hits. "
      "For ẓulm: ",False),(f"{ex['n']} occurrences, mean gap {ex['mean_gap']} āyahs, Fano factor {ex['fano']}",True),
     (f". Fano > 1 means bursty (clustered); ≈ 1 means random (Poisson); < 1 means evenly spaced.",False)])
figdoc(d,os.path.join(WK,"figs","fig_fano.png"),"Fano factor of 12 roots (computed from Book6). Bars above the dashed Poisson line are bursty/clustered.")
H(d,"3.  Run the test — is the clustering beyond chance?",size=12)
P(d,[("Press the dispersion-test button. The app compares the root's Fano factor against 5,000 random "
      "placements of the same number of hits. For ẓulm: ",False),(f"p ≈ {ex['p']:.2g}",True),
     (f" → verdict: {ex['verdict']}. Most content roots cluster, because the Qur'an returns to a theme in passages.",False)])
H(d,"Part B — The key skill: Fano factor and its p-value")
P(d,"Fano factor = variance ÷ mean of the gaps between occurrences. A memoryless (Poisson) process gives Fano ≈ 1. "
    "The permutation p = the fraction of random placements whose Fano is ≥ the observed one. Small p = clustering beyond chance.")
table(d,[["ẓulm — what the app computes","value"],
         ["occurrences","%d āyahs" % ex["n"]],
         ["mean gap between occurrences","%s āyahs" % ex["mean_gap"]],
         ["Fano factor (variance ÷ mean of gaps)","%s" % ex["fano"]],
         ["dispersion p (vs 5,000 random placements)","%.2g" % ex["p"]],
         ["verdict",ex["verdict"]]])
H(d,"Part C — The cross-check rule")
bullet(d,"Report one computed fact (Fano AND its permutation p) plus one labeled interpretation.")
bullet(d,"A high Fano is not a 'miracle' — it usually means the theme recurs in clustered passages. Say what the test licenses, no more.")
d.save(os.path.join(WK,"Signal_App_and_Test_Guide.docx"))

# EXERCISE
d=new_doc("Signal — Exercise")
TITLE(d,"Signal — Exercise: Is your root bursty or evenly spread?",
      "Part 1 a hand computation, Part 2 an app investigation. Submit the night before class; use only your own row.")
H(d,"Your assignment")
rows=[["#","your root","occurrences","first 5 occurrence āyah-indices (for Part 1)"]]
for i,b in enumerate(bank,1):
    rows.append([str(i), b["root"], str(b["n"]), ", ".join(map(str,b["first5"]))])
table(d,rows)
H(d,"Part 1 — By hand: the gap pattern",size=12)
bullet(d,"From your first 5 occurrence indices, compute the 4 gaps (differences between consecutive indices).")
bullet(d,"Compute the mean of those 4 gaps. (The app uses ALL gaps; this is a taster of the same idea.)")
H(d,"Part 2 — In the app: dispersion test",size=12)
bullet(d,[("App → Two Books → Signal → ",False),("🔁 Root recurrence",True),(". Pick your root.",False)])
bullet(d,"Record the Fano factor and the mean gap (all occurrences).")
bullet(d,[("Run the dispersion test; record the permutation ",False),("p",True),
          (" and the verdict (bursty / regular / ~Poisson).",False)])
H(d,"What to submit")
bullet(d,"Part 1: your 4 gaps and their mean.")
bullet(d,"Part 2: Fano factor, mean gap, permutation p, verdict.")
d.save(os.path.join(WK,"Signal_Exercise.docx"))

# ANSWER KEY
d=new_doc("Signal — Exercise Answer Key")
TITLE(d,"Signal — Exercise Answer Key (instructor)","All values computed from Book6 (5,000 random placements per root).")
rows=[["#","root","occurrences","mean gap","Fano","disp. p","verdict"]]
for i,b in enumerate(bank,1):
    rows.append([str(i),b["root"],str(b["n"]),str(b["mean_gap"]),str(b["fano"]),f"{b['p']:.3g}",b["verdict"]])
table(d,rows)
H(d,"Teaching point")
nb=sum(1 for b in bank if b["fano"]>1.2)
P(d,[(f"{nb} of 12 roots are bursty (Fano > 1) — content words cluster because the Qur'an develops a "
      "theme across consecutive passages, then moves on. This is ordinary discourse structure, NOT a "
      "hidden code: the dispersion test measures it honestly and the interpretation stays modest.",False)])
d.save(os.path.join(WK,"Signal_Exercise_Answer_Key.docx"))
print("signal kit built; bursty roots:", nb, "/12")

# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c","/tmp/wk2common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor, Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
GREY=RGBColor(0x55,0x55,0x55)
def fig(d,path,cap,width=6.0):
    if os.path.exists(path):
        d.add_picture(path,width=Inches(width)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)
d=new_doc("Week 2 — Using the App & Reading the Distribution Plots")
TITLE(d,"Week 2 — Using the App & Reading Every Distribution Plot",
      "A live walkthrough on one root (ظلم), theme: distribution & concentration. Figures below are computed from Book6 — the same corpus the app analyzes — so your app screens will match them. Size-true rule: read density per 1,000 ROOT-TOKENS.")
H(d,"Part A — Walkthrough: ظلم, the distribution way")
H(d,"1.  Open the app and analyze the root",size=12)
bullet(d,"Go to https://quranproject-quran-root-explorer.hf.space/ , type ظلم, click Analyze.")
bullet(d,"The result banner reads “290 ayahs matched.” Open the Per-Root Profile (left sidebar).")
H(d,"2.  Per-Root Profile — the headline metrics",size=12)
P(d,"Read the profile card: ظلم is named in 290 ayahs, spans 59 of the 114 surahs (its breadth), sits at the 98.6th percentile, and its concentration is top-3 share 21.7%, Gini 0.74. Crucially, its size-true home is Ibrahim — not al-Baqara.")
fig(d,os.path.join(WK,"shots","zulm_profile_card.png"),"Per-Root Profile metrics for ظلم (computed from Book6).",width=5.4)
H(d,"3.  The per-surah distribution chart",size=12)
P(d,"The “Ayah hits per surah” chart shows one bar per surah. al-Baqara towers over the rest — but that height is mostly surah length, not density. This is the length confound in a picture.")
fig(d,os.path.join(WK,"shots","zulm_ayah_hits_per_surah.png"),"Ayah hits per surah for ظلم — al-Baqara is tallest only because it is the longest surah.",width=6.4)
P(d,[("Read it correctly:  ",True),("the raw tallest bar (al-Baqara) is NOT the home. Normalize each surah by its root-tokens. For ظلم, the size-true home is Ibrahim at 15.8 per 1,000 root-tokens; al-Baqara is only 7.8.",False)])
H(d,"4.  Concentration — top-3 share and Gini",size=12)
P(d,"Read how unevenly the bars fall. For ظلم the three busiest surahs hold 21.7% of its ayahs and the Gini is 0.74 — moderately concentrated. The Lorenz curve makes concentration visible: the harder it bows, the more pooled.")
fig(d,os.path.join(WK,"fig_concentration.png"),"Lorenz curves: رشد concentrated (Gini 0.95) vs كفر spread (Gini 0.69).",width=4.4)
H(d,"Part B — Computing the size-true home (the key skill)")
table(d,[["Surah","ظلم tokens","surah root-tokens","per 1,000 root-tokens"],
         ["al-Baqara (raw busiest)","31","3,966","7.8"],
         ["Ibrahim (size-true home)","9","568","15.8"]])
bullet(d,"Divide each surah's root-tokens of ظلم by that surah's TOTAL root-tokens, ×1,000.")
bullet(d,"Apply the support floor: count ≥ 3 AND surah ≥ 30 root-tokens. Both pass → home = Ibrahim.")
bullet(d,"Never use raw hits, and never divide by ayah-count (ayahs vary in length too).")
H(d,"Part C — The cross-check rule")
bullet(d,"Every claim must be reproducible in the app and the per-1,000-root-tokens calculation.")
bullet(d,"Report one computed fact (with its size-true normalization + floor) + one labeled interpretation.")
d.save(os.path.join(WK,"Week2_App_and_Plot_Guide.docx")); print("app guide rebuilt with embedded figures")

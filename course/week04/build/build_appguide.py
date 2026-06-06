# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c","/tmp/wk4common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
from docx.shared import RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
GREY=RGBColor(0x55,0x55,0x55)
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week04"; FD=os.path.join(WK,"figs")
def fig(d,name,cap,width=6.0):
    p=os.path.join(FD,name)
    if os.path.exists(p):
        d.add_picture(p,width=Inches(width)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)
d=new_doc("Week 4 — Using the App: Co-occurrence")
TITLE(d,"Week 4 — Using the App: Finding a Root's True Companion",
      "A walkthrough on one target (صلو). Figures are computed from Book6 — the same corpus the app analyzes — so your app screens will match them.")
H(d,"Part A — The raw co-occurrence list")
H(d,"1.  Analyze the target and open its co-occurring roots",size=12)
bullet(d,"Go to https://quranproject-quran-root-explorer.hf.space/ , type صلو, click Analyze.")
bullet(d,"Open the co-occurring roots / partners panel. Note the shared-ayah (joint) count for each candidate.")
fig(d,"fig_raw_joint.png","Raw co-occurrence with prayer — the frequent roots قوم and ءله top the list.",width=6.0)
P(d,[("Do not stop here.",True),(" The raw leaders قوم (establish) and ءله (God) lead because they are everywhere — they share ayahs with almost every root. Raw count rewards fame, not friendship.",False)])
H(d,"Part B — Control for frequency")
H(d,"2.  Compute the times-over-chance ratio",size=12)
P(d,"For each candidate: expected = freq(target) × freq(candidate) ÷ 6,236; ratio = observed ÷ expected. For prayer, God's 44 shared ayahs are only ×1.6 (expected ≈ 27), while zakat's 28 are ×34.6 (expected ≈ 0.8).")
fig(d,"fig_controlled_ratio.png","Controlled for frequency, zakat is prayer's true companion — ×34.6 over chance.",width=5.8)
fig(d,"fig_flip.png","The flip: قوم / God top the raw list; zakat tops once you control for frequency.",width=6.2)
bullet(d,[("Report the controlled winner.",True),(" For صلو it is زكو — half of all zakat ayahs sit with prayer.",False)])
bullet(d,[("Apply the support floor.",True),(" Ignore any pair with fewer than 5 shared ayahs.",False)])
H(d,"Part C — The cross-check rule")
bullet(d,"Every claim must be reproducible in the app and the Week-4 data bank.")
bullet(d,"Report one computed fact (a controlled ratio) + one labeled interpretation.")
bullet(d,"Remember the limits: this control ignores ayah length (Week 5), shows no direction (Week 6), and association is not cause.")
d.save(os.path.join(WK,"Week4_App_and_Cooccurrence_Guide.docx")); print("app guide saved")

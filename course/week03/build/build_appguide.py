# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c","/tmp/wk3common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
from docx.shared import RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
GREY=RGBColor(0x55,0x55,0x55)
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week03"; FD=os.path.join(WK,"figs")
def fig(d,name,cap,width=6.0):
    p=os.path.join(FD,name)
    if os.path.exists(p):
        d.add_picture(p,width=Inches(width)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)
d=new_doc("Week 3 — Using the App: Forms & Partners")
TITLE(d,"Week 3 — Using the App: Reading Forms & Partners",
      "A walkthrough on one root (ءمن). Figures are computed from Book6 — the same corpus the app analyzes — so your app screens will match them.")
H(d,"Part A — Surface forms")
H(d,"1.  Analyze the root and open its forms",size=12)
bullet(d,"Go to https://quranproject-quran-root-explorer.hf.space/ , type ءمن, click Analyze.")
bullet(d,"Open the Per-Root Profile and find the Surface forms view (donut or list).")
fig(d,"fig_amn_forms.png","Surface forms of ءمن — 27 forms across 879 tokens; the verb آمن dominates at 41%.",width=5.0)
H(d,"2.  Read it by pattern family",size=12)
P(d,"Don't stop at the spellings — group them by pattern. The verb forms (آمن، يؤمن) are the act; the participle (مؤمن) is the agent; the masdar (إيمان) is the abstract act; and the intensive (أمين) is an attribute. For ءمن the verb family dominates — faith is most often an act.")
fig(d,"fig_amn_patterns.png","ءمن by pattern family: 61% verb (an act), 26% participle, 5% masdar, 5% security.",width=5.6)
P(d,[("Watch for polysemy:  ",True),("the same root branches into أمن (security) and أمين (trustworthy) — a second sense living in the forms.",False)])
H(d,"Part B — Partners")
H(d,"3.  Open the co-occurring roots / partners panel",size=12)
P(d,"The partners panel lists the roots that share ayahs with your root, already frequency/length-controlled (the mechanism is Weeks 4–5). Read the top of the list.")
fig(d,"fig_amn_partners.png","Partners of ءمن (length-controlled): صلح (righteous deeds) and عمل (works) lead — faith travels with works.",width=6.0)
bullet(d,[("Record the top three partners.",True),(" For ءمن: صلح, عمل, then رسل / قلب.",False)])
bullet(d,[("Flag any ANTONYM.",True),(" ءمن co-occurs heavily with كفر (disbelief) — opposites are defined together.",False)])
H(d,"Part C — The cross-check rule")
bullet(d,"Every claim must be reproducible in the app and the Week-3 data bank.")
bullet(d,"Report one computed fact (a form share or a partner's significance) + one labeled interpretation.")
d.save(os.path.join(WK,"Week3_App_and_Forms_Guide.docx")); print("app guide saved")

# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"dlcommon.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
GREY=RGBColor(0x55,0x55,0x55)
B=json.load(open(os.path.join(WK,"dl_data_bank.json"),encoding="utf-8"))
q=B["qaf"]
def fig(d,path,cap,width=6.2):
    if os.path.exists(path):
        d.add_picture(path,width=Inches(width)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)

d=new_doc("Disjoint Letters — App & Test Guide")
TITLE(d,"Disjoint Letters — Using the App & Reading the Tests",
      "A live walkthrough on one letter (ق), theme: are the muqaṭṭaʿāt a hidden letter-code, "
      "or a positional pointer? Every number below is computed from Book6 by the app's own engine, "
      "so your app screens match. The honest rule: trust the permutation p-value, not the eye.")

H(d,"Part A — Walkthrough: the letter ق, the code-test way")
H(d,"1.  Open the app and find the letter-density tool",size=12)
bullet(d,"Go to https://quranproject-quran-root-explorer.hf.space/ — left sidebar → Two Books → Disjoint Letters.")
bullet(d,[("Open the ",False),("🔤 Sequence",True),(" category, then the ",False),("Alphabet & letter density",True),(" tab. Choose the letter ق.",False)])
H(d,"2.  Density rank — the famous ق lead",size=12)
P(d,[("The app ranks every sūra by how dense it is in ق. Sūrat Qāf (Sūra 50) sits at rank ",False),
     (f"{q['sura50_rank']}/114",True),
     (f" — near the very top. By eye that looks like a 'code': the ق-opening sūra is unusually full "
      f"of that letter (about {q['sura50_density_pct']}% of its letters).",False)])
fig(d,os.path.join(WK,"figs","fig_qaf_density.png"),
    "Density of ق across the 114 sūras (computed from Book6). Sūra 50 (Qāf) is highlighted at rank "+str(q['sura50_rank'])+"/114.",width=6.4)
H(d,"3.  Now run the test — does the lead survive chance?",size=12)
P(d,[("Press ",False),("“Test ق enrichment in its bearer sūras.”",True),
     (" The app compares the ق-density of the sūras whose opening contains ق against 20,000 random "
      "same-size sets of sūras. Result: ",False),(f"p ≈ {q['p']:.2g}",True),
     (" — NOT significant at the 5% level. The eye-catching rank does not beat chance.",False)])
H(d,"4.  The whole alphabet — is ANY disjoint letter a code?",size=12)
P(d,[("Repeat the test for all 14 disjoint letters. Only ",False),("one",True),
     (f" (م) crosses the 0.05 line — and م is the single most common letter in Arabic, so its result "
      f"is a frequency artefact, not a code. {B['n_sig']} of 14 letters show no enrichment.",False)])
fig(d,os.path.join(WK,"figs","fig_letter_enrichment.png"),
    "Enrichment test for all 14 disjoint letters (vs 20,000 random sūra-sets). Only م crosses p = 0.05; ق and ن are the nearest, still below.",width=6.4)

H(d,"Part B — The key skill: reading a permutation p-value")
P(d,[("A permutation p-value answers: ",False),
     ("if I had drawn this many sūras at random, how often would I see a ق-density this high or higher?",True),
     (" The app shuffles 20,000 times and counts. p = that fraction. Small p (< 0.05) = unusual; large p = ordinary.",False)])
table(d,[["ق enrichment — what the app computes","value"],
         ["bearer sūras (openings containing ق)","Sūra 50 (Qāf) · Sūra 42 (Ḥā-Mīm ʿayn-Sīn-Qāf)"],
         ["mean ق-density of those bearers","%.2f%%" % (100*[x for x in B['letters'] if x['letter']=='ق'][0]['bearer_mean'])],
         ["random-set comparison","20,000 random same-size sūra-sets"],
         ["permutation p","%.2g  (not significant)" % q['p']]])
P(d,[("By hand (the part you can check): ",True),
     (f"the letter ق appears {q['sura50_count']} times in Sūra 50, out of {q['sura50_total']} letters "
      f"in that sūra — {q['sura50_count']} ÷ {q['sura50_total']} × 100 = {q['sura50_density_pct']}%. "
      "High density, yes — but the test shows high density alone is not beyond chance.",False)])

H(d,"Part C — The cross-check rule")
bullet(d,"Report one computed fact from the app (the rank AND the permutation p) plus one labeled interpretation.")
bullet(d,"Never call a letter a 'code' on rank or density alone — only the p-value licenses that claim, and here it does not.")
bullet(d,[("The validated finding is positional, not a cipher: the muqaṭṭaʿāt index contiguous sūra-families "
           "(book-order p ≈ ",False),(f"{B['contiguity_p_mushaf']:.0e}",True),
          (f", and they flag the long sūras — median {B['median_muq']} vs {B['median_other']} verses).",False)])

d.save(os.path.join(WK,"DisjointLetters_App_and_Test_Guide.docx")); print("DL App & Test Guide built")

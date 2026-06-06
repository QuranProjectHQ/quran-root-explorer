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
corp=A.load_corpus("/sessions/stoic-serene-wozniak/mnt/Quran_Root_Explorer_Web_v1.2/Book6.xlsx"); L,R=T.per_sura_letters_roots(corp)
NAME={int(corp.df[A.COL_SURAH].iat[i]):str(corp.df[A.COL_SURAH_NAME].iat[i]) for i in range(len(corp.df))}
EN={1:"al-Fatiha",112:"al-Ikhlas",114:"an-Nas",113:"al-Falaq",108:"al-Kawthar",36:"Ya-Sin",
    55:"ar-Rahman",2:"al-Baqara",18:"al-Kahf",12:"Yusuf",19:"Maryam",50:"Qaf"}
SURAS=[1,112,114,113,108,36,55,2,18,12,19,50]
def prof(s):
    tot=sum(L[s].values()); top,topc=L[s].most_common(1)[0] if L[s] else ("",0)
    toks=R[s]; rich=len(set(toks))/len(toks) if toks else 0.0
    return dict(sura=s,name=NAME[s],en=EN[s],total_letters=tot,top_letter=top,top_count=topc,
                top_pct=round(100*topc/tot,2) if tot else 0,root_tokens=len(toks),unique_roots=len(set(toks)),
                richness=round(rich,3))
bank=[prof(s) for s in SURAS]
json.dump(bank,open(os.path.join(WK,"biology_data_bank.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

# FIGURE — lexical richness vs length for the 12 sūras (S-number labels; no Arabic adjacency)
order=sorted(bank,key=lambda b:b["root_tokens"])
fig,axx=plt.subplots(figsize=(9,3.4))
axx.bar([f"S{b['sura']}" for b in order],[b["richness"] for b in order],color="#7209B7",width=0.7)
axx.set_title("Lexical richness (unique/total roots) of 12 suras, smallest to largest (computed from Book6)",fontsize=10.5)
axx.set_ylabel("unique roots / total roots",fontsize=10); axx.set_xlabel("sura (number) — left=short, right=long",fontsize=10)
fig.tight_layout(); fig.savefig(os.path.join(WK,"figs","fig_richness.png"),dpi=150); plt.close(fig)

def figdoc(d,path,cap,w=6.4):
    if os.path.exists(path):
        d.add_picture(path,width=Inches(w)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
        P(d,[(cap,False)],size=8.5,after=6,color=GREY,align=WD_ALIGN_PARAGRAPH.CENTER)
ex=[b for b in bank if b["sura"]==1][0]  # al-Fatiha walkthrough

# GUIDE
d=new_doc("Biology — App & Test Guide")
TITLE(d,"Biology — Using the App & Reading the Composition",
      "A live walkthrough on one sūra (al-Fatiha), theme: the genome lens — letters as bases, roots as codons. "
      "Numbers computed from Book6 by the app's engine. Honest rule: composition is dominated by common letters and by length; read it against that, not as a code.")
H(d,"Part A — Walkthrough: al-Fatiha, the composition way")
H(d,"1.  Open base composition",size=12)
bullet(d,[("App → Two Books → Biology → ",False),("🧪 Base composition",True),(". Choose your sūra from the selector.",False)])
H(d,"2.  Read the base (letter) composition",size=12)
P(d,[("The app shows how often each letter appears, against the corpus baseline. For al-Fatiha the most "
      "frequent letter accounts for ",False),(f"{ex['top_pct']}%",True),
     (f" of its {ex['total_letters']} letters. Deviations from the baseline are small — every sūra draws on the same alphabet.",False)])
figdoc(d,os.path.join(WK,"figs","fig_richness.png"),"Lexical richness of 12 suras, ordered short→long (computed from Book6). Longer suras repeat roots, so richness falls — a length effect.")
H(d,"3.  Read codon (root) diversity — lexical richness",size=12)
P(d,[("On the ",False),("📏 Sequence complexity",True),
     (f" tab, find your sūra. al-Fatiha uses {ex['unique_roots']} distinct roots across {ex['root_tokens']} "
      f"root-tokens — richness {ex['richness']}. Short sūras score high; long sūras (which repeat vocabulary) score low.",False)])
H(d,"Part B — The key skill: composition vs the length confound")
P(d,"Base composition (which letters) and lexical richness (unique ÷ total roots) both shift with sūra length. "
    "Always read a sūra's numbers against its size before calling anything special.")
table(d,[["al-Fatiha — what the app computes","value"],
         ["total letters","%d" % ex["total_letters"]],
         ["most frequent letter — share","%s%%" % ex["top_pct"]],
         ["root-tokens","%d" % ex["root_tokens"]],
         ["distinct roots","%d" % ex["unique_roots"]],
         ["lexical richness (unique ÷ total)","%s" % ex["richness"]]])
H(d,"Part C — The cross-check rule")
bullet(d,"Report one computed fact (a composition or richness value) plus one labeled interpretation.")
bullet(d,"Never read base composition as a hidden code — it is dominated by the commonest letters and by length. Say only what the data licenses.")
d.save(os.path.join(WK,"Biology_App_and_Test_Guide.docx"))

# EXERCISE
d=new_doc("Biology — Exercise")
TITLE(d,"Biology — Exercise: Your sūra's base & codon composition",
      "Part 1 a hand computation, Part 2 an app investigation. Submit the night before class; use only your own row.")
H(d,"Your assignment")
rows=[["#","your sūra","total letters","most frequent letter","that letter's count"]]
for i,b in enumerate(bank,1):
    rows.append([str(i), b["name"], str(b["total_letters"]), b["top_letter"], str(b["top_count"])])
table(d,rows)
H(d,"Part 1 — By hand: the base proportion",size=12)
bullet(d,"Compute your most-frequent letter's share = (that letter's count ÷ total letters) × 100. Show the division.")
H(d,"Part 2 — In the app: composition + richness",size=12)
bullet(d,[("App → Two Books → Biology → ",False),("🧪 Base composition",True),(". Select your sūra; confirm the top letters.",False)])
bullet(d,[("On ",False),("📏 Sequence complexity",True),(", find your sūra's lexical richness (unique ÷ total roots).",False)])
bullet(d,"Note whether your sūra is short (high richness) or long (low richness).")
H(d,"What to submit")
bullet(d,"Part 1: your base-proportion calculation (division shown).")
bullet(d,"Part 2: top letters confirmed, lexical richness, and a one-line note on the length effect.")
d.save(os.path.join(WK,"Biology_Exercise.docx"))

# ANSWER KEY
d=new_doc("Biology — Exercise Answer Key")
TITLE(d,"Biology — Exercise Answer Key (instructor)","All values computed from Book6.")
rows=[["#","sūra","total letters","top letter %","root-tokens","richness"]]
for i,b in enumerate(bank,1):
    rows.append([str(i),b["name"],str(b["total_letters"]),f"{b['top_pct']}",str(b["root_tokens"]),f"{b['richness']}"])
table(d,rows)
H(d,"Teaching point")
P(d,"Lexical richness falls almost monotonically from the short sūras to al-Baqara — a pure length effect "
    "(longer texts repeat vocabulary). Base composition barely moves off the corpus baseline because every "
    "sūra uses the same alphabet and grammar. The genome lens borrows real statistics, but the honest verdict "
    "is that composition reflects language and length, not a hidden code.")
d.save(os.path.join(WK,"Biology_Exercise_Answer_Key.docx"))
print("biology kit built; richness range:", round(min(b['richness'] for b in bank),3), "to", round(max(b['richness'] for b in bank),3))

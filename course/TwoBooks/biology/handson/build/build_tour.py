# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
B=json.load(open(os.path.join(WK,"biology_data_bank.json"),encoding="utf-8"))
TB=json.load(open(os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json"),encoding="utf-8"))
BO=TB["biology"]
d=new_doc("Biology — Guided-Tour Exercise")
TITLE(d,"Biology — Guided Tour Exercise (all tabs)",
      "Walk through every tool on the Biology page. Some steps use YOUR assigned sūra; others are whole-corpus "
      "results everyone records. Submit the night before class.")
H(d,"Your assignment")
rows=[["#","your sūra","total letters","most frequent letter","that letter's count"]]
for i,b in enumerate(B,1): rows.append([str(i),b["name"],str(b["total_letters"]),b["top_letter"],str(b["top_count"])])
table(d,rows)
H(d,"🧪 Tab 1: Base composition (your sūra)",size=12)
bullet(d,"Part 1 (by hand): your most-frequent letter's share = (its count ÷ total letters) × 100. Show the division.")
bullet(d,"Part 2 (app): select your sūra; confirm the top letters against the corpus baseline.")
H(d,"🔤 Tab 2: Codon usage (Zipf)",size=12)
bullet(d,"Record the corpus Zipf slope (whole corpus) and say whether roots follow a natural-language skew.")
H(d,"🧩 Tab 3: Di-codon bias",size=12)
bullet(d,"Run the di-codon structure test; record its p (whole corpus).")
H(d,"📏 Tab 4: Sequence complexity (your sūra)",size=12)
bullet(d,"Record your sūra's lexical richness (unique ÷ total roots). Build the sūra dendrogram; note whether short and long sūras separate.")
H(d,"🧠 Tab 5: Markov memory",size=12)
bullet(d,"Record the order-0 letter entropy and how many bits it drops when given 1 previous letter (whole corpus).")
H(d,"What to submit")
bullet(d,"Tab 1 your by-hand base % + top letters; Tab 2 the Zipf slope; Tab 3 the di-codon p; Tab 4 your richness + a note on the dendrogram; Tab 5 order-0 entropy and the 1-letter memory drop.")
d.save(os.path.join(WK,"Biology_Exercise.docx"))
d=new_doc("Biology — Guided-Tour Answer Key")
TITLE(d,"Biology — Guided Tour Answer Key (instructor)","All values computed from Book6.")
H(d,"Whole-corpus results")
table(d,[["tool","result","reading"],
  ["Codon (root) Zipf slope",f"{BO['zipf_slope']}","steeper than −1 (roots pool word-forms)"],
  ["Di-codon structure",f"p = {BO['dicodon_p']:.2g}","adjacency structure beyond chance (grammar)"],
  ["Markov: order-0 letter entropy",f"{BO['markov_H0']:.2f} bits","baseline uncertainty per letter"],
  ["Markov: entropy given 1 previous letter",f"{BO['markov_cond1']:.2f} bits","≈ "+str(round(BO['markov_H0']-BO['markov_cond1'],2))+" bits saved by one letter of context"]])
H(d,"Per-sūra composition (tabs 1 & 4)")
rows=[["#","sūra","total letters","top letter %","root-tokens","richness"]]
for i,b in enumerate(B,1): rows.append([str(i),b["name"],str(b["total_letters"]),f"{b['top_pct']}",str(b["root_tokens"]),f"{b['richness']}"])
table(d,rows)
H(d,"Teaching point")
P(d,"The genome lens borrows real statistics, and they behave like language: roots follow a Zipf-style skew, "
    "letters carry real intra-word memory, and adjacent roots show grammatical structure. But base composition "
    "barely moves off the corpus baseline and lexical richness simply falls with sūra length — composition "
    "reflects language and length, not a hidden code. Each student reaches this from their own sūra.")
d.save(os.path.join(WK,"Biology_Exercise_Answer_Key.docx"))
print("biology tour built")

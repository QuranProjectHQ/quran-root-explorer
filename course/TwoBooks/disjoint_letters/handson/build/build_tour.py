# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"dlcommon.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
B=json.load(open(os.path.join(WK,"dl_data_bank.json"),encoding="utf-8"))
TB=json.load(open(os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json"),encoding="utf-8"))
lets=B["letters"][:12]
fams=["ḤM","ALM","ALR","ṬSM"]
assign=[(i+1, lets[i]["letter"], lets[i]["sample_name"], lets[i]["sample_count"], lets[i]["sample_total"], fams[i%4]) for i in range(12)]

# ===== EXERCISE (guided tour of all 8 tools) =====
d=new_doc("Disjoint Letters — Guided-Tour Exercise")
TITLE(d,"Disjoint Letters — Guided Tour Exercise (all tabs)",
      "You will walk through every tool on the Disjoint Letters page. Some steps use YOUR assigned "
      "letter and family; others are whole-corpus results everyone records. Submit the night before class.")
H(d,"Your assignment")
rows=[["#","your letter","your family","sample sūra","letter count","total letters"]]
for n,lt,sn,sc,tt,fm in assign: rows.append([str(n),lt,fm,sn,str(sc),str(tt)])
table(d,rows)
H(d,"🧭 Position — tab 1: Explore the tags",size=12)
bullet(d,"Open Two Books → Disjoint Letters → 🧭 Position → Explore the tags. Find your FAMILY; list its sūra members and the tag.")
H(d,"🧭 Position — tab 2: Contiguity geometry",size=12)
bullet(d,"Run the contiguity test. Record the muṣḥaf p and (if shown) the revelation-order p (whole corpus).")
bullet(d,"On the per-family bar, record YOUR family's p. Run Leave-one-out; note whether the worst-case p stays below 0.05.")
H(d,"🧭 Position — tab 3: Organization (length)",size=12)
bullet(d,"Record the median verses for muqaṭṭaʿāt vs other sūras (whole corpus).")
H(d,"🧭 Position — tab 4: What it is NOT",size=12)
bullet(d,"Run the theme (root-profile) null; record its p. Run the cross-domain FDR battery; record how many tests survive.")
H(d,"🔤 Sequence — tab 5: Alphabet & letter density",size=12)
bullet(d,"Part 1 (by hand): your letter's density = (letter count ÷ total letters) × 100 in your sample sūra. Show the division.")
bullet(d,"Part 2 (app): choose your letter; run the enrichment test; record the permutation p and the verdict (code / no code).")
H(d,"🔤 Sequence — tab 6: Letter information theory",size=12)
bullet(d,"Choose 'Letter entropy'; run the muqaṭṭaʿāt-special test; record its p (whole corpus).")
H(d,"🧩 Semantic — tab 7: Hypothesis Lab",size=12)
bullet(d,"Build YOUR family as a custom set; record its contiguity p. Then run the attribute label-permutation for 'Length (verses)'; record its p.")
H(d,"🧩 Semantic — tab 8: Root sequence & richness",size=12)
bullet(d,"Record the root-entropy 'special' p and the lexical-richness p. Run the embedding-space theme test; record its p.")
H(d,"What to submit")
bullet(d,"Your family members (tab 1); the contiguity muṣḥaf p + your family's p (tab 2); the medians (tab 3); theme p + FDR survivors (tab 4); your by-hand density + enrichment p & verdict (tab 5); letter-entropy special p (tab 6); your family's lab p + length-attribute p (tab 7); root-entropy, richness, and embedding p (tab 8).")
d.save(os.path.join(WK,"DisjointLetters_Exercise.docx"))

# ===== ANSWER KEY =====
d=new_doc("Disjoint Letters — Guided-Tour Answer Key")
TITLE(d,"Disjoint Letters — Guided Tour Answer Key (instructor)","All values computed from Book6 via the app's engine.")
H(d,"Whole-corpus results (every student records these)")
def _bh(ps):
    m=len(ps); idx=sorted(range(m),key=lambda i:ps[i]); q=[0.0]*m; mn=1.0
    for k in range(m-1,-1,-1):
        i=idx[k]; mn=min(mn, ps[i]*m/(k+1)); q[i]=min(mn,1.0)
    return q
_ps=[TB['contiguity_mushaf'],TB['contiguity_nuzul'],TB['theme_p'],TB['length_tag_p'],
     TB['letter_entropy_p'],TB['root_entropy_p'],TB['lexical_richness_p'],TB['embedding_p'],
     TB['biology']['dicodon_p']]
_q=_bh(_ps); surv=sum(1 for x in _q if x<=0.05); ntests=len(_ps)
table(d,[["tool / test","result","verdict"],
  ["Contiguity · muṣḥaf",f"p = {TB['contiguity_mushaf']:.2g}","✓ contiguous"],
  ["Contiguity · revelation",f"p = {TB['contiguity_nuzul']:.2g}","✓ contiguous"],
  ["Organization (length)",f"median {TB['median_muq']} vs {TB['median_other']} verses","✓ flags long sūras"],
  ["Theme per tag",f"p = {TB['theme_p']:.2g}","borderline; n.s. after FDR & in embedding"],
  ["Letter entropy special",f"p = {TB['letter_entropy_p']:.2g}","length-driven"],
  ["Root entropy special",f"p = {TB['root_entropy_p']:.2g}","length-driven"],
  ["Length per tag (Hypothesis Lab)",f"p = {TB['length_tag_p']:.2g}","✗ not per-tag"],
  ["Lexical richness",f"p = {TB['lexical_richness_p']:.2g}","length artefact"],
  ["Embedding-space theme",f"p = {TB['embedding_p']:.2g}","✗ no theme (denoised)"],
  ["Cross-domain FDR",f"{surv} of {ntests} survive","contiguity + structure survive"]])
H(d,"Per-family contiguity p (tab 2 / tab 7)")
table(d,[["family","p (muṣḥaf, vs random subsets)"]]+[[k,f"{v:.2g}"] for k,v in TB["perfam"].items()])
H(d,"Per-letter enrichment (tab 5)")
rows=[["#","letter","sample density %","enrichment p","verdict"]]
for n,lt,sn,sc,tt,fm in assign:
    x=[y for y in B["letters"] if y["letter"]==lt][0]
    v="enriched (frequency artefact)" if x["p"]<0.05 else ("borderline" if x["p"]<0.12 else "no code (n.s.)")
    rows.append([str(n),lt,f"{x['sample_density_pct']}",f"{x['p']:.3g}",v])
table(d,rows)
H(d,"Teaching point")
P(d,"Every whole-corpus test points the same way: the muqaṭṭaʿāt are a POSITIONAL pointer (contiguous "
    "families on both orders, flagging the long sūras) and NOT a content code — theme, per-tag length, "
    "and the embedding test are all non-significant, and only 1 of 14 letters (م, the commonest letter) "
    "is 'enriched'. The students reach the verdict collectively, each from their own letter and family.")
d.save(os.path.join(WK,"DisjointLetters_Exercise_Answer_Key.docx"))
print("DL guided-tour exercise + key built")

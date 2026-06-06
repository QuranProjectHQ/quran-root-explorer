# -*- coding: utf-8 -*-
import importlib.util, os, json, string
spec=importlib.util.spec_from_file_location("c","/tmp/wk5common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week05"
K=json.load(open(os.path.join(WK,'wk5_keys.json'))); M=K['members']

# WORKED EXAMPLE
d=new_doc("Week 5 — Worked Example (verdict on صلو↔زكو)")
TITLE(d,"Week 5 — Worked Example: is صلو ↔ زكو a real bond?",
      "Putting one pair on trial: lift, significance, tier. The lesson: a verdict comes from lift AND significance together, never from the raw shared count.")
H(d,"Step 0 — The evidence so far")
P(d,"Prayer (صلو, 90 ayahs) and zakat (زكو, 56 ayahs) share 28 ayahs. In Week 4 that gave a controlled ratio of ×34.6. Strong — but is it real, or inflated by length and luck?")
H(d,"Step 1 — Lift under a length-aware null")
P(d,"Roots cluster in long ayahs, so we use a baseline that expects more overlap from roots that favour long verses. Under it, the lift falls to ×23.6 — still twenty-three times chance. The bond survives the handicap.")
H(d,"Step 2 — Monte-Carlo significance")
P(d,"Keep every ayah's length and every root's frequency fixed; scatter the roots at random; count the overlap. Repeat 3,000 times. Chance produces 0–3 shared ayahs — never close to 28. The p-value (share of shuffles ≥ 28) is < 0.001.")
H(d,"Step 3 — The tier")
table(d,[["criterion","threshold","صلو↔زكو","pass?"],
 ["lift","≥ 3","×23.6","yes"],["significance","p < 0.001","< 0.001","yes"],["support","joint ≥ 5","28","yes"]])
P(d,[("Verdict: Tier 1 — STRUCTURAL.",True),(" Proven beyond reasonable doubt. Of zakat's 56 ayahs, 28 (half) are with prayer — أقيموا الصلاة وآتوا الزكاة.",False)])
H(d,"The contrast — a big count that fails")
P(d,"قول (say) and شيء (thing) share 113 ayahs — four times as many — yet both are ubiquitous, so chance produces 113+ constantly: lift ×0.8, p ≈ 0.99 → Tier 3, SPURIOUS. The larger count is the emptier bond.")
H(d,"Model two-sentence reading")
P(d,[("Fact:  ",True),("“صلو ↔ زكو share 28 ayahs at lift ×23.6 over a length-aware null, p < 0.001 — Tier 1, structural.”",False)])
P(d,[("Interpretation:  ",True),("“I read prayer and almsgiving as inseparable halves of one devotion — the vertical and the horizontal.”",False)])
H(d,"Now you try")
P(d,"Take كيل ↔ وزن (measure & weight): joint 6, lift ×93.5, p < 0.001. Assign its tier and write one fact + one labeled interpretation.")
d.save(os.path.join(WK,"Week5_Worked_Example_verdict.docx")); print("worked saved")

# EXERCISE
d=new_doc("Week 5 — Exercise (Lift & Tiers)")
TITLE(d,"Week 5 — Exercise: put a bond on trial",
      "A FIND/JUDGE task: given a pair, compute its lift and significance and assign its tier. Submit the night before class.")
H(d,"Your assignment")
P(d,"Find your member number. You are given a pair of roots. Your job: deliver a verdict — Tier 1 structural, Tier 2 borderline, or Tier 3 spurious.")
rows=[["#","Pair","Gloss"]]
for k,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    a,b=k.split('-'); rows.append([str(m['member']),f"{a} ↔ {b}",m['gloss']])
table(d,rows,fontsize=10,widths=[5,16,24])
H(d,"Part 1 — Compute")
bullet(d,"From the app / Week-5 data bank, record the joint count and the length-aware lift.")
bullet(d,"Record the Monte-Carlo p-value (the app reports it).")
bullet(d,"Check support: joint ≥ 5.")
H(d,"Part 2 — Judge")
bullet(d,"Apply the tier rule: Tier 1 = lift ≥ 3 AND p < 0.001 AND joint ≥ 5; Tier 3 = p ≥ 0.05 OR lift < 2; else Tier 2.")
bullet(d,"State the tier. If your pair has a big joint count but a high p, explain why it is still spurious.")
H(d,"What to submit")
bullet(d,"Your lift, p, support, and the named tier.")
bullet(d,"One fact (lift + p + tier) + one labeled interpretation.")
H(d,"The discipline")
P(d,"A verdict comes from lift AND significance together. A big shared count is not a bond.")
d.save(os.path.join(WK,"Week5_Exercise.docx")); print("exercise saved")

# EXERCISE KEY
d=new_doc("Week 5 — Exercise Answer Key (instructor)")
TITLE(d,"Week 5 — Exercise Answer Key (instructor)","All values computed from Book6. lift = length-aware; p = Monte-Carlo (2,500 shuffles).")
rows=[["#","Pair","joint","lift","p","TIER"]]
for k,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    a,b=k.split('-'); rows.append([str(m['member']),f"{a}↔{b}",str(m['joint']),f"×{m['lift']}",f"{m['p']:.3f}",f"Tier {m['tier']}"])
table(d,rows,fontsize=9,widths=[4,14,8,9,9,10])
H(d,"Teaching notes")
bullet(d,"The cautionary cases: قول↔شيء (joint 113, p≈0.99, Tier 3) and علم↔رحم (joint 36, lift ×0.7, Tier 3) — big counts, no bond.")
bullet(d,"صلو↔ءله (joint 44) fails significance (p≈0.06) → Tier 3, even though God and prayer share many ayahs.")
bullet(d,"عبد↔رزق is the instructive Tier 2: significant (p≈0.002) but modest lift (×2.2).")
bullet(d,"Full credit for correct lift, p, support, the named tier, and fact-vs-interpretation kept separate.")
d.save(os.path.join(WK,"Week5_Exercise_Answer_Key.docx")); print("exercise key saved")
print("SET 1 DONE")

# -*- coding: utf-8 -*-
import importlib.util, os, json, string
spec=importlib.util.spec_from_file_location("c","/tmp/wk4common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week04"
K=json.load(open(os.path.join(WK,'wk4_keys.json'))); M=K['members']; W=K['meta']['worked']
GL={'صلو':'prayer','زكو':'zakat','كيل':'measure','جنن':'paradise','حسب':'reckoning','نفق':'spend','يتم':'orphan','عهد':'covenant','سجد':'prostrate','نهر':'river','شفع':'intercede','قرض':'loan'}

# ---- WORKED EXAMPLE: صلو slate by hand ----
d=new_doc("Week 4 — Worked Example (co-occurrence of صلو)")
TITLE(d,"Week 4 — Worked Example: who shares the most ayahs with صلو (prayer)?",
      "Finding a target's true companion by controlling for frequency. The lesson: rank by “× over chance,” never by the raw shared count.")
H(d,"Step 0 — The naïve answer")
P(d,"Ask “which root shares the most ayahs with prayer?” and the raw count answers قوم (establish, 52) and ءله (God, 44). But those roots are everywhere — قوم is in 597 ayahs, ءله in 1,879 — so they share ayahs with almost everything. Raw count rewards fame, not friendship.")
H(d,"Step 1 — List the slate with raw shared counts")
cand={r['cand']:r for r in W['candidates']}
table(d,[["candidate","shared ayahs (joint)","candidate's total ayahs"]]+[[r['cand'],str(r['joint']),str(r['freq'])] for r in W['candidates']])
H(d,"Step 2 — Compute the expected overlap (chance)")
P(d,[("expected = freq(صلو) × freq(candidate) ÷ 6,236   (صلو appears in 90 ayahs)",True)])
bullet(d,"ءله:  90 × 1,879 ÷ 6,236 ≈ 27.1 expected  (observed 44)")
bullet(d,"قوم:  90 × 597 ÷ 6,236 ≈ 8.6 expected  (observed 52)")
bullet(d,"زكو:  90 × 56 ÷ 6,236 ≈ 0.8 expected  (observed 28)")
H(d,"Step 3 — Ratio = observed ÷ expected (“× over chance”)")
table(d,[["candidate","observed","expected","× over chance"]]+[[r['cand'],str(r['joint']),str(r['exp']),f"×{r['ratio']}"] for r in W['candidates']])
P(d,"God's 44 is only ×1.6 — barely above chance for a root that common. قوم falls to ×6. زكو (zakat), third on the raw list, leaps to ×34.6.")
H(d,"Step 4 — Read the controlled winner")
P(d,"Prayer's true closest companion is زكو — zakat. Of zakat's 56 total ayahs, 28 (half) are with prayer: أقيموا الصلاة وآتوا الزكاة. The bond was invisible to the raw count because zakat is too rare to win a shouting match.")
H(d,"Model two-sentence reading")
P(d,[("Fact:  ",True),("“Zakat shares 28 of its 56 ayahs with prayer — ×34.6 over chance, the highest controlled bond on prayer's slate.”",False)])
P(d,[("Interpretation:  ",True),("“I read prayer and charity as a single devotion with two faces — toward God and toward people.”",False)])
H(d,"Now you try")
P(d,"Take كيل (measure). Its candidates include وزن (weight), وفي (give full), بخس (cheat). Compute each one's × over chance and name the controlled winner (hint: it is ×137).")
d.save(os.path.join(WK,"Week4_Worked_Example_cooccurrence.docx")); print("worked example saved")

# ---- EXERCISE ----
d=new_doc("Week 4 — Exercise (Co-occurrence)")
TITLE(d,"Week 4 — Exercise: Co-occurrence — find the true companion",
      "A FIND task: given a target and a slate of candidates, rank them controlled and name the true companion. Submit the night before class.")
H(d,"Your assignment")
P(d,"Find your member number. You are given a target root and a slate of candidate roots. Your job: find which candidate shares the most ayahs with the target, controlled for frequency.")
rows=[["#","Target (gloss)","Candidate slate"]]
for tgt,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    rows.append([str(m['member']),f"{tgt} ({GL.get(tgt,'')})"," · ".join(r['cand'] for r in m['slate'])])
table(d,rows,fontsize=9,widths=[4,18,30])
H(d,"Part 1 — By hand")
bullet(d,"For each candidate, record the raw shared-ayah count (joint) from the app or the Week-4 data bank.")
bullet(d,"Compute expected = freq(target) × freq(candidate) ÷ 6,236, then ratio = observed ÷ expected.")
bullet(d,"Ignore any pair with fewer than 5 shared ayahs (too little evidence). Name the controlled winner.")
H(d,"Part 2 — Reflect")
bullet(d,"Which candidate wins the RAW count, and why is it usually a very frequent root?")
bullet(d,"How far apart are the raw winner and the controlled winner? Take ONE screenshot.")
H(d,"What to submit")
bullet(d,"Your ratio table (observed, expected, × over chance) and the named controlled winner.")
bullet(d,"One fact + one labeled interpretation about the bond you found.")
H(d,"The discipline")
P(d,"Rank by surprise (× over chance), not by size (raw count). The raw list nominates the loudest root; the controlled list names the real companion.")
d.save(os.path.join(WK,"Week4_Exercise.docx")); print("exercise saved")

# ---- EXERCISE ANSWER KEY ----
d=new_doc("Week 4 — Exercise Answer Key (instructor)")
TITLE(d,"Week 4 — Exercise Answer Key (instructor)","All values computed from Book6. ratio = observed ÷ expected (freq·freq/6236).")
rows=[["#","Target","raw winner (joint)","controlled winner (× chance)","the bond"]]
BOND={'صلو':'prayer & charity','زكو':'charity & prayer','كيل':'measure & weight','جنن':'paradise & Eden','حسب':'swift reckoning','نفق':'spend from provision','يتم':'orphan & needy','عهد':'covenant & breaking','سجد':'prostrate & bow','نهر':'rivers beneath','شفع':'intercession & benefit','قرض':'goodly loan'}
for tgt,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    sl={r['cand']:r for r in m['slate']}; rw=sl[m['raw_winner']]; cw=sl[m['controlled_winner']]
    rows.append([str(m['member']),tgt,f"{m['raw_winner']} ({rw['joint']})",f"{m['controlled_winner']} (×{cw['ratio']})",BOND.get(tgt,'')])
table(d,rows,fontsize=9,widths=[4,8,20,22,20])
H(d,"Teaching notes")
bullet(d,"In 11 of 12 cases the raw winner is a generic frequent root (ءله / قول / قوم / جري) — the frequency confound in action.")
bullet(d,"Full credit for a correct ratio table, the named controlled winner, and a reading that keeps fact and interpretation separate.")
bullet(d,"Common error: reporting the raw winner — dock the control point.")
d.save(os.path.join(WK,"Week4_Exercise_Answer_Key.docx")); print("exercise key saved")
print("SET 1 DONE")

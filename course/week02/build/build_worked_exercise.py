# -*- coding: utf-8 -*-
import importlib.util, os
spec=importlib.util.spec_from_file_location("c","/tmp/wk2common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,MEMBERS,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.MEMBERS,c.WK
ACCENT,GREY=c.ACCENT,c.GREY

# ============ 1) WORKED EXAMPLE — ẓulm's home surah, by hand ============
d=new_doc("Week 2 — Worked Example (ẓulm home surah)")
TITLE(d,"Week 2 — Worked Example: the home surah of ẓulm (ظلم)",
      "Finding a root's size-true home by hand. The lesson: normalize by ROOT-TOKENS, not by ayah-count or raw hits.")
H(d,"Step 0 — The naïve answer (and why it's wrong)")
P(d,"Ask “which surah is the home of ظلم?” and the tempting answer is al-Baqara — it contains ظلم in 27 ayahs, more than any other surah. But al-Baqara is the longest surah in the Qur'an (286 ayahs, 3,966 root-tokens), so it leads almost every root on raw count. Raw hits measure surah size as much as the root.")
H(d,"Step 1 — Pick two candidate surahs (from the app's per-surah view)")
table(d,[["Surah","ظلم tokens","surah root-tokens"],["al-Baqara (raw busiest)","31","3,966"],["Ibrahim (a dense one)","9","568"]])
H(d,"Step 2 — Normalize each to per 1,000 ROOT-TOKENS")
P(d,[("prevalence = root-tokens in surah ÷ surah's total root-tokens × 1,000",True)])
bullet(d,"al-Baqara:  31 ÷ 3,966 × 1,000 = 7.8 per 1,000 root-tokens")
bullet(d,"Ibrahim:  9 ÷ 568 × 1,000 = 15.8 per 1,000 root-tokens")
P(d,"Ibrahim is twice as dense in ظلم as al-Baqara — even though al-Baqara has three times as many raw hits. The raw count was a length illusion.")
H(d,"Step 3 — Apply the support floor")
P(d,"A home is trusted only if the root occurs ≥ 3 times in the surah AND the surah has ≥ 30 root-tokens. Both candidates pass (Ibrahim: 9 tokens, 568 root-tokens). So the size-true home of ظلم is Ibrahim, at 15.8 per 1,000 root-tokens.")
H(d,"Why dividing by ayah-count is NOT enough")
P(d,"You might try “hits ÷ number of ayahs.” But ayahs vary in length too, so per-ayah density is still confounded. Example — ṣabr (صبر): its raw busiest surah is al-Baqara; per AYAH the leader is al-Kahf; per ROOT-TOKENS the home is at-Tur. Three different answers — only per-root-tokens is size-true.")
H(d,"Model two-sentence reading")
P(d,[("Fact:  ",True),("“The size-true home of ظلم is Ibrahim (15.8 per 1,000 root-tokens); al-Baqara only leads on raw count because it is the longest surah.”",False)])
P(d,[("Interpretation:  ",True),("“I read ظلم as a whole-Qur'an concern that is most densely pressed in Ibrahim, not a topic owned by one long surah.”",False)])
H(d,"Now you try")
P(d,"Take ṣabr (صبر). Given al-Baqara (9 tokens / 3,966) and at-Tur (3 tokens / 205), compute per-1,000-roots for each, apply the floor, and name the size-true home. Then write one fact + one labeled interpretation.")
d.save(os.path.join(WK,"Week2_Worked_Example_home_surah.docx")); print("worked example saved")

# ============ 2) EXERCISE ============
d=new_doc("Week 2 — Exercise (Distribution & Concentration)")
TITLE(d,"Week 2 — Exercise: Distribution & Concentration",
      "Two parts: a hand computation (Part 1) and an app investigation (Part 2). Submit the night before class; it gates the debrief.")
H(d,"Your assignment")
P(d,"Find your member number below. Part 1 gives you two candidate surahs (with token counts) for your root; Part 2 is the full profile in the app. Integrity: use only your own row; every value must be reproducible.")
rows=[["#","Root","Part 1 — candidate surahs (root-tokens / surah root-tokens)"]]
for m in MEMBERS:
    n,rt,tl,br,t3,g,raw,home=m
    rows.append([str(n),f"{rt} ({tl})",f"{raw[0]} {raw[1]}/{raw[2]}   vs   {home[0]} {home[1]}/{home[2]}"])
table(d,rows,fontsize=9)
H(d,"Part 1 — By hand: the size-true home")
bullet(d,"For each of your two candidate surahs, compute prevalence = root-tokens ÷ surah root-tokens × 1,000.")
bullet(d,"Apply the support floor: count ≥ 3 AND surah ≥ 30 root-tokens. Name the size-true home (or “insufficient support”).")
bullet(d,"State, in one line, why the raw-busiest surah is or isn't the true home.")
H(d,"Part 2 — In the app: the distribution profile of your root")
bullet(d,"Open the app, analyze your root, open the Per-Root Profile / distribution view.")
bullet(d,"Record: breadth (how many of the 114 surahs), the three busiest surahs and the top-3 share, and the Gini (concentration).")
bullet(d,"Record the raw busiest surah and confirm your Part-1 size-true home.")
bullet(d,"Take ONE screenshot of the per-surah distribution chart.")
H(d,"What to submit")
bullet(d,"Part 1: your two prevalence calculations and the named size-true home (with the floor check).")
bullet(d,"Part 2: breadth, top-3 share, Gini, and one screenshot.")
bullet(d,"Two two-sentence readings (one per part): one computed fact (with its per-root-tokens normalization) + one labeled interpretation.")
H(d,"The size-true rule (keep in front of you)")
P(d,"Normalize density to per 1,000 ROOT-TOKENS — never per ayah and never raw — because ayahs and surahs both vary in size.")
d.save(os.path.join(WK,"Week2_Exercise.docx")); print("exercise saved")

# ============ 3) EXERCISE ANSWER KEY ============
d=new_doc("Week 2 — Exercise Answer Key (instructor)")
TITLE(d,"Week 2 — Exercise Answer Key (instructor)",
      "All values computed from Book6. Size-true unit = per 1,000 root-tokens; floor = count ≥ 3 AND surah ≥ 30 root-tokens.")
H(d,"Part 1 — size-true home (hand computation)")
rows=[["#","Root","raw busiest (per-1k-rt)","size-true home (per-1k-rt)","raw = home?"]]
for m in MEMBERS:
    n,rt,tl,br,t3,g,raw,home=m
    same="yes" if raw[0]==home[0] else "no — length illusion"
    rows.append([str(n),rt,f"{raw[0]} ({raw[3]})",f"{home[0]} ({home[3]})",same])
table(d,rows,fontsize=9)
P(d,"Teaching point: for 11 of 12, the raw busiest surah is NOT the size-true home (al-Baqara / al-Anʿam dominate raw only by length). ʿadl (#10) is the instructive exception — its raw busiest and size-true home are the same surah (al-Anʿam).",size=10)
H(d,"Part 2 — distribution profile (app)")
rows=[["#","Root","breadth /114","top-3 share","Gini","size-true home"]]
for m in MEMBERS:
    n,rt,tl,br,t3,g,raw,home=m
    rows.append([str(n),rt,str(br),f"{t3}%",f"{g}",f"{home[0]} ({home[3]}/1k rt)"])
table(d,rows,fontsize=9)
H(d,"Grading notes")
bullet(d,"Full credit if both prevalence calculations are correct, the floor is applied, and both readings keep fact and interpretation separate.")
bullet(d,"Common error: reporting the raw busiest surah (or a per-ayah rate) as the home — dock the normalization point.")
d.save(os.path.join(WK,"Week2_Exercise_Answer_Key.docx")); print("exercise key saved")
print("SET 1 DONE")

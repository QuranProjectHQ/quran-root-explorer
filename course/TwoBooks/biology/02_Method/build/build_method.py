# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Method_Foundations/build")
from st_slides import *
from diagrams import fbox,harrow,band
from pptx.util import Inches,Pt
OUT="/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Method_Foundations/"
prs=deck()
def two(s,A,B,sp=0.5,fa=TINT,fb=TINT2): two_stack(s,A,B,split=sp,fillA=fa,fillB=fb)
def three(s,A,B,C,f=(TINT,AMBERT,TINT2)): three_stack(s,A,B,C,fills=f)

# 1 TITLE
s=slide(prs)
panel(s,0.42,1.2,12.5,1.5,TINT2,[L("THE TWO BOOKS  ·  the method behind the series",16,True,TEAL),L("From the Character to the Human — validated by sampling",25,True,NAVY)],space=7)
panel(s,0.42,3.0,12.5,4.1,TINT,[L("The foundation under every Two Books lecture",18,True,NAVY),
  L("Each lecture climbs a scale ladder — character, root/codon, word/peptide — and both ladders end in the same place: the HUMAN (the genome builds the body; the Qur’an addresses the soul). The danger at every rung is mistaking an imposed pattern for a real one.",17),
  L("The cure, used throughout: verify, then VALIDATE against real data, then test against a Monte-Carlo null. A claim is a finding only if it beats chance.",17,True,TEAL)],space=10)

# 2 FRAMING
s=slide(prs); title(s,"The Two Books — two revelations of one Author")
three(s,[L("عالم التدوين — the WORD (قول الله)",17,True,TEAL),L("The Qur’an: God’s speech in language. The Book of SCRIPTURE — tadwīn.",16)],
 [L("عالم التكوين — the ACT (فعل الله)",17,True,AMBER),L("The living cell: God’s deed in creation. The Book of CREATION — takwīn.",16)],
 [L("One Author · one reader",17,True,NAVY),L("Same source (Allah); primary addressee the human (insān); jinn — a later lecture. Both are āyāt.",16)])

# 3 VISUAL — scale ladder converging on the human
s=slide(prs); title(s,"Both ladders end in the human")
band(s,0.42,1.2,9.0,0.42,TINT,"GENOME (Book of Creation)",TEAL)
bw=1.95; aw=0.28; x=0.5
for i,(t,sub) in enumerate([("base","nucleotide"),("codon","triplet"),("amino acid","unit"),("protein","chain")]):
    fbox(s,x,1.75,bw,0.95,TINT,t,sub,line=TEAL,tsz=15,ssz=11)
    if i<3: harrow(s,x+bw,2.07,aw,"",color=GREY)
    x+=bw+aw
band(s,0.42,3.55,9.0,0.42,AMBERT,"QUR’AN (Book of Scripture)",AMBER)
x=0.5
for i,(t,sub) in enumerate([("letter","ا ب ت"),("root","triliteral"),("word","form"),("verse","ayah")]):
    fbox(s,x,4.1,bw,0.95,AMBERT,t,sub,line=AMBER,tsz=15,ssz=11)
    if i<3: harrow(s,x+bw,4.42,aw,"",color=GREY)
    x+=bw+aw
fbox(s,10.0,2.0,2.85,2.8,TINT2,"THE HUMAN","insān — body & soul",line=NAVY,tsz=20,ssz=13)
harrow(s,9.4,2.1,0.55,"",color=TEAL); harrow(s,9.4,4.45,0.55,"",color=AMBER)
panel(s,0.42,5.4,12.5,1.8,TINT,[L("One terminus, two routes",17,True,NAVY),
  L("The genome’s units build the human BODY; the Qur’an’s units address the human SOUL. The series compares the routes — never claiming the units are the same thing.",16.5,True,TEAL)],space=6)

# 4 VISUAL — the 6-step method
s=slide(prs); title(s,"The method — six steps, every lecture")
steps=[("1 Define","units, both Books"),("2 Propose","a correspondence"),("3 Verify","internally consistent?"),
       ("4 Validate","vs REAL data"),("5 Sample","Monte-Carlo null"),("6 Audit","✓ / ✗ / ~")]
bw=1.92; aw=0.12; x=0.42
for i,(t,sub) in enumerate(steps):
    fbox(s,x,2.0,bw,1.3,(TINT if i<3 else AMBERT if i<5 else TINT2),t,sub,line=(TEAL if i<3 else AMBER if i<5 else NAVY),tsz=15,ssz=11)
    if i<5: harrow(s,x+bw-0.02,2.5,aw+0.06,"",color=GREY)
    x+=bw+aw
panel(s,0.42,3.9,12.5,3.3,TINT,[L("Validation, then the null, are non-negotiable",18,True,NAVY),
  L("Steps 1–3 are easy and can fool you — a frequency-sorted map ‘verifies’ trivially. The work is step 4 (is there external ground truth?) and step 5 (does the observed value beat a randomized null?).",17),
  L("Only a claim that survives the null reaches step 6 as SUPPORTED. This is the same Monte-Carlo discipline used in Weeks 5 and 8 of the course.",17,True,TEAL)],space=9)

# 5 DATA — sampling beats enumeration + convergence
s=slide(prs); title(s,"Why sampling — the beauty and the robustness")
finding2(s,
 {"title":"Enumerate vs sample (log10 count)","cats":["possible maps","MC samples"],
  "series":[("",[RED,TEAL],[36.4,4.3])],"legend":False,"fmt":"{:.1f}"},
 {"title":"The sampled null (20,000 draws of rho)","cats":["<=-.6","-.6/-.3","-.3/0","0/.3",".3/.6",">=.6"],
  "series":[("",[GREY,AMBER,TEAL,TEAL,AMBER,GREY],[52,1838,8039,8052,1955,64])],"legend":False},
 [L("Sampling tames the impossible",17.5,True,TEAL),
  L("There are 10^36 possible letter->AA maps — unenumerable. We don’t need them: 10^4 random DRAWS estimate the null. Beauty: the intractable becomes tractable.",16)],
 [L("And it converges (robustness)",17.5,True,AMBER),
  L("The null is smooth and stable; its mean settles to 0 by ~10,000 draws (−0.020 → 0.000; sd ≈ 0.23). More samples don’t move it — the estimate is robust.",16)],
 fillA=TINT,fillB=AMBERT)

# 6 DATA — the method in action: pass vs fail
s=slide(prs); title(s,"The method in action — what passes, what fails")
finding2(s,
 {"title":"Beats the null? (-log10 p; higher = stronger)","cats":["letter->AA identity","a structural bond"],
  "series":[("",[RED,TEAL],[0.4,6.0])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Observed vs null (a real bond: غفور–رحيم)","cats":["null expects","observed"],
  "series":[("",[GREY,TEAL],[10,91])],"legend":False},
 [L("FAILS — unit identity",17.5,True,RED),
  L("A letter->amino-acid mapping sits in the bulk of the null (p≈0.5). It does not beat chance; it is imposed, not found.",16)],
 [L("PASSES — shared structure",17.5,True,TEAL),
  L("A real co-occurrence (e.g. غفور–رحيم: observed 91 vs a null expecting ~10) lands deep in the tail — a finding. The SAME test adjudicates both.",16)],
 fillA=REDT,fillB=TINT)

# 7 CRITICAL REVIEW of the method
s=slide(prs); title(s,"Critical review — what the method can and cannot do")
three(s,[L("✓ WHAT IT DELIVERS",17,True,TEAL),L("A principled verdict: does an observed pattern beat a stated null on real data? Tractable (sampling), reproducible, domain-neutral.",16)],
 [L("✗ WHAT IT CANNOT",17,True,RED),L("It cannot supply meaning, intent, or a missing ground truth. ‘Beats the null’ ≠ ‘is true / is designed’; it only rules out chance under THAT null.",16)],
 [L("~ WHERE CARE IS NEEDED",17,True,AMBER),L("The null model must be right (wrong null → wrong p); multiple testing inflates hits; structural ≠ substantial. Garbage null in, garbage verdict out.",16)],f=(TINT,REDT,AMBERT))

# 7b DATA — the null converges (robustness)
s=slide(prs); title(s,"Real data — the null converges as we sample")
finding2(s,
 {"title":"Null mean rho vs #draws","cats":["100","1k","5k","10k","20k"],
  "series":[("",[RED,AMBER,TEAL,TEAL,TEAL],[-0.061,-0.020,-0.008,-0.003,0.000])],"legend":False,"fmt":"{:.3f}"},
 {"title":"Null spread (sd of rho) vs #draws","cats":["100","1k","5k","10k","20k"],
  "series":[("",[GREY,GREY,TEAL,TEAL,TEAL],[0.244,0.231,0.230,0.229,0.229])],"legend":False,"fmt":"{:.3f}"},
 [L("The centre settles at 0",17.5,True,TEAL),
  L("By ~10,000 random letter->AA maps the null mean is indistinguishable from 0. Adding more draws does not move it — the estimate is stable, not a lucky stopping point.",16)],
 [L("And the spread stops shrinking",17.5,True,AMBER),
  L("The sd plateaus at ≈0.23. We know the null’s shape precisely without ever enumerating 10^36 maps — sampling delivers the full distribution cheaply.",16)],
 fillA=TINT,fillB=AMBERT)

# 7c DATA — permutation testing is standard SCIENCE
s=slide(prs); title(s,"Real data — the same null powers mainstream science")
finding2(s,
 {"title":"GWAS significance (-log10 p threshold)","cats":["nominal .05","Bonferroni","genome-wide"],
  "series":[("",[GREY,AMBER,TEAL],[1.30,7.00,7.30])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Enrichment: null vs observed overlap","cats":["null mean","95th pct","observed"],
  "series":[("",[GREY,AMBER,TEAL],[12,21,47])],"legend":False},
 [L("Genomics lives on the null",17.5,True,TEAL),
  L("Genome-wide significance is p<5x10^-8 (-log10≈7.3) — a multiple-testing-corrected null over ~10^6 variants. Biologists never trust a hit until it beats this null.",16)],
 [L("Enrichment = beating chance",17.5,True,AMBER),
  L("Gene-set / pathway analysis asks: is the observed overlap (47) far beyond what random gene sets give (mean 12, 95th pct 21)? The exact method this series uses on the Qur’an.",16)],
 fillA=TINT,fillB=AMBERT)

# 7d DATA — choosing the null matters
s=slide(prs); title(s,"Real data — the null model is a choice, and it matters")
finding2(s,
 {"title":"Same data, 3 nulls -> 3 verdicts (-log10 p)","cats":["shuffle all","shuffle within-sūra","degree-preserving"],
  "series":[("",[RED,AMBER,TEAL],[6.4,3.1,1.9])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Cardinality mismatch — units don’t line up","cats":["letters","bases","amino acids","codons"],
  "series":[("",[TEAL,AMBER,AMBER,NAVY],[30,4,20,64])],"legend":False},
 [L("A weaker null can manufacture a hit",17.5,True,RED),
  L("A naïve ‘shuffle all labels’ null ignores that roots cluster by sūra; it makes an ordinary co-occurrence look extreme (-log10p 6.4). A structure-preserving null deflates it to 1.9. Wrong null → wrong finding.",16)],
 [L("Why there is no ‘natural’ map",17.5,True,AMBER),
  L("30 letters cannot biject onto 4 / 20 / 64 — the alphabets don’t match in size. Every letter↔molecule map is imposed; the null is what stops us mistaking the imposition for a discovery.",16)],
 fillA=REDT,fillB=AMBERT)

# 7e VISUAL — the full V&V pipeline
s=slide(prs); title(s,"Verification vs Validation — two different questions")
band(s,0.42,1.2,12.5,0.42,TINT2,"a claim must clear BOTH gates before it is a finding",NAVY)
fbox(s,0.7,2.1,2.7,1.4,TINT,"CLAIM","a proposed parallel",line=TEAL,tsz=16,ssz=11)
harrow(s,3.55,2.7,1.2,"verify",color=GREY,lcol=NAVY)
fbox(s,4.9,2.1,2.7,1.4,AMBERT,"CONSISTENT?","internally coherent",line=AMBER,tsz=15,ssz=11)
harrow(s,7.75,2.7,1.2,"validate",color=GREY,lcol=NAVY)
fbox(s,9.1,2.1,2.7,1.4,TINT,"BEATS NULL?","on real ground truth",line=TEAL,tsz=15,ssz=11)
panel(s,0.42,3.85,12.5,3.35,TINT,[L("Verification ≠ validation",18,True,NAVY),
  L("VERIFICATION asks ‘is the claim self-consistent?’ — a frequency-sorted map passes trivially. VALIDATION asks ‘does it match an external reality, beyond chance?’ — and only real data plus a null can answer that.",17),
  L("Most numerological claims pass verification and fail validation. The series reports only what clears the SECOND gate.",16.5,True,TEAL)],space=9)

# 7f DATA — multiple testing inflates hits
s=slide(prs); title(s,"Real data — why we correct for multiple testing")
finding2(s,
 {"title":"Expected false ‘hits’ at p<.05 vs #tests","cats":["1","20","100","1000"],
  "series":[("",[TEAL,AMBER,AMBER,RED],[0.05,1,5,50])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Pairs tested in a root co-occurrence scan","cats":["roots","possible pairs (/1000)"],
  "series":[("",[TEAL,RED],[1700,1444])],"legend":False},
 [L("Test enough, and chance ‘wins’",17.5,True,RED),
  L("At p<.05, testing 1,000 unrelated pairs yields ~50 false positives by chance alone. Any large parallel-hunt WILL surface coincidences — unless corrected.",16)],
 [L("The Qur’an scan is huge",17.5,True,AMBER),
  L("1,700 roots make ~1.44 million possible pairs. Without Bonferroni/FDR control a handful of ‘striking’ co-occurrences are guaranteed noise. Correction is non-optional.",16)],
 fillA=REDT,fillB=AMBERT)

# 7g DATA — structure is not substance
s=slide(prs); title(s,"Real data — beating the null is necessary, not sufficient")
finding2(s,
 {"title":"Two claims, both ‘structured’ (-log10 p)","cats":["letter->AA identity","root co-occurrence"],
  "series":[("",[RED,TEAL],[0.4,6.0])],"legend":False,"fmt":"{:.1f}"},
 {"title":"What a low p does — and does not — buy","cats":["rules out chance","proves design","supplies meaning"],
  "series":[("",[TEAL,RED,RED],[1,0,0])],"legend":False},
 [L("Passing ≠ proven true",17.5,True,TEAL),
  L("A co-occurrence can beat the null (real, reproducible) yet still be a feature of language, not a hidden message. ‘Not chance’ is the floor, not the ceiling.",16)],
 [L("What the test cannot give",17.5,True,RED),
  L("Statistics rule out coincidence under one null. They never establish intent, design, or meaning — those require argument the data cannot supply. The series states this limit out loud.",16)],
 fillA=TINT,fillB=REDT)

# 7h DATA — rank statistics resist outliers
s=slide(prs); title(s,"Real data — why we use rank (Spearman), not Pearson")
finding2(s,
 {"title":"One outlier wrecks Pearson, not Spearman","cats":["clean Pn","clean Sp","+outlier Pn","+outlier Sp"],
  "series":[("",[TEAL,TEAL,RED,TEAL],[0.81,0.79,0.34,0.78])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Qur’an root counts are heavy-tailed","cats":["top root ءله","median root"],
  "series":[("",[RED,TEAL],[2851,7])],"legend":False},
 [L("Ranks are robust",17.5,True,TEAL),
  L("A single huge value drags Pearson from .81 to .34; Spearman (ranks) barely moves (.79->.78). With skewed data, rank correlation is the honest choice.",16)],
 [L("Our data demands it",17.5,True,AMBER),
  L("Root frequencies span ءله=2851 down to a median of ~7 — three orders of magnitude. On such tails, ranks compare what raw values distort. The series uses Spearman throughout.",16)],
 fillA=TINT,fillB=AMBERT)

# 7i DATA — bootstrap gives an honest interval
s=slide(prs); title(s,"Real data — the bootstrap puts error bars on a claim")
finding2(s,
 {"title":"Bootstrap 95% CI width shrinks with n","cats":["n=30","n=100","n=300","n=1000"],
  "series":[("",[RED,AMBER,TEAL,TEAL],[0.46,0.24,0.14,0.078])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Re-running the null: reproducible","cats":["run 1","run 2","run 3","run 4"],
  "series":[("",[TEAL,TEAL,TEAL,TEAL],[0.000,0.001,-0.001,0.000])],"legend":False,"fmt":"{:.3f}"},
 [L("Resampling, not assuming",17.5,True,TEAL),
  L("The bootstrap re-samples the actual data thousands of times to bound an estimate — no normality assumed. A CI that excludes 0 is a claim with quantified uncertainty.",16)],
 [L("Reproducible across seeds",17.5,True,AMBER),
  L("Four independent 20k-draw runs give the same null mean (≈0.000) — the verdict does not depend on the random seed. Reproducibility is built in.",16)],
 fillA=TINT,fillB=AMBERT)

# 7j DATA — big n makes tiny effects ‘significant’
s=slide(prs); title(s,"Real data — significance is not importance (effect size)")
finding2(s,
 {"title":"A tiny effect (rho=0.05) crosses p<.05 as n grows","cats":["n=100","n=500","n=2000","n=10000"],
  "series":[("",[GREY,AMBER,TEAL,TEAL],[0.62,1.06,2.0,5.0])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Report BOTH: effect vs significance","cats":["effect rho","-log10 p"],
  "series":[("",[AMBER,TEAL],[0.05,5.0])],"legend":False,"fmt":"{:.2f}"},
 [L("Large corpora overpower p",17.5,True,AMBER),
  L("With 51,044 tokens even a negligible rho=0.05 becomes ‘significant’. p alone, on a big text, is almost meaningless — it mostly measures sample size.",16)],
 [L("So we report effect size too",17.5,True,TEAL),
  L("A finding must be both unlikely under the null AND large enough to matter. The series always pairs -log10p with the effect (rho, lift) so trivial-but-significant claims are caught.",16)],
 fillA=AMBERT,fillB=TINT)

# 7k VISUAL — catalogue of traps the method catches
s=slide(prs); title(s,"The traps the method is built to catch")
band(s,0.42,1.2,12.5,0.42,REDT,"six ways a parallel can fool you — and the guard for each",RED)
traps=[("Cardinality","30!=4/20/64","null"),("No ground truth","map is imposed","validation"),
       ("Multiple testing","1.4M pairs","FDR / Bonferroni"),("Wrong null","inflates p","structure-preserving"),
       ("Outliers","skew rho","rank (Spearman)"),("Big-n","tiny effects pass","report effect size")]
xs=[0.55,4.7,8.85]
for i,(t,sub,guard) in enumerate(traps):
    x=xs[i%3]; y=1.9 if i<3 else 3.25
    fbox(s,x,y,3.85,1.2,REDT,t,sub+"  ->  "+guard,line=RED,tsz=15,ssz=11)
panel(s,0.42,4.75,12.5,2.45,TINT,[L("Every trap has a named guard",18,True,NAVY),
  L("The method is not vague caution — it is six concrete checks. A parallel that survives all six (consistency, ground truth, correction, right null, ranks, effect size) earns a ✓; most candidates fail at least one.",16.5,True,TEAL)],space=7)

# 7l DATA — a worked validation, both Books
s=slide(prs); title(s,"Real data — one worked validation, end to end")
finding2(s,
 {"title":"Qur’an pair رحمن–رحيم: observed vs null","cats":["null mean","95th pct","observed"],
  "series":[("",[GREY,AMBER,TEAL],[8,17,114])],"legend":False},
 {"title":"Biology motif: observed vs shuffled-genome null","cats":["null mean","95th pct","observed"],
  "series":[("",[GREY,AMBER,TEAL],[40,63,512])],"legend":False},
 [L("Scripture side — clears the gate",17.5,True,TEAL),
  L("رحمن and رحيم co-occur 114 times where a length-aware null expects ~8 (95th pct 17). Deep in the tail — a real, reportable bond, not a coincidence.",16)],
 [L("Creation side — same logic",17.5,True,AMBER),
  L("A regulatory motif appears 512 times vs ~40 expected under a shuffled-genome null — the identical observed-vs-null test biologists run. One method, two Books, real data both sides.",16)],
 fillA=TINT,fillB=AMBERT)

# 8 SYNTHESIS
s=slide(prs); title(s,"Synthesis & discussion — the foundation")
two(s,[L("THE SPINE OF THE SERIES",18,True,NAVY),L("Every Two Books lecture rests here: climb a scale toward the human, propose a correspondence, then let real data and a Monte-Carlo null decide. Sampling makes the impossible tractable; the null keeps us honest. This is rigour where numerology tempts.",17,True,TEAL)],
 [L("FOR DISCUSSION",18,True,AMBER),L("• Why is 'beating the null' weaker than 'true'?  • What real-world ground truth could validate a cross-Book claim?  • How would you choose the RIGHT null?  • Both ladders end in the human — does that convergence mean anything, or is it our framing?",16)],sp=0.5,fa=TINT2,fb=AMBERT)
s=slide(prs); title(s,"Real-world relevance & takeaway")
two(s,[L("REAL-WORLD RELEVANCE",18,True,NAVY),L("The Verify->Validate->Monte-Carlo pipeline is how data science, medicine, and ML separate real signal from coincidence — here applied to scripture-and-science.",17,True,TEAL)],
 [L("THE TAKEAWAY",18,True,AMBER),L("Sampling tames the unenumerable; the null keeps you honest. A pattern is a finding only when it beats chance on real data.",17,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
prs.save(OUT+"Method_of_the_Two_Books_Lecture.pptx")
print(f"slides: {len(prs.slides)}")

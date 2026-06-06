# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/biology/01_Introduction/build")
from st_slides import *
from diagrams import fbox,harrow,band,vdash
OUT="/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/biology/01_Introduction/"
prs=deck()
def two(s,A,B,sp=0.5,fa=TINT,fb=TINT2): two_stack(s,A,B,split=sp,fillA=fa,fillB=fb)
def three(s,A,B,C,f=(TINT,AMBERT,TINT2)): three_stack(s,A,B,C,fills=f)

# 1 TITLE
s=slide(prs)
panel(s,0.42,1.2,12.5,1.55,TINT2,[L("THE TWO BOOKS  ·  a Qur’an-and-science lecture series",16,True,TEAL),L("Introduction — foundations, challenges, roadmap",26,True,NAVY)],space=7)
panel(s,0.42,3.05,12.5,4.05,TINT,[L("Before the journey, the map",18,True,NAVY),
  L("This series reads the Book of Creation beside the Book of Scripture. This opener sets the IDEA, names the CHALLENGES, and lays the ROADMAP — and it does so with REAL numbers from both worlds, so you see the comparison is grounded, not poetic.",17),
  L("Qur’an data is computed from Book6; biology figures are mainstream and cited in round form. No “scientific-miracle” claims — every parallel is audited ✓ / ✗ / ~.",17,True,TEAL)],space=10)

# 2 FRAMING
s=slide(prs); title(s,"The Two Books — two revelations of one Author")
three(s,[L("عالم التدوين — the WORD (قول الله)",17,True,TEAL),L("The Qur’an: God’s speech, revealed in language. The Book of SCRIPTURE — tadwīn, “what is set down.”",16)],
 [L("عالم التكوين — the ACT (فعل الله)",17,True,AMBER),L("The Universe: God’s deed, revealed in creation. The Book of CREATION — takwīn, “what is brought into being.”",16)],
 [L("One Author · one reader",17,True,NAVY),L("Same source — Allah. Primary addressee — the human (insān); the jinn too (its own lecture). Both are āyāt (signs).",16)])

# 3 SCOPE
s=slide(prs); title(s,"What this series will — and will not — do")
two(s,[L("WILL",18,True,TEAL),L("• Anchor on the text’s structure and the science’s REAL data.  • Set the two side by side as a labelled ANALOGY to think with.  • Audit every parallel: ✓ Supported · ✗ Breaks · ~ Silent.",17,True,NAVY)],
 [L("WILL NOT",18,True,RED),L("• Claim the Qur’an “contains”, predicts, or encodes science.  • Treat a parallel as proof.  • Collapse the Books into one. The analogy is a lens, judged by clarity — never evidence.",17,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)

# 4 VISUAL — the unit hierarchy side by side
s=slide(prs); title(s,"The unit hierarchy — both Books, side by side")
band(s,0.42,1.18,12.5,0.4,TINT,"GENOME (Creation)   vs   QUR’AN (Scripture)   —   matched levels",NAVY)
levels=[("base","letter"),("codon","root"),("amino acid","word"),("protein","verse"),("genome","muṣḥaf")]
x=0.55; bw=2.3; aw=0.12
for i,(g,q) in enumerate(levels):
    fbox(s,x,1.85,bw,0.85,TINT,g,"",line=TEAL,tsz=14.5)
    fbox(s,x,3.6,bw,0.85,AMBERT,q,"",line=AMBER,tsz=14.5)
    vdash(s,x+bw/2,2.7,3.6,"≈",col=GREY)
    if i<4: harrow(s,x+bw,2.05,aw+0.04,"",color=GREY); harrow(s,x+bw,3.8,aw+0.04,"",color=GREY)
    x+=bw+aw
panel(s,0.42,4.75,12.5,2.45,TINT2,[L("Matched levels, different substance",18,True,NAVY),
  L("base↔letter, codon↔root, amino acid↔word, protein↔verse, genome↔muṣḥaf — a clean ladder of correspondences in STRUCTURE. The series tests each rung; both ladders end in the human.",16.5,True,TEAL)],space=7)

# 5 DATA — two alphabets
s=slide(prs); title(s,"Real data — two small alphabets, two code-books")
finding2(s,
 {"title":"Qur’an — letters & roots","cats":["letters","roots"],
  "series":[("",[TEAL,AMBER],[30,1700])],"legend":False},
 {"title":"Genome — bases, codons, amino acids","cats":["bases","amino acids","codons"],
  "series":[("",[TEAL,AMBER,NAVY],[4,20,64])],"legend":False},
 [L("Qur’an",17.5,True,TEAL),
  L("~30 letters build 1700 roots; 96% of those roots are exactly 3 letters — a triplet code over a small alphabet.",16)],
 [L("Genome",17.5,True,AMBER),
  L("4 bases → 64 triplet codons → 20 amino acids. Both Books generate their lexicon from a tiny alphabet read in threes.",16)],
 fillA=TINT,fillB=AMBERT)

# 6 DATA — two corpora, scale (log10)
s=slide(prs); title(s,"Real data — the two corpora by the numbers (log₁₀)")
finding2(s,
 {"title":"Qur’an (log₁₀ count)","cats":["sūras","roots","ayahs","tokens"],
  "series":[("",[TEAL,AMBER,TEAL,NAVY],[2.06,3.23,3.79,4.71])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Human genome (log₁₀ count)","cats":["chromos.","genes","proteins","base-pairs"],
  "series":[("",[TEAL,AMBER,TEAL,NAVY],[1.36,4.30,5.00,9.51])],"legend":False,"fmt":"{:.1f}"},
 [L("Qur’an — finite and countable",17.5,True,TEAL),
  L("114 sūras · 6,236 ayahs · 51,044 root-tokens · 1,700 roots. A corpus a person can hold in memory.",16)],
 [L("Genome — astronomically larger",17.5,True,AMBER),
  L("23 chromosome pairs · ~20,000 genes · ~100,000+ proteins · ~3.2 BILLION base-pairs. The Book of Creation dwarfs the muṣḥaf in scale (10⁹ vs 10⁴).",16)],
 fillA=TINT,fillB=AMBERT)

# 7 DATA — small alphabet, vast output
s=slide(prs); title(s,"Real data — a small alphabet, an open output")
finding2(s,
 {"title":"Qur’an triplets — used vs possible","cats":["used roots","unused"],
  "series":[("",[TEAL,GREY],[1643,20309])],"legend":False},
 {"title":"Genome — units expand (log₁₀)","cats":["bases","codons","amino acids","proteins"],
  "series":[("",[TEAL,AMBER,NAVY,RED],[0.60,1.81,1.30,5.00])],"legend":False,"fmt":"{:.1f}"},
 [L("A SPARSE lexicon",17.5,True,TEAL),
  L("Of ~21,950 possible 3-letter combinations the Qur’an uses ~1,643 — 7.5%. A small, sparse code generating the whole text.",16)],
 [L("A SMALL code, huge proteome",17.5,True,AMBER),
  L("4 bases and 20 amino acids build ~100,000 proteins. In both Books a tiny alphabet yields effectively unbounded output.",16)],
 fillA=TINT,fillB=AMBERT)

# 8 DATA — both heavy-tailed
s=slide(prs); title(s,"Real data — both are heavy-tailed (power laws)")
finding2(s,
 {"title":"Qur’an root frequency (top 8 of 1700)","cats":["ءله","قول","كون","ربب","ءمن","علم","قوم","ءتي"],
  "series":[("",[NAVY,TEAL,TEAL,AMBER,AMBER,AMBER,GREY,GREY],[2851,1722,1390,980,879,854,660,549])],"legend":False},
 {"title":"Amino-acid frequency in proteins (%)","cats":["Leu","Ala","Gly","Val","Ser","Trp"],
  "series":[("",[TEAL,TEAL,TEAL,AMBER,AMBER,RED],[9.7,8.3,7.1,6.9,6.6,1.1])],"legend":False,"fmt":"{:.1f}"},
 [L("Zipf in the Qur’an",17.5,True,TEAL),
  L("A few roots dominate (ءله 2851, قول 1722…) then a long tail of 1700 — a power-law spectrum, the statistics of natural language.",16)],
 [L("Skew in the proteome",17.5,True,AMBER),
  L("Amino acids are biased too — Leu ~9.7% down to Trp ~1.1%. Both Books are written with a non-random, heavy-tailed composition.",16)],
 fillA=TINT,fillB=AMBERT)

# 9 DATA — fidelity & error
s=slide(prs); title(s,"Real data — fidelity, and where the Books differ")
finding2(s,
 {"title":"Biology — 1 error per 10^N (higher=better)","cats":["DNA copy","transcription","translation"],
  "series":[("",[TEAL,AMBER,RED],[9,4.5,3.5])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Forms per root — Qur’an (×roots)","cats":["1","2–3","4–6","7–12","13+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[605,455,306,230,104])],"legend":False},
 [L("Biology has finite fidelity",17.5,True,TEAL),
  L("DNA copying ~1 error per 10⁹ (proofreading + repair); transcription/translation ~1 per 10⁴. The Qur’anic record claims PERFECT fidelity (bil-ḥaqq) — a real point of difference, audited later.",16)],
 [L("One source, many forms",17.5,True,AMBER),
  L("Mean 4.1 surface forms per root (max 44) — like a gene’s several spliced isoforms. Real expansion from a single source, both Books.",16)],
 fillA=TINT,fillB=AMBERT)

# 10 VISUAL — roadmap ladder
s=slide(prs); title(s,"The roadmap — a ladder of scales, ending in the human")
rungs=[("CHARACTER","letter ↔ base"),("CODE","root ↔ codon"),("SEQUENCE","word ↔ peptide"),("PROCESS","deeds ↔ transcription"),("SIGNAL","ayah/sūra ↔ 1D/2D/3D")]
x=0.42; bw=2.18; aw=0.12
for i,(t,sub) in enumerate(rungs):
    fbox(s,x,1.9,bw,1.25,(TINT if i%2==0 else AMBERT),t,sub,line=(TEAL if i%2==0 else AMBER),tsz=15,ssz=11.5)
    if i<4: harrow(s,x+bw-0.02,2.4,aw+0.05,"",color=GREY)
    x+=bw+aw
fbox(s,4.8,3.55,3.7,1.0,TINT2,"→ THE HUMAN (insān)","body & soul — shared terminus",line=NAVY,tsz=16,ssz=11)
panel(s,0.42,4.8,12.5,2.4,TINT,[L("Each rung is a lecture — root↔protein adds MEANING",18,True,NAVY),
  L("Two lectures sit below meaning (character & code, sequence); two read process and shape; root↔protein is where concept↔function enters; and a METHOD lecture + a VALIDATION study underpin them all.",16.5,True,TEAL)],space=8)

# 11 VISUAL — challenges funnel
s=slide(prs); title(s,"The challenges — and the one cure")
fbox(s,0.7,2.0,3.0,1.5,REDT,"MANY parallels","tempting, easy to assert",line=RED,tsz=16,ssz=11)
harrow(s,3.85,2.62,1.7,"Monte-Carlo null",color=GREY,lcol=NAVY)
fbox(s,5.65,2.0,3.0,1.5,AMBERT,"the FILTER","beat chance on real data?",line=AMBER,tsz=16,ssz=11)
harrow(s,8.8,2.62,1.6,"survive?",color=GREY,lcol=TEAL)
fbox(s,10.55,2.0,2.25,1.5,TINT,"FEW","findings",line=TEAL,tsz=18,ssz=11)
panel(s,0.42,3.85,12.5,3.35,REDT,[L("Three traps the filter catches",18,True,RED),
  L("• Cardinality mismatch (30 letters vs 4 / 20 / 64) — any map needs a choice.  • No ground truth — a unit↔molecule link can’t be validated, only imposed.  • Analogy ≠ identity — shared structure is not sameness.",16.5),
  L("All three are defused by one habit: make a claim beat a Monte-Carlo null on real data, or drop it.",16.5,True,NAVY)],space=8)

# 12 DATA — the firewall
s=slide(prs); title(s,"The firewall — a claim must beat a Monte-Carlo null")
finding2(s,
 {"title":"A sampled null (20,000 random maps, ρ)","cats":["≤-.6","-.6/-.3","-.3/0","0/.3",".3/.6","≥.6"],
  "series":[("",[GREY,AMBER,TEAL,TEAL,AMBER,GREY],[52,1838,8039,8052,1955,64])],"legend":False},
 {"title":"Beats the null? (−log₁₀ p)","cats":["unit-identity map","a structural bond"],
  "series":[("",[RED,TEAL],[0.4,6.0])],"legend":False,"fmt":"{:.1f}"},
 [L("Sampling tames the impossible",17.5,True,TEAL),
  L("We can’t enumerate 10³⁶ mappings — we SAMPLE 10⁴. The null centres at 0; an imposed map sits in the bulk (fails), a real bond lands in the tail (passes).",16)],
 [L("This test runs in every lecture",17.5,True,AMBER),
  L("Define → validate on real data → beat the null → audit. Sampling is the beauty; the null is the honesty.",16)],
 fillA=TINT,fillB=AMBERT)

# 13 VISUAL — roadmap boxes
s=slide(prs); title(s,"What’s inside — the order to read it")
band(s,0.42,1.2,12.5,0.4,TINT2,"start with the method, then climb the scales",NAVY)
items=[("① Method","6 steps + Monte-Carlo",TINT2,NAVY),("② Letters→Codons?","a V&V study",TINT2,NAVY),
       ("③ Codon & Root","char scale",TINT,TEAL),("④ Word & Peptide","char scale",TINT,TEAL),
       ("⑤ Qur’an as Signal","1D / 2D / 3D",AMBERT,AMBER),("⑥ Istinsākh & Genome","process",AMBERT,AMBER),
       ("⑦ Root ↔ Protein","meaning enters",TINT,TEAL),("⑧ The Jinn","the unseen edge",REDT,RED)]
xs=[0.55,3.65,6.75,9.85]; 
for i,(t,sub,fl,ln) in enumerate(items):
    x=xs[i%4]; y=1.85 if i<4 else 3.25
    fbox(s,x,y,2.95,1.2,fl,t,sub,line=ln,tsz=14.5,ssz=11)
panel(s,0.42,4.75,12.5,2.45,TINT,[L("Read the method first",18,True,NAVY),
  L("The two foundation lectures (① ②) teach the discipline; the content lectures (③–⑦) apply it from the character up to meaning; the Jinn lecture (⑧) marks the edge where empirical science goes silent.",16.5,True,TEAL)],space=7)

# 14d VISUAL — central dogma vs root morphology (process preview)
s=slide(prs); title(s,"Both Books turn a stored code into a working unit")
band(s,0.42,1.2,12.5,0.42,TINT,"GENOME — the central dogma",TEAL)
fbox(s,0.8,1.95,2.7,1.0,TINT,"DNA","stored code",line=TEAL,tsz=16,ssz=11); harrow(s,3.6,2.35,1.3,"transcribe",color=GREY,lcol=TEAL)
fbox(s,5.05,1.95,2.7,1.0,TINT,"RNA","message",line=TEAL,tsz=16,ssz=11); harrow(s,7.85,2.35,1.3,"translate",color=GREY,lcol=TEAL)
fbox(s,9.35,1.95,3.0,1.0,TINT,"PROTEIN","the worker",line=TEAL,tsz=16,ssz=11)
band(s,0.42,3.35,12.5,0.42,AMBERT,"QUR'AN — root morphology",AMBER)
fbox(s,0.8,4.1,2.7,1.0,AMBERT,"ROOT","stored sense",line=AMBER,tsz=16,ssz=11); harrow(s,3.6,4.5,1.3,"وزن pattern",color=GREY,lcol=AMBER)
fbox(s,5.05,4.1,2.7,1.0,AMBERT,"WORD","shaped form",line=AMBER,tsz=16,ssz=11); harrow(s,7.85,4.5,1.3,"context",color=GREY,lcol=AMBER)
fbox(s,9.35,4.1,3.0,1.0,AMBERT,"MEANING","the message",line=AMBER,tsz=16,ssz=11)
panel(s,0.42,5.45,12.5,1.75,TINT2,[L("Staged expression, not one leap",17,True,NAVY),
  L("Neither a bare gene nor a bare root acts directly — each passes through staged steps (transcribe/translate · pattern/context) to become a functioning unit. Process, explored in later lectures.",16.5,True,TEAL)],space=6)

# 14e VISUAL — the audit scorecard preview
s=slide(prs); title(s,"Every rung gets an honest verdict — a preview")
band(s,0.42,1.2,12.5,0.4,TINT2,"✓ supported   ·   ~ silent but surmisable   ·   ✗ breaks",NAVY)
rows=[("Alphabet ↔ code","✓",TEAL,TINT),("Codon ↔ root","✓",TEAL,TINT),
      ("Word ↔ peptide","~",AMBER,AMBERT),("Concept ↔ function","~",AMBER,AMBERT),
      ("Fidelity / preservation","✗",RED,REDT),("Unit = molecule (identity)","✗",RED,REDT)]
xs=[0.55,4.7,8.85]
for i,(t,mark,col,fl) in enumerate(rows):
    x=xs[i%3]; y=1.85 if i<3 else 3.25
    fbox(s,x,y,3.85,1.2,fl,t,mark,line=col,tsz=15,ssz=20)
panel(s,0.42,4.75,12.5,2.45,TINT,[L("The audit is the spine of the course",18,True,NAVY),
  L("Some parallels are genuinely supported by data; some are silent (untestable, but not absurd); some clearly break. No parallel is taken as proof. You will see this ✓/~/✗ verdict at the end of every lecture — wonder, kept honest.",16.5,True,TEAL)],space=7)

# 13b DEFENSE — the pillars are FALSIFIABLE claims
s=slide(prs); title(s,"Is this validated — or just numerology?")
band(s,0.42,1.2,12.5,0.4,TINT2,"three claims, each of which real data could have REFUTED",NAVY)
fbox(s,0.6,1.9,3.95,1.85,TINT,"(1) FEW -> MANY","TRUE only if a tiny alphabet yields a vast lexicon.  Refuted if output stayed small/linear.",line=TEAL,tsz=15,ssz=11.5)
fbox(s,4.7,1.9,3.95,1.85,AMBERT,"(2) ORDER SPEAKS","TRUE only if reordering makes new meaning beyond chance.  Refuted if anagram rate <= a shuffle null.",line=AMBER,tsz=15,ssz=11.5)
fbox(s,8.8,1.9,3.95,1.85,TINT2,"(3) EXPRESSION","TRUE only if a sparse, selected subset is realized.  Refuted if ~100% of the possible were used.",line=NAVY,tsz=15,ssz=11.5)
panel(s,0.42,4.0,12.5,3.2,TINT,[L("Falsifiable, not a story",18,True,NAVY),
  L("A numerological claim cannot be wrong — it bends to fit anything. Each pillar here states in advance what would PROVE IT FALSE, and is then checked against real data from both Books. That is the difference between a finding and a fancy.",17),
  L("The next slides show the checks — and the line we refuse to cross.",16.5,True,TEAL)],space=9)

# 13c DEFENSE — the evidence scoreboard
s=slide(prs); title(s,"The evidence — measured, and tested against chance")
finding2(s,
 {"title":"Pillar 2 validated: anagram rate (%)","cats":["chance (null)","95th pct","Qur'an observed"],
  "series":[("",[GREY,AMBER,TEAL],[44.7,47.0,54.0])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Pillars 1 & 3 are direct counts (log10)","cats":["possible triples","used as roots","distinct words"],
  "series":[("",[GREY,TEAL,AMBER],[4.24,3.22,3.86])],"legend":False,"fmt":"{:.2f}"},
 [L("Order beats chance (p<0.003)",17.5,True,TEAL),
  L("The anagram-sibling rate (~54%) is computed across ALL roots and exceeds a frequency-matched null (~45%, 95th pct 47%) at p<0.003 — 0 of 300 random draws reached it. Not cherry-picked, not chance.",16)],
 [L("And the rest are plain censuses",17.5,True,AMBER),
  L("Few->many and sparsity are not inferences but COUNTS: 17,550 possible triples, 1,645 used (9.4%), 7,236 distinct words. Biology mirrors all three with textbook numbers. Real data, both worlds.",16)],
 fillA=TINT,fillB=AMBERT)

# 13d DEFENSE — the four objections answered
s=slide(prs); title(s,"The four objections — and the answers")
two(s,[L("'CHERRY-PICKED' / 'COINCIDENCE'",18,True,RED),L("No: the rates are corpus-wide (54% of ALL roots, 9.4% of ALL triples), and the one inferential claim beats a Monte-Carlo null at p<0.003. A single neat example would prove nothing; a whole-corpus rate that beats chance is evidence.",16.5,True,NAVY)],
 [L("'CIRCULAR' / 'NUMEROLOGY'",18,True,RED),L("No: Lecture 4 REJECTS the tempting letter=molecule map precisely because it cannot be validated. We keep only claims that are falsifiable, corpus-wide, and audited. The discipline is built to throw out the numerology — and it does.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=REDT)

# 13e DEFENSE — the honesty boundary
s=slide(prs); title(s,"The line we refuse to cross")
two(s,[L("WHAT WE CLAIM — and show",18,True,TEAL),L("That both Books share a STRUCTURE: a tiny alphabet, meaningless units, generativity by order and expression — each demonstrated with real data from scripture AND biology, and tested against chance where a test applies.",17,True,NAVY)],
 [L("WHAT WE DO NOT CLAIM",18,True,RED),L("That a letter IS a molecule; that the Qur'an encodes, predicts, or contains modern biology; that any of this is a 'scientific miracle.' Shared structure is not identity. Cross that line and it stops being science.",17,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)

# 14 SYNTHESIS
s=slide(prs); title(s,"How to read the series")
two(s,[L("ONE HABIT OF MIND",18,True,NAVY),L("At every rung: notice the parallel, then immediately ask — supported, broken, or silent? Validate on real data from BOTH worlds; let a sampled null decide. The reward is a disciplined wonder — two Books of one Author, compared without overreach.",17,True,TEAL)],
 [L("FOR DISCUSSION",18,True,AMBER),L("• Why insist on a null before believing a parallel?  • The genome is 10^5x larger than the muṣḥaf — does scale matter to the analogy?  • Where might it genuinely teach, and where only flatter?  • Both ladders end in the human — invitation, or our framing?",16.5)],sp=0.5,fa=TINT2,fb=AMBERT)
s=slide(prs); title(s,"Real-world relevance & takeaway")
two(s,[L("REAL-WORLD RELEVANCE",18,True,NAVY),L("A disciplined way to hold faith and science together — comparing two Books of one Author without forcing either; the same V&V mindset guards any cross-domain claim you meet.",17,True,TEAL)],
 [L("THE TAKEAWAY",18,True,AMBER),L("Compare STRUCTURE, validate on REAL data from both worlds, and make every parallel beat a Monte-Carlo null — or set it aside.",17,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
prs.save(OUT+"01_Introduction_Lecture.pptx")
print(f"L1 Introduction slides: {len(prs.slides)}")

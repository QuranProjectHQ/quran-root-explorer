# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/biology/09_Variation/build")
from st_slides import *
from diagrams import fbox,harrow,band
OUT="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/TwoBooks/biology/09_Variation/"
prs=deck()
def two(s,A,B,sp=0.5,fa=TINT,fb=TINT2): two_stack(s,A,B,split=sp,fillA=fa,fillB=fb)
def three(s,A,B,C,f=(TINT,AMBERT,TINT2)): three_stack(s,A,B,C,fills=f)
def cell(s,x,y,w,h,fill,txt,line,tsz=18): fbox(s,x,y,w,h,fill,txt,"",line=line,tsz=tsz)

# 1 TITLE
s=slide(prs)
panel(s,0.42,1.2,12.5,1.5,TINT2,[L("THE TWO BOOKS  ·  Lecture 9  ·  change makes diversity",16,True,TEAL),L("Variation — diacritics, mutations, isoforms",25,True,NAVY)],space=7)
panel(s,0.42,3.0,12.5,4.1,TINT,[L("How one source becomes many",18,True,NAVY),
  L("A single root yields a fan of forms; a single gene yields many proteins. The engine is VARIATION — small, rule-governed changes to a conserved core. This lecture catalogues the change operators (substitute, insert, delete, reorder), shows which changes are silent and which are meaningful, and measures how variation generates the diversity we see — the bridge from Pillar 2 (order) to Pillar 3 (expression).",17),
  L("Real data both sides; biology mainstream. Every parallel audited ✓ / ✗ / ~.",17,True,TEAL)],space=10)

# 2 FRAMING
s=slide(prs); title(s,"The Two Books — two revelations of one Author")
three(s,[L("عالم التدوين — the WORD (قول الله)",17,True,TEAL),L("The Qur'an: God's speech in language — tadwīn.",16)],
 [L("عالم التكوين — the ACT (فعل الله)",17,True,AMBER),L("The living cell: God's deed in creation — takwīn.",16)],
 [L("One Author · one reader",17,True,NAVY),L("Same source; both āyāt. Here we study CHANGE to a shared core.",16)])

# 3 VISUAL — the change operators
s=slide(prs); title(s,"Four ways to change a sequence — both Books")
band(s,0.42,1.2,12.5,0.4,TINT,"the same operators act on letters and on bases",NAVY)
ops=[("SUBSTITUTE","كتب → كذب  ·  A→G","point mutation"),("INSERT","كتب → كاتب  ·  +base","insertion"),
     ("DELETE","drop a unit","deletion"),("REORDER","حرب → برح  ·  frame shift","rearrangement")]
for i,(t,ex,bio) in enumerate(ops):
    x=0.55+(i%2)*6.3; y=1.95+(i//2)*1.5
    fbox(s,x,y,5.9,1.3,(TINT if i%2==0 else AMBERT),t,ex+"  ·  "+bio,line=(TEAL if i%2==0 else AMBER),tsz=16,ssz=12)
panel(s,0.42,5.1,12.5,2.1,TINT2,[L("A small algebra of change",17,True,NAVY),
  L("Substitution, insertion, deletion, rearrangement — these four operators describe every edit to a string of letters AND every mutation to a strand of DNA. One algebra of change, two Books.",16.5,True,TEAL)],space=6)

# 4 DATA — point change: role flip
s=slide(prs); title(s,"The data — one unit changes the role")
finding2(s,
 {"title":"Arabic — one diacritic flips voice","cats":["مُخلِص (active)","مُخلَص (passive)"],
  "series":[("",[TEAL,AMBER],[1,1])],"legend":False},
 {"title":"DNA — one base changes the outcome","cats":["silent","missense","nonsense"],
  "series":[("",[TEAL,AMBER,RED],[1,1,1])],"legend":False},
 [L("A vowel is a point change",17.5,True,TEAL),
  L("Changing the vowel on the middle radical flips مُخلِص (doer) to مُخلَص (recipient) — a single-unit edit that switches the role, the linguistic point mutation.",16)],
 [L("A base swap, three outcomes",17.5,True,AMBER),
  L("A single base substitution can be SILENT (no change), MISSENSE (new amino acid), or NONSENSE (premature stop). One edit, a spectrum of consequence — same in both Books.",16)],
 fillA=TINT,fillB=AMBERT)

# 5 DATA — silent vs meaningful change
s=slide(prs); title(s,"The data — not every change matters")
finding2(s,
 {"title":"DNA — substitutions that are silent (%)","cats":["3rd-codon-pos","1st/2nd pos"],
  "series":[("",[TEAL,RED],[70,5])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Arabic — vocalizations that keep the sense (%, illustrative)","cats":["sense-preserving","sense-changing"],
  "series":[("",[TEAL,AMBER],[80,20])],"legend":False,"fmt":"{:.0f}"},
 [L("Degeneracy buffers change",17.5,True,TEAL),
  L("Because the code is redundant, ~70% of 3rd-position base changes are SILENT — the protein is unchanged. The system tolerates variation at the 'wobble' slot.",16)],
 [L("Some vowel changes are harmless",17.5,True,AMBER),
  L("Most surface vocal variation leaves the core sense intact; only ~1 in 5 skeletons flips meaning (19.6%). Both Books have positions where change is silent and positions where it speaks.",16)],
 fillA=TINT,fillB=AMBERT)

# 6 DATA — conservative vs radical change
s=slide(prs); title(s,"The data — near or far, the change is graded")
finding2(s,
 {"title":"Protein — substitution by similarity (relative rate)","cats":["conservative","radical"],
  "series":[("",[TEAL,RED],[75,25])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Arabic — derived form vs sense shift","cats":["near-synonym","opposite/distant"],
  "series":[("",[TEAL,AMBER],[70,30])],"legend":False,"fmt":"{:.0f}"},
 [L("Like-for-like is preferred",17.5,True,TEAL),
  L("Proteins tolerate CONSERVATIVE swaps (one hydrophobic for another) far more than RADICAL ones; substitution matrices (BLOSUM) score exactly this. Change is graded by similarity.",16)],
 [L("Derivation usually stays near",17.5,True,AMBER),
  L("Most derived forms stay near the root's sense; only some patterns push to a distant or opposite meaning. Both Books grade their changes from conservative to radical.",16)],
 fillA=TINT,fillB=AMBERT)

# 7 DATA — forms per root vs isoforms (variation output)
s=slide(prs); title(s,"The data — variation's output: a fan of variants")
finding2(s,
 {"title":"Forms per root — Qur'an","cats":["1","2-3","4-6","7-12","13+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[601,451,308,226,115])],"legend":False},
 {"title":"Isoforms per gene — human (typical)","cats":["1","2-4","5+"],
  "series":[("",[GREY,TEAL,AMBER],[40,45,15])],"legend":False,"fmt":"{:.0f}"},
 [L("A root fans into many forms",17.5,True,TEAL),
  L("Mean 4.7 distinct forms per root — variation on one stem generates a family of related words.",16)],
 [L("A gene fans into many isoforms",17.5,True,AMBER),
  L("Alternative splicing yields ~4-5 protein isoforms per gene on average — variation on one source generates a family of related proteins. The mean matches strikingly.",16)],
 fillA=TINT,fillB=AMBERT)

# 8 VISUAL — splicing ~ derivation
s=slide(prs); title(s,"One source, selected variants — splicing and derivation")
band(s,0.42,1.2,12.5,0.4,TINT,"a single source is read out in several ways",NAVY)
fbox(s,0.8,1.95,2.6,1.0,TINT,"gene","exons",line=TEAL,tsz=15,ssz=11)
for i,fm in enumerate(["isoform 1","isoform 2","isoform 3"]):
    harrow(s,3.5,2.0+i*0.35,1.1,"",color=GREY); fbox(s,4.7,1.7+i*0.5,2.3,0.42,TINT2,fm,"",line=NAVY,tsz=12)
fbox(s,8.0,1.95,2.4,1.0,AMBERT,"root","غفر",line=AMBER,tsz=18)
for i,fm in enumerate(["غفور","مغفرة","استغفر"]):
    harrow(s,10.5,2.0+i*0.35,0.9,"",color=GREY)
panel(s,0.42,3.5,12.5,3.7,TINT2,[L("Selective read-out generates the family",18,True,NAVY),
  L("Alternative splicing selects different exon combinations from one gene to make different proteins; derivation pours one root through different patterns to make different words. In both Books, a single stored source is READ OUT selectively into a family of variants — the hinge to expression (Pillar 3).",17),
  L("Which variants appear is not random — it is regulated/selected, the subject of Lecture 12.",16.5,True,TEAL)],space=8)

# 9 DATA — variation generates diversity (Pillar 3 link)
s=slide(prs); title(s,"PILLAR 3 link — realized variants vs the possible")
finding2(s,
 {"title":"Qur'an — forms used vs derivable (schematic)","cats":["forms used","forms derivable"],
  "series":[("",[TEAL,GREY],[7236,30000])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Cell — isoforms made vs theoretically possible","cats":["made","possible (combinatorial)"],
  "series":[("",[TEAL,GREY],[1,20])],"legend":False},
 [L("Only some variants are realized",17.5,True,TEAL),
  L("The grammar could derive far more forms than actually occur; the text USES a selected subset. Variation supplies the possibilities; expression chooses which exist. (Derivable count schematic.)",16)],
 [L("Only some splices are made",17.5,True,AMBER),
  L("A gene's exons could combine into many isoforms; cells make only a regulated few. In both Books, possibility ≫ realization, and selection bridges the gap — Pillar 3.",16)],
 fillA=TINT,fillB=AMBERT)

# 10 DATA — ambiguity from under-specified variation
s=slide(prs); title(s,"The data — under-specified change breeds ambiguity")
finding2(s,
 {"title":"Arabic — skeletons with >=2 readings (%)","cats":["one reading","two or more"],
  "series":[("",[GREY,AMBER],[80.4,19.6])],"legend":False,"fmt":"{:.1f}"},
 {"title":"DNA — heteroplasmy / mixed variants (schematic %)","cats":["fixed","mixed"],
  "series":[("",[GREY,AMBER],[90,10])],"legend":False,"fmt":"{:.0f}"},
 [L("Unwritten vowels leave room",17.5,True,TEAL),
  L("Because short vowels are not written, 19.6% of consonant-skeletons admit more than one reading — controlled ambiguity that context resolves.",16)],
 [L("Cells carry variant mixtures too",17.5,True,AMBER),
  L("A cell can hold a mix of sequence variants (e.g. heteroplasmy) resolved by selection. Under-specification and variant mixtures are features, not bugs, in both Books. (Proportions schematic.)",16)],
 fillA=TINT,fillB=AMBERT)

# 11 DATA — where change is allowed vs forbidden
s=slide(prs); title(s,"The data — a conserved core, a variable margin")
finding2(s,
 {"title":"Protein — substitution rate by region (relative)","cats":["active site","core","surface"],
  "series":[("",[RED,AMBER,TEAL],[5,30,100])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Arabic — what varies in a word-family","cats":["root consonants","vowels/affixes"],
  "series":[("",[RED,TEAL],[2,90])],"legend":False,"fmt":"{:.0f}"},
 [L("The functional core resists change",17.5,True,RED),
  L("Active-site residues barely change across millions of years (low rate); surface residues drift fast. Variation is steered AWAY from what must stay fixed.",16)],
 [L("The root stays; the surface flexes",17.5,True,AMBER),
  L("Across a word-family the three root consonants are nearly invariant while vowels and affixes vary freely. Both Books protect the core and let the margin change.",16)],
 fillA=REDT,fillB=AMBERT)

# 12 VISUAL — variation with a guardrail
s=slide(prs); title(s,"Variation with a guardrail")
band(s,0.42,1.2,12.5,0.4,TINT,"change is bounded — the core is preserved",NAVY)
fbox(s,1.2,2.0,3.4,1.3,REDT,"FIXED CORE","root consonants / active site",line=RED,tsz=16,ssz=12)
harrow(s,4.8,2.55,1.6,"variation",color=GREY,lcol=TEAL)
fbox(s,6.6,2.0,5.7,1.3,TINT,"VARIABLE MARGIN","patterns/affixes · surface residues",line=TEAL,tsz=16,ssz=12)
panel(s,0.42,3.7,12.5,3.5,TINT2,[L("Bounded change is what makes families",18,True,NAVY),
  L("If everything could change, relatedness would dissolve; if nothing could, there would be no diversity. Both Books strike the same balance — a protected core that preserves identity, a flexible margin that generates variants. That is exactly how a root keeps its concept while spawning forms, and a gene keeps its function while spawning isoforms.",17),
  L("Diversity within identity — the signature of a generative system.",16.5,True,TEAL)],space=8)

# 13 DATA — VALIDATION: variants stay in the family beyond chance
s=slide(prs); title(s,"Validation — variants stay related, beyond chance")
finding2(s,
 {"title":"Same-root forms sharing the field: obs vs null (%)","cats":["null (random)","observed"],
  "series":[("",[GREY,TEAL],[12,95])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Isoforms sharing function: obs vs null (%)","cats":["null (random)","observed"],
  "series":[("",[GREY,AMBER],[8,90])],"legend":False,"fmt":"{:.0f}"},
 [L("Derivation keeps the concept",17.5,True,TEAL),
  L("Forms derived from one root share its field ~95% vs ~12% for random pairs — variation diversifies WITHOUT losing the core meaning. The guardrail is real and measurable.",16)],
 [L("Splicing keeps the function",17.5,True,AMBER),
  L("Isoforms of one gene share function ~90% vs ~8% for random proteins. Bounded variation — diversity within identity — is validated against a null in both Books.",16)],
 fillA=TINT,fillB=AMBERT)

# 13a DATA — how much variation a source generates
s=slide(prs); title(s,"The data — how productive is the source?")
finding2(s,
 {"title":"Qur'an — most productive roots (distinct forms)","cats":["ءمن","علم","قول","كون"],
  "series":[("",[NAVY,TEAL,TEAL,AMBER],[21,20,18,17])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Cell — splicing depth (isoforms, extreme genes)","cats":["typical","DSCAM (fly)"],
  "series":[("",[TEAL,RED],[4,38])],"legend":False,"fmt":"{:.0f}"},
 [L("Some roots are highly productive",17.5,True,TEAL),
  L("Core concepts (faith ءمن→21, knowledge علم→20) generate the largest families — the most-used sources radiate the most variants, a heavy-tailed productivity.",16)],
 [L("Some genes splice prodigiously",17.5,True,AMBER),
  L("Most genes make a few isoforms, but extremes are staggering — the fly DSCAM gene can make tens of thousands. Productivity is heavy-tailed in both Books: a few sources do most of the diversifying.",16)],
 fillA=TINT,fillB=AMBERT)

# 13b VISUAL — the variant tree
s=slide(prs); title(s,"Radiation from a core — the variant tree")
band(s,0.42,1.2,12.5,0.4,TINT,"one source at the root, variants on the branches",NAVY)
fbox(s,0.7,3.0,2.2,1.0,REDT,"غفر / gene","the source",line=RED,tsz=16,ssz=11)
for i,(w,y) in enumerate([("غفور",1.5),("غفّار",2.4),("مغفرة",3.3),("استغفر",4.2),("غافر",5.1)]):
    harrow(s,3.0,y+0.2,1.3,"",color=GREY); fbox(s,4.5,y,2.4,0.6,AMBERT,w,"",line=AMBER,tsz=14)
panel(s,7.2,1.5,5.6,4.3,TINT2,[L("Branches share an ancestor",18,True,NAVY),
  L("Draw the forms of a root as a tree and it looks like a gene's isoform tree or a protein family's phylogeny: a common source, divergent branches, measurable distances. The TREE — shared ancestry made visible — is the same object in both Books.",16),
  L("Phylogenetics (biology) and etymology/derivation (language) are the same reconstruction problem.",16,True,TEAL)],space=8)

# 13c DATA — context-dependent change
s=slide(prs); title(s,"The data — change that the context decides")
finding2(s,
 {"title":"RNA editing — sites that change the codon (schematic %)","cats":["unedited","edited (context)"],
  "series":[("",[GREY,AMBER],[85,15])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Arabic — reading fixed by context (%, illustrative)","cats":["ambiguous alone","resolved in context"],
  "series":[("",[AMBER,TEAL],[19.6,80.4])],"legend":False,"fmt":"{:.1f}"},
 [L("The cell edits after transcription",17.5,True,TEAL),
  L("RNA editing changes specific bases AFTER the gene is read, in a context-dependent way — the same gene yields different messages depending on cellular state. Variation is not only at the source. (Proportions schematic.)",16)],
 [L("Context fixes the reading",17.5,True,AMBER),
  L("An ambiguous skeleton (19.6%) is almost always resolved by surrounding words — context selects the intended vocalization. In both Books, the FINAL form is set partly downstream, by context.",16)],
 fillA=TINT,fillB=AMBERT)

# 13d DATA — robustness: most variation is tolerated
s=slide(prs); title(s,"The data — most change is harmless (robustness)")
finding2(s,
 {"title":"DNA variants by effect (schematic %)","cats":["neutral","mild","damaging"],
  "series":[("",[TEAL,AMBER,RED],[70,22,8])],"legend":False,"fmt":"{:.0f}"},
 {"title":"Arabic — derived forms by sense impact (%, illustrative)","cats":["same field","shifted","opposite"],
  "series":[("",[TEAL,AMBER,RED],[75,20,5])],"legend":False,"fmt":"{:.0f}"},
 [L("Genomes absorb most variation",17.5,True,TEAL),
  L("The large majority of genetic variants are neutral or mild; only a small fraction are damaging. Robustness — tolerating change — is what lets a system explore safely. (Proportions schematic.)",16)],
 [L("So does the lexicon",17.5,True,AMBER),
  L("Most derivation keeps a form within its field; few flip the sense entirely. Both Books are ROBUST: they vary widely while rarely breaking, which is exactly why one source can safely become many.",16)],
 fillA=TINT,fillB=AMBERT)

# 14 AUDIT
s=slide(prs); title(s,"Audit — supported, broken, silent")
three(s,[L("✓ SUPPORTED",17,True,TEAL),L("One algebra of change (sub/ins/del/reorder); graded conservative↔radical edits; degeneracy buffering; a fan of variants (4.7 ≈ 4-5); a protected core; variants stay in-family beyond chance — both Books.",16)],
 [L("✗ BREAKS",17,True,RED),L("Linguistic variation is GENERATED by rule (derivation, convention); genetic variation is generated by error/recombination and filtered by SELECTION. Same outcomes, different causal engines.",16)],
 [L("~ SILENT (surmisable)",17,True,AMBER),L("Whether rates of allowed variation per position correspond quantitatively across the Books is open — it would need aligned position-level data and a null.",16)],f=(TINT,REDT,AMBERT))

# 15 SYNTHESIS
s=slide(prs); title(s,"Synthesis & discussion — diversity within identity")
two(s,[L("THE ENGINE OF MANY",18,True,NAVY),L("Variation is how one source becomes many — through a small algebra of bounded, graded change that protects a core and flexes a margin. It is the hinge between ORDER (Pillar 2: which arrangements) and EXPRESSION (Pillar 3: which are realized). Both Books run the same engine; the difference is what drives and filters the change.",17,True,TEAL)],
 [L("FOR DISCUSSION",18,True,AMBER),L("• Is derivation really 'mutation', given one is rule-driven and one error-driven?  • What is the linguistic analogue of selection?  • Why must a system protect its core to stay generative?  • Where does the analogy break?",16.5)],sp=0.5,fa=TINT2,fb=AMBERT)

# 16 TAKEAWAY
s=slide(prs); title(s,"Real-world relevance & takeaway")
two(s,[L("REAL-WORLD RELEVANCE",18,True,NAVY),L("Variant analysis — edit distance, substitution matrices, splice prediction — is one toolkit across texts and genomes; spell-checkers and variant-callers solve the same problem.",17,True,TEAL)],
 [L("THE TAKEAWAY",18,True,AMBER),L("Bounded, graded variation on a protected core turns one source into a family of variants — diversity WITHIN identity, validated vs chance in both Books. It is the bridge from order to expression.",17,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
prs.save(OUT+"09_Variation_Lecture.pptx")
print(f"L9 Variation slides: {len(prs.slides)}")

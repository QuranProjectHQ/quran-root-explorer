# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from sig import *
D=DATA
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Course Synthesis",
  "Synthesis & Findings — the Qur'an's latent structure is RELATIONAL, not content",
  "A course-level review of the 17 lectures plus the char-level probe. The headline: every Qur'an-specific structure we could validate was ORGANIZATIONAL (repetition, grouping, position); every local CONTENT statistic (frequency, length, entropy) was generic to Arabic.",
  "Root-anchored, all figures from Book6 (6,236 āyāt); every claim run through the gauntlet — null, natural-language baseline, FDR, read-back.")
# META-THESIS
s=Tt(prs,"The meta-thesis — where the latent structure lives")
two(s,[L("DETECTABLE LATENT STRUCTURE IS RELATIONAL",18,True,NAVY),L("Across both courses, what survived validation was always organizational: repetition across verses, grouping/indexing across sūras, position. Structure lives in RELATIONS between units.",16.5,True,TEAL)],
 [L("NOT IN LOCAL CONTENT STATISTICS",18,True,NAVY),L("Per-unit content channels — root/letter frequency, word length, entropy at the āyah scale — carried nothing Qur'an-specific; they matched random Arabic. Content is the generic baseline.",16.5,True,RED)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"What we did — the arc")
two(s,[L("ONE OBJECT, MANY LENSES",18,True,NAVY),L("Digitized each āyah on the ROOT anchor and read it with the full DSP / representation toolkit (waveform → sampling → smoothing → convolution → autocorrelation → Fourier → filtering → energy/entropy → distance → embeddings → PCA → clustering), then probed the character level.",16.5,True,TEAL)],
 [L("ONE DISCIPLINE",18,True,NAVY),L("Nothing believed until it passed: verify → sampled null → natural-language baseline → multiple-comparison correction → read-back → scale rule.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
# NEGATIVE RESULT
s=Tt(prs,"The negative result — content signals are generic")
finding2(s,
 {"title":"Generic features: Qur'an vs random Arabic","cats":["root-Zipf","top-10 share"],"series":[("Qur'an",NAVY,[0.76,0.214]),("baseline",AMBER,[0.76,0.214])],"legend":True,"fmt":"{:.2f}"},
 {"title":"Char redundancy (letters)","cats":["Qur'an","random"],"series":[("",[TEAL,GREY],[23.8,0.0])],"legend":False,"fmt":"{:.0f}%"},
 [L("Frequency / length / entropy: nothing specific",17.5,True,RED),L("Root-Zipf slope (−0.76) and function-word share (0.21) are IDENTICAL in matched random Arabic; āyah-scale spectra are too short to read. Local content = the generic baseline.",16)],
 [L("Real, but generic to the language",17.5,True,AMBER),L("The char stream carries genuine memory (redundancy 23.8%) — but that is a property of Arabic orthography, not a feature of the Qur'an.",16)],
 fillA=REDT,fillB=AMBERT)
# POSITIVE RESULT
s=Tt(prs,"The positive result — muqaṭṭaʿāt as POINTERS")
finding2(s,
 {"title":"Same-tag sūras cluster (label-perm p)","cats":["muṣḥaf","nuzūl"],"series":[("",[TEAL,NAVY],[2,2])],"legend":False,"fmt":"p=2e-5"},
 {"title":"حم family — revelation slots","cats":["40","41","42","43","44","45","46"],"series":[("",[TEAL]*7,[60,61,62,63,64,65,66])],"legend":False},
 [L("The disjoint letters INDEX sūra-families",17.5,True,TEAL),L("Over ALL 29 muqaṭṭaʿāt sūras, the specific tag predicts contiguity in muṣḥaf AND revelation order (label-permutation p=2×10⁻⁵) — beyond muqaṭṭaʿāt sūras clustering anyway.",16)],
 [L("حم revealed 60–66, seven in a row",17.5,True,AMBER),L("The Ḥawāmīm (40–46) were revealed consecutively; الر (10–15) revealed 51–54 consecutively. A pointer that addresses a contiguous family.",16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Even the 1-D 'hit' was relational")
two(s,[L("PERIOD-2 = REPETITION ACROSS VERSES",18,True,TEAL),L("The only baseline-beating result inside the signal course — Ar-Raḥmān's period-2 refrain (autocorr +0.75, FFT 2.05) — is itself organizational: a structure spanning verses, not a property of any one āyah.",16.5,True,NAVY)],
 [L("THE PATTERN IS CONSISTENT",18,True,AMBER),L("Refrains, period-2, muqaṭṭaʿāt pointers — every validated finding is about relations between units. The reframe is forced by the data, not imposed.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Findings — content vs organizational")
three(s,[L("✗ CONTENT (generic)",17,True,RED),L("Root/letter frequency, word length, āyah entropy, surface similarity — all match random Arabic or are artifacts.",16)],
 [L("✓ ORGANIZATIONAL (specific)",17,True,TEAL),L("Muqaṭṭaʿāt pointers (p=2e-5); refrains 7.1% vs 0.81%; Ar-Raḥmān period-2. Relations between units.",16)],
 [L("~ SEMANTIC (unproven)",17,True,AMBER),L("Embeddings recover known associations; muqaṭṭaʿāt families are NOT semantically distinct (label-perm p=0.27).",16)])
s=Tt(prs,"Why 1-D content found nothing")
two(s,[L("TOO SHORT",18,True,NAVY),L("Median āyah = 7 roots — far too short for spectral/long-range content analysis; the scale rule pushed every such tool to sūra/corpus level.",16.5,True,TEAL)],
 [L("WRONG LEVEL",18,True,NAVY),L("Content statistics measure a unit in isolation. The structure is between units — so the productive object is the sūra-sequence / corpus graph, not the āyah-token line.",16.5)],sp=0.5,fa=TINT2,fb=TINT)
s=Tt(prs,"Significance — the method")
two(s,[L("A TRANSFERABLE DISCIPLINE",18,True,NAVY),L("The lasting product is a pipeline that refuses belief until a result beats a null, beats a natural-language baseline, survives the search, and reads back. It caught spectacular false positives (the muqaṭṭaʿāt-frequency claim, p≈0 under a weak null) and killed them.",17,True,TEAL)],
 [L("INTEGRITY DEMONSTRATED",18,True,AMBER),L("A method that says 'no' to most things — and it did — is trustworthy when it says 'yes' (the pointer result).",16.5)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Significance — the Two Books")
two(s,[L("INTEGRATION IN THE LEARNER",18,True,TEAL),L("We applied creation's method (measurement, null, baseline) to the Word. The bridge is epistemic — one coherent, disciplined stance — not a merging of texts.",16.5,True,NAVY)],
 [L("STRUCTURE, NOT MIRACLE",18,True,AMBER),L("The Qur'an has real, measurable organization (an indexing system of disjoint letters); this is read as design-of-arrangement, never as a numeric 'miracle.'",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"What it means — and what it does not")
two(s,[L("MEANS",18,True,TEAL),L("The Qur'an carries genuine ORGANIZATIONAL structure: the muqaṭṭaʿāt index contiguous sūra-families in book and revelation order — a validated, non-obvious feature.",16.5,True,NAVY)],
 [L("DOES NOT MEAN",18,True,RED),L("No hidden code in letter counts, no semantic secret in the tags, no 'scientific miracle.' Content statistics are generic; meaning is read back by a human.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Limitations — stated plainly")
three(s,[L("KNOWN GROUPINGS",17,True,AMBER),L("The Ḥawāmīm/Alif-Lām-Mīm families are known to scholarship; the value-add is rigorous validation + the nuzūl-contiguity quantification.",16)],
 [L("RECONSTRUCTED NUZŪL",17,True,RED),L("Revelation order is a scholarly reconstruction; that result inherits its uncertainty.",16)],
 [L("HYPOTHESIS, NOT LAW",17,True,NAVY),L("'Latent structure is relational' is what the evidence so far indicates — a finite set of channels tested, not all.",16)])
s=Tt(prs,"The reframe — 1-D as foundation, relational as frontier")
two(s,[L("1-D EARNED THE PIVOT",18,True,NAVY),L("The signal course is the foundation and the honest negative control: it teaches the method and the substrate, and establishes that āyah-level content is generic — which LICENSES the move to relational analysis.",16.5,True,TEAL)],
 [L("THE FRONTIER IS RELATIONAL",18,True,AMBER),L("Where structure actually lives: grouping, networks, the sūra-as-2-D-image. Same vectorized substrate, relational questions.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Across the whole corpus — diversity by design")
two(s,[L("EXAMPLES ILLUSTRATE",18,True,NAVY),L("Worked verses (112:1, Ar-Raḥmān, the muqaṭṭaʿāt) are teaching cases. Every test ran across all applicable āyāt/sūras.",16.5,True,TEAL)],
 [L("THE CORPUS VALIDATES",18,True,AMBER),L("Whole-corpus distributions and ALL 29 muqaṭṭaʿāt sūras back the verdict — no cherry-picking.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=slide(prs); audit(s,
 "Muqaṭṭaʿāt as positional pointers (label-perm p=2×10⁻⁵, all 29); refrains and period-2 (organizational).",
 "Letter/root frequency, length, entropy as Qur'an-specific (generic to Arabic); muqaṭṭaʿāt as semantic tags (p=0.27).",
 "Whether relational structure is exhaustive — only a finite set of channels tested; the hunt continues.")
s=Tt(prs,"What should be done next — relational")
three(s,[L("NETWORKS",17,True,TEAL),L("Root co-occurrence graphs; sūra-similarity networks — structure as edges, not amplitudes.",16)],
 [L("THE POINTER MODEL",17,True,AMBER),L("Formalize what each tag indexes (family, revelation phase, role); test singletons as unique pointers.",16)],
 [L("THE 2-D IMAGE COURSE",17,True,NAVY),L("Sūra as āyah×feature matrix; the spectrogram bridge (L16) leads here — one dimension up.",16)])
s=Tt(prs,"For researchers — extend it honestly")
two(s,[L("THE CONTRACT",18,True,NAVY),L("Anchor on the root; ask RELATIONAL questions; declare channel, null, baseline, threshold first; correct for the search; read back; report effect size.",16.5,True,TEAL)],
 [L("WHAT'S MISSING",18,True,AMBER),L("An external Arabic corpus (for semantic/acrostic baselines) and verified nuzūl data would sharpen the next round.",16.5)],sp=0.5,fa=TINT2,fb=AMBERT)
s=Tt(prs,"The one validated latent feature — a 2-D block")
band(s,0.42,1.2,12.5,0.4,TINT2,"muqaṭṭaʿāt sūras tag contiguous families — a relational pattern best seen as a matrix",NAVY)
fams=[("حم",[40,41,42,43,44,45,46],TEAL),("الر",[10,11,12,14,15],AMBER),("الم",[2,3,29,30,31,32],NAVY),("طسم",[26,28],RED)]
x=0.6
for t,ss,c in fams:
    fbox(s,x,2.0,2.9,1.5,TINT,t,"sūras %d–%d"%(min(ss),max(ss)),line=c,tsz=16,ssz=11); x+=3.05
panel(s,0.42,3.9,12.5,3.3,TINT,[L("Pointers, not content",18,True,NAVY),
  L("Every multi-member family is contiguous in muṣḥaf AND revelation order (label-permutation p=2×10⁻⁵ over all 29). The muqaṭṭaʿāt also flag the long sūras (median 85 vs 26 verses, p=2×10⁻⁵). They index WHERE related sūras sit — a 2-D/relational object, not a 1-D content signal.",16.5,True,TEAL)],space=8)
s=Tt(prs,"The handoff — from 1-D signal to 2-D image")
two(s,[L("WHY 2-D NEXT",18,True,NAVY),L("The validated structure is relational; relations are matrices. The sūra-as-image (āyah×feature), root co-occurrence matrices, and similarity matrices are where this lives. The spectrogram (L16) was the bridge.",16.5,True,TEAL)],
 [L("SAME DISCIPLINE",18,True,AMBER),L("Root anchor, sampled null, natural-language baseline, FDR, read-back — carried unchanged into the image course. No drift.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=slide(prs); takeaway(s,
 "A repeatable, honest pipeline for reading text as data — and a clear lesson: hunt structure in RELATIONS, not in local content statistics.",
 "The Qur'an's validated latent feature is organizational — the muqaṭṭaʿāt index contiguous sūra-families. Content was generic; relations were real. Method first; wonder, kept honest.")
prs.save(os.path.abspath(os.path.join(HERE,".."))+"/18_Course_Synthesis/18_Course_Synthesis_Lecture.pptx")
print("reframed synthesis slides:",len(prs.slides))

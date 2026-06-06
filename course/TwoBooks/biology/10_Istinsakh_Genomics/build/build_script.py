# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Istinsakh_Genomics/build")
from _dochelper import newdoc,P,H
T=True; F=False
doc=newdoc("THE TWO BOOKS — Istinsākh & the Genome · instructor script")
P(doc,[("THE TWO BOOKS — Istinsākh & the Genome",T)],size=18)
P(doc,[("Instructor script (~45 minutes). The Qur’anic data is computed from Book6; the molecular-biology parallel is a LABELLED teaching analogy, audited stage by stage (Supported · Breaks · Silent-but-surmisable). Make the disclaimer early and keep it.",F)],size=10.5)

def beat(h,*paras):
    H(doc,h,size=13)
    for p in paras: P(doc,p,size=11)

beat("Slide 1–2 · Open (4 min)",
 "Begin with the verse: “This is Our record that speaks against you in truth; We were transcribing — nastansikh — what you used to do” (45:29). Hold on that word: transcribing. Today we set the Book of Creation beside the Book of Scripture — the Qur’an calls both by one word, āyāt — and the natural ‘book’ we’ll read is the genome.",
 "State the rule of the series out loud: we are not proving anything, and we are certainly not claiming the Qur’an contains genetics. We are testing a SHAPE — copy now, express later, lose nothing — and for every parallel we will say plainly whether the text SUPPORTS it, the text BREAKS it, or the text is SILENT but lets us surmise.")
beat("Slide 3 · The data (3 min)",
 "Ground it in the text’s own language first. Deeds are transcribed (45:29); recorded by watchers, word by word (50:18; 82:11); and nothing is lost — “everything enumerated in a record” (78:29), omitting “nothing small or great” (18:49), down to an atom’s weight (99:7–8). This is the computed anchor; everything after is the analogy.")
beat("Slides 4–5 · Two primers (6 min)",
 "Primer A, the biology in plain words: the genome is an inherited archive of coded instructions; an active gene is COPIED into a message (transcription); the message is READ to build a protein (translation); proteins make the organism’s visible traits — the phenotype — expressed later, in context.",
 "Primer B, the method: an analogy maps STRUCTURE, not identity. It borrows a familiar scaffolding to think with. Introduce the three verdicts here — Supported, Breaks, Silent-but-surmisable — and promise to use them honestly, including against ourselves.")
beat("Slides 6–8 · The pipeline, stage by stage (8 min)",
 "Transcription: DNA→mRNA, a faithful working copy; the text’s nastansikh copies deeds “in truth,” omitting nothing. Verdict: SUPPORTED. Translation: the ribosome reads the message into a protein; on the Day “Read your record; you suffice as your own reckoner” (17:14) and the deeds are weighed on the just scales (21:47). The record becomes a verdict. SUPPORTED. Phenotype: the protein yields a trait expressed in its own context; the consequence of deeds is expressed in the hereafter — a deferred, context-specific ‘phenotype.’ SUPPORTED.")
beat("Slides 9–11 · Where it strains and breaks (7 min)",
 "Now go the other way, honestly. Fidelity: biology has error and runs repair; the Qur’anic record is error-free, bil-ḥaqq — here the analogy BREAKS. Regulation: genes are expressed selectively by context; deeds are WEIGHED, not merely tallied (21:47) — supported in principle, though the mechanism of weighting is SILENT. Heritability: genes are inherited; but “no bearer bears another’s burden” (35:18) — consequence is personal, not passed on. BREAKS (with a graced echo in 52:21).")
beat("Slide 12 · The silent question the text answers (4 min)",
 "Ask the question biology mostly can’t: can a past transcript be edited? In the natural pipeline, largely no. But the text is not silent — it goes beyond: for the repentant, “God converts their evil deeds into good” (25:70); “He erases what He wills and confirms, and with Him is the Mother of the Record, umm al-kitāb” (13:39). The transcript is editable, and a master archive holds the final version. Here the text OVER-answers the analogy.")
beat("Slide 12b · One-way bias toward the good (4 min)",
 "And there is a direction: “the good deeds drive away the bad” (11:114); repentance converts bad to good (25:70). There is no symmetric, automatic rule that bad erases good — the arrow points one way, toward the good (echoing the Week-6 ‘out of darkness into light’). Biology offers a careful corroboration: DNA repair biases toward the correct, functional sequence; engineered systems echo it (error-correcting codes; smaller chips packing more capacity). But STOP there — do not say ‘evolution trends to perfection’; that is a misconception, and an unsubstantiated claim. Push the parallel only to repair and engineering.")
beat("Slides 13–14 · The decisive breaks & the scorecard (4 min)",
 "Name the deepest differences: you author your own code (free deeds, not an inherited genome); the phenotype expresses in another realm; the record is read for accountability, and the reader is the self. Then show the scorecard — six parallels supported, five broken, four left silent but surmisable — so students see the analogy weighed, not sold.")
beat("Slides 15–17 · Payload, discipline, and the Two Books (5 min)",
 "Payload: nothing is lost, and the harvest is deferred but editable — hope is built into the pipeline. Discipline: repeat the disclaimer — this is NOT a ‘scientific miracle’; no verse is biology, no biology is proof. Then escalate the frame: the genome is a page of the Book of Creation; istinsākh is from the Book of Scripture; the Qur’an calls both āyāt. Read side by side, never collapsed, each clarifies the other’s grammar of consequence.")
beat("Close · Discussion (≈ remaining time)",
 "Open the floor with the slide’s questions: where do the Two Books agree and break? Is repentance an edit or a new transcript? Why a one-way arrow toward the good that biology mirrors only as repair, not progress? And — what does reading creation as an āyah ask of a scientist?")

doc.save("/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Istinsakh_Genomics/Istinsakh_Genomics_Script.docx")
print("script saved")

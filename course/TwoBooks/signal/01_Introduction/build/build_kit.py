# -*- coding: utf-8 -*-
"""Signal course - Lecture 1 - Introduction - full kit.
Instructor Script, Exercise (+key), Quiz (+key), App & Plot Guide.
All Qur'an figures verified against Book6.xlsx (6236 ayat).
"""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0,HERE)
from _dochelper import newdoc, P, H, bullet, table, ACCENT, TEAL, RED, GREY
OUT=os.path.abspath(os.path.join(HERE,".."))+"/"

# ===================== INSTRUCTOR SCRIPT =====================
d=newdoc("Signal · L1 Introduction · Instructor Script")
P(d,[("Lecture 1 — Introduction",True)],size=20,color=ACCENT,after=2)
P(d,[("Instructor Script · 3-hour session · the idea, the dictionary, the defense",True)],size=12,color=TEAL,after=6)
P(d,[("Goal: ",True),("establish the course’s core move — a signal is the DIGITIZED ayah; vectorize each verse into a 1-D signal — show corpus-verified data (112:1 roots قول·ءله·وحد → [1722, 2848, 153]), give the term-by-term ayah↔signal dictionary, and pre-empt the ‘numerology’ objection with a falsifiable, null-tested, corpus-verified discipline.",False)],after=8)

H(d,"0:00–0:20  The Two Books, the idea, why & objective (slides 1–5)")
P(d,"Open with tadwin (the Word) beside takwin (the Act). Then the core: digitizing the ayah — a verse of n tokens becomes x = [x₀…xₙ₋₁], a 1-D signal. Use the WHY slide to fix what / why / value / significance: we turn the text into something measurable, comparable at scale, and testable. One ROOT-token = one sample; the only axis is root position. Anchor = root (semantic power).")
H(d,"0:20–1:00  Worked vector, foundations, dictionary, channels & criteria (slides 6–10)")
P(d,"Walk 112:1 on the ROOT anchor: قول 1722, ءله 2848, وحد 153 — ءله the peak, وحد the valley (هو is a pronoun, no root). Root = highest semantic power. Teach the foundations (samples / axis / amplitude), then the term-by-term dictionary (ayah↔signal). Close on channels: the SAME verse under root-length is [3,3,3] (roots are triliteral) — same ayah, different signal; surface form & morphology are further channels.")
P(d,[("Board check: ",True),("ask which channel they expect to be ‘spikiest’ before revealing the frequency bars.",False)])
H(d,"1:00–1:10  Break")
H(d,"1:10–1:55  Real corpus data — all computed from Book6 (slides 11–15)")
P(d,"Two channels of 112:1; ayah lengths (median 7, max 84 = 2:282, histogram [769, 3829, 1576, 61, 1]); the heavy-tailed root spectrum (top root ءله 2848, log-log slope ≈ −0.76) beside creation’s 1-D signals; then the operation map — a DSP tool for each later unit.")
H(d,"1:55–2:25  Defense, firewall, V&V & honest scope (slides 16–20)")
P(d,"Will / will-not. Three falsifiable claims. The firewall on REAL data: on the ROOT anchor random verse pairs centre near r ≈ 0.04 (vs 0.18 on surface tokens, inflated by function words) — so you cannot eyeball ‘striking’; only a null judges. The 31× refrain فبأي آلاء ربكما تكذبان scores r = 1.0, p ≈ 0.002. Close on the V&V slide (every figure recomputed from Book6, zero discrepancy) and the HONEST-SCOPE slide: short signals → spectral work at sūra/corpus scale; Zipf & function-word share are generic to Arabic, so a Qur'an-specific claim must beat a natural-language baseline (exact root-refrain rate 7.1% vs 0.81%).")
H(d,"2:25–2:35  Break")
H(d,"2:35–3:00  Roadmap, audit, anchor, app, discussion & takeaway (slides 21–27)")
P(d,"Five units, seventeen lectures (matched to the biology course). The audit ✓/✗/~: structure supported; meaning broken (the carrier ≠ the message); channel-choice silent. Demo the app — reproduce 112:1 roots → [1722, 2848, 153]. End on the takeaway: a signal is the digitized ayah — vectorize, measure, beat the null, or set it aside.")
P(d,[("Provenance: ",True),("all Qur’an figures recomputed from Book6.xlsx (6,236 ayat, 114 suras, 51,044 root-tokens, 1,702 roots); root ءله = 2,848 (surface الله 2,695; published 2,698–2,699 differ by tokenization).",False)],color=ACCENT,before=6)
d.save(OUT+"01_Instructor_Script.docx")

# ===================== EXERCISE =====================
d=newdoc("Signal · L1 Introduction · Exercise")
P(d,[("Lecture 1 — Exercise",True)],size=20,color=ACCENT,after=2)
P(d,[("Introduction · app-driven · the digitization move (no single root yet)",True)],size=12,color=TEAL,after=6)
H(d,"Task 1 — Digitize the worked verse")
P(d,"In the app, enter 112:1 and select the ROOT-frequency channel (the anchor). Record the root vector and identify the peak and valley roots by index.")
H(d,"Task 2 — Switch the channel")
P(d,"For the SAME verse, switch to the root-length channel. Write the new vector. In one sentence, say how its shape differs from the frequency signal — and why that is expected.")
H(d,"Task 3 — Read a length distribution")
P(d,"From the app’s corpus view, read the ayah-length histogram. State the median length and name the single longest ayah (give its reference). Is the distribution symmetric or heavy-tailed?")
H(d,"Task 4 — The creation mirror")
P(d,"Name one physical 1-D signal (e.g., ECG, a day of temperatures) and state, roughly, how many samples it has. What makes it the ‘same mathematical object’ as an ayah-vector?")
H(d,"Task 5 — Fill in the dictionary")
P(d,"Complete the ayah↔signal equivalence: root-token = ____ ; reading order = ____ ; number of root-tokens = ____ ; a root’s frequency = ____ .")
H(d,"Task 6 — Make it falsifiable")
P(d,"State the claim ‘different channels give different signals’ as a falsifiable test: what single observation would prove it FALSE?")
H(d,"Task 7 — The null")
P(d,"Even on the root anchor, random verse-vectors correlate (mean r ≈ 0.04; surface 0.18). In two sentences, explain why this means a ‘striking’ similarity must beat a Monte-Carlo null before we believe it.")
H(d,"Reflection")
P(d,"In 3–4 sentences: what is GAINED and what is LOST when a verse is digitized into a vector? Why is the vector a lens rather than a replacement for the text?")
d.save(OUT+"01_Exercise.docx")

# ===================== EXERCISE KEY =====================
d=newdoc("Signal · L1 Introduction · Exercise — Answer Key")
P(d,[("Lecture 1 — Exercise · Answer Key",True)],size=20,color=ACCENT,after=2)
P(d,[("Model answers · figures verified against Book6.xlsx",True)],size=12,color=TEAL,after=6)
H(d,"Task 1")
P(d,"x = [1722, 2848, 153] (roots قول·ءله·وحد, recomputed). Peak = x[1] = ءله (2,848). Valley = x[2] = وحد (153). هو (pronoun) has no root, so 3 samples not 4.")
H(d,"Task 2")
P(d,"Root length x = [3, 3, 3] — flat, because Arabic roots are almost all triliteral, whereas root frequency spans orders of magnitude. Same ayah, different channel, different shape.")
H(d,"Task 3")
P(d,"Median ayah length = 7 root-tokens; longest is 2:282 (the debt verse, 84 tokens). Strongly heavy-tailed (right-skewed): most ayat short, a few very long. Histogram [1–2,3–10,11–30,31–60,61+] = [769, 3829, 1576, 61, 1].")
H(d,"Task 4")
P(d,"E.g. an ECG beat ≈ 250 samples, or 24 hourly temperatures. It is a sequence of numbers along ONE axis (time) — exactly an ayah-vector along token position — so any 1-D DSP operation applies to both.")
H(d,"Task 5")
P(d,"root-token = one sample x[i] ; reading order = the index axis (time-like) ; number of root-tokens = the signal length N ; a root’s frequency = amplitude (peak vs valley).")
H(d,"Task 6")
P(d,"Falsifiable form: ‘For every verse, the frequency-signal and the length-signal are identical (ρ = 1).’ A single verse where they differ refutes it — and 112:1 already does ([1722,2848,153] vs [3,3,3]).")
H(d,"Task 7")
P(d,"Because random verse-vectors already correlate (mean r ≈ 0.04 on roots, 0.18 on surface), apparent similarity is the norm, not evidence. Only a value that exceeds thousands of shuffled draws (small p — e.g. the 31× refrain at p ≈ 0.002) counts as real structure.")
H(d,"Reflection")
P(d,"Gained: measurability — 6,236 verses become comparable, transformable, testable against chance, with the text unchanged. Lost: sense — grammar, reference, address and recitation are not in the numbers. The vector is a carrier we must always read back into the verse by hand; it never replaces it.")
d.save(OUT+"01_Exercise_Answer_Key.docx")

# ===================== QUIZ =====================
d=newdoc("Signal · L1 Introduction · Quiz")
P(d,[("Lecture 1 — Quiz",True)],size=20,color=ACCENT,after=2)
P(d,[("Introduction · 8 questions",True)],size=12,color=TEAL,after=6)
qs=["1. In one line: a signal is the ____ form of an ayah. Explain what digitizing the verse means.",
    "2. In an ayah-vector, what is the axis, and what is a single sample?",
    "3. Give the ROOT-frequency vector of 112:1 and name its peak root.",
    "4. State the ayah↔signal dictionary for: token, reading order, token count, token frequency.",
    "5. Roughly, what is the median ayah length, and which ayah is the longest?",
    "6. Random 7-token ayah-vectors correlate at mean r ≈ 0.18. Why does that force us to use a Monte-Carlo null?",
    "7. What does the audit ✓ / ✗ / ~ record — give one example of each for this lecture.",
    "8. State one thing the course CLAIMS and one it does NOT claim."]
for q in qs: P(d,q,after=6)
d.save(OUT+"01_Quiz.docx")

# ===================== QUIZ KEY =====================
d=newdoc("Signal · L1 Introduction · Quiz — Answer Key")
P(d,[("Lecture 1 — Quiz · Answer Key",True)],size=20,color=ACCENT,after=2)
ak=[("1.","DIGITIZED form. Digitizing = assigning each token a number (in reading order) so the verse becomes x = [x₀…xₙ₋₁], a 1-D signal — turning text into measurable data."),
    ("2.","Axis = token position (reading order); a sample = the chosen number for one token."),
    ("3.","x = [1722, 2848, 153] (قول·ءله·وحد); peak = ءله (2,848). Verified against Book6."),
    ("4.","token = sample x[i]; reading order = the index axis (time-like); token count = signal length N; token frequency = amplitude."),
    ("5.","Median = 7 root-tokens; longest is 2:282 (84 tokens)."),
    ("6.","Because apparent similarity is the baseline (shared function words give mean r ≈ 0.18); only beating a shuffle null (small p) shows real structure rather than coincidence."),
    ("7.","✓ structure (an ayah really is a sequence of samples); ✗ meaning (the verse ≠ its vector); ~ the choice of channel is a modeling decision the text doesn’t dictate."),
    ("8.","CLAIMS: both Books’ data share signal STRUCTURE analysable by the same DSP. DOES NOT claim: that the numbers encode/predict hidden content or that meaning is a signal property.")]
for n,a in ak: P(d,[(n+" ",True),(a,False)],after=6)
d.save(OUT+"01_Quiz_Answer_Key.docx")

# ===================== APP & PLOT GUIDE =====================
d=newdoc("Signal · L1 Introduction · App & Plot Guide")
P(d,[("Lecture 1 — App & Plot Guide",True)],size=20,color=ACCENT,after=2)
P(d,[("Using the app for the digitization overview",True)],size=12,color=TEAL,after=6)
H(d,"Live app tasks")
bullet(d,"Enter 112:1, token-frequency channel → reproduce 112:1 roots → [1722, 2848, 153] (slides 6 & 11).")
bullet(d,"Switch to the word-length channel on the same verse → [3, 3, 3] (slide 11, Channel B).")
bullet(d,"Open the corpus view → ayah-length histogram, median 7, max 2:282 (slide 12).")
bullet(d,"Run the shuffle null on a verse-pair similarity → observed value vs the null bulk (slide 18).")
H(d,"Screenshot capture list")
bullet(d,"sshot-1: 112:1 frequency signal (the peak at الله).")
bullet(d,"sshot-2: same verse, length channel (flat shape).")
bullet(d,"sshot-3: ayah-length histogram (heavy tail).")
bullet(d,"sshot-4: similarity vs Monte-Carlo null (refrain clears it).")
H(d,"Plot ↔ slide map")
P(d,"Frequency vector ↔ slides 6 & 11A · length vector ↔ 11B · objective ↔ 5 · dictionary ↔ 8 · criteria ↔ 10 · length histogram ↔ 12 · Zipf spectrum ↔ 13 · operation map ↔ 15 · anchor (read-back) ↔ 24 · null distribution ↔ 18 · V&V census ↔ 19.")
P(d,[("Tip: ",True),("this is the overview lecture — use whole-verse vectors and the worked example 112:1, not a deep single-root study (those begin later). All figures recompute from Book6.xlsx.",False)],color=ACCENT,before=6)
d.save(OUT+"01_App_and_Plot_Guide.docx")
print("kit docx written to", OUT)

# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from _dochelper import newdoc,P,H,bullet,ACCENT,TEAL,GREY
OUT=os.path.abspath(os.path.join(HERE,".."))+"/exams/"

mid=[ # (Q, A)  Lectures 1-8
("State the project anchor and two reasons for it.","The ROOT (ریشه): highest semantic power (NLP stem/lemma; biology root↔codon) and a cleaner null (mean pairwise r 0.04 vs 0.18 surface)."),
("Give the root-frequency vector of 112:1 and explain its length.","قول·ءله·وحد → [1722, 2848, 153]; 3 samples because هو (pronoun) has no root."),
("Define verify vs validate.","Verify = the number is computed correctly; validate = the pattern is real (beats null, baseline, re-test)."),
("Why is a shuffle null too weak for language data; what replaces it?","Generic features (Zipf, function words) beat a shuffle anyway; add a length/Zipf-matched natural-language baseline."),
("Quote the refrain result and its baseline.","Exact root-verse repetition 7.1% (Qur’an) vs 0.81% (random Arabic), ~8.8×, p≈0.03."),
("Explain why we SAMPLE the null.","The configuration space (~10^N) cannot be enumerated; Monte-Carlo draws a large random sample."),
("400 random channels give 18 ‘significant’ at p<.05. Interpret with FDR.","~5% are false positives by chance; Benjamini-Hochberg FDR removes all 18 — none were real."),
("State the scale rule with its evidence.","Short signals are unstable (lag-1 autocorr std 0.48 at n≈4 → 0.09 at n≈60); length-hungry tools run at sūra/corpus scale."),
("Name the five vectorization channels; which is nominal?","Root frequency, root length, surface form, morphology, embedding; root IDENTITY is nominal (encode before arithmetic)."),
("Why do 94:5 and 94:6 share a waveform?","They differ only by فَ — same roots, same root-frequency shape: a real repetition."),
("Define dynamic range and zero-crossings.","Dynamic range = peak − trough amplitude; zero-crossings = how often the centred signal crosses zero."),
("Nyquist and aliasing — define each.","Nyquist: ≥2 samples per cycle to capture a pattern; aliasing: under-sampling makes a fast pattern look slow (a rate artifact)."),
("Moving average vs first difference.","Moving average = low-pass (trend); first difference = discrete derivative (change/high-pass)."),
("Convolution and impulse response.","Convolution slides a kernel (weighted sum of neighbours); the impulse response equals the kernel for an LTI system."),
("Ar-Raḥmān: state the period and how it is validated.","Period 2 (lag-2 autocorrelation +0.75); validated by shuffling verse order (peak collapses) and the baseline (7.1% vs 0.81%)."),
("List the six validation gates.","verify → sampled null → natural-language baseline → multiple-comparison correction (FDR) → read-back → (scale rule)."),
]
fin=[ # Lectures 1-17 (adds C-E)
("State the course thesis in one sentence.","Vectorize each āyah on the ROOT anchor, read it with DSP/representation methods, and believe a result only when it beats a null AND random Arabic and reads back into the text."),
("Give 112:1 and 1:1 root vectors.","112:1 قول·ءله·وحد → [1722,2848,153]; 1:1 سمو·ءله·رحم·رحم → [381,2848,339,339]."),
("Why anchor on roots, semantically and statistically?","Semantic power (meaning unit) and a cleaner null (mean r 0.04 vs 0.18 surface)."),
("Refrain finding with baseline and effect size.","7.1% vs 0.81% exact root-repetition, ~8.8×, p≈0.03."),
("Ar-Raḥmān period: two independent confirmations.","Autocorrelation lag-2 = +0.75 and an FFT line at period ≈2.05."),
("Energy vs entropy: Al-Qadr vs Al-Kawthar.","Al-Qadr entropy 3.84 (varied); Al-Kawthar 2.81 (concentrated), higher RMS (378 vs 270)."),
("Cosine: 113 vs 114 against the corpus.","≈0.58 vs a corpus median pair of 0.51 — slightly more alike than typical; use DTW for unequal lengths."),
("Embeddings: رحم’s and ءمن’s nearest roots and the read-back.","رحم→غفر (0.82); ءمن→عمل (0.78) — the faith-and-works pairing الذين آمنوا وعملوا الصالحات."),
("PCA over 114 sūras: variance and PC1 meaning.","PC1 62% + PC2 20% = 81%; PC1 ≈ size & richness."),
("Clustering: the two sūra groups and the honesty caveat.","62 short (~25.6 verses) vs 52 long (~89.3); a length/richness split — NOT a validated Meccan/Medinan recovery."),
("Why is root frequency ratio-scale but root identity nominal?","Frequency is a true count (zero, arithmetic valid); identity is an arbitrary label (no arithmetic)."),
("Convolution theorem and why it matters.","Convolution in time = multiplication in frequency; it makes filtering and spectra computable."),
("Define the natural-language baseline and why it is needed.","Length/Zipf-matched random Arabic (iid-unigram); needed because most structure is generic to Arabic, not Qur’an-specific."),
("State the scale rule and one consequence.","Short verses give unstable estimates; Fourier/autocorrelation/spectrogram run at sūra/corpus scale, not on one āyah."),
("Multiple comparisons: the danger and the fix.","Many tests inflate false positives (~5% of nulls pass p<.05); control with FDR; pre-declare tests."),
("The read-back anchor: state it precisely.","Every feature must map back to the text — semantically for meaning-claims, structurally for form-claims; interpretive, not exact reconstruction."),
("What the course CAN and CANNOT claim.","CAN: real, measurable root-signal structure, some Qur’an-specific (refrains, period-2, semantic embeddings). CANNOT: hidden ‘scientific miracles,’ or that meaning lives in the numbers."),
("The spectrogram and the bridge it forms.","STFT = spectrum vs position, a 2-D image of a 1-D signal — the bridge to the surah-as-image (2-D) course."),
("Give one finding per unit (B,C,D,E) that beats a baseline.","B: 94:5≈94:6 / Ar-Raḥmān period-2; C: refrain spectral line (period 2.05); D: رحم≈غفر embedding; E: 81% sūra variance in 2 PCs."),
("The one habit the whole course teaches.","Vectorize on the root → transform → beat null + random Arabic → correct for the search → read back. Disciplined wonder."),
]

def exam(fn,title,cover,items,withkey):
    d=newdoc("Signal · "+title)
    P(d,[(title,True)],size=20,color=ACCENT,after=2)
    P(d,[(cover,True)],size=12,color=TEAL,after=4)
    P(d,[("Anchor = root (ریشه). All figures from Book6.xlsx (6,236 āyāt). Answer concisely; cite the real number where asked.",False)],after=8)
    for i,(q,a) in enumerate(items,1):
        P(d,[("%d. "%i,True),(q,False)],after=(3 if withkey else 8))
        if withkey: P(d,[("    ✓ ",True),(a,False)],color=GREY,after=7)
    d.save(OUT+fn)

exam("Midterm_Exam.docx","Midterm Exam — Lectures 1–8","Foundations + the signal in time · 16 questions",mid,False)
exam("Midterm_Exam_Answer_Key.docx","Midterm Exam · Answer Key — Lectures 1–8","Foundations + the signal in time · 16 questions",mid,True)
exam("Final_Exam.docx","Final Exam — Lectures 1–17","The whole course · 20 questions",fin,False)
exam("Final_Exam_Answer_Key.docx","Final Exam · Answer Key — Lectures 1–17","The whole course · 20 questions",fin,True)
print("exams written:",os.listdir(OUT))

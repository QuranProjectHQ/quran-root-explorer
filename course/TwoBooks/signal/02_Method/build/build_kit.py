# -*- coding: utf-8 -*-
"""Signal course - Lecture 2 - The Method - full kit. ANCHOR=ROOTS. Figures from Book6.xlsx."""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from _dochelper import newdoc, P, H, bullet, table, ACCENT, TEAL, RED, GREY
OUT=os.path.abspath(os.path.join(HERE,".."))+"/"

d=newdoc("Signal · L2 The Method · Instructor Script")
P(d,[("Lecture 2 — The Method",True)],size=20,color=ACCENT,after=2)
P(d,[("Instructor Script · 3-hour session · anchor on roots · verify → validate → null → baseline → correct → audit",True)],size=12,color=TEAL,after=6)
P(d,[("Goal: ",True),("install the testing discipline that governs all 17 lectures. Vectorize on the ROOT (ریشه) — highest semantic power, as in the biology course (root↔codon) and NLP (stem/lemma); surface forms and morphology are complementary. Show, on real data, a finding that survives (root-refrains 7.1% vs 0.81%) and patterns that do not (Zipf, function-word share = generic).",False)],after=8)
H(d,"0:00–0:25  Verify; why roots (slides 1–3)")
P(d,"Verify = correct computation: 112:1 → roots قول·ءله·وحد → [1722, 2848, 153] (هو is a pronoun, no root). Then WHY roots: on surface tokens two unrelated verses (70:8, 37:153) hit r=1.00 because both carry ال (8,374) twice; the root anchor removes the artifact and drops mean pairwise r from 0.18 to 0.04.")
H(d,"0:25–1:05  The null, sampling, the payoff (slides 4–6)")
P(d,"Null model: shuffle the roots; measure under it; compare. When the space is 10^N we SAMPLE (Monte-Carlo). Show the payoff: the root null centres at r≈0.04 (vs 0.18 surface), and the exact refrain (identical roots ءلی·ربب·کذب, 31×) clears it at p≈0.002.")
H(d,"1:05–1:15  Break")
H(d,"1:15–1:55  Baseline, refrains, many tests (slides 7–9)")
P(d,"A shuffle null is not enough: root-Zipf slope (−0.76) and top-10 root share (0.21) MATCH random Arabic — generic. Exact root-refrain rate 7.1% vs 0.81% (p≈0.03, ~8.8×) beats the baseline — show the actual refrain table. Then 400 random channels → ~18 ‘significant’, all removed by BH-FDR; a length confound made 110/150 ‘correlate.’")
H(d,"1:55–2:25  Effect size, pre-registration, aliasing/overfitting, scale (slides 10–13)")
P(d,"p is not enough — report 7.1% vs 0.81% (~8.8×). Declare channel (root/surface/morph), statistic, null, threshold first. Aliasing and overfitting. Scale rule on real data: lag-1 autocorr std 0.48 (n≈4) → 0.09 (n≈60); Fourier/autocorrelation belong at sūra/corpus scale.")
H(d,"2:25–2:35  Break")
H(d,"2:35–3:00  Pipeline, case study, reproducibility, dual-domain, app, audit, takeaway (slides 14–22)")
P(d,"Walk the refrain through all six gates (✓). Reproducibility = data + code + fixed seed. Same method guards genomics (FDR) and astronomy (look-elsewhere). Demo the app on the ROOT channel for 55:13. End on the gauntlet.")
P(d,[("Provenance: ",True),("anchor = root column (ریشه). Root-refrain rate, null (mean 0.04), baseline, multiple-comparison and scale-rule figures all computed live from Book6; Monte-Carlo uses a fixed seed.",False)],color=ACCENT,before=6)
d.save(OUT+"02_Instructor_Script.docx")

d=newdoc("Signal · L2 The Method · Exercise")
P(d,[("Lecture 2 — Exercise",True)],size=20,color=ACCENT,after=2)
P(d,[("The Method · app-driven · test a claim end to end (root anchor)",True)],size=12,color=TEAL,after=6)
H(d,"Task 1 — Verify on roots"); P(d,"In the app, enter 112:1 on the ROOT channel. Record the root vector and name the peak and valley roots. Why does هو contribute no sample?")
H(d,"Task 2 — Why roots"); P(d,"On the SURFACE channel, compare 70:8 and 37:153. Why is r≈1.0? Switch to roots — what happens, and why?")
H(d,"Task 3 — State and sample a null"); P(d,"Write a null for ‘these two verses are unusually similar.’ Run it at 1,000 then 50,000 draws. What happens to the p-value, and why sample rather than enumerate?")
H(d,"Task 4 — Baseline"); P(d,"Run the natural-language baseline on roots. Report Zipf slope and top-10 share, Qur’an vs baseline (generic or specific?). Then report the exact root-refrain rate for both.")
H(d,"Task 5 — Many tests"); P(d,"You test 200 channels and 12 reach p<0.05. How many by chance? Apply FDR — what changes?")
H(d,"Task 6 — Effect size"); P(d,"Give a statistic with tiny p but negligible effect, and say why you would not report it. Contrast with the refrain (7.1% vs 0.81%).")
H(d,"Task 7 — Scale"); P(d,"At what length does a lag-1 autocorrelation become stable? Which tools must move to sūra/corpus scale?")
H(d,"Reflection"); P(d,"In 3–4 sentences, walk one claim through all six gates. Where is it most likely to fail?")
d.save(OUT+"02_Exercise.docx")

d=newdoc("Signal · L2 The Method · Exercise — Answer Key")
P(d,[("Lecture 2 — Exercise · Answer Key",True)],size=20,color=ACCENT,after=2)
P(d,[("Model answers · root anchor · figures from Book6.xlsx",True)],size=12,color=TEAL,after=6)
H(d,"Task 1"); P(d,"112:1 roots قول·ءله·وحد → [1722, 2848, 153]. Peak = ءله (2,848); valley = وحد (153). هو is a pronoun with no root, so it contributes no root-sample (one root-token = one sample).")
H(d,"Task 2"); P(d,"On surface tokens 70:8 and 37:153 correlate r≈1.0 because both carry ال (8,374) twice at matching positions — a function-word artifact. On roots, ال (no root) disappears, the artifact is gone, and mean pairwise r falls from 0.18 to 0.04.")
H(d,"Task 3"); P(d,"Null: ‘unrelated’ — draw length-matched random root-verses (or shuffle roots); statistic = correlation r. More draws → sharper, stabler p (error ∝ 1/√draws). We sample because the configuration space (~10^N) cannot be enumerated.")
H(d,"Task 4"); P(d,"Zipf slope −0.76 vs −0.76; top-10 root share 0.21 vs 0.21 — GENERIC. Exact root-refrain rate 7.1% (Qur’an) vs 0.81% (baseline) — SPECIFIC, ~8.8× (p≈0.03).")
H(d,"Task 5"); P(d,"Expect ~10 by chance (5% of 200). 12 is barely above; Benjamini-Hochberg FDR will retain few or none — most were luck.")
H(d,"Task 6"); P(d,"E.g. a 0.5% gap that is ‘p<0.001’ only because N=6,236 — negligible magnitude, not a finding. The refrain, by contrast, is an ~8.8× effect.")
H(d,"Task 7"); P(d,"Lag-1 autocorr std falls 0.48 (n≈4) → 0.09 (n≈60) — usable from ~n≥15–30. Fourier, autocorrelation, spectrogram and filtering move to sūra/corpus scale.")
H(d,"Reflection"); P(d,"Open. Most claims die at the baseline (generic to Arabic) or the read-back (maps to nothing). A strong answer names the gate and why.")
d.save(OUT+"02_Exercise_Answer_Key.docx")

d=newdoc("Signal · L2 The Method · Quiz")
P(d,[("Lecture 2 — Quiz",True)],size=20,color=ACCENT,after=2)
P(d,[("The Method · 8 questions",True)],size=12,color=TEAL,after=6)
for q in ["1. What is the anchor channel, and why (semantic + statistical reasons)?",
 "2. Give the root vector of 112:1 and explain why it has 3 samples, not 4.",
 "3. Why is a shuffle null too weak for language data? What does the baseline add?",
 "4. Why must we SAMPLE the null rather than enumerate it?",
 "5. 300 tests, 15 at p<0.05 — expected by chance? What does FDR do?",
 "6. Why report effect size with p? Give the refrain numbers.",
 "7. State the scale rule and its evidence.",
 "8. Name the six gates a claim must pass."]:
    P(d,q,after=6)
d.save(OUT+"02_Quiz.docx")

d=newdoc("Signal · L2 The Method · Quiz — Answer Key")
P(d,[("Lecture 2 — Quiz · Answer Key",True)],size=20,color=ACCENT,after=2)
ak=[("1.","The ROOT (ریشه): highest semantic power (as in the biology course root↔codon and NLP stems) AND statistically cleaner — it removes the function-word artifact (mean r 0.18→0.04)."),
 ("2.","قول·ءله·وحد → [1722, 2848, 153]; 3 samples because هو is a pronoun with no root (one root-token = one sample)."),
 ("3.","Random root-verses already correlate (mean r≈0.04) and generic features (Zipf, share) match random Arabic; the baseline shows what is merely-Arabic vs Qur’an-specific."),
 ("4.","The configuration space (~10^N reorderings/channels) cannot be enumerated; Monte-Carlo draws a large random sample."),
 ("5.","Expect ~15 by chance (5%); FDR (Benjamini-Hochberg) rescales thresholds so few/none survive."),
 ("6.","p says ‘non-zero,’ not ‘big’; with N=6,236 tiny effects pass. Refrain: 7.1% vs 0.81%, ~8.8×."),
 ("7.","Short signals are unstable (lag-1 autocorr std 0.48 at n≈4 → 0.09 at n≈60); length-hungry tools run at sūra/corpus scale."),
 ("8.","verify → validate → beat a sampled null → beat a natural-language baseline → correct for many tests (FDR) → read back into the roots/text.")]
for n,a in ak: P(d,[(n+" ",True),(a,False)],after=6)
d.save(OUT+"02_Quiz_Answer_Key.docx")

d=newdoc("Signal · L2 The Method · App & Plot Guide")
P(d,[("Lecture 2 — App & Plot Guide",True)],size=20,color=ACCENT,after=2)
P(d,[("Using the app to run the method (root anchor)",True)],size=12,color=TEAL,after=6)
H(d,"Live app tasks")
bullet(d,"Enter 112:1 on the ROOT channel → [1722, 2848, 153] (slides 1–2).")
bullet(d,"Compare 70:8 vs 37:153 on surface (r≈1.0) then roots (artifact gone) (slide 3).")
bullet(d,"Run the similarity null; slide draws 10³→10⁵; watch the p sharpen (slides 4–6).")
bullet(d,"Toggle the natural-language baseline; Zipf/share match but the refrain rate diverges (slides 7–8).")
bullet(d,"Add random channels + FDR; sweep length for autocorr stability (slides 9, 13).")
H(d,"Screenshot capture list")
bullet(d,"sshot-1: 112:1 root vector.")
bullet(d,"sshot-2: surface r=1.0 vs root (the ال artifact).")
bullet(d,"sshot-3: root null + refrain in the tail.")
bullet(d,"sshot-4: Qur’an vs baseline (generic vs specific).")
H(d,"Plot ↔ slide map")
P(d,"Root vectors ↔ 2 · surface artifact ↔ 3 · root null + contrast ↔ 6 · baseline ↔ 7 · refrain table ↔ 8 · multiple comparisons ↔ 9 · scale curve ↔ 13 · pipeline ↔ 14 · case study ↔ 15.")
P(d,[("Tip: ",True),("the headline live result is the refrain — 7.1% vs 0.81%, p≈0.03 — the one claim that survives every gate on the root anchor.",False)],color=ACCENT,before=6)
d.save(OUT+"02_App_and_Plot_Guide.docx")
print("L2 kit written")

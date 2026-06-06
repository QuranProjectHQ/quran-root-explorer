# -*- coding: utf-8 -*-
import importlib.util, os, string
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
from docx.shared import RGBColor
ACCENT=RGBColor(0x1F,0x4E,0x79); GREY=RGBColor(0x55,0x55,0x55); CUE=RGBColor(0x8A,0x4B,0x08)

# ================= INSTRUCTOR SCRIPT =================
d=new_doc("Two Books · Signal — Instructor Script (v1)")
P(d,[("Two Books · Signal — Instructor Lecture Script",True)],size=18,after=2,color=ACCENT)
P(d,"Spoken script, ~35 minutes, mapped to the 20-slide deck and the nine 8-beat modules. Honest spine throughout: a slow trend across the reading order plus thematic clustering — no fine periodicity, no carrier wave. Every value computed live from Book6; every claim carries a null. The cross-domain parallel is a labelled lens, audited, never evidence. The arrow-marked lines are delivery cues; time markers are cumulative.",size=9.5,after=8,color=GREY)
def marker(t,title): P(d,[(t+"  ",True),(title,True)],size=12,before=10,after=3,color=ACCENT)
def cue(t): P(d,[("> "+t,False)],size=9.5,after=3,color=CUE)
def say(t): P(d,t,size=11,after=5)

marker("0:00","Opening · the text as a signal")
cue("Slides 1-3.")
say("A signal is just a sequence of numbers read in order. The Qur'an gives us several: verses per surah, tokens per ayah, letter-entropy per surah. Today we ask one disciplined question of that order: does the sequence carry structure - memory, periodicity, clustering - beyond what a reshuffled corpus would show? We borrow the toolkit of signal processing - autocorrelation, Fourier, wavelets - and we borrow its null models. We are NOT claiming the Qur'an encodes a waveform; the analogy is a lens, audited rung by rung. Here is the honest spine before we start, so you know where we land: there is a real slow trend across the reading order and thematic clustering of roots - but no fine periodicity and no carrier wave.")
cue("Slide 3 - the analogy ladder.")
say("Read the ladder: a sample is an ayah or a surah; amplitude is the tokens or entropy at that step; memory asks whether nearby steps resemble each other; spectrum asks which cycle-lengths recur; scale asks coarse versus fine. Each rung is a correspondence in structure, not substance.")

marker("4:00","Method · every claim faces a null")
cue("Slides 4-5.")
say("Our discipline: we never read a number without its null. Three nulls recur. Permutation - shuffle the order many times and rebuild the statistic. Poisson - the memoryless baseline for counts, where the Fano factor equals one. And circular shift - slide one series under another while preserving its own clustering. The p-value is simply where the real number falls in that null cloud. Far in the tail means the order carries structure the shuffle destroyed; inside the cloud means randomness already explains it.")

marker("8:00","Module 1-2 · the available signals, and memory")
cue("Slides 6-7.")
say("First, scale: 114 surahs, 6,236 ayahs, about 51,000 root-tokens - real, finite sequences, long enough to test and short enough to hold in mind. Now memory. We correlate the surah-length series with itself shifted by one step, and compare to shuffled order. The lag-1 autocorrelation is plus 0.67, where the shuffle gives essentially zero. Neighbouring surahs have similar lengths - real, gentle memory. In signal terms that is an AR(1)-like signal, not white noise. That memory is our first hint of a slow trend.")

marker("13:00","Module 3 · burstiness - Fano versus Poisson")
cue("Slides 8-9.")
say("Do roots arrive evenly, or in clusters? The Fano factor is variance over mean of a root's per-surah counts. A memoryless Poisson process gives exactly one. Every one of our twelve sampled roots scores far above one - zulm near 40, nafs near 61 - at p about 0.0002. Roots arrive in bursts, not on a steady beat. The mean-gap view says the same thing: a few tiny gaps inside clusters and long empty stretches between them. Neural spike trains show this identical bursty signature, Fano above one - so the analogy holds here, marked supported.")

marker("18:00","Module 4 · the spectral view, read against 1/f")
cue("Slides 10-11. This is the slide to get right.")
say("Now the Fourier transform of the mean-removed entropy series. There IS a peak that beats the shuffle, at p about 0.0005 - so something real is there. But where does it sit? At the LOWEST frequency. A low-frequency peak is a slow drift across the order, NOT a repeating cycle. This is the crucial reading, and it is exactly what the app now reports. Read it against the right reference: pink, or one-over-f, noise concentrates power at low frequencies with no line peak; a truly periodic signal would show a sharp spike at one frequency. The Qur'an spectrum looks one-over-f-like - low-frequency dominance - not periodic. So we mark the periodicity rung tilde, not a check: real structure, but a trend, not a carrier.")

marker("24:00","Module 5-6 · scale and localization")
cue("Slides 12-13.")
say("The FFT mixes every position together; a wavelet pins structure to a scale. A pure Haar transform splits variation by scale - 2, 4, up to 128 surahs - and a shuffle null flags any scale carrying more energy than chance. The significant energy sits at the COARSE scales: 32, 64, 128 surahs. That is the same slow trend the FFT saw, now localized to large scales; fine scales are null. The Ricker scalogram then shows WHERE on the order each scale lives - and the coarse energy is spread across the whole order, a global trend, not a hot spot in one region.")

marker("29:00","Module 7-8 · verse rhythm and co-recurrence")
cue("Slides 14-15.")
say("Verse rhythm: the coefficient of variation of ayah lengths - standard deviation over mean - is about 0.75. Near zero would be a metronome; 0.75 is wide variability, close to natural speech phrasing. Rhythm, not a fixed pulse. Finally co-recurrence: cross-correlation slides one root's occurrence series under another's and measures overlap at each lag. A peak at lag zero means shared ayahs; a peak off zero means one leads. We judge it against a circular-shift null, never raw size - and we do not promote overlap into causation.")

marker("32:00","Module 9 · synthesis, audit, and the disclaimer")
cue("Slides 16-18.")
say("Pull it together. What survives the null: memory at plus 0.67, a low-frequency spectral peak, and coarse wavelet scales - all the SAME slow trend - plus bursty roots. What does NOT appear: fine periodicity, a fixed-period carrier, any mid-band cycle. The honest reading: read in order, the Qur'an behaves like a coherent natural signal - gentle memory, bursty thematic repetition, a slow global trend - the fingerprint of coherent language, not an engineered waveform. The audit slide states this rung by rung: memory check, burstiness check, scale check, periodicity tilde, carrier-wave cross, lead-lag tilde.")
cue("Slide 18 - say this verbatim.")
say("And the disclaimer, plainly: we are not claiming the Qur'an encodes a frequency, predicts signal processing, or hides a waveform. A surviving peak is a slow trend, not a designed cycle; a bursty root is coherent themed repetition, not a transmitted code. The lens is a disciplined way to ASK whether order carries structure, with a null behind every answer - judged by clarity, never offered as proof.")

marker("34:00","Close")
cue("Slides 19-20.")
say("Quick reference is on slide 19 - the terms and the live Book6 numbers. To close: one sequence, read honestly - every claim with its null, every parallel a labelled lens. Next in the series, Biology reads the same corpus as a genome; then the FDR Summary collects every Two Books test into one corrected dashboard. See you there.")
d.save(os.path.join(WK,"Signal_Instructor_Script.docx"))
print("signal script saved | words:",sum(len(p.text.split()) for p in d.paragraphs))

# ================= QUIZ =================
# Each item: (stem, correct_text, [distractors...], explanation). Correct position rotates A-D.
import string
d=new_doc("Two Books · Signal — Quiz")
TITLE(d,"Two Books · Signal — Quiz",
      "13 questions · ~15 minutes · auto-graded. Choose the single best answer unless told otherwise. Every value is reproducible live from Book6. (Paste into Google Forms.)")
QQ=[
("1.  Reading the Qur'an 'as a signal' means treating it as:","a sequence of numbers read IN ORDER",["a random set of words","a 2-D image","a fixed periodic wave"],"a signal is a sequence read in order; we test whether the ORDER carries structure."),
("2.  The lag-1 autocorrelation of surah-length is about +0.67 (shuffled ~0). This means:","neighbouring surahs have similar lengths - gentle memory",["surah lengths are random","every surah is the same length","the corpus is periodic"],"lag-1 = +0.67 vs ~0 shuffled: neighbouring surahs resemble each other (AR(1)-like memory)."),
("3.  For a memoryless (Poisson) process, the Fano factor equals:","1",["0","the mean","infinity"],"Poisson gives Fano = variance/mean = 1, the baseline for even arrivals."),
("4.  Every sampled root has Fano far above 1 (e.g. zulm ~40) at p ~ 0.0002. The roots are:","bursty / clustered",["evenly spaced","absent","periodic"],"Fano >> 1 at p ~ 0.0002 for every sampled root - occurrences arrive in clusters."),
("5.  The entropy-spectrum peak beats the shuffle at p ~ 0.0005 AND sits at the lowest frequency. The honest reading is:","a slow trend across the order, not a cycle",["a fixed repeating cycle","white noise","no structure at all"],"significant BUT lowest-frequency = a slow drift, not a repeating cycle (the app reports this)."),
("6.  Which reference signal best matches the Qur'an entropy spectrum?","pink / 1-over-f noise (low-frequency dominance)",["a pure periodic tone (line spectrum)","white noise (flat)","a single click"],"1/f noise: low-frequency dominance with no line peak - matches a trend, unlike a periodic tone."),
("7.  A wavelet decomposition differs from the FFT because it asks:","how much variation lives at each SCALE",["which fixed cycle-lengths recur","the mean of the signal","the total energy only"],"wavelets resolve energy by SCALE (2..128 surahs); the FFT resolves by fixed frequency."),
("8.  The significant Haar wavelet scales are:","32, 64, 128 (coarse)",["2, 4, 8 (fine)","none","all scales equally"],"coarse scales 32/64/128 are significant - the slow trend localized to large scales."),
("9.  In the Ricker scalogram the coarse-scale energy is spread across the whole order. The slow trend is therefore:","global, not a local artefact",["a local hot spot in one region","absent","periodic"],"spread across the whole order = a global trend, not a one-region artefact."),
("10.  The coefficient of variation of ayah lengths is about 0.75, which indicates:","wide variability, like natural speech phrasing",["a perfectly regular metronome pulse","all ayahs equal","a fixed cycle"],"CV ~ 0.75 = wide variability, near natural speech; far from a metronome (CV~0)."),
("11.  Cross-correlation between two roots is judged significant against:","a circular-shift null that preserves each signal's clustering",["raw peak size","the mean gap","the Fano factor"],"a circular-shift null preserves each root's clustering; significance is judged against it, not raw size."),
("12.  Which claim is LICENSED by the signal analysis?","reading order carries a slow trend and bursty clustering",["the Qur'an encodes a hidden frequency","one root causes another","the text is a periodic carrier wave"],"only the trend + clustering reading is licensed; encoding/causation/carrier claims are not."),
("13.  On the audit, 'spectrum <-> periodicity' is marked tilde (~) rather than a check because:","the significant peak is a low-frequency TREND, not a true cycle",["the peak is not significant","there is no peak","periodicity was proven"],"the peak is real but low-frequency (a trend), so the periodicity rung is ~, not a check."),
]
KEY=[]
for qi,(stem,correct,distr,expl) in enumerate(QQ):
    pos=qi%4
    opts=list(distr); opts.insert(pos,correct)
    P(d,[(stem,True)],size=10.5,after=2,before=6)
    for i,o in enumerate(opts): P(d,f"{string.ascii_uppercase[i]})  {o}",size=10,after=1)
    KEY.append((str(qi+1),string.ascii_uppercase[pos],expl))
d.save(os.path.join(WK,"Signal_Quiz.docx")); print("signal quiz saved (rotated)")

d=new_doc("Two Books · Signal — Quiz Answer Key (instructor)")
TITLE(d,"Two Books · Signal — Quiz Answer Key (instructor)","One point each, 13 total. Every value reproducible live from Book6.")
H(d,"Answers")
for n,a,ex in KEY: P(d,[(f"{n}.  {a}  ",True),("- "+ex,False)],size=10,after=2)
H(d,"Grading notes")
bullet(d,"Q5, Q6, Q13 are the core 'trend-not-cycle' checks - they confirm the student did NOT over-read the spectral peak as periodicity.")
bullet(d,"Q3, Q4 verify the Poisson/Fano burstiness logic; Q11 verifies null discipline.")
d.save(os.path.join(WK,"Signal_Quiz_Answer_Key.docx")); print("signal key saved | letters:",[a for _,a,_ in KEY])

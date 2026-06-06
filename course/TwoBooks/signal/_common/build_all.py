# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from sig import *
D=DATA; counts={}

def scale_slide(prs,robust,heavy):
    s=Tt(prs,"The scale rule — match the tool to the length")
    two(s,[L("ROBUST AT ĀYAH SCALE",18,True,TEAL),L(robust,16.5,True,NAVY)],
          [L("NEEDS SŪRA / CORPUS SCALE",18,True,AMBER),L(heavy,16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)

# ============== L3 ==============
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 3","Vectorization Schemes — root, surface, morphology, frequency",
  "One verse, many signals. The ANCHOR is the ROOT (ریشه); surface form and morphology are complementary. 1:1 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ → roots سمو·ءله·رحم·رحم → [381, 2848, 339, 339].",
  "Each channel measures a different property of the same root-tokens; the choice is stated and validated. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — many channels over one anchor")
two(s,[L("THE ANCHOR IS THE ROOT",18,True,NAVY),L("Every channel is computed over the same roots (ریشه): the unit of meaning, as in NLP (stem/lemma) and biology (root↔codon).",16.5,True,TEAL)],
 [L("CHANNELS LAYER ON TOP",18,True,NAVY),L("Frequency, length, surface form, morphology, position, embedding — each turns the SAME roots into a different 1-D signal.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — levels of measurement")
three(s,[L("NOMINAL",17,True,RED),L("Root IDENTITY (which of 1,702) is a LABEL — no arithmetic; one-hot or embed first.",16)],
 [L("ORDINAL",17,True,AMBER),L("Position is the index axis; morphological pattern can be ordered, not metric.",16)],
 [L("RATIO",17,True,TEAL),L("Root FREQUENCY and LENGTH are true counts with a real zero — addable, averageable, transformable.",16)])
s=Tt(prs,"Channel A — root frequency (the anchor signal)")
band(s,0.42,1.18,12.5,0.4,TINT,"1:1 roots سمو · ءله · رحم · رحم — amplitude = corpus frequency",TEAL)
line_signal(s,2.0,1.75,9.0,D["L3"]["rootfreq"],col=TEAL,bh=2.6,labels=D["L3"]["roots"],vmax=2848)
panel(s,0.42,5.6,12.5,1.6,TINT2,[L("x = [381, 2848, 339, 339]",18,True,NAVY),
  L("ءله towers (2,848); رحم appears twice (رحمن and رحيم share the root رحم) — a repeated sample. Frequency exposes prominence and repetition.",16.5,True,TEAL)],space=6)
s=Tt(prs,"Channel B — root length; Channel C — surface form")
two(s,[L("ROOT LENGTH → [3, 3, 3, 3]",18,True,TEAL),L("Arabic roots are overwhelmingly triliteral, so length is nearly flat — itself information: a weak discriminator at the root scale.",16.5,True,NAVY)],
 [L("SURFACE FORM → اسم · الله · رحمن · رحيم",18,True,AMBER),L("The inflected words restore what the root drops (the وزن pattern, definiteness) — richer surface, lower compression.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Real data — channels disagree, and that is the point")
finding2(s,
 {"title":"Root frequency (1:1)","cats":["سمو","ءله","رحم","رحم"],"series":[("",[TEAL,NAVY,AMBER,AMBER],[381,2848,339,339])],"legend":False},
 {"title":"Root length (1:1)","cats":["سمو","ءله","رحم","رحم"],"series":[("",[TEAL,TEAL,TEAL,TEAL],[3,3,3,3])],"legend":False},
 [L("Frequency: spiky, informative",17.5,True,TEAL),L("One tall peak (ءله) and a repeated mid root (رحم×2) — prominence and repetition.",16)],
 [L("Length: flat, weak here",17.5,True,AMBER),L("All triliteral → [3,3,3,3]. Same verse, different channel, almost no shape.",16)],fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Encoding nominal roots — when you must use identity")
three(s,[L("ONE-HOT",17,True,TEAL),L("Each root → a 0/1 vector of length 1,702. Sparse, exact, high-dimensional.",16)],
 [L("REPLACE-BY-FREQUENCY",17,True,AMBER),L("Map each root to its count → collapses to the ratio channel. Simple, defensible.",16)],
 [L("EMBEDDING",17,True,NAVY),L("Learn a dense vector per root from co-occurrence (Lecture 14). Numeric by construction.",16)])
s=Tt(prs,"Dual-domain — channels in creation’s data")
two(s,[L("عالم التكوين",18,True,AMBER),L("A patient measured by ECG, SpO₂, temperature; a gene by expression, methylation, conservation. Same object, many signals.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("A verse measured over the same roots by frequency, length, morphology, embedding. The anchor fixes the unit; the channel fixes the question.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
corpus_slide(prs,3)
scale_slide(prs,"Per-root channels (frequency, length, surface) read directly at āyah scale — no length needed.",
  "Combining channels into distances/embeddings, and any spectral reading, waits for sūra/corpus scale.")
threads_block(prs,
 "Each channel is a stated rule over the roots: frequency/length are ratio counts; root-identity is nominal and is one-hot/embedded first.",
 "Which representation exposes structure — here frequency reveals the ءله peak and the رحم repeat that length hides.",
 "Re-encode (scalar→one-hot), normalize, or reorder roots to test a channel’s sensitivity; a robust feature survives re-encoding.",
 "A channel-feature must name real roots: the 1:1 peak reads back to ءله, the repeat to رحم (رحمن/رحيم).",
 "A channel that ‘separates’ verses must beat random-Arabic separation; generic Zipf structure is shared by every channel.")
finish_block(prs,
 "Which channel is the most ‘honest’ — and which the most arbitrary? When would surface form beat the root anchor?",
 "Anchor on the root; choose the channel for the question; one verse yields many signals, all over the same unit.",
 "Treating root-IDENTITY numbers as magnitudes — averaging ‘root #500 and #1700’ is meaningless.",
 "Use root FREQUENCY/length (ratio) directly; for identity, one-hot or embed before any arithmetic.")
roadmap_pos(prs,3)
appslide(prs,[("① VERSE","enter 1:1",TINT,TEAL),("② CHANNEL","root/surface/morph",AMBERT,AMBER),("③ SIGNAL","see the bars",TINT,TEAL),("④ NORMALIZE","z-score toggle",REDT,RED)],
  "Switch channels on 1:1 and watch the signal change while the roots stay fixed. Reproduce [381, 2848, 339, 339], then flip to length [3,3,3,3].")
s=slide(prs); audit(s,"Channels are real, computable, distinct — faithful measurements of the root-tokens.","Reading a channel AS meaning: the numbers measure form/frequency, not sense.","Which channel is ‘best’ is question-dependent — a modeling choice the text does not dictate.")
s=slide(prs); takeaway(s,"Feature engineering — choosing how to represent data — is the heart of NLP and ML; the channel decides what you can see.","Anchor on the ROOT; layer channels on top; declare, normalize, validate each like any claim.")
counts[3]=save(prs,"03_Vectorization_Schemes","03_Vectorization_Schemes_Lecture.pptx")

# ============== L4 ==============
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 4","The Waveform — the per-root signal of a verse",
  "Read a verse as a waveform: each root a sample, amplitude = its corpus frequency. 94:5 فَإِنَّ مَعَ الْعُسْرِ يُسْرًا and 94:6 إِنَّ مَعَ الْعُسْرِ يُسْرًا — almost the same verse, almost the same waveform.",
  "Amplitude, peaks, troughs, dynamic range, zero-crossings — the vocabulary of a 1-D signal, on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — a verse is a waveform")
two(s,[L("AMPLITUDE ALONG POSITION",18,True,NAVY),L("Plot root-frequency against root position and the verse becomes a waveform — the same object as audio or an ECG, read along one axis.",16.5,True,TEAL)],
 [L("SHAPE = MEANING-FREE STRUCTURE",18,True,NAVY),L("Peaks (frequent roots), troughs (rare roots), the rise-and-fall between — the verse’s form, measurable before its sense.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"94:5 — the waveform of فَإِنَّ مَعَ الْعُسْرِ يُسْرًا")
band(s,0.42,1.18,12.5,0.4,TINT,"roots of 94:5 · amplitude = corpus frequency",TEAL)
line_signal(s,1.6,1.75,9.8,D["L4"]["94:5"]["rootfreq"],col=TEAL,bh=2.6,labels=D["L4"]["94:5"]["roots"])
panel(s,0.42,5.6,12.5,1.6,TINT2,[L("x = %s"%D["L4"]["94:5"]["rootfreq"],18,True,NAVY),
  L("Roots %s — the waveform rises and falls across the samples: a shape we can measure, compare, transform."%(" · ".join(D["L4"]["94:5"]["roots"])),16.5,True,TEAL)],space=6)
s=Tt(prs,"Conceptual foundation — the waveform vocabulary")
three(s,[L("PEAK / TROUGH",17,True,TEAL),L("Max sample = peak (commonest root); min = trough (rarest). They anchor the shape.",16)],
 [L("DYNAMIC RANGE",17,True,AMBER),L("max−min (or ratio): wide = spiky, dominated by one root; narrow = even.",16)],
 [L("ZERO-CROSSINGS",17,True,NAVY),L("After centring, how often the signal crosses zero — how ‘busy’ the verse is.",16)])
s=Tt(prs,"94:5 vs 94:6 — a near-repeat, a near-identical waveform")
finding2(s,
 {"title":"94:5  فَإِنَّ مَعَ الْعُسْرِ يُسْرًا","cats":D["L4"]["94:5"]["roots"],"series":[("",[TEAL]*len(D["L4"]["94:5"]["roots"]),D["L4"]["94:5"]["rootfreq"])],"legend":False},
 {"title":"94:6  إِنَّ مَعَ الْعُسْرِ يُسْرًا","cats":D["L4"]["94:6"]["roots"],"series":[("",[AMBER]*len(D["L4"]["94:6"]["roots"]),D["L4"]["94:6"]["rootfreq"])],"legend":False},
 [L("The same shape twice",17.5,True,TEAL),L("94:5 and 94:6 differ only by فَ — their root waveforms are nearly identical: a real, audible repetition made visible.",16)],
 [L("Repetition is structure",17.5,True,AMBER),L("Two adjacent verses, one waveform = a deliberate echo (مع العسر يسرا). Form mirrors meaning.",16)],fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Real data — the waveform of 103 Al-ʿAsr")
line_signal(s,0.8,1.5,11.7,D["L5"]["asr_signal"],col=TEAL,bh=3.0)
panel(s,0.42,5.05,12.5,2.15,TINT,[L("وَالْعَصْرِ · إِنَّ الْإِنسَانَ لَفِي خُسْرٍ · إِلَّا الَّذِينَ … — %d root samples"%len(D["L5"]["asr_signal"]),17,True,NAVY),
  L("The waveform grows with the third, long verse — length and amplitude both carry the sūra’s argument.",16.5,True,TEAL)],space=7)
s=Tt(prs,"Reading the shape — three numbers")
v=D["L4"]["94:5"]["rootfreq"]
three(s,[L("PEAK = %d"%max(v),17,True,TEAL),L("the most frequent root in 94:5 — the waveform’s crest.",16)],
 [L("TROUGH = %d"%min(v),17,True,AMBER),L("the rarest root — the waveform’s dip.",16)],
 [L("DYNAMIC RANGE = %d"%(max(v)-min(v)),17,True,NAVY),L("peak − trough: how spiky the verse is. A wide range means one root dominates the shape.",16)])
s=Tt(prs,"Dual-domain — waveforms everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("An ECG beat, a spoken word, a seismograph — amplitude-against-time waveforms read by peaks, troughs, range.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The verse-as-waveform is the same object: amplitude-against-position. Every waveform tool transfers, starting with the shape itself.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
corpus_slide(prs,4)
scale_slide(prs,"Amplitude, peak, trough, dynamic range need no length — robust on a single āyah.",
  "Spectral/periodic reading of the waveform waits for sūra/corpus scale (Lecture 9+).")
threads_block(prs,
 "Amplitude = a root’s corpus frequency, ratio-scale; the waveform is exact and reproducible from Book6.",
 "Repetition and prominence — peaks, troughs, and repeated shapes (94:5≈94:6) the flat text does not display.",
 "Shuffle the roots to destroy the waveform; a real echo (94:5/94:6) survives as a matched shape, a coincidence does not.",
 "A peak reads back to a specific root (e.g. ءله); a matched waveform reads back to a real rhetorical repetition.",
 "A ‘striking’ peak must beat random-Arabic: ءله peaking is expected (commonest root), not a discovery, until it exceeds the baseline.")
finish_block(prs,
 "What is gained and lost when a verse becomes a waveform? Is 94:5≈94:6 a coincidence or a device — how would you test it?",
 "The waveform exposes prominence and repetition; read its shape before interpreting, and validate any peak against the baseline.",
 "Calling the tallest bar the ‘most important’ word — it is only the commonest root (ءله), not the key idea.",
 "Compare the peak to random-Arabic; report prominence relative to the baseline, then read it back to the root.")
roadmap_pos(prs,4)
appslide(prs,[("① VERSE","enter 94:5",TINT,TEAL),("② WAVEFORM","root-freq bars",AMBERT,AMBER),("③ MARKERS","peak·trough·range",TINT,TEAL),("④ COMPARE","overlay 94:6",REDT,RED)],
  "Plot 94:5, read its peak/trough/range, then overlay 94:6 to see the near-identical echo — the waveform of a repetition.")
s=slide(prs); audit(s,"The waveform is literally the verse’s root-frequency sequence — exact and reproducible.","The waveform is not the meaning; a tall peak is a common root, not an important idea.","Which features ‘matter’ is question-dependent; the raw waveform asserts nothing alone.")
s=slide(prs); takeaway(s,"Reading a waveform — peaks, range, repetition — is the first move in audio, biomedical and sensor analysis.","A verse is a waveform of root-amplitudes; 94:5≈94:6 shows repetition as a repeated shape. Measure form before interpreting.")
counts[4]=save(prs,"04_Waveform","04_Waveform_Lecture.pptx")

# ============== L5 SAMPLING & QUANTIZATION ==============
asr=D["L5"]["asr_signal"]; mx=max(asr)
q3=[round(v/mx*2)/2*mx for v in asr]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 5","Sampling & Quantization — turning the verse into samples",
  "Two choices set a digital signal: how finely we SAMPLE (one root = one sample) and how finely we QUANTIZE the amplitude. 103 وَالْعَصْرِ · إِنَّ الْإِنسَانَ لَفِي خُسْرٍ · إِلَّا الَّذِينَ آمَنُوا … is our test signal.",
  "Nyquist, aliasing, bit-depth, quantization error — the bedrock of digital signal processing, on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — sample, then quantize")
two(s,[L("SAMPLING = pick the points",18,True,NAVY),L("Our sampling rule is fixed: one ROOT = one sample, in reading order. Coarsen it (drop roots, bin them) and you lose detail.",16.5,True,TEAL)],
 [L("QUANTIZATION = round the value",18,True,NAVY),L("Amplitude (root frequency) is rounded to a finite set of levels. Fewer levels (bits) = a coarser, blockier signal.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — Nyquist & aliasing")
three(s,[L("SAMPLING RATE",17,True,TEAL),L("How many samples per unit. Too few and fast structure is missed or mis-seen.",16)],
 [L("NYQUIST",17,True,AMBER),L("To capture a pattern you need ≥2 samples per cycle. The Ar-Raḥmān refrain (period 2) is right at this edge.",16)],
 [L("ALIASING",17,True,RED),L("Under-sample and a fast pattern masquerades as a slow one — an artifact of the rate, not the verse.",16)])
s=Tt(prs,"103 Al-ʿAsr — the test signal at full resolution")
line_signal(s,0.8,1.5,11.7,asr,col=TEAL,bh=3.0)
panel(s,0.42,5.05,12.5,2.15,TINT,[L("%d root samples, amplitude 1 … %d"%(len(asr),mx),17,True,NAVY),
  L("The full-resolution root-frequency waveform of Sūrat al-ʿAsr. Every following step degrades this on purpose, to see what survives.",16.5,True,TEAL)],space=7)
s=Tt(prs,"Quantization — the same verse at 3 levels")
two(s,[L("FULL → 3 LEVELS",18,True,TEAL),L("Round each amplitude to one of three levels. The peaks survive; the fine differences between mid-frequency roots collapse — that lost detail is QUANTIZATION ERROR.",16.5,True,NAVY)],
 [L("BIT-DEPTH",18,True,AMBER),L("3 levels ≈ under 2 bits. More bits → finer amplitude → smaller error. The trade-off is resolution vs storage, exactly as in audio.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Aliasing — under-sampling invents structure")
two(s,[L("DROP EVERY OTHER ROOT",18,True,RED),L("Halving the sampling rate can make two different verses look identical, or invent a periodicity that is not there. The pattern you ‘see’ is then a function of the rate.",16.5,True,NAVY)],
 [L("THE GUARD",18,True,TEAL),L("Sample finely enough for the structure you seek (Nyquist), and declare the rate. Never read a periodicity without checking it is above the aliasing limit.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — every ADC does this")
two(s,[L("عالم التكوين",18,True,AMBER),L("A microphone, an ECG, a camera all sample-and-quantize the analog world; CD audio is 44.1 kHz × 16 bits. Aliasing is why wheels spin backwards on film.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("Digitizing the verse is the same act: choose the sampling unit (the root) and the amplitude resolution, and know what each choice discards.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — resolution is a choice","A digital signal is fixed by two resolutions: how finely you sample (one root) and how finely you quantize amplitude.","Sampling rate and bit-depth recur in Fourier (L9) and filtering (L11) — every transform assumes a resolution.")
corpus_slide(prs,5)
scale_slide(prs,"Quantization and bit-depth apply to any length — fine on a single āyah.",
  "Aliasing/Nyquist claims about periodicity need enough samples — test at sūra/corpus scale.")
threads_block(prs,
 "Sample = one root; amplitude = root frequency (ratio). Sampling rate and bit-depth are declared numbers, not free knobs.",
 "How coarse a measurement still preserves the verse’s shape — the resolution floor below which structure is lost.",
 "Down-sample / re-quantize as a declared transform; a real feature survives moderate coarsening, an artifact appears or vanishes with the rate.",
 "A surviving peak reads back to the root that made it; an aliased ‘periodicity’ reads back to nothing — it is a rate artifact.",
 "A periodicity must beat random Arabic AND exceed the aliasing limit before it counts as real.")
finish_block(prs,
 "How few levels can 103 tolerate before its argument-shape is lost? When does down-sampling create a fake pattern?",
 "Sampling and quantization are lossy by design; know the loss, declare the rate, and never read structure below Nyquist.",
 "Reading a periodicity from an under-sampled signal — it may be an aliasing artifact of the rate.",
 "Check the sampling rate against the pattern’s period (Nyquist); re-test at a finer rate before believing it.")
roadmap_pos(prs,5)
appslide(prs,[("① VERSE","103 Al-ʿAsr",TINT,TEAL),("② BIT-DEPTH","levels slider",AMBERT,AMBER),("③ RATE","down-sample",TINT,TEAL),("④ ERROR","watch the loss",REDT,RED)],
  "Slide bit-depth from full to 3 levels and watch the waveform blockify; halve the sampling rate and watch aliasing distort 103’s shape.")
s=slide(prs); audit(s,"Sampling and quantization are exact, declared operations on the root signal.","Treating a quantized/aliased artifact as real structure of the verse.","The ‘right’ resolution is question-dependent — stated, not assumed.")
s=slide(prs); takeaway(s,"Every digital recording you own is sampled and quantized; Nyquist and aliasing govern audio, imaging and instrumentation.","One root = one sample; round amplitude to levels; sample above Nyquist; declare the rate and know the loss.")
counts[5]=save(prs,"05_Sampling_Quantization","05_Sampling_Quantization_Lecture.pptx")

# ============== L6 SMOOTHING, TREND & DIFFERENCE ==============
k=D["L6"]["kursi"]; 
def movavg(x,w=3):
    o=[]; 
    for i in range(len(x)):
        a=max(0,i-w//2); b=min(len(x),i+w//2+1); o.append(round(sum(x[a:b])/(b-a),1))
    return o
ks=movavg(k,3); kd=[k[i+1]-k[i] for i in range(len(k)-1)]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 6","Smoothing, Trend & Difference — the slow and the fast",
  "Every signal splits into a slow TREND and fast DETAIL. A moving average extracts the trend; the first difference extracts the change. Test signal: 2:255 آيَةُ الْكُرْسِيّ — a long verse of %d root samples."%D["L6"]["kursi_n"],
  "Moving average (low-pass), window length, derivative/first-difference, edge effects — on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — separate trend from detail")
two(s,[L("MOVING AVERAGE → trend",18,True,NAVY),L("Replace each sample by the average of its neighbours. The fast wiggles cancel; the slow shape (the trend) remains. It is a low-pass filter.",16.5,True,TEAL)],
 [L("FIRST DIFFERENCE → change",18,True,NAVY),L("Subtract each sample from the next. Flat stretches go to ~0; jumps stand out. It is the discrete derivative — a high-pass view.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — window, edges, derivative")
three(s,[L("WINDOW LENGTH",17,True,TEAL),L("Wider window = smoother trend, more detail removed. The window is a declared choice.",16)],
 [L("EDGE EFFECTS",17,True,AMBER),L("Near the verse’s start/end the window runs off the edge — handle by shrinking or padding, and say which.",16)],
 [L("DERIVATIVE",17,True,NAVY),L("The first difference approximates the slope — where the root-frequency rises or falls fastest.",16)])
s=Tt(prs,"2:255 — raw root-frequency waveform")
line_signal(s,0.7,1.5,11.9,k,col=TEAL,bh=3.0)
panel(s,0.42,5.05,12.5,2.15,TINT,[L("Āyat al-Kursī — %d root samples"%len(k),17,True,NAVY),
  L("Long enough to have a real trend and detail. The spikes are frequent roots (ءله, ربب …); the valleys are rare ones.",16.5,True,TEAL)],space=7)
s=Tt(prs,"Trend vs detail — smoothing the verse")
two(s,[L("3-WINDOW MOVING AVERAGE",18,True,TEAL),L("The smoothed signal follows the verse’s slow drift and suppresses single-root spikes — the ‘melody’ under the ‘notes.’",16.5,True,NAVY)],
 [L("FIRST DIFFERENCE",18,True,AMBER),L("The difference signal is near zero on even stretches and large where a common root meets a rare one — the verse’s sharpest transitions.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"The smoothed and difference signals")
finding2(s,
 {"title":"Raw vs smoothed (first 8 samples)","cats":["1","2","3","4","5","6","7","8"],"series":[("raw",TEAL,k[:8]),("smooth",AMBER,ks[:8])],"legend":True},
 {"title":"|first difference| (first 8)","cats":["1","2","3","4","5","6","7","8"],"series":[("",[NAVY]*8,[abs(x) for x in kd[:8]])],"legend":False},
 [L("Smoothing keeps the slow shape",17.5,True,TEAL),L("The averaged line tracks the trend and drops the single-sample spikes — denoising without erasing the verse’s drift.",16)],
 [L("Difference marks the jumps",17.5,True,AMBER),L("Large |difference| flags the steep transitions between common and rare roots — the verse’s structural seams.",16)],fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Dual-domain — trend and change everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("Moving averages smooth stock prices and temperature series; derivatives find edges in images and onsets in audio.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same operators read the verse: the trend is its slow contour, the difference its sharp turns — both computed on the root signal.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — every signal is trend + detail","A signal splits into a slow trend (low-pass) and fast change (difference); they are two views of one root waveform.","Smoothing is convolution (L7); the frequency view of trend vs detail is the spectrum (L9).")
corpus_slide(prs,6)
scale_slide(prs,"Smoothing and differencing work on any length, but are meaningful where a verse is long (2:255).",
  "A ‘trend across the corpus’ claim is a corpus-scale statement — test it there, not on one short āyah.")
threads_block(prs,
 "The window length and edge rule are declared numbers; smoothing/difference are exact linear operators on the root signal.",
 "The slow TREND (theme drift) and the sharp TRANSITIONS — structure the raw waveform hides under its spikes.",
 "Vary the window (a declared reorder of scale); a real trend is stable across windows, a fragile one is not.",
 "A trend reads back to a stretch of the verse; a difference spike reads back to a specific common-to-rare root transition.",
 "A ‘trend’ must beat random-Arabic drift; smoothing a random verse also looks smooth — compare to the baseline.")
finish_block(prs,
 "Which window best reveals 2:255’s structure? Is the trend a real theme or an artifact of common roots?",
 "Trend and detail are two views of one signal; smoothing denoises, differencing localises change — pick per question.",
 "Choosing the window AFTER seeing the nicest-looking trend — that is fitting the smoother to the wish.",
 "Declare the window first; show the trend is stable across nearby windows and beats a baseline.")
roadmap_pos(prs,6)
appslide(prs,[("① VERSE","2:255",TINT,TEAL),("② WINDOW","width slider",AMBERT,AMBER),("③ TREND","smoothed line",TINT,TEAL),("④ DIFF","change signal",REDT,RED)],
  "Slide the smoothing window on Āyat al-Kursī and watch the trend emerge; toggle the first-difference to see where the verse turns sharpest.")
s=slide(prs); audit(s,"Moving average and first difference are exact, declared linear operators.","Reading the smoothed trend as a hidden ‘message’ rather than a low-frequency summary.","The right window is question-dependent — stated, not assumed.")
s=slide(prs); takeaway(s,"Moving averages and derivatives are everywhere — finance, climate, image edges, audio onsets.","Split the root signal into trend (low-pass) and change (difference); declare the window; validate the trend against a baseline.")
counts[6]=save(prs,"06_Smoothing_Trend_Difference","06_Smoothing_Trend_Difference_Lecture.pptx")

# ============== L7 CONVOLUTION & LTI ==============
nasr=D["L7"]["nasr"]
def convbox(x,k=3):
    o=[];
    for i in range(len(x)):
        a=max(0,i-k//2); b=min(len(x),i+k//2+1); o.append(round(sum(x[a:b])/(b-a),1))
    return o
nc=convbox(nasr,3)
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 7","Convolution & LTI Systems — sliding a kernel",
  "Convolution slides a small KERNEL along the signal, replacing each sample by a weighted blend of its neighbours. It is the master operation of DSP. Test signal: 110 إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ …",
  "Kernel, impulse response, linearity, time-invariance — on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — a kernel that slides")
two(s,[L("CONVOLUTION",18,True,NAVY),L("Pick a small weight pattern (the kernel). Slide it across the root signal; at each position output the weighted sum. Smoothing, edges, echoes are all one kernel or another.",16.5,True,TEAL)],
 [L("IMPULSE RESPONSE",18,True,NAVY),L("Feed in a single spike; what comes out IS the kernel. A linear, time-invariant (LTI) system is fully described by this one response.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — what makes a system LTI")
three(s,[L("LINEARITY",17,True,TEAL),L("The response to a sum is the sum of responses; scaling the input scales the output.",16)],
 [L("TIME-INVARIANCE",17,True,AMBER),L("Shift the verse and the output just shifts — the rule does not change with position.",16)],
 [L("COMMUTATIVITY",17,True,NAVY),L("Signal∗kernel = kernel∗signal. The kernel and the data play symmetric roles.",16)])
s=Tt(prs,"110 An-Naṣr — the input signal")
line_signal(s,1.2,1.5,11.0,nasr,col=TEAL,bh=3.0)
panel(s,0.42,5.05,12.5,2.15,TINT,[L("%d root samples"%len(nasr),17,True,NAVY),
  L("إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ · وَرَأَيْتَ النَّاسَ … the raw root-frequency waveform we will convolve.",16.5,True,TEAL)],space=7)
s=Tt(prs,"Convolution with a box kernel [⅓,⅓,⅓]")
finding2(s,
 {"title":"Input (first 10 roots)","cats":[str(i+1) for i in range(10)],"series":[("",[TEAL]*10,nasr[:10])],"legend":False},
 {"title":"Output = input ∗ box kernel","cats":[str(i+1) for i in range(10)],"series":[("",[AMBER]*10,nc[:10])],"legend":False},
 [L("The kernel blends neighbours",17.5,True,TEAL),L("Each output sample is the average of three input roots — the box kernel is a smoother. Change the weights and the same machinery sharpens or detects edges.",16)],
 [L("One operation, many effects",17.5,True,AMBER),L("Box → smooth; [−1,1] → edges; [1,0,…,1] → echo. The kernel encodes the whole behaviour of the LTI system.",16)],fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Kernels are a vocabulary")
three(s,[L("SMOOTH",17,True,TEAL),L("[⅓,⅓,⅓] — average; removes spikes (Lecture 6’s moving average IS a convolution).",16)],
 [L("EDGE",17,True,AMBER),L("[−1,1] — first difference; flags transitions between common and rare roots.",16)],
 [L("ECHO",17,True,NAVY),L("a delayed copy added back — models the refrain/repetition structure seen in Lecture 8.",16)])
s=Tt(prs,"Dual-domain — convolution runs the world")
two(s,[L("عالم التكوين",18,True,AMBER),L("Image blur and sharpen, audio reverb, and every convolutional neural network are convolutions; an LTI system’s impulse response is its fingerprint.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same kernels read the verse — smoothing its waveform, detecting its edges, modelling its echoes — all on the root signal.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — one operation, many effects","Convolution with a chosen kernel smooths, sharpens, or echoes; an LTI system IS its impulse response.","Convolution in time becomes multiplication in frequency (L9) — the bridge to the spectrum.")
corpus_slide(prs,7)
scale_slide(prs,"Local kernels (width 2–3) act fine on short verses — convolution is local.",
  "Long kernels and frequency-domain convolution (Lecture 9) need sūra/corpus length.")
threads_block(prs,
 "The kernel weights are declared; convolution is an exact linear operator on the root signal.",
 "Local motifs — the response pattern a kernel draws out (smooth contour, edges, echoes) hidden in the raw waveform.",
 "Swap kernels (a declared transform) to probe different structure; a real motif responds consistently, noise does not.",
 "A strong response reads back to a real local pattern of roots; a spurious one maps to nothing.",
 "A kernel-found ‘motif’ must beat random Arabic — a box kernel smooths a random verse too.")
finish_block(prs,
 "Which kernel best reveals An-Naṣr’s structure? How is Lecture 6’s moving average secretly a convolution?",
 "Convolution is the one operation behind smoothing, edges and echoes; the kernel is the whole story of an LTI system.",
 "Inventing a bespoke kernel that makes one verse look special — then never testing it elsewhere.",
 "Fix the kernel in advance; apply it corpus-wide; require the response to beat a baseline.")
roadmap_pos(prs,7)
appslide(prs,[("① VERSE","110 An-Naṣr",TINT,TEAL),("② KERNEL","box/edge/echo",AMBERT,AMBER),("③ CONVOLVE","slide it",TINT,TEAL),("④ RESPONSE","see the output",REDT,RED)],
  "Pick a kernel (box, edge, echo) and slide it along An-Naṣr; watch smoothing, edge-detection and echo emerge from one operation.")
s=slide(prs); audit(s,"Convolution and the impulse response are exact, declared LTI operations.","Mistaking a kernel’s artifact (e.g. an echo you inserted) for structure in the verse.","Which kernel is ‘right’ is question-dependent — declared, not assumed.")
s=slide(prs); takeaway(s,"Convolution powers image filters, audio effects and every CNN; the impulse response defines an LTI system.","Slide a declared kernel along the root signal; smoothing, edges and echoes are one operation; validate any motif against a baseline.")
counts[7]=save(prs,"07_Convolution_LTI","07_Convolution_LTI_Lecture.pptx")

# ============== L8 AUTOCORRELATION & PERIODICITY ==============
ac=D["L8"]["autocorr_lag0_12"]; ind=D["L8"]["refrain_indicator"]; nref=D["L8"]["n_refrain"]; slen=D["L8"]["sura_len"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 8","Autocorrelation & Periodicity — does the verse repeat?",
  "Autocorrelation slides a signal against a shifted copy of itself: peaks at a lag reveal a period. Sūrat ar-Raḥmān (55) repeats فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ %d times — and the math finds it."%nref,
  "Lag, autocorrelation, periodicity, stationarity — a real, baseline-beating result. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — correlate a signal with itself")
two(s,[L("SHIFT AND COMPARE",18,True,NAVY),L("Take the signal, shift it by a lag, and measure how well it matches the original. A high match at lag k means the pattern repeats every k steps.",16.5,True,TEAL)],
 [L("PERIODICITY",18,True,NAVY),L("A refrain that returns every other verse will make autocorrelation peak at even lags — a period-2 signature, visible in the numbers.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — lag, ACF, stationarity")
three(s,[L("LAG",17,True,TEAL),L("The shift, in verses. Lag 0 is the signal vs itself (=1).",16)],
 [L("ACF PEAK",17,True,AMBER),L("A high autocorrelation at lag k = a repeat every k. The first strong positive peak is the period.",16)],
 [L("STATIONARITY",17,True,NAVY),L("Autocorrelation assumes the structure is steady across the sūra — check before trusting it.",16)])
s=Tt(prs,"Ar-Raḥmān — the refrain indicator over %d verses"%slen)
line_signal(s,0.6,1.6,12.0,ind,col=TEAL,bh=2.6)
panel(s,0.42,4.5,12.5,2.7,TINT,[L("1 where the verse IS فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ, else 0 — %d ones"%nref,17,True,NAVY),
  L("The spikes are nearly evenly spaced — the refrain returns on a regular beat. The eye suspects a period; autocorrelation measures it.",16.5,True,TEAL)],space=7)
s=Tt(prs,"The autocorrelation — a period-2 signature")
finding2(s,
 {"title":"Autocorrelation at even lags (positive)","cats":["lag 0","lag 2","lag 4","lag 6"],"series":[("",[NAVY,TEAL,TEAL,AMBER],[ac[0],ac[2],ac[4],ac[6]])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Odd lags (anti-phase, negative)","cats":["lag 1","lag 3","lag 5"],"series":[("",[RED,RED,AMBER],[abs(ac[1]),abs(ac[3]),abs(ac[5])])],"legend":False,"fmt":"{:.2f}"},
 [L("Even lags POSITIVE: +0.75 at lag 2",17.5,True,TEAL),L("The signal matches itself when shifted by 2 verses — a clean period-2: the refrain comes roughly every other verse.",16)],
 [L("Odd lags NEGATIVE: −0.67 at lag 1",17.5,True,AMBER),L("Shift by 1 and refrain lands on non-refrain — anti-correlated. The alternation confirms the rhythm.",16)],fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Validation — this beats chance and the baseline")
two(s,[L("BEATS A NULL",18,True,TEAL),L("Shuffle the verse order: the lag-2 peak collapses. The observed period-2 is far in the tail — not an accident of arrangement.",16.5,True,NAVY)],
 [L("BEATS RANDOM ARABIC",18,True,AMBER),L("Exact-verse repetition runs 7.1% in the Qur’an vs 0.81% in matched random Arabic (~8.8×, p≈0.03). Ar-Raḥmān’s refrain is a real, specific device.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — periodicity is universal")
two(s,[L("عالم التكوين",18,True,AMBER),L("Autocorrelation finds the heart rate in an ECG, the pitch of a voice, the season in climate data, the orbit in a light curve.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The very same tool finds the refrain’s period in a sūra — رحمة as rhythm. One mathematics, two Books.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — repetition has a period","Autocorrelation turns ‘it feels repetitive’ into a measured period — Ar-Raḥmān is a validated period-2.","Period in time = a peak in frequency; Fourier (L9) reads the same refrain as a spectral line.")
corpus_slide(prs,8)
scale_slide(prs,"Autocorrelation needs a sequence with several cycles — Ar-Raḥmān’s %d verses qualify."%slen,
  "On a single short āyah there are too few samples; periodicity is a sūra/corpus-scale claim.")
threads_block(prs,
 "The indicator (refrain? 1/0) and the lag are exact; autocorrelation is a declared, reproducible statistic.",
 "Periodicity and rhyme — the hidden beat (period 2) that the flat list of verses does not show.",
 "Shuffle verse order (a declared reorder) to build the null; the real period-2 peak survives only on the true order.",
 "The lag-2 peak reads back to an ACTUAL refrain (فبأي آلاء ربكما تكذبان) returning every other verse.",
 "The period beats both a shuffle null and the random-Arabic baseline (7.1% vs 0.81%) — a genuine finding.")
finish_block(prs,
 "Why do odd lags go negative? Could the period-2 be a confound of verse length — how would you check?",
 "Autocorrelation turns ‘it feels repetitive’ into a measured period — here a clean, validated period-2 refrain.",
 "Declaring a period after eyeballing the spikes, with no null — that is pattern-seeing, not measuring.",
 "Pre-declare the lag test; confirm the peak survives shuffling and beats the natural-language baseline.")
roadmap_pos(prs,8)
appslide(prs,[("① SŪRA","Ar-Raḥmān 55",TINT,TEAL),("② INDICATOR","refrain? 1/0",AMBERT,AMBER),("③ ACF","lag plot",TINT,TEAL),("④ NULL","shuffle order",REDT,RED)],
  "Build the refrain indicator for Sūrat ar-Raḥmān, read the lag-2 peak (+0.75), then shuffle the verse order and watch the period collapse.")
s=slide(prs); audit(s,"Period-2 in Ar-Raḥmān: autocorrelation +0.75 at lag 2, beats a shuffle null AND the random-Arabic baseline.","Reading a periodicity from a non-stationary or under-sampled signal without a null.","Whether a weak ACF bump is ‘real’ on a short sūra — set aside until tested at scale.")
s=slide(prs); takeaway(s,"Autocorrelation extracts heart rate, pitch, season and orbit; it is the standard period detector.","Shift-and-compare the root/indicator signal; Ar-Raḥmān shows a validated period-2 refrain — repetition you can measure.")
counts[8]=save(prs,"08_Autocorrelation_Periodicity","08_Autocorrelation_Periodicity_Lecture.pptx")

# ============== L9 FOURIER & THE SPECTRUM ==============
ft=D["L9"]["fft_top"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 9","Fourier & the Spectrum — the verse as frequencies",
  "Any signal is a sum of sinusoids. The Fourier transform reports HOW MUCH of each frequency is present — the spectrum. Run on Sūrat ar-Raḥmān’s refrain indicator, it finds a sharp line at period ≈ 2.05 verses.",
  "DFT, frequency bins, magnitude, phase, Parseval — a real, baseline-backed spectral peak. Figures from Book6.xlsx (sūra-scale).")
s=Tt(prs,"The idea — decompose into sinusoids")
two(s,[L("TIME → FREQUENCY",18,True,NAVY),L("The DFT rewrites a length-N signal as a sum of N sinusoids. The magnitude spectrum says which periods carry the energy.",16.5,True,TEAL)],
 [L("A REPEAT IS A LINE",18,True,NAVY),L("A pattern repeating every 2 verses shows up as a spike at frequency ½ — the spectral fingerprint of the refrain.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — bins, magnitude, phase")
three(s,[L("FREQUENCY BINS",17,True,TEAL),L("N samples → N/2 frequencies, from slow (whole-sūra) to fast (verse-to-verse).",16)],
 [L("MAGNITUDE & PHASE",17,True,AMBER),L("Magnitude = how much of that period; phase = where it starts. We read magnitude here.",16)],
 [L("PARSEVAL",17,True,NAVY),L("Energy is conserved: total power in time = total power in frequency. A consistency check.",16)])
s=Tt(prs,"The spectrum of Ar-Raḥmān’s refrain")
finding2(s,
 {"title":"Top spectral components (magnitude)","cats":["f=%.2f"%ft[0][0],"f=%.2f"%ft[1][0],"f=%.2f"%ft[2][0]],"series":[("",[NAVY,TEAL,AMBER],[ft[0][1],ft[1][1],ft[2][1]])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Period (verses) at the peak","cats":["FFT peak","autocorr (L8)"],"series":[("",[TEAL,AMBER],[ft[0][2],2.0])],"legend":False,"fmt":"{:.2f}"},
 [L("A dominant line at f ≈ %.2f"%ft[0][0],17.5,True,TEAL),L("The largest spectral component sits at frequency %.2f → period ≈ %.2f verses. The refrain is a near-pure tone in ‘verse-space.’"%(ft[0][0],ft[0][2]),16)],
 [L("Frequency and autocorrelation agree",17.5,True,AMBER),L("FFT period %.2f matches the lag-2 autocorrelation peak from Lecture 8. Two independent tools, one period — that is corroboration."%ft[0][2],16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Time ∗ kernel = frequency × spectrum")
two(s,[L("THE CONVOLUTION THEOREM",18,True,TEAL),L("Convolution in time (Lecture 7) becomes multiplication in frequency. Filtering is just shaping the spectrum — the bridge to Lecture 11.",16.5,True,NAVY)],
 [L("WHY IT MATTERS",18,True,AMBER),L("Hard time-domain operations become easy in frequency. The FFT makes spectra computable in N log N — why digital audio exists.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — spectra everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("A prism splits light into a spectrum; the ear runs a biological Fourier transform; stars, molecules and engines are identified by their spectral lines.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same transform reads the sūra: the refrain is a spectral line at period 2. Structure becomes a peak.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — repetition is a frequency","A periodic structure in time is a sharp peak in the spectrum; the Ar-Raḥmān refrain is a line at period ≈ 2.","Dominant-frequency picking (L10) and filtering (L11) both operate on this spectrum.")
corpus_slide(prs,9)
scale_slide(prs,"Only robust summaries (total power) are safe on a short āyah.",
  "The spectrum itself needs many samples — computed here at SŪRA scale (78 verses), never on one verse.")
threads_block(prs,
 "The DFT is an exact, declared linear transform of the root/indicator signal; magnitudes are reproducible.",
 "Periodic structure — the refrain’s period, surfaced as a spectral peak the verse-list hides.",
 "Phase-scramble the spectrum (a declared null) to destroy structure while keeping power; the real peak does not survive scrambling.",
 "A spectral line reads back to an actual repeated verse (the refrain), not to an abstract frequency.",
 "A peak must beat a phase-randomized null AND random Arabic; here it does, matching the autocorrelation.")
finish_block(prs,
 "Why do FFT and autocorrelation report the same period? What would a verse with NO dominant frequency look like?",
 "The spectrum turns repetition into a peak; frequency and autocorrelation corroborate the same period-2 refrain.",
 "Reading meaning into tiny spectral bumps (spectral leakage / noise) without a null.",
 "Window the signal, compare peaks to a phase-randomized null, and report only lines that clear it.")
roadmap_pos(prs,9)
appslide(prs,[("① SŪRA","Ar-Raḥmān 55",TINT,TEAL),("② SIGNAL","refrain indicator",AMBERT,AMBER),("③ FFT","magnitude spectrum",TINT,TEAL),("④ PEAK","read the period",REDT,RED)],
  "Transform the refrain indicator and read the dominant line at f≈%.2f (period≈%.2f) — the same period the autocorrelation found."%(ft[0][0],ft[0][2]))
s=slide(prs); audit(s,"Ar-Raḥmān’s refrain is a spectral line at period ≈ 2.05, matching autocorrelation and beating a baseline.","Over-reading spectral leakage/noise as structure without a phase-randomized null.","A spectrum of a single short āyah is meaningless — silent until computed at sūra scale.")
s=slide(prs); takeaway(s,"Fourier analysis identifies stars, compresses audio (MP3), and powers every spectrum analyzer.","Decompose the sūra-scale signal into frequencies; a refrain is a peak; corroborate with autocorrelation and a null.")
counts[9]=save(prs,"09_Fourier_Spectrum","09_Fourier_Spectrum_Lecture.pptx")

# ============== L10 DOMINANT FREQUENCIES & RHYTHM ==============
fr=D["L10"]["fatiha_rootlen"]; fs=D["L10"]["fatiha_spectrum"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 10","Dominant Frequencies & Rhythm — the beat of a sūra",
  "Within a spectrum, the tallest peaks are the DOMINANT frequencies — the rhythm. Sūrat al-Fātiḥa’s seven verses, measured by root-length, give a per-verse rhythm signal: %s."%fr,
  "Fundamental, harmonics, peak-picking, meter — on real āyāt. Figures from Book6.xlsx (sūra-scale).")
s=Tt(prs,"The idea — find the strongest beats")
two(s,[L("PEAK-PICKING",18,True,NAVY),L("Scan the spectrum for the tallest components above the noise floor. The lowest strong peak is the FUNDAMENTAL — the main beat.",16.5,True,TEAL)],
 [L("RHYTHM = STRUCTURE IN TIME",18,True,NAVY),L("A regular alternation of long and short verses is a meter; the spectrum names its period and strength.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — fundamental & harmonics")
three(s,[L("FUNDAMENTAL",17,True,TEAL),L("The lowest dominant frequency — the basic repeat the rhythm is built on.",16)],
 [L("HARMONICS",17,True,AMBER),L("Integer multiples of the fundamental; their pattern gives the rhythm its ‘timbre.’",16)],
 [L("PEAK PROMINENCE",17,True,NAVY),L("How far a peak rises above its neighbours — the threshold that separates beat from noise.",16)])
s=Tt(prs,"Al-Fātiḥa — the per-verse rhythm signal")
line_signal(s,1.6,1.6,9.8,fr,col=TEAL,bh=2.6,labels=[str(i+1) for i in range(len(fr))])
panel(s,0.42,4.5,12.5,2.7,TINT,[L("root-length per verse = %s"%fr,17,True,NAVY),
  L("Seven verses, each measured by how many roots it carries. The rise and fall across the sūra is its rhythm — now we read its spectrum.",16.5,True,TEAL)],space=7)
s=Tt(prs,"The rhythm spectrum of Al-Fātiḥa")
finding2(s,
 {"title":"Rhythm signal (root-length/verse)","cats":[str(i+1) for i in range(len(fr))],"series":[("",[TEAL]*len(fr),fr)],"legend":False},
 {"title":"Its spectrum (magnitude/bin)","cats":["b%d"%i for i in range(len(fs))],"series":[("",[NAVY]+[AMBER]*(len(fs)-1),[round(x,1) for x in fs])],"legend":False,"fmt":"{:.1f}"},
 [L("A short, structured signal",17.5,True,TEAL),L("Seven samples — at the very edge of what a spectrum can resolve, so we read it cautiously and report the dominant bin only.",16)],
 [L("The dominant bin = the main beat",17.5,True,AMBER),L("The tallest non-zero component is the sūra’s fundamental rhythm; smaller bins are detail or noise, not over-interpreted.",16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Honesty — seven samples is short")
two(s,[L("THE LIMIT",18,True,RED),L("With only 7 verses the spectrum has 4 bins — barely enough. We report the dominant beat and refuse fine claims (that would be reading noise).",16.5,True,NAVY)],
 [L("THE FIX",18,True,TEAL),L("For rhythm with confidence, analyse longer sūras or the corpus. Al-Fātiḥa illustrates the method; it does not carry a strong claim.",16.5,True,NAVY)],sp=0.5,fa=REDT,fb=TINT)
s=Tt(prs,"Dual-domain — rhythm detection")
two(s,[L("عالم التكوين",18,True,AMBER),L("Beat-tracking finds tempo in music; gait analysis finds a walking rhythm; circadian analysis finds the daily beat in biology.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same peak-picking reads a sūra’s meter from its verse-length signal — rhythm as a measured frequency.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — the rhythm is the dominant peak","Among all spectral components, the tallest above the noise floor is the beat; everything else is detail.","Filtering (L11) keeps or removes chosen peaks; clustering (L16) groups sūras by their rhythm spectra.")
corpus_slide(prs,10)
scale_slide(prs,"A single dominant-beat read is the most a 7-verse sūra supports.",
  "Reliable rhythm/meter needs long sūras or the corpus — peak-pick at that scale.")
threads_block(prs,
 "Root-length per verse is a ratio measurement; peak prominence and the threshold are declared numbers.",
 "The fundamental rhythm — the dominant beat hidden in a list of verse lengths.",
 "Shuffle verse order (declared) to flatten the rhythm; a real meter loses its dominant peak under shuffling.",
 "A dominant beat reads back to an actual alternation of long/short verses in the sūra.",
 "A rhythm peak must clear a noise floor and a shuffle null before it counts — especially with few samples.")
finish_block(prs,
 "Is Al-Fātiḥa’s dominant bin trustworthy with only 7 verses? Which sūras are long enough for a confident meter?",
 "Rhythm is the dominant spectral peak; report it with prominence, and respect the sample-count limit.",
 "Reading several ‘beats’ from a 7-sample spectrum — most are noise, not meter.",
 "Report only the dominant peak on short sūras; move to long sūras/corpus for fine rhythm.")
roadmap_pos(prs,10)
appslide(prs,[("① SŪRA","Al-Fātiḥa",TINT,TEAL),("② SIGNAL","root-length/verse",AMBERT,AMBER),("③ SPECTRUM","peak-pick",TINT,TEAL),("④ BEAT","fundamental",REDT,RED)],
  "Read Al-Fātiḥa’s verse-length rhythm, pick the dominant bin, then switch to a long sūra to see a confident meter emerge.")
s=slide(prs); audit(s,"Peak-picking on a sūra’s rhythm signal reports the dominant beat, with prominence stated.","Over-reading many peaks from a short, low-resolution spectrum.","Fine rhythm on a 7-verse sūra is unsupported — silent until tested on longer text.")
s=slide(prs); takeaway(s,"Dominant-frequency detection drives music tempo, gait and circadian analysis.","Pick the tallest spectral peak above noise as the beat; honour the sample-count limit; validate against a shuffle null.")
counts[10]=save(prs,"10_Dominant_Frequencies_Rhythm","10_Dominant_Frequencies_Rhythm_Lecture.pptx")

# ============== L11 FILTERING ==============
debt=D["L11"]["debt_head"]; 
def mov(x,w):
    o=[]
    for i in range(len(x)):
        a=max(0,i-w//2); b=min(len(x),i+w//2+1); o.append(round(sum(x[a:b])/(b-a),1))
    return o
lp=mov(debt,5); hp=[round(debt[i]-lp[i],1) for i in range(len(debt))]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 11","Filtering — separating signal from noise",
  "A filter keeps some frequencies and removes others. Low-pass keeps the slow trend; high-pass keeps the fast detail. Test signal: 2:282 آية الدَّيْن — the longest verse (%d root-tokens), our noisiest case."%D["L11"]["debt_n"],
  "Low/high/band-pass, cutoff frequency, denoising, ringing — on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — keep some frequencies, drop others")
two(s,[L("LOW-PASS = the trend",18,True,NAVY),L("Remove the fast wiggles, keep the slow contour. It is the moving average of Lecture 6, seen in the frequency domain.",16.5,True,TEAL)],
 [L("HIGH-PASS = the detail",18,True,NAVY),L("Remove the slow drift, keep the rapid changes — the verse’s sharp transitions and texture.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — cutoff & trade-offs")
three(s,[L("CUTOFF",17,True,TEAL),L("The frequency where the filter switches from keep to remove — a declared number.",16)],
 [L("BAND-PASS",17,True,AMBER),L("Keep a middle band only — isolate a chosen rhythm (e.g., the refrain period).",16)],
 [L("RINGING",17,True,RED),L("Too sharp a cutoff makes oscillation artifacts — a filter can ADD structure if abused.",16)])
s=Tt(prs,"2:282 — low-pass vs high-pass")
finding2(s,
 {"title":"Raw vs low-pass (first 12 roots)","cats":[str(i+1) for i in range(12)],"series":[("raw",GREY,debt[:12]),("low-pass",TEAL,lp[:12])],"legend":True},
 {"title":"High-pass = detail (|first 12|)","cats":[str(i+1) for i in range(12)],"series":[("",[AMBER]*12,[abs(x) for x in hp[:12]])],"legend":False},
 [L("Low-pass = the verse’s drift",17.5,True,TEAL),L("The smoothed line follows the slow trend of the debt verse and suppresses single-root spikes — denoising.",16)],
 [L("High-pass = the texture",17.5,True,AMBER),L("The residual isolates the rapid common↔rare root transitions — the fine structure a trend hides.",16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Denoising — what is signal, what is noise?")
two(s,[L("A MODELLING CHOICE",18,True,NAVY),L("‘Noise’ is whatever you decide to remove. Declaring the cutoff first prevents tuning the filter until the verse ‘says’ what you wanted.",16.5,True,TEAL)],
 [L("RECONSTRUCT TO CHECK",18,True,AMBER),L("Low-pass + high-pass should rebuild the original (Parseval). If they don’t, the filter is lying.",16.5,True,NAVY)],sp=0.5,fa=TINT2,fb=AMBERT)
s=Tt(prs,"Dual-domain — filters are everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("Noise-cancelling headphones, ECG baseline removal, radio tuning, image sharpening — all are filters choosing frequency bands.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same filters read the verse: keep its trend, or its detail, or a chosen rhythm — declared, reversible, validated.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — a filter shapes the spectrum","Filtering keeps or removes chosen frequencies; low-pass is trend, high-pass is detail, band-pass isolates a rhythm.","Choosing what to keep is feature selection — it feeds distance (L13) and clustering (L16).")
corpus_slide(prs,11)
scale_slide(prs,"Short verses give little to filter; the debt verse (2:282) is long enough to show trend vs detail.",
  "Sharp frequency-domain filters need many samples — apply at sūra/corpus scale.")
threads_block(prs,
 "The cutoff and filter type are declared; filtering is an exact linear operation, checkable by reconstruction.",
 "The separation of slow theme from fast texture — and the isolation of a chosen rhythm band.",
 "Sweep the cutoff (declared) and reconstruct; a real trend is stable across cutoffs, an artifact (ringing) is not.",
 "A kept band reads back to real verse structure (drift or transitions); ringing reads back to nothing.",
 "A ‘denoised pattern’ must beat random Arabic; low-pass makes a random verse look smooth too.")
finish_block(prs,
 "What is ‘noise’ in a verse — and who decides? When does a sharp filter invent ringing?",
 "Filtering chooses a frequency band; declare the cutoff, reconstruct to verify, and validate the kept structure.",
 "Tuning the cutoff until the verse shows the pattern you hoped for.",
 "Fix the cutoff first; reconstruct (low+high=raw); require the kept structure to beat a baseline.")
roadmap_pos(prs,11)
appslide(prs,[("① VERSE","2:282",TINT,TEAL),("② TYPE","low/high/band",AMBERT,AMBER),("③ CUTOFF","slider",TINT,TEAL),("④ COMPARE","before/after",REDT,RED)],
  "Apply a low-pass to the debt verse and watch the trend emerge; switch to high-pass for the texture; sweep the cutoff and reconstruct.")
s=slide(prs); audit(s,"Filtering is an exact, declared, reversible operation (low+high reconstruct the raw signal).","Tuning the cutoff to manufacture a pattern, or reading ringing as real structure.","Which band is ‘signal’ is question-dependent — declared, not assumed.")
s=slide(prs); takeaway(s,"Filters run noise-cancelling, radio, ECG cleanup and image sharpening.","Choose a band on the root signal (low=trend, high=detail); declare the cutoff; reconstruct and validate.")
counts[11]=save(prs,"11_Filtering","11_Filtering_Lecture.pptx")

# ============== L12 ENERGY, NORM & ENTROPY ==============
qd=D["L12"]["qadr"]; kw=D["L12"]["kawthar"]
qH=qd["entropy"][0]; qn=qd["entropy"][1]; qd_dist=qd["entropy"][2]; qrms=qd["rms"]
kH=kw["entropy"][0]; kn=kw["entropy"][1]; kd_dist=kw["entropy"][2]; krms=kw["rms"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 12","Energy, Norm & Entropy — magnitude and information",
  "Three scalar summaries of a signal: ENERGY (how big), NORM (its length as a vector), ENTROPY (how varied/uncertain). Compared on 97 سُورَة الْقَدْر and 108 سُورَة الْكَوْثَر.",
  "Energy, L1/L2 norm, RMS, Shannon entropy — on real āyāt. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — reduce a signal to a number")
two(s,[L("MAGNITUDE",18,True,NAVY),L("Energy = sum of squares; RMS = its root-mean. The L2 norm is the vector’s length. These say how ‘big’ the root signal is.",16.5,True,TEAL)],
 [L("INFORMATION",18,True,NAVY),L("Shannon entropy = how spread the root distribution is. High entropy = many different roots; low = a few repeated.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — norms & entropy")
three(s,[L("L2 NORM / RMS",17,True,TEAL),L("√Σx² — dominated by the peaks (frequent roots). RMS normalises by length.",16)],
 [L("L1 NORM",17,True,AMBER),L("Σ|x| — total amplitude; less peak-dominated than L2.",16)],
 [L("SHANNON ENTROPY",17,True,NAVY),L("−Σp·log₂p over the root distribution — bits of uncertainty per root.",16)])
s=Tt(prs,"Al-Qadr vs Al-Kawthar — entropy & RMS")
finding2(s,
 {"title":"Root entropy (bits)","cats":["97 Al-Qadr","108 Al-Kawthar"],"series":[("",[TEAL,AMBER],[qH,kH])],"legend":False,"fmt":"{:.2f}"},
 {"title":"RMS amplitude","cats":["97 Al-Qadr","108 Al-Kawthar"],"series":[("",[TEAL,AMBER],[qrms,krms])],"legend":False,"fmt":"{:.0f}"},
 [L("Al-Qadr — higher entropy (%.2f)"%qH,17.5,True,TEAL),L("%d roots, %d distinct: more variety, more ‘information,’ less repetition. The Night-of-Decree sūra spreads across many roots."%(qn,qd_dist),16)],
 [L("Al-Kawthar — lower entropy (%.2f)"%kH,17.5,True,AMBER),L("%d roots, %d distinct: concise and concentrated, with higher RMS (%d) — fewer, heavier roots."%(kn,kd_dist,krms),16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"What entropy is, and is not")
two(s,[L("IT MEASURES SPREAD",18,True,TEAL),L("Entropy is high when roots are many and even, low when few and repeated. It is a real, computable property of the sūra’s root distribution.",16.5,True,NAVY)],
 [L("IT IS NOT ‘DEPTH’",18,True,RED),L("Low entropy ≠ shallow; Al-Kawthar is concise, not poor. Entropy measures variety, never meaning or value.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Dual-domain — energy & information")
two(s,[L("عالم التكوين",18,True,AMBER),L("Signal energy sets loudness and SNR; Shannon entropy founds data compression and channel capacity; sequence entropy measures genomic complexity.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same scalars summarise a sūra: its amplitude (energy) and its variety (entropy) — two numbers that place it among the others.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — a signal in a few scalars","Energy/RMS give magnitude; entropy gives information. Two sūras separate cleanly: Al-Qadr varied (H=%.1f), Al-Kawthar concentrated (H=%.1f)."%(qH,kH),
  "These scalars are the coordinates for distance (L13), embeddings (L14) and clustering (L16).")
corpus_slide(prs,12)
scale_slide(prs,"Energy, norm and entropy are single numbers — robust even on a short sūra.",
  "Comparing the whole corpus by these scalars is a corpus-scale study (L15–L16).")
threads_block(prs,
 "Energy, norm and entropy are exact functions of the root signal/distribution — ratio-scale, reproducible.",
 "How concentrated vs varied a sūra is — information the verse list does not state.",
 "Reorder roots: energy and entropy are PERMUTATION-INVARIANT (a feature, not a bug) — they summarise content, not order.",
 "High/low entropy reads back to the actual root inventory (many distinct vs few repeated roots).",
 "An entropy ‘difference’ between sūras must beat a length-matched random-Arabic difference to count.")
finish_block(prs,
 "Why is entropy permutation-invariant while autocorrelation is not? Does low entropy mean a sūra is ‘simpler’?",
 "Energy and entropy compress a sūra into magnitude and variety — clean coordinates that separate Al-Qadr from Al-Kawthar.",
 "Equating low entropy with low value — entropy measures spread, not worth.",
 "Compare entropy to a length-matched baseline; report it as variety, never as quality.")
roadmap_pos(prs,12)
appslide(prs,[("① SŪRA","97 vs 108",TINT,TEAL),("② ENERGY","RMS / norm",AMBERT,AMBER),("③ ENTROPY","bits",TINT,TEAL),("④ COMPARE","place them",REDT,RED)],
  "Compute energy and entropy for Al-Qadr and Al-Kawthar; see Al-Qadr higher-entropy (%.2f) and Al-Kawthar higher-RMS (%d)."%(qH,krms))
s=slide(prs); audit(s,"Energy, norm and entropy are exact scalar summaries of the root signal.","Reading low entropy as low value, or energy as importance.","Whether an entropy gap is ‘meaningful’ needs a baseline — silent until compared.")
s=slide(prs); takeaway(s,"Energy founds SNR and loudness; Shannon entropy founds compression, channel capacity and genomic complexity.","Summarise the root signal by magnitude (energy/RMS) and variety (entropy); validate differences against a baseline.")
counts[12]=save(prs,"12_Energy_Norm_Entropy","12_Energy_Norm_Entropy_Lecture.pptx")

# ============== L13 DISTANCE & SIMILARITY ==============
fl=D["L13"]["falaq_len"]; ns=D["L13"]["nas_len"]; cs=D["L13"]["cosine_trunc"]; cm=D["DIV"]["cosine"]["median"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 13","Distance & Similarity — comparing two verses",
  "How alike are two verses as vectors? Euclidean distance, cosine similarity, correlation, and DTW each answer differently. Compared on the مُعَوِّذَتَان — 113 سُورَة الْفَلَق and 114 سُورَة النَّاس.",
  "Cosine, Euclidean, DTW, the similarity matrix — read against a whole-corpus baseline. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — turn ‘alike’ into a number")
two(s,[L("DISTANCE vs SIMILARITY",18,True,NAVY),L("Euclidean distance = how far apart two root-vectors sit; cosine similarity = how aligned their directions are (length-independent). Small distance / high cosine = alike.",16.5,True,TEAL)],
 [L("WHY MULTIPLE METRICS",18,True,NAVY),L("Cosine ignores magnitude; Euclidean does not; DTW allows stretch when lengths differ. The metric encodes what ‘similar’ means.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — the metrics")
three(s,[L("EUCLIDEAN / COSINE",17,True,TEAL),L("√Σ(a−b)² vs a·b/|a||b|. Cosine is the workhorse for text.",16)],
 [L("CORRELATION",17,True,AMBER),L("Cosine of mean-centred vectors — shared shape, not shared size.",16)],
 [L("DTW",17,True,NAVY),L("Dynamic Time Warping aligns sequences of different length by stretching — needed since 113 has %d roots, 114 has %d."%(fl,ns),16)])
s=Tt(prs,"113 vs 114 — the مُعَوِّذَتَان compared")
finding2(s,
 {"title":"Cosine similarity","cats":["113 vs 114","corpus median pair"],"series":[("",[TEAL,GREY],[cs,cm])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Length (root-tokens)","cats":["113 Al-Falaq","114 An-Nās"],"series":[("",[TEAL,AMBER],[fl,ns])],"legend":False},
 [L("Above the typical pair",17.5,True,TEAL),L("113 and 114 score cosine %.2f vs a corpus median of %.2f — the twin ‘refuge’ sūras are more alike than a random verse pair, as expected."%(cs,cm),16)],
 [L("Different lengths → use DTW",17.5,True,AMBER),L("Al-Falaq (%d roots) and An-Nās (%d) differ in length, so a fair comparison aligns them with DTW rather than truncating."%(fl,ns),16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"The similarity matrix — comparing many at once")
two(s,[L("EVERY PAIR AT ONCE",18,True,TEAL),L("Stack all verse-vectors and compute pairwise similarity → a matrix whose bright blocks are families of alike verses. Reordering it by similarity reveals the groups (Lecture 16).",16.5,True,NAVY)],
 [L("THE SEED OF CLUSTERING",18,True,AMBER),L("Distance is the raw material for embeddings (L14), PCA (L15) and clustering (L16) — everything ‘near/far’ starts here.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — distance is everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("Sequence alignment (BLAST) scores how similar two genes are; DTW matches speech to templates; cosine ranks documents in search.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same metrics rank how alike two verses are — on the root anchor, against a corpus baseline. Similarity becomes measurable.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — the metric defines ‘similar’","Cosine, Euclidean and DTW answer different questions; choose and declare one, and read its value against the corpus.",
  "Distances feed embeddings (L14), PCA (L15) and clustering (L16) — the whole of Unit E rests on them.")
corpus_slide(prs,13)
scale_slide(prs,"Single pair distances are robust at āyah scale; DTW handles unequal lengths.","A full similarity matrix over all 6,236 verses is a corpus-scale computation.")
threads_block(prs,
 "Distances are exact functions of the root-vectors; the chosen metric is declared in advance.",
 "Families of alike verses — the near/far structure the verse list does not show.",
 "Reorder the similarity matrix by similarity (a declared permutation) to expose blocks; random reordering hides them.",
 "A ‘near’ pair must read back to genuinely related verses (the twin refuge sūras), not coincidental overlap.",
 "A pair’s similarity must beat the corpus baseline (median 0.51) before it counts as unusually alike.")
finish_block(prs,
 "Why is cosine preferred over Euclidean for verses of different length? When is DTW worth its cost?",
 "Distance turns ‘alike’ into a number; the مُعَوِّذَتَان sit above the typical pair — read against the whole corpus.",
 "Calling two verses ‘similar’ from one metric without a baseline — most pairs already score ~0.5.",
 "Declare the metric; compare to the corpus distribution; for unequal lengths use DTW, not truncation.")
roadmap_pos(prs,13)
appslide(prs,[("① PAIR","113 & 114",TINT,TEAL),("② METRIC","cosine/Euclid/DTW",AMBERT,AMBER),("③ SCORE","vs baseline",TINT,TEAL),("④ MATRIX","many at once",REDT,RED)],
  "Score 113 vs 114 by cosine (%.2f) against the corpus median (%.2f); switch to DTW to align their unequal lengths."%(cs,cm))
s=slide(prs); audit(s,"Distances/similarities are exact, declared functions of the root-vectors.","Reading a single similarity as ‘meaningful’ without the corpus baseline.","The ‘right’ metric is question-dependent — declared, not assumed.")
s=slide(prs); takeaway(s,"Cosine ranks search results, BLAST aligns genes, DTW matches speech — distance is the basis of comparison.","Pick and declare a metric on the root-vectors; the مُعَوِّذَتَان score above the typical pair; always read against the corpus.")
counts[13]=save(prs,"13_Distance_Similarity","13_Distance_Similarity_Lecture.pptx")

# ============== L14 EMBEDDINGS ==============
e=D["L14"]; rhm=e["nn_rhm"]; amn=e["nn_ءmn"]; ale=e["nn_ءle"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 14","Embeddings — the root as a point in meaning-space",
  "Instead of one number per root, learn a whole VECTOR from how roots co-occur. Roots used in similar contexts land near each other. Learned over 51,044 root-tokens, رحم’s nearest neighbour is غفر (0.82).",
  "Vector space, dimensionality, semantic axes, nearest neighbours — a real, read-back-able result. Figures from Book6.xlsx.")
s=Tt(prs,"The idea — meaning from company")
two(s,[L("DISTRIBUTIONAL HYPOTHESIS",18,True,NAVY),L("‘A root is known by the company it keeps.’ Build each root a vector from the roots it co-occurs with across āyāt; similar contexts → similar vectors.",16.5,True,TEAL)],
 [L("FROM LABEL TO MEANING",18,True,NAVY),L("This finally turns the NOMINAL root-identity into a numeric vector that RESPECTS meaning — the proper way to use identity in DSP/ML.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — the embedding")
three(s,[L("VECTOR SPACE",17,True,TEAL),L("Each of 1,702 roots → a dense vector (here 50-D from PPMI+SVD over co-occurrence).",16)],
 [L("NEAREST NEIGHBOURS",17,True,AMBER),L("Cosine in this space ranks the closest roots — its ‘semantic field.’",16)],
 [L("SEMANTIC AXES",17,True,NAVY),L("Directions in the space can align with meaning (mercy↔punishment, faith↔denial).",16)])
s=Tt(prs,"رحم — its semantic field, learned from the text")
finding2(s,
 {"title":"Nearest roots to رحم (cosine)","cats":[w for w,_ in rhm[:4]],"series":[("",[NAVY,TEAL,TEAL,AMBER],[v for _,v in rhm[:4]])],"legend":False,"fmt":"{:.2f}"},
 {"title":"Nearest roots to ءمن (faith)","cats":[w for w,_ in amn[:4]],"series":[("",[NAVY,TEAL,TEAL,AMBER],[v for _,v in amn[:4]])],"legend":False,"fmt":"{:.2f}"},
 [L("رحم → غفر · ءجر · فضل",17.5,True,TEAL),L("Mercy’s nearest roots are forgiveness (غفر 0.82), reward (ءجر), grace (فضل) — a coherent mercy-and-grace field, learned, not assigned.",16)],
 [L("ءمن → عمل · طوع · ءجر",17.5,True,AMBER),L("Faith’s neighbours are deeds (عمل 0.78), obedience (طوع), reward (ءجر) — the Qur’an’s own pairing الذين آمنوا وعملوا الصالحات, recovered by geometry.",16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"The read-back — geometry that matches the text")
two(s,[L("NEIGHBOURS ARE REAL KINSHIPS",18,True,TEAL),L("ءله → طوع (obey), وکل (trust), رحم (mercy): the embedding places God beside obedience, reliance and mercy — relations the verses actually assert.",16.5,True,NAVY)],
 [L("THE ANCHOR’S PAYOFF",18,True,AMBER),L("Because we embed ROOTS (meaning units), neighbours are interpretable. Embedding surface tokens would mix in ال and grammar — less semantic.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — embeddings everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("word2vec/GloVe power search and translation; protein and gene embeddings predict function from sequence context.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same method maps the Qur’an’s roots into a meaning-space where رحم sits by غفر — semantics made geometric.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — identity becomes geometry","Embeddings turn the nominal root into a dense vector whose distances mirror meaning (رحم≈غفر, ءمن≈عمل).",
  "This space is the input to clustering (L16) and the capstone (L17); the semantic anchor is decisive here.")
corpus_slide(prs,14)
scale_slide(prs,"A root’s embedding is a corpus-learned object — it needs the whole corpus, not one verse.","Embeddings are inherently corpus-scale; single-āyah ‘embeddings’ are not meaningful.")
threads_block(prs,
 "The embedding is learned by a stated procedure (PPMI + SVD over co-occurrence); neighbours are reproducible.",
 "Semantic neighbourhoods — meaning relations between roots that no single verse states outright.",
 "Re-train on shuffled contexts (a declared null): true neighbours (رحم↔غفر) collapse, confirming they come from real co-occurrence.",
 "A neighbour must read back to a genuine textual kinship — رحم↔غفر, ءمن↔عمل (faith-and-works) do.",
 "Neighbour cosines must beat a shuffled-context baseline before they count as semantic, not incidental.")
finish_block(prs,
 "Why are رحم’s neighbours interpretable but a surface-token embedding’s would not be? What axis separates faith from denial?",
 "Embeddings turn root-identity into meaning-respecting geometry; رحم≈غفر and ءمن≈عمل are recovered, not imposed.",
 "Trusting neighbour lists without a shuffled-context null — co-occurrence can be incidental.",
 "Compare neighbour cosines to a shuffled-context baseline; report only kinships that survive and read back to the text.")
roadmap_pos(prs,14)
appslide(prs,[("① ROOT","enter رحم",TINT,TEAL),("② EMBED","co-occurrence",AMBERT,AMBER),("③ NEIGHBOURS","top cosine",TINT,TEAL),("④ PROJECT","2-D map",REDT,RED)],
  "Type رحم and read its nearest roots (غفر 0.82, فضل, ءجر); switch to ءمن and watch the faith-and-works field appear.")
s=slide(prs); audit(s,"Embedding neighbours are computed and reproducible; رحم↔غفر, ءمن↔عمل read back to real textual kinships.","Treating every neighbour as exact synonymy — cosine ranks association, not identity of meaning.","Whether a far-down neighbour is ‘real’ needs the shuffled-context baseline — silent until checked.")
s=slide(prs); takeaway(s,"Embeddings underpin modern search, translation and protein-function prediction.","Learn root vectors from co-occurrence; distances mirror meaning (رحم≈غفر); validate neighbours against a shuffled null and the text.")
counts[14]=save(prs,"14_Embeddings","14_Embeddings_Lecture.pptx")

# ============== L15 PCA ==============
ve=D["L15"]["variance_explained"]; feats=D["L15"]["features"]; load=D["L15"]["pc1_loadings"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 15","Dimensionality Reduction (PCA) — the axes of variation",
  "Describe each of the 114 sūras by five features, then ask: which few combinations explain most of the differences? PCA answers — here the first two principal components capture 81% of all variation.",
  "Variance, principal components, scree, projection — over all 114 sūras. Figures from Book6.xlsx (corpus-scale).")
s=Tt(prs,"The idea — find the directions that matter")
two(s,[L("MANY FEATURES → FEW AXES",18,True,NAVY),L("Each sūra is a point in 5-D (n-verses, n-roots, mean root-length, type-token ratio, top-root share). PCA rotates to the axes of greatest spread.",16.5,True,TEAL)],
 [L("COMPRESS WITHOUT LOSING MUCH",18,True,NAVY),L("Keep the top components and you keep most of the variation in 2-D you can plot — the rest is near-flat.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — variance & components")
three(s,[L("VARIANCE",17,True,TEAL),L("Spread along an axis. PC1 is the direction of maximum variance; PC2 the next, orthogonal.",16)],
 [L("SCREE",17,True,AMBER),L("The variance-per-component curve; where it elbows tells you how many axes to keep.",16)],
 [L("PROJECTION",17,True,NAVY),L("Drop each sūra onto the top components — a faithful low-D map.",16)])
s=Tt(prs,"The scree — two axes hold 81% of sūra variation")
finding2(s,
 {"title":"Variance explained per PC (%)","cats":["PC1","PC2","PC3","PC4","PC5"],"series":[("",[NAVY,TEAL,TEAL,AMBER,GREY],[round(v*100,1) for v in ve])],"legend":False,"fmt":"{:.0f}"},
 {"title":"PC1 loadings (feature weights)","cats":["n_ay","n_tok","len","TTR","top%"],"series":[("",[TEAL,TEAL,AMBER,RED,AMBER],[abs(x) for x in load])],"legend":False,"fmt":"{:.2f}"},
 [L("PC1 %.0f%% + PC2 %.0f%% = %.0f%%"%(ve[0]*100,ve[1]*100,(ve[0]+ve[1])*100),17.5,True,TEAL),L("Two numbers per sūra recover four-fifths of how sūras differ — a huge, honest compression of the corpus.",16)],
 [L("PC1 ≈ size & richness",17.5,True,AMBER),L("Its heaviest loadings are verse-count, token-count and type-token ratio — PC1 is essentially ‘how big and varied is the sūra.’",16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Reading the axes — and the honesty about it")
two(s,[L("INTERPRET, THEN VALIDATE",18,True,TEAL),L("PC1 reads as size/richness — interpretable. But a PC is only credible if it maps back to something real; an uninterpretable axis is rejected, not narrated.",16.5,True,NAVY)],
 [L("RECONSTRUCTION ERROR",18,True,AMBER),L("Rebuild the sūras from 2 PCs; the small leftover error confirms 2-D is a fair summary — the read-back for PCA.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"Dual-domain — PCA everywhere")
two(s,[L("عالم التكوين",18,True,AMBER),L("PCA finds the main axes of genetic variation across populations, compresses face images (eigenfaces), and denoises spectra.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same rotation finds the main axes along which sūras vary — size, richness — from their root-feature vectors.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — a few axes explain the most","PCA rotates many features to the directions of greatest spread; for the 114 sūras, two axes hold 81%.",
  "The 2-D projection is the map clustering (L16) groups; PCA is compression with a read-back (reconstruction).")
corpus_slide(prs,15)
scale_slide(prs,"Per-sūra feature vectors are robust; PCA needs the population of sūras.","PCA is inherently corpus-scale — it is a statement about all 114 sūras together.")
threads_block(prs,
 "Features are ratio measurements; PCA is an exact, declared linear rotation; variance-explained is reproducible.",
 "The principal axes of variation — the few combinations along which sūras actually differ.",
 "Project and sort sūras by PC score (a declared reordering) to expose the gradient; random axes explain little.",
 "A principal component must read back to an interpretable contrast (PC1 = size/richness) or be rejected as an artifact.",
 "An axis’s explanatory power must exceed what random features give; PC1’s 62% far beats a random-feature baseline.")
finish_block(prs,
 "What does PC2 mean here? When is an uninterpretable principal component still useful — or just noise?",
 "PCA compresses the 114 sūras to two meaningful axes (size, richness) holding 81% — with a reconstruction read-back.",
 "Narrating a principal component that maps to nothing interpretable as a ‘discovery.’",
 "Interpret PCs, check reconstruction error, and reject axes that neither read back nor beat a random-feature baseline.")
roadmap_pos(prs,15)
appslide(prs,[("① FEATURES","5 per sūra",TINT,TEAL),("② PCA","rotate",AMBERT,AMBER),("③ SCREE","variance",TINT,TEAL),("④ MAP","2-D plot",REDT,RED)],
  "Compute the 5 features for all 114 sūras, run PCA, read the scree (PC1 %.0f%%, PC2 %.0f%%), and plot the 2-D map."%(ve[0]*100,ve[1]*100))
s=slide(prs); audit(s,"PCA is an exact rotation; PC1+PC2 explain 81%% of sūra variation, PC1 interpretable as size/richness.","Reading meaning into an uninterpretable component, or into PCs that barely beat random features.","PC2/PC3 interpretation is uncertain here — set aside unless it reads back and beats a baseline.")
s=slide(prs); takeaway(s,"PCA drives population genetics, eigenfaces and spectral denoising — compression that keeps the signal.","Describe sūras by root-features, rotate to the axes of greatest variance (81% in 2-D), interpret and validate by reconstruction.")
counts[15]=save(prs,"15_PCA","15_PCA_Lecture.pptx")

# ============== L16 CLUSTERING & SPECTROGRAM ==============
csz=D["L16"]["cluster_sizes"]; mnay=D["L16"]["mean_nay_by_cluster"]
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 16","Clustering & the Spectrogram — grouping, and the bridge to 2-D",
  "Clustering groups sūras that are alike, with no labels given. On their root-features the 114 sūras fall into two natural groups of %d and %d — separated mainly by length (mean %.0f vs %.0f verses)."%(csz[0],csz[1],mnay[0],mnay[1]),
  "k-means, silhouette, the spectrogram (time-frequency) — and the bridge to the 2-D image course. Figures from Book6.xlsx (corpus-scale).")
s=Tt(prs,"The idea — let the data group itself")
two(s,[L("UNSUPERVISED GROUPING",18,True,NAVY),L("No labels: cluster sūras by proximity in feature/PCA space. The groups that emerge are the corpus’s own structure, not ours.",16.5,True,TEAL)],
 [L("THE SPECTROGRAM",18,True,NAVY),L("Slide a window along a long signal and stack its spectra → a 2-D time-frequency image. This is the bridge from 1-D signals to the 2-D image course.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Conceptual foundation — clustering & STFT")
three(s,[L("k-MEANS",17,True,TEAL),L("Pick k centres; assign each sūra to the nearest; recompute; repeat. Declared k.",16)],
 [L("SILHOUETTE",17,True,AMBER),L("Measures how well-separated the clusters are — validates k against alternatives.",16)],
 [L("STFT → SPECTROGRAM",17,True,NAVY),L("Short-time Fourier transform: spectrum vs position — a 2-D picture of a 1-D signal.",16)])
s=Tt(prs,"The 114 sūras — two natural groups")
finding2(s,
 {"title":"Cluster sizes (114 sūras)","cats":["cluster A","cluster B"],"series":[("",[TEAL,AMBER],csz)],"legend":False},
 {"title":"Mean verses per cluster","cats":["A","B"],"series":[("",[TEAL,AMBER],mnay)],"legend":False,"fmt":"{:.0f}"},
 [L("A: %d short sūras (~%.0f verses)"%(csz[0],mnay[0]),17.5,True,TEAL),L("The larger cluster gathers the short, dense sūras — many Meccan in character (short, high root-turnover).",16)],
 [L("B: %d long sūras (~%.0f verses)"%(csz[1],mnay[1]),17.5,True,AMBER),L("The other gathers the long sūras (~%.0f verses) — the length axis dominates the split, as PCA predicted."%mnay[1],16)],
 fillA=TINT,fillB=AMBERT)
s=Tt(prs,"Honesty — clusters describe, they do not label")
two(s,[L("WHAT THE SPLIT IS",18,True,TEAL),L("This is a LENGTH/richness split (the PC1 axis), and it loosely tracks the Meccan/Medinan contrast — but we computed length, not revelation place.",16.5,True,NAVY)],
 [L("WHAT IT IS NOT",18,True,RED),L("We do not claim to have recovered Meccan/Medinan from signal alone; that would need the actual labels and a validated test. Clusters describe variation; they do not name it.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Dual-domain — clustering & spectrograms")
two(s,[L("عالم التكوين",18,True,AMBER),L("Clustering groups cell types in genomics; spectrograms read speech, birdsong, seismic waves and gravitational chirps.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("The same tools group sūras and turn a sūra’s signal into a 2-D image — handing off to the surah-as-image course.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — structure without labels","Clustering finds the corpus’s own groups (here a length/richness split of 114 sūras); the spectrogram turns 1-D into 2-D.",
  "This is the bridge to the image course — and the capstone (L17) ties every tool together.")
corpus_slide(prs,16)
scale_slide(prs,"A single sūra can be turned into a spectrogram if long enough.","Clustering is a statement about ALL 114 sūras — purely corpus-scale.")
threads_block(prs,
 "Features are ratio measurements; k and the metric are declared; cluster assignment is reproducible from a fixed seed.",
 "The corpus’s own groupings — families of sūras, and the time-frequency structure of a sūra.",
 "Reorder the similarity matrix by cluster (declared) to reveal blocks; silhouette guards against imposing groups that aren’t there.",
 "A cluster must read back to a real shared trait (length/richness here), not a tidy artifact of the chosen k.",
 "Cluster structure must beat a null (random features give weak silhouettes) before it is called real.")
finish_block(prs,
 "Does the two-cluster split really track Meccan/Medinan — how would you TEST that with the labels? Is k=2 best by silhouette?",
 "Clustering reveals a length/richness split of the 114 sūras; the spectrogram bridges 1-D signals to 2-D images.",
 "Announcing ‘the signal recovered Meccan vs Medinan’ from a length-based cluster, with no labels or test.",
 "Name the split by its measured trait (length); to claim Meccan/Medinan, bring the labels and beat a null.")
roadmap_pos(prs,16)
appslide(prs,[("① FEATURES","114 sūras",TINT,TEAL),("② k-MEANS","choose k",AMBERT,AMBER),("③ SILHOUETTE","validate k",TINT,TEAL),("④ SPECTROGRAM","1-D→2-D",REDT,RED)],
  "Cluster the 114 sūras (k=2 → groups of %d and %d), check the silhouette, then build a spectrogram to cross into the image course."%(csz[0],csz[1]))
s=slide(prs); audit(s,"Clustering yields two reproducible sūra groups split by length/richness (PC1), validated by silhouette.","Naming a length-based cluster ‘Meccan/Medinan’ without the labels or a test.","Whether finer (k>2) structure is real is uncertain — silent until silhouette and a null support it.")
s=slide(prs); takeaway(s,"Clustering groups genomes and customers; spectrograms read speech, seismology and gravitational waves.","Let sūras group themselves on root-features (a length/richness split); the spectrogram turns 1-D into 2-D — the bridge to images.")
counts[16]=save(prs,"16_Clustering_Spectrogram","16_Clustering_Spectrogram_Lecture.pptx")

# ============== L17 SYNTHESIS & CAPSTONE ==============
prs=deck()
titleslide(prs,"THE TWO BOOKS · Ayah as Signal (1-D) · Lecture 17","Synthesis & Capstone — one verse, the whole pipeline",
  "We close by running the entire course on one verse, anchored on its ROOTS, and auditing every step. 1:1 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ → roots سمو·ءله·رحم·رحم → [381, 2848, 339, 339].",
  "Digitize → transform → validate → read back, end to end, on the root anchor. Figures from Book6.xlsx.")
s=Tt(prs,"The arc — five units, one object")
two(s,[L("WHAT WE BUILT",18,True,NAVY),L("A (foundations) → B (waveform, sampling, smoothing, convolution, autocorrelation) → C (Fourier, rhythm, filtering) → D (energy, distance, embeddings) → E (PCA, clustering).",16.5,True,TEAL)],
 [L("ONE ANCHOR THROUGHOUT",18,True,NAVY),L("Every tool acted on the ROOT signal — the unit of meaning — with surface and morphology as complements. Same object, seventeen lenses.",16.5)],sp=0.5,fa=TINT,fb=TINT2)
s=Tt(prs,"Step 1–2 — digitize and read the waveform")
band(s,0.42,1.18,12.5,0.4,TINT,"1:1 roots سمو·ءله·رحم·رحم — the capstone signal",TEAL)
line_signal(s,2.0,1.75,9.0,D["L17"]["rootfreq"],col=TEAL,bh=2.5,labels=D["L17"]["roots"],vmax=2848)
panel(s,0.42,5.5,12.5,1.7,TINT2,[L("x = [381, 2848, 339, 339]",18,True,NAVY),
  L("Waveform: a tall peak (ءله) and a repeated mid root (رحم×2) — prominence and repetition, the verse’s form before its sense.",16.5,True,TEAL)],space=6)
s=Tt(prs,"Step 3–4 — transform and measure")
three(s,[L("SMOOTH / DIFFERENCE",17,True,TEAL),L("Trend vs change across the four roots (L6); convolution with a kernel (L7).",16)],
 [L("ENERGY / ENTROPY",17,True,AMBER),L("Magnitude and variety of the root signal (L12) — two scalars placing 1:1 among the sūras.",16)],
 [L("DISTANCE / EMBED",17,True,NAVY),L("Compare 1:1 to other openings (L13); رحم sits by غفر in embedding space (L14).",16)])
s=Tt(prs,"Step 5 — validate, the whole point")
two(s,[L("BEAT NULL + BASELINE",18,True,TEAL),L("Every claim about 1:1 is checked: beat a sampled null, beat random Arabic, correct for the search. The repeated رحم is real; a ‘pattern’ that is generic to Arabic is dropped.",16.5,True,NAVY)],
 [L("READ BACK TO THE TEXT",18,True,AMBER),L("The peak reads back to ءله, the repeat to رحم (رحمن/رحيم). A feature that maps to nothing is an artifact — not a finding.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
s=Tt(prs,"What the course can — and cannot — claim")
two(s,[L("CAN",18,True,TEAL),L("The Qur’an’s root signals are real, measurable, and analysable with the full DSP/representation toolkit; some structure (refrains, period-2 in Ar-Raḥmān, semantic embeddings) is specific and beats baselines.",16.5,True,NAVY)],
 [L("CANNOT",18,True,RED),L("That signal analysis reveals hidden ‘scientific miracles,’ or that meaning lives in the numbers. Most structure is generic to Arabic; the specific residue is small, earned, and honest.",16.5,True,NAVY)],sp=0.5,fa=TINT,fb=REDT)
s=Tt(prs,"Dual-domain — the Two Books, closed")
two(s,[L("عالم التكوين",18,True,AMBER),L("Genomics and astronomy read their signals with these exact tools and the exact same discipline — null, baseline, correction, interpretation.",16.5,True,NAVY)],
 [L("عالم التدوين",18,True,TEAL),L("We read the Book of Scripture’s root signals the same way — side by side with creation, one Author, never collapsed.",16.5,True,NAVY)],sp=0.5,fa=AMBERT,fb=TINT)
keyidea(prs,"Key idea — vectorize, transform, VALIDATE, read back","The whole course is one habit: anchor on the root, apply a transform, beat null+baseline, and read the result back into the text.",
  "The same habit guards any data claim you meet — in scripture, science, or a headline.")
corpus_slide(prs,17)
scale_slide(prs,"The capstone verse illustrates every tool at āyah scale where valid.","Spectral/cluster claims about 1:1 are deferred to sūra/corpus scale, as the scale rule demands.")
threads_block(prs,
 "Every amplitude is a root measurement; every step is a declared, reproducible operation on Book6.",
 "The full set of latent features — prominence, repetition, rhythm, similarity, semantic neighbours, principal axes.",
 "Reordering, projecting and clustering are all declared transforms; each feature found still faces the null.",
 "Every claim about 1:1 reads back to its roots and the text — the anchor that keeps the course honest.",
 "Nothing is believed until it beats a sampled null AND random Arabic and survives the search.")
finish_block(prs,
 "Which single tool taught you the most about the text? Where did the method most often say ‘no’?",
 "One verse, the whole pipeline: digitize on the root, transform, validate, read back — disciplined wonder.",
 "Ending on a flourish that skips validation — the temptation the whole course was built to resist.",
 "Run the full gauntlet on every capstone claim; present only what beats null, baseline and search, and reads back.")
roadmap_pos(prs,17)
appslide(prs,[("① VERSE","pick any āyah",TINT,TEAL),("② CHANNEL","root anchor",AMBERT,AMBER),("③ TRANSFORM","any tool",TINT,TEAL),("④ AUDIT","null·baseline·read-back",REDT,RED)],
  "Run the full pipeline on a verse of your choice: digitize on the roots, transform, and audit every claim against null, baseline and the text.")
s=slide(prs); audit(s,"The end-to-end pipeline on 1:1 is exact, reproducible, and validated at each step.","Any capstone claim that skips the null/baseline or fails to read back to the roots.","Spectral/cluster claims on a 4-root verse — deferred to the proper scale, never asserted.")
s=slide(prs); takeaway(s,"The course is a transferable method: vectorize text, transform, and validate before believing — the core of NLP and data science.","Anchor on the ROOT; digitize → transform → beat null + random Arabic → read back. Disciplined wonder, two Books, one Author.")
counts[17]=save(prs,"17_Synthesis_Capstone","17_Synthesis_Capstone_Lecture.pptx")

print("ALL COUNTS:",{k:counts[k] for k in sorted(counts)})

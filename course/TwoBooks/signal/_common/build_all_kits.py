# -*- coding: utf-8 -*-
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from _dochelper import newdoc,P,H,bullet,table,ACCENT,TEAL,RED,GREY
ROOT=os.path.abspath(os.path.join(HERE,".."))
FOLD={3:"03_Vectorization_Schemes",4:"04_Waveform",5:"05_Sampling_Quantization",6:"06_Smoothing_Trend_Difference",
7:"07_Convolution_LTI",8:"08_Autocorrelation_Periodicity",9:"09_Fourier_Spectrum",10:"10_Dominant_Frequencies_Rhythm",
11:"11_Filtering",12:"12_Energy_Norm_Entropy",13:"13_Distance_Similarity",14:"14_Embeddings",15:"15_PCA",
16:"16_Clustering_Spectrogram",17:"17_Synthesis_Capstone"}
TITLE={3:"Vectorization Schemes",4:"The Waveform",5:"Sampling & Quantization",6:"Smoothing, Trend & Difference",
7:"Convolution & LTI Systems",8:"Autocorrelation & Periodicity",9:"Fourier & the Spectrum",10:"Dominant Frequencies & Rhythm",
11:"Filtering",12:"Energy, Norm & Entropy",13:"Distance & Similarity",14:"Embeddings",15:"Dimensionality Reduction (PCA)",
16:"Clustering & the Spectrogram",17:"Synthesis & Capstone"}

# per-lecture: goal, verse, key real result, tasks[(q,a)], quiz[(q,a)], app[bullets]
K={
3:dict(goal="learn the channel taxonomy over the ROOT anchor — frequency, length, surface, morphology, embedding — and when each applies.",
 verse="1:1 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ → roots سمو·ءله·رحم·رحم → [381, 2848, 339, 339]",
 key="root frequency is spiky ([381,2848,339,339]); root length is flat ([3,3,3,3]) — same verse, different channels.",
 tasks=[("Vectorize 1:1 on the root-frequency channel; give the vector and the peak root.","[381, 2848, 339, 339]; peak = ءله (2,848); رحم repeats (رحمن/رحيم share رحم)."),
   ("Give 1:1 on the root-length channel and explain its shape.","[3,3,3,3] — flat, because Arabic roots are overwhelmingly triliteral."),
   ("Why can root IDENTITY not be averaged?","It is nominal — an arbitrary label; arithmetic on labels is meaningless. One-hot or embed first."),
   ("Name two ways to make root-identity numeric.","One-hot encoding; replace-by-frequency; or a learned embedding (L14)."),
   ("Why normalize before combining channels?","Frequency spans 1→2,848, length 1→6; without z-scoring, frequency dominates every distance."),
   ("Across the 114 sūras, type-token ratio runs 0.15→0.56→1.00. What does that tell you?","Channel behaviour is not uniform; a channel must work across the whole corpus, not one verse.")],
 quiz=[("What is the anchor channel and why?","The root (ریشه) — highest semantic power (NLP stem/lemma; biology root↔codon)."),
   ("Give 1:1’s root-frequency vector.","[381, 2848, 339, 339]."),
   ("Why is root length ≈ flat?","Roots are nearly all triliteral."),
   ("Nominal, ordinal, ratio — classify root frequency.","Ratio (true zero, arithmetic valid)."),
   ("Two encodings for nominal roots?","One-hot; embedding."),
   ("Why declare + normalize a channel first?","To avoid tuning the representation to the wished result and to make channels comparable."),
   ("What does TTR 0.15→1.0 across sūras show?","Channels behave differently across the corpus."),
   ("One thing channels do NOT give?","Meaning — they measure form/frequency, not sense.")],
 app=["Enter 1:1; root-frequency channel → [381, 2848, 339, 339].","Switch to root-length → [3,3,3,3].","Toggle z-score normalization.","Read TTR across sūras (0.15→0.56→1.00)."]),
4:dict(goal="read a verse as a waveform — amplitude, peak, trough, dynamic range — and see repetition as a repeated shape.",
 verse="94:5 فَإِنَّ مَعَ الْعُسْرِ يُسْرًا and 94:6 إِنَّ مَعَ الْعُسْرِ يُسْرًا",
 key="94:5 and 94:6 have nearly identical root waveforms — a real, measurable repetition (مع العسر يسرا).",
 tasks=[("Plot 94:5 as a root-frequency waveform; identify peak and trough.","The peak is the most frequent root, the trough the rarest; report indices from the app."),
   ("Compare 94:5 and 94:6. Why are the waveforms nearly identical?","They differ only by فَ; same roots → same shape — a deliberate echo."),
   ("Define dynamic range and compute it for 94:5.","peak − trough of the root-frequency signal (read the value in the app)."),
   ("What are zero-crossings, and what do they measure?","After centring, how often the signal crosses zero — how ‘busy’ the verse is."),
   ("Across 6,139 verses median dynamic range is 1,360. Is 94:5 spiky or flat relative to that?","Compare its range to 1,360 — above = spiky (one dominant root)."),
   ("Why is a tall peak NOT the ‘most important’ word?","It is only the commonest root (e.g. ءله); prominence ≠ importance until validated.")],
 quiz=[("What is plotted in a verse waveform?","Root frequency (amplitude) vs root position."),
   ("Why do 94:5 and 94:6 match?","Same roots; differ only by فَ."),
   ("Define dynamic range.","Peak minus trough amplitude."),
   ("What do zero-crossings measure?","How rapidly the signal alternates."),
   ("Median per-verse dynamic range across the corpus?","≈ 1,360 (p10 118, p90 2,839)."),
   ("Is the peak the most important word?","No — only the commonest root."),
   ("Same object in creation?","ECG/audio/seismograph waveform."),
   ("Scale: is the raw waveform OK on one āyah?","Yes — amplitude/peak/range need no length.")],
 app=["Plot 94:5; mark peak/trough/range.","Overlay 94:6 — the echo.","Read dynamic range vs corpus median 1,360.","View 103 Al-ʿAsr full waveform."]),
5:dict(goal="understand sampling (one root = one sample) and quantization (amplitude levels), with Nyquist and aliasing.",
 verse="103 وَالْعَصْرِ · إِنَّ الْإِنسَانَ لَفِي خُسْرٍ · إِلَّا الَّذِينَ آمَنُوا …",
 key="quantizing Al-ʿAsr to 3 levels keeps the peaks but loses fine differences (quantization error); halving the rate can alias.",
 tasks=[("State our sampling rule and one way to coarsen it.","One root = one sample; coarsen by dropping/binning roots."),
   ("What is quantization error?","The detail lost when amplitudes are rounded to a finite set of levels."),
   ("State the Nyquist idea for the Ar-Raḥmān refrain (period 2).","Need ≥2 samples per cycle; period-2 is right at the limit — finer sampling is safer."),
   ("What is aliasing, in text terms?","Under-sampling makes a fast pattern look slow — an artifact of the rate, e.g. coarse root-binning inventing a period."),
   ("Verse-length quartiles are 4/7/11/20. Why does this set the regime?","Most verses are short; resolution is length-limited corpus-wide, not by one long example."),
   ("How do you guard against aliasing?","Sample above Nyquist for the structure sought; declare the rate; re-test finer.")],
 quiz=[("Two resolutions of a digital signal?","Sampling rate and bit-depth (quantization levels)."),
   ("Our sampling unit?","One root."),
   ("Quantization error is?","Loss from rounding amplitude to levels."),
   ("Nyquist requires?","≥2 samples per cycle."),
   ("Aliasing is?","A fast pattern masquerading as slow from under-sampling."),
   ("Median verse length (roots)?","7 (quartiles 4/7/11/20)."),
   ("Guard against aliasing?","Sample above Nyquist; declare the rate."),
   ("Real-world analogue?","ADC in audio/ECG; CD = 44.1 kHz × 16 bit.")],
 app=["Load 103 at full resolution.","Slide bit-depth to 3 levels (watch blockiness).","Halve the sampling rate (watch aliasing).","Read verse-length quartiles 4/7/11/20."]),
6:dict(goal="split a verse signal into slow trend (moving average) and fast change (first difference).",
 verse="2:255 آيَةُ الْكُرْسِيّ (a long verse)",
 key="a 3-window moving average tracks Āyat al-Kursī’s trend; the first difference flags common↔rare root transitions.",
 tasks=[("What does a moving average do to a verse signal?","Averages neighbours → keeps the slow trend, removes spikes (low-pass)."),
   ("What does the first difference reveal?","Where the signal changes fastest — the verse’s sharp transitions (a derivative)."),
   ("How does window length change the trend?","Wider window = smoother trend, more detail removed."),
   ("What are edge effects and how are they handled?","Near verse ends the window runs off; shrink or pad — and state which."),
   ("Per-verse dynamic range spans p10 118 to p90 2,839. Why compute trend corpus-wide?","Verses differ hugely in detail; the operator is applied to all, not a favourite."),
   ("Why declare the window in advance?","To avoid choosing the window that produces the nicest-looking trend.")],
 quiz=[("Moving average = which filter?","Low-pass (trend)."),
   ("First difference ≈ ?","Discrete derivative (change/high-pass)."),
   ("Wider window →?","Smoother trend, less detail."),
   ("Edge effect fix?","Shrink window or pad; declare it."),
   ("Trend on which test verse?","2:255 Āyat al-Kursī."),
   ("Why declare window first?","To avoid fitting the smoother to the wish."),
   ("Real-world analogue?","Stock/temperature smoothing; image edges."),
   ("Smoothing is also a …?","Convolution (L7).")],
 app=["Load 2:255; slide the smoothing window.","Toggle the first-difference signal.","Split view: trend vs detail.","Compare ranges across verses."]),
7:dict(goal="learn convolution — sliding a kernel — and the LTI/impulse-response idea.",
 verse="110 إِذَا جَاءَ نَصْرُ اللَّهِ وَالْفَتْحُ …",
 key="convolving An-Naṣr with a box kernel [⅓,⅓,⅓] smooths it; the kernel IS the impulse response.",
 tasks=[("Define convolution in one sentence.","Slide a kernel along the signal; each output = weighted sum of neighbours."),
   ("What is the impulse response?","The output for a single spike input — it equals the kernel for an LTI system."),
   ("Name the two LTI properties.","Linearity and time-invariance."),
   ("Give a smoothing, an edge, and an echo kernel.","[⅓,⅓,⅓]; [−1,1]; a delayed copy added back."),
   ("How is Lecture 6’s moving average a convolution?","It is convolution with a box kernel."),
   ("Why test a kernel corpus-wide (lengths 1→84)?","A kernel must behave across the whole length range, not one short sūra.")],
 quiz=[("Convolution does what?","Slides a kernel; weighted-sum of neighbours."),
   ("Impulse response =?","The kernel (LTI)."),
   ("Two LTI properties?","Linearity; time-invariance."),
   ("Edge kernel?","[−1,1]."),
   ("Moving average is convolution with?","A box kernel."),
   ("Commutativity means?","signal∗kernel = kernel∗signal."),
   ("Real-world analogue?","Image blur/sharpen; CNNs; reverb."),
   ("Convolution in time = ? in frequency","Multiplication (L9).")],
 app=["Load 110; pick a kernel (box/edge/echo).","Slide it; view the output.","See the impulse response.","Apply across verses of varied length."]),
8:dict(goal="use autocorrelation to detect periodicity — and find Ar-Raḥmān’s validated period-2 refrain.",
 verse="55 فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ (×31)",
 key="autocorrelation of the refrain indicator peaks +0.75 at lag 2 (period 2); refrains beat the baseline 7.1% vs 0.81%.",
 tasks=[("What does autocorrelation measure?","How well a signal matches a shifted copy of itself at each lag."),
   ("Interpret lag-2 = +0.75 for Ar-Raḥmān.","The pattern repeats every 2 verses — a period-2 refrain."),
   ("Why are odd lags negative (lag-1 = −0.67)?","Refrain lands on non-refrain when shifted by 1 — anti-phase alternation."),
   ("How do you null-test the period?","Shuffle verse order; the lag-2 peak collapses → the period is real."),
   ("Quote the baseline result.","Exact-verse repetition 7.1% (Qur’an) vs 0.81% (random Arabic), ~8.8×, p≈0.03."),
   ("29 of 114 sūras have repeats, 79 are long enough. Why does this matter?","Periodicity is scanned corpus-wide, not only in Ar-Raḥmān.")],
 quiz=[("Autocorrelation measures?","Self-similarity at a lag."),
   ("Ar-Raḥmān period?","2 (lag-2 = +0.75)."),
   ("Why odd lags negative?","Anti-phase alternation of refrain/non-refrain."),
   ("Null test for period?","Shuffle verse order."),
   ("Refrain rate vs baseline?","7.1% vs 0.81% (~8.8×)."),
   ("How many sūras carry repeats?","29 of 114."),
   ("Stationarity assumption?","Structure steady across the sūra."),
   ("Real-world analogue?","Heart rate, pitch, seasonality.")],
 app=["Build the refrain indicator for sūra 55.","Read the lag plot (lag-2 = +0.75).","Shuffle verse order — period collapses.","Scan other sūras for periodicity."]),
9:dict(goal="decompose a sūra-scale signal into frequencies; find the refrain as a spectral line.",
 verse="55 Ar-Raḥmān refrain (sūra-scale)",
 key="the refrain indicator’s spectrum peaks at f≈0.49 → period ≈ 2.05, matching the lag-2 autocorrelation.",
 tasks=[("What does the magnitude spectrum report?","How much of each frequency (period) is present in the signal."),
   ("What period does the dominant line give, and what confirms it?","≈2.05 verses; it matches the lag-2 autocorrelation (L8)."),
   ("Why must this be at sūra scale?","Spectra need many samples; a single āyah has too few."),
   ("State the convolution theorem.","Convolution in time = multiplication in frequency."),
   ("How do you null-test a spectral peak?","Phase-randomize (keep power, destroy structure); the real peak does not survive."),
   ("79 sūras are spectral-capable (≥20 verses). Why report that?","The Fourier method runs across all of them, not one example.")],
 quiz=[("Fourier transform gives?","The spectrum — content per frequency."),
   ("Refrain period from FFT?","≈2.05 verses."),
   ("It agrees with?","Lag-2 autocorrelation."),
   ("Convolution theorem?","Time-convolution = frequency-multiplication."),
   ("Null for a peak?","Phase-randomization."),
   ("Spectral-capable sūras?","79 of 114 (≥20 verses)."),
   ("Scale for spectra?","Sūra/corpus, never one āyah."),
   ("Real-world analogue?","Light spectra; MP3; spectrum analyzers.")],
 app=["Build sūra-55 refrain indicator.","Run FFT; read the dominant line (f≈0.49).","Confirm period ≈2.05 vs autocorrelation.","Phase-randomize to null-test."]),
10:dict(goal="pick dominant frequencies (the beat) from a spectrum; respect the sample-count limit.",
 verse="1 الفاتحة (7 verses; root-length per verse)",
 key="Al-Fātiḥa’s rhythm spectrum has 4 bins (7 verses) — report only the dominant beat; fine rhythm needs long sūras.",
 tasks=[("What is peak-picking?","Finding the tallest spectral components above the noise floor."),
   ("Define fundamental and harmonics.","Fundamental = lowest dominant frequency; harmonics = its integer multiples."),
   ("Why is Al-Fātiḥa’s spectrum low-resolution?","Only 7 verses → 4 frequency bins."),
   ("What may you claim from it, and not?","The dominant beat only; not fine multi-peak rhythm (that would be noise)."),
   ("Where does confident rhythm come from?","Long sūras (79 are ≥20 verses) or the corpus."),
   ("How do you null-test a rhythm peak?","Shuffle verse order; a real meter loses its dominant peak.")],
 quiz=[("Peak-picking finds?","Dominant frequencies (the beat)."),
   ("Fundamental?","Lowest dominant frequency."),
   ("Al-Fātiḥa bins?","4 (7 verses)."),
   ("Claim from a 7-verse spectrum?","Dominant beat only."),
   ("Confident rhythm needs?","Long sūras/corpus."),
   ("Null for a beat?","Shuffle verse order."),
   ("Peak prominence is?","Height above neighbours (the threshold)."),
   ("Real-world analogue?","Music tempo; gait; circadian rhythm.")],
 app=["Load Al-Fātiḥa root-length rhythm.","Pick the dominant bin.","Switch to a long sūra for a confident meter.","Shuffle to null-test."]),
11:dict(goal="separate signal from noise with low/high/band-pass filters; declare the cutoff.",
 verse="2:282 آية الدَّيْن (the longest verse, 84 root-tokens)",
 key="a low-pass keeps the debt verse’s trend; high-pass keeps its texture; low+high reconstruct the original.",
 tasks=[("What does a low-pass keep? A high-pass?","Low-pass: slow trend; high-pass: fast detail."),
   ("What is the cutoff frequency?","Where the filter switches from keep to remove — a declared number."),
   ("What is ringing?","Oscillation artifacts from too-sharp a cutoff — a filter can ADD structure."),
   ("How do you verify a filter did not lie?","low-pass + high-pass should reconstruct the original (Parseval)."),
   ("Why declare the cutoff first?","To avoid tuning it until the verse shows the wished pattern."),
   ("Why test cutoffs across the corpus?","So a filter is not over-fit to one verse (lengths 4/7/11/20).")],
 quiz=[("Low-pass keeps?","The trend."),
   ("High-pass keeps?","The detail."),
   ("Cutoff is?","The keep/remove frequency."),
   ("Ringing is?","Artifact oscillation from sharp cutoffs."),
   ("Reconstruction check?","low+high = original."),
   ("Test verse?","2:282 (debt verse)."),
   ("Declare cutoff when?","Before filtering."),
   ("Real-world analogue?","Noise-cancelling; radio; ECG cleanup.")],
 app=["Load 2:282; apply low-pass.","Switch to high-pass (texture).","Sweep the cutoff; reconstruct.","Compare across verse lengths."]),
12:dict(goal="summarise a signal by energy, norm and entropy; compare two sūras.",
 verse="97 الْقَدْر vs 108 الْكَوْثَر",
 key="Al-Qadr entropy 3.84 bits (varied) vs Al-Kawthar 2.81 (concentrated); RMS 270 vs 378.",
 tasks=[("Define energy and RMS for a signal.","Energy = Σx²; RMS = √(mean x²)."),
   ("Define Shannon entropy of the root distribution.","−Σ p·log₂p over the roots — bits of uncertainty."),
   ("Compare Al-Qadr and Al-Kawthar by entropy.","Al-Qadr 3.84 (more varied) vs Al-Kawthar 2.81 (more concentrated)."),
   ("Why is entropy permutation-invariant?","It depends on the root distribution, not order — it summarises content, not sequence."),
   ("Does low entropy mean a sūra is ‘lesser’?","No — it measures variety, never value (Al-Kawthar is concise, not poor)."),
   ("Per-sūra entropy spans 1.42→7.93. Why compute it for all 114?","The two sūras are points in a whole distribution.")],
 quiz=[("Energy =?","Σx²."),
   ("Entropy measures?","Variety/uncertainty of the root distribution."),
   ("Al-Qadr vs Al-Kawthar entropy?","3.84 vs 2.81 bits."),
   ("Entropy and order?","Permutation-invariant."),
   ("Low entropy = low value?","No."),
   ("Entropy range across sūras?","1.42 → 7.93 bits."),
   ("L2 norm is dominated by?","Peaks (frequent roots)."),
   ("Real-world analogue?","SNR; data compression; genomic complexity.")],
 app=["Compute energy/RMS for 97 and 108.","Compute root entropy for each.","Place them in the 1.42→7.93 range.","Compare to a length-matched baseline."]),
13:dict(goal="measure how alike two verses are — cosine, Euclidean, DTW — against a corpus baseline.",
 verse="113 الفلق vs 114 الناس (المعوذتان)",
 key="113 vs 114 cosine ≈ 0.58 vs a corpus median pair 0.51; their lengths (15 vs 16) call for DTW.",
 tasks=[("Cosine vs Euclidean — what differs?","Cosine ignores magnitude (direction only); Euclidean includes it."),
   ("Why DTW for 113 vs 114?","Different lengths (15 vs 16 roots) — DTW aligns by stretching."),
   ("Quote the result vs the baseline.","Cosine ≈0.58 vs corpus median pair 0.51 — slightly more alike than typical."),
   ("What is a similarity matrix?","Pairwise similarity of all verses; reorder it to expose families."),
   ("Why read a similarity against the corpus?","Most pairs already score ~0.5; ‘alike’ needs the baseline."),
   ("Which later tools build on distance?","Embeddings (L14), PCA (L15), clustering (L16).")],
 quiz=[("Cosine ignores?","Magnitude (length)."),
   ("DTW handles?","Different-length sequences."),
   ("113 vs 114 cosine?","≈0.58."),
   ("Corpus median pair?","0.51."),
   ("Similarity matrix is?","All pairwise similarities."),
   ("Why baseline a similarity?","Most pairs ~0.5 already."),
   ("Builds on distance?","Embeddings/PCA/clustering."),
   ("Real-world analogue?","Search ranking; BLAST; speech DTW.")],
 app=["Score 113 vs 114 by cosine (0.58).","Compare to corpus median 0.51.","Switch to DTW for unequal lengths.","Build a similarity matrix."]),
14:dict(goal="learn root embeddings from co-occurrence; read semantic neighbourhoods.",
 verse="roots رحم · ءمن (embedding neighbours)",
 key="رحم’s nearest root is غفر (0.82); ءمن’s is عمل (0.78) — the Qur’an’s faith-and-works pairing, recovered by geometry.",
 tasks=[("State the distributional hypothesis.","A root is known by the roots it co-occurs with."),
   ("Give رحم’s nearest neighbours.","غفر (0.82), ءجر (0.77), فضل (0.77)."),
   ("Give ءمن’s nearest neighbours and the textual echo.","عمل (0.78), طوع, ءجر — الذين آمنوا وعملوا الصالحات."),
   ("Why embed ROOTS rather than surface tokens?","Roots carry meaning; surface tokens mix in ال and grammar — less semantic."),
   ("How do you null-test a neighbour?","Re-train on shuffled contexts; real neighbours (رحم↔غفر) collapse."),
   ("Why is embedding inherently corpus-scale?","A root’s vector is learned from its co-occurrences across the whole corpus.")],
 quiz=[("Distributional hypothesis?","Meaning from company (co-occurrence)."),
   ("رحم nearest root?","غفر (0.82)."),
   ("ءمن nearest root?","عمل (0.78)."),
   ("Why roots not surface?","Roots carry meaning; surface mixes grammar."),
   ("Null test?","Shuffled-context re-training."),
   ("Embedding scale?","Corpus (not one āyah)."),
   ("Embedding turns identity into?","Geometry (a vector)."),
   ("Real-world analogue?","word2vec; protein/gene embeddings.")],
 app=["Enter رحم; read neighbours (غفر, فضل, ءجر).","Enter ءمن; see عمل/طوع/ءجر.","Project to 2-D.","Shuffle contexts to null-test."]),
15:dict(goal="reduce many sūra features to a few principal axes; interpret and validate.",
 verse="all 114 sūras × 5 root-features",
 key="PC1 (62%) + PC2 (20%) = 81% of sūra variation; PC1 ≈ size & richness.",
 tasks=[("What does PCA find?","The orthogonal axes of greatest variance in the feature space."),
   ("How much variance do PC1+PC2 hold?","81% (PC1 62%, PC2 20%)."),
   ("Interpret PC1.","Size and richness (verse-count, token-count, type-token ratio load heaviest)."),
   ("What is the scree plot for?","To choose how many components to keep (the elbow)."),
   ("What is the read-back for PCA?","Reconstruction error — rebuild from 2 PCs; small error = fair summary."),
   ("Why reject an uninterpretable PC?","An axis that maps to nothing real is an artifact, not a discovery.")],
 quiz=[("PCA finds?","Axes of maximum variance."),
   ("PC1+PC2 variance?","81%."),
   ("PC1 ≈?","Size/richness."),
   ("Scree plot chooses?","Number of components."),
   ("PCA read-back?","Reconstruction error."),
   ("Reject a PC when?","It is uninterpretable / no baseline."),
   ("Scale of PCA?","Corpus (all 114 sūras)."),
   ("Real-world analogue?","Population genetics; eigenfaces.")],
 app=["Compute 5 features for 114 sūras.","Run PCA; read the scree (62/20).","Plot the 2-D map.","Check reconstruction error."]),
16:dict(goal="group sūras without labels (clustering) and turn 1-D into 2-D (spectrogram).",
 verse="all 114 sūras (root-features)",
 key="k=2 splits the 114 sūras into 62 and 52 — mainly by length (mean 25.6 vs 89.3 verses).",
 tasks=[("What is unsupervised clustering?","Grouping by proximity with no labels given."),
   ("Describe the two sūra clusters.","62 short (~25.6 verses) and 52 long (~89.3 verses) — a length/richness split."),
   ("What does silhouette validate?","How well-separated the clusters are — and the choice of k."),
   ("What is a spectrogram?","Spectrum vs position (STFT) — a 2-D image of a 1-D signal."),
   ("Why is the cluster NOT ‘Meccan/Medinan’?","We computed length, not revelation place; that claim needs the labels and a test."),
   ("Why cluster the whole corpus?","Structure is a statement about all 114 sūras, none excluded.")],
 quiz=[("Clustering is?","Unsupervised grouping."),
   ("Two clusters here?","62 short, 52 long."),
   ("Split by?","Length/richness (PC1)."),
   ("Silhouette validates?","Separation / k."),
   ("Spectrogram is?","Spectrum vs time (STFT), a 2-D image."),
   ("Is it Meccan/Medinan?","No — length-based; needs labels to claim."),
   ("Bridge to which course?","The surah-as-image (2-D) course."),
   ("Real-world analogue?","Cell-type clustering; speech spectrograms.")],
 app=["Cluster 114 sūras (k=2 → 62/52).","Check the silhouette.","Build a spectrogram (STFT).","Cross into the image course."]),
17:dict(goal="run the whole pipeline on one verse and audit every step — the course in one arc.",
 verse="1:1 بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ → [381, 2848, 339, 339]",
 key="digitize → transform → beat null + random Arabic → read back; most candidates die, the survivors (refrains, period-2, رحم≈غفر) are real.",
 tasks=[("Vectorize 1:1 on the root anchor.","[381, 2848, 339, 339] (سمو·ءله·رحم·رحم)."),
   ("Name three transforms you would apply and what each shows.","Smoothing (trend), entropy (variety), embedding (رحم≈غفر)."),
   ("State the six validation gates.","verify → null → baseline → FDR → read-back (+ scale rule)."),
   ("Give one finding that survives all gates.","Refrains 7.1% vs 0.81%; or Ar-Raḥmān period-2; or رحم↔غفر."),
   ("State one thing the course CANNOT claim.","Hidden ‘scientific miracles,’ or that meaning lives in the numbers."),
   ("Why anchor on the root throughout?","Highest semantic power; cleaner null (mean r 0.04 vs 0.18 surface).")],
 quiz=[("1:1 root vector?","[381, 2848, 339, 339]."),
   ("Six gates?","verify, null, baseline, FDR, read-back, scale."),
   ("A surviving finding?","Refrains 7.1% vs 0.81%."),
   ("A claim NOT made?","Scientific miracles / meaning-in-numbers."),
   ("Anchor and why?","Root — semantic power + cleaner null."),
   ("Most candidates do what?","Fail the gauntlet."),
   ("Reordering is?","A declared tool, validated by a null."),
   ("Real-world transfer?","NLP/data-science discipline for any claim.")],
 app=["Pick any āyah; root channel.","Apply a transform.","Audit: null, baseline, read-back.","Compare to corpus statistics."]),
}

def kit(lec):
    fold=os.path.join(ROOT,FOLD[lec]); pfx="%02d"%lec; t=TITLE[lec]; k=K[lec]
    # Instructor script
    d=newdoc("Signal · L%d %s · Instructor Script"%(lec,t))
    P(d,[("Lecture %d — %s"%(lec,t),True)],size=20,color=ACCENT,after=2)
    P(d,[("Instructor Script · 3-hour session · root anchor · verify → null → baseline → audit",True)],size=12,color=TEAL,after=6)
    P(d,[("Goal: ",True),(k["goal"]+" Worked example: "+k["verse"]+". Key result: "+k["key"],False)],after=8)
    H(d,"0:00–0:25  The idea & foundations")
    P(d,"Open on the root anchor; state the lecture’s operation and the conceptual foundation. Worked verse: "+k["verse"]+".")
    H(d,"0:25–1:05  Worked data — on real āyāt")
    P(d,k["key"]+" Every figure is recomputed from Book6.xlsx (6,236 āyāt); examples illustrate, the corpus validates.")
    H(d,"1:05–1:15  Break")
    H(d,"1:15–1:55  Across the corpus + the five threads")
    P(d,"Show the whole-corpus distribution (not one verse); then instantiate the threads — criteria, latent-feature objective, reordering-as-tool, read-back anchor, natural-language baseline — and the scale rule.")
    H(d,"1:55–2:25  Validation & the app")
    P(d,"Beat a sampled null AND random Arabic, correct for the search, read back to the roots/text. Demo the app live on "+k["verse"].split(" ")[0]+".")
    H(d,"2:25–2:35  Break")
    H(d,"2:35–3:00  Audit, discussion & takeaway")
    P(d,"Close with the audit ✓/✗/~, the discussion questions, and the takeaway. Most candidate patterns fail; the survivors are real.")
    P(d,[("Provenance: ",True),("all figures computed from Book6.xlsx; root column (ریشه) is the anchor; Monte-Carlo uses a fixed seed.",False)],color=ACCENT,before=6)
    d.save(os.path.join(fold,pfx+"_Instructor_Script.docx"))
    # Exercise
    d=newdoc("Signal · L%d %s · Exercise"%(lec,t))
    P(d,[("Lecture %d — Exercise"%lec,True)],size=20,color=ACCENT,after=2)
    P(d,[(t+" · app-driven · root anchor",True)],size=12,color=TEAL,after=6)
    for i,(q,a) in enumerate(k["tasks"],1):
        H(d,"Task %d"%i); P(d,q)
    H(d,"Reflection"); P(d,"In 3–4 sentences: what latent feature did this lecture surface, and how would you prove it is real (null, baseline, read-back)?")
    d.save(os.path.join(fold,pfx+"_Exercise.docx"))
    # Exercise key
    d=newdoc("Signal · L%d %s · Exercise — Answer Key"%(lec,t))
    P(d,[("Lecture %d — Exercise · Answer Key"%lec,True)],size=20,color=ACCENT,after=2)
    P(d,[("Model answers · figures from Book6.xlsx",True)],size=12,color=TEAL,after=6)
    for i,(q,a) in enumerate(k["tasks"],1):
        H(d,"Task %d"%i); P(d,a)
    H(d,"Reflection"); P(d,"A strong answer names the feature, the transform, and the gate most likely to kill it (usually the natural-language baseline or the read-back).")
    d.save(os.path.join(fold,pfx+"_Exercise_Answer_Key.docx"))
    # Quiz
    d=newdoc("Signal · L%d %s · Quiz"%(lec,t))
    P(d,[("Lecture %d — Quiz"%lec,True)],size=20,color=ACCENT,after=2)
    P(d,[(t+" · %d questions"%len(k["quiz"]),True)],size=12,color=TEAL,after=6)
    for i,(q,a) in enumerate(k["quiz"],1): P(d,"%d. %s"%(i,q),after=6)
    d.save(os.path.join(fold,pfx+"_Quiz.docx"))
    # Quiz key
    d=newdoc("Signal · L%d %s · Quiz — Answer Key"%(lec,t))
    P(d,[("Lecture %d — Quiz · Answer Key"%lec,True)],size=20,color=ACCENT,after=2)
    for i,(q,a) in enumerate(k["quiz"],1): P(d,[("%d. "%i,True),(a,False)],after=6)
    d.save(os.path.join(fold,pfx+"_Quiz_Answer_Key.docx"))
    # App guide
    d=newdoc("Signal · L%d %s · App & Plot Guide"%(lec,t))
    P(d,[("Lecture %d — App & Plot Guide"%lec,True)],size=20,color=ACCENT,after=2)
    P(d,[("Using the app on the root anchor",True)],size=12,color=TEAL,after=6)
    H(d,"Live app tasks")
    for b in k["app"]: bullet(d,b)
    H(d,"Key result to reproduce")
    P(d,k["key"])
    P(d,[("Tip: ",True),("examples illustrate; always validate on the whole corpus (null + natural-language baseline) and read back to the roots/text.",False)],color=ACCENT,before=6)
    d.save(os.path.join(fold,pfx+"_App_and_Plot_Guide.docx"))
    return 6

tot=0
for lec in range(3,18): tot+=kit(lec)
print("kit docx written:",tot)

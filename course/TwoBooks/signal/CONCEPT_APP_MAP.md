# Signal Course — New-Concepts & App-Use Map (17 lectures)

**Rule (locked).** Every lecture introduces **new DSP concepts**, a **new ayah example** (no example reused as the headline case), and a **distinct app use**. Concepts are *cumulative*: each lecture builds on prior ones but adds its own. This map is the anti-repetition contract for lectures 2–17, enforcing the standing standards ("distinct examples per lecture · no repeated content slides · app central, distinct app focus per lecture").

> **Anchor (locked).** Vectorize on the **ROOT (ریشه, col 4)** — the unit of highest semantic power, as in the biology course (root↔codon) and in NLP (stem/lemma). **Surface forms (col 5)** and **morphology (col 7)** are complementary channels, always available. Worked example: 112:1 قل هو الله أحد → roots قول·ءله·وحد → [1722, 2848, 153] (هو is a pronoun, no root). Anchoring on roots also removes the function-word artifact: mean pairwise r falls from 0.18 (surface) to 0.04 (roots).

> Common spine in every lecture: the ayah is **digitized** into a 1-D signal; every figure is **recomputed from Book6.xlsx**; every claim that can be tested **beats a Monte-Carlo null**; the lecture ends with the **audit ✓/✗/~** and a **Real-world relevance & takeaway**.

> **Scale rule (locked).** Ayah signals are short (median 7 tokens), so estimates are unstable at ayah scale — lag-1 autocorrelation std falls 0.48 (n≈4) → 0.31 (7) → 0.16 (15) → 0.09 (60). Length-hungry tools (Fourier, autocorrelation, spectrogram, filtering) are therefore applied at **sūra or corpus scale**; ayah-scale work is limited to robust statistics (amplitude, peak, energy, distance). State the scale on every analytic slide.

## Recurring threads (carried through every lecture, 2–17)

Four ideas from Lecture 1 are **standing threads** — each must reappear, instantiated to that lecture's topic, on at least one slide:

1. **Criteria for number assignment** — the amplitude is a *measurement, not a label*; the channel is declared first, rule-based, corpus-consistent (nominal codes such as root-id are transformed before any arithmetic).
2. **Latent-feature objective** — the lecture's operation exists to *surface hidden structure*, not for its own sake; name the latent feature it seeks.
3. **Reordering-as-tool** — permuting tokens / sorting or clustering ayāt is a *legitimate, declared* manipulation (the null is itself a shuffle); state the reordering used.
4. **Read-back anchor** — any feature found must *map back to the text* (interpretive inverse, not exact reconstruction): semantically for meaning-claims, structurally for form-claims, and it must beat a null.
5. **Natural-language baseline** — beating a *shuffle* null only shows "not random." A claim of Qur'an-specific structure must also beat a **length/Zipf-matched natural-language baseline** (iid-unigram pseudo-āyāt, or another Arabic corpus). Generic features of Arabic (Zipf slope, function-word share) are *expected* to match the baseline; only the residue that exceeds it is Qur'an-specific. When the configuration space is too large to enumerate, the baseline/null is **sampled** (Monte-Carlo), not computed exhaustively.

**Living threads (revision protocol).** These four are *not frozen*. As each lecture explores the actual Book6 data, the data may enrich or sharpen a thread (a better read-back rule for periodic features, what makes a learned embedding axis a valid measurement, etc.). When that happens: (1) update the thread's definition **here first** (this map is the single source of truth); (2) **thread it back** — rebuild Lecture 1 and every other built lecture from its `build_*.py` so all decks reflect the matured concept; (3) any enrichment that changes a *claim* (not just wording) must itself meet the standard — verified on Book6, beating a null where testable — before it propagates. Decks are generated from scripts, so re-propagation is a rebuild, not hand-editing.

### Per-lecture instantiation (the threads in action)

| # | Latent feature sought (thread 2) | Reordering / manipulation (thread 3) | Read-back anchor (thread 4) | Criteria / validity check (thread 1) |
|---|---|---|---|---|
| 02 | what *counts* as a real feature (meta) | token shuffle builds the null | the refrain bond ↔ an actual repeated verse | channel declared first; finding beats the null |
| 03 | which channel exposes structure | re-encode (scalar/one-hot); normalize | each value ↔ a real token property (freq, length) | measurement-not-label (root-id → one-hot); z-score declared |
| 04 | peaks/troughs = prominent vs rare tokens | sort tokens by amplitude to inspect | a peak ↔ a specific salient word (e.g. الله) | frequency = ratio scale; dynamic range computed |
| 05 | how coarse a measurement still keeps the shape | down-sample / re-quantize | aliasing ↔ misread tokens; bit-loss ↔ lost distinctions | Nyquist threshold; quantization error bounded |
| 06 | trend (drift) vs detail (token jumps) | window sweep; first-difference operator | a trend ↔ a build-up across the verse; a spike ↔ a rare word | window length & edge handling declared |
| 07 | local motifs (response to a kernel) | slide / swap kernels (convolution) | a strong response ↔ a real local token pattern | LTI assumptions stated; kernel declared |
| 08 | periodicity / rhyme structure | lag shifts; shuffle to null the ACF | an ACF peak ↔ an actual refrain/rhyme | stationarity caveat; ACF peak beats shuffle null |
| 09 | frequency components / periodic structure | transform to frequency; phase-scramble null | a dominant bin ↔ a real repetition period | Parseval check; peak vs phase-randomized null |
| 10 | fundamental rhythm / meter | peak-pick; isolate harmonics | the fundamental ↔ the sūra's cadence | peak-prominence threshold; null |
| 11 | structure vs noise | apply low-/high-/band-pass | low-pass survivor ↔ gross shape; residual ↔ fine detail | cutoff declared, not tuned to a wished result |
| 12 | information content / concentration | normalize; compare sūras | high entropy ↔ lexically diverse verse; low ↔ repetitive | normalization declared; compared vs baseline |
| 13 | which ayāt are "near" each other | similarity matrix; DTW alignment; reorder by similarity | a near pair ↔ genuinely related verses (113/114) | metric declared; beats a random-pair null |
| 14 | semantic axes / neighborhoods | project to 2-D; nearest-neighbor reorder | a neighbor ↔ a semantically related root (رحمن/رحيم) — **semantic anchor decisive** | embedding numeric by construction; neighbors validated against meaning |
| 15 | principal axes of variation | project onto PCs; sort ayāt by PC score | a PC ↔ an interpretable contrast — **maps to nothing ⇒ reject** | variance explained; reconstruction error; interpretability gate |
| 16 | groups of ayāt; time–frequency structure | cluster rows; STFT windows | a cluster ↔ a real grouping (Meccan/Medinan); a band ↔ a real local periodicity | silhouette; cluster stability vs null; k declared |
| 17 | end-to-end discovery on one ayah | all declared transforms in sequence | the final claim must read back into the text | full audit + null on the chosen channel |


## Unit A — Foundations

| # | Lecture | New concepts (first introduced here) | Headline ayah example | App use (distinct) |
|---|---|---|---|---|
| 01 | Introduction | signal · sample · axis · amplitude · digitization/vectorization · channel · **criteria for number assignment** (measurement-not-label; levels of measurement) · **objective: latent features** · **interpretive inverse / read-back anchor** · reordering as a declared tool · heavy-tail (Zipf) · the null (intro) · audit | **112:1** قل هو الله أحد → roots [1722, 2848, 153] | digitize a verse; switch channel; reproduce the vector; run a shuffle null |
| 02 | The Method | verification vs validation · null hypothesis & p-value · sampling the null · **aliasing & over-fitting** as cautionary tales · reproducibility | **108** Al-Kawthar (shortest sūra) + the 55 refrain as the bond | Monte-Carlo panel: set #draws → null histogram + p-value; aliasing toggle |
| 03 | Vectorization Schemes | the channel taxonomy formalized · scalar vs one-hot encoding · **normalization / standardization (z-score)** | **1:1** بسم الله الرحمن الرحيم (all five channels overlaid) | channel switcher with side-by-side overlay; normalization toggle |

## Unit B — The signal in time

| # | Lecture | New concepts | Headline ayah example | App use |
|---|---|---|---|---|
| 04 | The Waveform | waveform · time-domain plot · peak/trough · **dynamic range** · zero-crossings | **94:5–6** فإن مع العسر يسرا (its repeat) | waveform viewer: peak/trough markers, dynamic-range & zero-crossing readout |
| 05 | Sampling & Quantization | sampling rate · **Nyquist** · aliasing (deeper) · quantization · bit-depth · quantization error | **103** Al-ʿAsr | sampling-rate & bit-depth sliders; watch aliasing + quantization error live |
| 06 | Smoothing, Trend & Difference | moving average (low-pass) · window length · trend vs detail · **first difference / derivative** · edge effects | **2:255** Āyat al-Kursī (a long signal) | smoothing-window slider; difference toggle; trend/detail split view |
| 07 | Convolution & LTI Systems | **convolution** · kernel/filter · impulse response · linearity & time-invariance · commutativity | **110** An-Naṣr | kernel picker (box / triangular / edge); convolve & view impulse response |
| 08 | Autocorrelation & Periodicity | autocorrelation · lag · periodicity · ACF peaks · rhyme detection · stationarity | **55** Ar-Raḥmān refrain فبأي آلاء ربكما تكذبان (31×) | autocorrelation lag plot; ACF peak finder; refrain detector across a sūra |

## Unit C — The signal in frequency

| # | Lecture | New concepts | Headline ayah example | App use |
|---|---|---|---|---|
| 09 | Fourier & the Spectrum | Fourier series / **DFT** · frequency bins · magnitude spectrum · phase · Parseval | **109** Al-Kāfirūn (highly repetitive) | FFT view; magnitude/phase toggle; frequency-bin inspector |
| 10 | Dominant Frequencies & Rhythm | dominant frequency · fundamental · **spectral peak-picking** · rhythm/meter · harmonics | **1** Al-Fātiḥa (rhythm of the whole sūra) | spectral peak picker; fundamental/harmonic highlighter; rhythm meter |
| 11 | Filtering | low-/high-/band-pass · **cutoff frequency** · denoising · filter trade-offs (ringing) | **2:282** (the debt verse — noisy long signal) | low/high/band-pass filter with cutoff slider; before/after denoise |

## Unit D — Information, distance & space

| # | Lecture | New concepts | Headline ayah example | App use |
|---|---|---|---|---|
| 12 | Energy, Norm & Entropy | energy · L1/L2 norm · RMS · **Shannon entropy** · information content | **97** Al-Qadr vs **108** Al-Kawthar (energy/entropy compare) | energy / norm / entropy meters; compare two sūras |
| 13 | Distance & Similarity | Euclidean & **cosine** distance · correlation as similarity · **dynamic time warping (DTW)** · similarity matrix | **113 vs 114** Al-Falaq vs An-Nās (the muʿawwidhatān) | verse-pair similarity (Euclidean/cosine/DTW selector); similarity heat-map |
| 14 | Embeddings | embeddings · vector space · dimensionality · semantic axes · **nearest neighbors** | root family **رحمن / رحيم** in embedding space | embedding explorer; 2-D projection; nearest-neighbor roots |

## Unit E — Structure & synthesis

| # | Lecture | New concepts | Headline ayah example | App use |
|---|---|---|---|---|
| 15 | Dimensionality Reduction (PCA) | variance · **principal components** · scree plot · projection · reconstruction | all **6,236** ayah-vectors (principal axes) | PCA biplot / scree; project ayāt; color by sūra |
| 16 | Clustering & the Spectrogram | clustering (k-means / hierarchical) · silhouette · the **spectrogram (STFT)** · windowing · bridge to 2-D | Meccan vs Medinan sūras (clusters) | cluster map (k slider); spectrogram view; Meccan/Medinan overlay |
| 17 | Synthesis & Capstone | end-to-end pipeline · channel-selection justification · full audit · synthesis | student-chosen ayah (worked end-to-end) | full pipeline runner: ayah → channel → transform → audit → null |

## Exam coverage

`exams/Midterm_Exam.docx` — Lectures 1–8 (foundations + the signal in time). `exams/Final_Exam.docx` — Lectures 1–17.

## Parked idea — character-level signal (for critical review, later)

Worth exploring once the root-anchored course is built: a **character-level** signal equivalence. At the char level there is no semantic luxury, but **communication- and information-theory** dimensions become first-class — per-character entropy, conditional entropy / Markov order, mutual information between positions, compressibility (Kolmogorov/▷ gzip ratio), and channel-capacity framing of the consonantal skeleton. These can be as valuable as semantics when working on *sequences*, and would complement the root anchor (meaning) with an information-theoretic layer (transmission). Not for now — flagged for critical review.

## Build guard (check before saving each deck)

1. No headline ayah example repeats a previous lecture's headline. 2. Every "new concept" cell above appears as a fresh content slide, not a restatement. 3. The app-use slide describes this lecture's distinct interaction. 4. ≥20 slides, ≥half visual, figures recomputed from Book6, null where testable, audit + takeaway present. 5. The five recurring threads (criteria · latent-feature objective · reordering-as-tool · read-back anchor · natural-language baseline) each appear, instantiated to this lecture per the table above. 6. The scale of every analytic claim (ayah / sūra / corpus) is stated, and length-hungry tools are not used at ayah scale.

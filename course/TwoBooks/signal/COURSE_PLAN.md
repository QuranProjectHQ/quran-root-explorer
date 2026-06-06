# The Two Books — Ayah as Signal (1-D) — Course Plan

**عالم التدوين (the ayah, vectorized into a 1-D signal) · عالم التكوين (creation's data, as physical signals)** — one Author, both *āyāt*.

A self-contained Two Books course, **parallel to the biology course**. Its core idea: **vectorize the text** — turn each **ayah** into a **1-D numeric vector** (a signal) and read it with the mathematics of **digital signal processing**. The unit is the **ayah**: a verse with *n* tokens becomes a length-*n* signal whose samples are per-token numbers (token frequency, word length, root id, embedding component…). The anchor is the **ROOT** (ریشه) — highest semantic power, as in the biology course (root↔codon) and NLP (stem/lemma); surface forms and morphology are complementary channels. For example, **قل هو الله أحد** (112:1) on the root anchor is roots قول·ءله·وحد → **[1722, 2848, 153]** — ءله a tall peak, وحد a valley (هو is a pronoun, no root). The "Book of Creation" side is the same: nature's data (sensor time-series, measurements) are also 1-D signals, analyzed by the same math.

> Distinct from the **biology** course (`../biology/`, units→meaning) and the **surah-as-2-D-image** course (`../image/`). Here the object is the **vectorized ayah signal**.


## Meta-thesis (what the course found)

The detectable latent structure of the Qur'an is **relational / organizational, not in local content statistics.** Validated, Qur'an-specific findings were all about *relations between units* — refrains and Ar-Raḥmān's period-2 (repetition across verses), and the **muqaṭṭaʿāt as positional pointers** indexing contiguous sūra-families (label-permutation p = 2×10⁻⁵ over all 29 muqaṭṭaʿāt sūras, in both muṣḥaf and revelation order). Per-unit content channels (root/letter frequency, word length, entropy) matched random Arabic. Consequently this 1-D course is reframed as the **foundation + honest negative control** that motivates relational / 2-D analysis; the productive object is the sūra-sequence / corpus graph, not the āyah-token sequence. (Evidence-based hypothesis, not a proven law.)

## What "signal" means here (read first)

- **Vectorization, not acoustics.** The signal is the *numeric vectorization of the text data*, not (primarily) the sound of recitation. Each ayah → a vector of numbers.
- **Ayah-level.** One ayah = one signal. A token = one sample. (Surah-level / 2-D is the image course.)
- **Many vectorizations.** The same ayah yields several signals — by token frequency, word length, root identity, position, or a learned embedding — each a different "channel."

## Standing standards (inherited from the biology course)

≥20 editable slides per deck · ≥half visual · zero empty space · dual-domain real data · *Real-world relevance & takeaway* slide each · no "scientific-miracle" claims · audit ✓/✗/~ · Monte-Carlo where testable · app central · distinct examples per lecture · no repeated content slides. Per-lecture kit: slides+script, exercise+key, quiz+key, app guide; course midterm + final.

## Lecture sequence — 17 lectures (university standard, simple → complex)

A full-semester arc, **17 lectures** matching the biology course, covering the canonical digital-signal-processing syllabus applied to the vectorized ayah.

### Unit A — Foundations
1. **Introduction** — the idea and its conceptual foundations: vectorize the ayah into a 1-D signal; the roadmap; the numerology defense.
2. **The Method** — DSP verification & validation; the Monte-Carlo null; aliasing/over-fitting as cautionary tales.
3. **Vectorization Schemes** — the ways to turn an ayah into a vector (frequency, length, root id, embedding) and what each captures.

### Unit B — The signal in time (the ayah-vector as a sequence)
4. **The Waveform** — the per-token signal; amplitude = a token's value (e.g., rarity).
5. **Sampling & Quantization** — token = sample; resolution, the Nyquist idea, aliasing when a channel is too coarse.
6. **Smoothing, Trend & Difference** — moving averages; the derivative signal.
7. **Convolution & LTI Systems** — the impulse response; sliding a kernel along the ayah-vector.
8. **Autocorrelation & Periodicity** — repetition and rhyme structure within and across ayāt.

### Unit C — The signal in frequency
9. **Fourier & the Spectrum** — periodic structure of the ayah-vector.
10. **Dominant Frequencies & Rhythm** — the spectral peaks of a verse.
11. **Filtering** — separating trend from detail; denoising the vector.

### Unit D — Information, distance & space
12. **Energy, Norm & Entropy** — the magnitude and information of an ayah-vector.
13. **Distance & Similarity** — comparing two ayāt as vectors (correlation, cosine, DTW).
14. **Embeddings** — the ayah as a point in a high-dimensional space.

### Unit E — Structure & synthesis
15. **Dimensionality Reduction (PCA)** — the principal axes of variation across ayāt.
16. **Clustering & the Spectrogram** — grouping ayāt by their signals; the bridge toward the 2-D image course.
17. **Synthesis & Capstone** — vectorize and analyze one ayah end-to-end.

## Seed status

`01_Introduction/` is built (deck) as the template starter, opening with the idea + conceptual foundations and real ayah-vector data. `seed_Quran_as_Signal/` holds the original signal deck as source material. Remaining lectures to be built to the locked standard, as in the biology course.

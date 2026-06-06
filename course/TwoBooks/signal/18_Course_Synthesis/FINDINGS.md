# Signal Course — Synthesis & Findings (one-page report)

*Root-anchored (ریشه). All figures recomputed from `Book6.xlsx` (6,236 āyāt · 114 sūras · 51,044 root-tokens · 1,702 roots).*

## What we did
Digitized each āyah on the **root** anchor and read it with the full DSP / representation toolkit across 17 lectures (waveform → sampling → smoothing → convolution → autocorrelation → Fourier → filtering → energy/entropy → distance → embeddings → PCA → clustering). Nothing was believed until it passed a gauntlet: **verify → sampled null → natural-language baseline → multiple-comparison (FDR) → read-back → scale rule.**

## Findings that beat the baseline (Qur'an-specific)
- **Refrains:** exact whole-verse (root) repetition **7.1% vs 0.81%** in length/Zipf-matched random Arabic (~**8.8×**, p≈0.03).
- **Period-2 rhythm:** Sūrat ar-Raḥmān's فبأي آلاء ربكما تكذبان returns every ~2 verses — **autocorrelation +0.75 at lag 2** and an **FFT line at period 2.05** (two independent confirmations).
- **Semantic geometry:** root embeddings recover real fields — **رحم→غفر (0.82)**, **ءمن→عمل (0.78)** (the faith-and-works pairing الذين آمنوا وعملوا الصالحات).
- **Low-dimensional sūras:** **PCA — 81%** of sūra variation in 2 components (PC1 ≈ size & richness).

## What is generic (NOT Qur'an-specific)
Root-Zipf slope (−0.76) and top-10 root share (0.21) are **identical** in random Arabic — properties of the language. Surface "similarities" (e.g. 70:8 ≈ 37:153, r=1.0) are **artifacts of ال**, removed by the root anchor (null mean r 0.18 → 0.04).

## Significance
- **Method:** a transferable discipline — vectorize, transform, and refuse belief until a result beats null + baseline, survives the search, and reads back. Guards any data claim.
- **Two Books:** applying creation's method (measurement/null/baseline) to the Word. The integration is **epistemic — in the learner**, not a merging of texts; قول↔فعل two-way, one Author, distinct genres.

## What it means — and does not
Means: the text is genuinely analysable as signal, with measurable rhythm, repetition, semantic geometry and low-dimensional structure. Does **not** mean hidden "scientific miracles," numeric codes, or that meaning lives in the numbers — the vector is the carrier; the verse is read back by a human.

## Limitations
Short āyāt (median 7 roots) push spectral tools to sūra/corpus scale; Book6 stems are noisy (Persian forms, conflated roots); the channel×op×verse search needs FDR/pre-registration.

## Next
Stronger baselines (real Arabic poetry/hadith); labelled tests for Meccan/Medinan & nuzūl; a verified triliteral lemmatizer; the **char-level information-theory** series (seed written); the **2-D image** course (via the spectrogram bridge).

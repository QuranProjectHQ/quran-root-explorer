# The Two Books — Ayah as a Character-Level Signal (Information Theory) — SEED

*A future sibling series to `../signal/` (root-anchored) and `../image/` (2-D). Parked idea — pick up only after the root-anchored signal course is complete and validated.*

## The idea

The `signal/` course anchors on the **root** (ریشه) — the unit of meaning. This series drops *below* meaning to the **character** (the consonantal skeleton / rasm). At the char level there is **no semantic luxury**, but the **communication- and information-theory** dimensions become first-class — and for *sequences* these can be as valuable as semantics.

> Anchor here = the **character/letter sequence**. The verse becomes a string of symbols over a ~28-letter alphabet (optionally the 14 ḥurūf muqaṭṭaʿāt as a special sub-alphabet).

## What becomes measurable (the information layer)

- **Per-character entropy** H(X) — how surprising the next letter is; bits per letter.
- **Conditional entropy / Markov order** H(Xₙ | Xₙ₋₁ …) — how much memory the letter stream carries.
- **Mutual information** between positions / between consonants — long-range dependency.
- **Redundancy & compressibility** — gzip/Kolmogorov ratio vs a random 28-letter string; the channel-coding view of the rasm.
- **Channel capacity** framing of the consonantal skeleton (Arabic drops short vowels — a real lossy channel the reader decodes).
- **n-gram / suffix structure**, letter-transition matrices, entropy rate.

## Why it complements the root anchor

Roots carry **meaning** (the *tadwīn* message); characters carry **transmission** (the *information* that survives a lossy channel). Together: a meaning layer + an information layer over the same text. The muqaṭṭaʿāt (الم, حم, …) are a natural bridge — letters with no root, pure signal.

## The dual-domain parallel (Two Books)

DNA is read at the **nucleotide/char level** by exactly these tools — entropy, mutual information, compressibility of the genome. The char-level Qur'an series would mirror genomics' *sequence* information theory, just as `signal/` mirrors its *expression* analysis.

## Standing standards (inherit from signal/)

Root/char anchor stated · ≥20 editable slides · ≥half visual · figures computed from Book6.xlsx (use the **rasm / letter** columns) · beat a null AND a natural-language baseline · scale rule · audit ✓/✗/~ · no "scientific-miracle" claims · per-lecture kit + exams.

## Status

SEED only. Not started. Flagged during the signal course (Lecture-1/2 design) for critical review.

## Objective — latent features in the Qur'an (the only point)

This series is **not** information theory for its own sake. Its goal is the same as the signal course: **discover latent (hidden, non-obvious) features in the Qur'an**, held to the strict bar — *latent · Qur'an-specific (beats a natural-language baseline) · found by the method · reads back to the text.* The char level is chosen because it can reach structure the root level cannot: pure-symbol, sub-semantic, transmission-layer structure.

### Candidate latent-feature hunts (each to be null- and baseline-tested)

1. **Muqaṭṭaʿāt anomaly.** The disjoint letters (الم, حم, ن, ق …) are pure characters with no root/meaning — the ideal char-level object. *Testable claim:* do the muqaṭṭaʿāt of a sūra over-represent that sūra's most frequent letters beyond a length-matched null? A real, classic, falsifiable hypothesis only the char level can pose.
2. **Mutual-information decay length.** How far does letter-to-letter dependency reach (MI vs lag)? A characteristic correlation length that differs from matched random Arabic would be a genuine latent signature.
3. **Entropy / compressibility outliers.** Which sūras are anomalously ordered (low conditional entropy, high gzip-compressibility) versus the corpus AND versus random Arabic? Outliers that read back to real features (e.g. heavy refrain/rhyme) are candidates.
4. **Boundary information (separate regime, col 7).** Does word-boundary predictability carry Qur'an-specific structure beyond ordinary Arabic?

### Honesty clause

As in the signal course, expect most char-level structure to be **generic to Arabic** (its orthographic redundancy ≈ 24%). Only the residue that beats the natural-language baseline and reads back counts as a latent feature of the Qur'an. The muqaṭṭaʿāt test is the most promising — and the most falsifiable — place to look.


> **See also:** the disjoint-letter *pointer* result that emerged from this char-level work is now its own focused study in `../disjoint_letters/` (REPORT.md + FINDINGS.md).

# Char-Level Series — Methodology Decision: the SPACE question (locked)

**Source:** the de-diacriticized text, **col 6** (it contains all characters). Persian letter forms (ی، ک) and hamza variants give a **37-letter** inventory.

## Decision (data-driven)

| Regime | alphabet | H₁ | H(Xₙ\|Xₙ₋₁) | shuffled baseline | MI | redundancy |
|---|---|---|---|---|---|---|
| **A — letters only (PRIMARY)** | 37 | 4.405 | 3.969 | 4.402 | 0.436 | 23.8% |
| B — letters + space | 38 | 4.028 | 3.287 | 4.026 | 0.741 | 37.4% |

*(within-verse bigrams, no cross-verse bridging; shuffled = same unigram, order destroyed)*

**Space is NOT counted as a character** for the core information-theory measures. Reasons:
1. Space is **28% of all symbols** — far above natural Arabic word-spacing (~15–18%) — because col 6 **splits clitics** (ال, ب, و, ف…). It is a *sub-word* boundary, not a word boundary.
2. Including it nearly **doubles** the apparent mutual information (0.436 → 0.741) and inflates redundancy (+14 pts); ~0.3 of those bits measure the **tokenizer's segmentation**, not the letter system.
3. The intrinsic, corpus-comparable quantity (entropy/redundancy of the Arabic script) requires letters only.

## Rules for the series

- **Primary analyses:** letters only; reset the model at token boundaries (bigrams within a token/verse), never across verses.
- **Boundary/segmentation studies:** allowed but **separate and explicitly labeled**, and they must use **natural word boundaries (col 7)**, not col-6 clitic splits.
- **Never mix regimes** in one claim; always state which regime a number came from.
- Same locked discipline as the signal course: sampled null, **natural-language baseline** (shuffled-letter and other-Arabic-corpus), FDR, read-back, audit ✓/✗/~.

## Headline real result (Regime A)

The de-diacriticized Qur'anic letter stream carries genuine **sequential memory**: conditional entropy 3.969 vs a shuffled 4.402 bits/char (MI = 0.436 bits, redundancy 23.8%) — the consonantal skeleton is far from random, exactly as an information-bearing, error-resilient channel should be.

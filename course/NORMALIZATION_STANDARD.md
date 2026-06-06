# Normalization Standard — LOCKED (all weeks)

_Locked 2026-05-30. Size is the recurring confound in this corpus, at every level. This standard fixes how we normalize so the trap does not recur._

## The rule
**Always normalize density to per 1,000 ROOT-TOKENS (size-true). Never normalize by a count of containers (ayahs or surahs), because containers vary in size.**

- Corpus level (Week 1): a root's rate = term-frequency ÷ 51,044 total root-tokens × 1,000. (Per-1,000-ayahs is reported too, but only as "share of verses," never as the size-true measure.)
- Surah level (Week 2, home surah / density): prevalence = the root's tokens in the surah ÷ the surah's total root-tokens × 1,000. **Do NOT divide by the surah's ayah count** — ayahs vary in length just as surahs do, so per-ayah density is still confounded.
- Same logic applies at any future level: the denominator is always root-tokens, never a container count.

## Why (the tested evidence)
- al-Baqara is the largest surah by both ayahs (286) and root-tokens (3,966), so raw counts crown it for 30 of the 50 most frequent roots. Normalizing (either way) drops it to 0/50.
- But per-ayah and per-root-tokens can disagree. Worked case ṣabr (صبر): raw busiest = al-Baqara → per-AYAH home = al-Kahf → per-ROOT-TOKENS home = at-Tur. Three different surahs; only per-root-tokens is size-true.

## Support floor (small-sample reliability)
A size-true home is trusted only if: **count ≥ 3 in the surah AND the surah has ≥ 30 root-tokens.** If no surah qualifies, report **"insufficient support,"** not a number. (Example: ʿusr (عسر) — its highest prevalence, ash-Sharh at 2/16 tokens = 125/1k, fails the floor; ʿusr has no reliable home.)

## Unit
Report **per 1,000 root-tokens** everywhere for cross-week consistency (per-100 is simply this ÷ 10). Round to one decimal at the surah level.

## Enforcement
- Any figure, table, or claim that reports a density must state the denominator as root-tokens.
- Verification grep for each week's docs: flag "per 1k ayahs" / "÷ surah ayahs" used as a *size-true* claim (allowed only when explicitly labeled "share of verses," not as density).

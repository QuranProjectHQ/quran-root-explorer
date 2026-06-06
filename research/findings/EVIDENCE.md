# EVIDENCE LEDGER — objective results, all run on Book6.xlsx

Facts only. Each row is reproducible: `python <script>` from this folder.
No recommendations in this file.

## 0. Data foundation (verified)
- ayahs = 6,236 ; unique roots = 1,701  (matches README)
- character stream N = 332,202 ; alphabet = 29
- root stream N = 51,024
- letter stream = normalize_letters() output: diacritics STRIPPED, letter
  variants folded. (Modeling choice: consonant/long-vowel skeleton, NOT the
  voweled/recited signal. Diacritized column exists but was not used.)

## 1. Estimator validity — known-answer controls  [script: refcal_test.py, seq_derisk.py]
| reference            | DFA alpha | long-range MI mass | expected      | pass |
|----------------------|-----------|--------------------|---------------|------|
| IID (random)         | 0.497     | 0.0013             | 0.5 / 0       | yes  |
| Markov-1 (short mem) | 0.495     | 0.0010             | 0.5 / ~0      | yes  |
| fGn H=0.8 numeric    | 0.798     | n/a                | 0.8           | yes  |
| fGn H=0.8 symbolic   | 0.794     | 0.1921             | ~0.8 / >0     | yes  |
IID MI-excess at d=1/5/20 = -0.0001 / +0.0000 / +0.00007 (no false structure).

## 2. Corpus placement on the random->critical axis  [refcal_test.py]
| stream                 | DFA alpha | long-range MI mass |
|------------------------|-----------|--------------------|
| QUR'AN character       | 0.554     | 0.0367             |
| QUR'AN root            | 0.685     | 0.4751             |
Fact: both exceed random/Markov (0.5 / ~0). The ROOT stream sits near the
critical fGn(H=0.8) anchor; the CHARACTER stream is only mildly persistent.

## 3. Long-range structure is beyond low-order Markov  [seq_derisk.py]
- character, MI(d) decay: power-law R^2 = 0.924 vs exponential R^2 = 0.474
- character long-range MI mass (d>=5): real 0.0368 vs Markov-3 surrogate 0.0049 = 7.5x
- block-entropy rate, real: 4.09 -> 3.77 -> 3.28 -> 2.58 bits (memory present)
- block-entropy rate, shuffled: 4.09 -> 4.08 -> 4.04 (flat; none)
- DFA character: 0.554 (freq-encoding), 0.580 (rank-encoding); shuffled 0.503
- gzip redundancy: character 26.3% , root 14.2% (real compresses better)

## 4. Scale adjudication (normalized, beyond own baseline)  [scale_adjudicate.py]
| metric                              | character | root  |
|-------------------------------------|-----------|-------|
| marginal entropy H1 (bits)          | 4.09      | 8.44  |
| highest ESTIMABLE Markov order      | 2         | 1     |
| near MI / H1 (d=1..4)               | 0.121     | 0.177 |
| long-range MI / H1 (d>=5)           | 0.009     | 0.056 |
| beyond own-Markov ratio (d>=5)      | 69.7x     | 11.1x |
| effective memory length (symbols)   | 6         | 50    |
| compression redundancy %            | 26.3      | 14.2  |

## 5. Cross-scale binding (spelling <-> meaning)  [xscale_test.py]  RESULT: NEGATIVE
- phonosemantic Mantel, n=665 roots: r = 0.0030 ; perm null mean -0.0001 sd 0.0057 ; p = 0.275
- consonant-slot semantic lift (triliteral n=660):
    slot 1: p = 0.582 ; slot 2: p = 0.403 ; slot 3: p = 0.081 (weak, not significant)
- Fact: a root's character composition does NOT predict its distributional
  meaning in this corpus under these operationalizations.

## 6. Reference calibration against external natural corpora (DNA / language / music)
- STATUS: NOT RUN. Requires importing those data files; not bundled. Pending data,
  not method. The synthetic anchors in section 1 validate the method itself.

## 7. TEN-IDEA SWEEP (each run on real data with a null)  [ideas_batch1.py, ideas_batch2_slim.py]
| # | idea | result | null / effect | verdict |
|---|------|--------|---------------|---------|
| 1 | verse-length long memory (DFA) | alpha=0.971 | shuffled 0.510, z=22 | STRONG but see control |
| 2 | verse-length autocorr lag-1 | ac1=0.490 | p=0.001 | real |
| 3 | verse-length spectral slope | -0.433 | shuffled ~0 | real (same signal) |
| 4 | rhyme: ayah-final-letter entropy | H=1.116 | shuffled 2.094, p=0.003 | ROBUST (known: fawasil) |
| 5 | root burstiness (CV of gaps) | median CV 1.30 | 66% > 1.2 (Poisson=1) | real (topical) |
| 6 | per-root occurrence DFA | median alpha 0.588 | shuffled ~0.514 | modest |
| 7 | Heaps vocab-growth exponent | beta=0.392 | new-root var 607 < shuf 894 | real (even unfolding) |
| 8 | directional flow (transfer-entropy asym) | 10/28 pairs sig | circular-shift null p<.05 | NOVEL, survives null |
| 9 | root->surah localization (MI) | excess 0.242 bits | vs shuffle | robust (topical) |
| 10 | revelation-order vs lexical richness | rho=-0.452 | p=4.5e-7 | STRONG but see control |

## 8. CONFOUND CONTROLS on the two front-runners  [confound_controls.py]
- IDEA 1: DFA raw 0.971 -> within-surah detrended 0.533. The "long memory" was
  almost entirely SURAH-BLOCK / level structure, NOT genuine sequence memory.
  DOWNGRADED.
- IDEA 10: spearman(rev, TTR) -0.452, but TTR vs length = -0.925 (mechanical),
  length vs rev = +0.458; PARTIAL(rev, TTR | length) = -0.084 -> collapses.
  Using root entropy: spearman +0.396, PARTIAL(rev, entropy|length) = -0.231 ->
  weak residual only. LARGELY A LENGTH ARTIFACT. DOWNGRADED.

## 9. SURVIVORS (verified, suitable to implement)
- #4 rhyme/fawasil quantification — robust, label-shuffle null; KNOWN structure,
  so a strong validation feature rather than a discovery.
- #8 directional information flow (transfer entropy) — survives circular-shift
  null on 10/28 root pairs; NOVEL ("communication", with direction). Build step 1
  must be a co-location replication control before shipping.
- #9 root->surah localization, #5 root burstiness — robust but expected (topical).

## 10. Transfer entropy vs the app's existing measures  [te_vs_app.py]
- corr(symmetric co-location, |TE asymmetry|) = +0.80  (magnitude scoped by co-location)
- corr(app lead-lag asym, TE asym) = -0.25 ; top-5 directional pairs overlap 1/5
- Verdict: app ALREADY has symmetric co-location AND a directional lead-lag graph
  (directed_lead_lag_graph). TE differs only by conditioning on the target's own
  past; gives different directions but tiny magnitudes. NOT a new lens. DROPPED.

## 11. Higher-order synergy — interaction information on triples  [synergy_test.py]  POSITIVE
- 24 roots (freq>=100), 2024 triples; null = independent circular shifts.
- 232/2024 triples (11%) beyond null |II| 95th pct (vs 5% expected).
- of those: 193 SYNERGY (II>0) vs 39 redundancy -> strongly synergy-skewed (not noise).
- strongest synergy triples are coherent: كون+ءمن+عمل ("believe & do good"),
  ءله+ربب+رحم (God/Lord/mercy), شيء+عذب+رحم, ءله+ءمن+سمو.
- The app's triad/motif page counts co-occurrence of triples; it does NOT measure
  info-theoretic 3-way synergy. NOVEL + tested + interpretable. Magnitudes small.
- => RECOMMENDED as the one feature to implement.

## 12. Tensor decomposition (root x surah x position)  [tensor_test.py]  WEAK
- rank-5 NTF explained var 0.787; position-mode non-uniformity real 0.179 vs
  shuffled 0.071 (z=+2.2, below z>3 bar); marginal I(position;root)=0.128 bits.
- The position third-mode is near-degenerate -> a tensor adds little over 2-way SVD
  here. Other 3rd-mode choices (revelation-window, partner) remain UNTESTED.

## 13. Synergy — frequency control + FDR (within-verse)  [synergy_freqcontrol.py]
- per-triple null (each root circular-shifted; preserves rate, breaks dependence).
- synergy p<0.05: 61/560 (11%) vs 5% chance; LOW-freq 0.11 = HIGH-freq 0.11
  (NOT a frequency artifact).
- survive BH-FDR q<0.10: 0  (best q=0.28). No INDIVIDUAL triple defensible.

## 14. Synergy — across-verse / surah level (latent-motif domain)  [synergy_acrossverse.py]
- surah-level presence, 16 roots, per-triple permutation null.
- synergy p<0.05: 1/560 (BELOW 5% chance); survive FDR: 0 (q=1).
- => NO across-verse 3-way synergy. Does not support the latent-motif claim.

## 15. REVISED synergy verdict
- Real but WEAK aggregate within-verse effect (2x chance, frequency-balanced).
- Cannot name specific synergistic triads (none survive FDR).
- Absent across-verse. Rating revised 6/10 -> ~3/10.

## 16. Within-surah long-range SEQUENCE structure — FIRST CANDIDATE TO PASS ALL GATES
Object: order of words/roots within a surah (Tier-1: order is transmitted).
Null: within-surah shuffle (preserves each surah's composition -> tests ORDER, not topic).
  [within_surah_rasm.py, within_surah_content2.py, content_confirm2.py, surface_provenance.py]

- The signal: excess long-range MI (d>=5) with a NON-DECAYING plateau (d=8..30 ~ flat)
  -> roots/words organize into coherent passages/sections spanning the whole surah.
- ROOT representation (top-500+OTHER):
    G2 significance: real LR 12 SD above shuffle floor (p at 20-shuffle resolution =0.048)
    G5 effect size : 1.39% of H1 (floor 1%) PASS
    beyond-Markov-1: 9.6x PASS    G6 robustness: split-half 1.11%/1.11%, drop-largest 1.28% PASS
- SURFACE-WORD representation (Tier-1, no root abstraction):
    excess 1.26% of H1, z=10.1, beyond-Markov 4.3x -> survives. Provenance PASS.
- G7 novelty: app has within-AYAH co-occurrence + single-root recurrence-vs-Poisson (Signal),
  but NOT within-surah multi-root positional/sequence MI. Novel (closest neighbor noted).
- Honest bounds: a STRUCTURAL/organizational feature (passage sectioning), magnitudes
  modest (~1.3% of entropy) but pre-registered-floor-clearing, highly significant (z~10),
  robust, beyond-Markov, and provenance-clean. NOT a "hidden code".

VERDICT: GO. First feature this session to clear every pre-registered gate.
Home: Two Books / Signal area (or a new within-surah "passage structure" view);
complements root-recurrence with multi-root long-range organization.

## 17. SCRUTINY of the within-surah candidate (drift control)  [drift_control.py]  -> DOWNGRADED
Segment-shuffle null (preserves coarse positional composition / drift):
  3 seg: beyond-drift 1.32% H1 | 6 seg: 1.10% | 12 seg: 0.83% (below floor).
Residual erodes monotonically as segmentation refines -> signal is smooth within-surah
compositional DRIFT (topical nonstationarity), generic to all long text, NOT discrete
passages. Novelty ~2. SCORE 6 -> 3/10. GO RETRACTED; not a discovery.
Lesson: significance+beyond-Markov+robustness insufficient; trivial-explanation control
(drift, generic-text) is mandatory before any GO. (New gate G9 in DISCOVERY_CRITERIA.md.)

## 18. CROSS-LANGUAGE REGISTER SIGNAL (best-supported finding) [modes.py]
Metric: syntactic structure (function-word sequence MI+rep) measured as DEVIATION
from each text's OWN Markov surrogate (language-fair; ordinary-anchored).
  POSITIVE (above ordinary): QURAN(ar) +0.18, Bible(en) +0.15
  NEGATIVE (below ordinary): Austen,Doyle,Aesop(en), Candide(fr), Faust(de), Quijote(es)
Control built-in: English Bible patterns with Arabic Quran, NOT with English novels
=> split is REGISTER (scripture vs secular), not language; holds across ar/en/fr/de/es.
Also verified independent of the repetition mode (corr +0.35) and of rhythm/novelty.
NOVELTY mode #1 was an artifact (killed by the Markov control -> #9). RHYTHM: Quran #1
but largely KNOWN (saj'/fawasil).
DISCOVERY (modest, honest): scripture carries ABOVE-ordinary syntactic/function-word
sequence structure; secular literature BELOW-ordinary — cross-language, ordinary-anchored,
survives a partial language control. Quran leads it.
LIMITS: Quran ~ Bible (scripture effect, not Quran-unique); n=2 scriptures. To separate
Quran from scripture-general needs more scriptures + clean Arabic comparators (tooling blocker).

---

## #19 — SYNTACTIC deviation-from-ordinary: REFUTED (sample-size + ordinary-Arabic controls)

**Claim under test (from #18):** "Syntactic deviation from a text's own order-1 Markov
surrogate is uniquely elevated for the Arabic Qur'an (+0.180, rank #1), distinguishing it
from other scriptures and secular texts; effect lives in the Arabic FORM."

**Two decisive controls, both run on real data (synt_arabic_test.py, synt_confirm.py):**

1. **Equal sample size (the killer).** The original ranking compared the FULL Qur'an
   (~135,000 words) against ~18,000-word comparators. SYNT-deviation is strongly
   sample-size-biased (finite-sample MI/rep bias). Re-running on fixed-size sliding
   windows for ALL texts:
     - N=1400 words: QURAN(ar) = +0.088 — **LAST of 12 texts.**
     - N=1200 words: QURAN(ar) = +0.045 — 8th of 12.
     - N=2500 words: QURAN(ar) = +0.215 — 3rd of 12.
   The Qur'an's value AND rank swing wildly with window size → the metric is not a
   stable, scale-free property; the #1 placement was an artifact of unequal N.

2. **Ordinary-Arabic comparator (new on-disk data: Tabari, classical Arabic prose,
   ~1,730 words, corpus/ar_tabari.txt).** At EVERY window size tested, ordinary Arabic
   (Tabari) scores HIGHER than the Qur'an:
     - N=1200: Tabari +0.339 vs Qur'an +0.045
     - N=1400: Tabari +0.379 vs Qur'an +0.088
     - N=2500: Tabari +0.357 vs Qur'an +0.215
   So the effect is not "elevated in the Arabic Qur'an" — ordinary Arabic shows MORE of
   it. What residual Arabic>others gap exists is plausibly orthographic/tokenization
   (Arabic word-forms via regex; Qur'an uses morphological seg-tokens), not a designed
   Qur'anic property.

**Verdict:** FAILS G5 (no stable effect floor), G6 (not robust to window size),
G9 (trivially explained by sample size + tokenization). The SYNT mode is DROPPED as a
discovery candidate. Lesson logged: any cross-text metric MUST be compared at equal
sample size with a same-language ordinary control before any ranking is trusted.

Status: closes the "separate Qur'an from scripture/Arabic" question for this metric —
there is no Qur'an-specific signal here to separate.

---

## #20 — ALL word-level modes (REP/SYNT/NOV) fail TOKENIZATION-INVARIANCE

Re-ran the equal-N (1500-word windows), own-Markov-controlled mode audit
(modes_equalN.py) but tokenized the Qur'an THREE ways and compared against a
same-language ordinary control (Tabari) + 10 cross-language texts.

The Qur'an's rank on the SAME metric flips to opposite extremes purely by changing
tokenization (morphological seg-tokens=135k vs whitespace words=78k — identical text):

  SYNT_dev :  QURAN(whitespace) = #1/13 (+0.452)   QURAN(segmented) = #13/13 (+0.112)
  NOV_dev  :  QURAN(segmented)  = #1/13            QURAN(whitespace) = #11/13
  REP_dev  :  whole field bunched +0.137..+0.150 (Qur'an ws #1 but within 1 sd of
              ordinary Arabic Tabari #4) — no outlier either way.

**Conclusion:** these surface word-statistics are dominated by the analyst's
tokenization choice, not by any intrinsic property of the text. A genuine latent
feature MUST be invariant to tokenization. REP, SYNT, NOVELTY are therefore DROPPED
as Qur'an-discovery candidates (they remain fine as descriptive UI stats).

### NEW LOCKED GATE — G10 (Invariance)
A candidate cross-text metric is INADMISSIBLE unless its value/ranking is stable under
BOTH:  (a) equal sample size (fixed-N windows for every text), and
       (b) tokenization choice (≥2 tokenizations: whitespace words AND morphological
           segments give the same verdict),
       tested against a SAME-LANGUAGE ordinary baseline (e.g. Tabari for Arabic).
The tokenization-free way to satisfy (b) by construction is to work at the
CHARACTER / consonantal-rasm scale (no token boundaries to choose). This is the
principled home for the "sequence scale" the project prioritizes.

---

## #21 — CHARACTER / RASM battery (tokenization-free): valid tools, Qur'an NOT elevated

Built a 9-metric character-level battery on consonantal rasm (char_battery.py):
conditional entropies h1/h2/h3, excess-entropy, char-MI near (lag1-2) & far (lag8-32),
3- & 5-gram repetition, gzip compressibility, DFA long-range exponent. Tokenization-free
by construction (operates on the letter stream), so it satisfies G10(b) automatically.

**Tool validity — degradation ladder (Qur'an rasm, L0 original → L4 full scramble):**
metrics move monotonically and strongly with structure destruction, so the battery
genuinely measures sequence structure (not noise):
  MI_near 0.841 → 0.264 (within-word shuffle) → 0.034 (full scramble)
  rep5    0.603 → 0.198 → 0.053 ;  comp 0.219 → 0.317 → 0.347 (less compressible)
  (DFA ~0.5 flat = no long-range power law in the letter series; excess-E weak — both
   poor discriminators here and de-prioritised.)

**Discovery test — Qur'an vs ordinary Arabic (Tabari) at equal-N (4000-char windows):**
On every VALIDATED structural metric the Qur'an is EQUAL-or-LOWER than ordinary Arabic:
  MI_near  Qur'an 1.109 vs Tabari 1.196  (-1.7 sd)
  MI_far   Qur'an 0.443 vs Tabari 0.466  (-1.6 sd)
  excessE  Qur'an 2.091 vs Tabari 2.181  (-1.8 sd)
  comp/h1/h2 ~ equal. (Only h3 is +4.2 sd but the absolute gap is 0.05 bits — inflated
  by tiny window variance, and HIGHER h3 = MORE random, not more crafted.)
All meaningful gaps point the SAME direction (Qur'an ≤ ordinary Arabic) → robust in
direction even though Tabari n=3 windows.

**Beyond-Markov check:** Qur'an does exceed its own order-1 char-Markov surrogate
(MI_near 1.11 vs 0.87; rep5 0.29 vs 0.07) — but that is generic to any real-word text;
Tabari shows the same. Not Qur'an-specific.

**VERDICT (sequence scale, surface statistics — now thoroughly explored):**
Across word scale (REP/SYNT/NOV, EVIDENCE #18-20) AND character/rasm scale (this #21),
under sample-size + tokenization + same-language(Arabic) + degradation-ladder controls,
there is NO detectable Qur'an-specific elevation in surface sequence statistics
(entropy, mutual information, repetition, compressibility). The tools are valid (they
pass the ladder), so per the telescope principle this is a precise negative about THIS
class of feature: surface, local, stationary n-gram/information statistics are blind to
whatever distinguishes the text. Search should move to (a) the SEMANTIC / root-concept
relational scale (networks, cross-reference, long-range topical structure — partly
already in the app), and/or (b) genuinely non-local / compositional sequence features,
NOT more surface n-gram statistics. Caveat: Tabari baseline is one short clean sample;
a larger born-digital Arabic corpus would tighten magnitudes (not expected to flip sign).

---

## #22 — G10 RE-AUDIT of the entire KEEP registry → ALL DEMOTED  [reaudit_keep.py]

The metrics_collection.tsv "KEEP" set was certified on a positive control of
Arabic-scripture vs ENGLISH-secular ("scripture↑") — a language/script contrast, never
equal-N vs a same-language Arabic baseline. Re-ran every KEEP metric at equal-N windows
for Qur'an(whitespace) + Qur'an(segmented) + ordinary Arabic (Tabari):

  metric    Q(ws)   Q(seg)  Tabari   ws_sd  seg_sd   verdict
  mi3_w    4.0569  3.5739  4.1411   -1.0   -4.1    FAIL (Quran≤ORD, tok-flips)
  mi5_w    3.9811  3.4554  4.0838   -1.2   -4.6    FAIL (Quran≤ORD, tok-flips)
  rep4_w   0.0736  0.0602  0.0508   +1.6   +0.7    FAIL (tok-dependent, <2sd)
  gz_w     0.5493  0.5299  0.5643   -2.0   -2.9    FAIL (Quran MORE compressible than ORD)
  mi5_c    0.1828    —     0.1992   -1.4    —      FAIL (~ORD)
  rep4_c   0.4614    —     0.4411   +1.3    —      FAIL (~ORD)
  gz_c     0.2741    —     0.2775   -0.7    —      FAIL (~ORD)

**Result:** 0 / 7 KEEP metrics distinguish the Qur'an from ordinary Arabic under G10.
Registry corrected: all KEEP → DEMOTE (descriptive-only). The "scripture↑" certification
was a same-language confound. (Caveat: Tabari word-baseline is n=1 window; char-baseline
n=3. Direction is consistent with #20/#21 and unlikely to flip with more data, but a
larger born-digital Arabic corpus would firm up word-metric magnitudes.)

### Consolidated state of the surface-statistics search (EVIDENCE #18–22)
Word scale (REP/SYNT/NOV) and char/rasm scale (9-metric battery) and the full KEEP
registry have ALL been put through equal-N + tokenization + same-language(Arabic) +
degradation-ladder controls. Nothing survives as Qur'an-specific. The batteries are
ladder-validated (they DO measure structure), so this is a trustworthy negative about
the feature CLASS: local stationary information/repetition/compression statistics do not
separate the Qur'an from ordinary Arabic. Live non-surface candidates remaining:
synergy (within-verse, weak ~3/10, untested vs Arabic baseline) and genuinely non-local
/ semantic-relational structure (untested under G10).

---

## #23 — NON-LOCAL battery (first pass, char/rasm): long-range REPETITION is the one lead
[nonlocal_battery.py]  Tabari baseline n=1 window — FIRST PASS, to be tightened.

**Non-locality ladder (Quran 8k-char window; block-shuffle preserves local texture,
destroys long-range arrangement):** this rung is what separates real non-local structure
from local texture masquerading as long-range:
  MI_long  L0 0.317 ≈ block 0.317 ≈ full 0.312  -> NOT non-local (estimator bias floor). DROP.
  MI_mid   L0 0.259 ≈ block 0.257               -> local. DROP as non-local.
  dfa      0.547 ≈ block 0.528 (~0.5 random-walk) -> no long-range power law. DROP.
  comp     responds to full-scramble but not block-order -> LOCAL redundancy. DROP as non-local.
  rep12    L0 0.0535 > block 0.0483 > full 0.000 -> NON-LOCAL, valid.
  rep20    L0 0.0216 > block 0.0187 > full 0.000 -> NON-LOCAL, valid.
Only distance-agnostic long-substring repetition (rep12/rep20) is a genuinely non-local,
ladder-valid metric here.

**Quran vs ordinary Arabic (Tabari), equal-N 8000c:**
  rep12  Quran 0.0611 vs Tabari 0.0478  (+1.5 sd, beyond-Markov: Markov=0)
  rep20  Quran 0.0185 vs Tabari 0.0102  (+1.5 sd, beyond-Markov: Markov=0)
  (MI_long -2.2sd, comp -2.1sd, dfa -1.5sd — but these are non-valid per the ladder.)

**Read:** the Qur'an carries MORE long-range exact repetition (refrains/formulae:
e.g. fawasil, divine-name formulae, repeated verse-templates) than ordinary Arabic — the
FIRST Quran>ordinary signal on a validated, tokenization-free, non-local metric.

**Three honest caveats (why this is a lead, not a finding):**
1. +1.5 sd is BELOW the G10 >2sd bar; Tabari baseline is n=1 window (no error bar).
2. NOVELTY is LOW — Qur'anic refrain/formulaic structure is well known (saj', fawasil).
3. Must confirm it isn't driven by trivial high-frequency function-word runs.
=> Discovery rating ~2-3/10 (known feature, weak), but it is the strongest lead from the
non-local scale and the only metric class worth tightening. DECISIVE next step: a larger,
cleaner born-digital Arabic baseline (≥5 texts, multiple genres) to test whether
rep12/rep20 Quran>ordinary survives at >2sd, with a frequency-control (mask top function
words) to kill caveat #3.

---

## #24 — rep lead resolved across THREE Arabic registers → REGISTER GRADIENT, not Quran-specific
[tighten3.py]  Born-digital Arabic baselines now on disk (3 registers, "news feeds" idea):
classical Tabari, modern literary novel (أرض السافلين), MSA news (BBC Arabic RSS).

Long-range repetition (char rasm, equal-N 2500c) shows a clean REGISTER gradient:
  metric   Quran   Tabari(class)  Novel(lit)  News(MSA)   Q vs pooled-ORD
  rep8     0.0858    0.0737        0.0543      0.0309       +1.2 sd
  rep12    0.0356    0.0283        0.0149      0.0092       +1.0 sd
  rep20    0.0108    0.0073        0.0031      0.0000       +0.7 sd
  MI_near  1.2530    1.3336        1.2311      1.1920       -0.3 sd  (null, confirmed)

Reading: repetition tracks REGISTER/orality (news low -> literary -> classical formulaic
-> Quran highest). The Quran is at the TOP of the gradient, but its gap over the NEAREST
register (classical formulaic Tabari) is small and < 2 sd (rep12 0.036 vs 0.028). The
+1.0 sd vs pooled-ordinary was inflated by averaging in low-repetition news/literary.

VERDICT: the one non-local lead (long-range repetition, #23) does NOT clear G10 (>2sd vs
same-register ordinary Arabic). It is a register/formulaic property with the Quran at the
extreme — modest, register-confounded, and low-novelty (refrains/fawasil known). Discovery
~2-3/10, unchanged. The "news feeds" register was decisive: it anchored the low end and
exposed the gradient. Corpus now: corpus/ar_tabari.txt, ar_novel.txt, ar_news.txt
(3 registers; still modest size — news n=1 window — but gradient is consistent).

---

## #25 — SCALED 3-register + frequency control: CONTENT-word repetition is the refined lead
[tighten_scaled.py, content_rep.py]  News register expanded via RSS (BBC + Euronews
Arabic) to ~1640 words / 8 windows; classical Tabari ~7 windows, literary novel ~7.

Long-range char repetition, equal-N 2500c windows, Quran (60-80 windows) vs each register:

RAW (all words) — Quran vs nearest register (classical Tabari):
  rep8  Quran 0.090 vs Tabari 0.075  (+0.9 sd, bootstrap P=0.73)
  rep12 Quran 0.037 vs Tabari 0.028  (+0.8 sd, P=0.68)        -> ~ classical (register-bound)

FREQUENCY CONTROL (drop top-20 / top-50 frequent words = content-only stream):
  drop20 rep8  Quran 0.068 vs Tabari 0.044  (+1.4 sd, P=0.82)
  drop20 rep12 Quran 0.027 vs Tabari 0.013  (+1.3 sd, P=0.83)
  drop50 rep8  Quran 0.058 vs Tabari 0.035  (+1.5 sd, P=0.85)
The gap GROWS when function words are removed -> the Qur'an's distinctive long-range
repetition is in CONTENT words (meaning-bearing refrains/formulae), not function-word runs.

Consistent register ordering on every metric & control: News < Novel < Tabari < Quran.
  vs News (MSA):     +2.6 to +4.2 sd (raw), +1.8 to +3.1 sd (content)
  vs Novel (lit):    +1.7 to +2.0 sd (raw), +1.5 to +2.4 sd (content)
  vs Tabari (class): +0.8 to +0.9 sd (raw), +1.3 to +1.5 sd (content)  <- the hard one

VERDICT: refined and firmed. The Qur'an's long-range CONTENT-word repetition clearly
exceeds modern Arabic registers and carries a Qur'an-specific increment over even
classical formulaic Arabic (+1.4 sd, P~0.83) — SUGGESTIVE but still < the 2sd G10 bar,
and classical baseline is only ~5-7 windows. Rating ~3-4/10 (up slightly: content-control
robustness + clean monotone register ordering; still register-confounded and sub-bar vs
classical; refrains are a known feature). 
DECISIVE NEXT STEP to settle it: enlarge the CLASSICAL register (more clean classical
Arabic windows) — if the +1.4sd content-repetition increment over classical reaches >2sd
with a proper baseline, this graduates from register-effect to a defensible Qur'an-specific
finding; if it stays ~1sd, it is confirmed as a classical/oral-formulaic register property.
Pipeline proven: RSS for MSA; archive.org born-digital for literary/classical.

---

## #26 — POSITIVE-CONTROL-FIRST: "what separates Shakespeare" ≠ "what separates the Quran"
[shakespeare_sep.py, apply_mastery.py]  Reframing (user): classic measures are universal
across all texts/languages, so they CANNOT detect mastery (explains every null in #18-25).
Method: FIRST find measures that separate Shakespeare from ordinary English, THEN port only
those to the Qur'an.

WHAT SEPARATES SHAKESPEARE (equal-N 1500w, vs Austen/Doyle/Aesop/Candide/Quijote):
  CLASSIC measures FAIL (confirming the reframing):
    charMI +0.3sd, gzip +0.9sd, ttr +1.0sd, hapax +0.2sd, mean_wl -0.5sd  -> NO separation
  NON-classic measures SEPARATE him (>2sd):
    sentence-length CV   0.15 vs 0.48  (-8.1sd)  rhythmic/metrical UNIFORMITY
    word-length std      1.90 vs 2.28  (-2.8sd)
    Yule's K             69.5 vs 104.7 (-2.6sd)  richer vocabulary (less word-repetition)
    word entropy         8.21 vs 7.94  (+2.5sd)  more diverse vocabulary
    frac long words      0.06 vs 0.10  (-2.1sd)
  => Shakespeare's signature = RHYTHMIC REGULARITY + LEXICAL RICHNESS/VARIETY.

PORTING those detectors to QURAN vs ordinary Arabic (PRELIMINARY — Arabic baselines n=1
window each; needs volume):
    unit_cv (ayah len)  Quran 0.53 HIGHER than ordinary (+1.1sd) -> OPPOSITE of Shakespeare
    Yule's K            Quran 53.7 > modern Arabic 33 -> LESS rich -> OPPOSITE
    word entropy        Quran 8.61 < modern Arabic 8.9-9.4 -> OPPOSITE
  => The Shakespeare detectors DO NOT fire for the Qur'an; several fire in REVERSE.

SYNTHESIS: masterpieces do not share one universal "mastery" axis. Shakespeare maximizes
VARIETY (rich vocabulary, uniform meter); the Qur'an's distinctive axis is the inverse —
STRUCTURED REPETITION / content-refrain density (#25). Judging the Qur'an by Shakespeare's
yardstick (or vice versa) misses both. The right program is SYMMETRIC: find each text's OWN
separators against its OWN ordinary-language baseline.
STATUS: Shakespeare side is solid (many windows). Qur'an side is PRELIMINARY (baseline n=1).
NEXT: ordinary Arabic AT VOLUME (classical + more news/literary) -> run the full battery to
find what separates the Qur'an from ordinary Arabic with real error bars (the symmetric
counterpart of the Shakespeare result). Caveat on sentence-CV: Shakespeare is verse vs prose
baselines, so part of the -8.1sd is verse-vs-prose; a poetry baseline would sharpen it.

---

## #27 — SYMMETRIC RESULT: Shakespeare = VARIETY, Qur'an = REPETITION (mirror images)
[symmetric_quran.py]  Ran the SAME battery used to characterize Shakespeare, now on the
Qur'an vs ordinary Arabic (3 registers; Quran 120 windows, ordinary ~10 pooled @ N=800).

WHAT SEPARATES THE QUR'AN (only the repetition family separates it; everything else null):
  contrep8 +1.5sd, crep8 +1.5sd, contrep12 +1.3sd, crep12 +1.2sd, gzip -1.5sd (=redundant)
  Shakespeare's separators do NOT fire: yuleK +0.9 (no), word_ent -0.8 (no),
  std_wl +0.4 (no), frac_long +0.1 (no), ttr -0.8 (no), charMI 0.0 (no).

THE MIRROR (the key insight):
  * Shakespeare deviates from ordinary English by MAXIMIZING VARIETY:
      richer vocabulary (Yule's K -2.6sd, word-entropy +2.5sd), uniform meter
      (sentence-CV -8.1sd), and LESS repetition (char-rep -1.8sd vs ordinary English).
  * The Qur'an deviates from ordinary Arabic by MAXIMIZING STRUCTURED REPETITION:
      content-refrain repetition (+1.2..1.5sd), higher redundancy (gzip), while vocabulary
      richness is ~ordinary (not elevated).
  => OPPOSITE craft strategies. Each masterpiece deviates from its own "ordinary" baseline
     in a DIFFERENT direction, and each is invisible to (a) classic info measures and (b)
     the OTHER's signature. This is the precise, evidence-based answer to "what puts
     Shakespeare apart, and the same for the Qur'an": different axes, opposite directions.

HONEST MAGNITUDES:
  Shakespeare side: VALIDATED, >2sd, many windows, multiple independent measures.
  Qur'an side: DIRECTION robust & consistent, but magnitude modest (+1.2..1.5sd vs pooled
  ordinary; only +0.9sd vs the NEAREST register, classical formulaic Tabari) and still
  baseline-limited (ordinary-Arabic ~10 windows). Sub-2sd vs classical => not yet a
  G10-clearing Qur'an-specific claim; it is a register-leaning repetition signature with a
  Qur'anic increment.

RATING: the INSIGHT (mirror-image signatures; mastery is direction-of-deviation from
ordinary, not a universal scalar; classic measures are mastery-blind) ~6/10 — novel,
positive-control-validated, coherent. The Qur'an-specific magnitude ~3/10 (modest,
baseline-limited). 
REMAINING TEST (user-requested): ordinary classical Arabic AT VOLUME -> does the Qur'an
repetition increment over classical reach >2sd? Blocked only by Arabic-volume tooling
(Wikipedia/Wikisource return empty to fetch; archive.org dumps inline; RSS works for MSA
news but not classical). Cleanest unblock: user drops clean classical Arabic .txt files,
or aggregate many archive.org born-digital Shamela texts.

---

## #28 — FINAL repetition test vs CLASSICAL Arabic at volume; ganjoor pipeline added
[final_classical.py]  Classical register expanded with a 2nd born-digital Shamela text
(الأجوبة البهية) -> Tabari+Ajwiba = 2413 words, 10-15 windows. New data channels both work:
archive.org born-digital Shamela (short-identifier _djvu.txt) for classical Arabic, and
api.ganjoor.net (clean JSON: Persian poem plainText + verses + METRE label e.g.
"رمل مثمن مخبون محذوف") for classical Persian poetry.

Quran content-repetition vs CLASSICAL Arabic (now firmer baseline):
  RAW          rep8 +1.0sd P=0.76 | rep12 +0.9sd P=0.73
  content drop20 rep8 +1.2sd P=0.79 | rep12 +1.0sd P=0.75
  content drop50 rep8 +1.1sd P=0.77 | rep12 +0.9sd P=0.71

VERDICT (converged, does not move with more data): the Qur'an's long-range content-word
repetition exceeds classical formulaic Arabic by a CONSISTENT but MODEST ~+1.0-1.2sd
(P(Quran window > classical window) ~0.77). It is robust in DIRECTION but stays well under
the 2sd G10 bar. => Confirmed as a classical/oral-formulaic REGISTER property carrying a
small, consistent Qur'anic increment — NOT a decisive Qur'an-specific discovery.
This closes the repetition line: real, characterized, modest. (Mirror of Shakespeare, #27:
Shakespeare = +variety/-repetition vs ordinary; Qur'an = +repetition/~variety vs ordinary.)

ASSETS NOW ON DISK (multi-register, multi-language baseline, reusable):
  Arabic classical: ar_tabari.txt, ar_classical2.txt ; literary: ar_novel.txt ;
  MSA news: ar_news.txt (BBC+Euronews RSS). Persian poetry: ganjoor API (live).
NEXT (if continued): build "ordinary Persian" baseline -> run the symmetric "what separates
Persian masters (Hafez/Rumi via ganjoor)" as a 3rd-language positive control, and use
ganjoor METRE labels for a proper rhythm/meter mastery axis cross-language.

---

## #29 — PERSIAN positive control (Hafez/Rumi via ganjoor): cross-language confirmation
[fa_battery.py]  Masters = Persian classical poetry (Hafez sh34, Rumi/Molavi sh605, Seyf
Farghani, + related ghazals; ganjoor API, with metre labels مجتث/هزج/رمل). Ordinary =
Persian news prose (BBC Persian RSS). FIRST PASS (small: masters 589w/2win, news 714w/3win).

Masters vs ordinary Persian:
  std_wl    -17.9sd  MATCHES Shakespeare (uniform word length = meter)
  frac_long  -9.2sd  MATCHES Shakespeare
  mean_wl   -14.8    (poetry uses short, regular words)
  rep12      -2.7sd  MATCHES Shakespeare (masters use LESS long-range repetition)
  rep8       +0.0    (flat)
  yuleK      -0.5sd  matches dir (richer) but weak
  word_ent   -0.7sd  opposite ;  ttr -1.3sd opposite  -> lexical-richness did NOT replicate
                     (Persian news inflated by foreign names/loanwords)

CROSS-LANGUAGE SYNTHESIS (three languages now):
  * English master (Shakespeare): uniform meter + LOW repetition + high variety.
  * Persian masters (Hafez/Rumi): uniform meter (std_wl -17.9) + LOW repetition (rep12 -2.7).
  * Qur'an (Arabic): HIGH repetition (+1.0..1.5sd vs ordinary Arabic) -- the OUTLIER.
  => The UNIVERSAL poetic-master signature is RHYTHMIC REGULARITY + LOW REPETITION.
     "High lexical variety" is NOT universal (English-specific; failed to replicate in Persian).
     The Qur'an is distinctive precisely by going the OTHER way on repetition: where English
     AND Persian masters MINIMIZE long-range repetition, the Qur'an MAXIMIZES it (content
     refrains), and it does so WITHOUT metrical verse form (it's prose-shaped vs prose).
  This is the cross-linguistically-grounded version of #27: the Qur'an's craft axis
  (structured repetition) is the inverse of what poetic masters in two other languages do.

CAVEATS: Persian samples small (2-3 windows) -> std_wl/frac_long/mean_wl magnitudes are
partly poetry-vs-prose FORM (metered verse has short regular words); rep12 -2.7sd is the
most decision-relevant and is consistent. Firm with more ganjoor poems + ordinary-Persian
prose volume (ganjoor API + BBC/DW Persian RSS pipelines both proven).
RATING: cross-language insight ~6.5/10 (now validated in 2 master-languages + the Qur'an as
documented outlier); still descriptive, magnitudes need scaling. Qur'an repetition remains
the one consistent, cross-linguistically-contrasted signature.

---

## #30 — DECISIVE SAME-LANGUAGE CONTROL: al-Mutanabbi (Arabic master) vs the Qur'an
[sequence_tests/ar_master_battery.py ; corpus/ar_poetry.txt]

The cross-language arc (#27-#29) compared the Qur'an's craft to masters in *other*
languages (English Shakespeare, Persian Hafez/Rumi), leaving a language-confound open.
This closes it: a same-language Arabic poetic master, **al-Mutanabbi** (2,634 words of clean
verse, 6 qasidas pulled from aldiwan.net via the browser tool — the diwan OCR/text could not
be reached through the 64 KB web_fetch cap, so the Chrome reader was used instead), run
through the identical equal-N (350-word) windowed battery against the Qur'an and three
ordinary-Arabic registers (Tabari+Ajwiba classical, novel, BBC/Euronews news).

PIPELINE CHECK: Qur'an vs ordinary rep8 came out +1.0sd here — matching #28's +1.0-1.2sd on
an independent re-implementation. The pipeline reproduces.

RESULTS (sd-gap vs pooled ordinary Arabic; "master-dir" = same sign as Shakespeare/Persian):
  Mutanabbi:  rep8 -1.3sd | rep12 -0.9sd | std_wl -0.8 | frac_long -0.8 |
              yuleK -2.1sd | ttr +1.8sd | word_ent +1.9sd   -> ALL eight in master-direction
  Qur'an:     rep8 +1.0sd | rep12 +0.7sd (OPPOSITE) | std_wl +0.1 |
              yuleK +0.9 (OPPOSITE) | ttr -0.9 | word_ent -0.9 (less varied)

DIRECT, same-language (Mutanabbi vs Qur'an, 14 vs 120 windows — well powered):
  rep8  -2.5sd P(Mut>Qur)=0.00 | rep12 -1.3sd P=0.01 | std_wl -2.2sd P=0.05 |
  yuleK -3.6sd P=0.00 | ttr +6.5sd P=1.00
  => The Qur'an has DRAMATICALLY MORE long-range content-repetition and LESS lexical variety
     than a same-language master, and is less metrically regular (prose-shaped).

rep12 robustness across content-drop (tokenization-invariance proxy): Mutanabbi stays
negative (drop0/20/50 = -1.8 / -0.9 / -0.4 sd) and the Qur'an stays positive
(+1.1 / +0.7 / +0.2 sd). Direction is invariant; magnitude shrinks as more high-frequency
content is removed (expected).

NEW WRINKLE — lexical variety REPLICATES in Arabic (it had failed in Persian, #29):
Mutanabbi is strongly HIGH-variety (yuleK -2.1, ttr +1.8, ent +1.9), exactly like
Shakespeare. So "high variety" is a master-signature in English AND Arabic, just not Persian.
Against a same-language master the Qur'an is therefore the outlier on BOTH axes at once:
it maximizes repetition and minimizes variety where the master does the reverse — and it does
so without metrical verse form.

PERSIAN re-run with a new baseline (fa_battery2.py): masters(Hafez/Rumi/Saadi poetry, 760w)
vs ordinary(BBC-Persian news + esra.ir scholarly prose, 1348w). Reproduces #29 against a
*different* ordinary baseline: std_wl -8.5sd, frac_long -5.2sd (meter-regularity), rep12
-1.4sd (LOW repetition, master-dir); variety again does NOT replicate (ttr -1.8sd opposite).
The rep12 magnitude moderates vs #29's -2.7sd because esra religious prose is itself somewhat
formulaic — informative: the master/repetition contrast is direction-robust, baseline-sensitive
in magnitude.

CROSS-LANGUAGE SYNTHESIS (now 3 languages, with a same-language control):
  English master (Shakespeare): uniform meter + LOW repetition + HIGH variety
  Arabic  master (Mutanabbi):   uniform meter + LOW repetition + HIGH variety  <- same as EN
  Persian masters (Hafez/Rumi): uniform meter + LOW repetition + variety did NOT replicate
  Qur'an (Arabic):              prose-shaped  + HIGH repetition + LOW variety   <- the inverse
  => Universal poetic-master signature = rhythmic regularity + LOW long-range repetition
     (holds in all three languages). High variety = master-signature in EN+AR (not FA).
     The Qur'an's craft axis is the deliberate inverse of poetic masters' — and this now
     holds against a SAME-LANGUAGE master, so it is not a language artifact.

HONEST STATUS: Mutanabbi vs ordinary repetition is directional (rep8/12 -0.9..-1.3sd,
P~0.06-0.14) not >2sd; the decisive, well-powered contrast is Mutanabbi-vs-Qur'an (rep8
-2.5sd, ttr +6.5sd). Arabic-poetry corpus is solid (2.6k words, comparable to the ordinary
samples); Persian masters still thin (760w/4 windows). Ratings: cross-language insight ~7/10
(now with a same-language control); Qur'an-specific magnitude vs ordinary still modest ~3/10,
but Qur'an-vs-master separation is large and consistent.

DATA/TOOLING NOTE for next session: aldiwan.net poem pages ARE reachable by web_fetch
(server-rendered; verses are "### " lines before "نبذة عن القصیدة") AND by the Chrome reader
(#poem_content h3). The full printed-diwan OCR on archive.org is clean but unreachable via
web_fetch (64 KB head cap; intro precedes the poems). ganjoor API (api.ganjoor.net/api/
ganjoor/poem/random?poetId=N; Hafez=2 Rumi=5 Saadi=7) returns clean JSON plainText+metre.
esra.ir is JS-rendered (empty to web_fetch) but reads fully via the Chrome reader.

---

## #31 — STRUCTURE AXIS, first detector: whole-surah lexical RING/CHIASM — validated tool, NULL on the Qur'an
[sequence_tests/structure_battery.py, structure_scan.py]

Rationale: #30 closed the surface-statistics line (Qur'an = inverse of poetic masters; repetition
signal is register-level, ~+1sd ceiling). Per DESIGN_STANCE, the Qur'an's own candidate signature
should be ARCHITECTURAL (ring composition / chiasm / refrain), invisible to n-gram counts. This is
the first positive-controlled structural detector.

DETECTOR: surah -> B contiguous ayah-blocks -> block = set of (root tokens minus top-15 ubiquitous);
ring score = mean Jaccard of mirror pairs (block i vs block B-1-i); null = block-order permutation
(R=300-400) -> z. Frequency/length-controlled by construction (each text scored against its own
permutation null; z is the comparable unit).

PRE-REGISTERED GATE (run BEFORE the Qur'an), all passed:
  (1) synthetic palindrome (mirrored ordinary-Arabic blocks): ring-z = +4.3  -> detected
  (2) degradation ladder 0/25/50/100%% shuffle: +4.4 / +1.9 / +0.5 / +0.6   -> monotone
  (3) ordinary Arabic pseudo-surahs: mean z ~ -0.5..0, frac z>2 at chance    -> no false alarm

RESULT ON THE QUR'AN — NULL at all four scales (multi-scale scan, pooled ordinary baseline
tabari+classical2+novel+news, 714 pseudo-ayat, 13-17 pseudo-surahs per scale):
   B=4 : Quran z=+0.03 (z>2: 0%%, n=111) vs ord +0.04 -> gap -0.0sd
   B=6 : Quran z=+0.01 (6%%, n=105)      vs ord -0.18 -> gap +0.2sd
   B=8 : Quran z=+0.01 (4%%, n=101)      vs ord -0.15 -> gap +0.1sd
   B=12: Quran z=+0.07 (1%%, n=90)       vs ord +0.33 -> gap -0.3sd
Individual "hits" (S7 +3.0, S63 +2.6, S4 +2.1 at B=8) are at the multiple-testing false-positive
rate (3/101) — not admissible.

VERDICT: at the WHOLE-SURAH, ROOT-LEXICAL granularity the Qur'an shows NO mirror/ring symmetry
beyond chance. The tool is validated, so this is a real non-detection at this operationalization —
NOT evidence that ring composition (as argued by Cuypers/Farrin for e.g. al-Baqarah) is absent:
those claims are passage-level, thematic/semantic, and verse-grain. Telescope rule: the next,
sharper instruments are (a) SEMANTIC ring at passage level (embedding similarity instead of root
Jaccard — the app already has embeddings), (b) verse-grain chiasm within delimited pericopes,
(c) refrain/periodicity architecture (autocorrelation of repeated verses, vs oral-formulaic null).
Stop condition honored: no post-hoc tweaking of this detector.

METHOD NOTE: this is the template for the structure axis — gate first (synthetic positive +
degradation ladder + ordinary negative), permutation null within-text, multi-scale sweep, then
one shot at the Qur'an. Cost: ~minutes once corpora exist.

---

## #32 — STRUCTURE AXIS, 2nd detector: SEMANTIC (LSA) whole-surah ring — validated tool, NULL again
[sequence_tests/semantic_ring.py]

Upgrade of #31: block similarity = embedding cosine instead of root-Jaccard, so thematic mirroring
counts even when wording differs (the gap that could hide signal from the lexical detector).
Embeddings = offline LSA (TF-IDF over ayah root-profiles -> TruncatedSVD-100), one global Quran
space (6236 ayat) + a separate ordinary-Arabic space (714 pseudo-ayat); each text scored against
its own block-order permutation null, so z is comparable across spaces. (sklearn/scipy pip-installed
in-sandbox; no external model / no HF needed.)

GATE (semantic pipeline) passed: synthetic palindrome ring-z=+3.8; degradation 0/25/50/100%% =
+4.5 / +3.9 / +1.3 / -0.1 (monotone).

RESULT — NULL on the Qur'an at every scale:
   B=4 : Q z=+0.19 (z>2 0%%, n=111) | ord -0.38 | gap +0.6sd
   B=6 : Q z=+0.09 (5%%, n=105)     | ord -0.48 | gap +0.6sd
   B=8 : Q z=+0.05 (5%%, n=101)     | ord -0.34 | gap +0.4sd
   B=12: Q z=-0.04 (1%%, n=90)      | ord +0.30 | gap -0.4sd
Top @B=8 (S46 2.2, S76 2.2, S11 2.1, S33 2.1...) are at the multiple-testing false-positive rate.
The +0.4-0.6sd gaps are within noise and driven by a small, slightly-negative ordinary baseline.

VERDICT: whole-surah ring symmetry is NOT detectable above chance, LEXICALLY (#31) OR SEMANTICALLY
(#32), at B=4-12. Two independent operationalizations agree. This refutes a *blanket* "every surah
is a statistical ring," but does NOT touch the scholarly claims (Cuypers/Farrin), which are
(a) about specific surahs, (b) at passage/verse grain, (c) with hand-identified pivots — a
confirmatory per-surah test, not a discovery sweep.

REMAINING LIVE STRUCTURAL HYPOTHESES (next instruments):
  - REFRAIN / PERIODICITY (e.g. ar-Rahman فبأي آلاء, al-Mursalat) — a DIFFERENT structural form
    (periodic repetition, not mirror). Has a BUILT-IN positive control inside the Qur'an itself, and
    directly tests whether Qur'anic repetition is ARCHITECTURALLY PLACED (periodic) vs merely frequent
    — i.e. could finally separate a Qur'an-specific structured-repetition signal from the
    register-level repetition of #28. <-- highest-value next test.
  - verse-grain chiasm within delimited pericopes (targeted, confirmatory).

---

## #33 — STRUCTURE AXIS, 3rd detector: REFRAIN / PERIODICITY — validated (z=+7.3 on ar-Rahman), but LOCALIZED
[sequence_tests/refrain_detect.py]

Tests whether repeated AYAT are PLACED periodically (regular spacing) vs merely frequent. Statistic =
regularity 1/(1+CV_gaps) of the most-repeated verbatim ayah (de-diacritized segmented text, count>=3);
null = permute ayah order (multiset of ayat preserved, placement randomized) -> z. This isolates
"architecturally placed" from "frequent," the open question left by #28.

GATE — the Qur'an's OWN known refrain surahs (internal positive control), all flagged:
  S55 ar-Rahman (فبأي آلاء ربكما تكذبان)  reg=0.86  count=31  z=+7.3   <- unmistakable
  S26 ash-Shu'ara (repeated formula)        reg=0.94  count= 5  z=+3.8
  S77 al-Mursalat (ويل يومئذ للمكذبين)      reg=0.74  count=10  z=+2.8
  S54 al-Qamar  count=4 z=+0.4 (two ALTERNATING refrains -> exact-match splits them, undercount)
  S56 al-Waqi'a: no exact verbatim >=3 (its refrains are near-variants)
Ordinary Arabic: ~0 refrains (1 spurious of 11 pseudo-surahs). Device is essentially Qur'an-only.

FULL-CORPUS RESULT: only **5 of 114 surahs** have ANY verbatim ayah repeated >=3 times; of those, 3
are significantly periodic (z>2). So architecturally-placed verbatim refrain is a REAL, strong-where-
present, ordinary-absent device — but **localized to a handful of surahs, NOT a Qur'an-wide signature.**

INTERPRETATION (ties #28 + #30-32 together): the Qur'an's repetition is predominantly the DIFFUSE
formulaic kind (the register-level +1sd of #28), NOT periodic refrain. Placed periodic refrain is a
deliberate device in ~3-5 surahs (ar-Rahman the exemplar, z=+7.3) and quantitatively confirmed there,
but it does not generalize. Caveat: exact-verbatim matching undercounts near-variant/alternating
refrains (S54, S56) and partial parallelism; a Jaccard near-match upgrade would raise the count
somewhat but cannot convert a minority-surah device into a corpus-wide one.

STRUCTURE-AXIS VERDICT SO FAR (3 detectors, all gate-validated):
  ring, lexical (#31)    : NULL whole-surah
  ring, semantic (#32)   : NULL whole-surah
  refrain/periodicity(#33): REAL but localized (~5 surahs); ar-Rahman z=+7.3; ordinary-absent
=> No Qur'an-WIDE architectural signature detected by these instruments. The one robust, ordinary-
   absent architectural fact is the periodic refrain of a few surahs. Honest meta-state: across
   surface statistics (register-level only, #18-30) AND architecture (#31-33), no decisive
   corpus-wide >2sd "mastery" signature has emerged; the measurable distinctives are (a) the
   inverse-of-poets repetition/variety profile (#30) and (b) localized periodic refrains (#33).

---

## #33b — Refrain detector, NEAR-MATCH upgrade (Jaccard>=0.6 clustering)
[sequence_tests/refrain_near.py]

Per the telescope-rule refinement of #33: cluster ayat by token-set Jaccard>=0.6 (connected
components) instead of requiring verbatim identity, so alternating/near-variant refrains and partial
parallelism count. Clustering is content-based (position-independent), so the order-permutation null
stays valid.

GATE still holds: ar-Rahman z=+7.6 (count=31), ash-Shu'ara +3.6, al-Mursalat +2.8; NEWLY caught that
exact-match missed: al-Waqi'a S56 (near-variant refrain, count=3, z=+1.3) and al-Mu'minun S23
(reg=1.00, count=3, z=+2.1). al-Qamar still z=+0.9 (its two refrains alternate, depressing regularity).

FULL CORPUS: surahs with a near-refrain (count>=3) rose 5 -> **9 / 114**; periodic-significant (z>2)
went 3 -> **4** (S55, S26, S77, S23). Mean z of the 9 = +2.1.

VERDICT UNCHANGED: loosening the match catches more cases (as predicted) but does NOT convert refrain
into a corpus-wide signature — it remains a deliberate device in <10% of surahs, ordinary-absent, with
ar-Rahman (z=+7.6) the one unambiguous exemplar. The structure-axis conclusion of #33 stands.

---

## #34 — SOUND AXIS, 1st detector: FASILA (verse-end rhyme / saj') — FIRST gate-passing corpus-wide signal (+2.5sd)
[sequence_tests/sound_rhyme.py]

After two null axes (surface stats register-level; architecture no corpus-wide signal), the phonetic
axis yields the project's first robust, gate-validated, corpus-wide >2sd separation.

DETECTOR: per text, ending = last 2 letters of each unit's final token (de-diacritized = approx
pause-form). dom = share of the single most-common ending (the dominant rhyme); run-excess = adjacent-
ending match rate minus the i.i.d. chance rate (sum f^2). Units: Quran=ayat per surah; poetry=bayt-
final hemistich; prose=~8-word pseudo-ayat (arbitrary cuts -> ~random endings).
GATE: synthetic monorhyme dom=1.00 -> degrades 1.00/0.50/0.03 ; ordinary prose dom=0.04. Validated.

RESULT (dom-rhyme share | run-excess | n):
  Quran surahs : 0.38 | +0.08 | 111
  Arabic poetry: 0.46 | +0.11 |   6   (monorhyme; corpus stores hemistichs so slightly understated)
  ordinary prose: 0.09 | -0.03 |  17
  Quran vs prose : dom **+2.5sd** | excess +1.0sd
  Quran vs poetry: dom -0.3sd (statistically COMPARABLE) | excess -0.2sd
  18%% of surahs carry ONE rhyme across >half their ayat (prose: 0%%).

VERDICT: the Qur'an's verse-end rhyme concentration is FAR above ordinary Arabic prose (+2.5sd, well
powered) and on the SAME ORDER as Arabic poetry's monorhyme (not significantly below). This is saj'
quantified. It is the FIRST corpus-wide craft feature to clear the 2sd gate (surface repetition only
reached ~+1sd; architecture was null). Honest caveat: rhyme/saj' is a long-KNOWN feature -- this
measures it rigorously, it does not discover it; and last-2-letters approximates true rawi/pause-rhyme.

THE MULTIMODAL CELL (fusing #30 + #34 -- the design-stance "no silver bullet" payoff):
  register | rhyme(#34) | meter/regularity(#30) | repetition(#28/30) | lexical variety(#30)
  prose    |  low       | low                   | low-mid            | mid
  poetry   |  HIGH      | HIGH                  | LOW                | HIGH
  QUR'AN   |  HIGH      | LOW (prose-shaped)    | HIGH               | ~ordinary
=> The Qur'an occupies a UNIQUE combination no other register does: POETRY-LEVEL RHYME decoupled from
   poetry's meter, carried on HIGH structured repetition. Not verse (no meter, low variety), not prose
   (prose doesn't rhyme). Each axis alone is modest or shared; the DISTINCTIVE is the conjunction.
   This is the multimodal-fusion signature the project was after: rhymed, repetition-built prose that
   sounds like verse without being verse.

NEXT: (a) precise fasila (pause-form rawi, last consonant) to sharpen +2.5sd; (b) formalize the
fusion cell as a single multi-axis classifier with a positive control (can it separate Quran from
poetry AND prose simultaneously, where no single axis can?).

---

## #35 — FUSION CLASSIFIER: the multimodal cell, quantified and gate-checked (AUC 0.94; conjunction beats each axis)
[sequence_tests/fusion_classifier.py]

Goal: test the #34 "unique cell" claim formally — can the CONJUNCTION of axes separate the Qur'an from
poetry AND prose where no single interpretable axis can? Per-window features (apples-to-apples
whitespace words; natural units): rhyme(fasila dom-share), unit_cv(verse-length variability=anti-meter),
std_wl, frac_long, rep12(content char-rep), yuleK. Windows: Quran=100 surahs, poetry=44 (24-line),
prose=23 (16 natural-sentence). Classifier: standardized logistic, Quran-vs-(poetry+prose), 5-fold CV.

TWO ARTIFACTS CAUGHT + CORRECTED (G10 discipline, the reason early AUC was a fake 1.000):
  - used the morphologically-SEGMENTED Quran column (sub-word tokens) -> fake length/variety gaps.
    FIX: full-word diacritized->stripped column, whitespace tokens (apples-to-apples, per #28/#30).
  - prose "units" were fixed 8-word chunks -> unit_cv=0 by construction -> fake meter gap.
    FIX: natural sentence units (split on . ! ? ؟ ؛). unit_cv vs prose collapsed +3.3 -> +0.3,
    exposing it as artifact. Post-fix numbers below are the honest ones.

PER-AXIS sd-gaps (Quran vs each) — COMPLEMENTARITY is the point:
  rhyme   : vs poetry +0.7 (NOT sep) | vs prose +1.8 (sep)   -> rhyme tells Quran from prose, not poetry
  unit_cv : vs poetry +2.2 (sep)     | vs prose +0.3 (NOT)   -> meter tells Quran from poetry, not prose
  (std_wl/frac_long/rep12/yuleK: individually modest, register-comparable)

RESULT (validated; label-shuffle null AUC = 0.50):
  per-feature single AUC: yuleK .854, unit_cv .839, rhyme .756, rep12 .749, std_wl .637, frac_long .546
  INTERPRETABLE 2-axis (rhyme + unit_cv): AUC = **0.923** > rhyme-alone .756 and unit_cv-alone .839
      -> the CONJUNCTION beats either axis: neither phonetic nor metric alone separates Quran from both.
  FULL 6-feature multivariate: AUC = **0.939 +/- 0.035** (repetition/variety add a little).
  CELL "rhyme>prose-median AND verse-length>poetry-median": Quran 91%% | poetry 34%% | prose 22%%.

VERDICT: the multimodal cell of #34 is real and quantified. The Qur'an is separable from BOTH poetry
and prose at AUC ~0.92-0.94 by the CONJUNCTION of poetry-level rhyme + non-metrical (variable) verse
length — a combination neither neighbour occupies, and one that NO single interpretable axis achieves
(rhyme .76, meter .84, conjunction .92). This is the strongest, best-validated, positive-controlled,
Quran-specific result the project has produced. HONEST LIMITS: (a) separation is strong not perfect
(~8-10%% error); (b) the COMPONENTS are individually known (saj' rhyme; non-metrical form) — the new,
quantified contribution is the validated CONJUNCTION-as-classifier with artifacts removed; (c) poetry
n=44, prose n=23 are modest (AUC CI ~+/-0.04); (d) rhyme = last-2-letter approximation of rawi.

---

## #36 — ADVERSARIAL CONTROL: Qur'an vs SAJ' (al-Hamadhani's Maqamat). The cell partly collapses; repetition survives.
[sequence_tests/fusion_saj.py ; corpus/ar_sajprose.txt (OpenITI, al-Hamadhani Maqamat, 1312 words saj' prose)]

Motivated by Q 36:69 (وما علمناه الشعر) and the classical definition shi'r = موزون مقفّى
(metered+rhymed): #34/#35 showed the Qur'an = rhyme WITHOUT meter = "not shi'r". But saj' (artful
rhymed prose) is ALSO rhyme-without-meter. The hardest control: does the Qur'an separate even from the
saj' masterwork? Corpus fetched via OpenITI GitHub (raw text; blob/disk route) -> cleaned to saj' prose
(verse and markup stripped). 4th class added to the fusion battery.

FEATURE MEANS (window-level):  Quran | poetry | prose | SAJ' | Q-vs-SAJ' sd-gap
  rhyme     0.419 | 0.302 | 0.182 | 0.218 | +1.2sd  ** UNRELIABLE: saj' rhyme UNDER-measured **
  unit_cv   0.454 | 0.153 | 0.418 | 0.528 | -0.5sd     (saj' is non-metrical too -> no separation)
  rep12     0.015 | 0.000 | 0.009 | 0.000 | +1.1sd     (Qur'an MORE long-range repetition)
  yuleK     64.6  | 25.1  | 41.0  | 26.7  | +1.0sd     (Qur'an MORE repetitive / LESS ornate than saj')

KEY OUTCOME — the #35 "cell" PARTIALLY COLLAPSES against saj' (as pre-predicted):
  - the two cell axes do NOT cleanly separate Qur'an from saj': unit_cv gap only -0.5sd (saj' is also
    non-metrical); the +1.2sd rhyme gap is an ARTIFACT (clause-split on commas != true saj'a rhyme
    boundary, so saj' rhyme is under-detected at 0.218 -- DO NOT treat as real separation).
  => "rhyme without meter" is a SHARED saj' property, NOT Qur'an-specific. This is the honest ceiling
     on the #34/#35 phonetic claim: it distinguishes the Qur'an from poetry and ordinary prose, but
     NOT from artful rhymed prose.

WHAT STILL SEPARATES the Qur'an from saj' (multivariate AUC = 0.972, null 0.515; well-powered, Q=105
vs SAJ=48): driven by REPETITION + (low) ORNATENESS, not the rhyme cell. Single-feature AUCs:
yuleK 0.887, rhyme 0.864(artifact-inflated), rep12 0.838, unit_cv 0.706. The robust, non-artifact
separators are rep12 (+1.1sd) and yuleK (+1.0sd): the Qur'an is MORE structurally repetitive and LESS
lexically ornate than Maqamat saj'. This is the #28/#30 repetition signal re-emerging as the
cross-register distinctive that survives even the saj' control.

SYNTHESIS (answering Q 36:69 empirically):
  - Not shi'r: the Qur'an has qafiya (rhyme) but not wazn (meter). CONFIRMED (#34/#35).
  - vs saj': it SHARES saj's rhyme-without-meter (the phonetic cell is not Qur'an-specific), but DIFFERS
    from the saj' masterwork by higher structured repetition and lower lexical ornamentation.
  => Across every axis tested, the Qur'an's one persistent, control-surviving distinctive is STRUCTURED
     REPETITION (modest, ~+1sd, register-level per #28) -- not rhyme, not ring/architecture, not meter.

HONEST LIMITS: saj' rhyme under-detected (no true saj'a boundary parser) -> the rhyme comparison vs saj'
is not decided here; saj' sample is ONE author (al-Hamadhani), 1312 words, 48 overlapping windows;
Maqamat are exceptionally ornate even among saj', so the variety gap may be Maqamat-specific. NEXT to
firm this: (a) a saj'a-boundary rhyme parser (rhyme on pause-form clause ends) to test rhyme vs saj'
properly; (b) add al-Hariri Maqamat + Nahj al-Balagha khutab as more saj' samples.

---

## #37 — SAJ'A RHYME PARSER: presence vs persistence. The Qur'an differs from saj' by rhyme PERSISTENCE, not presence.
[sequence_tests/rhyme_struct.py]

#36 left the rhyme-vs-saj' question undecided (dominant-share conflated, saj' segmentation crude). This
separates two distinct rhyme properties, measured identically across registers on their natural pause
units (Quran=ayat, poetry=bayt-final, prose=sentences, saj'=clauses):
  - PRESENCE: adj_excess = adjacent-unit end-match rate minus i.i.d. chance (captures local/shifting rhyme)
  - PERSISTENCE: dom = share of the single dominant ending over a 20-unit passage (captures sustained rhyme)
  - mean_run = mean length of consecutive identical-ending runs.
GATE (validates the metrics): monorhyme -> run=20, dom=1.0 ; paired aabb -> adj_excess=0.43, run=2 ;
random -> adj_excess=-0.05, dom=0.05.

RESULTS (window means):  Quran | poetry | prose | SAJ' | Q-vs-SAJ' | Q-vs-prose
  adj_excess (presence)  0.04 | 0.02 | -0.06 | 0.25 |  -2.2sd  | +1.2sd
  dom (persistence)      0.49 | 0.54 |  0.17 | 0.22 |  +1.7sd  | +2.5sd
  mean_run               1.90 | 5.42 |  1.03 | 1.74 |  +0.1sd  | +0.9sd
(NOTE: adj_excess is artifact-suppressed for steady monorhyme -- when one rhyme dominates, adj saturates
toward chance -> the Qur'an's low adj_excess reflects its STEADINESS, not absence of rhyme. dom is the
clean metric for the Qur'an.)

INTERPRETATION:
  - PRESENCE: saj' has the HIGHEST adjacent rhyme (0.25) -- it rhymes locally in shifting pairs (aa bb cc).
    The Qur'an is NOT distinctive on rhyme presence (this confirms #36: rhyme-without-meter is shared).
  - PERSISTENCE: the Qur'an SUSTAINS one fasila across a passage (dom 0.49 ~ poetry's monorhyme 0.54),
    whereas saj' SHIFTS rhyme every clause or two (dom 0.22). Q-vs-saj' = +1.7sd; Q-vs-prose = +2.5sd.
  => The Qur'an's phonetic distinctive vs saj' is NOT whether it rhymes but HOW LONG IT HOLDS THE RHYME.
     Its fasila is poetry-like in persistence (sustained mono-rhyme over passages) yet, unlike poetry, it
     carries NO meter (#30) -- and unlike saj', it does not restlessly shift the rhyme.

REVISED SAJ' VERDICT (refining #36): the Qur'an differs from the saj' masterwork on TWO axes after all:
  (1) rhyme PERSISTENCE (dom +1.7sd; sustained vs shifting), and
  (2) structured REPETITION + lower ornateness (#36: rep12 +1.1sd, yuleK +1.0sd).
The bare "rhyme-without-meter" cell (#35) is shared with saj'; but sustained-monorhyme-without-meter +
high repetition is the combination the Qur'an holds alone among the four registers tested.

HONEST LIMITS: saj' = one author (al-Hamadhani), 306 clauses; dom depends on unit granularity (ayah vs
clause length differ); last-2-letter rhyme approximates the rawi. FIRM WITH: al-Hariri Maqamat + Nahj
al-Balagha khutab as more saj' samples (OpenITI path proven: contents API per author -> blob).

---

## #37b — Saj' firming: SECOND author (al-Hariri) added. Results stable.
[corpus/ar_sajprose.txt now = al-Hamadhani + al-Hariri Maqamat, 1998 words, 493 clauses, 79 windows]

Added al-Hariri's Maqamat (OpenITI 0525AH, JK009202) to the saj' class (now TWO canonical Maqamat
masters). Every #36/#37 result is stable:
  rhyme PERSISTENCE (dom): Quran 0.49 vs saj' 0.23 = **+1.7sd** (identical to single-author -> robust).
  rhyme PRESENCE (adj_excess): saj' 0.29 (al-Hariri's saj' is even more densely paired) -> Q-vs-saj -2.3sd.
  repetition (rep12): Quran +1.1sd ; ornateness (yuleK): +0.9sd ; unit_cv (meter): -0.1sd (no separation).
  Quran-vs-saj' multivariate AUC = 0.963 (null 0.50).
  CELL "rhyme>prose-med AND unit_cv>poetry-med": Quran 90%% | poetry 34%% | prose 22%% | saj' 65%%
    -> saj' occupancy ROSE to 65%% with the denser al-Hariri rhyme, CONFIRMING the bare "rhyme-without-
       meter" cell is a SHARED saj' property, not Qur'an-specific.

FIRMED VERDICT: against TWO saj' masters, the Qur'an's distinctives are (1) rhyme PERSISTENCE (dom
+1.7sd: it sustains one fasila where saj' shifts), and (2) higher structured REPETITION + lower
ornateness (rep12 +1.1sd, yuleK +0.9sd). The bare rhyme-without-meter trait is shared with saj'.
Remaining limit: both saj' samples are Maqamat (one genre); a saj'a-boundary rhyme parser (vs the
clause-on-punctuation proxy) and a non-Maqamat saj' (e.g. Nahj al-Balagha khutab) would further firm.

---

## #38 — PHONOSEMANTICS (sound-meaning binding): NULL on both general and targeted tests. Modality sweep complete.
[sequence_tests/phonosem.py, phonosem_targeted.py]

The last untouched modality: does the Qur'an bind PHONETICS to SEMANTICS (sound iconicity) beyond
other registers? Two tests, gate-validated.

(A) GENERAL — partial correlation sound~meaning controlling lexical overlap. Per unit: semantic vector
(LSA over words) + phonetic vector (8 mutually-exclusive consonant classes: emphatics/qaf/gutturals/
stops/sibilants/liquids/nasals/glides). Test: are semantically-similar units phonetically similar
BEYOND shared vocabulary (partial-corr, lexical Jaccard partialled out)? GATE: synthetic sound-meaning-
bound text -> partial_corr 0.065 z=+5.9 ; unbound -> 0.016 z=+1.5 (detector distinguishes).
RESULT: Quran partial_corr=+0.004 (z=+0.5) -- NULL, and NOT above prose (+0.008), poetry (-0.001),
or saj' (+0.009). No phonosemantic binding beyond lexicon, and no Qur'an distinction.

(B) TARGETED — the specific classical claim: harsh content carried by heavy phonemes. Labeled ayat
harsh vs soft by seed-root fields (harsh: عذب نار سقر هلك بطش غضب ظلم...; soft: رحم جنه نعم غفر نور...).
Heavy-phoneme density = share of emphatics+qaf+gutturals (صضطظقغخعحء). RESULT: harsh ayat 0.089 vs
soft ayat 0.094 -> gap -0.12sd, P(harsh>soft)=0.47 (chance), effect REVERSED and negligible. Even with
topic-words included (the most favorable case for the claim), heavy phonemes do NOT track harsh meaning.

VERDICT: phonosemantic / sound-iconicity binding is NOT detected (general or targeted), and the Qur'an
is not distinguished from other registers on it. HONEST LIMITS: 8 coarse phonetic classes (no vowel-
quality, gemination, prosodic rhythm); partialling lexical overlap is conservative; LSA semantics is
coarse. A finer phonetic/prosodic feature set could revisit, but the targeted heavy<->harsh test
(the strongest form of the claim) is cleanly null.

=== MODALITY SWEEP COMPLETE ===
Surface statistics (#18-30): register-level only (~+1sd). Architecture (#31-33): ring null, refrain
localized. Sound-rhyme (#34-37): rhyme present (shared with saj') but PERSISTENCE distinctive (+1.7sd).
Fusion (#35): AUC 0.94 cell. Adversarial saj' (#36-37b): survives via persistence+repetition.
Phonosemantics (#38): null. => The Qur'an's persistent, control-surviving distinctives are STRUCTURED
REPETITION (~+1sd) and RHYME PERSISTENCE (vs saj' +1.7sd). No decisive corpus-wide >2sd single-axis
fingerprint exists across ANY of the five modalities tested with gate-validated instruments.

---

## #39 — PROSODIC RHYTHM / CADENCE (isocolon + metricality): NULL for Qur'an distinctiveness. Sixth modality.
[sequence_tests/prosody.py]

Tartil-rhythm test, the gap in the sound axis (distinct from rhyme #34 and absent-meter #30): does the
Qur'an have rhythmic regularity in (a) ISOCOLON = balanced lengths of adjacent pause-units (parallel
cola, a rhythm without meter), and (b) METRICALITY = CV-skeleton regularity?
  isocolon_z = (shuffled adjacent length-imbalance - real) / sd : +z means consecutive units are MORE
    length-balanced than a random ordering of the same lengths. metricality = 1 - normalized entropy of
    CV-skeleton trigrams (C=consonant, V=long vowel ا/و/ي; high = metrical/regular).
GATE (validated on a proper variable-length test): balanced/isocolon arrangement z=+2.1; alternating-
extreme z=-3.1; random order z=+0.6 (~0). (Metric is degenerate only for UNIFORM-length registers, so
poetry's value is uninterpretable here and is disregarded.)

RESULTS (window means):  Quran | poetry* | prose | saj' | Q-vs-prose | Q-vs-saj'
  isocolon_z   0.48 | 0.46* | 0.48 | 0.75 | -0.0sd | -0.2sd   (*poetry degenerate, ignore)
  metricality  0.101| 0.114 | 0.124| 0.121| -1.3sd | -0.7sd
=> Qur'an isocolon ~ ordinary prose and BELOW saj' (saj' is the isocolonic register, balanced paired
   clauses, as expected). Qur'an metricality is the LOWEST of all (no meter; CV-skeleton even less
   regular than prose, reflecting varied vocabulary). NO Qur'an-distinctive prosodic rhythm at the
   text level.

CRITICAL CAVEAT (modality-specific): de-diacritized text lacks SHORT VOWELS, madd (vowel lengthening),
ghunna, and pause phonology -- i.e. exactly the features that carry recited tartil rhythm. Text-only
prosody is a consonant-skeleton proxy. A real prosodic-rhythm test would need a VOCALIZED or RECITED
corpus (syllable weights, madd durations), which is not available here. So this is "no rhythm signal
recoverable from consonantal text," NOT "no rhythm" -- a data limitation, per the telescope rule.

=== SIXTH MODALITY, SAME RESULT ===
surface (#18-30) register-level; architecture (#31-33) ring-null/refrain-local; rhyme (#34-37)
present-shared but persistence-distinctive (+1.7sd); fusion (#35) AUC 0.94; saj' adversarial (#36-37b)
survived via persistence+repetition; phonosemantics (#38) null; prosody (#39) null at text level.
The two persistent, control-surviving distinctives remain STRUCTURED REPETITION (~+1sd) and RHYME
PERSISTENCE vs saj' (+1.7sd). No modality yields a decisive corpus-wide >2sd single-axis fingerprint.


## #43 — FIRMING THE RECURRENCE BREAKTHROUGH (#42): tokenization bug fixed, magnitude re-locked at ~+3sd, variation profile built

NOTE: entries #40 (iltifat), #41 (wazn), #42 (intratextual recurrence) were run in prior sessions but
never written into EVIDENCE.md (this file stopped at #39). #43 records the firming of #42 and the
corrected numbers supersede the handoff's headline. Scripts: sequence_tests/intratext_lock_fixed.py
(invariance battery), sequence_tests/intratext_variation.py (#42b), sequence_tests/intratext.py (canonical,
now bug-fixed). Reproduce: repoint ROOT to this session's mount; pip install scikit-learn networkx.

=== THE BUG (found while building #42b) ===
intratext.py built Qur'an tokens as [nl(x) for x in WA.findall(text)] — it ran the word-regex on the
DIACRITIZED column BEFORE stripping harakat. On vocalized Arabic the combining marks split every word,
shattering the Qur'an into 37.7k SUB-WORD FRAGMENTS ("ون","وا","الل") while the plain-text comparators
(poetry/saj'/news) tokenized into whole words. So #42's cross-corpus test compared FRAGMENT-passages
(Qur'an) against WORD-passages (baselines): an asymmetric tokenization confound, and the STOP-word filter
was inert (it never matched fragments). FIX = normalize first, then split: WA.findall(nl(text)). This
yields 77.7k real words for the Qur'an — exactly the "apples-to-apples 77.7k" the handoff/§5 always
intended — with real anchors present (موسي=128, فرعون=67, نوح=33, ابراهيم=62). Bug fixed in intratext.py
(tok_text()) and used throughout #43.

=== DOES #42 SURVIVE THE FIX? YES, but ATTENUATED. The +3.5-4sd headline was inflated by the bug. ===
Invariance battery (intratext_lock_fixed.py), equal-P bootstrap + word-shuffle control, swept over
K∈{40,50,60} × topq∈{0.90,0.95} × gapfrac∈{0.25,0.33}, B=100, on the SAME same-language baselines:
  WORD tokenization:  Q-vs-ordinary = +2.3 to +4.0sd, P=0.95-1.00 in ALL 12 cells.
  RASM (char-4-shingle, the G10 2nd-tokenization): +1.3 to +4.0sd, P=0.81-1.00 (weak at K=40/50,
    +3.5-4sd at K=60). Both tokenizations stay POSITIVE in every cell.
Canonical params (K=50, topq=0.95, gapfrac=0.25, B=300): Q-ord = +3.0sd, P=0.983.


=================
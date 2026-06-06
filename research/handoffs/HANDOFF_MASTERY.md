# HANDOFF — Cross-Language "Mastery Signature" Investigation

================================================================================
## ★ NEXT SESSION — START HERE ★   (state as of #66 / 17 lenses + connectome layer; coverage ~72%)
================================================================================

READ FIRST (continuity anchors): FINDINGS_SYNTHESIS.md (the digest — every verdict classified) · this handoff
· EVIDENCE.md (raw #18–#66) · DESIGN_STANCE.md (LOCKED controls) · SIX_LENSES_PAPER.md (17-lens narrative) ·
DESIGN_OF_EXPERIMENTS.md · CROSS_IMPACT.md. Lectures: C:\Users\torki\Downloads\RootCourse\10-Minute Nuance\ (10 written + index).

POSITIVES (cross-text, gated): #42 varied long-range recurrence (~+3σ, shared-in-kind w/ poetry) · rhyme
  persistence (+1.7σ vs saj') · FĀṢILA SYSTEM (#62/#63, Lens 17: heavy ending-repetition >saj' + content-fit z+12)
  · fusion cell (#35, AUC 0.94) · MUQAṬṬAʿĀT position + half-alphabet (#50/#51, sui generis, DIVINELY-ROOTED).
DOWN-WEIGHTED by comparators (nothing is final): muqaṭṭaʿāt content-cohesion (#59 = general grouping) ·
  canonical-order coherence (#57/E1/E4 = internal-only, ordinary prose more locally coherent).
CONNECTOME (#65): integrated small-world ecosystem, keystone hubs, emergent fields — but topology GENERAL to
  language (NOT distinctive); use as MAP; PPMI-normalize. Collocation (#66): PPMI(association) × sūra-spread(local↔global).
UNIFYING THESIS: ARCHITECTURE OF RETURN — locally LESS continuous than ordinary prose, globally RETURNS more.

LOCKED PRINCIPLES (DESIGN_STANCE.md — obey ALL): divine-rootedness (rasm/roots over ḥarakāt; human
  names/groupings = control-only) · absence-of-evidence ≠ absence (telescope) · VOICE: data-driven, no
  overclaim, no miracle-tone, no naive propositions · CROSS-IMPACT propagation (nothing is final; re-evaluate
  verdicts via other modalities) · REARRANGEMENT built into every experiment · MULTI-GRAIN & NETWORK-FIRST
  (no one-size-fits-all; topologies/communities/dynamics) · CONNECTOME/ECOSYSTEM (connect all, retain every
  part) · NORMALIZE for frequency (PPMI/TF-IDF/effect-size; universal-to-language ≠ distinctive w/o comparator)
  · keep the PAPER live at every finding · interaction: always offer 1/2/3 + a recommendation.

NEXT RESEARCH CANDIDATES: extend muqaṭṭaʿāt/rasm positional thread (network-first: dynamic communities,
  bipartite sūra×letter, letter-transition graph) · multi-layer connectome (letters↔roots↔āyahs↔sūras) ·
  E5 permutation entropy · referent-aware iltifat (coref-blocked) · recited (data-blocked, DEPRIORITIZED ḥarakāt).
APP: v1.4 feedback/bug widgets shipped; IA re-spine = v2.0 (APP_PLAN.md). Per-lens impact: COVERAGE_MAP.html.

>>> STANDING LENS (user-mandated, never drop) — SIGNAL-GEOMETRY / POINTER <<<
    Full register: IDEA_SIGNALS_GEOMETRY.md. Āyah = "sign": treat units as signals; formulate in
    many ways (1D/2D point-area-vector). Toolkit to operationalize over time: signals, vectors,
    signal-combination, MASKING/FILTERING (two roles: remove a mask to reveal hidden signal; apply
    a mask/band-pass to isolate), transformation, translation in vector space, decomposition
    (SVD/PCA/ICA/NMF), projection/collinearity, distance metrics. Concept = pointer = mask+vector.
    WAVELET-ON-LENGTH: TESTED, NO CREDIT (this session). Baseline +2.35sd, BUT independence check
    FAILED — masking rhyme-ending (project out #33) collapses it to 1.37 (sub-2sd, saj' 2.04 exceeds);
    and a 2nd non-length formulation (lexical novelty) is null for the Qur'an (0.37, below prose/poetry).
    => largely #33 seen through the length channel. Script: sequence_tests/wavelet_indep.py (dep:
    PyWavelets). Naive univariate point-pattern = DEAD (N-confound). METHOD stays OPEN for untested
    formulations: root-grain, masked/subspace, 2D area/image, semantic-field signals (telescope rule).
    SUB-UNIT POSITIONAL/DIRECTIONAL LENS (user-mandated): ayah = inviolate unit, but study sub-units
    (char->root->morph token); positional/spatial; default scan R->L, reverse allowed for discovery.
    VERIFIED viable (posdir_prelim.py): end-cadence real & null-sig in ALL corpora (z 3.3-6.4) but
    Qur'an mid/low (0.132 vs poetry 0.344) = NO credit on first feature. Directionality real but
    linear-slope flip is trivial; need NON-antisymmetric directional stat (fwd/bwd entropy, triplet
    asymmetry) next. To pursue: root/morph-grain (COL_SEGMENTED), feature-specific positional profiles.
    GATE STILL APPLIES to every spawned test: equal-N + null + comparator + positive-control.

>>> MODALITY #46 — LEXICAL-SEMANTIC / TOPICAL FIELD DYNAMICS === DONE (this session). NULL. <<<
    Per-unit semantic-field label -> shuffle-controlled field SEQUENCING (switch, MI) + COHESION
    (run-length) excess, equal-N, comparators, gate-passed. TWO taggers: (A) seed-lexicon, (B) data-
    driven TF-IDF->KMeans (every unit labeled, removes OTHER bias). BOTH NULL: |g|<0.5sd vs all
    comparators; Qur'an clusters fields if anything LESS than ordinary (run g=-0.44 vs ord); poetry
    most cohesive. 12th modality register-level/null. #42 recurrence still the SOLE distinctive.
    Scripts: fields46.py, fields46_clusters.py. EVIDENCE #46. Coverage lexical-semantic 50->72%,
    overall ~58->~60%. UNTESTED sub-region (if revisited): passage-grain cohesion via embedding
    similarity (semantic_ring LSA) + coarser pericope grain.

>>> MODALITY #47 — DEPENDENCY-SYNTAX (Lens 13) === DONE (local stanza run). REGISTER-LEVEL / NULL. <<<
    Parser blocked in sandbox (torch CUDA wheel too big; CPU index 403) but RAN LOCALLY via
    run_dependency_syntax.py (stanza UD-PADT, diacritics stripped, equal-N=188). Gate passed (scramble
    raised dep_dist 2.18->2.27). On EVERY metric Qur'an BELOW ordinary prose — shallower trees (depth g=
    -0.66), shorter deps (g=-0.36), fewer long deps (g=-0.27); above poetry/saj' (+0.3..+1.25 genre gap);
    all sub-2sd. The Qur'an is syntactically SIMPLER than prose, no embedding-depth fingerprint — REAL-
    PARSER confirmation of Lens 11. Caveats: MSA parser on Classical Arabic, small baselines, 4 metrics.
    Coverage dependency-syntax 35->75%; overall ~60->~64%. EVIDENCE #47; Lens 13 added to paper. Scripts:
    sequence_tests/dependency_syntax.py, run_dependency_syntax.py (+.bat).

>>> MODALITY #48 — DIRECTIONAL sub-unit + root-grain positional === DONE. No new distinctive. <<<
    directional48.py. (A) Genuine directional time-irreversibility (signed increment-skew): Qur'an LEAST
    directional of all (-0.054, z=-1.23); poetry/saj' show it more; sub-2sd, Qur'an-null. (B) Root-rarity
    vs position (Qur'an-internal): +0.072 z=+13.4 — rare roots toward ayah END, but confounded (generic
    word order + rhyme); not a distinctiveness claim, PARKED pending root/morph comparator + rhyme-residual.
    EVIDENCE #48; IDEA_SIGNALS_GEOMETRY §8. No coverage change.

>>> MODALITY #49 / Lens 14 — RECITED/PHONOLOGICAL === detector built + Qur'an-internal validated; DISTINCTIVENESS DATA-BLOCKED. <<<
    sequence_tests/recited_phon.py: rule-based syllabifier on the VOCALIZED Qur'an (COL_DIACRITIZED) ->
    heavy_ratio/madd/ghunna/rhythm. Gate ok (de-diac -> 0 syllables). INTERNAL POSITIVE: short surahs more
    isochronous (CV 0.36 vs 0.48); weight-sequence ALTERNATION vs shuffle (Baqara z=-10.7, Rahman -6.0).
    But these may be universal Arabic phonotactics — DISTINCTIVENESS needs VOCALIZED COMPARATORS (none
    install/fetch in sandbox). >>> UNBLOCK LOCALLY: run_recited_phon.py — PATH A drop Tashkeela (voc prose)
    + voc dīwān into corpus/ (gold-vs-gold, best); PATH B symmetric auto-diacritize via CAMeL (diacritize
    comparators AND a stripped Qur'an with same tool — avoid #42-style gold-vs-noisy confound). Paste
    evidence_49_results.txt back. <<< Coverage recited UNCHANGED ~0 (block). EVIDENCE #49; Lens 14 in paper.

>>> MODALITY #50 / Lens 15 — MUQATTA'AT / RASM POINTER === DONE. POSITIVE (divinely-rooted). <<<
    sequence_tests/muqattaat_pointer.py (rasm only, no ḥarakāt). A) bearer enrichment 1.064x z=+2.17
    p=.024 (ق/S50 1.73x, ص/S38 1.46x, ن/S68 1.24x). B) half-alphabet 14/28 exact (احرسصطعقكلمنهي).
    C) mushaf contiguity 19 adjacent pairs vs null 7.1, p<1e-4. Gate valid (pos 1.49x, neg 1.01x).
    Internal design structure of revealed text, permutation-nulled, sui generis. EVIDENCE #50; Lens 15.

>>> #51 — MUQATTA'AT DEEPENED === DONE. Pointer is ROBUST + spatially strong. <<<
    muqattaat_deepen.py: Moran's I=+0.54 z=5.8 p<1e-4 (mushaf); ROBUST under nuzūl order (I=+0.31 p<1e-4,
    contiguity p=.001) -> not an arrangement artifact, strongest in canonical order; bearer enrichment
    concentrated in DISTINCTIVE letters (ط/ق/ن/ص ~1.2x), common ا/ل/م ~1.0. EVIDENCE #51; Lens 15 sharpened.

>>> #52 — MUQATTA'AT PHONETIC BALANCE === DONE. Popular 'half of every category' claim NOT significant. <<<
    muqattaat_phonetic.py: voicing splits EXACTLY half (5/10, 9/18), emphatic 2/4, stop 4/8 (striking
    individually) BUT aggregate balance vs random 14-subset p=0.14 (sub-2σ; throat/labial deviate).
    Structure = CARDINALITY (14/28) + POSITION (#50/#51), NOT phonetics. Honest tempering. EVIDENCE #52.

>>> #53 — SIGNAL-GEOMETRY ON ROOTS === DONE. POSITIVE: muqaṭṭaʿāt are ROOT-SPACE coherent. <<<
    muqattaat_rootspace.py: 29 muqaṭṭaʿāt sūras cosine 0.53 vs null 0.25, z=+6.9 p<1e-4; same-letter groups
    tight (Ḥā-Mīm z=+3.1, الر z=+2.7, الم z=+3.3). Opening letters track LEXICAL-THEMATIC families. Pointer
    is now POSITION + CONTENT structure. Caveat: mostly-Meccan register inflates 29-set; subgroups tighter
    -> letter-specific. EVIDENCE #53; Lens 15 deepened.

>>> #54 — MECCAN-CONTROLLED null === DONE. Caveat RESOLVED, effect STRENGTHENS (z=+7.4). <<<
    muqattaat_rootspace_meccan.py: root-space cohesion survives & strengthens vs Meccan-only null (Meccan
    baseline lower bc Medinan legal sūras inflate all-corpus). Letter-grouping is genuinely letter-specific,
    NOT register. #53 caveat closed. EVIDENCE #54; Lens 15 updated.

>>> #55 — "THE BOOK" THEME ANCHOR === DONE. YES: muqaṭṭaʿāt over-express revelation lexicon. <<<
    muqattaat_revelation.py: whole-sūra REV-root rate 0.071 vs 0.048 z=+3.55 p=.0002; openings ~5x
    (0.31 vs 0.06) — letters are a frontispiece to scripture-about-scripture. Anchors PART of #53/#54
    cohesion (theme z=3.5 < cohesion z=6.9). EVIDENCE #55; Lens 15 updated. (Teaching handout also made:
    Creation_as_Signs_handout.docx — creation-as-āyāt, for a 10-min student session.)

>>> #56 — PER-LETTER ROOT-SIGNATURES === DONE. No letter→theme cipher (global NULL); thematic at margin. <<<
    muqattaat_letter_signatures.py: families NOT separable as whole vectors (within 0.574 ≈ between 0.570,
    z=+0.30 p=0.37). Distinctive roots ARE thematic (الر→Yūsuf prison/measure; طس→Mūsā/Pharaoh sorcery;
    الم→law trade/ribā/divorce; حم→dispute) BUT confounded with narrative content (الر holds Sūrat Yūsuf).
    Closes muqaṭṭaʿāt content arc: cohesion real & theme-anchored (#53/#54/#55); SEPARATION not established.
    EVIDENCE #56; Lens 15 finalized.

>>> #57 — CANONICAL-ORDER THEMATIC COHERENCE === DONE. POSITIVE (length-controlled). <<<
    canonical_order_theme.py: adjacent sūras root-similar beyond the length gradient (length-band(6) null
    z=+3.14 p=.0007; full-shuffle z=+10.6 mostly = length). NMF recovers refuge/eschatology/creed/devotion
    themes. 3rd divinely-rooted positive (whole-muṣḥaf arrangement). Lens 16 added; coverage ~70%. EVIDENCE #57.

>>> #58 — SŪRA-JUNCTION INTERLOCK (tanāsub al-suwar) === DONE. REAL but not canonical-specific. <<<
    sura_junction.py: seam-interlock real under BOTH legitimate orders (full-shuffle null 0.071):
    CANONICAL z=+3.98, NUZŪL z=+5.92 — chronology interlocks MORE; canonical NOT specially optimized.
    Honest reading: muṣḥaf sustains seam-coherence DESPITE abandoning chronological grouping (coherence
    against the grain); not evidence of unique canonical design. Overlaps #57; period/length-locality is the
    driver. REARRANGEMENT scenarios (user-suggested: canonical vs nuzūl) baked in. EVIDENCE #58. No coverage change.
    METHOD NOTE: add EDIT-DISTANCE (Levenshtein) as a multimodal recurrence/variation metric — see IDEA_SIGNALS_GEOMETRY §7.

>>> REARRANGEMENT PROGRAM (user-mandated, first-class) — see DESIGN_OF_EXPERIMENTS.md <<<
    'Rearrangement' is now a lens family with a live DoE matrix: ORDERING MECHANISMS (linear index; āyah-
    FINAL word as root/concept stream; rhyme-class; root first-occurrence; freq-rank) × SCALES (word-in-āyah,
    āyah-in-sūra, sūra-in-muṣḥaf, recurrence-pairs) × METHODS (edit-distance/SW, LCS, Kendall τ/inversion,
    genome-rearrangement, DTW, optimal transport, permutation entropy, Moran/Geary, Mantel, block-permutation
    sensitivity). Methods in IDEA_SIGNALS_GEOMETRY §7+§9. Nulls: random-at-scale + allowed-practice reorderings
    (nuzūl/Nöldeke) reported together. Done so far: #57, #58.

>>> RECENT (this session): #59/E2, #61/E3, #62 fāṣila-fit <<<
    #59/E2 fāṣila-concept stream: verse-ends chain LEAST (rhyme decouples horizontally) — m2 not privileged.
    #61/E3: re-expression QUANTIFIED — recurrence pairs cos 0.68 but edit-sim 0.27, Kendall +0.42 (confirms #42).
    #62 fāṣila–CONTENT FIT (munāsabat al-fawāṣil; user rhyme-end grouping): STRONG POSITIVE — āyah-final word
       predicts body content; ROOT grain mean z=+11.3 (13/14), MORPHOLOGY grain mean z=+12.1 (16/16; قدیر+32
       رحیم+29 صادقین+27 حکیم+26). Survives self-repetition control. Qur'an-INTERNAL; morphology = apt unit
       for the ending. Reconciles E2 (caps own āyah, not next). Scripts: fasila_content_fit.py, recurrence_editdist.py.

>>> #63 — fāṣila COMPARATOR === DONE. ending-REPETITION is cross-text DISTINCTIVE (exceeds saj'). <<<
    Comparators have ~0 endings recurring ≥10x; equal-N frac-recurs≥3x: QURAN 0.28 vs saj' 0.04, ord 0.10,
    poetry 0.02 (saj' ties on type-TTR but not heavy repeti
# Seventeen Computational Lenses on Qur'anic Style — Conceptual Foundations

*An orientation to what each lens looks at, why, and how it reads on the Qur'an itself.*

> Companion documents: empirical results in `EVIDENCE.md` (#18–63); integrated findings in
> `MASTERY_REPORT.md`; the next forks are scoped at the top of `HANDOFF_MASTERY.md`.
> This paper is **conceptual and illustrative**: every worked example is drawn from the Qur'an only,
> so a reader can see *what each lens measures* before consulting the numbers.

---

## Abstract

The classical claim of *iʿjāz* (the Qur'an's inimitability) is, at root, a claim that its language
occupies a region no other Arabic text reaches. To examine that claim empirically — without presuming
it — we adopted a **positive-control-first** program: a stylistic measure earns the right to be applied
to the Qur'an only after it provably separates a *known* master from ordinary writing in the same
language. Under that discipline we built and gate-validated twelve families of detectors, twelve "lenses,"
each targeting a different layer of verbal craft: (1) lexical–statistical texture and repetition,
(2) large-scale architecture (ring composition and refrain), (3) end-rhyme / *fāṣila*, (4) sound–meaning
iconicity (phonosemantics), (5) the multimodal *fusion* of these, (6) prosodic rhythm (the written
trace of *tartīl*), (7) morpho-syntactic structure (*iltifāt* — grammatical person/number/tense
shifting), (8) morphological-template (*wazn*) distribution, (9) intra-textual narrative recurrence
(the same story re-told across distant sūrahs with variation), (10) discourse macrostructure (the
sequencing of speech-act *moves* — oath, narrative, judgment, address), and (11) shallow syntactic
complexity (parataxis vs. hypotaxis — *wāw*-coordination, relative-clause embedding, clause length), and
(12) lexical-semantic field dynamics (whether the text *sequences* or *clusters* topical fields — mercy,
judgment, nature, law, covenant — distinctively), and (13) **dependency-syntax** with a real
parser (embedding depth and dependency distance — the deep test Lens 11 could only proxy), and (14)
the **recited / phonological** layer (syllable weight, *madd*, *ghunna*, isochrony — the vocalized
stratum where *tartīl* lives), and (15) the **muqaṭṭaʿāt / rasm pointer** — the disjoint opening letters
and their placement in the revealed consonantal text and canonical order, and (16) **canonical-order
thematic coherence** (whether the arrangement of sūras is thematically smooth beyond their length gradient), and (17) the **fāṣila system** — recurrence and
content-fit at the verse-end (do the endings repeat heavily, beyond rhyme, and fit their verse's content?).
This paper explains the
**conceptual foundation** of each lens and walks through a concrete Qur'anic case for it. The empirical
verdicts are summarized at the end of each section and treated fully in the companion files; the purpose
here is orientation, not adjudication. One result stands apart: lens (9), measured at passage scale with
the right controls, is the **one single axis to put the Qur'an clearly into the 2σ neighbourhood beyond
ordinary Arabic** (~+3σ after a tokenization-bug correction; EVIDENCE #43) — sharpening, rather than
replacing, the structured-repetition signature that runs through the whole sweep.

---

## 1. The question, and the rules of evidence

"Is the Qur'an a linguistic masterpiece?" is not, as stated, a testable proposition — *masterpiece* is
an evaluative word. We reformulate it into a falsifiable shape:

> **Does the Qur'an occupy a measurable region of stylistic space that ordinary Arabic — and even
> Arabic masters — do not?**

Four rules govern the search, so that conviction guides *where we look* while evidence decides *what we
claim*:

- **Divine-rootedness control.** Study the *revealed* text, not what humans later added: the priority
  object is the consonantal *rasm* and its content — roots, words, āyah boundaries and counts, sūrah
  structure, and the canonical arrangement (and the order of letters, including the *muqaṭṭaʿāt*). Human
  notational/editorial artifacts — chiefly the *ḥarakāt* (vowel pointing), and likewise tajwīd notation,
  punctuation and editorial sūra titles — are **deprioritized**, because a signal found in them describes
  the editors, not the revelation. (This is why Lens 14, built on the *ḥarakāt*, is retained but not a
  priority line.)
- **Positive-control-first.** A measure is admissible only if it first separates a known master from
  ordinary text in its own language. A yardstick that cannot tell Shakespeare from a newspaper has no
  authority to pronounce on the Qur'an. (This single rule eliminated most "obvious" measures: entropy,
  compression, and mutual information are *mastery-blind* — they fail to separate masters at all.)
- **The telescope rule.** A non-detection means *the instrument was too weak*, never that the feature is
  absent. We therefore (a) validate every detector on a synthetic positive control and a degradation
  ladder before trusting a null, and (b) report nulls as "no signal at this resolution," not "no signal."
- **The invariance gate (G10).** A cross-text verdict is inadmissible unless it survives equal-sized
  windows, at least two tokenizations, and a *same-language* ordinary baseline — with a permutation or
  bootstrap null and, ideally, a ≥2 standard-deviation separation. This is what stops a lucky artifact
  from being mistaken for a discovery (we caught two such artifacts mid-program; see Lens 5).

A recurring touchstone is the Qur'an's own statement about its genre, *Yā-Sīn* 36:69 —
وَمَا عَلَّمْنَاهُ الشِّعْرَ وَمَا يَنبَغِي لَهُ ("We did not teach him poetry, nor would it befit him").
Classical poetics define *shiʿr* as كلام موزون مقفّى — speech that is **metered and rhymed**. Several
lenses below turn out to measure exactly the two halves of that definition (rhyme; meter), which lets us
give 36:69 an empirical reading rather than only a theological one.

---

## 2. Preliminaries — text, units, and how a "lens" is built

**The text and its natural units.** The Qur'an segments naturally at two scales: the *āyah* (verse),
whose end is the *fāṣila* (the rhyme/cadence boundary), and the *sūrah* (chapter). Most lenses treat the
āyah as the basic unit and a window of consecutive āyāt (or a whole sūrah) as the sample.

**Normalization.** Arabic reaches a reader in many orthographic variants; before counting anything we
fold letters to a canonical skeleton (alif variants → ا, the *yāʾ*/*alif maqṣūra* → ي, *tāʾ marbūṭa* → ه,
etc.) and, for most lenses, strip the diacritics. This last choice matters and returns in Lens 6: it
makes lexical comparison fair but renders the short vowels — the carriers of recited rhythm — invisible.

**Anatomy of a lens.** Each detector has the same skeleton, dictated by the rules above:
1. a **feature** (what is counted — a repetition rate, a rhyme class, a phoneme ratio, …);
2. a **null model** (usually a permutation that destroys the structure while preserving the ingredients,
   e.g. shuffling āyah order to test placement);
3. a **gate** (a synthetic positive control the detector *must* flag, a degradation ladder it must track
   monotonically, and an ordinary-text negative it must read near zero) — run *before* the Qur'an;
4. a **report** as a standardized effect size (σ-gap) with a bootstrap probability, against a
   same-language baseline.

With that scaffold fixed, the eleven lenses differ only in *what layer of language they make visible*.

---

## 3. Lens 1 — Lexical–statistical texture and repetition

**Concept.** The oldest computational stylometry treats a text as a bag of tokens and measures its
information texture: vocabulary richness (type–token ratio, Yule's K), word-length regularity, and —
most relevant here — **long-range repetition**, the rate at which content recurs across a passage.
Repetition is the natural quantitative correlate of the Qur'an's celebrated *mathānī* (المثاني, "the
oft-repeated"; cf. الحجر 87, وَلَقَدْ آتَيْنَاكَ سَبْعًا مِّنَ الْمَثَانِي): refrains, formulae, and
recurring narratives.

**What it measures.** Over equal-sized windows we compute character- and word-level repetition (with
frequent function-words optionally removed, to isolate *content* repetition), lexical variety, and
word-length spread, each against a same-language ordinary baseline and ≥2 tokenizations (the G10 gate).

**A Qur'anic case.** Consider *al-Raḥmān* (55). Its verse فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ
recurs **thirty-one times**, threaded between successive descriptions of creation and reward. At the
bag-of-words level this drives the surah's content-repetition far above ordinary prose. The same texture,
softer, pervades the recurring closures of *al-Qamar* (54): after each destroyed nation the refrain
فَهَلْ مِن مُّدَّكِرٍ returns, punctuated by وَلَقَدْ يَسَّرْنَا الْقُرْآنَ لِلذِّكْرِ. And at the largest
scale, the story of Mūsā is retold across al-Baqarah, al-Aʿrāf, Ṭā-Hā, al-Qaṣaṣ and more — the same
narrative, re-voiced with variation. Lens 1 is the lens that *sees* all of this as one quantity:
structured recurrence.

**What we found.** Repetition is the Qur'an's most *consistent* statistical signature — it is genuinely
elevated and ordinary-absent in direction — but its **magnitude is modest**: ~+1σ above classical Arabic,
below the 2σ admissibility bar, and it behaves as a *register* property (shared, in kind, with oral-
formulaic and rhymed-prose Arabic) rather than a Qur'an-unique fingerprint. The cross-language twist
(Lens 5) is that this is the *opposite* of what poetic masters do: Mutanabbi, Shakespeare and Hafez
*minimize* long-range repetition; the Qur'an maximizes it. (EVIDENCE #18–30.)

---

## 4. Lens 2 — Architecture: ring composition and refrain

**Concept.** Beyond local texture lies *composition*: how a sūrah is built as a whole. Two architectural
forms are claimed for the Qur'an. **Ring composition (chiasmus)** is concentric symmetry — a passage
ordered A · B · C · Bʹ · Aʹ, so that the opening mirrors the close around a pivot; a substantial
scholarly literature (e.g. Cuypers on *al-Māʾida* and *al-Baqarah*, Farrin on whole-sūrah symmetry)
argues the Qur'an is pervasively ring-structured. **Refrain** is the opposite move in time: a fixed line
returning at regular intervals (a *periodic*, not mirror, structure).

**What it measures.** For *ring*, we cut a sūrah into blocks and ask whether block *i* is more similar
(in shared roots, then in latent *semantics*) to its mirror block than a random re-ordering of the blocks
would predict — a permutation test on *position*. For *refrain*, we locate near-identical āyāt and ask
whether their spacing is *more regular* than a shuffle of the same āyāt — i.e. whether the repetition is
*architecturally placed*, not merely frequent.

**A Qur'anic case.** *Ring*: open *al-Baqarah* and the scholarly claim is that its great blocks (the
disbelievers / the People of the Book / the Children of Israel / legislation / …) fold symmetrically
about the central passage on the *qibla* — an A·B·…·Bʹ·Aʹ arc spanning the longest sūrah. *Refrain*:
*al-Raḥmān*'s فَبِأَيِّ آلَاءِ returns on a near-fixed beat; *al-Mursalāt* (77) tolls
وَيْلٌ يَوْمَئِذٍ لِّلْمُكَذِّبِينَ ten times; *al-Qamar* alternates two refrains across its panels. These
are the textbook instances the two detectors are built to catch.

**What we found.** A clean split. **Ring composition is *not* detectable corpus-wide** — neither lexically
nor semantically, at any block scale — once tested against a permutation null (the scholarly claims are
passage-level, semantic, and rely on hand-identified pivots, which a uniform statistical sweep does not
reproduce; this is a telescope-rule non-detection, not a refutation of those readings). **Refrain is real
but localized**: only ~9 of 114 sūrahs carry a periodically-placed refrain, with *al-Raḥmān* an
overwhelming outlier (its placement is ~7σ more regular than chance). So architecture, as a *general*
signature, is a null; as a *local device*, it is unmistakably real where it occurs. (EVIDENCE #31–33b.)

---

## 5. Lens 3 — Rhyme and the *fāṣila* (presence vs. persistence)

**Concept.** Every āyah ends in a *fāṣila*, a rhyme/assonance at the pause. This is the audible spine of
Qur'anic style and the *qāfiya* half of the poetry definition. But "rhyme" hides two different
properties that must be separated: **presence** (do neighbouring units rhyme at all?) and **persistence**
(does *one* rhyme hold across a long stretch, or does it shift?). Poetry holds a single rhyme for an
entire poem (*monorhyme*); ordinary prose does not rhyme; rhymed prose (*sajʿ*) rhymes but **shifts** its
rhyme every clause or two. The Qur'an's position on these two axes is the empirical content of "rhyme."

**What it measures.** *Presence* = the rate at which adjacent units share a rhyme ending, above the
chance rate implied by their ending frequencies. *Persistence* = the share of a single dominant ending
across a 20-unit window (high ⇒ one sustained rhyme). Both are computed identically on each register's
natural pause units (āyah, verse-line, sentence, sajʿ-clause), so registers can be compared on the same
footing.

**A Qur'anic case.** Short Meccan sūrahs make the *fāṣila* vivid. *al-Ikhlāṣ* (112) holds one rhyme
across all four āyāt — أَحَدٌ · الصَّمَدُ · يُولَدْ · أَحَدٌ (the rhyme on a final *-ad*). *al-Fātiḥa*
sustains a nasal *-īm/-īn* fāṣila — الرَّحِيمِ · الْعَالَمِينَ · الرَّحِيمِ · الدِّينِ · نَسْتَعِينُ ·
الْمُسْتَقِيمَ · الضَّالِّينَ. *ash-Shams* (91) runs a long *-hā* down the whole sūrah
(ضُحَاهَا · تَلَاهَا · جَلَّاهَا · يَغْشَاهَا · بَنَاهَا · …). In each case a single rhyme is *held*, not
shuffled — the hallmark our "persistence" axis is designed to quantify.

**What we found.** Two-part result. On **presence**, the Qur'an rhymes strongly — far above ordinary prose
(~+2.5σ) and comparable to poetry — but this property is **shared with sajʿ**, so it is *not*
Qur'an-specific (sajʿ rhymes too). On **persistence**, the Qur'an separates even from sajʿ: it *sustains*
one fāṣila across a passage (dominant-rhyme share ≈ 0.49, near poetry's monorhyme ≈ 0.54) where sajʿ
restlessly shifts (≈ 0.23) — a +1.7σ gap, stable across two sajʿ masters (al-Hamadhānī, al-Ḥarīrī). So
the distinctive is not *that* the Qur'an rhymes but *how long it holds the rhyme* — verse-like
persistence, carried on prose with no meter. (EVIDENCE #34, #36–37b.)

---

## 6. Lens 4 — Phonosemantics: sound–meaning iconicity

**Concept.** Sound symbolism (phonosemantics) is the hypothesis that the *sound* of words is not
arbitrary with respect to their *meaning* — that "heavy," emphatic, guttural phonemes (the *mufakhkhama*
ص ض ط ظ ق and the gutturals خ غ ع ح ء ه) cluster in passages of harshness, force and dread, while
"light," flowing sonorants (ل ر م ن and the long vowels) gather in passages of mercy and ease. This is
a recurrent theme in Arabic rhetorical appreciation of the Qur'an: that its *jaras al-alfāẓ* (the ring of
the words) is fitted to the sense.

**What it measures.** Two tests. A **general** one asks whether semantically similar āyāt are also
phonetically similar *beyond* the trivial fact that they share words — a partial correlation between a
semantic-similarity matrix and a phoneme-class-similarity matrix, with lexical overlap partialled out.
A **targeted** one operationalizes the classic claim directly: classify āyāt by a *harsh* vs *gentle*
semantic field (seed roots: عذب، نار، سقر، بطش، غضب… vs رحم، جنة، نور، غفر…) and compare the density of
heavy phonemes between the two.

**A Qur'anic case.** The intuition is easy to *hear*. *al-Masad* (111) opens
تَبَّتْ يَدَا أَبِي لَهَبٍ وَتَبَّ — clipped plosives (ت، ب) hammering a curse. *al-Qāriʿa* (101) rolls a
heavy *qāf* through its name and refrain: الْقَارِعَةُ · مَا الْقَارِعَةُ · وَمَا أَدْرَاكَ مَا
الْقَارِعَةُ. Against these, the gentleness of *al-Kawthar* or the long-vowelled flow of mercy verses
seems to *soften* the consonantal palette. Lens 4 asks whether that felt iconicity is statistically real
and stronger in the Qur'an than elsewhere.

**What we found.** **Null** — on both tests, and this is one of the more striking results. General
sound–meaning binding beyond shared vocabulary is ≈ 0 in the Qur'an and no higher than in prose, poetry,
or sajʿ. The targeted "harsh content ⇒ heavy phonemes" test is also null and in fact slightly *reversed*
(harsh āyāt carry marginally *fewer* heavy phonemes than gentle ones). The felt iconicity of a verse like
*al-Masad* appears to be a property of *individual salient words* and the reader's interpretive framing,
not a measurable system-wide coupling of sound to meaning. (Caveat per the telescope rule: our phonetic
features are coarse consonant classes; finer prosodic/affective features could revisit — but the strong
form of the claim is cleanly unsupported.) (EVIDENCE #38.)

---

## 7. Lens 5 — Multimodal fusion: the "cell"

**Concept.** "No silver bullet": if no single axis is decisive, the signature may live in a *combination*.
Fusion asks whether the **conjunction** of features locates the Qur'an where no single feature can. The
guiding idea is a stylistic coordinate space — rhyme × meter × repetition × variety — in which each genre
occupies a *cell*. Poetry = rhyme + meter + high variety; ordinary prose = none of these; the question is
which cell the Qur'an inhabits, and whether it is one no neighbour shares.

**What it measures.** A classifier is trained to separate Qur'an windows from poetry-and-prose windows
using all axes at once; its cross-validated accuracy is compared with the best *single*-axis accuracy and
with a label-shuffle null. The decisive quantity is not raw accuracy but the **gap**: does the conjunction
beat every axis alone?

**A methodological aside (why the gate matters).** This lens is where the G10 gate earned its keep. An
early run scored a *perfect* AUC = 1.000 — which was a lie: it came from comparing the Qur'an's
*morphologically segmented* tokens against whole-word poetry/prose (a tokenization artifact), compounded
by fixed-length prose "units" that made verse-length variation separate trivially. Both artifacts were
caught and removed; the honest score is ~0.94, not 1.0. The episode is a concrete illustration of the
rule: an instrument that looks too good is usually measuring itself.

**A Qur'anic case.** Take a short Meccan sūrah and read it against the cell. *al-Ikhlāṣ* rhymes (Lens 3,
present *and* sustained), yet does **not** scan to any *baḥr* (no meter), and its diction is plain, not
ornate. That triad — *holds a rhyme like verse · keeps no meter like prose · leans on repetition/plainness
rather than poetic ornament* — is the cell. No qaṣīda sits there (it would scan); no ḫuṭba sits there (it
would not sustain rhyme); even sajʿ sits only partly (it shifts its rhyme and prizes ornament).

**What we found.** The conjunction works where the parts do not. The Qur'an is separable from poetry *and*
prose at AUC ≈ 0.94 (null 0.50); the interpretable two-axis conjunction **rhyme × (non-)meter** reaches
≈ 0.92, beating rhyme alone (~0.76) and meter alone (~0.84) — because rhyme distinguishes the Qur'an from
prose but not poetry, while non-metrical variable verse length distinguishes it from poetry but not prose.
*Only together do they isolate it.* Against the adversarial sajʿ control the bare cell is partly shared,
but the Qur'an still separates (AUC ≈ 0.96) via rhyme *persistence* and *repetition*. (EVIDENCE #35–37b.)

---

## 8. Lens 6 — Prosodic rhythm: the written trace of *tartīl*

**Concept.** Distinct from rhyme (which letters end the line) and from meter (a fixed syllabic template),
*rhythm* is the felt pulse of the recitation — *tartīl*. One text-visible facet of it is **isocolon**: the
tendency of successive pause-units to be *balanced in length*, producing parallel cola — a rhythm *without*
meter. Short Meccan sūrahs feel drum-like and rapid; later Medinan legal passages flow in long breaths.
That contrast is, in part, a rhythm of āyah lengths.

**What it measures.** *Isocolon* = whether adjacent pause-units are more length-balanced than a random
re-ordering of the same units (a placement test). A second feature, *metricality*, gauges how periodic the
consonant–vowel skeleton is (a meter proxy: high for a regular *baḥr*, low for prose).

**A Qur'anic case.** Compare extremes. *al-ʿĀdiyāt* (100) and *al-Qāriʿa* (101) move in short, near-equal
beats — clipped āyāt of similar length, a strong pulse. The "verse of debt," آية الدين (2:282), is by far
the longest āyah in the Qur'an, a single sustained legal period. Lens 6 asks whether, *within* a passage,
the Qur'an balances adjacent āyāt into parallel cola more than ordinary prose, and whether any of this
amounts to meter.

**What we found.** Null for distinctiveness — with the program's most important *caveat*. The Qur'an's
isocolon equals ordinary prose and sits *below* sajʿ (sajʿ is the genuinely isocolonic register of
balanced paired clauses); its metricality is the lowest of all (decisively *no meter*, confirming the
*wazn* half of 36:69). **But** this lens is computed from *consonantal* text — the diacritics, *madd*
(vowel lengthening), *ghunna*, and pause phonology that actually carry recited rhythm are invisible to it.
So the honest reading is "*no rhythm recoverable from the written skeleton*," not "no rhythm." This points
straight at the program's frontier (§11). (EVIDENCE #39.)

---

## 9. Lens 7 — Morpho-syntactic structure: *iltifāt*

**Concept.** Beneath texture, architecture, and sound lies the **grammatical** layer, and it houses the
device the classical critics held to be most distinctively Qur'anic: ***iltifāt*** (الالتفات, "the
turning"). An iltifāt is an abrupt, rule-governed shift of grammatical **person, number, tense, or
addressee** in mid-passage while the referent stays the same — God spoken *about* in the third person
and, a clause later, *addressed* in the second; a singular that becomes a plural; a past that slides into
a vivid present. Al-Zarkashī and al-Suyūṭī catalogue it as a beauty unique to high Arabic style and
especially dense in the Qur'an. The empirical question: does the Qur'an *shift* — in person, number, or
tense — at a higher **rate**, or in a distinctive **pattern**, than ordinary Arabic, poetry, and sajʿ?

**What it measures.** A lightweight tagger labels each pause-unit with its dominant person (1/2/3),
number, and tense, read from independent pronouns (أنا، نحن، أنتم، هو، إيّاك…), the vocative *yā*, attached
clitic pronouns (ـكم، ـهم، ـها، ـنا…) and verb agreement (imperfect prefixes ت/ن/ي/أ vs perfect suffixes).
An *iltifāt event* is a change between adjacent units along any axis. The detector reports a **shift-rate**
and a **transition-type profile** (which shifts: 3→2, 2→3, …), each against (a) a *within-text shuffle*
null that tests whether shifts are *placed* non-randomly and (b) the same-language baselines — with
quoted-speech (*qāla*-framed) boundaries controlled, since ordinary reported speech changes person
without being iltifāt. Because the comparison corpora are unsegmented, the tagger runs on raw text
identically everywhere; calibrated against the Qur'an's own gold morphological segmentation it agrees on
dominant person ~81% of the time.

**A Qur'anic case.** The textbook instance is *al-Fātiḥa*: the opening praises God in the **third**
person — الْحَمْدُ لِلّهِ … مَالِكِ يَوْمِ الدِّينِ — then pivots, mid-sūrah, to **direct address**:
إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ ("**You** [alone] we worship"). A single 3→2 turn reorients the
whole prayer. The longer-range classic is *Yūnus* 10:22, the sea-voyage: it begins addressing the
audience — هُوَ الَّذِي يُسَيِّرُكُمْ ("He it is who carries **you**") — and, as the storm rises, *turns
away* from them into the third person — وَجَرَيْنَ بِهِم … وَفَرِحُوا بِهَا ("and they sailed with
**them** … and **they** rejoiced"), the grammatical swerve enacting the passengers' estrangement. These
are exactly the events the detector is built to count.

**What we found.** **Null vs ordinary Arabic, register-level otherwise.** At equal sample size and across
two tokenizations, the Qur'an's **person**-shift rate is statistically indistinguishable from ordinary
Arabic prose (Δ ≈ ±0.1–0.25σ, P ≈ 0.44–0.50); it exceeds poetry and sajʿ only as a *genre* gap (those
registers are more person-monotone). Number-shifting is, if anything, *lower* than ordinary (more
number-stable). The transition profile does show the Qur'an to be markedly **address-oriented** — its
commonest turns are 3→2 and 2→3, and ~62% of its person-shifts involve the second person, against ~40%
for prose and sajʿ — but this is a *poetry-like* trait that lyric poetry (~69%) **exceeds**, and it sits
below the 2σ bar against every baseline. So iltifāt behaves precisely like the refrain of Lens 2: a real,
artful, **localized** device, not an elevated corpus-wide bulk statistic. One decisive caveat keeps this
from being the last word: the detector is **referent-blind**, whereas true iltifāt requires the shift to
be *referent-constant*; a referent-blind rate conflates ordinary topic-change with genuine iltifāt, and
that confound — not the device's absence — is the likeliest reason no bulk signal appears. The honest
completion needs a gold morphological tagger plus a coreference layer (§13). (EVIDENCE #40.)

---

## 10. Lens 8 — Morphological-template (*wazn*) distribution

**Concept.** Arabic is a templatic language: a consonantal *root* is poured into a *wazn* (pattern) to
make a word — the root k-t-b yields *kataba* (wrote), *kātib* (writer), *maktūb* (written), *kitāb* (book).
The distribution over these derivational templates — verb forms I–X, the participles, the intensive
"attribute" patterns (*faʿīl*, *faʿʿāl*: رَحِيم، غَفَّار) — is a stylistic fingerprint, and the Qur'an's
density of divine-attribute patterns at the verse-end is a natural place to look for one.

**What it measures.** Each content word is sorted, from its de-diacritized skeleton, into a coarse
derivational bucket (form X *istafʿala*, form VII *infaʿala*, the *mu-* participles, form IV *afʿala*,
active participle *fāʿil*, intensive *faʿīl/faʿūl*, broken plural, bare triliteral, other). Over equal-N
word windows we compute the template histogram and score its **JS-divergence from the ordinary-Arabic
histogram**, plus per-bucket rates — against ≥2 tokenizations and a permutation gate.

**A Qur'anic case.** Hear the close of countless āyāt: عَزِيزٌ حَكِيمٌ ، غَفُورٌ رَحِيمٌ ، سَمِيعٌ بَصِيرٌ —
paired *faʿīl* attributes, an intensive-adjective pattern used with unusual density. If any wazn signature
is Qur'an-distinctive, this clustering of *ṣiyaġ al-mubālaġa* (intensive patterns) is the candidate.

**What we found.** **Register-level — and exactly matched by a poetry master.** The Qur'an's template
distribution sits ~+1σ from ordinary prose (JS-divergence), stable across two tokenizations — but
Mutanabbi's poetry sits at the *same* +1σ, so the divergence is genre-level, not Qur'an-specific, and it
is below the 2σ bar. The one >2σ per-bucket cell (fewer bare four-letter *fāʿil* shapes) is
negative-direction and an artifact of classifier granularity (Qur'anic active participles mostly appear
in plural/derived forms that fall in other buckets), not a real avoidance. So *wazn*, like most lenses,
is a register property the Qur'an shares with masters, not a fingerprint. (EVIDENCE #41.)

---

## 11. Lens 9 — Intra-textual narrative recurrence

**Concept.** The Qur'an's most visible large-scale habit is **re-telling**: the story of Mūsā returns in
al-Baqara, al-Aʿrāf, Ṭā-Hā, al-Qaṣaṣ and more; Nūḥ, Ādam, and the punished nations recur across distant
sūrahs — never quite verbatim, always *re-voiced with variation*. This is the narrative correlate of the
*mathānī* (the "oft-repeated"). The question: does the Qur'an show **long-range passage recurrence** —
the same content returning across a great distance — beyond what ordinary Arabic, poetry, or sajʿ do?

**What it measures.** Text is cut into 50-content-word passages; we take their TF-IDF cosine similarities
and ask whether the *far-apart* pairs (separated by a large gap) have a **heavy upper tail** above the
far-pair median — a few distant passages that spike in similarity, the signature of a retold episode
against an otherwise diverse background (which separates true recurrence from mere topical homogeneity).
Two controls make the test decisive: an **equal passage count** per corpus (bootstrap subsampling, to
neutralize the Qur'an's size advantage), a **word-shuffle null** (shuffle all content words and re-chunk:
this preserves the Qur'an's repetitive *vocabulary* but destroys passage-level co-occurrence, so the
residual is recurrence *beyond* mere lexical repetition), and a **verbatim exclusion** (drop near-identical
pairs, so the signal cannot be the refrains of Lens 2).

**A Qur'anic case.** Set Mūsā-before-Pharaoh in al-Aʿrāf 7 beside the same confrontation in Ṭā-Hā 20 and
al-Shuʿarāʾ 26: the staff, the sorcerers, the divine reassurance recur — same lexical-semantic core,
re-ordered and re-weighted each time. No single āyah is copied; the *passage* returns. That is exactly the
0.5–0.9-similarity "far twin" the detector is built to find.

**What we found.** **The one breakthrough of the whole sweep.** This is the one single axis to place the
Qur'an clearly into the 2σ neighbourhood beyond ordinary Arabic: passage-recurrence excess, after the
word-shuffle control, is **~+3σ above ordinary prose** (corrected in #43 from a bug-inflated +3.5–4σ;
range +2.3–4.0 across passage-size, quantile, gap and seed; ordinary residual ≈0 — ordinary narrative does
not return to itself at long range), and it *survives verbatim exclusion* essentially unchanged (the
recurrence lives in the 0.5–0.9 similarity band, not in copies) — so it is genuine **varied retelling**,
not refrain. Two honest qualifications keep it in proportion. First, it is not a *new* axis so much as the
project's central **structured-repetition** signature finally measured at the right grain: the repetition
lens (Lens 1) read only ~+1σ as a bulk rate; the same craft, seen as long-range varied passage-recurrence
with the proper null, reads ~+3σ. Second, it is not unique in *kind*: poetry also clears the bar (+2σ —
Mutanabbi reuses figures and themes across the dīwān); the Qur'an simply **maximizes** a recurrence-genre
trait, by a clear margin. (Baseline magnitudes rest on small passage counts and are provisional.)
(EVIDENCE #42; magnitude **corrected to ~+3σ** in #43 after a tokenization bug — see the note below.)

A correction worth stating plainly, because the program's own rules demand it. While building the
variation profile (EVIDENCE #43) we found that Lens 9's pipeline had been tokenizing the *diacritized*
Qur'an by splitting on the word-regex *before* stripping the ḥarakāt — shattering each word into sub-word
fragments, while the plain-text comparators stayed whole. That asymmetry **inflated** the headline. With
the fix (normalize first, then split — yielding the intended 77.7k real words), the recurrence excess
**survives but settles at ~+3σ** vs ordinary Arabic (range +2.3–4.0 across passage-size, quantile, gap and
seed; word-shuffle-controlled; surviving a second, rasm-character tokenization), with poetry still ~+2σ.
The axis still crosses into the 2σ neighbourhood and remains the program's one structural distinctive — it
is simply more modest than first reported. The variation profile then *characterizes* it: the same figures
recur across vast spans (Mūsā across 32 sūrahs, Ibrāhīm 22, Nūḥ 21), yet the retellings keep verbatim runs
short (~2 tokens) and word-order heavily re-sequenced — recurrence carried by **re-expression, not
copying**. "The same story, told differently each time."

---

## 12. Lens 10 — Discourse macrostructure: the rhythm of *genres*

The nine prior lenses each read one *layer* of language. The tenth reads the *arrangement of registers*:
a sūrah is famous for moving, sometimes abruptly, between an oath, a narrative of past prophets, a scene
of the Judgment, a direct address to the listener, and a flat theological assertion. The hypothesis is
that the Qur'an's signature might live not in any single move but in how it *sequences* them — a
macro-rhythm of genres that ordinary prose, poetry and *sajʿ* (which tend to hold one register) do not
share. This is the cleanest lens to compute from bare text: no parser is needed, only a tagger that labels
each unit by its dominant *speech-act move* and a statistic on the resulting sequence.

**Anatomy.** Each unit (an āyah for the Qur'an; a clause for the comparators) is tagged with one of six
moves — *oath, address/command, narrative, judgment/eschatology, interrogation, assertion* — by
general-Arabic lexical cues applied identically to every corpus. The structural question is then put the
way Lens 9 put recurrence: compare the real move-sequence to a **reshuffle of its own labels**, so that
mere base-rate differences in how often each move appears cancel out, and only genuine *sequencing*
survives. Two statistics carry it — the **switch rate** (how often adjacent units change move) and the
**transition mut
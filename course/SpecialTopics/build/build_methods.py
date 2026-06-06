# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/SpecialTopics/build")
from _dochelper import newdoc,P,H
T=True; F=False
# entries: (week, order_in_week, "Week label", "title", [(bold_label, text), ...])
E=[]
def add(week,ow,wk,title,body): E.append((week,ow,wk,title,body))

add(1,0,"Week 1 (frequency)","إنذار (warning) vs تبشير (glad tidings)",[
 ("Method. ","Surface-form sense-filtering of two polysemous roots: بشر = glad-tidings vs human/mortal; نذر = warn vs vow. Count true-warning vs true-tidings ayahs; the messenger's ROLE; pairing rate and order; and the agnostic verb بشّر used for punishment."),
 ("Data. ","Warning = 113 ayahs; glad-tidings = 91, of which 9 announce punishment → net-glad ≈ 82. ROLE: warner 41 vs herald 12 (~3.4×). Shared-ayah 21 times; explicit بشيرًا ونذيرًا doublet rare (5:19, 35:24), tidings named first. Discards: human bashar 28; vow nadhr 3."),
 ("Verdict (scoped). ","Leaning WARNING — modestly in distribution (≈1.24×; ≈1.38× net of irony) and strongly as a ROLE. The either/or is half wrong: the corpus binds the two and leads the pairing with tidings — warning is the volume, mercy the framing."),
 ("Limitation. ","Sense-field and punishment-field membership are transparent lexical choices. The key control — not counting agnostic بشّر as “good news” — keeps the tidings figure honest."),
])
add(1,1,"Week 1 (frequency & address)","who does the Qur'an address?",[
 ("Method. ","Root + surface + morphology together: separate the NOUN of a group (المؤمنون, a category) from the VERBAL phrase (الذين آمنوا, an act); separate MENTION from ADDRESS (vocative يا أيها …); track the speech frame قُل vs قالوا."),
 ("Data. ","Believers: noun 224 + verbal 219; disbelievers: noun 159 + verbal 152 — each ~50/50 identity vs act. الناس named 241×. Vocative “O…!”: believers 89, mankind 20, Prophet 13, Banū Isrāʾīl 6. قُل (Say!) 379; قالوا (they said) 314."),
 ("Verdict (scoped). ","Primary addressee = the believing community (89 vocatives) inside a universal frame (الناس named 241×, called 20×); a scripted dialogue (Say! 379 vs they-said 314), not a monologue. Groups named as both fixed identity and ongoing act."),
 ("Limitation. ","Mention ≠ address (الناس 241 vs 20). Noun/verbal split is a principled morphological choice — collapsing them erases the identity-vs-act distinction."),
])
add(2,0,"Week 2 (distribution)","muṣḥaf order vs revelation order",[
 ("Method. ","Use the revelation-order index (col 12) for every sūra; correlate it with muṣḥaf position (1–114) and sūra length; bin the muṣḥaf into quarters; read off landmark sūras."),
 ("Data. ","corr(muṣḥaf#, revelation#) = −0.41. Avg length by quarter: Q1 119 → Q2 61 → Q3 30 → Q4 11 ayahs. Q4 avg revelation-rank 29 vs ~67 elsewhere. al-ʿAlaq revealed 1st at position 96; al-Tawba revealed 114th at position 9; al-Fātiḥa #1 revealed 5th; al-Baqara #2 revealed 87th (longest, 286)."),
 ("Verdict (scoped). ","Non-chronological, graded by descending length, clustering short early-Meccan sūras at the end. Interpretation (historical): tradition holds the arrangement was prophet-directed and liturgical — thematic, not biographical. Data shows the shape; the reason lies outside the text."),
 ("Limitation. ","Length is a tendency, not a law (al-Fātiḥa short yet first). Revelation order is a received dataset, not textually marked. We map WHAT, not WHY."),
])
add(3,0,"Week 3 (forms)","مُخلِص vs مُخلَص (active vs passive participle)",[
 ("Method. ","Read the ḥarakah on the lām from the vocalized text (col 11): kasra = active, fatḥa = passive. Number from the suffix; definiteness from the article. All 20 participle occurrences classified, then matched to their ayah's roots."),
 ("Data. ","ACTIVE = 11 (3 sing, all al-Zumar; 8 plur); 10/11 with دين; all indefinite. PASSIVE = 9 (1 sing, Moses 19:51; 8 plur); 8/9 with عبد; 7 definite. Passive referents: Joseph (12:24), Moses (19:51), the Iblīs exception (15:40, 38:83)."),
 ("Verdict (scoped). ","Active↔religion/indefinite/human-act; passive↔servants/definite/divine-election. The human strives as مُخلِص; being made مُخلَص is God's to give, mirroring يُزكّيهم. One root holds both halves of the doer→grace synthesis."),
 ("Limitation. ","The kasra/fatḥa is the Ḥafṣ reading; 12:24, 15:40, the al-Ṣāffāt series, 38:83, 19:51 are known qirāʾāt variant points. A property of one reading (Lesson #9)."),
])
add(3,1,"Week 3 (forms)","دين vs إسلام vs قرآن",[
 ("Method. ","Sense-filter three polysemous roots (دين = religion / Day-of-Judgment / debt; سلم = Islam / peace / Solomon; قرء = Qur’an / recite / periods), then test pairwise ayah-level co-occurrence and each word's collocates."),
 ("Data. ","دين senses: religion 72, Judgment 13, debt 2. Shared ayahs: دين+إسلام = 7 (3:19, 5:3, 3:85); دين+قرآن = 0; إسلام+قرآن = 0. قرآن pairs with كتاب 10, nazzala 13, dhikr 11."),
 ("Verdict (scoped). ","دين = genus (way / Reckoning / debt); إسلام = species (the accepted دين); قرآن = the Book that conveys it. دين ⊇ إسلام; قرآن is neither, the vehicle."),
 ("Limitation. ","Zero co-occurrence is blunt, but the corpus never lexically equates قرآن with the religion and reserves the identity for دين↔إسلام."),
])
add(9,0,"Week 9 (interpretation)","does Islam rule by the sword or by peace?",[
 ("Principle. ","The exact word may be absent while the concept is present — so we test the concept-field, not a single lexeme."),
 ("Method. ","Sense-filter the war-field (قتل = mostly kill/murder vs combat qitāl; حرب; جهاد) and the clemency-field (سلم also = Islam/Solomon; صلح mostly = righteous deeds). Count combat-specific forms; weigh against the conditions; read command verses in context."),
 ("Data. ","سيف (sword) = 0 occurrences. قتل root: 104 killing/murder vs 66 combat (qitāl). حرب = 11. Conditioning verses: 2:190 (defensive), 8:61 (incline to peace), 2:256 (no compulsion), 60:8 (justice to non-combatants)."),
 ("Verdict (scoped). ","Neither slogan holds. The sword has no lexical footprint; combat is real but a hedged minority — defensive, bounded, suspended on the enemy's peace, belief left free. Permission to fight inside a default of peace."),
 ("Limitation. ","Sense-field boundaries are lexical choices; conditionality is read from context. Raw root totals would mislead either way — the control is counting forms and reading verses."),
])
add(10,0,"Week 10 (forms)","غفر — what kind of forgiveness?",[
 ("Method. ","Tally every غفر surface form (col 9); separate Divine-Name intensives from verbs; test غفر's ayah-mates (sin? mercy? garden?). Root sense is concrete: مِغْفَر = a helmet that covers."),
 ("Data. ","Forms: Ghafūr 71, verbs 54, مغفرة 28, istighfār 37, Ghaffār only 4. Collocation: غفر+رحمة 91, غفر+ذنب 19, غفر+جنّة 9 (e.g. 3:133)."),
 ("Verdict (scoped). ","Primary sense = COVERING/erasing a fault (named on sin, twinned with mercy). Elevation is downstream and consequential, not lexical. The “status promotion” reading imports the destination into the word."),
])
add(10,1,"Week 10 (forms)","غفّار vs توّاب, and why “…إنه كان توّابا” (110:3)",[
 ("Method. ","Collect every occurrence of each intensive Name; record its paired Name and its ayah's roots. غفر = cover (unilateral); توب = turn/return (bilateral). Read 110:3 in context (victory; people entering “in crowds”)."),
 ("Data. ","Ghaffār = 4; pairs with al-ʿAzīz 3× (38:66, 39:5, 40:42); about sin (غفر+ذنب 19). Tawwāb = 8; pairs with al-Raḥīm 6× (2:37, 2:54, 9:104…); bilateral (9:118); توب+عبد 5, توب+ذنب 2."),
 ("Verdict (scoped). ","110:3 commands استغفار (seek covering, from غفر) yet names God توّاب (the ever-Returning). غفّار would narrow the moment to sin-erasure; توّاب fits a scene about return and a restored bond at the mission's end."),
 ("Limitation. ","A reading of placement and collocation, not a proof; the company each Name keeps (might vs mercy) is computed. The ـابا cadence is a formal echo, not the cause."),
])

add(3,2,"Week 3 (forms)","verb-as-act vs noun-as-state (آمنوا/مؤمن, صالح/مصلح)",[
 ("Method. ","Count the VERBAL phrase (الذين آمنوا, an act/journey) apart from the NOUN (المؤمنون, a settled trait); the intensive (كفّار) apart from the plain (كافر); and for صلح separate four forms — الصالحات (deeds), صالح (a righteous person), مصلح (an active reformer), إصلاح (reconciliation)."),
 ("Data. ","Faith: verbal 219 vs noun 224. Disbelief: verbal 152 vs noun 135, intensive كفّار 26. صلح: deeds الصالحات 98, person صالح 38, reformer مصلح only 5. Proof verses: 49:14 (claim آمنّا rejected, “faith has not entered your hearts”); 11:117 (towns spared as مصلحون, not صالحون); 7:170 (reward of المصلحين)."),
 ("Verdict (scoped). ","The grammar carries the theology: the perfect verb marks an act/journey (49:14 distinguishes the verbal claim from instilled faith); salvation’s formula الذين آمنوا وعملوا الصالحات is built on sustained verbs; مصلح (making-good) outranks صالح (being-good) where a society’s fate is at stake."),
 ("Limitation. ","Counting the root صلح as one idea would merge four concepts; only form separation keeps them apart. For faith the verb/noun counts are near-equal — the point is that the corpus deploys BOTH deliberately, not which dominates."),
])

add(7,0,"Week 7 (themes & reach)","local, regional or global content?",[
 ("Method. ","Count ayahs naming markers in three analyst-defined tiers — GLOBAL (الناس, العالمين, heavens & earth, آدم); REGIONAL (Moses, Pharaoh, Abraham, Jesus, People of the Book); LOCAL (sacred House, ʿĀd & Thamūd, Arabic tongue, Mecca, Quraysh) — via the vocalized text, then compare tiers."),
 ("Data. ","GLOBAL: mankind 179, the worlds 61, heavens & earth 133, Adam 30. REGIONAL: Moses 131, Pharaoh 67, Abraham 63, Jesus/Messiah 31, People of the Book 31. LOCAL: sacred House 17, ʿĀd 32, Thamūd 25, Arabic tongue 11, Mecca ~3, Quraysh 1."),
 ("Verdict (scoped). ","All three scales at once: a global address, a narrative carried by the shared Abrahamic/Near-East past (by far the densest — Moses rivals “mankind”), and a local Ḥijāz treated as stage, not subject. The particular is a doorway to the universal."),
 ("Limitation. ","Name-mention proxies REACH, not emphasis; proper-name normalization is imperfect; the local/regional/global tiers are the analyst's, not a Qur'anic category. The asymmetry (Moses 131 vs Mecca ~3) is nonetheless robust."),
])

add(2,1,"Week 2 (distribution)","what defines a Sūra and an Ayah?",[
 ("Method. ","Count ayahs per sūra (floor/ceiling/distribution) and root-tokens per ayah (shortest = disjointed letters; longest = 2:282); ask whether length DEFINES the units or only corroborates a marked boundary."),
 ("Data. ","Sūra: 3–286 ayahs (floor al-Kawthar/al-ʿAsr/an-Nasr = 3; ceiling al-Baqara = 286; median 39). Ayah: 1–84 root-tokens (median 7); الم and مدهامتان (55:64) = 1 token; the debt verse 2:282 = 84 (the only 61+). 769 ayahs have ≤2 tokens."),
 ("Verdict (scoped). ","Both units have measurable ranges that corroborate the anchors, but length defines neither. The units are MARKED — sūras by name & basmala, ayahs by received verse-stops; the disjointed letters (الم as a whole ayah) prove the marking precedes length, grammar, even meaning."),
 ("Limitation. ","Length corroborates, not defines; the boundaries are received (narrated/recitational), not computed — mirroring the muṣḥaf-order limit."),
])
add(9,1,"Week 9 (interpretation)","equity — ECONOMIC standing",[
 ("Method. ","Gather verses assigning women financial entitlements; report what each fixes; separate the datum from the equity verdict."),
 ("Data. ","Inheritance share guaranteed (4:7, “men a share… and women a share”); dowry is the woman’s own (4:4); earnings retained by the earner (4:32)."),
 ("Verdict (scoped). ","Computed: the corpus establishes women’s independent financial personhood. Whether the overall system is “equal” is interpretive; financial agency is stated plainly."),
 ("Limitation. ","Adequacy/“equality” is debated, not settled by citation; pre-Islamic context is interpretation, not data."),
])
add(9,2,"Week 9 (interpretation)","equity — SOCIAL & SPIRITUAL standing",[
 ("Method. ","Read verses on origin, reward, and mutual standing at face value; mark parity that is stated vs interpreted; keep moral standing apart from role."),
 ("Data. ","Same origin (49:13, 4:1); same reward (33:35’s ten matched pairs; “male or female” formula ×4, e.g. 3:195); mutual guardianship (9:71)."),
 ("Verdict (scoped). ","Computed: in origin, agency, and reward the text states parity explicitly and repeatedly — moral/spiritual standing is symmetric on its face. Role/legal differentiation is a distinct question."),
 ("Limitation. ","Face-value parity in reward/origin is strong; role “equality” is contested and not decided by these verses. Registers kept apart."),
])
add(9,3,"Week 9 (interpretation)","equity — INHERITANCE",[
 ("Method. ","Read 4:7, 4:11, 4:12, 4:176; report shares by heir-configuration, not one ratio; separate the fixed datum from the equity verdict."),
 ("Data. ","Women’s inheritance fixed as a right (4:7); the 2:1 holds in the parents→children case (4:11) but not universally — uterine siblings inherit equally (4:12); other parent/spouse shares vary."),
 ("Verdict (scoped). ","Computed: a fixed, case-specific schedule (not a blanket “half”). Equity is the interpretive crux — net-parity readings pair the male’s larger share with his maintenance duty; others read inequality. Numbers alone do not decide."),
 ("Limitation. ","Quoting only 4:11, or only the equal cases, are mirror-image cherry-picks (cf. Closer Look #9). The honest datum is the full schedule plus the maintenance asymmetry."),
])
add(9,4,"Week 9 (interpretation)","equity — TESTIMONY",[
 ("Method. ","Compare testimony verses across contexts — debt documentation (2:282) vs liʿān (24:6–9); read the weight each assigns; let the variation carry the finding."),
 ("Data. ","Debt: two women for one man (2:282). Liʿān: each spouse swears four oaths and HER four avert the penalty (24:6–9) — one-to-one. Weight 0.5 vs 1.0 by context."),
 ("Verdict (scoped). ","Computed: testimony weight is context-dependent, not uniform; “half” is not a general rule. 2:282 concerns record-keeping of an unfamiliar commercial transaction, not a courtroom scale of worth."),
 ("Limitation. ","Universalizing 2:282 ignores liʿān; citing only liʿān ignores the debt asymmetry. The datum is the variation; the reason for it is interpretation."),
])

add(4,0,"Week 4 (co-occurrence)","wealth & children — blessing or trial?",[
 ("Method. ","Find ayahs naming both مال and أولاد; read what is predicated of the pair; separate the recurring pairing from the moral lesson."),
 ("Data. ","Each ~80×; co-occur as a fixed pair 16×. Where paired, cast as trial/fitna (8:28, 64:15), adornment of worldly life (18:46), or that “will not avail against God” (3:10) — never as a token of favour."),
 ("Verdict (scoped). ","The pair is a stable lexical unit consistently demoted from reward to test — the durative-conditional logic (what you DO with them decides)."),
 ("Limitation. ","The pairing is robust; the “trial” framing is a tendency in the paired usage, not a blanket valuation — some ayahs call children a gift."),
])
add(7,1,"Week 7 (themes)","one word for sunrise and scripture (آية)",[
 ("Method. ","The sign-root (آية, 353×) tagged where it co-occurs with NATURE roots vs SCRIPTURE roots; compare registers."),
 ("Data. ","Explicit co-occurrence: scripture 137, nature 35, general 181. 41:53 fuses them: “Our signs in the horizons and in themselves.”"),
 ("Verdict (scoped). ","آية spans both — leaning verbally to recited signs (137 vs 35) while naming nature with the same term; the conflation is deliberate (book and world as one signage)."),
 ("Limitation. ","Co-occurrence captures explicit pairing only; the tiers are the analyst's. The dual use of one word is the robust datum."),
])
add(9,5,"Week 9 (interpretation)","does the Qur'an abrogate itself? (نسخ)",[
 ("Method. ","Every occurrence of root نسخ read in context; “abrogate” sense separated from “copy/transcribe”; check whether the text names which verse cancels which."),
 ("Data. ","Only 4 occurrences. Two = abrogate (2:106, 22:52); two = copy (نسخة 7:154, نستنسخ 45:29). No verse-cancels-verse case is ever named."),
 ("Verdict (scoped). ","Intra-Qur'anic abrogation rests on ~2 verses and is a juristic construct on a thin lexical base — not a self-declared feature."),
 ("Limitation. ","Does not settle whether abrogation is true; 2:106's “sign” may mean a miracle or prior scripture, itself a reading."),
])
add(9,6,"Week 9 (interpretation)","is intercession denied or affirmed? (شفاعة)",[
 ("Method. ","Read the شفع verses (26×) by type: independent intercession (denied) vs God-permitted (affirmed); let the qualifier “by His leave” reconcile them."),
 ("Data. ","Denied as independent (2:48); only by His leave (2:255); belongs wholly to God (39:44)."),
 ("Verdict (scoped). ","No contradiction — one conditioned rule: intercession is denied as an autonomous power, affirmed only as God-permitted."),
 ("Limitation. ","Who in fact receives that leave is the interpretive question. Reading the negations absolutely (ignoring “except by His leave”) is the classic audit failure (Closer Look #9)."),
])
add(10,2,"Week 10 (forms)","الله / رب / الرحمن / إله — which Name does which work?",[
 ("Method. ","Count the principal divine words; read each grammatically (proper name? possessed? negated?); separate frequency from role."),
 ("Data. ","الله 2698 (proper name; never pluralised); رب ≈972 (relational, overwhelmingly possessed — your/our/my Lord); الرحمن 57 (signature attribute, Basmala); إله = the generic, mostly NEGATED (“no إله but Allah”)."),
 ("Verdict (scoped). ","Not interchangeable — they divide labour: identity (الله), relationship (رب), mercy-attribute (الرحمن), negated generic (إله)."),
 ("Limitation. ","Lemma counting flattens رب's possessive forms; the relational point is read from usage. “Roles” are a descriptive gloss, not a Qur'anic taxonomy."),
])

add(4,1,"Week 4 (co-occurrence)","one light, many darknesses (نور / ظلمات)",[
 ("Method. ","Count every surface form of each, tagging singular vs plural; weigh light against darkness overall."),
 ("Data. ","نور 43, ALWAYS singular (أنوار = 0); ظلمات 23, ALWAYS plural (singular ظلمة = 0). Light outnumbers darkness ~2:1."),
 ("Verdict (scoped). ","Zero exceptions: a single نور vs plural ظلمات, light leading ~2:1. Interpretation: the grammar encodes a creed — truth is ONE, error MANY."),
 ("Limitation. ","Morphology is a hard datum (0 counter-examples); “one truth, many errors” is the labelled reading. نار (fire) is a different sense, excluded."),
])
add(5,0,"Week 5 (lift & support)","which Divine-Name pairs truly bond? (count vs lift)",[
 ("Method. ","For each Name-pair compute shared-ayah COUNT and LIFT (joint ÷ expected); read them together."),
 ("Data. ","ʿAlīm+Ḥakīm 71 v / lift 3.2×; Ghafūr+Raḥīm 91 / 9.0×; ʿAzīz+Ḥakīm 49 / 13.8×; Ghafūr+Ḥalīm 9 / 13.9×."),
 ("Verdict (scoped). ","The most FREQUENT pair (ʿAlīm+Ḥakīm) is among the WEAKEST by lift (ʿilm appears 728×); the tightest bond is Ghafūr+Ḥalīm (13.9×, rare); the gold standard ʿAzīz+Ḥakīm has strong lift AND support."),
 ("Limitation. ","High lift on low count (Ghafūr+Ḥalīm, 9 v) is thin support — read count, lift, and stability together (ties to Week 8)."),
])
add(6,0,"Week 6 (direction)","“out of darkness into light” — a one-way arrow",[
 ("Method. ","Count the directional phrase both ways (الظلمات→النور vs النور→الظلمات) and record the SUBJECT of each."),
 ("Data. ","dark→light 7×, light→dark 1×. God is the subject of the 7; the lone reversal (2:257) is the ṭāghūt."),
 ("Verdict (scoped). ","Salvation has a fixed direction — out of the plural darknesses into the single light — and God is its agent; the one reversal names the false patron. Direction encodes agency."),
 ("Limitation. ","Small support (eight directional phrases); the 7:1 asymmetry is clear but rests on few verses. “Direction = agency” is the labelled reading."),
])
add(8,0,"Week 8 (motifs & support)","the hypocrite syndrome — and its support (نفاق)",[
 ("Method. ","Sense-filter نفق to the munāfiq forms (not “spending”); count pairwise links and the full trio; read each one's verse-support."),
 ("Data. ","قلب+مرض 12; نفق+قلب 9; نفق+كذب 3; نفق+خدع 1. Full trio (munāfiq + heart + disease) = 3 verses."),
 ("Verdict (scoped). ","A robust PAIRWISE syndrome (diseased heart, deception) but a thin TRIO (3 v). The portrait is real; quoting it as a tight three-part formula overstates a small base."),
 ("Limitation. ","نفق is polysemous (only munāfiq forms counted); 3 supporting verses means leave-one-out would shake the trio — the Week-8 caution."),
])

add(9,7,"Week 9 (interpretation · labelled analogy)","istinsākh & genomic transcription",[
 ("Status. ","A LABELLED ANALOGY (reflection), not a data claim or a “scientific miracle.” The computed anchor is the recording-of-deeds verses; the genomics parallel is an explicitly-flagged heuristic."),
 ("Anchor (computed). ","45:29 “We were transcribing (نستنسخ) what you did” — root نسخ = transcribe/record (sense-checked vs the abrogation sense). Recording field: 50:18 (a watcher by every word), 78:29 (all enumerated in a record), 18:49 (nothing small or great omitted), 17:13–14, 99:7 (an atom’s weight)."),
 ("Parallels (labelled). ","Faithful copying; deferred expression (record now, outcome later); total fidelity. Each pairs a mainstream genomics fact with a verse — the parallel, not an identity."),
 ("Limits / no overclaim. ","The analogy breaks where it matters: free deeds author the template (interpretation); the “phenotype” expresses in another realm; moral not mechanistic; error-free vs mutation-prone. Value is pedagogical, NOT evidential — the Qur’an is not claimed to describe DNA."),
])

doc=newdoc("RootCourse — Special Topics · Methods & Data (peer-review record)")
P(doc,[("RootCourse — Special Topics: Methods & Data",T)],size=18)
P(doc,[("A standing, peer-reviewable record (companion to the ten Closer Looks), sorted by home week. Every value is computed from Book6.xlsx; surface forms and vocalization are read from the aligned root/token columns and the voweled text (col 11). Interpretation is labelled, never presented as computed fact.",F)],size=10.5)
E.sort(key=lambda e:(e[0],e[1]))
for n,(wk_no,ow,wk,title,body) in enumerate(E,1):
    H(doc,f"{n} · {wk} — {title}")
    for lbl,txt in body: P(doc,[(lbl,T),(txt,F)])
doc.save("/sessions/kind-compassionate-feynman/mnt/RootCourse/SpecialTopics/SpecialTopics_Methods.docx")
print("methods doc rebuilt, sorted by week:", [(e[0],e[3][:18]) for e in E])

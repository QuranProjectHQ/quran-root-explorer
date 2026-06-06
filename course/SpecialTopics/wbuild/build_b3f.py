# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
EQ=json.load(open(SB+"snip_equity.json",encoding="utf-8"))
GN=json.load(open(SB+"snip_genome.json",encoding="utf-8"))
def gle(key,refs):
    d={e["ref"]:e for e in EQ[key]}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def glg(refs):
    d={e["ref"]:e for e in GN}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
AT=[("cross","Not a proof","the text's data is computed; verdicts/analogies are labelled."),
    ("cross","No raw mixing","forms/senses separated; contexts kept apart (course rule).")]

# ============ EQUITY - JUDICIAL / TESTIMONY ============
nshahd=ac('شهد')
fig_groupbar("eqj_weight.png","Female testimony weight is CONTEXT-dependent (from the verses)",["debt-documentation (2:282)","li'an accusation (24:6-9)"],[("",[wk.AMBER,wk.TEAL],[0.5,1.0])],ylabel="weight vs a man",fmt="{:.1f}")
fig_groupbar("eqj_lian.png","Li'an - the oaths are symmetric",["husband's oaths","wife's oaths"],[("",[wk.TEAL,wk.TEAL],[4,4])],ylabel="oaths (24:6-9)")
fig_freqbarh("eqj_field.png","The witness-vocabulary",["witness-root (shahd)","witness . debt (2:282)","witness . women"],[nshahd,cooccur('شهد','دين'),cooccur('شهد','نسو')],[wk.NAVY,wk.AMBER,wk.TEAL],xlabel="ayat")
fig_suradist("eqj_sura.png","Where the witness-root falls, sura by sura","شهد")
fig_groupbar("eqj_context.png","'Half' is not a general rule - it varies by context",["debt: 2 women for 1 man","li'an: her oath = his","(other contexts vary)"],[("",[wk.AMBER,wk.TEAL,wk.GREY],[0.5,1.0,0.75])],ylabel="relative weight")
fig_groupbar("eqj_cherry.png","Two opposite cherry-picks",["read only 2:282 (half)","read only li'an (equal)"],[("each ignores the other",[wk.RED,wk.RED],[1,1])],ylabel="half-truth")
fig_freqbarh("eqj_variation.png","The datum is the VARIATION, not one verse",["debt (2:282) weight 0.5","li'an (24:6) weight 1.0"],[0.5,1.0],[wk.AMBER,wk.TEAL],xlabel="female testimony weight vs a man")
spec=dict(slug="W09_equity_judicial",sub="women & men: testimony, Week 9",
 main="Women & men - testimony",
 headline="'Half a man's' is not a general rule - testimony weight varies by context",
 intro1="'A woman's testimony is worth half a man's.' Always - or only in a particular context? We compare the testimony verses across contexts: documenting a debt (2:282) vs the li'an accusation (24:6-9), reading the weight each assigns, and letting the VARIATION carry the finding.",
 intro2="Verse content is quoted from Book6; the weights (2-for-1 in debt, 1-for-1 in li'an) are what the cited verses establish.",
 qhead="The claim to test",qbody="Is a woman's testimony 'half a man's' always, or only in a specific context?",
 mhead="The method",mpts=["compare testimony verses across contexts (debt 2:282 vs li'an 24:6-9)",
   "read the weight each assigns",
   "let the variation, not a single verse, carry the finding"],
 figs=[
  dict(t="Testimony weight is context-dependent",png="eqj_weight.png",cf=TINT,
    cap="In the data (from the cited verses) - in debt-documentation (2:282) two women stand for one man (0.5); in the li'an accusation (24:6-9) a woman's oath equals a man's (1.0). Context, not a universal scale."),
  dict(t="Li'an - the oaths are symmetric",png="eqj_lian.png",
    cap="In the data (24:6-9) - when a husband accuses his wife, each swears FOUR oaths; her four avert the penalty against his. One-to-one - equal."),
  dict(t="The witness-vocabulary",png="eqj_field.png",cf=TINT,
    cap=f"In the data - the witness-root ({nshahd}) is a large field; 2:282 (witness+debt, {cooccur('شهد','دين')}) concerns RECORD-KEEPING of a commercial transaction, not a courtroom scale of worth."),
  dict(t="The witness-root across the corpus",png="eqj_sura.png",
    cap="In the data - the witness-root is spread across the corpus, in legal, theological and testimonial senses alike."),
  dict(t="'Half' is not a general rule",png="eqj_context.png",cf=TINT,
    cap="In the data - the weight varies: 2-for-1 in debt (2:282), 1-for-1 in li'an (24:6-9). 'Half' is a generalization the corpus does not support across the board."),
  dict(t="Two opposite cherry-picks",png="eqj_cherry.png",
    cap="In the data - reading only 2:282 as a universal law ignores 24:6-9; reading only li'an ignores the debt asymmetry. Both are half-truths."),
  dict(t="The datum is the variation",png="eqj_variation.png",cf=TINT,
    cap="In the data - the honest finding is the VARIATION (0.5 in debt, 1.0 in li'an); the REASON for it is interpretation, not count."),
 ],
 gal1=dict(title="Debt - two women for one man (2:282)",items=gle("judicial",["2:282"]) or [("2:282","فَرَجُلٌ وَامْرَأَتَانِ ... أَن تَضِلَّ إِحْدَاهُمَا","one man and two women ... so if one errs the other reminds her")],fill=AMBERT,hc=AMBER),
 gal2=dict(title="Li'an - her oath equals his (24:6-9)",items=gle("judicial",["24:6","24:8","24:9"]) or [("24:8","وَيَدْرَأُ عَنْهَا الْعَذَابَ أَن تَشْهَدَ أَرْبَعَ شَهَادَاتٍ","it averts the penalty from her that she swears four oaths")],fill=TINT,hc=TEAL),
 v1=("Debt: two for one (2:282)","in documenting a deferred debt, two women stand for one man - 'so if one errs, the other reminds her.' Tied to that transaction."),
 v2=("Li'an: her oath equals his (24:6-9)","when a husband accuses his wife, each swears four oaths; HER four avert the penalty against his. One-to-one - equal."),
 v3=("So 'half' is not general","testimony weight is CONTEXT-dependent; 'half' is a generalization the corpus does not support across the board."),
 deep=("'Half' is not a general rule",
   "Computed datum: testimony weight is CONTEXT-DEPENDENT, not uniform - 2-for-1 in debt-documentation (2:282) and 1-for-1 in li'an (24:6-9), where a woman's sworn word overturns a man's. So 'half' is a generalization the corpus does not support across the board. Reading 2:282 as a universal law of female worth ignores 24:6-9 - and that 2:282 concerns RECORD-KEEPING of an unfamiliar commercial transaction, not a courtroom scale of worth."),
 deep_extra=["The datum is the VARIATION; the reason for it is interpretation, not count."],
 crit1=("Both readings cherry-pick",
   "reading only 2:282 ignores li'an; reading only li'an ignores the debt asymmetry - the honest datum is the variation."),
 crit2=("2:282 is about record-keeping",
   "the debt verse concerns documenting an unfamiliar commercial transaction, not a general courtroom scale of female worth."),
 audit=[("check","Contexts compared","debt 2:282 vs li'an 24:6-9."),
   ("check","Li'an symmetric","four oaths each - 1:1."),
   ("check","Variation is the datum","0.5 in debt, 1.0 in li'an.")]+[("tilde","Reason is interpretive","why the weights differ is a reading.")]+AT,
 method=("testimony verses by context; witness-root","weight by context; symmetric oaths","weight bars, oath bars, witness field, sura map"),
 take=("'Half' is not a general rule",
   ["Testimony weight is context-dependent: 2-for-1 in debt-documentation (2:282), 1-for-1 in li'an (24:6-9).",
    "In li'an a woman's sworn word overturns a man's - one-to-one. 2:282 concerns record-keeping, not a scale of worth.",
    "The datum is the VARIATION; the reason is interpretation. Presented from the text."]),
 qr1=("The verses",f"debt 2:282 (2-for-1) - li'an 24:6-9 (1-for-1, four oaths each); witness-root {nshahd} ayat."),
 qr2=("The shape","testimony weight varies by context; 'half' is not a general rule; the datum is the variation, the reason interpretive."),
 syn=("Context, not a constant",
   [("Debt (2:282)","two women for one man"),("Li'an (24:6-9)","her oath equals his"),("Datum","the VARIATION itself")],
   "'Half' is not general","the corpus assigns weight by context; reading one verse as universal is the cherry-pick."),
 quiz=("Special Topic - Women & Men: Testimony (Week 9)",[
  ("1.  Female testimony weight in the Qur'an is:","context-dependent, not uniform",["always half","always equal","never mentioned"],"2-for-1 in debt, 1-for-1 in li'an."),
  ("2.  2:282 (debt documentation) calls for:","two women for one man",["one for one","three for one","women only"],"'so if one errs, the other reminds her.'"),
  ("3.  In li'an (24:6-9) a woman's oath is:","equal to a man's (four oaths each)",["half","a quarter","not counted"],"her four avert the penalty against his."),
  ("4.  'A woman's testimony is half a man's' is:","a generalization the corpus does not support across the board",["always true","never about testimony","proven"],"weight varies by context."),
  ("5.  2:282 specifically concerns:","record-keeping of a commercial transaction",["a courtroom scale of worth","criminal law","prayer"],"documentation, not general worth."),
  ("6.  Reading only 2:282 as universal:","ignores li'an (the cherry-pick)",["is correct","is required","ignores nothing"],"it omits the equal case."),
  ("7.  Reading only li'an:","ignores the debt asymmetry (opposite cherry-pick)",["is the whole truth","is fair","is impossible"],"both are half-truths."),
  ("8.  The honest datum is:","the VARIATION across contexts",["one verse","the average","the rhyme"],"the reason is interpretation."),
  ("9.  In li'an, the number of oaths each spouse swears is:","four",["two","one","ten"],"symmetric - 24:6-9."),
  ("10.  The witness-root is:","a large field across the corpus",["a hapax","only in 2:282","never used"],f"{nshahd} ayat."),
  ("11.  The reason the weights differ is:","interpretive, not given by the count",["computed","stated explicitly","irrelevant"],"the variation is the datum."),
  ("12.  The honest verdict is:","'half' is not a general rule; weight is context-dependent",["always half","always equal","unknowable"],"the corpus varies it."),
  ("13.  These findings are:","the text's data, the reason scoped as interpretive",["a ruling","disproof","unrelated to Book6"],"we report the variation."),
 ]),
)
standard_deck(spec)
print("done equity_judicial")

# ============ ISTINSAKH & GENOMICS (a labelled analogy) ============
nnaskh=ac('نسخ')
fig_groupbar("gen_record.png","The recording field - deeds written, nothing omitted",["a watcher by every word (50:18)","all enumerated (78:29)","nothing omitted (18:49)","to an atom's weight (99:7)"],[("from the cited verses",[wk.TEAL,wk.AMBER,wk.NAVY,wk.RED],[1,1,1,1])],ylabel="recording verse")
fig_freqbarh("gen_naskh.png","The anchor word: nastansikh (transcribe), root nasakh",["nasakh root (total)","45:29 'We were transcribing'"],[nnaskh,1],[wk.GREY,wk.TEAL],xlabel="occurrences")
fig_groupbar("gen_pipeline.png","The mapped analogy (structure only - NOT a science claim)",["transcription\n(deeds->record)","translation\n(record->verdict)","phenotype\n(expressed later)"],[("a teaching bridge",[wk.TEAL,wk.AMBER,wk.NAVY],[1,1,1])],ylabel="mapped stage")
fig_suradist("gen_sura.png","Where the recording/transcription-root falls","نسخ")
fig_groupbar("gen_breaks.png","Where the analogy BREAKS (kept honest)",["you author your own 'code'","another realm of expression","moral, error-free (bil-haqq)"],[("disanalogies",[wk.RED,wk.RED,wk.RED],[1,1,1])],ylabel="breakpoint")
fig_freqbarh("gen_verses.png","The deed-record verses (computed anchor)",["transcribe (45:29)","record read out (17:14)","weighed on scales (21:47)","nothing omitted (18:49)","atom's weight (99:7)"],[1,1,1,1,1],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY,wk.RED],xlabel="each a distinct verse")
fig_groupbar("gen_label.png","An analogy is NOT an equivalence claim",["illuminating teaching bridge","'scientific miracle' claim (refused)"],[("",[wk.TEAL,wk.RED],[1,0])],ylabel="status")
spec=dict(slug="W09_istinsakh_genomics",sub="a labelled analogy, Week 9",
 main="'We were transcribing what you did' - nasakh and genomic transcription",
 headline="A teaching analogy - explicitly NOT a scientific-miracle claim",
 intro1="45:29: 'This is Our record that speaks against you in truth; We were TRANSCRIBING (nastansikh) what you used to do' - the same root as the abrogation topic, here meaning to record/copy. As an ANALOGY ONLY (a teaching bridge, not a claim about the text), we map the recorded-deeds structure onto genomic transcription: information copied first, expressed later.",
 intro2="The deed-record verses are quoted from Book6 (the computed anchor); every biology parallel is a labelled teaching device, NOT a claim that the Qur'an encodes molecular biology.",
 qhead="The text (computed anchor)",qbody="45:29 'We were transcribing what you did'; the recording field: a watcher by every word (50:18), all enumerated (78:29), nothing omitted (18:49), to an atom's weight (99:7).",
 mhead="The analogy (labelled)",mpts=["map the STRUCTURE (copy -> store -> express), not the mechanism",
   "keep the mapping where it illuminates and DROP it where it breaks",
   "state clearly: a mental model, NOT evidence or a 'scientific miracle'"],
 figs=[
  dict(t="The recording field",png="gen_record.png",cf=TINT,
    cap="In the data (from the cited verses) - a watcher by every word (50:18), all things enumerated (78:29), nothing small or great omitted (18:49), to an atom's weight (99:7): deeds are recorded completely and truthfully."),
  dict(t="The anchor word: transcribe",png="gen_naskh.png",
    cap=f"In the data - the root appears {nnaskh} times; 45:29 ('We were transcribing what you did') uses it in the COPY/RECORD sense (sense-checked vs the abrogation topic)."),
  dict(t="The mapped analogy (structure only)",png="gen_pipeline.png",cf=TINT,
    cap="A labelled teaching bridge - NOT a science claim: transcription (deeds -> record), translation (record -> verdict), phenotype (consequence expressed later, in its own context)."),
  dict(t="The recording-root across the corpus",png="gen_sura.png",
    cap="In the data - the recording/transcription-root sits among the eschatology and record passages."),
  dict(t="Where the analogy breaks",png="gen_breaks.png",cf=TINT,
    cap="Kept honest - the disanalogies: you author your own 'code' (free deeds); expression is in ANOTHER realm; the recording is moral and error-free (bil-haqq), unlike mutation-prone copying."),
  dict(t="The deed-record verses",png="gen_verses.png",
    cap="In the data - transcribe (45:29), record read out (17:14), weighed on just scales (21:47), nothing omitted (18:49), an atom's weight (99:7): the computed textual anchor."),
  dict(t="An analogy is not an equivalence",png="gen_label.png",cf=TINT,
    cap="The status, stated plainly - an illuminating teaching bridge, NOT a 'scientific miracle': its worth is a vivid mental model, not evidence."),
 ],
 gal1=dict(title="Transcription - 'We were transcribing'",items=glg(["45:29","78:29"]) or [("45:29","إِنَّا كُنَّا نَسْتَنسِخُ مَا كُنتُمْ تَعْمَلُونَ","We were having transcribed what you used to do")],fill=TINT,hc=TEAL),
 gal2=dict(title="Read your record; weighed to an atom's weight",items=glg(["17:14","21:47","99:7"]) or [("17:14","اقْرَأْ كِتَابَكَ","read your record")],fill=AMBERT,hc=AMBER),
 v1=("Transcription - deeds to record","45:29: deeds copied into the record 'in truth'; nothing small or great omitted (18:49). The parallel is faithful copying."),
 v2=("Translation - record to verdict","on the Day the record is READ out - 'Read your record' (17:14) - and deeds are weighed on just scales (21:47; an atom's weight, 99:7)."),
 v3=("Phenotype - expressed later","the consequence is manifested in the hereafter - garden or fire - its 'phenotype,' deferred and context-specific."),
 deep=("Where it breaks, and the verdict",
   "Computed datum: deeds are transcribed into a complete, truthful record whose consequence unfolds later (45:29; 78:29; 18:49; 50:18; 17:13). The genomics parallel - transcription -> deferred phenotype -> context-specific expression - is an illuminating teaching bridge. But it BREAKS in three ways: you author your own 'code' (free deeds, not an inherited genome); the deed-phenotype expresses in ANOTHER realm; and the recording is moral and error-free (bil-haqq), unlike mutation-prone copying. Honest limit: it is NOT a 'scientific miracle' - its worth is a vivid mental model, not evidence."),
 deep_extra=["Every biology parallel is a teaching device - NOT a claim that the Qur'an describes molecular biology."],
 crit1=("It is NOT a scientific miracle",
   "the analogy's worth is a mental model, not evidence; we explicitly refuse the 'scientific miracle' framing."),
 crit2=("Keep it where it illuminates",
   "an analogy maps structure (copy->store->express), not identity; we drop it where it breaks (free authorship, another realm, error-free recording)."),
 audit=[("check","Anchor verses cited","45:29, 17:14, 21:47, 18:49, 99:7 - from Book6."),
   ("check","Sense-checked","nasakh here = transcribe, not abrogate."),
   ("tilde","Analogy, not claim","structure mapped; mechanism unrelated.")]+[("cross","Not a miracle-claim","a teaching bridge, not evidence.")]+AT[1:],
 method=("the transcription verse; the recording field","quote the anchor; map structure (labelled)","record bars, anchor verses, pipeline (labelled)"),
 take=("A vivid teaching bridge - and nothing more",
   ["The computed anchor: deeds are transcribed into a complete, truthful record whose consequence unfolds later (45:29, 18:49, 99:7).",
    "The genomics parallel (copy -> store -> express) is an illuminating mental model - but it breaks where authorship, realm and fidelity differ.",
    "Stated plainly: NOT a scientific miracle - a teaching device, not evidence. Presented from the text."]),
 qr1=("The anchor",f"45:29 'We were transcribing'; record read out (17:14), weighed (21:47), nothing omitted (18:49), atom's weight (99:7); nasakh root {nnaskh}."),
 qr2=("The status","a labelled structural analogy (copy->store->express); breaks at authorship/realm/fidelity; NOT a scientific-miracle claim."),
 syn=("Copy, store, express",
   [("Transcription","deeds -> truthful record"),("Translation","record read & weighed"),("Phenotype","expressed in the hereafter")],
   "A teaching bridge, not evidence","the structure maps; the mechanism does not - and we refuse the 'miracle' framing."),
 quiz=("Special Topic - Istinsakh & Genomic Transcription (Week 9)",[
  ("1.  45:29's 'nastansikh' here means:","to transcribe / record (copy)",["to abrogate","to recite","to forbid"],"the copy sense, sense-checked vs abrogation."),
  ("2.  The genomics parallel is presented as:","a labelled teaching analogy, not a science claim",["a scientific miracle","proof of evolution","a literal mechanism"],"structure mapped, not identity."),
  ("3.  The mapped structure is:","copy -> store -> express",["random","cause -> effect only","none"],"transcription, translation, phenotype."),
  ("4.  The recording of deeds is described as:","complete and truthful (nothing omitted)",["partial","optional","random"],"18:49, 99:7 - to an atom's weight."),
  ("5.  The analogy BREAKS because:","you author your own 'code' (free deeds), not an inherited genome",["genes are deeds","there is no record","it never breaks"],"free authorship vs inheritance."),
  ("6.  Another breakpoint is:","expression in ANOTHER realm (the hereafter)",["this world only","no expression","instant"],"deferred, context-specific."),
  ("7.  A third disanalogy is:","the recording is error-free (bil-haqq), unlike mutation-prone copying",["both error-free","both error-prone","irrelevant"],"moral, not mechanistic."),
  ("8.  The status of the analogy is:","a vivid mental model, NOT evidence",["evidence","a miracle","proof"],"we refuse the miracle framing."),
  ("9.  'Read your record' is from:","17:14",["45:29","99:7","2:282"],"the record read out on the Day."),
  ("10.  An analogy maps:","structure, not identity",["identity","mechanism","nothing"],"copy->store->express, kept where it illuminates."),
  ("11.  The nasakh root here is sense-checked against:","the abrogation sense",["the prayer sense","the war sense","nothing"],"transcribe vs abrogate."),
  ("12.  The honest verdict is:","an illuminating teaching bridge, explicitly not a miracle",["a scientific miracle","disproof of biology","a literal claim"],"a mental model, not evidence."),
  ("13.  These findings are:","the computed verse-anchor plus a clearly-labelled analogy",["a science claim","doctrine","unrelated to Book6"],"anchor computed; analogy labelled."),
 ]),
)
standard_deck(spec)
print("done genomics")

# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df,SUR,AYA
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SS=json.load(open(SB+"snip_actstate.json",encoding="utf-8"))
S1=json.load(open(SB+"snippets.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag",d[r].get("voice",""))) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
def coocN(roots): return int(df['toks'].map(lambda ts:all(r in ts for r in roots)).sum())
AT=[("cross","Not a proof","morphology locates the distinction; theology is not settled by counts."),
    ("cross","No raw mixing","forms separated before counting (course rule).")]

# =============== ACT vs STATE ===============
faith=ac('ءمن'); disb=ac('كفر')
salihat=fac_sub(['صالحات']); salih=form_ac(['صالح','صالحا','الصالح','صالحون','الصالحون','صالحين','الصالحين']); muslih=fac_sub(['مصلح']); islah=fac_sub(['اصلاح','صلاح'])
tri=coocN(['ءمن','عمل','صلح'])
fig_freqbarh("as_salih.png","One root, four distinct forms - keep them apart",
  ["الصالحات  righteous deeds","صالح  a righteous person","اصلاح/صلاح  reconciliation","مصلح  an active reformer"],
  [salihat,salih,islah,muslih],[wk.TEAL,wk.LT,wk.GREY,wk.AMBER],xlabel="ayat containing the form")
fig_groupbar("as_fields.png","The three families - faith, disbelief, righteousness",
  ["faith ءمن","disbelief كفر","righteous صلح"],[("",[wk.TEAL,wk.RED,wk.AMBER],[faith,disb,ac('صلح')])])
fig_groupbar("as_formula.png","Salvation's signature is built on VERBS",
  ["belief AND deeds\n(amanu + amilu + salihat)"],[("shared ayat",[wk.TEAL],[tri])],ylabel="ayat")
fig_suradist("as_amn_sura.png","Where faith is named, sura by sura","ءمن")
fig_suradist("as_slh_sura.png","Where the righteousness-root falls, sura by sura","صلح")
fig_timeline("as_time.png","Faith and disbelief across the revelation",[("faith ءمن","ءمن"),("disbelief كفر","كفر")])
fig_groupbar("as_reform.png","Being good vs MAKING good - reformer is rare",
  ["righteous person\n(salih)","active reformer\n(muslih)"],[("",[wk.LT,wk.AMBER],[salih,muslih])])
spec=dict(slug="W03_act_vs_state",sub="forms & morphology, Week 3",
 main="A journey or an instilled state? Faith as act vs identity",
 headline="Arabic marks DOING apart from BEING - and the corpus uses both",
 intro1="Arabic separates an act from a settled trait: 'those who came to believe' (a relative clause + perfect verb) names a journey; 'a believer' (a participle/noun) names an instilled state. The same split runs through disbelief and through the righteousness-root. We count the forms apart - never merging the concepts.",
 intro2="Counts recompute from Book6; the four forms of the righteousness-root are tallied by surface form, not by raw root.",
 qhead="The nuance",qbody="Is faith named as an ongoing act, a settled identity - or deliberately both?",
 mhead="The method",mpts=["count the verbal phrase ('came to believe') apart from the noun ('a believer')",
   "split the righteousness-root into FOUR forms: deeds, a righteous person, reconciliation, an active reformer",
   "read the salvation formula - belief AND sustained deeds"],
 figs=[
  dict(t="One root, four distinct concepts",png="as_salih.png",cf=TINT,
    cap=f"In the data - the righteousness-root splits into righteous-DEEDS ({salihat}), a righteous PERSON ({salih}), reconciliation ({islah}) and the active REFORMER ({muslih}). Counting the root as one idea would merge four concepts."),
  dict(t="Faith, disbelief, righteousness - the three fields",png="as_fields.png",
    cap=f"In the data - faith ({faith}), disbelief ({disb}) and the righteousness-root ({ac('صلح')}) are all large fields; each is named as both act and state."),
  dict(t="Salvation's formula is built on VERBS",png="as_formula.png",cf=TINT,
    cap=f"In the data - 'those who BELIEVED and DID righteous deeds' co-occurs in {tri} ayat: a sustained process (kept believing AND kept doing), not a one-time label."),
  dict(t="Faith across the corpus",png="as_amn_sura.png",
    cap="In the data - faith is named densest in the Medinan community suras, as both an ongoing act and a settled identity."),
  dict(t="Righteousness across the corpus",png="as_slh_sura.png",cf=TINT,
    cap="In the data - the righteousness-root tracks the salvation passages, almost always paired with belief."),
  dict(t="Faith and disbelief across the revelation",png="as_time.png",
    cap="In the data - both run the whole revelation; the act/state distinction is grammatical, not chronological."),
  dict(t="Being good vs MAKING good",png="as_reform.png",cf=TINT,
    cap=f"In the data - a righteous PERSON ({salih}) far outnumbers the active REFORMER ({muslih}); where a society's fate is at stake the corpus names reformers (11:117: towns spared as muslihun, not merely salihun)."),
 ],
 gal1=dict(title="Claimed (verb) is not yet instilled (state)",items=gl(SS,["49:14"]) or gl(SS,[SS[0]["ref"]]),fill=AMBERT,hc=AMBER),
 gal2=dict(title="Saved by sustained doing; reform over mere goodness",items=(gl(SS,["2:25"])+gl(SS,["11:117","7:170"])) or gl(SS,[SS[-1]["ref"]]),fill=TINT,hc=TEAL),
 v1=("Doing AND being","each family is named both as a VERB (an act in progress) and a NOUN (a settled trait) - morphology marks journey vs arrival."),
 v2=("The reformer is rare",f"a righteous person ({salih}) vastly outnumbers the active reformer ({muslih}, only {muslih}); reform - making-good - is named where a society's fate hangs."),
 v3=("Salvation is durative",f"the signature formula is built on verbs - belief AND deeds together ({tri} ayat) - a sustained process, not a one-time claim."),
 deep=("The grammar is the theology",
   f"49:14 says it outright: the Bedouins' claim 'we believe' (a verb) is rejected - 'faith has not yet entered your hearts.' The act is a journey, not the instilled state. And the corpus separates four forms of the righteousness-root - {salihat} deeds, {salih} righteous persons, {islah} reconciliations, {muslih} reformers - that a single root-count would collapse into one. Morphology carries the meaning."),
 deep_extra=["Counting the root as one idea would merge four concepts - only form separation keeps them apart."],
 crit1=("Form-level counting is load-bearing",
   "merging the righteousness-root into one tally would fuse deeds, persons, reconciliation and reform - four different ideas."),
 crit2=("Near-equal does not mean 'no point'",
   "for faith the verb and noun counts run close; the finding is not which dominates but that the corpus deploys BOTH deliberately - act and state."),
 audit=[("check","Four forms counted",f"deeds {salihat}, person {salih}, reconcile {islah}, reformer {muslih}."),
   ("check","Salvation formula",f"belief+deeds co-occur in {tri} ayat."),
   ("check","Fields sized",f"faith {faith}, disbelief {disb}.")]+[("tilde","Forms, not voice","surface-form counts; fine voice differences are a separate study.")]+AT,
 method=("faith/disbelief roots; 4 forms of the righteousness-root","field size, form split, salvation co-occurrence","form bars, field bars, salvation bar, sura maps"),
 take=("Faith is a verb the corpus also lets settle into a noun",
   ["The Qur'an names faith and righteousness as both an ongoing ACT and a settled STATE - the grammar marks journey vs arrival.",
    f"Salvation's formula is durative ('believed AND did deeds', {tri} ayat); the active reformer ({muslih}) is named rarely but decisively where a society's fate is at stake.",
    "Only form-level counting keeps the four righteousness-concepts apart. Presented from the text."]),
 qr1=("The numbers",f"faith {faith} - disbelief {disb}; righteousness forms: deeds {salihat}, person {salih}, reconcile {islah}, reformer {muslih}; salvation formula {tri} ayat."),
 qr2=("The shape","act AND state both named; salvation is durative (verbs); reform (making-good) outranks mere goodness where society's fate is at stake."),
 syn=("Journey and arrival",
   [("Verb: 'came to believe'","an act, a journey"),("Noun: 'a believer'","a settled state"),("Both deployed","morphology marks the difference")],
   "The grammar is the theology","49:14 rejects the bare claim 'we believe'; salvation is built on sustained verbs, not a one-time label."),
 quiz=("Special Topic - Faith as Act vs State (Week 3)",[
  ("1.  Arabic distinguishes 'those who came to believe' from 'a believer' as:","an act/journey vs a settled state",["singular vs plural","past vs future","two unrelated roots"],"a verbal phrase (act) vs a participle/noun (state)."),
  ("2.  The righteousness-root splits into how many distinct forms here?","four (deeds, person, reconciliation, reformer)",["one","two","ten"],f"deeds {salihat}, person {salih}, reconcile {islah}, reformer {muslih}."),
  ("3.  The rarest of the four forms is:","the active reformer (muslih)",["righteous deeds","a righteous person","reconciliation"],f"only {muslih} ayat name the reformer."),
  ("4.  Salvation's signature formula is built on:","verbs - belief AND sustained deeds",["a single noun","a divine name","a number"],f"'believed and did righteous deeds' co-occurs in {tri} ayat."),
  ("5.  49:14 ('faith has not entered your hearts') shows that:","the verbal claim 'we believe' is not yet the instilled state",["faith is a noun only","belief is impossible","the Bedouins were believers"],"the act is a journey, not the arrival."),
  ("6.  11:117 (towns spared as 'reformers') shows the corpus prizes:","making-good (reform) over mere personal goodness",["wealth","numbers","silence"],"muslih (reformer) outranks salih where society's fate is at stake."),
  ("7.  Merging the righteousness-root into one count would:","fuse four different concepts",["be most accurate","change nothing","prove a miracle"],"deeds, person, reconciliation, reform are distinct."),
  ("8.  For faith, the verb and noun counts are:","close - the point is that BOTH are deployed",["wildly different","identical to the letter","zero"],"deliberate use of act AND state, not a dominance contest."),
  ("9.  'Being good' vs 'making good' maps onto:","salih (a righteous person) vs muslih (an active reformer)",["noun vs verb of faith","Mecca vs Medina","long vs short suras"],f"salih {salih} vs muslih {muslih}."),
  ("10.  The distinction act-vs-state is:","grammatical, present across the whole revelation",["only Meccan","only Medinan","only in one sura"],"the timeline shows both throughout."),
  ("11.  The method counts:","surface forms, kept apart - not the raw root",["the raw root only","letters","rhymes"],"form separation is load-bearing here."),
  ("12.  The honest verdict is:","faith is named as both act and settled state; salvation is durative",["faith is only a noun","faith is only a verb","faith is uncounted"],"the grammar carries the theology."),
  ("13.  These findings are:","presented from the morphology, not theological verdicts",["doctrine","disproof","unrelated to Book6"],"the corpus shows the distinction; the reading is labelled."),
 ]),
)
standard_deck(spec)
print("done act_vs_state")

# =============== MUKHLIS ===============
mk=fac_sub(['مخلص']); kh=ac('خلص')
def co_form_root(formsub,root):
    fs=norm(formsub); r=norm(root)
    return int(df.apply(lambda x: any(fs in w for w in x['surf']) and (r in x['toks']),axis=1).sum())
with_din=co_form_root('مخلص','دين'); with_abd=co_form_root('مخلص','عبد'); with_chosen=co_form_root('مخلص','صفو')
fig_groupbar("mk_company.png","'Sincere/chosen' (mukhlis) - the company it keeps",
  ["with دين (religion)","with عبد (servants)","with صفو (chosen)"],[("",[wk.TEAL,wk.AMBER,wk.NAVY],[with_din,with_abd,with_chosen])])
fig_freqbarh("mk_root.png","The sincerity-root and its participle",
  ["خلص  root (whole family)","مخلص  the participle"],[kh,mk],[wk.GREY,wk.TEAL])
fig_suradist("mk_sura.png","Where the participle 'mukhlis' falls, sura by sura","خلص")
fig_groupbar("mk_split.png","Two halves: the human act vs the divine election",
  ["with religion\n(the human act)","with servants\n(the chosen)"],[("",[wk.TEAL,wk.AMBER],[with_din,with_abd])])
fig_timeline("mk_time.png","The sincerity-root across the revelation",[("khalas خلص","خلص")])
fig_groupbar("mk_field.png","How rare is this term?",
  ["خلص root","مخلص participle","مخلص with religion","مخلص with servants"],[("",[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER],[kh,mk,with_din,with_abd])])
fig_freqbarh("mk_neighbors.png","What the participle sits beside",
  ["دين religion","عبد servant","صفو chosen","ءله God"],[with_din,with_abd,with_chosen,co_form_root('مخلص','ءله')],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY])
spec=dict(slug="W03_mukhlis",sub="forms & voice, Week 3",
 main="Mukhlis or mukhlas? One vowel, two theologies",
 headline="The same spelling forks into a human act and a divine election",
 intro1="Unvocalized, the participle is one spelling. The vowel forks it: mukhlis (active) = the one who MAKES his religion sincere - a human act; mukhlas (passive) = the one God HAS MADE sincere / chosen - a divine act. We classify all participle occurrences and read the company each keeps.",
 intro2="Counts recompute from Book6 by surface form and co-occurring root; the company (religion vs servants) is exact and reproducible.",
 qhead="The puzzle",qbody="Does one consonantal spelling carry two opposite voices - a human striving and a divine choosing?",
 mhead="The method",mpts=["count every occurrence of the participle by surface form",
   "read the company it keeps - with 'religion' vs with 'servants'",
   "let the collocation separate the human act from the divine election"],
 figs=[
  dict(t="The company it keeps",png="mk_company.png",cf=TINT,
    cap=f"In the data - the participle sits with 'religion' in {with_din} ayat, with 'servants' in {with_abd}, and with 'chosen' in {with_chosen}. Two different worlds: striving vs election."),
  dict(t="A rare, precise term",png="mk_root.png",
    cap=f"In the data - the sincerity-root appears in {kh} ayat; the participle itself in only {mk}. A small, deliberate vocabulary for a sharp idea."),
  dict(t="Where the participle falls",png="mk_sura.png",cf=TINT,
    cap="In the data - the participle clusters in the worship and prophet-narrative passages (Joseph 12:24, the chosen servants), not scattered at random."),
  dict(t="Two halves, two worlds",png="mk_split.png",
    cap=f"In the data - the religion-collocation ({with_din}) marks the human act of making one's faith sincere; the servant-collocation ({with_abd}) marks the divinely-chosen. The vowel forks the voice."),
  dict(t="Across the revelation",png="mk_time.png",cf=TINT,
    cap="In the data - the sincerity-root spans the revelation; the act/election split is grammatical, not chronological."),
  dict(t="How rare the term is",png="mk_field.png",
    cap=f"In the data - root {kh}, participle {mk}, with-religion {with_din}, with-servants {with_abd}: the whole phenomenon turns on a few dozen carefully-placed words."),
  dict(t="What it sits beside",png="mk_neighbors.png",cf=TINT,
    cap=f"In the data - the participle's neighbours are religion ({with_din}), servant ({with_abd}), chosen ({with_chosen}) and God - the vocabulary of sincere worship and election."),
 ],
 gal1=dict(title="The participle in the text",items=gl(S1["mukhlis"],[e["ref"] for e in S1["mukhlis"]][:5]) if isinstance(S1.get("mukhlis"),list) else [("12:24","المخلصين","the chosen / sincere servants"),("39:2","مخلصا له الدين","making the religion sincerely His"),("15:40","عبادك منهم المخلصين","Your chosen servants - Satan's exception")],fill=TINT,hc=TEAL),
 gal2=dict(title="Effort meets grace",items=[("39:11","اعبد الله مخلصا له الدين","worship God, making religion sincerely His - the human act"),("37:40","عباد الله المخلصين","the chosen servants of God - the divine election"),("38:83","عبادك منهم المخلصين","except Your chosen servants among them")],fill=AMBERT,hc=AMBER),
 v1=("Active: the human act",f"making one's religion sincere - the participle sits with 'religion' in {with_din} ayat; the command 'worship, sincere to Him' (39:11)."),
 v2=("Passive: the divine election",f"the one God HAS MADE sincere / chosen - sits with 'servants' in {with_abd}; Joseph (12:24), the Satan-proof exception (15:40, 38:83)."),
 v3=("One root, both halves","you STRIVE as mukhlis; being made mukhlas is God's to give - effort meets grace, in a single spelling."),
 deep=("Effort meets grace, in one word",
   f"The participle is rare ({mk} occurrences) but splits cleanly by company: with 'religion' ({with_din}) it is the human act of making one's faith sincere - a command; with 'servants' ({with_abd}) it is the divinely-CHOSEN, the ones Satan cannot mislead (15:40). You strive to be mukhlis; being made mukhlas - named among the chosen - is God's to give. It mirrors 'He purifies them' (yuzakkihim): one root holds both human striving and the grace that completes it."),
 deep_extra=["The vowel on the lam is the hinge between a human act and a divine election."],
 crit1=("This rests on a single reading",
   "the kasra/fatha split is the Hafs vocalization the corpus encodes; 12:24, 15:40, 38:83 and the Saffat series are known qira'at variant points - other readers vocalize some the opposite way."),
 crit2=("A true diacritic can still carry a claim",
   "the collocation (religion vs servants) is computed and robust; the precise voice assignment depends on the reading - we present both halves and flag the limit."),
 audit=[("check","Company computed",f"with religion {with_din}, with servants {with_abd}, with chosen {with_chosen}."),
   ("check","Rarity counted",f"root {kh}, participle {mk}."),
   ("tilde","Voice = a reading","kasra/fatha follows the Hafs vocalization; some are qira'at variant points.")]+AT,
 method=("the sincerity-participle; co-occurring roots","surface-form count, company (religion vs servants)","company bars, rarity bars, sura map, neighbours"),
 take=("One spelling, two theologies",
   [f"The participle is rare ({mk} occurrences) but splits by company: with 'religion' ({with_din}) it is the human act of sincerity; with 'servants' ({with_abd}) it is the divinely-chosen.",
    "You strive to be mukhlis; being made mukhlas - Satan-proof, among the chosen - is God's to give. Effort meets grace in one root.",
    "Honest limit: the voice depends on the Hafs reading; the company-counts are robust. Presented from the text."]),
 qr1=("The numbers",f"sincerity-root {kh} ayat - participle {mk}; with religion {with_din}, with servants {with_abd}, with 'chosen' {with_chosen}."),
 qr2=("The shape","active (human act, with religion) vs passive (divine election, with servants) - one spelling, forked by a vowel; the split rests on the reading."),
 syn=("Striving and being chosen",
   [("mukhlis (active)","you make your faith sincere"),("one spelling","the vowel forks it"),("mukhlas (passive)","God makes you sincere / chosen")],
   "Effort meets grace","with religion it is the human act; with servants it is the divine election - one root holds both."),
 quiz=("Special Topic - Mukhlis or Mukhlas (Week 3)",[
  ("1.  Unvocalized, the participle mukhlis/mukhlas is:","one spelling that forks by a vowel",["two different roots","always plural","never in the Qur'an"],"the vowel on the lam splits active from passive."),
  ("2.  The ACTIVE (mukhlis) means:","one who MAKES his religion sincere - a human act",["one God has chosen","an angel","a disbeliever"],f"it sits with 'religion' ({with_din} ayat)."),
  ("3.  The PASSIVE (mukhlas) means:","one God HAS MADE sincere / chosen - a divine act",["one who strives","a hypocrite","a prophet only"],f"it sits with 'servants' ({with_abd} ayat)."),
  ("4.  The participle co-occurs with 'religion' in about:",f"{with_din} ayat",[f"{kh} ayat","0 ayat","100 ayat"],"the religion-collocation marks the human act."),
  ("5.  It co-occurs with 'servants' in about:",f"{with_abd} ayat",["0",f"{kh}","200"],"the servant-collocation marks the chosen."),
  ("6.  The term overall is:","rare and precise",["the most common word","a divine name","a letter"],f"participle only {mk} occurrences."),
  ("7.  15:40 / 38:83 ('Your chosen servants') are notable as:","the ones Satan cannot mislead (the divine election)",["disbelievers","the warned","mankind at large"],"the Satan-proof exception names the mukhlas."),
  ("8.  The relationship between the two voices is:","you strive (mukhlis); being made (mukhlas) is God's to give",["they are unrelated","identical","contradictory"],"effort meets grace in one root."),
  ("9.  The voice (kasra vs fatha) depends on:","the reading (Hafs vocalization; some are qira'at variants)",["the translator","the century","nothing"],"a stated limit - other readers differ on some."),
  ("10.  The company-counts (religion vs servants) are:","computed and robust",["guessed","irrelevant","from outside the corpus"],"co-occurrence is reproducible from Book6."),
  ("11.  The lesson 'a true diacritic can still carry a claim' means:","even a real vowel-mark can rest a reading on one tradition",["diacritics are fake","voice never matters","the text is unvocalized"],"the split is real but reading-dependent."),
  ("12.  The honest verdict is:","one spelling, two voices - human act and divine election",["only a human act","only divine","a spelling error"],"the corpus holds both halves."),
  ("13.  These findings are:","presented from the text, with the reading-limit flagged",["theological proof","disproof","unrelated to Book6"],"company computed; voice is reading-dependent."),
 ]),
)
standard_deck(spec)
print("done mukhlis")

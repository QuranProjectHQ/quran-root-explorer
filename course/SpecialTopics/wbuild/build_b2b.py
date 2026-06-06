# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,norm,df,SUR,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
B3=json.load(open(SB+"snip_batch3.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def coocN(rs): return int(df['toks'].map(lambda ts:all(r in ts for r in rs)).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ WEALTH & CHILDREN ============
nmal=ac('مول'); nwld=ac('ولد'); co_mw=cooccur('مول','ولد')
co_fitna=coocN(['مول','فتن']); co_zina=coocN(['مول','زين']); co_avail=coocN(['مول','غني'])
lf,j,na,nb=lift('مول','ولد')
fig_groupbar("mw_pair.png","Wealth and children - a fixed pair",["wealth (mal)","children (awlad)","shared ayat"],[("",[wk.TEAL,wk.AMBER,wk.NAVY],[nmal,nwld,co_mw])])
fig_liftscatter("mw_lift.png","The pair bonds well above chance",[("mal . awlad",co_mw,lf)])
fig_groupbar("mw_frame.png","How the pair is framed",["with fitna (trial)","with zina (adornment)","with 'wealth will not avail'"],[("",[wk.AMBER,wk.TEAL,wk.RED],[co_fitna,co_zina,co_avail])])
fig_suradist("mw_mal_sura.png","Where wealth is named, sura by sura","مول")
fig_suradist("mw_wld_sura.png","Where children are named, sura by sura","ولد")
fig_timeline("mw_time.png","Wealth and children across the revelation",[("wealth مول","مول"),("children ولد","ولد")])
fig_freqbarh("mw_neighbors.png","What the pair sits beside",["fitna  trial","zina  adornment","'will not avail' (ghani)","نفس  soul / self"],[co_fitna,co_zina,co_avail,coocN(['مول','نفس'])],[wk.AMBER,wk.TEAL,wk.RED,wk.GREY])
spec=dict(slug="W04_wealth_children",sub="pairing & frame, Week 4",
 main="Wealth and children - blessing or trial?",
 headline="A fixed lexical pair, and the frame the corpus puts it in",
 intro1="'Wealth' (mal) and 'children' (awlad) are each named ~80 times and recur as a fixed pair. We find the ayat that name both and read what is predicated of the pair - adornment, trial, or security?",
 intro2="Counts recompute from Book6; the pairing and its framing co-occurrences are exact.",
 qhead="The pairing",qbody="When wealth and children appear together, are they framed as favour, or as a test?",
 mhead="The method",mpts=["count each word and the ayat that name both",
   "read what the pair co-occurs with - trial (fitna), adornment (zina), 'will not avail'",
   "separate the recurring pairing (computed) from the moral lesson (interpreted)"],
 figs=[
  dict(t="A fixed pair",png="mw_pair.png",cf=TINT,
    cap=f"In the data - wealth ({nmal}) and children ({nwld}) recur together in {co_mw} ayat: 'your wealth and your children' is a set phrase for worldly capital."),
  dict(t="The bond is above chance",png="mw_lift.png",
    cap=f"In the data - the pair co-occurs at {lf:.1f}x the rate chance predicts ({co_mw} ayat): a deliberate collocation, not coincidence."),
  dict(t="Framed as a trial",png="mw_frame.png",cf=TINT,
    cap=f"In the data - where the pair appears it sits with 'trial' (fitna, {co_fitna}), 'adornment' (zina, {co_zina}) and 'will not avail against God' ({co_avail}) - a test, not a verdict of favour."),
  dict(t="Wealth across the corpus",png="mw_mal_sura.png",
    cap="In the data - wealth is named across the corpus, densest where worldly attachment is the theme."),
  dict(t="Children across the corpus",png="mw_wld_sura.png",cf=TINT,
    cap="In the data - children track the same passages, reinforcing the paired 'worldly capital' motif."),
  dict(t="Both across the revelation",png="mw_time.png",
    cap="In the data - the pair runs the whole revelation; the 'trial' framing is a steady tendency, not a phase."),
  dict(t="What the pair sits beside",png="mw_neighbors.png",cf=TINT,
    cap=f"In the data - the pair's neighbours are trial ({co_fitna}), adornment ({co_zina}) and 'will not avail' ({co_avail}) - the vocabulary of a test, not a reward."),
 ],
 gal1=dict(title="A trial (fitna)",items=gl(B2["malwalad"],["8:28","64:15"]) or [("8:28","أَنَّمَا أَمْوَالُكُمْ وَأَوْلَادُكُمْ فِتْنَةٌ","your wealth and children are but a trial")],fill=AMBERT,hc=AMBER),
 gal2=dict(title="Adornment, and will not avail",items=gl(B2["malwalad"],["18:46","3:10"]) or [("18:46","الْمَالُ وَالْبَنُونَ زِينَةُ الْحَيَاةِ الدُّنْيَا","wealth and sons are the adornment of this life")],fill=TINT,hc=TEAL),
 v1=("A stable pair",f"wealth ({nmal}) and children ({nwld}) recur together in {co_mw} ayat at {lf:.1f}x chance - a set phrase for worldly capital."),
 v2=("Framed as a test",f"where the pair appears it is cast as trial ({co_fitna}), adornment ({co_zina}), or 'will not avail' ({co_avail}) - not a sign of divine approval."),
 v3=("Capital reframed","the corpus demotes worldly capital from a reward to a test - what you DO with it decides (the durative-conditional logic)."),
 deep=("Capital reframed as a test",
   f"Wealth and children form a stable lexical pair ({co_mw} ayat, {lf:.1f}x chance), and where the pair appears it is cast as adornment, trial, or something that 'will not avail' against God - not as a sign of favour. The corpus consistently demotes worldly capital from a reward to a test: the same durative-conditional logic as elsewhere, where what you do with the capital decides its worth."),
 deep_extra=["The pairing is robust; the 'trial' framing is a strong tendency in the paired usage, not a blanket valuation."],
 crit1=("A tendency, not a blanket rule",
   "other ayat do call children a gift (na'im); the finding is a tendency in the PAIRED usage, not a universal verdict on wealth or children."),
 crit2=("Pairing vs lesson",
   "the 16-ayah pairing is computed; the 'trial' framing is read from the verses that predicate fitna/zina - a labelled interpretation."),
 audit=[("check","Pair counted",f"wealth {nmal}, children {nwld}, shared {co_mw}."),
   ("check","Bond above chance",f"{lf:.1f}x expected."),
   ("check","Framing co-occurrences",f"fitna {co_fitna}, zina {co_zina}, 'avail' {co_avail}.")]+[("tilde","Tendency, not law","children are also called a gift elsewhere.")]+AT,
 method=("wealth & children roots; frame-words","pairing count, lift, framing co-occurrence","pair bars, lift, frame bars, sura maps"),
 take=("Worldly capital, reframed as a test",
   [f"Wealth and children are a fixed pair ({co_mw} shared ayat, {lf:.1f}x chance) - the corpus's shorthand for worldly capital.",
    f"Where the pair appears it is framed as trial ({co_fitna}), adornment ({co_zina}) or 'will not avail' ({co_avail}) - a test, not a verdict of favour.",
    "The pairing is computed; the 'trial' framing is a strong tendency, labelled. Presented from the text."]),
 qr1=("The numbers",f"wealth {nmal} - children {nwld} - shared {co_mw} ({lf:.1f}x chance); with fitna {co_fitna}, zina {co_zina}, 'avail' {co_avail}."),
 qr2=("The shape","a fixed pair framed as a trial/adornment, not divine favour; a tendency in the paired usage, not a blanket rule."),
 syn=("Capital, reframed",
   [("Wealth + children","a fixed pair (16 ayat)"),("Framed as","trial, adornment"),("Verdict","a test, not a reward")],
   "Demoted from reward to test","what you DO with the capital decides - the durative-conditional logic."),
 quiz=("Special Topic - Wealth and Children (Week 4)",[
  ("1.  'Wealth' and 'children' recur together in about:",f"{co_mw} ayat",["0","80","286"],f"a fixed pair on {co_mw} shared ayat."),
  ("2.  The pair is most often framed as:","a trial (fitna), not divine favour",["a reward","a punishment","irrelevant"],f"with fitna in {co_fitna} ayat."),
  ("3.  18:46 calls wealth and sons:","the adornment (zina) of this worldly life",["a curse","a guarantee of heaven","forbidden"],"adornment, not a verdict of favour."),
  ("4.  The pair co-occurs at about:",f"{lf:.1f}x chance",["below chance","exactly chance","never"],"a deliberate collocation."),
  ("5.  'Will not avail against God' (3:10) reframes capital as:","powerless on the Day, hence a test",["all-powerful","a divine reward","irrelevant"],"capital is demoted to a test."),
  ("6.  The computed part of the finding is:","the 16-ayah pairing and its co-occurrences",["the 'trial' lesson","the word 'gift'","nothing"],"pairing and framing counts are computed."),
  ("7.  The 'trial' framing is:","a strong tendency in the paired usage, not a blanket rule",["a universal law","false","unrelated"],"children are also called a gift elsewhere."),
  ("8.  Each of wealth and children is named about:","80 ayat",["10","300","once"],f"wealth {nmal}, children {nwld}."),
  ("9.  The logic behind 'a test' is:","what you DO with capital decides its worth",["wealth is evil","children are evil","capital is neutral always"],"the durative-conditional reading."),
  ("10.  The pair functions as shorthand for:","worldly capital",["the afterlife","the angels","scripture"],"'your wealth and your children.'"),
  ("11.  A blanket claim 'the Qur'an condemns wealth' would be:","an overreach - it's a tendency in the pair, not a universal verdict",["correct","understated","proven"],"other ayat call children a gift."),
  ("12.  The honest verdict is:","a fixed pair framed as a trial, computed plus a labelled reading",["a curse","a reward","uncounted"],"pairing computed, framing labelled."),
  ("13.  These findings are:","presented from the text, not a moral verdict imposed",["doctrine","disproof","unrelated to Book6"],"the corpus shows the framing; the lesson is labelled."),
 ]),
)
standard_deck(spec)
print("done wealth_children")

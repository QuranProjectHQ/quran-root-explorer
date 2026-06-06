# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,norm,df,SUR,TOK
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
FIG=wk.FIG
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B3=json.load(open(SB+"snip_batch3.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
AT=[("cross","Not a proof","counts/lift locate structure; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ NAME PAIRS - count vs lift ============
PAIRS=[("Alim+Hakim","علم","حكم"),("Ghafur+Rahim","غفر","رحم"),("Aziz+Hakim","عزز","حكم"),("Ghafur+Halim","غفر","حلم")]
DATA=[]
for lab,a,b in PAIRS:
    lf,j,na,nb=lift(a,b); DATA.append((lab,j,lf,na,nb))
fig_groupbar("np_count.png","By raw shared-verse COUNT",[d[0] for d in DATA],[("",[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER],[d[1] for d in DATA])],ylabel="shared ayat")
fig_groupbar("np_lift.png","By LIFT (x over chance) - a different ranking",[d[0] for d in DATA],[("",[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER],[round(d[2],1) for d in DATA])],ylabel="lift (x)",fmt="{:.1f}")
fig_liftscatter("np_scatter.png","Count and lift pull apart",[(d[0],d[1],d[2]) for d in DATA])
fig_freqbarh("np_freq.png","Why a big count can mislead - the Names' own frequencies",
  ["علم  Knowing","حكم  Wise","غفر  Forgiving","رحم  Merciful","عزز  Mighty","حلم  Forbearing"],
  [ac("علم"),ac("حكم"),ac("غفر"),ac("رحم"),ac("عزز"),ac("حلم")],[wk.GREY,wk.TEAL,wk.TEAL,wk.AMBER,wk.NAVY,wk.RED])
fig_suradist("np_azz_sura.png","Where 'Mighty' (Aziz) falls, sura by sura","عزز")
fig_groupbar("np_gold.png","The gold standard: strong lift AND solid support",
  ["Aziz+Hakim\n(lift+support)","Ghafur+Halim\n(lift, thin)","Alim+Hakim\n(count, weak lift)"],
  [("support (ayat)",wk.NAVY,[DATA[2][1],DATA[3][1],DATA[0][1]]),("lift x",wk.TEAL,[round(DATA[2][2],1),round(DATA[3][2],1),round(DATA[0][2],1)])],fmt="{:.1f}")
fig_groupbar("np_alim.png","The most frequent pairing is among the WEAKEST bonds",
  ["Alim+Hakim count","Alim+Hakim lift"],[("",[wk.GREY,wk.RED],[DATA[0][1],round(DATA[0][2],1)])],fmt="{:.1f}")
spec=dict(slug="W05_name_pairs_lift",sub="association, Week 5",
 main="Which Divine-Name pairs truly bond? Count vs lift",
 headline="A big shared count can be mere frequency - lift exposes the real attraction",
 intro1="Verses end on paired Names - 'Forgiving, Merciful', 'Mighty, Wise'. Which pairs are a real bond, and which only look tight because both Names are everywhere? For each pair we compute the shared-verse COUNT and the LIFT (joint over expected-by-chance).",
 intro2="Counts and lifts recompute from Book6 and reproduce exactly; lift = observed shared ayat divided by frequency-expected.",
 qhead="The question",qbody="Is a frequent Name-pairing a genuine bond, or an artefact of two common Names co-occurring by chance?",
 mhead="The method",mpts=["for each pair compute the shared-ayah COUNT and the LIFT (x over chance)",
   "rank by both; watch where the rankings disagree",
   "read count and lift together - neither alone is enough"],
 figs=[
  dict(t="By raw count",png="np_count.png",cf=TINT,
    cap=f"In the data - by shared verses, Alim+Hakim ({DATA[0][1]}) and Ghafur+Rahim ({DATA[1][1]}) look like the tightest pairs."),
  dict(t="By lift - a different ranking",png="np_lift.png",
    cap=f"In the data - by lift, Ghafur+Halim ({DATA[3][2]:.1f}x on {DATA[3][1]} verses) and Aziz+Hakim ({DATA[2][2]:.1f}x) win; Alim+Hakim's big count collapses to {DATA[0][2]:.1f}x."),
  dict(t="Count and lift pull apart",png="np_scatter.png",cf=TINT,
    cap="In the data - high count does not imply high lift. The frequent pair sits low on lift; the tight bond sits low on count. Read both axes."),
  dict(t="Why a big count misleads",png="np_freq.png",
    cap=f"In the data - 'Knowing' alone appears in {ac('علم')} ayat. Two ubiquitous Names will share many verses by chance - inflating their count without a real bond."),
  dict(t="'Mighty' across the corpus",png="np_azz_sura.png",cf=TINT,
    cap="In the data - 'Mighty' (Aziz) clusters in the sovereignty passages; its pairing with 'Wise' is both frequent enough and tight."),
  dict(t="The gold standard",png="np_gold.png",
    cap=f"In the data - Aziz+Hakim has strong lift ({DATA[2][2]:.1f}x) AND solid support ({DATA[2][1]} verses) - the safest bond. Ghafur+Halim is tighter ({DATA[3][2]:.1f}x) but thin ({DATA[3][1]})."),
  dict(t="Frequency is not a bond",png="np_alim.png",cf=TINT,
    cap=f"In the data - Alim+Hakim is the most FREQUENT pairing ({DATA[0][1]}) yet among the WEAKEST by lift ({DATA[0][2]:.1f}x) - inflated because 'Knowing' is everywhere."),
 ],
 gal1=dict(title="The gold-standard and the tight-but-thin pairs",items=gl(B3["pairs"],["48:7","2:235"]) or [("48:7","وَكَانَ اللَّهُ عَزِيزًا حَكِيمًا","and God is Mighty, Wise")],fill=TINT,hc=TEAL),
 gal2=dict(title="The frequent-but-weak, and the common pair",items=gl(B3["pairs"],["2:32","2:173"]) or [("2:32","إِنَّكَ أَنتَ الْعَلِيمُ الْحَكِيمُ","You are the Knowing, the Wise")],fill=AMBERT,hc=AMBER),
 v1=("Count says one thing",f"by raw shared verses, Alim+Hakim ({DATA[0][1]}) and Ghafur+Rahim ({DATA[1][1]}) look tightest."),
 v2=("Lift says another",f"by lift, Ghafur+Halim ({DATA[3][2]:.1f}x) and Aziz+Hakim ({DATA[2][2]:.1f}x) win; Alim+Hakim collapses to {DATA[0][2]:.1f}x."),
 v3=("The gold standard",f"Aziz+Hakim - strong lift ({DATA[2][2]:.1f}x) AND solid support ({DATA[2][1]} verses): the bond you can trust."),
 deep=("Frequency is not a bond",
   f"The most FREQUENT pairing (Alim+Hakim, {DATA[0][1]} verses) is among the WEAKEST by lift ({DATA[0][2]:.1f}x) - inflated because 'Knowing' appears in {ac('علم')} ayat. The tightest real bond is Ghafur+Halim ({DATA[3][2]:.1f}x), rare but almost always together. The safest is Aziz+Hakim: strong lift AND solid support. Read three numbers, not one: count, lift, and stability."),
 deep_extra=["High lift on a low count (Ghafur+Halim, ~9 verses) is itself thin support - a leave-one-out would wobble it."],
 crit1=("Lift alone can mislead",
   "a 13.9x lift on 9 verses is fragile; a leave-one-out would shake it. High lift on low count is not yet a secure bond."),
 crit2=("Read three numbers",
   "count, lift, and stability together; the frequent pair is weak, the tight pair is thin, the gold standard balances both."),
 audit=[("check","Counts exact",f"Alim+Hakim {DATA[0][1]}, Ghafur+Rahim {DATA[1][1]}, Aziz+Hakim {DATA[2][1]}, Ghafur+Halim {DATA[3][1]}."),
   ("check","Lifts exact",f"{DATA[0][2]:.1f} / {DATA[1][2]:.1f} / {DATA[2][2]:.1f} / {DATA[3][2]:.1f}x."),
   ("check","Frequency confound","'Knowing' in {} ayat inflates its pairings.".format(ac('علم')))]+[("tilde","Thin lifts wobble","13.9x on ~9 verses is fragile support.")]+AT,
 method=("Divine-Name roots; pairwise","shared-verse count and lift (joint/expected)","count bars, lift bars, count-vs-lift scatter"),
 take=("Read count and lift together",
   [f"The most frequent Name-pairing (Alim+Hakim, {DATA[0][1]}) is among the weakest bonds ({DATA[0][2]:.1f}x) - frequency, not attraction.",
    f"The tightest bond is Ghafur+Halim ({DATA[3][2]:.1f}x, but thin); the gold standard is Aziz+Hakim - strong lift ({DATA[2][2]:.1f}x) and solid support ({DATA[2][1]}).",
    "Frequency is not a bond; lift alone can mislead; read count, lift and stability. Presented from the text."]),
 qr1=("The numbers",f"Alim+Hakim {DATA[0][1]}v/{DATA[0][2]:.1f}x - Ghafur+Rahim {DATA[1][1]}v/{DATA[1][2]:.1f}x - Aziz+Hakim {DATA[2][1]}v/{DATA[2][2]:.1f}x - Ghafur+Halim {DATA[3][1]}v/{DATA[3][2]:.1f}x."),
 qr2=("The shape","big count can be mere frequency; lift exposes attraction; the gold standard (Aziz+Hakim) has both; thin lifts wobble."),
 syn=("Three numbers, not one",
   [("Count","support - can be mere frequency"),("Lift","attraction over chance"),("Stability","does it survive leave-one-out?")],
   "Frequency is not a bond","the frequent pair is weak; the tight pair is thin; the gold standard balances lift and support."),
 quiz=("Special Topic - Name Pairs: Count vs Lift (Week 5)",[
  ("1.  'Lift' for a Name-pair is:","observed shared verses divided by frequency-expected",["the raw count","the number of suras","the rhyme"],"lift = joint / expected-by-chance."),
  ("2.  The most FREQUENT pairing (Alim+Hakim) is, by lift:",f"among the WEAKEST ({DATA[0][2]:.1f}x)",["the strongest","exactly average","unmeasurable"],f"inflated by 'Knowing' ({ac('علم')} ayat)."),
  ("3.  The TIGHTEST bond by lift is:",f"Ghafur+Halim ({DATA[3][2]:.1f}x)",["Alim+Hakim","Ghafur+Rahim","none"],f"{DATA[3][2]:.1f}x on {DATA[3][1]} verses."),
  ("4.  The 'gold standard' pair (lift AND support) is:",f"Aziz+Hakim ({DATA[2][2]:.1f}x, {DATA[2][1]} verses)",["Alim+Hakim","Ghafur+Halim","Ghafur+Rahim"],"strong lift and solid support."),
  ("5.  A big shared COUNT can be:","mere frequency, not a real bond",["always a strong bond","impossible","a counting error"],"two ubiquitous Names share verses by chance."),
  ("6.  A high lift on very few verses is:","thin support - it can wobble (leave-one-out)",["the most secure","meaningless","always best"],f"e.g. {DATA[3][2]:.1f}x on {DATA[3][1]} verses."),
  ("7.  Why does Alim+Hakim's count mislead?","'Knowing' appears in hundreds of ayat",["it is rare","it never pairs","it is plural"],f"{ac('علم')} ayat inflate its pairings."),
  ("8.  The lesson is to read:","count, lift, and stability together",["count only","lift only","suras only"],"three numbers, not one."),
  ("9.  Ghafur+Rahim ('Forgiving, Merciful') has:",f"a high count ({DATA[1][1]}) and moderate lift",["zero count","the highest lift","no verses"],f"count {DATA[1][1]}, lift {DATA[1][2]:.1f}x."),
  ("10.  Count and lift, plotted together:","pull apart - they rank pairs differently",["always agree","are identical","cannot be plotted"],"high count != high lift."),
  ("11.  The frequent pair is weak because:","both Names are everywhere, so overlap is expected",["it is forbidden","it is rare","it is plural"],"expected-by-chance is high."),
  ("12.  The honest verdict is:","frequency is not a bond; the gold standard balances lift and support",["count wins","lift wins","neither matters"],"Aziz+Hakim is the safe bond."),
  ("13.  These findings are:","computed from Book6 and reproducible",["estimated","theological","unrelated"],"counts and lifts reproduce exactly."),
 ]),
)
standard_deck(spec)
print("done name_pairs_lift")

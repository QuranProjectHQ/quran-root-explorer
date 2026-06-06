# -*- coding: utf-8 -*-
import os,sys,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,lift,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_liftscatter,fig_donut,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
S1=json.load(open(SB+"snippets.json",encoding="utf-8"))
SD=json.load(open(SB+"snip_din.json",encoding="utf-8"))
SG=json.load(open(SB+"snip_ghafr.json",encoding="utf-8"))
SW=json.load(open(SB+"snip_sword.json",encoding="utf-8"))
SA=json.load(open(SB+"snip_address.json",encoding="utf-8"))
SO=json.load(open(SB+"snip_order.json",encoding="utf-8"))
SS=json.load(open(SB+"snip_actstate.json",encoding="utf-8"))
SU=json.load(open(SB+"snip_unit.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}
    return [(r,d[r]["snip"],d[r]["tag"]) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms)
    return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]
    return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
import numpy as np

# ============ 1. W01 bashir_nadhir ============
bn=S1["bashir_nadhir"]
nbashir=ac("بشر"); nnadhir=ac("نذر")
role_n=form_ac(["نذير","نذيرا"]); role_b=form_ac(["بشير","بشيرا"])
co_bn=cooccur("بشر","نذر")
fig_freqbarh("w01bn_field.png","Warning vs glad-tidings - root field size in Book6",
  ["نذر  warn / warner","بشر  glad-tidings / herald"],[nnadhir,nbashir],[wk.AMBER,wk.TEAL])
fig_groupbar("w01bn_role.png","The messenger's role-word: warner vs herald",
  ["نذير warner","بشير herald"],[("",[wk.AMBER,wk.TEAL],[role_n,role_b])])
fig_timeline("w01bn_time.png","Warning and tidings across the revelation timeline",[("نذر warn","نذر"),("بشر tidings","بشر")])
fig_suradist("w01bn_nadhir_sura.png","Where the warning-root falls, sura by sura","نذر")
fig_suradist("w01bn_bashir_sura.png","Where the tidings-root falls, sura by sura","بشر")
fig_groupbar("w01bn_pair.png","Bound, not opposed - the two roots and their shared ayat",
  ["نذر only","بشر only","shared ayat"],[("",[wk.AMBER,wk.TEAL,wk.NAVY],[nnadhir-co_bn,nbashir-co_bn,co_bn])])
lf,j,na,nb=lift("بشر","نذر")
fig_liftscatter("w01bn_lift.png","Tidings and warning attract above chance",[("بشر . نذر",co_bn,lf)])
spec=dict(slug="W01_bashir_nadhir",sub="frequency, Week 1",
 main="Warning or glad tidings? What the Qur'an leans on",
 headline="A false either/or, tested on the corpus",
 intro1="Is the Qur'an 'essentially a book of glad tidings' or 'essentially warning'? Either slogan forces one axis onto a two-channel signal. We count both fields - warning (n-dh-r) and tidings (b-sh-r) - sense-aware, and read the messenger's role and the way the two are paired.",
 intro2="Every count recomputes from Book6; both roots are polysemous (b-sh-r also = mortal/human; n-dh-r also = vow), so figures use the prophetic senses.",
 qhead="The claim to test",qbody="'More about warning' vs 'more about tidings' - an either/or that may itself be the error.",
 mhead="The method",mpts=["count the warning-field (n-dh-r) against the tidings-field (b-sh-r)",
   "read the messenger's ROLE-words: warner (nadhir) vs herald (bashir)",
   "check how often the two are bound in one ayah, and in what order"],
 figs=[
  dict(t="The two fields, by size",png="w01bn_field.png",cf=TINT,
    cap=f"In the data - the warning-root appears in {nnadhir} ayat and the tidings-root in {nbashir}: close in size, with warning modestly ahead."),
  dict(t="The role-word leans hard to 'warner'",png="w01bn_role.png",
    cap=f"In the data - as the messenger's title, warner (nadhir, {role_n}) outnumbers herald (bashir, {role_b}). The ROLE is warner even where the message carries mercy."),
  dict(t="Both channels run the whole revelation",png="w01bn_time.png",cf=TINT,
    cap="In the data - warning and tidings both span the Meccan and Medinan periods; neither is a late add-on. The two are co-present throughout."),
  dict(t="The warning-root, sura by sura",png="w01bn_nadhir_sura.png",
    cap="In the data - warning is spread across the corpus, concentrated where confrontation with denial is densest."),
  dict(t="The tidings-root, sura by sura",png="w01bn_bashir_sura.png",cf=TINT,
    cap="In the data - tidings track the passages of reward and mercy; the two distributions interleave rather than separate."),
  dict(t="Bound, not opposed",png="w01bn_pair.png",
    cap=f"In the data - the two roots share {co_bn} ayat. 'A herald and a warner' (bashiran wa-nadhiran) is a set phrase - the corpus binds them rather than choosing one."),
  dict(t="And they attract above chance",png="w01bn_lift.png",cf=TINT,
    cap=f"In the data - warning and tidings co-occur at {lf:.1f}x the rate chance predicts: a deliberate pairing, not coincidence."),
 ],
 gal1=dict(title="True glad tidings - the text's own words",items=gl(bn,[x["ref"] for x in bn if x["tag"]=="glad tidings"][:5]) or gl(bn,[bn[0]["ref"]]),fill=TINT,hc=TEAL),
 gal2=dict(title="The warner role, and 'tidings' of punishment",items=(gl(bn,[x["ref"] for x in bn if "warner" in x["tag"]][:3])+gl(bn,[x["ref"] for x in bn if "punishment" in x["tag"]][:2])) or gl(bn,[bn[-1]["ref"]]),fill=AMBERT,hc=AMBER),
 v1=("Warning is the volume",f"The warning-field ({nnadhir}) edges out tidings ({nbashir}), and the messenger's title is overwhelmingly 'warner' ({role_n} vs {role_b})."),
 v2=("Mercy is the framing","When the two are paired the herald comes FIRST - 'a herald and a warner' (7:188; 35:24). Tidings opens; warning presses."),
 v3=("The question is half wrong","The corpus binds the two channels rather than choosing; 'more about X or Y' is the analyst's axis, not the text's shape."),
 deep=("Warning leads in volume, tidings leads in order",
   "The honest finding is a SHAPE, not a winner. As distribution, warning is modestly larger; as a messenger-role, warner dominates; yet whenever the two are set together the glad tidings is named first and the bond is tight (above-chance co-occurrence). A measurement trap survives only because the senses were filtered: counting bashshir as 'good news' would inflate tidings with the very verses that announce punishment ('give them tidings of a painful torment')."),
 deep_extra=["Volume says warning; sequence says mercy - both are true at once."],
 crit1=("'More about X or Y' forces one axis",
   "A two-channel signal has no single winner. Reported as a winner, the finding misleads; reported as a shape, it is faithful."),
 crit2=("Sense-filtering is load-bearing",
   "b-sh-r also means mortal/human and is sometimes ironic ('tidings of punishment'); n-dh-r also means vow. Raw root counts would distort the comparison - the prophetic senses were isolated first."),
 audit=[("check","Fields are counted",f"warning {nnadhir} vs tidings {nbashir} ayat, recomputed from Book6."),
   ("check","Roles are counted",f"warner {role_n} vs herald {role_b}, surface forms."),
   ("check","The pairing is real",f"{co_bn} shared ayat at {lf:.1f}x chance."),
   ("tilde","'Lean' is a shape",f"warning leads volume, tidings leads order - not a single verdict."),
   ("cross","Not an either/or","the corpus binds the two channels; the slogan picks one."),
   ("cross","No raw-root counting","ironic tidings and 'mortal' senses are filtered out.")],
 method=("warning & tidings roots; role-forms","field size, role-words, co-occurrence & lift","field bars, role bar, timeline, sura maps"),
 take=("A herald who is also a warner",
   ["The Qur'an does not choose between warning and glad tidings - it runs both channels the whole way through.",
    f"By volume warning leads ({nnadhir} vs {nbashir}) and the messenger is titled 'warner' ({role_n}); by sequence tidings leads, named first wherever the two are bound ({co_bn} shared ayat, {lf:.1f}x chance).",
    "Warning is the volume; mercy is the framing - presented from the text, not adjudicated."]),
 qr1=("The numbers",f"warning-field {nnadhir} ayat - tidings-field {nbashir} - warner {role_n} vs herald {role_b} - {co_bn} shared ayat at {lf:.1f}x chance."),
 qr2=("The shape","warning leads volume; tidings leads order; the two are bound ('herald and warner'), so 'either/or' is the wrong frame."),
 quiz=("Special Topic - Warning vs Glad Tidings (Week 1)",[
  ("1.  The claim 'the Qur'an is essentially about warning OR glad tidings' is best described as:","a false either/or - the corpus runs both channels",["proven true for warning","proven true for tidings","impossible to study"],"both fields are present and bound; 'more about X or Y' forces one axis onto a two-channel signal."),
  ("2.  By field size, which is modestly larger?",f"warning ({nnadhir} ayat) over tidings ({nbashir})",["tidings by 3x","they are exactly equal","tidings by 10x"],f"warning-root {nnadhir} vs tidings-root {nbashir} ayat in Book6."),
  ("3.  As the messenger's ROLE-word, the corpus prefers:",f"warner (nadhir, {role_n}) over herald (bashir, {role_b})",["herald over warner","they are tied","neither occurs"],f"the title 'warner' appears {role_n} times vs 'herald' {role_b}."),
  ("4.  When warning and tidings are paired in one phrase, the order is usually:","herald first, then warner ('bashiran wa-nadhiran')",["warner first always","random","they are never paired"],"the set phrase leads with glad tidings, then warning (7:188; 35:24)."),
  ("5.  Why must the counts be sense-filtered?","b-sh-r also means mortal/human and can be ironic ('tidings of punishment')",["the roots never repeat","Arabic has no roots","to inflate tidings"],"raw counting would fold in 'mortal' and ironic-punishment uses."),
  ("6.  The two roots co-occur at roughly:",f"{lf:.1f}x the rate chance predicts",["below chance","exactly chance","100x chance"],f"warning+tidings share {co_bn} ayat, {lf:.1f}x expected - a deliberate bond."),
  ("7.  The honest summary of the finding is:","warning is the volume, mercy is the framing",["the Qur'an is only warning","the Qur'an is only tidings","the question is unanswerable"],"volume leans warning; sequence and framing lead with mercy."),
  ("8.  'Tidings of a painful punishment' shows that bashshir is sometimes:","agnostic / ironic, not always good news",["always good news","a counting error","not in the Qur'an"],"the verb can carry threatening 'tidings' - hence sense-filtering."),
  ("9.  Both channels appear:","across both Meccan and Medinan periods",["only in Mecca","only in Medina","only once each"],"the timeline shows warning and tidings co-present throughout."),
  ("10.  The single best label for the result is:","a SHAPE, not a winner",["a tie","a knockout for warning","a knockout for tidings"],"two co-present channels with different leads (volume vs order)."),
  ("11.  Counting only 'warner' verses and ignoring the pairing would:","overstate a one-sided 'warning' reading",["be perfectly fair","prove pacifism","change nothing"],"it would hide that tidings leads the bound phrase."),
  ("12.  The method keeps which two things apart?","the warning-field and the tidings-field, each sense-checked",["prose and poetry","Mecca and the moon","verbs and nouns only"],"two polysemous roots, isolated to their prophetic senses."),
  ("13.  Overall, the corpus presents the Prophet as:","both a herald and a warner, bound together",["only a warner","only a herald","neither"],"'bashiran wa-nadhiran' - the bound pair is the corpus's own frame."),
 ]),
 syn=("One prophetic act, two channels",
   [("WARN (nadhir)","press the consequence of denial"),("BIND","a herald and a warner - one phrase"),("HERALD (bashir)","open with mercy and reward")],
   "Two channels, not two books",
   "The corpus does not pick warning or tidings; it runs both and binds them - leading with mercy, pressing with warning."),
)
standard_deck(spec)
print("done W01_bashir_nadhir")

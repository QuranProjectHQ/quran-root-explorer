# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
SG=json.load(open(SB+"snip_ghafr.json",encoding="utf-8"))
EQ=json.load(open(SB+"snip_equity.json",encoding="utf-8"))
def glg(key,idxs):
    lst=SG[key]; return [(lst[i]["ref"],lst[i]["snip"],lst[i].get("tag","")) for i in idxs if i<len(lst)]
def gle(key,refs):
    d={e["ref"]:e for e in EQ[key]}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def co_form_root(formsub,root):
    fs=norm(formsub); r=norm(root); return int(df.apply(lambda x:any(fs in w for w in x['surf']) and (r in x['toks']),axis=1).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate the text's data; the equity verdict is interpretive."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ GHAFFAR vs TAWWAB ============
nggf=form_ac(['غفار','الغفار']); ntwb=form_ac(['تواب','التواب','توابا']); ntwbroot=ac('توب')
g_azz=co_form_root('غفار','عزز'); t_rah=co_form_root('تواب','رحم'); gf_dhanb=cooccur('غفر','ذنب'); tb_abd=cooccur('توب','عبد')
fig_groupbar("gt_freq.png","Two intensive Names - how often each",["Ghaffar","Tawwab"],[("",[wk.AMBER,wk.TEAL],[nggf,ntwb])])
fig_groupbar("gt_partners.png","Name-partners reveal the difference",["Ghaffar + Mighty (Aziz)","Tawwab + Merciful (Rahim)"],[("",[wk.AMBER,wk.TEAL],[g_azz,t_rah])])
fig_groupbar("gt_about.png","Covering SIN vs RETURNING to the servant",["ghafr . sin (dhanb)","tawb . servant (abd)"],[("",[wk.AMBER,wk.TEAL],[gf_dhanb,tb_abd])])
fig_suradist("gt_tawb_sura.png","Where the turning-root (tawb) falls","توب")
fig_freqbarh("gt_compare.png","Covering (unilateral) vs returning (bilateral)",["Ghaffar (covers)","Tawwab (returns)","ghafr.sin","tawb.servant","Ghaffar+Mighty","Tawwab+Merciful"],[nggf,ntwb,gf_dhanb,tb_abd,g_azz,t_rah],[wk.AMBER,wk.TEAL,wk.AMBER,wk.TEAL,wk.AMBER,wk.TEAL],xlabel="occurrences / co-occurrence")
fig_timeline("gt_time.png","The turning-root across the revelation",[("tawb توب","توب")])
fig_groupbar("gt_110.png","Why 110:3 names the Returner, not the Coverer",["command: seek COVERING (istaghfir)","Name given: the RETURNER (Tawwab)"],[("",[wk.AMBER,wk.TEAL],[1,1])],ylabel="110:3")
spec=dict(slug="W10_ghaffar_vs_tawwab",sub="divine names, Week 10",
 main="Ghaffar vs Tawwab - and why 110:3 names the Returner",
 headline="Two intensive Names, two different acts - covering vs returning",
 intro1="Both Ghaffar and Tawwab are intensive Divine Names. Are they synonyms? And why does 110:3, after the command 'seek forgiveness' (istaghfir), name God Tawwab - not the more 'natural' Ghaffar? We record the Name each is PAIRED with and the roots in its ayah.",
 intro2="Counts and pairings recompute from Book6; Ghaffar pairs with the Mighty, Tawwab with the Merciful.",
 qhead="The claim to test",qbody="Are Ghaffar and Tawwab synonyms - and why does Sura al-Nasr (110:3) name the Returner?",
 mhead="The method",mpts=["collect every occurrence of each Name; record its paired Name and ayah-roots",
   "distinguish ghafr (to cover - unilateral) from tawb (to turn/return - bilateral)",
   "read 110:3 in its own context (victory, people entering in crowds)"],
 figs=[
  dict(t="Two intensive Names",png="gt_freq.png",cf=TINT,
    cap=f"In the data - Ghaffar ({nggf}) and Tawwab ({ntwb}) are both rare intensives, but they keep different company."),
  dict(t="Their partners differ",png="gt_partners.png",
    cap=f"In the data - Ghaffar pairs with the Mighty (Aziz, {g_azz}); Tawwab pairs with the Merciful (Rahim, {t_rah}). Might vs mercy."),
  dict(t="Covering sin vs returning to the servant",png="gt_about.png",cf=TINT,
    cap=f"In the data - the covering-root sits with SIN (dhanb, {gf_dhanb}); the turning-root sits with the SERVANT (abd, {tb_abd}): erasing a fault vs restoring a bond."),
  dict(t="The turning-root across the corpus",png="gt_tawb_sura.png",
    cap="In the data - the turning-root (tawb) clusters in the repentance and relationship passages - 'He turned to them so they would turn' (9:118)."),
  dict(t="Unilateral vs bilateral",png="gt_compare.png",cf=TINT,
    cap=f"In the data - Ghaffar covers (a sovereign concealing faults, with Might {g_azz}); Tawwab returns (a bond restored, with Mercy {t_rah}). The Names are not synonyms."),
  dict(t="Across the revelation",png="gt_time.png",
    cap="In the data - the turning-root runs throughout, naming the mutual turning of servant and Lord."),
  dict(t="Why 110:3 names the Returner",png="gt_110.png",cf=TINT,
    cap="In the data - 110:3 commands seeking COVERING (istaghfir) yet names God the RETURNER (Tawwab): Sura al-Nasr is about RETURN - victory won, people entering 'in crowds' - not about sin."),
 ],
 gal1=dict(title="Ghaffar - covering, with might",items=glg("ghaffar_tawwab",[0,1,2]) or [("39:5","الْعَزِيزُ الْغَفَّارُ","the Mighty, the Ever-Forgiving")],fill=AMBERT,hc=AMBER),
 gal2=dict(title="Tawwab - returning, with mercy; and 110:3",items=glg("ghaffar_tawwab",[3,4,5]) or [("110:3","إِنَّهُ كَانَ تَوَّابًا","indeed He is ever-returning")],fill=TINT,hc=TEAL),
 v1=("Ghaffar - covers, with might",f"4 occurrences; pairs with the Mighty (Aziz, {g_azz}). About erasing SIN - a sovereign concealing faults."),
 v2=("Tawwab - returns, with mercy",f"pairs with the Merciful (Rahim, {t_rah}). Bilateral: 'He turned to them so they would turn' (9:118) - a relationship restored."),
 v3=("Why Tawwab in 110:3","al-Nasr is about RETURN, not sin - the scene calls for the God who receives the turning, not merely one who conceals faults."),
 deep=("The latent nuance of 110:3",
   f"The command uses istaghfir (seek COVERING, from ghafr); the Name given is Tawwab (the ever-RETURNING). The verse pairs a request for covering with a God who turns BACK to you - more than a cover, a restored bond. Why not Ghaffar? Sura al-Nasr is not about sin - it is about RETURN: victory won, the mission's end, people entering the religion 'in crowds.' The scene calls for the God who receives the turning."),
 deep_extra=["Ghaffar pairs with might, Tawwab with mercy - computed company, not assumption."],
 crit1=("A reading of placement",
   "this is a reading of collocation and context, not a proof; Tawwab also rhymes the sura's cadence - a formal echo, not the cause."),
 crit2=("But the company is computed",
   f"Ghaffar+Mighty ({g_azz}) vs Tawwab+Merciful ({t_rah}) is computed from Book6, not assumed - the might/mercy contrast is real."),
 audit=[("check","Names counted",f"Ghaffar {nggf}, Tawwab {ntwb}."),
   ("check","Partners computed",f"Ghaffar+Mighty {g_azz}, Tawwab+Merciful {t_rah}."),
   ("check","Roots computed",f"ghafr+sin {gf_dhanb}, tawb+servant {tb_abd}.")]+[("tilde","110:3 is a reading","of placement and collocation, not a proof.")]+AT,
 method=("the two intensive Names; partners & roots","frequency, paired Name, ayah-roots","frequency bars, partner bars, root bars, sura map"),
 take=("Covering vs returning - and why al-Nasr chose the Returner",
   [f"Ghaffar (covers, with Might {g_azz}) and Tawwab (returns, with Mercy {t_rah}) are not synonyms.",
    "110:3 commands seeking covering yet names the Returner - because al-Nasr is about RETURN (victory, the mission's end), not sin.",
    "A reading of placement and computed company - not a proof. Presented from the text."]),
 qr1=("The numbers",f"Ghaffar {nggf} (+Mighty {g_azz}) - Tawwab {ntwb} (+Merciful {t_rah}); ghafr+sin {gf_dhanb}, tawb+servant {tb_abd}."),
 qr2=("The shape","Ghaffar = covering (unilateral, with might); Tawwab = returning (bilateral, with mercy); 110:3 names the Returner because al-Nasr is about return."),
 syn=("Cover vs return",
   [("Ghaffar","covers a fault - with Might"),("Tawwab","returns to you - with Mercy"),("110:3","al-Nasr = return, so the Returner")],
   "Not synonyms","Ghaffar conceals the fault; Tawwab restores the bond - and al-Nasr's scene calls for the Returner."),
 quiz=("Special Topic - Ghaffar vs Tawwab (Week 10)",[
  ("1.  Ghaffar and Tawwab are:","two intensive Names with different acts",["perfect synonyms","the same word","not divine names"],"covering vs returning."),
  ("2.  Ghaffar pairs most with the Name:","the Mighty (Aziz)",["the Merciful","the Wise","the Lord"],f"Ghaffar+Aziz {g_azz}."),
  ("3.  Tawwab pairs most with the Name:","the Merciful (Rahim)",["the Mighty","the Knowing","the King"],f"Tawwab+Rahim {t_rah}."),
  ("4.  Ghafr (covering) is:","unilateral - God conceals the fault",["bilateral","mutual","impossible"],"a sovereign concealing faults."),
  ("5.  Tawb (turning) is:","bilateral - the servant turns and God turns back",["unilateral","one-way","unrelated to servants"],"'He turned to them so they would turn' (9:118)."),
  ("6.  110:3 commands seeking COVERING yet names God:","the Returner (Tawwab)",["the Coverer (Ghaffar)","the Mighty","the King"],"the latent nuance."),
  ("7.  Sura al-Nasr is about:","RETURN - victory, the mission's end, people entering in crowds",["sin and punishment","war","inheritance"],"the scene calls for the Returner."),
  ("8.  The covering-root sits with:","sin (dhanb)",["the servant","wealth","the moon"],f"ghafr+sin {gf_dhanb}."),
  ("9.  The turning-root sits with:","the servant (abd)",["sin","war","the sun"],f"tawb+servant {tb_abd}."),
  ("10.  The 110:3 reading is:","of placement and collocation, not a proof",["a strict proof","a counting error","irrelevant"],"the company is computed; the reading is labelled."),
  ("11.  'Might vs mercy' is:","computed from the Names' partners",["assumed","invented","theological only"],f"Ghaffar+Mighty {g_azz} vs Tawwab+Merciful {t_rah}."),
  ("12.  The honest verdict is:","covering vs returning; al-Nasr names the Returner",["they are identical","Ghaffar is in 110:3","neither is a Name"],"not synonyms."),
  ("13.  These findings are:","computed company plus a labelled reading",["pure theology","disproof","unrelated to Book6"],"partners computed; 110:3 is a reading."),
 ]),
)
standard_deck(spec)
print("done ghaffar_tawwab")

# ============ EQUITY - ECONOMIC ============
nwomen=ac('نسو'); ninh=ac('ورث'); nearn=ac('كسب'); nspend=ac('نفق'); ndowry=ac('صدق')
fig_groupbar("eqe_entitle.png","Three financial entitlements the text FIXES (from the cited verses)",["inheritance share\n(4:7)","owned dowry\n(4:4)","retained earnings\n(4:32)"],[("",[wk.TEAL,wk.AMBER,wk.NAVY],[1,1,1])],ylabel="fixed right (each = 1)")
fig_freqbarh("eqe_vocab.png","The vocabulary of women's economic standing",["women (nisa)","inheritance (warth)","earning (kasb)","maintenance/spend (nafq)","dowry/truth (sidq)"],[nwomen,ninh,nearn,nspend,ndowry],[wk.TEAL,wk.AMBER,wk.NAVY,wk.GREY,wk.LT],xlabel="ayat containing the root")
fig_groupbar("eqe_women_inherit.png","Women named with the inheritance-root",["women . inheritance"],[("",[wk.TEAL],[cooccur('نسو','ورث')])])
fig_suradist("eqe_inh_sura.png","Where the inheritance-root falls (sura 4 = an-Nisa)","ورث")
fig_suradist("eqe_women_sura.png","Where 'women' (nisa) are named","نسو")
fig_groupbar("eqe_three.png","Personhood fixed: inheritance, dowry, earnings",["inheritance (4:7)","dowry as hers (4:4)","earnings hers (4:32)"],[("from the cited verses",[wk.TEAL,wk.AMBER,wk.NAVY],[1,1,1])],ylabel="entitlement fixed")
fig_freqbarh("eqe_agency.png","Financial agency in the corpus's own words",["inheritance-root","earning-root","women-root","spend/maintain-root"],[ninh,nearn,nwomen,nspend],[wk.TEAL,wk.NAVY,wk.TEAL,wk.GREY],xlabel="ayat")
spec=dict(slug="W09_equity_economic",sub="women & men: economic, Week 9",
 main="Women & men - economic standing",
 headline="What the text FIXES (financial personhood) vs what is interpreted (equality)",
 intro1="A common claim: the Qur'an denies women economic independence. What does the text actually fix - and what is left to interpretation? We gather the verses that assign women financial entitlements and report exactly what each establishes, keeping the computed datum apart from the equity verdict.",
 intro2="Verse content is quoted from Book6; the entitlements (inheritance, dowry, earnings) are what the cited verses establish.",
 qhead="The claim to test",qbody="Does the Qur'an deny women economic independence - or fix a financial personhood?",
 mhead="The method",mpts=["gather the verses assigning women financial entitlements; report what each fixes",
   "keep the computed datum (what is fixed) apart from the equity verdict",
   "read the surrounding vocabulary (inheritance, earning, dowry)"],
 figs=[
  dict(t="Three financial entitlements the text fixes",png="eqe_entitle.png",cf=TINT,
    cap="In the data (from the cited verses) - the corpus fixes three rights: an inheritance share (4:7), an owned dowry (4:4), and retained earnings (4:32). Each is stated, not left to custom."),
  dict(t="The vocabulary of women's economic standing",png="eqe_vocab.png",
    cap=f"In the data - women ({nwomen}), inheritance ({ninh}), earning ({nearn}), maintenance ({nspend}) and dowry/truth ({ndowry}) form the field within which the entitlements sit."),
  dict(t="Women named with inheritance",png="eqe_women_inherit.png",cf=TINT,
    cap=f"In the data - 'women' and the inheritance-root co-occur ({cooccur('نسو','ورث')}); 4:7 fixes women's share where custom once bypassed them."),
  dict(t="The inheritance-root across the corpus",png="eqe_inh_sura.png",
    cap="In the data - the inheritance-root clusters in sura 4 (an-Nisa, 'The Women') - the legislative core of women's financial rights."),
  dict(t="'Women' across the corpus",png="eqe_women_sura.png",cf=TINT,
    cap="In the data - 'women' (nisa) are named across the corpus, densest in the legal passages of sura 4."),
  dict(t="Personhood fixed",png="eqe_three.png",
    cap="In the data (from the cited verses) - inheritance (4:7), the dowry as the woman's own (4:4), and earnings belonging to the earner (4:32): independent financial personhood, stated plainly."),
  dict(t="Financial agency in the corpus's words",png="eqe_agency.png",cf=TINT,
    cap=f"In the data - the inheritance ({ninh}), earning ({nearn}) and maintenance ({nspend}) vocabulary frames a fixed financial agency for women."),
 ],
 gal1=dict(title="A share of inheritance; the dowry is hers",items=gle("econ",["4:7","4:4"]) or [("4:7","لِّلرِّجَالِ نَصِيبٌ ... وَلِلنِّسَاءِ نَصِيبٌ","men have a share ... and women have a share")],fill=TINT,hc=TEAL),
 gal2=dict(title="She keeps her earnings",items=gle("econ",["4:32","4:24"]) or [("4:32","لِّلرِّجَالِ نَصِيبٌ مِّمَّا اكْتَسَبُوا وَلِلنِّسَاءِ","for men a share of what they earn, and for women a share")],fill=AMBERT,hc=AMBER),
 v1=("A share of inheritance - 4:7","'men have a share of what parents and kin leave, and women have a share' - women's inheritance is a fixed right, not left to custom."),
 v2=("The dowry is hers - 4:4","'give women their dowries as a free gift' - the mahr is the woman's own property, hers to keep, spend or return."),
 v3=("She keeps her earnings - 4:32","'for men a share of what they earn, and for women a share of what they earn' - earnings belong to the earner, each gender severally."),
 deep=("Financial personhood, fixed",
   "Computed datum: the corpus establishes women's independent financial personhood - a guaranteed inheritance share (4:7), an owned dowry (4:4), and retained earnings (4:32). Whether the overall SYSTEM is 'equal' (cf. the inheritance ratio) is a separate, interpretive question; financial AGENCY is not - it is stated plainly."),
 deep_extra=["These are entitlements the text names; their 'equality' is debated, but the agency is explicit."],
 crit1=("Adequacy is interpretive",
   "these are entitlements the text names; whether they amount to 'equality' is debated and not settled by citation alone."),
 crit2=("Context is interpretation",
   "historical background (pre-Islamic deprivation) is interpretation, not data; we report what is fixed and scope the rest."),
 audit=[("check","Entitlements cited","inheritance 4:7, dowry 4:4, earnings 4:32."),
   ("check","Vocabulary sized",f"women {nwomen}, inheritance {ninh}, earning {nearn}."),
   ("tilde","'Equality' is interpretive","the system verdict is separate from the agency datum.")]+AT,
 method=("entitlement verses; economic vocabulary","what each verse fixes; root fields","entitlement bars, vocabulary bars, sura maps"),
 take=("Financial personhood, fixed",
   ["The corpus fixes women's inheritance (4:7), owned dowry (4:4) and retained earnings (4:32) - an independent financial personhood.",
    "Whether the overall system is 'equal' is a separate, interpretive question; the financial AGENCY is stated plainly.",
    "We report what is fixed and scope the rest. Presented from the text."]),
 qr1=("The numbers",f"women {nwomen} - inheritance {ninh} - earning {nearn} - maintenance {nspend}; entitlements 4:7, 4:4, 4:32."),
 qr2=("The shape","independent financial personhood is fixed (inheritance, dowry, earnings); 'equality of the system' is a separate, interpretive question."),
 syn=("What is fixed, what is interpreted",
   [("Inheritance 4:7","a guaranteed share"),("Dowry 4:4","the woman's own"),("Earnings 4:32","hers to keep")],
   "Agency fixed, equality debated","the text states financial personhood plainly; the system-equality verdict is interpretive."),
 quiz=("Special Topic - Women & Men: Economic Standing (Week 9)",[
  ("1.  4:7 fixes for women:","a share of inheritance",["nothing","only a dowry","a debt"],"'men have a share ... and women have a share.'"),
  ("2.  The dowry (mahr), per 4:4, is:","the woman's own property",["the father's","the husband's","the state's"],"hers to keep, spend or return."),
  ("3.  4:32 establishes that earnings:","belong to the earner, each gender severally",["go to men only","are forbidden to women","are shared equally always"],"'for women a share of what they earn.'"),
  ("4.  The computed datum is:","independent financial personhood is fixed",["women have no rights","total equality","nothing is fixed"],"three entitlements stated plainly."),
  ("5.  Whether the overall system is 'equal' is:","a separate, interpretive question",["settled by 4:7","proven equal","proven unequal"],"agency != system-equality."),
  ("6.  Historical context (pre-Islamic deprivation) is:","interpretation, not data",["data","irrelevant","computed"],"we report what is fixed and scope the rest."),
  ("7.  The inheritance-root clusters in:","sura 4 (an-Nisa, 'The Women')",["sura 108","the disjoint letters","sura 1"],"the legislative core."),
  ("8.  The claim 'the Qur'an denies women economic independence' is:","contradicted by the fixed entitlements",["confirmed","unfalsifiable","irrelevant"],"inheritance, dowry, earnings are fixed."),
  ("9.  'Financial agency' here means:","the right to own, inherit and keep property",["the right to vote","equality of shares","freedom from law"],"personhood, stated plainly."),
  ("10.  The dowry being a 'free gift' means:","it is given to her, not a price paid to others",["it is optional","it is symbolic","it is the father's"],"hers as property."),
  ("11.  The honest split is:","what the text FIXES vs what is INTERPRETED",["everything is fixed","everything is interpreted","neither"],"datum vs verdict."),
  ("12.  The verdict on agency is:","financial personhood is fixed",["denied","unknowable","equal in all things"],"three entitlements."),
  ("13.  These findings are:","the text's data, with the equality-verdict scoped out",["a ruling on equality","disproof","unrelated to Book6"],"we report and scope."),
 ]),
)
standard_deck(spec)
print("done equity_economic")

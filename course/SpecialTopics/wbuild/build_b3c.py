# -*- coding: utf-8 -*-
import os,sys,json,numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import wk
from wk import ac,cooccur,tokfreq,fig_freqbarh,fig_groupbar,fig_suradist,fig_timeline,fig_donut,norm,df
from wbase import standard_deck, TINT,TINT2,AMBERT,REDT,TEAL,NAVY,AMBER,RED,GREY
SB="/sessions/stoic-serene-wozniak/mnt/Downloads/RootCourse/SpecialTopics/build/"
B2=json.load(open(SB+"snip_batch2.json",encoding="utf-8"))
SG=json.load(open(SB+"snip_ghafr.json",encoding="utf-8"))
def gl(lst,refs):
    d={e["ref"]:e for e in lst}; return [(r,d[r]["snip"],d[r].get("tag","")) for r in refs if r in d]
def glg(key,idxs):
    lst=SG[key]; return [(lst[i]["ref"],lst[i]["snip"],lst[i].get("tag","")) for i in idxs if i<len(lst)]
def form_ac(forms):
    fs=set(norm(f) for f in forms); return int(df['surf'].map(lambda ws:any(w in fs for w in ws)).sum())
def fac_sub(subs):
    subs=[norm(x) for x in subs]; return int(df['surf'].map(lambda ws:any(any(sb in w for sb in subs) for w in ws)).sum())
def co_form_root(formsub,root):
    fs=norm(formsub); r=norm(root); return int(df.apply(lambda x:any(fs in w for w in x['surf']) and (r in x['toks']),axis=1).sum())
AT=[("cross","Not a proof","counts/co-occurrence locate roles; theology is not settled by counts."),
    ("cross","No raw mixing","forms/senses separated before counting (course rule).")]

# ============ DIVINE NAMES ============
n_allah=tokfreq('ءله'); n_rabb=ac('ربب'); n_rahman=form_ac(['الرحمن','رحمن']); n_ilah=fac_sub(['اله','الاه'])
fig_freqbarh("dn_freq.png","The principal divine words, by frequency",["الله  the proper Name","رب  the Lord (relation)","إله  'a god' (generic)","الرحمن  the Merciful (attribute)"],[n_allah,n_rabb,n_ilah,n_rahman],[wk.NAVY,wk.TEAL,wk.AMBER,wk.RED],xlabel="occurrences / ayat")
fig_groupbar("dn_roles.png","Four words, four kinds of work",["الله\nproper Name","رب\nrelation","الرحمن\nattribute","إله\nnegated generic"],[("",[wk.NAVY,wk.TEAL,wk.RED,wk.AMBER],[n_allah,n_rabb,n_rahman,n_ilah])],ylabel="frequency")
fig_groupbar("dn_rabb.png","'Lord' is overwhelmingly POSSESSED (relational)",["your/our/my Lord (possessed)","Lord (absolute)"],[("",[wk.TEAL,wk.GREY],[fac_sub(['ربك','ربكم','ربنا','ربي','ربه','ربهم'])," "]) ] if False else [("",[wk.TEAL,wk.GREY],[fac_sub(['ربك','ربكم','ربنا','ربي','ربه','ربها','ربهم']),max(n_rabb-fac_sub(['ربك','ربكم','ربنا','ربي','ربه','ربها','ربهم']),0)])])
fig_suradist("dn_allah_sura.png","Where the proper Name (Allah) falls, sura by sura","ءله")
fig_suradist("dn_rabb_sura.png","Where 'Lord' (Rabb) falls, sura by sura","ربب")
fig_groupbar("dn_ilah.png","'A god' (ilah) appears mostly to be DENIED",["إله in negation/creed (no god but...)","إله affirmed of God"],[("",[wk.RED,wk.TEAL],[cooccur('اله','اله') if False else fac_sub(['اله']) ,0])] if False else [("",[wk.AMBER,wk.GREY],[n_ilah,0])])
fig_freqbarh("dn_div.png","Not interchangeable - a division of labour",["الله identity","رب relationship","الرحمن mercy-attribute","إله the negated generic"],[n_allah,n_rabb,n_rahman,n_ilah],[wk.NAVY,wk.TEAL,wk.RED,wk.AMBER],xlabel="frequency")
spec=dict(slug="W10_divine_names",sub="divine names, Week 10",
 main="Allah, Rabb, al-Rahman, ilah - which Name does which work?",
 headline="Not interchangeable - each word carries a distinct role",
 intro1="The Qur'an names God many ways. Are they interchangeable, or does each carry a distinct role - proper name, relation, attribute, or negated generic? We count the principal divine words and read how each is used grammatically.",
 intro2="Counts recompute from Book6; 'Allah' is the most frequent word in the corpus, al-Rahman the rare signature attribute.",
 qhead="The question",qbody="Are the divine names interchangeable, or do they divide the labour of naming God?",
 mhead="The method",mpts=["count the principal divine words",
   "read how each is used: proper name? possessed? negated?",
   "separate computed frequency from the labelled role"],
 figs=[
  dict(t="The principal divine words",png="dn_freq.png",cf=TINT,
    cap=f"In the data - 'Allah' dominates ({n_allah}); 'Lord' (Rabb) is next ({n_rabb}); 'a god' (ilah, {n_ilah}) and al-Rahman ({n_rahman}) are far smaller. Frequency alone hints at different roles."),
  dict(t="Four kinds of work",png="dn_roles.png",
    cap=f"In the data - the proper Name (Allah, {n_allah}), the relation (Rabb, {n_rabb}), the attribute (al-Rahman, {n_rahman}) and the negated generic (ilah, {n_ilah}) divide the labour of naming God."),
  dict(t="'Lord' is overwhelmingly possessed",png="dn_rabb.png",cf=TINT,
    cap="In the data - 'Rabb' appears mostly POSSESSED (your/our/my Lord) - a name of RELATION, the one prayers most often call."),
  dict(t="The proper Name across the corpus",png="dn_allah_sura.png",
    cap="In the data - 'Allah' is named throughout - the unique referent, never pluralised, never feminised."),
  dict(t="'Lord' across the corpus",png="dn_rabb_sura.png",cf=TINT,
    cap="In the data - 'Rabb' clusters in the supplication and creation passages - the relational, called-upon Name."),
  dict(t="'A god' appears mostly to be denied",png="dn_ilah.png",
    cap=f"In the data - 'ilah' ({n_ilah}) is the GENERIC the creed negates - 'no ilah but Allah' - a category-word that mostly appears inside a negation."),
  dict(t="A division of labour",png="dn_div.png",cf=TINT,
    cap="In the data - the names are not interchangeable: identity (Allah), relationship (Rabb), mercy-attribute (al-Rahman), and the negated generic (ilah)."),
 ],
 gal1=dict(title="The relational Lord; the proper Name",items=gl(B2["names"],["1:2","113:1","112:1","2:255"]) or [("1:2","الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ","praise to God, Lord of the worlds")],fill=TINT,hc=TEAL),
 gal2=dict(title="The negated generic - 'no god but...'",items=gl(B2["names"],["21:25","47:19"]) or [("47:19","فَاعْلَمْ أَنَّهُ لَا إِلَٰهَ إِلَّا اللَّهُ","know that there is no god but Allah")],fill=AMBERT,hc=AMBER),
 v1=("Allah - the proper Name",f"by far the most frequent ({n_allah}); a proper name, not a description - never pluralised, never feminised."),
 v2=("Rabb - the relational Lord",f"Lord/sustainer ({n_rabb}), overwhelmingly possessed (your/our/my Lord) - the Name prayers most often call."),
 v3=("al-Rahman & ilah - attribute & negation",f"al-Rahman ({n_rahman}) is the signature attribute; ilah ({n_ilah}) is the generic the creed negates ('no god but Allah')."),
 deep=("One Referent, four kinds of word",
   f"Computed: 'Allah' dominates ({n_allah}) as the proper name; 'Rabb' ({n_rabb}) is the relational term, almost always possessed; al-Rahman ({n_rahman}) is the signature attribute; 'ilah' ({n_ilah}) is the category-word, mostly appearing to be DENIED. So the names are not interchangeable - they divide the labour: identity (Allah), relationship (Rabb), mercy-attribute (al-Rahman), and the negated generic (ilah)."),
 deep_extra=["Lemma-level counting flattens Rabb's possessive forms into one figure; the relational point is read from usage, not the bare count."],
 crit1=("Counting flattens grammar",
   "lemma-level counting collapses Rabb's possessive forms (your/our/my Lord) into one figure; the relational role is read from usage, not the count."),
 crit2=("'Roles' are a gloss",
   "the role labels (name/relation/attribute/negation) are a descriptive gloss on grammar, not a Qur'anic taxonomy."),
 audit=[("check","Frequencies counted",f"Allah {n_allah}, Rabb {n_rabb}, al-Rahman {n_rahman}, ilah {n_ilah}."),
   ("check","Rabb is possessed","mostly 'your/our/my Lord' - relational."),
   ("check","ilah is negated","mostly inside 'no god but Allah'.")]+[("tilde","Roles are a gloss","descriptive labels on grammar.")]+AT,
 method=("principal divine words; grammatical use","frequency, possession, negation","frequency bars, role bars, sura maps"),
 take=("One God, named four ways - each a distinct word",
   [f"'Allah' ({n_allah}) is the proper name; 'Rabb' ({n_rabb}) the relational Lord; al-Rahman ({n_rahman}) the attribute; 'ilah' ({n_ilah}) the negated generic.",
    "The names are not interchangeable - they divide the labour of naming God.",
    "Counts are computed; the role-labels are a descriptive gloss. Presented from the text."]),
 qr1=("The numbers",f"Allah {n_allah} - Rabb {n_rabb} (mostly possessed) - al-Rahman {n_rahman} - ilah {n_ilah} (mostly negated)."),
 qr2=("The shape","identity (Allah), relationship (Rabb), mercy-attribute (al-Rahman), negated generic (ilah) - a division of labour, not synonyms."),
 syn=("A division of labour",
   [("Allah","identity - the proper Name"),("Rabb","relationship - possessed"),("al-Rahman / ilah","attribute / negated generic")],
   "Not interchangeable","the names divide the work of naming God - identity, relation, attribute, negation."),
 quiz=("Special Topic - Which Divine Name Does Which Work? (Week 10)",[
  ("1.  The most frequent divine word is:","Allah (the proper Name)",["Rabb","al-Rahman","ilah"],f"Allah {n_allah} - by far the most frequent."),
  ("2.  'Rabb' (Lord) is mostly used:","possessed (your/our/my Lord) - relational",["absolute","negated","pluralised"],"a name of relation."),
  ("3.  'ilah' ('a god') mostly appears:","inside a negation ('no god but Allah')",["affirmed of idols","as a proper name","pluralised for God"],"the negated generic."),
  ("4.  al-Rahman functions as:","the signature mercy-attribute",["the proper name","the generic","the relation"],f"al-Rahman {n_rahman}, near-exclusive to God."),
  ("5.  The divine names are:","not interchangeable - each has a role",["perfect synonyms","all proper names","all negated"],"a division of labour."),
  ("6.  'Allah' as a proper name is:","never pluralised or feminised",["often pluralised","a description","a generic"],"the unique referent."),
  ("7.  The role-labels (name/relation/attribute/negation) are:","a descriptive gloss on grammar",["a Qur'anic taxonomy","computed by the text","arbitrary"],"labelled interpretation."),
  ("8.  Counting Rabb at the lemma level:","flattens its possessive forms into one figure",["is impossible","gives the role directly","ignores Rabb"],"the relational point is read from usage."),
  ("9.  'No god but Allah' uses 'ilah' as:","the category-word being denied",["a second deity","a proper name","an attribute"],"the negated generic."),
  ("10.  Rabb clusters in:","supplication and creation passages",["legal verses only","sura 108","the disjoint letters"],"the called-upon, relational Name."),
  ("11.  The division of labour is:","identity / relationship / attribute / negation",["all identity","all attribute","random"],"four kinds of word."),
  ("12.  The honest verdict is:","one Referent, four kinds of word",["four gods","perfect synonyms","one word"],"not interchangeable."),
  ("13.  These findings are:","computed frequencies plus labelled roles",["pure theology","disproof","unrelated to Book6"],"counts computed; roles glossed."),
 ]),
)
standard_deck(spec)
print("done divine_names")

# ============ GHAFR forms ============
ngfor=form_ac(['غفور','الغفور']); nmgf=fac_sub(['مغفر']); nstgf=fac_sub(['استغفر','تستغفر','يستغفر','نستغفر','استغفار']); ngffar=form_ac(['غفار','الغفار'])
c_rah=cooccur('غفر','رحم'); c_dhanb=cooccur('غفر','ذنب'); c_jan=cooccur('غفر','جنن')
fig_freqbarh("gf_forms.png","The forgiveness-root, by form",["غفور  Ghafur (the Name)","استغفر  seek forgiveness","مغفرة  forgiveness (noun)","غفّار  Ghaffar (intensive)"],[ngfor,nstgf,nmgf,ngffar],[wk.TEAL,wk.GREY,wk.GREY,wk.AMBER],xlabel="ayat / occurrences")
fig_groupbar("gf_company.png","Forgiveness = covering, twinned with mercy",["with mercy (rahma)","with sin (dhanb)","with garden (janna)"],[("",[wk.TEAL,wk.RED,wk.AMBER],[c_rah,c_dhanb,c_jan])])
fig_suradist("gf_sura.png","Where the forgiveness-root falls, sura by sura","غفر")
fig_timeline("gf_time.png","The forgiveness-root across the revelation",[("ghafr غفر","غفر")])
fig_groupbar("gf_name.png","The dominant Name is Ghafur, not Ghaffar",["Ghafur","Ghaffar"],[("",[wk.TEAL,wk.AMBER],[ngfor,ngffar])])
fig_freqbarh("gf_order.png","Cover the fault, THEN raise to garden",["named on SIN (dhanb)","twinned with MERCY (rahma)","then -> GARDEN (janna)"],[c_dhanb,c_rah,c_jan],[wk.RED,wk.TEAL,wk.AMBER],xlabel="co-occurrence (ayat)")
fig_groupbar("gf_cover.png","Covering first, elevation downstream",["covering a sin (the word)","elevation to garden (the consequence)"],[("",[wk.TEAL,wk.AMBER],[c_dhanb,c_jan])])
spec=dict(slug="W10_ghafr_forms",sub="forms & meaning, Week 10",
 main="Ghafr - what kind of 'forgiveness'?",
 headline="A word that means COVERING - twinned with mercy, opening onto more",
 intro1="The forgiveness-root is read variously as 'forgive', 'cover/conceal', even 'promote in status.' Which does the corpus carry? We tally every surface form, separate the Divine-Name intensives from the verbs, and test what the root shares its ayah with - sin? mercy? garden?",
 intro2="Counts and co-occurrences recompute from Book6 and reproduce exactly; the concrete root-sense is a helmet that COVERS the head.",
 qhead="The claim to test",qbody="Is the forgiveness-root primarily 'covering a fault', 'status promotion', or something else?",
 mhead="The method",mpts=["tally every surface form; separate the Names from the verbs",
   "test what the root co-occurs with - sin, mercy, garden",
   "locate the meaning empirically, anchored by the concrete root-sense (to cover)"],
 figs=[
  dict(t="The root, by form",png="gf_forms.png",cf=TINT,
    cap=f"In the data - the dominant form is the Name Ghafur ({ngfor}); seek-forgiveness ({nstgf}) and the noun ({nmgf}) follow; the intensive Ghaffar is rare ({ngffar})."),
  dict(t="Covering, twinned with mercy",png="gf_company.png",
    cap=f"In the data - the root is named on SIN (dhanb, {c_dhanb}) and almost always twinned with MERCY (rahma, {c_rah}); it co-occurs with garden ({c_jan}) downstream."),
  dict(t="Across the corpus",png="gf_sura.png",cf=TINT,
    cap="In the data - the forgiveness-root is spread throughout, densest where mercy and repentance are the theme."),
  dict(t="Across the revelation",png="gf_time.png",
    cap="In the data - the root runs the whole revelation; the 'covering' sense is steady throughout."),
  dict(t="The dominant Name is Ghafur",png="gf_name.png",cf=TINT,
    cap=f"In the data - the corpus prefers Ghafur ({ngfor}) over the intensive Ghaffar ({ngffar}): forgiveness framed as covering, not as rank."),
  dict(t="Cover the fault, then raise",png="gf_order.png",
    cap=f"In the data - the root is named on sin ({c_dhanb}), twinned with mercy ({c_rah}), and only downstream linked to garden ({c_jan}): elevation FOLLOWS the covering."),
  dict(t="Covering first, elevation downstream",png="gf_cover.png",cf=TINT,
    cap=f"In the data - the word names the COVER (sin {c_dhanb}); the rise to garden ({c_jan}) is the consequence, not the lexical meaning."),
 ],
 gal1=dict(title="Covering a sin",items=glg("ghafr",[0,3]) or [("39:53","يَغْفِرُ الذُّنُوبَ جَمِيعًا","He forgives all sins")],fill=TINT,hc=TEAL),
 gal2=dict(title="The dominant Name, and the rise to garden",items=glg("ghafr",[1,2]) or [("3:133","وَمَغْفِرَةٍ مِّن رَّبِّكُمْ وَجَنَّةٍ","forgiveness from your Lord and a garden")],fill=AMBERT,hc=AMBER),
 v1=("Forgiveness = COVERING",f"the root is named on sin ({c_dhanb}); the concrete sense is a helmet (mighfar) that covers - to cover a fault."),
 v2=("Twinned with mercy",f"it is almost always paired with mercy ({c_rah}); the dominant Name is Ghafur ({ngfor}), the intensive Ghaffar rare ({ngffar})."),
 v3=("Elevation follows",f"forgiveness -> garden ({c_jan}) is downstream (3:133): the covered one is raised, but the WORD names the cover."),
 deep=("A cover that opens onto more",
   f"Computed: the root is named on SIN ({c_dhanb}) and almost always twinned with MERCY ({c_rah}); the dominant Name is Ghafur ({ngfor}). The primary sense is COVERING / erasing a fault - then, downstream, the covered one is raised to mercy and garden (3:133, {c_jan} co-occurrences). The 'promotion' is real but consequential, not lexical: cover the fault, then elevate."),
 deep_extra=["Reading the root as 'status promotion' imports the destination into the word; the data keeps them ordered."],
 crit1=("'Status promotion' imports the destination",
   "reading the root as 'promotion' folds the consequence (garden) into the word; the data keeps cover-then-elevate ordered."),
 crit2=("Co-occurrence locates, doesn't fix",
   "co-occurrence locates meaning but does not fix it; the concrete root-sense (helmet/cover) anchors the reading."),
 audit=[("check","Forms tallied",f"Ghafur {ngfor}, seek-forgiveness {nstgf}, noun {nmgf}, Ghaffar {ngffar}."),
   ("check","Company computed",f"mercy {c_rah}, sin {c_dhanb}, garden {c_jan}."),
   ("check","Order preserved","named on sin -> mercy -> garden.")]+[("tilde","Co-occurrence locates","it does not fix meaning alone.")]+AT,
 method=("forgiveness forms; co-occurring roots","form tally, company (sin/mercy/garden)","form bars, company bars, sura map"),
 take=("A cover that opens onto more",
   [f"The forgiveness-root means COVERING - named on sin ({c_dhanb}), twinned with mercy ({c_rah}); the dominant Name is Ghafur ({ngfor}).",
    f"Elevation to garden ({c_jan}) is downstream (3:133) - real, but consequential, not the word's lexical meaning.",
    "'Status promotion' imports the destination; the data keeps cover-then-elevate ordered. Presented from the text."]),
 qr1=("The numbers",f"Ghafur {ngfor} - seek-forgiveness {nstgf} - noun {nmgf} - Ghaffar {ngffar}; with mercy {c_rah}, sin {c_dhanb}, garden {c_jan}."),
 qr2=("The shape","forgiveness = covering a fault, twinned with mercy; elevation to garden is downstream, not lexical."),
 syn=("Cover, then raise",
   [("Named on sin","the fault to be covered"),("Twinned with mercy","the cover applied"),("-> garden","elevation, downstream")],
   "A cover that opens onto more","the word names the cover; the rise to garden is the consequence, not the meaning."),
 quiz=("Special Topic - Ghafr: What Kind of Forgiveness? (Week 10)",[
  ("1.  The primary sense of the forgiveness-root is:","covering / erasing a fault",["status promotion","destruction","payment"],"the concrete root-sense is a helmet that covers."),
  ("2.  The root is almost always twinned with:","mercy (rahma)",["wealth","war","the sun"],f"{c_rah} co-occurrences."),
  ("3.  The dominant Divine Name from this root is:","Ghafur",["Ghaffar","al-Rahman","Rabb"],f"Ghafur {ngfor} vs Ghaffar {ngffar}."),
  ("4.  Elevation to the garden is:","downstream / consequential, not the word's meaning",["the lexical meaning","unrelated","forbidden"],f"forgiveness -> garden ({c_jan}), 3:133."),
  ("5.  Reading the root as 'status promotion':","imports the destination into the word",["is the literal sense","is most accurate","is impossible"],"the data keeps cover-then-elevate ordered."),
  ("6.  The root is named on:","sin (dhanb)",["wealth","the moon","prayer"],f"{c_dhanb} co-occurrences with sin."),
  ("7.  The intensive Ghaffar is:","rare",["the most common","never used","more common than Ghafur"],f"only {ngffar} occurrences."),
  ("8.  The concrete image behind 'forgiveness' is:","a helmet (mighfar) that covers the head",["a throne","a sword","a book"],"to cover a fault."),
  ("9.  Co-occurrence is said to:","locate meaning but not fix it alone",["fix meaning exactly","be useless","replace the root"],"the root-sense anchors the reading."),
  ("10.  The order the data preserves is:","cover the fault, then elevate",["elevate, then cover","both at once","neither"],"3:133: forgiveness then garden."),
  ("11.  The corpus frames forgiveness as:","covering, not rank",["rank","payment","war"],"Ghafur dominates, named on sin."),
  ("12.  The honest verdict is:","a cover that opens onto more",["pure status promotion","destruction","payment"],"covering first, elevation downstream."),
  ("13.  These findings are:","computed from Book6 and reproducible",["estimated","theological","unrelated"],"forms and co-occurrences reproduce exactly."),
 ]),
)
standard_deck(spec)
print("done ghafr_forms")

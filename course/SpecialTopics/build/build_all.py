# -*- coding: utf-8 -*-
import sys, json
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/SpecialTopics/build")
from st_slides import *  # includes ebar, finding2, LTEAL
OUT="/sessions/kind-compassionate-feynman/mnt/RootCourse/SpecialTopics/"
S1=json.load(open("snippets.json",encoding="utf-8"))      # mukhlis, bashir_nadhir
SD=json.load(open("snip_din.json",encoding="utf-8"))
SG=json.load(open("snip_ghafr.json",encoding="utf-8"))
SW=json.load(open("snip_sword.json",encoding="utf-8"))
SA=json.load(open("snip_address.json",encoding="utf-8"))
SO=json.load(open("snip_order.json",encoding="utf-8"))
SS=json.load(open("snip_actstate.json",encoding="utf-8"))
SC=json.load(open("snip_scope.json",encoding="utf-8"))
SU=json.load(open("snip_unit.json",encoding="utf-8"))
EQ=json.load(open("snip_equity.json",encoding="utf-8"))
B2=json.load(open("snip_batch2.json",encoding="utf-8"))
B3=json.load(open("snip_batch3.json",encoding="utf-8"))
GN=json.load(open("snip_genome.json",encoding="utf-8"))
def _save(prs,path):
    import os
    try: prs.save(path); print("saved", os.path.basename(path))
    except PermissionError: print("LOCKED (open in PowerPoint) — skipped", os.path.basename(path))

# ===== 1. MUKHLIS (Week 3 forms) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 3 (forms) — مُخلِص or مُخلَص? one mark on the lām, two theologies",20)
two_stack(s,
 [L("THE PUZZLE",18,True,RED),
  L("Unvocalized, مخلص is one spelling. The vowel on the lām forks it into two words of opposite voice:",17.5),
  L("kasra → مُخلِص (active): the one who MAKES his religion sincere — a human act.",17.5,True,TEAL),
  L("fatḥa → مُخلَص (passive): the one God HAS MADE sincere / chosen — a divine act.",17.5,True,AMBER)],
 [L("THE METHOD  (only data — no interpretation)",18,True,NAVY),
  L("• Voice — read the ḥarakah on the lām straight from the vocalized text (Book6 col 11).",17),
  L("• Number — from the surface suffix: ـًا singular vs ـِين / ـُون plural.",17),
  L("• Definiteness — from the article (ال). All 20 participle occurrences classified, then matched to their ayah’s roots.",17)],
 split=0.46,fillA=REDT,fillB=TINT2)
s=slide(prs); title(s,"Special Topic · Week 3 — the two halves live in different worlds")
finding2(s,
 {"title":"Company each keeps","cats":["مُخلِص","مُخلَص"],
  "series":[("with دين (religion)",TEAL,[10,0]),("with عبد (servants)",AMBER,[4,8])]},
 {"title":"Counts","cats":["مُخلِص","مُخلَص"],
  "series":[("singular",GREY,[3,1]),("plural",TEAL,[8,8])]},
 [L("ACTIVE مُخلِص (kasra) — 11",17.5,True,TEAL),
  L("The human’s act: “making the religion sincerely His.”",16),
  L("10 of 11 with دين; all indefinite.",16,True,NAVY)],
 [L("PASSIVE مُخلَص (fatḥa) — 9",17.5,True,AMBER),
  L("God’s election: “the chosen servants.” 8 of 9 with عبد.",16),
  L("Joseph 12:24, Moses 19:51; the Iblīs exception 15:40, 38:83.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 3 — effort meets grace (and the reading that carries it)",20)
two_stack(s,
 [L("THE VERDICT  (interpretation)",18,True,NAVY),
  L("You STRIVE as مُخلِص — make your religion sincere; that is the command, in the indefinite plural.",17.5),
  L("Being made مُخلَص — Satan-proof, named among the chosen — is God’s to give; it mirrors يُزكّيهم (“He purifies them”).",17.5),
  L("One root holds both halves of the synthesis: حسن فاعلي and the grace that completes it.",17.5,True,TEAL)],
 [L("THE CAVEAT — Lesson #9 in the flesh",18,True,RED),
  L("This kasra/fatḥa is the Ḥafṣ reading the corpus encodes; 12:24, 15:40, the al-Ṣāffāt series, 38:83, 19:51 are known qirāʾāt variant points — other readers vocalize some the opposite way.",17),
  L("A true diacritic can still carry a claim that rests on a single reading.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
mk=S1["mukhlis"]
appendix(s if False else slide(prs),[]) if False else None
s=slide(prs); title(s,"Special Topic · Week 3 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[
 ("ACTIVE مُخلِص — “…making the religion sincerely His”",TEAL,TINT,
   [(x["ref"],x["snip"],"active · kasra") for x in mk if x["voice"]=="active"]),
 ("PASSIVE مُخلَص — “…of the chosen servants”",AMBER,AMBERT,
   [(x["ref"],x["snip"],"passive · fatḥa") for x in mk if x["voice"]=="passive"]),
])
_save(prs,OUT+"SpecialTopic_W03_mukhlis.pptx"); print("mukhlis",len(prs.slides))

# ===== 2. BASHIR / NADHIR (Week 1 frequency) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 1 (frequency) — is the Qur’an more about إنذار (warning) or تبشير (glad tidings)?",18)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("“Essentially a book of glad tidings” — or its opposite, “essentially warning.” Either way, an either/or.",17.5),
  L("Critical first move: this may be a FALSE dichotomy — warning and tidings could be two faces of one prophetic act.",17.5,True,RED)],
 [L("THE METHOD  (surface-form discipline — both roots are polysemous)",18,True,TEAL),
  L("• بشر = glad-tidings AND human/mortal;  نذر = warn AND vow. Each token sense-filtered from the vocalized text.",17),
  L("• Count true warning vs true tidings; the messenger’s ROLE; pairing rate and order.",17),
  L("• Watch the trap: بشّر is sometimes agnostic — “فبَشِّرْهُ بعذابٍ أليم”, tidings OF punishment.",17,True,NAVY)],
 split=0.4,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 1 — close in the corpus, lopsided in the role")
finding2(s,
 {"title":"Field size (ayahs)","cats":["إنذار","تبشير","glad-net"],
  "series":[("",[AMBER,TEAL,LTEAL],[113,91,82])],"legend":False},
 {"title":"Messenger’s role","cats":["نذير","بشير"],
  "series":[("",[AMBER,TEAL],[41,12])],"legend":False},
 [L("WARNING is larger",17.5,True,AMBER),
  L("113 vs 91 ayahs; 9 “tidings” announce punishment (net ≈ 82).",16),
  L("As a ROLE, warner beats herald 41 to 12 (~3.4×).",16,True,NAVY)],
 [L("YET tidings comes FIRST",17.5,True,TEAL),
  L("When paired (5:19, 35:24): بَشيرًا وَنَذيرًا — herald before warner.",16),
  L("Warning is the volume; mercy is the framing.",16,True,NAVY)],
 fillA=AMBERT,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 1 — verdict: the question is half wrong",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Leaning WARNING — modestly in distribution (113 vs 91 ≈ 1.24×; ≈1.38× net of ironic tidings)…",17.5),
  L("…and strongly as a ROLE: “I am only a clear WARNER” (نذير مبين) — warner 41, herald 12.",17.5),
  L("But the either/or is half wrong: the corpus binds them (بشيرًا ونذيرًا) and leads with tidings. Warning is the volume; mercy the framing.",17.5,True,TEAL)],
 [L("CRITIQUE OF THE SUGGESTION",18,True,RED),
  L("“More about X or Y” forces one axis onto a two-channel signal. The honest finding is a SHAPE, not a winner.",17),
  L("And a measurement trap survives only because we sense-checked it: counting بشّر as “good news” would inflate tidings by the very verses that threaten punishment.",17,True,NAVY)],
 split=0.54,fillA=TINT,fillB=REDT)
bn=S1["bashir_nadhir"]
s=slide(prs); title(s,"Special Topic · Week 1 — Appendix: input snippets (sampled; Book6 col 11)",19)
appendix(s,[
 ("TRUE glad tidings (بشّر + mercy / garden)",TEAL,TINT,[(x["ref"],x["snip"],x["tag"]) for x in bn if x["tag"]=="glad tidings"][:2]),
 ("AGNOSTIC ‘tidings’ — of punishment",RED,REDT,[(x["ref"],x["snip"],x["tag"]) for x in bn if "punishment" in x["tag"]][:2]),
 ("WARNER role (نذير / بشيرًا ونذيرًا)",AMBER,AMBERT,[(x["ref"],x["snip"],x["tag"]) for x in bn if "warner" in x["tag"]][:2]),
])
_save(prs,OUT+"SpecialTopic_W01_bashir_nadhir.pptx"); print("bashir_nadhir",len(prs.slides))

# ===== 3. DIN / ISLAM / QURAN (Week 3) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 3 — is دين the same as إسلام, or قرآن, or both, or neither?",19)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("People use دين, إسلام and قرآن almost interchangeably for “the religion.” Are they one thing in the corpus — or three?",17.5)],
 [L("THE METHOD  (surface-form discipline — all three roots are polysemous)",18,True,TEAL),
  L("• دين = religion / Day-of-Judgment / debt;  سلم = submission(Islam) / peace / Solomon;  قرء = Qur’an / to recite / periods.",17),
  L("• Sense-filter each token; then ask: do the three roots ever share an ayah? what does each pair with?",17),
  L("• Equivalence leaves a fingerprint — synonyms co-occur and gloss each other. Test for it; don’t assume it.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 3 — three words, three categories")
finding2(s,
 {"title":"Shared ayahs","cats":["دين·إسلام","دين·قرآن","إسلام·قرآن"],
  "series":[("",[TEAL,RED,RED],[7,0,0])],"legend":False},
 {"title":"دين — three senses","cats":["religion","Judgment","debt"],
  "series":[("",[TEAL,AMBER,GREY],[72,13,2])],"legend":False},
 [L("دين ≈ إسلام — partly",17.5,True,TEAL),
  L("7 shared ayahs — the identity verses (3:19, 5:3).",16),
  L("إسلام = the specific دين accepted (3:85); دين is broader.",16,True,NAVY)],
 [L("قرآن — neither",17.5,True,RED),
  L("Zero shared ayahs; it pairs with Book, sent-down, reminder.",16),
  L("قرآن is the recited TEXT — the vehicle, not the religion.",16,True,NAVY)],
 fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 3 — verdict: a genus, a species, and a Book",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("• دين is the GENUS — a way / religion (72), also “the Reckoning” (Day of Judgment, 13) and even “debt” (2). It can be anyone’s: “to you your دين, to me mine” (109:6).",16.5),
  L("• إسلام is the SPECIES — the one دين God names as accepted. So دين ⊇ إسلام: equivalent only in the chosen case.",16.5),
  L("• قرآن is the BOOK — the recited text that carries the دين. Neither دين nor إسلام; the vehicle, not the destination.",16.5,True,TEAL)],
 [L("CRITIQUE OF THE SUGGESTION",18,True,RED),
  L("“دين = إسلام = قرآن” is a folk shortcut the corpus only half-supports. Zero co-occurrence is blunt, but the corpus never lexically equates قرآن with the religion, and reserves the identity strictly for دين↔إسلام.",16.5),
  L("Most “دين = Islam” claims quietly ignore the 13 “Day of Judgment” uses and the debt of 2:282.",16.5,True,NAVY)],
 split=0.52,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 3 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[
 ("دين — the three senses",AMBER,AMBERT,[(e["ref"],e["snip"],e["tag"]) for e in SD if ("Judgment" in e["tag"] or "debt" in e["tag"] or "each one" in e["tag"])]),
 ("دين = إسلام — the identity verses",TEAL,TINT,[(e["ref"],e["snip"],e["tag"]) for e in SD if ("identity" in e["tag"] or "approved" in e["tag"] or "accepted" in e["tag"])]),
 ("قرآن — the Book / sent down",RED,REDT,[(e["ref"],e["snip"],e["tag"]) for e in SD if "قرآن" in e["tag"]]),
])
_save(prs,OUT+"SpecialTopic_W03_din_islam_quran.pptx"); print("din",len(prs.slides))

# ===== 4. GHAFR forms (Week 10) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 10 (forms) — غفر: what kind of “forgiveness”?",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("غفر is read variously as “forgive”, “cover/conceal”, even “promote in status.” Which does the corpus actually carry?",17.5),
  L("Anchor (to the Prophet): “…فاستغفره إنه كان توّابا” — seek His covering. (110:3)",17.5,True,TEAL)],
 [L("THE METHOD",18,True,TEAL),
  L("• Tally every غفر surface form (Book6 col 9); separate the Divine-Name intensives from the verbs.",17),
  L("• Test what غفر shares its ayah with — sin? mercy? garden/elevation? — to locate its meaning empirically.",17),
  L("• The root sense is concrete: مِغْفَر = a helmet that COVERS the head; forgiveness = covering a fault.",17,True,NAVY)],
 split=0.42,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 10 — covering, twinned with mercy")
finding2(s,
 {"title":"غفر forms","cats":["غفور","verb","مغفرة","استغفر","غفّار"],
  "series":[("",[TEAL,GREY,GREY,GREY,AMBER],[71,54,28,37,4])],"legend":False},
 {"title":"غفر shares its ayah with","cats":["رحمة","ذنب","جنة"],
  "series":[("",[TEAL,RED,AMBER],[91,19,9])],"legend":False},
 [L("Forgiveness = COVERING",17.5,True,TEAL),
  L("غفر is named on sin (ذنب 19). The Name is Ghafūr (71); Ghaffār rare (4).",16),
  L("The corpus frames it as covering, not rank.",16,True,NAVY)],
 [L("“Status promotion” — scoped",17.5,True,AMBER),
  L("A downstream echo: مغفرة → جنّة in 3:133; غفر+garden = 9.",16),
  L("Elevation FOLLOWS the covering; the word names the cover.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 10 — verdict: a cover that opens onto more",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: غفر is named on SIN (ذنب 19) and almost always twinned with MERCY (رحمة 91); the Name is Ghafūr (71).",17.5),
  L("Interpretation: the primary sense is COVERING / erasing a fault — then, downstream, the covered one is raised to mercy and garden (3:133). The “promotion” is real but consequential, not lexical.",17.5,True,TEAL)],
 [L("CRITIQUE OF THE SUGGESTION",18,True,RED),
  L("Reading غفر as “status promotion” imports the destination into the word. The data keeps them ordered: cover the fault → then elevate.",17),
  L("Honest limit: co-occurrence locates meaning but does not fix it; the concrete root-sense (helmet/cover) anchors the reading.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
g=SG["ghafr"]
s=slide(prs); title(s,"Special Topic · Week 10 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[
 ("COVERING a sin",TEAL,TINT,[(g[0]["ref"],g[0]["snip"],g[0]["tag"]),(g[3]["ref"],g[3]["snip"],g[3]["tag"])]),
 ("the dominant Name: Ghafūr",AMBER,AMBERT,[(g[1]["ref"],g[1]["snip"],g[1]["tag"])]),
 ("forgiveness → garden (the rise)",RED,REDT,[(g[2]["ref"],g[2]["snip"],g[2]["tag"])]),
])
_save(prs,OUT+"SpecialTopic_W10_ghafr_forms.pptx"); print("ghafr",len(prs.slides))

# ===== 5. GHAFFAR vs TAWWAB + why 110:3 (Week 10) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 10 — غفّار vs توّاب, and why “…إنه كان توّابا” (not غفّارا)",19)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("Both غفّار and توّاب are intensive Divine Names. Are they synonyms? And why does 110:3, after the command “seek forgiveness” (استغفره), name God توّاب — not the more “natural” غفّار?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Collect every occurrence of each Name; record the Name it is PAIRED with, and the roots in its ayah.",17),
  L("• غفر = to cover (unilateral: God conceals the fault). توب = to turn / return (bilateral: the servant turns, and God turns back).",17),
  L("• Read 110:3 in its own context — victory, people entering “in crowds” — and ask which intensive the scene calls for.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 10 — covering vs returning")
finding2(s,
 {"title":"Name-partners","cats":["الغفّار","التوّاب"],
  "series":[("with al-ʿAzīz (Mighty)",AMBER,[3,0]),("with al-Raḥīm (Merciful)",TEAL,[0,8])]},
 {"title":"What each is about","cats":["غفر·ذنب","توب·عبد","توب·ذنب"],
  "series":[("",[AMBER,TEAL,GREY],[19,5,2])],"legend":False},
 [L("GHAFFĀR — covers, with MIGHT",17.5,True,AMBER),
  L("4×; pairs with al-ʿAzīz 3× (39:5, 40:42, 38:66). About erasing SIN.",16),
  L("A sovereign concealing faults.",16,True,NAVY)],
 [L("TAWWĀB — returns, with MERCY",17.5,True,TEAL),
  L("8×; pairs with al-Raḥīm. Bilateral: “He turned to them so they would turn” (9:118).",16),
  L("A relationship restored, not just a record wiped.",16,True,NAVY)],
 fillA=AMBERT,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 10 — the latent nuance of 110:3",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("The command uses استغفر (seek COVERING, from غفر); the Name given is توّاب (the ever-RETURNING). The verse pairs a request for covering with a God who turns BACK to you — more than a cover, a restored bond.",17),
  L("Why not غفّار? Sūrat al-Naṣr is not about sin — it is about RETURN: victory won, the mission’s end, people entering the religion “in crowds.” The scene calls for the God who receives the turning, not merely one who conceals faults.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("غفّار would have narrowed the moment to sin-erasure; توّاب widens it to mutual turning — the fitting close to a life of mission. (تواب also rhymes the sūra’s ـابا cadence — a formal echo, not the cause.)",16.5),
  L("Limit: this is a reading of placement and collocation, not a proof; but the company each Name keeps (might vs mercy) is computed, not assumed.",16.5,True,NAVY)],
 split=0.54,fillA=TINT,fillB=REDT)
gt=SG["ghaffar_tawwab"]
s=slide(prs); title(s,"Special Topic · Week 10 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[
 ("GHAFFĀR — might & condition",AMBER,AMBERT,[(gt[0]["ref"],gt[0]["snip"],gt[0]["tag"]),(gt[1]["ref"],gt[1]["snip"],gt[1]["tag"]),(gt[2]["ref"],gt[2]["snip"],gt[2]["tag"])]),
 ("TAWWĀB — mercy & mutual turning",TEAL,TINT,[(gt[3]["ref"],gt[3]["snip"],gt[3]["tag"]),(gt[4]["ref"],gt[4]["snip"],gt[4]["tag"])]),
 ("110:3 — seek covering, meet the Returner",RED,REDT,[(gt[5]["ref"],gt[5]["snip"],gt[5]["tag"])]),
])
_save(prs,OUT+"SpecialTopic_W10_ghaffar_vs_tawwab.pptx"); print("ghaffar_tawwab",len(prs.slides))

# ===== 6. SWORD vs PEACE (Week 9 interpretation) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — does Islam rule by the sword or by peace?",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("A loaded either/or: “Islam spread by the sword” vs “Islam is a religion of pure peace.” The corpus is the referee.",17.5),
  L("First data point that reframes it: the literal word سيف (sword) never occurs in the Qur’an — not once.",17.5,True,RED)],
 [L("THE METHOD  (sense-filtered — raw counts mislead)",18,True,TEAL),
  L("• قتل is mostly “kill / murder”, not war; صلح is mostly “righteous deeds”; سلم also = Islam / Solomon. So count FORMS, not roots.",17),
  L("• Separate combat (qitāl / qātala) from killing; weigh the war-words against the conditions placed on them.",17),
  L("• Then read the command verses in context: who, when, and with what limits.",17,True,NAVY)],
 split=0.42,fillA=REDT,fillB=TINT2)
s=slide(prs); title(s,"Special Topic · Week 9 — the sword is absent; combat is a hedged minority")
finding2(s,
 {"title":"War vocabulary","cats":["سيف","حرب","قتال","جهد"],
  "series":[("",[RED,AMBER,AMBER,GREY],[0,11,66,36])],"legend":False},
 {"title":"قتل root: killing vs combat","cats":["kill / murder","combat"],
  "series":[("",[GREY,AMBER],[104,66])],"legend":False},
 [L("The SWORD is absent",17.5,True,RED),
  L("سيف = 0. War-words exist (combat 66, war 11) but are a minority even of the killing-root.",16),
  L("No lexical basis for “the sword.”",16,True,NAVY)],
 [L("Killing ≠ war",17.5,True,AMBER),
  L("104 of the قتل root are killing/murder — much of it CONDEMNED (“who kills one soul kills all”, 5:32).",16),
  L("Only 66 are mutual combat (qitāl).",16,True,NAVY)],
 fillA=REDT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 9 — verdict: conditioned combat inside a default of peace",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Neither slogan holds. Combat is permitted but CONDITIONED: defensive (“fight those who fight you”, 2:190), bounded (“do not transgress”), suspended on the enemy’s peace (“if they incline to peace, incline to it”, 8:61).",17),
  L("And belief is left free: “no compulsion in religion” (2:256); be just to those who do not fight you (60:8).",17,True,TEAL)],
 [L("CRITIQUE OF THE SUGGESTION",18,True,RED),
  L("“Rules by the sword” has no lexical basis (سيف = 0) and ignores the conditions; “pure pacifism” ignores the real qitāl commands. Both cherry-pick.",17),
  L("Raw counts would mislead either way — صلح is mostly “righteous deeds”, قتل mostly “killing”, سلم also “Islam/Solomon”. Only sense-filtered forms were counted.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pick(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SW if e["ref"] in refs]
appendix(s,[
 ("Fighting is CONDITIONED",AMBER,AMBERT,pick({"2:190","60:8"})),
 ("Peace & no compulsion",TEAL,TINT,pick({"8:61","2:256","49:9"})),
 ("Killing CONDEMNED",RED,REDT,pick({"5:32"})),
])
_save(prs,OUT+"SpecialTopic_W09_sword_or_peace.pptx"); print("sword_or_peace",len(prs.slides))


# ===== 7. WHO THE QURAN ADDRESSES (Week 1 frequency & address) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 1 — who does the Qur’an address?",20)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("Is the Qur’an speaking to everyone, to one community, or to its opponents? And does it name groups as fixed identities or as ongoing acts?",17.5)],
 [L("THE METHOD  (root + surface + morphology together)",18,True,TEAL),
  L("• Separate the NOUN of a group (المؤمنون = the believers, a category) from the VERBAL phrase (الذين آمنوا = those who came to believe, an act).",17),
  L("• Separate MENTION (named anywhere) from ADDRESS (the vocative “يا أيها …”). And track the speech frame: قُل (“Say!”) vs قالوا (“they said”).",17),
  L("• Counting roots alone would blur all of this — so we count forms and phrases.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 1 — named as identity AND act; addressed in community")
finding2(s,
 {"title":"Named: noun vs verbal","cats":["مؤمنون / آمنوا","كافرون / كفروا"],
  "series":[("noun (category)",TEAL,[224,159]),("verbal (act)",AMBER,[219,152])]},
 {"title":"Who is called “O…!”","cats":["آمنوا","الناس","النبي","إسرائيل"],
  "series":[("",[TEAL,AMBER,NAVY,GREY],[89,20,13,6])],"legend":False},
 [L("Identity AND act",17.5,True,TEAL),
  L("Believers & disbelievers are each named ~half as a fixed NOUN and half as an ongoing VERB (الذين آمنوا / كفروا).",16),
  L("Faith and denial are processes, not only labels.",16,True,NAVY)],
 [L("Addressed in-community",17.5,True,AMBER),
  L("Direct “O…!” goes to believers 89×, mankind only 20×, the Prophet 13×.",16),
  L("A universal frame, a community focus.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 1 — a community address inside a universal frame, in dialogue",18)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Primary addressee = the believing community (89 vocatives), set inside a universal frame: الناس (mankind) is named 241× and called 20×.",17),
  L("And it is a scripted DIALOGUE — God tells the Prophet “Say!” (قُل) 379× and quotes opponents “they said” (قالوا) 314×. A back-and-forth, not a monologue.",17,True,TEAL)],
 [L("CRITIQUE — where naïve counting fails",18,True,RED),
  L("Mention ≠ address: الناس is named 241× but directly called only 20× — counting mentions would overstate the universal address.",17),
  L("Noun vs verbal must be split: collapsing الذين آمنوا into المؤمنون erases the identity-vs-act distinction. Root + surface + morphology keep the concepts apart.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 1 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pk(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SA if e["ref"] in refs]
appendix(s,[
 ("UNIVERSAL — “O mankind”",AMBER,AMBERT,pk({"49:13","2:21","3:64"})),
 ("COMMUNITY — “O believers”",TEAL,TINT,pk({"5:1","2:104"})),
 ("DIALOGUE — Say / they said",NAVY,TINT2,pk({"112:1","109:1","2:11"})),
])
_save(prs,OUT+"SpecialTopic_W01_who_addressed.pptx"); print("who_addressed",len(prs.slides))


# ===== 8. MUSHAF ORDER vs REVELATION ORDER (Week 2 distribution) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 2 — why is the Qur’an’s order not its revelation order?",19)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("The Qur’an was revealed over ~23 years, but the written order (muṣḥaf) is not chronological. What rule governs the arrangement instead?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Use the revelation-order index (Book6 col 12) for every sūra; compare it to the muṣḥaf position (1–114) and to sūra length.",17),
  L("• Correlate the three; bin the muṣḥaf into quarters; read off the landmark sūras.",17),
  L("• Resolution is the SŪRA, not the ayah: the revelation rank is a per-sūra order taken from historical narration and aḥādīth — not computed, and a single sūra can mix Meccan and Medinan verses.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 2 — graded by length, not by time")
finding2(s,
 {"title":"Landmark sūras: position vs timing","cats":["Fātiḥa","Baqara","ʿAlaq","Tawba"],
  "series":[("muṣḥaf #",TEAL,[1,2,96,9]),("revelation #",AMBER,[5,87,1,114])]},
 {"title":"Avg length by muṣḥaf quarter (ayahs)","cats":["Q1","Q2","Q3","Q4"],
  "series":[("",[NAVY,TEAL,LTEAL,GREY],[119,61,30,11])],"legend":False},
 [L("Arranged by LENGTH, not time",17.5,True,TEAL),
  L("The muṣḥaf runs longest→shortest (Q1 ≈119 ayahs → Q4 ≈11). Its correlation with revelation order is only −0.41.",16),
  L("Length is the visible organizing rule.",16,True,NAVY)],
 [L("The first becomes the 96th",17.5,True,AMBER),
  L("al-ʿAlaq (“Read!”, revealed 1st) sits at position 96; al-Tawba (revealed last, 114th) at position 9; al-Fātiḥa (#1) was revealed 5th.",16),
  L("Position encodes no chronology.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 2 — a thematic order, not a timeline",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: the canonical order is non-chronological (corr −0.41) and graded by descending length, clustering the short early-Meccan sūras at the end (Q4 avg revelation-rank 29 vs ~67 elsewhere).",17),
  L("Interpretation (labelled, historical): tradition holds the order was prophet-directed and liturgical — a thematic/structural arrangement, not a biography. The data shows the shape; the reason lies outside the text.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Length is a strong but imperfect rule — al-Fātiḥa is short yet first (an opening, not the longest). So “longest-first” is a tendency, not a law.",17),
  L("Revelation order is NARRATED (sīra & aḥādīth), not data-derived — and only at the sūra level (Meccan/Medinan verses mix within a sūra). So the timeline itself is an approximation; we map WHAT the order is and decline to compute WHY.",16,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 2 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pk(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SO if e["ref"] in refs]
appendix(s,[
 ("FIRST & LAST revealed",AMBER,AMBERT,pk({"96:1","9:1"})),
 ("Opening of the muṣḥaf",TEAL,TINT,pk({"1:2","2:1"})),
 ("Short Meccan, placed late",NAVY,TINT2,pk({"108:1","110:1"})),
])
_save(prs,OUT+"SpecialTopic_W02_mushaf_vs_revelation.pptx"); print("mushaf_order",len(prs.slides))


# ===== 9. VERB-ACT vs NOUN-IDENTITY (Week 3 forms) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 3 — الذين آمنوا vs مؤمن: a journey, or an instilled state?",19)
two_stack(s,
 [L("THE NUANCE",18,True,NAVY),
  L("Arabic marks DOING apart from BEING. الذين آمنوا (relative + perfect verb) = those who came to believe — an act, a journey. مؤمن (participle/noun) = a believer — faith as a settled, instilled trait.",17.5),
  L("The same split runs through كفر (act vs hardened كفّار) and صلح (doing good vs being good vs making good).",17.5,True,TEAL)],
 [L("THE METHOD  (root + surface + morphology — never mix the concepts)",18,True,TEAL),
  L("• Count the VERBAL phrase (الذين آمنوا) apart from the NOUN (المؤمنون); the intensive (كفّار) apart from the plain (كافر).",17),
  L("• For صلح, separate four forms: الصالحات (deeds) · صالح (a righteous person) · مصلح (an active reformer) · إصلاح (reconciliation).",17,True,NAVY)],
 split=0.5,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 3 — named as act AND as state; good vs reform")
finding2(s,
 {"title":"Act (verb) vs settled state (noun)","cats":["faith","disbelief","righteous"],
  "series":[("verb — act",AMBER,[219,152,51]),("noun — state",TEAL,[224,135,38])]},
 {"title":"صلح: three distinct forms","cats":["الصالحات","صالح","مصلح"],
  "series":[("",[TEAL,LTEAL,AMBER],[98,38,5])],"legend":False},
 [L("Doing AND being",17.5,True,TEAL),
  L("Each family is named ~half as a VERB (an act in progress) and ~half as a NOUN (a settled trait). كفّار (hardened ingrate) is a separate intensive class (26).",16),
  L("Morphology marks journey vs arrival.",16,True,NAVY)],
 [L("Being good vs MAKING good",17.5,True,AMBER),
  L("صلح splits: 98 righteous-deeds, 38 righteous-persons (صالح) — but only 5 reformers (مصلح), who actively make-good.",16),
  L("11:117: towns are spared as مصلحون, not merely صالحون.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 3 — the grammar is the theology",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("49:14 says it outright: the Bedouins’ claim “آمنّا” (verb) is rejected — “faith has not yet entered your hearts.” The act is a journey, not the instilled state.",17),
  L("Salvation’s signature formula — الذين آمنوا وعملوا الصالحات — is built on VERBS (kept believing AND kept doing): a sustained process, echoing the durative conditional of the synthesis. And مصلح (active reform) outranks صالح (personal goodness) where a society’s fate is at stake.",17,True,TEAL)],
 [L("CRITIQUE — why form-level matters",18,True,RED),
  L("Counting the root صلح as one idea would merge FOUR concepts — deeds, a righteous person, reconciliation, and reform. Only form separation keeps them apart.",17),
  L("And for faith the verb/noun counts are near-equal (219 vs 224): the point is not which dominates, but that the corpus deploys BOTH deliberately — act and state.",17,True,NAVY)],
 split=0.54,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 3 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pk(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SS if e["ref"] in refs]
appendix(s,[
 ("Claimed (verb) ≠ instilled (heart)",AMBER,AMBERT,pk({"49:14"})),
 ("Saved by sustained DOING",TEAL,TINT,pk({"2:25"})),
 ("Reform > mere righteousness",NAVY,TINT2,pk({"11:117","7:170"})),
])
_save(prs,OUT+"SpecialTopic_W03_act_vs_state.pptx"); print("act_vs_state",len(prs.slides))


# ===== 10. LOCAL / REGIONAL / GLOBAL reach (Week 7 themes) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 7 — local, regional, or global? the reach of the Qur’an’s content",18)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("Is the Qur’an a local Arabian text, a regional Near-Eastern one, or a universal address to all humanity? Its own vocabulary can tell us where it points.",17.5)],
 [L("THE METHOD  (name-fields, by tier)",18,True,TEAL),
  L("• GLOBAL: الناس (mankind), العالمين (the worlds), heavens & earth, آدم. REGIONAL: the Abrahamic / Near-East prophets (Moses, Pharaoh, Abraham, Jesus, People of the Book).",17),
  L("• LOCAL: the sacred House, ʿĀd & Thamūd, the Arabic tongue, Mecca, Quraysh. Count ayahs naming each; compare the three tiers.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 7 — a global frame told through a regional past")
finding2(s,
 {"title":"Global frame vs regional story","cats":["الناس","العالمين","موسى","فرعون","إبراهيم"],
  "series":[("",[TEAL,TEAL,AMBER,AMBER,AMBER],[179,61,131,67,63])],"legend":False},
 {"title":"Local setting — named sparingly","cats":["الكعبة","عاد","ثمود","عربي","مكة","قريش"],
  "series":[("",[RED,RED,RED,GREY,RED,RED],[17,32,25,11,3,1])],"legend":False},
 [L("Global frame, regional story",17.5,True,TEAL),
  L("Framed globally (mankind 179, worlds 61, heavens & earth 133) — yet the narrative runs through the Near-East.",16),
  L("Moses fills 131 ayahs — rivaling “mankind” itself — with Pharaoh 67 and Abraham 63.",16,True,NAVY)],
 [L("Its own backyard, barely named",17.5,True,RED),
  L("The Arabian setting is sparse by name: the sacred House 17, ʿĀd 32, Thamūd 25, the Arabic tongue 11 — but Mecca only ~3, Quraysh once.",16),
  L("The local is the stage, not the subject.",16,True,NAVY)],
 fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 7 — the particular as a doorway to the universal",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("All three scales operate at once. The Qur’an addresses ALL mankind (global), tells its story through the shared Abrahamic past (regional, by far the densest), and treats its own Ḥijāz as the stage rather than the subject.",17),
  L("A distant Exodus outweighs the local Quraysh: the particular becomes the doorway to the universal, not its rival.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Name-mention proxies REACH, not emphasis or weight; proper-name normalization is imperfect; “local/regional/global” is the analyst’s tier, not a Qur’anic category (labelled interpretation).",17),
  L("But the asymmetry is robust — Moses (131) vs Mecca (~3) is no rounding artifact.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 7 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pk(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SC if e["ref"] in refs]
appendix(s,[
 ("GLOBAL — all mankind / the worlds",TEAL,TINT,pk({"1:2","49:13"})),
 ("REGIONAL — the Abrahamic past",AMBER,AMBERT,pk({"79:17","2:136"})),
 ("LOCAL — House & Quraysh",RED,REDT,pk({"3:96","106:1"})),
])
_save(prs,OUT+"SpecialTopic_W07_local_regional_global.pptx"); print("scope",len(prs.slides))


# ===== 11. WHAT DEFINES A SURAH / AN AYAH (Week 2 distribution) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 2 — what defines a Sūra and an Ayah?",20)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("Can we define the Qur’an’s two units by measurable criteria? Length is one handle — does it corroborate the anchor cases (al-Baqara, al-Kawthar; the debt verse; the disjointed letters)?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Sūra: count ayahs per sūra (1–114); find the floor, the ceiling, the distribution.",17),
  L("• Ayah: count root-tokens per ayah; find the shortest (disjointed letters) and the longest (2:282).",17),
  L("• Ask whether length DEFINES the units or only corroborates a boundary that is otherwise MARKED.",17,True,NAVY)],
 split=0.36,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 2 — bounded units, with measurable ranges")
finding2(s,
 {"title":"Sūra length — # sūras by ayah-count","cats":["3–10","11–50","51–100","101–200","201+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[19,48,29,15,3])],"legend":False},
 {"title":"Ayah length — # ayahs by root-tokens","cats":["1–2","3–10","11–30","31–60","61+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[769,3829,1576,61,1])],"legend":False},
 [L("A Sūra: 3 → 286 ayahs",17.5,True,TEAL),
  L("A named, basmala-bounded unit (except at-Tawba). Floor = 3 (al-Kawthar, al-ʿAsr, an-Nasr); ceiling = al-Baqara (286); median 39.",16),
  L("Length is one visible criterion.",16,True,NAVY)],
 [L("An Ayah: 1 → 84 tokens",17.5,True,AMBER),
  L("A marked verse — from a single token (الم; مدهامتان 55:64) to the 84-token debt verse (2:282). Median 7.",16),
  L("An ayah need not be a sentence.",16,True,NAVY)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 2 — length corroborates, but marking defines",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Both units have measurable ranges that corroborate the anchors — sūras 3–286 ayahs, ayahs 1–84 root-tokens. But length DEFINES neither.",17),
  L("The units are MARKED: sūras by name and basmala, ayahs by received verse-stops. The disjointed letters (الم as a whole ayah) prove the marking is prior to length, grammar, or even meaning.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Length is a corroborating, not a defining, criterion. The boundaries are received — narrated and recitational — not computed; counting can describe the units, not derive them.",17),
  L("This mirrors the muṣḥaf-order limit: the segmentation, like the arrangement, is given, not inferred.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 2 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pk(refs): return [(e["ref"],e["snip"],e["tag"]) for e in SU if e["ref"] in refs]
appendix(s,[
 ("Shortest sūras (3 ayahs)",TEAL,TINT,pk({"108:1","110:1"})),
 ("Shortest ayahs — 1 token",GREY,TINT2,pk({"2:1","55:64"})),
 ("Longest ayah & sūra",RED,REDT,pk({"2:282","2:286"})),
])
_save(prs,OUT+"SpecialTopic_W02_surah_ayah_units.pptx"); print("units",len(prs.slides))


def eq_appendix(s,key,cols):
    appendix(s,cols)
# ===== 12. EQUITY — ECONOMIC (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — women & men: ECONOMIC standing",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("A common claim: the Qur’an denies women economic independence. What does the text actually fix — and what is left to interpretation?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Gather the verses that assign women financial entitlements; report exactly what each establishes.",17),
  L("• Keep the computed datum (what is fixed) apart from the equity verdict (whether the whole is “equal”).",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — three financial entitlements the text fixes")
three_stack(s,
 [L("A share of inheritance — 4:7",17,True,TEAL),
  L("“Men have a share of what parents and kin leave, and women have a share.” Women’s inheritance is fixed as a right, not left to custom.",16)],
 [L("The dowry is hers — 4:4",17,True,AMBER),
  L("“Give women their dowries as a free gift.” The mahr is the woman’s own property — hers to keep, spend, or return at will.",16)],
 [L("She keeps her earnings — 4:32",17,True,NAVY),
  L("“For men a share of what they earn, and for women a share of what they earn.” Earnings belong to the earner, each gender severally.",16)],
 fills=(TINT,AMBERT,TINT2))
s=slide(prs); title(s,"Special Topic · Week 9 — verdict: financial personhood, fixed",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed datum: the corpus establishes women’s independent financial personhood — a guaranteed inheritance share (4:7), an owned dowry (4:4), and retained earnings (4:32).",17),
  L("Whether the overall SYSTEM is “equal” (cf. the inheritance ratio) is a separate, interpretive question; financial AGENCY is not — it is stated plainly.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("These are entitlements the text names; their adequacy or “equality” is debated and not settled by citation alone.",17),
  L("Historical context (pre-Islamic deprivation) is interpretation, not data. We report what is fixed and scope the rest.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[("A share of inheritance",TEAL,TINT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["econ"] if e["ref"]=="4:7"]),
            ("The dowry is hers",AMBER,AMBERT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["econ"] if e["ref"] in ("4:4","4:24")]),
            ("She keeps her earnings",NAVY,TINT2,[(e["ref"],e["snip"],e["tag"]) for e in EQ["econ"] if e["ref"]=="4:32"])])
_save(prs,OUT+"SpecialTopic_W09_equity_economic.pptx"); print("eq_econ",len(prs.slides))

# ===== 13. EQUITY — SOCIAL / SPIRITUAL (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — women & men: SOCIAL & SPIRITUAL standing",19)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("Are women and men equal in moral and spiritual standing in the text — in origin, reward, and mutual relation?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Read the verses on creation, reward, and mutual standing at face value; mark where parity is COMPUTED (stated) vs interpreted.",17),
  L("• Keep moral standing apart from role/legal differentiation (separate verses, separate question).",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — parity stated in origin, reward, and relation")
three_stack(s,
 [L("Same origin — 49:13, 4:1",17,True,TEAL),
  L("Humanity created “from a male and a female” (49:13) and “from one soul” (4:1); rank is by taqwā, not sex.",16)],
 [L("Same reward — 33:35, 3:195",17,True,AMBER),
  L("33:35 pairs ten virtues for men and women identically, promising the same forgiveness and reward; 3:195: “I will not waste the work of any worker among you, male or female.”",16)],
 [L("Mutual guardianship — 9:71",17,True,NAVY),
  L("“The believing men and the believing women are guardians (awliyāʾ) of one another” — a reciprocal relation, not one-way.",16)],
 fills=(TINT,AMBERT,TINT2))
s=slide(prs); title(s,"Special Topic · Week 9 — verdict: symmetric in standing",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed datum: in origin, moral agency, and reward the text states parity explicitly and repeatedly — 33:35’s ten matched pairs, the “male or female” reward formula (4×), reciprocal guardianship (9:71).",17),
  L("On the face of the text, spiritual and moral standing is symmetric. Role and legal differentiations (other verses) are a distinct question, not this one.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Face-value parity in origin and reward is a strong textual datum. Whether social ROLES are “equal” is contested and not decided by these verses.",17),
  L("We keep the registers apart — moral standing vs role — rather than collapse one into the other.",17,True,NAVY)],
 split=0.52,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[("Same origin",TEAL,TINT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["social"] if e["ref"] in ("49:13","4:1")]),
            ("Same reward",AMBER,AMBERT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["social"] if e["ref"] in ("33:35","3:195")]),
            ("Mutual guardianship",NAVY,TINT2,[(e["ref"],e["snip"],e["tag"]) for e in EQ["social"] if e["ref"]=="9:71"])])
_save(prs,OUT+"SpecialTopic_W09_equity_social.pptx"); print("eq_social",len(prs.slides))

# ===== 14. EQUITY — INHERITANCE (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — women & men: INHERITANCE",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("“The Qur’an gives women half.” Is the famous 2:1 the whole picture, or one case among several?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Read the inheritance verses (4:7, 4:11, 4:12, 4:176); report the actual shares by heir-CONFIGURATION, not a single ratio.",17),
  L("• Separate the fixed datum from the equity verdict (which depends on the surrounding obligations).",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — a fixed right, with case-specific shares")
three_stack(s,
 [L("Women inherit — fixed (4:7)",17,True,TEAL),
  L("Where custom once bypassed them, 4:7 guarantees women a defined share of parents’ and kin’s estate — an enforceable right.",16)],
 [L("The 2:1 case (4:11)",17,True,AMBER),
  L("In the parents→children case, a son receives the share of two daughters (4:11). This specific configuration is the verse most often quoted.",16)],
 [L("Not always 2:1 (4:12)",17,True,RED),
  L("Shares vary by configuration: uterine siblings inherit equally (4:12); some parent and spouse shares match. The ratio is case-specific, not a blanket “half.”",16)],
 fills=(TINT,AMBERT,REDT))
s=slide(prs); title(s,"Special Topic · Week 9 — verdict: a fixed schedule, an interpreted equity",18)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed datum: the corpus FIXES women’s inheritance as an enforceable right (4:7) and specifies shares that vary by heir — the well-known 2:1 holds in the child case (4:11) but not universally (uterine siblings equal, 4:12).",17),
  L("Whether the scheme is “equitable” is the interpretive crux: readings that pair the male’s larger share with his exclusive maintenance duty argue net-parity; others read it as unequal. The numbers alone do not decide.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Quoting only 4:11’s 2:1 is a cherry-pick (cf. Closer Look #9); quoting only the equal cases is the opposite cherry-pick.",17),
  L("The honest datum is the FULL schedule plus the maintenance asymmetry — and the verdict turns on the interpretive frame, not the count.",17,True,NAVY)],
 split=0.54,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[("Women inherit — fixed",TEAL,TINT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["inherit"] if e["ref"]=="4:7"]),
            ("The 2:1 child case",AMBER,AMBERT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["inherit"] if e["ref"]=="4:11"]),
            ("Equal cases exist",RED,REDT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["inherit"] if e["ref"] in ("4:12","4:176")])])
_save(prs,OUT+"SpecialTopic_W09_equity_inheritance.pptx"); print("eq_inherit",len(prs.slides))

# ===== 15. EQUITY — JUDICIAL / TESTIMONY (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — women & men: TESTIMONY",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("“A woman’s testimony is worth half a man’s.” Always — or only in a particular context?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Compare the testimony verses across contexts: documenting a debt (2:282) vs the liʿān accusation (24:6–9). Read the weight each assigns.",17),
  L("• Let the variation, not a single verse, carry the finding.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — testimony weight is context-dependent")
finding2(s,
 {"title":"Female testimony weight, by context","cats":["debt 2:282","liʿān 24:6–9"],
  "series":[("",[AMBER,TEAL],[0.5,1.0])],"legend":False,"fmt":"{:.1f}"},
 {"title":"Liʿān — oaths are symmetric","cats":["husband","wife"],
  "series":[("",[TEAL,TEAL],[4,4])],"legend":False},
 [L("Debt: two women for one man (2:282)",17,True,AMBER),
  L("In documenting a deferred debt, two women stand for one man — “so if one errs, the other reminds her.” Tied to that transaction, not a universal scale of worth.",15.5)],
 [L("Liʿān: her oath equals his (24:6–9)",17,True,TEAL),
  L("When a husband accuses his wife, each swears four oaths; HER four oaths avert the penalty against his. One-to-one — equal.",15.5)],
 fillA=AMBERT,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — verdict: “half” is not a general rule",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed datum: testimony weight is CONTEXT-DEPENDENT, not uniform — 2-for-1 in debt-documentation (2:282) and 1-for-1 in liʿān (24:6–9), where a woman’s sworn word overturns a man’s.",17),
  L("So “half” is a generalization the corpus does not support across the board.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Reading 2:282 as a universal law of female worth ignores 24:6–9 — and that 2:282 concerns RECORD-KEEPING of an unfamiliar commercial transaction, not a courtroom scale of worth.",17),
  L("Reading only liʿān ignores the debt asymmetry. The datum is the VARIATION; the reason for it is interpretation, not count.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
appendix(s,[("Debt — two for one (2:282)",AMBER,AMBERT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["judicial"] if e["ref"]=="2:282"]),
            ("Liʿān — her oath equals his",TEAL,TINT,[(e["ref"],e["snip"],e["tag"]) for e in EQ["judicial"] if e["ref"]=="24:6"]),
            ("Her oaths avert the penalty",NAVY,TINT2,[(e["ref"],e["snip"],e["tag"]) for e in EQ["judicial"] if e["ref"] in ("24:8","24:9")])])
_save(prs,OUT+"SpecialTopic_W09_equity_judicial.pptx"); print("eq_judicial",len(prs.slides))


def col3(s,key,heads):
    appendix(s,[(h,c,fl,[(e["ref"],e["snip"],e["tag"]) for e in B2[key] if e["ref"] in rfs]) for (h,c,fl,rfs) in heads])
# ===== 16. NASKH — abrogation (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — does the Qur’an abrogate itself? (نسخ)",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("A whole doctrine (naskh) holds that later verses cancel earlier ones. How much textual ground does the word itself actually cover?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Find every occurrence of the root نسخ; read each in context; separate the “abrogate” sense from the “copy / transcribe” sense.",17),
  L("• Ask whether the text ever NAMES which verse cancels which.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — four uses, and half are not “abrogation”")
three_stack(s,
 [L("Only 4 occurrences in the whole Qur’an",17,True,NAVY),
  L("The root نسخ appears just four times — a slender base for so large a doctrine.",16)],
 [L("Two mean ABROGATE — 2:106, 22:52",17,True,AMBER),
  L("“Whatever sign We abrogate or cause to be forgotten, We bring better or like it” (2:106); God abrogates what Satan casts (22:52).",16)],
 [L("Two mean COPY / WRITE — 7:154, 45:29",17,True,GREY),
  L("The other two are about transcription: the tablets’ text (نسخة, 7:154) and “We were having it copied” (نستنسخ, 45:29). Same root, different sense.",16)],
 fills=(TINT2,AMBERT,TINT))
s=slide(prs); title(s,"Special Topic · Week 9 — a large doctrine on a slender textual base",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: the abrogation idea rests on ~2 verses (2:106, 22:52); the word also means “copy,” and the text NEVER names a specific verse-cancels-verse case. Which verses (if any) abrogate which is entirely interpretive.",17),
  L("So intra-Qur’anic abrogation is a juristic CONSTRUCT built atop a thin lexical base — not a self-declared feature of the text.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("This does not settle whether abrogation is true — only that the corpus barely uses the word and never lists cases.",17),
  L("2:106’s “sign” (آية) may mean a miracle or a prior scripture, not necessarily a Qur’anic verse — itself a reading.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3(s,"naskh",[("ABROGATE sense (2 of 4)",AMBER,AMBERT,{"2:106","22:52"}),("COPY / TRANSCRIBE sense (2 of 4)",GREY,TINT2,{"7:154","45:29"})])
_save(prs,OUT+"SpecialTopic_W09_naskh_abrogation.pptx"); print("naskh",len(prs.slides))

# ===== 17. SHAFAA — intercession (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — is intercession denied or affirmed? (شفاعة)",20)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("Some verses say no intercession will help; others speak of intercession “by His leave.” A contradiction — or two halves of one rule?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Read the شفع verses (26 occurrences) by type: independent intercession (denied) vs God-permitted intercession (affirmed).",17),
  L("• Let the qualifier “by His leave” do its work rather than pitting verses against each other.",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — denied as a power, permitted as a gift")
three_stack(s,
 [L("Denied as INDEPENDENT — 2:48",17,True,RED),
  L("“Guard a Day when no soul avails another, no intercession is accepted, no ransom taken” — no autonomous broker can override the verdict.",16)],
 [L("Only by HIS LEAVE — 2:255",17,True,TEAL),
  L("Āyat al-Kursī: “Who is there that can intercede with Him except by His leave?” — intercession exists, but only as God permits.",16)],
 [L("Belongs WHOLLY to God — 39:44",17,True,NAVY),
  L("“Say: intercession belongs altogether to God.” The power is His to grant; it is never a rival authority.",16)],
 fills=(REDT,TINT,TINT2))
s=slide(prs); title(s,"Special Topic · Week 9 — not a contradiction, a single conditioned rule",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: the two sets are reconciled by one qualifier. Intercession is denied as an INDEPENDENT power and affirmed only as GOD-PERMITTED — “by His leave,” “belongs wholly to God.”",17),
  L("The apparent contradiction dissolves once the conditional clause is read with the negation, not against it.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Whether anyone in fact receives that leave — and who — is the interpretive question the count does not settle.",17),
  L("Reading the “no intercession” verses absolutely (ignoring “except by His leave”) is the classic audit failure (cf. Closer Look #9).",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3(s,"shafaa",[("Denied as INDEPENDENT",RED,REDT,{"2:48","2:254"}),("Only by HIS LEAVE",TEAL,TINT,{"2:255","10:3"}),("By His approval only",NAVY,TINT2,{"39:44","21:28"})])
_save(prs,OUT+"SpecialTopic_W09_shafaa_intercession.pptx"); print("shafaa",len(prs.slides))

# ===== 18. MAL + AWLAD — wealth & children (Week 4) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 4 — wealth & children: blessing or trial? (مال + أولاد)",19)
two_stack(s,
 [L("THE PAIRING",18,True,NAVY),
  L("“Wealth” (مال) and “children” (أولاد) are each named ~80×, and they co-occur as a fixed pair 16 times. What frame does the corpus put them in?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Find the ayahs that name both; read what is predicated of the pair — adornment, trial, or security?",17),
  L("• Separate the recurring pairing (computed) from the moral lesson (interpreted).",17,True,NAVY)],
 split=0.34,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 4 — the pair, and how it is framed")
three_stack(s,
 [L("A fixed pair — 16 shared ayahs",17,True,TEAL),
  L("Mal (80) and awlād (80) recur together 16× — “your wealth and your children” is a set phrase for worldly capital.",16)],
 [L("Framed as a TRIAL — 8:28, 64:15",17,True,AMBER),
  L("“Know that your wealth and your children are but a trial (fitna)” — the pair is a test, not a verdict of favour.",16)],
 [L("That will not avail — 18:46, 3:10",17,True,RED),
  L("“Wealth and sons are the adornment of the worldly life” (18:46); “neither their wealth nor their children will avail them against God” (3:10).",16)],
 fills=(TINT,AMBERT,REDT))
s=slide(prs); title(s,"Special Topic · Week 4 — capital reframed as a test",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: wealth+children form a stable lexical pair (16 ayahs), and where the pair appears it is cast as adornment / trial / something that “will not avail” — not as a sign of divine approval.",17),
  L("Interpretation: the corpus consistently demotes worldly capital from a reward to a test — the same durative-conditional logic as the synthesis (what you DO with them decides).",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("The pairing is robust; the “trial” framing is drawn from the verses that predicate fitna/zīna — other ayahs do call children a gift (e.g. naʿīm). The pair is not always pejorative.",17),
  L("So the finding is a TENDENCY in the paired usage, not a blanket valuation of wealth or children.",17,True,NAVY)],
 split=0.52,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 4 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3(s,"malwalad",[("A trial (fitna)",AMBER,AMBERT,{"8:28","64:15"}),("Adornment of this life",TEAL,TINT,{"18:46"}),("Will not avail against God",RED,REDT,{"3:10","3:116"})])
_save(prs,OUT+"SpecialTopic_W04_wealth_children.pptx"); print("malwalad",len(prs.slides))

# ===== 19. AYAT — signs in nature vs scripture (Week 7) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 7 — one word for sunrise and scripture (آية)",20)
two_stack(s,
 [L("THE OBSERVATION",18,True,NAVY),
  L("The Qur’an calls a verse an آية — and calls a sunrise, the rain, the human body an آية too. Does the same word really span cosmos and scripture?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• The sign-root (آية) appears 353×. Tag where it co-occurs with NATURE roots (sun, moon, night, creation, rain…) vs SCRIPTURE roots (book, sent-down, recite, made-clear).",17),
  L("• Compare the two registers; note what the overlap implies.",17,True,NAVY)],
 split=0.36,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 7 — verbally toward scripture, conceptually both")
finding2(s,
 {"title":"“Sign” co-occurs with","cats":["nature","scripture"],
  "series":[("",[TEAL,AMBER],[35,137])],"legend":False},
 {"title":"The sign-root (353) by explicit context","cats":["nature","scripture","general"],
  "series":[("",[TEAL,AMBER,GREY],[35,137,181])],"legend":False},
 [L("One word, two books",17.5,True,TEAL),
  L("The root appears 353×. Explicitly it sits with scripture (137) far more than with nature (35) — yet it is the SAME word for a recited verse and a sunrise.",16)],
 [L("The fusion — 41:53",17.5,True,AMBER),
  L("“We will show them Our signs in the horizons and in themselves.” Cosmos and self are read as a text; reading creation is reading revelation.",16)],
 fillA=TINT,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 7 — creation and revelation share one vocabulary",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: آية spans both registers — leaning verbally to the recited signs (137 vs 35 in explicit co-occurrence) while naming nature with the very same term.",17),
  L("Interpretation: the conflation is deliberate — the book and the world are presented as two volumes of one signage, each meant to be “read.”",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Co-occurrence captures EXPLICIT pairing, not all uses — 181 are general “Our signs.” The nature/scripture tiers are the analyst’s.",17),
  L("But the dual use of one word is the robust datum, independent of the tiering.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 7 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3(s,"ayat",[("The fusion (signs in self & cosmos)",NAVY,TINT2,{"41:53","51:21"}),("NATURE signs",TEAL,TINT,{"2:164","16:12"}),("SCRIPTURE signs",AMBER,AMBERT,{"45:6","2:252"})])
_save(prs,OUT+"SpecialTopic_W07_signs_nature_scripture.pptx"); print("ayat",len(prs.slides))

# ===== 20. DIVINE NAMES — الله / رب / الرحمن / إله (Week 10) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 10 — الله, رب, الرحمن, إله: which Name does which work?",18)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("The Qur’an names God many ways. Are they interchangeable, or does each carry a distinct role — proper name, relation, attribute, or the negated generic?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Count the principal divine words; read how each is used grammatically (proper name? possessed? negated?).",17),
  L("• Separate the computed frequency from the labelled role.",17,True,NAVY)],
 split=0.36,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 10 — a proper Name, a relation, an attribute, a negation")
three_stack(s,
 [L("الله — the proper Name (2698)",17,True,NAVY),
  L("By far the most frequent (2698). A proper name, not a description; never pluralised, never feminised — the unique referent.",16)],
 [L("رب — the relational Lord (≈972)",17,True,TEAL),
  L("Lord / sustainer, overwhelmingly possessed — your Lord, our Lord, my Lord. A name of RELATION, the one prayers most often call.",16)],
 [L("الرحمن (57) · إله — attribute & negation",17,True,AMBER),
  L("al-Raḥmān: near-exclusive to God, paired in the Basmala. إله (“a god”) is the GENERIC the creed negates — “no إله but Allah.”",16)],
 fills=(TINT2,TINT,AMBERT))
s=slide(prs); title(s,"Special Topic · Week 10 — one Referent, four kinds of word",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed: الله dominates (2698) as the proper name; رب (≈972) is the relational term, almost always possessed; الرحمن (57) is the signature attribute; إله is the category-word, mostly appearing to be DENIED.",17),
  L("So the names are not interchangeable — they divide the labour: identity (الله), relationship (رب), mercy-attribute (الرحمن), and the negated generic (إله).",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Lemma-level counting flattens رب’s possessive forms (your/our/my Lord) into one figure; the relational point is read from usage, not the bare count.",17),
  L("“Roles” are a descriptive gloss on grammar, not a Qur’anic taxonomy.",17,True,NAVY)],
 split=0.52,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 10 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3(s,"names",[("رَبّ — the relational Lord",TEAL,TINT,{"1:2","113:1"}),("الله — the proper Name",NAVY,TINT2,{"112:1","2:255"}),("إله — the negated generic",AMBER,AMBERT,{"21:25","47:19"})])
_save(prs,OUT+"SpecialTopic_W10_divine_names.pptx"); print("names",len(prs.slides))


def col3b(s,key,heads):
    appendix(s,[(h,c,fl,[(e["ref"],e["snip"],e["tag"]) for e in B3[key] if e["ref"] in rfs]) for (h,c,fl,rfs) in heads])
# ===== 21. LIGHT & DARKNESS — number (Week 4) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 4 — one light, many darknesses (نور / ظلمات)",20)
two_stack(s,
 [L("THE OBSERVATION",18,True,NAVY),
  L("Light and darkness are a stock Qur’anic pair. But look at their NUMBER: is نور ever plural? is ظلمات ever singular?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Count every surface form of each, tagging singular vs plural; then weigh light against darkness overall.",17),
  L("• Let the grammatical number — not a translator’s choice — carry the finding.",17,True,NAVY)],
 split=0.36,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 4 — light is always singular, darkness always plural")
finding2(s,
 {"title":"Singular vs plural","cats":["نور","أنوار","ظلمات","ظلمة"],
  "series":[("",[TEAL,GREY,NAVY,GREY],[43,0,23,0])],"legend":False},
 {"title":"Light outweighs darkness","cats":["نور","ظلمات"],
  "series":[("",[TEAL,NAVY],[43,23])],"legend":False},
 [L("One light, many darknesses",17.5,True,TEAL),
  L("نور appears 43× and is ALWAYS singular (أنوار = 0). ظلمات appears 23× and is ALWAYS plural (the singular ظلمة = 0).",16)],
 [L("And light leads",17.5,True,NAVY),
  L("Light is named nearly twice as often as darkness (43 vs 23). The corpus weights illumination over its absence.",16)],
 fillA=TINT,fillB=TINT2)
s=slide(prs); title(s,"Special Topic · Week 4 — unity of light, multiplicity of dark",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed, with zero exceptions: a single نور (never pluralised) set against plural ظلمات (never singularised) — and light outnumbers darkness ~2:1.",17),
  L("Interpretation: the grammar encodes a creed — truth/guidance is ONE, error and confusion are MANY. The number is the message.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("The morphology is a hard datum (0 counter-examples). “One truth, many errors” is the labelled reading laid over it.",17),
  L("نار (fire) shares the lexical family but is a different sense and excluded.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 4 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3b(s,"light",[("God IS light",TEAL,TINT,{"24:35"}),("He made darknesses & the light",NAVY,TINT2,{"6:1"}),("out of darkness(es) into light",AMBER,AMBERT,{"2:257","5:16"})])
_save(prs,OUT+"SpecialTopic_W04_light_darkness.pptx"); print("light",len(prs.slides))

# ===== 22. NAME PAIRS — count vs lift (Week 5) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 5 — which Divine-Name pairs truly bond? (count vs lift)",18)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("Verses end on paired Names — “Forgiving, Merciful”, “Mighty, Wise”. Which pairs are a real bond, and which just look tight because both Names are everywhere?",17.5)],
 [L("THE METHOD  (Week-5 lesson)",18,True,TEAL),
  L("• For each pair compute the shared-ayah COUNT and the LIFT (× over chance = joint ÷ expected).",17),
  L("• A big count can be mere frequency; lift exposes the genuine attraction. Read them together.",17,True,NAVY)],
 split=0.38,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 5 — count and lift rank the pairs differently")
finding2(s,
 {"title":"Shared count (ayahs together)","cats":["ʿAlīm+Ḥakīm","Ghafūr+Raḥīm","ʿAzīz+Ḥakīm","Ghafūr+Ḥalīm"],
  "series":[("",[GREY,TEAL,TEAL,AMBER],[71,91,49,9])],"legend":False},
 {"title":"Lift (× over chance)","cats":["ʿAlīm+Ḥakīm","Ghafūr+Raḥīm","ʿAzīz+Ḥakīm","Ghafūr+Ḥalīm"],
  "series":[("",[GREY,TEAL,TEAL,AMBER],[3.2,9.0,13.8,13.9])],"legend":False,"fmt":"{:.1f}×"},
 [L("Count says one thing",17.5,True,GREY),
  L("By raw shared verses, ʿAlīm+Ḥakīm (71) and Ghafūr+Raḥīm (91) look like the tightest Name-pairs.",16)],
 [L("Lift says another",17.5,True,AMBER),
  L("By lift, Ghafūr+Ḥalīm (13.9× on just 9 v) and ʿAzīz+Ḥakīm (13.8×) win; ʿAlīm+Ḥakīm’s 71 collapses to 3.2× — both Names are simply everywhere.",16)],
 fillA=TINT2,fillB=AMBERT)
s=slide(prs); title(s,"Special Topic · Week 5 — frequency is not a bond",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("The most FREQUENT pairing (ʿAlīm+Ḥakīm, 71 verses) is among the WEAKEST by lift (3.2×) — inflated because ʿilm appears 728×. The tightest real bond is Ghafūr+Ḥalīm (13.9×): rare, but almost always together.",17),
  L("The gold standard is ʿAzīz+Ḥakīm — strong lift (13.8×) AND solid support (49 verses).",17,True,TEAL)],
 [L("CRITIQUE & LIMIT (ties to Week 8)",18,True,RED),
  L("High lift on low count (Ghafūr+Ḥalīm, 9 v) is itself thin support — a leave-one-out would wobble it.",17),
  L("So read three numbers, not one: count, lift, and stability. Lift alone can mislead in either direction.",17,True,NAVY)],
 split=0.52,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 5 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3b(s,"pairs",[("ʿAzīz Ḥakīm (lift 13.8×, 49 v)",TEAL,TINT,{"48:7"}),("Ghafūr Ḥalīm (lift 13.9×, 9 v)",AMBER,AMBERT,{"2:235"}),("ʿAlīm Ḥakīm (count 71, lift 3.2×)",GREY,TINT2,{"2:32"}),("Ghafūr Raḥīm (count 91)",TEAL,TINT,{"2:173"})])
_save(prs,OUT+"SpecialTopic_W05_name_pairs_lift.pptx"); print("pairs",len(prs.slides))

# ===== 23. OUT OF DARKNESS INTO LIGHT — direction (Week 6) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 6 — “out of darkness into light”: a one-way arrow",19)
two_stack(s,
 [L("THE QUESTION",18,True,NAVY),
  L("The Qur’an speaks of moving between darkness and light. Is the movement symmetric, or does it run in a fixed direction — and who is its agent?",17.5)],
 [L("THE METHOD",18,True,TEAL),
  L("• Count the directional phrase both ways: from الظلمات to النور vs from النور to الظلمات.",17),
  L("• Record the SUBJECT of each (who brings whom). Direction + agency is the Week-6 move.",17,True,NAVY)],
 split=0.36,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 6 — the arrow points one way, and names its agent")
finding2(s,
 {"title":"Direction of movement (ayahs)","cats":["dark → light","light → dark"],
  "series":[("",[TEAL,RED],[7,1])],"legend":False},
 {"title":"Who moves you","cats":["God → light","ṭāghūt → dark"],
  "series":[("",[TEAL,RED],[7,1])],"legend":False},
 [L("A one-way arrow",17.5,True,TEAL),
  L("The journey is from (plural) darkness to (single) light 7×, and the reverse only once. God “brings them out of the darknesses into the light.”",16)],
 [L("The lone reversal proves the rule",17.5,True,RED),
  L("The single light→dark case (2:257) is the ṭāghūt (false gods) dragging people the wrong way — the exception that names the agent of darkness.",16)],
 fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 6 — direction encodes agency",20)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Salvation has a direction: out of the plural darknesses into the single light (7:1), and God is its subject. The one reversal is explicitly attributed to the ṭāghūt.",17),
  L("So the arrow encodes agency — toward light is God’s work; toward darkness is the false patron’s. (This builds on the Week-4 number: one light, many darknesses.)",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("Small support — eight directional phrases in all; the 7:1 asymmetry is clear but rests on few verses.",17),
  L("“Direction = agency” is the labelled reading; the counts and subjects are the computed part.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 6 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3b(s,"light",[("God → light (2:257, 5:16, 14:1)",TEAL,TINT,{"2:257","5:16","14:1"}),("the ṭāghūt → darkness (2:257)",RED,REDT,{"2:257"})])
_save(prs,OUT+"SpecialTopic_W06_darkness_to_light.pptx"); print("direction",len(prs.slides))

# ===== 24. THE HYPOCRITE SYNDROME — motif support (Week 8) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 8 — the hypocrite syndrome: a motif, and its support (نفاق)",18)
two_stack(s,
 [L("THE CLAIM TO TEST",18,True,NAVY),
  L("The Qur’an paints the hypocrite (munāfiq) with a recurring cluster — a diseased heart and deception. Is the full three-part motif as solid as it feels?",17.5)],
 [L("THE METHOD  (Week-8 lesson: lift is not enough — read support)",18,True,TEAL),
  L("• Sense-filter نفق to the hypocrite forms (not “spending”). Count the pairwise links and the full trio; read each one’s verse-SUPPORT.",17),
  L("• A vivid motif on few verses is fragile — count the base.",17,True,NAVY)],
 split=0.4,fillA=TINT2,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 8 — strong as pairs, thin as a trio")
finding2(s,
 {"title":"Pairwise links (shared ayahs)","cats":["قلب·مرض","نفق·قلب","نفق·كذب","نفق·خدع"],
  "series":[("",[TEAL,TEAL,AMBER,RED],[12,9,3,1])],"legend":False},
 {"title":"Pairwise vs the full trio","cats":["قلب·مرض pair","full trio"],
  "series":[("",[TEAL,RED],[12,3])],"legend":False},
 [L("A real syndrome — pairwise",17.5,True,TEAL),
  L("Hypocrisy clusters with a diseased heart and deceit: قلب+مرض 12× (“in their hearts a disease”), نفق+قلب 9×, نفق+كذب 3×.",16)],
 [L("But the trio is thin",17.5,True,RED),
  L("The complete munāfiq + heart + disease motif holds in only 3 verses — strong as a theme, slim as a trio.",16)],
 fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 8 — the portrait is real; its tightest form rests on little",18)
two_stack(s,
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("The hypocrite is drawn as heart-diseased and deceptive — a robust PAIRWISE syndrome (قلب↔مرض 12, نفق↔قلب 9) but a thin TRIO (3 verses).",17),
  L("So the portrait is genuine; quoting it as a tight three-part formula overstates a 3-verse base. Support, not vividness, decides.",17,True,TEAL)],
 [L("CRITIQUE & LIMIT",18,True,RED),
  L("نفق is polysemous (spend vs hypocrite) — only the munāfiq forms were counted.",17),
  L("With 3 supporting verses, a leave-one-out would shake the trio — the exact Week-8 caution.",17,True,NAVY)],
 split=0.5,fillA=TINT,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 8 — Appendix: input snippets (Book6, vocalized col 11)",19)
col3b(s,"hypo",[("diseased heart",TEAL,TINT,{"2:10","8:49"}),("deception",AMBER,AMBERT,{"4:142"}),("they lie",RED,REDT,{"63:1"})])
_save(prs,OUT+"SpecialTopic_W08_hypocrite_syndrome.pptx"); print("hypo",len(prs.slides))


# ===== 25. ISTINSĀKH & GENOMIC TRANSCRIPTION — a labelled analogy (Week 9) =====
prs=deck()
s=slide(prs); title(s,"Special Topic · Week 9 — “We were transcribing what you did”: نستنسخ & genomic transcription (an analogy)",17)
two_stack(s,
 [L("THE TEXT  (computed anchor)",18,True,NAVY),
  L("45:29 — “This is Our record that speaks against you in truth; We were TRANSCRIBING (نستنسخ) what you used to do.” The same root نسخ as the abrogation topic — here meaning to record/copy.",17),
  L("The recording field: a watcher by every word (50:18), all things enumerated in a record (78:29), nothing small or great omitted (18:49), to an atom’s weight (99:7).",17,True,TEAL)],
 [L("THE ANALOGY  (labelled — a teaching bridge, not a science claim)",18,True,RED),
  L("As an ANALOGY ONLY (not a claim about the text): picture it like genomic transcription — the recorded deeds “transcribed” now, the consequence expressed later, in the hereafter’s own context. A mental model, nothing more.",17),
  L("Every parallel below is a teaching device — NOT a claim that the Qur’an describes, predicts, or encodes molecular biology.",17,True,NAVY)],
 split=0.5,fillA=TINT2,fillB=REDT)
s=slide(prs); title(s,"Special Topic · Week 9 — a 60-second primer (genomics, and what an analogy is)",18)
three_stack(s,
 [L("The genome = an instruction archive",17,True,TEAL),
  L("Every living cell carries DNA — a long coded text of instructions (genes). You don’t choose it; you inherit it. Think of it as a master archive that is never used all at once.",16)],
 [L("Transcription → translation → phenotype",17,True,AMBER),
  L("The cell COPIES an active gene into a portable message (mRNA) — that step is “transcription.” The message is then READ to build a protein (“translation”), and proteins produce the organism’s visible traits — the “phenotype,” expressed in its own time and context. Information is copied first, expressed later, and preserved faithfully.",16)],
 [L("What an analogy (equivalence) is — and isn’t",17,True,NAVY),
  L("An analogy maps the STRUCTURE of one system onto another (copy → store → express) to aid understanding. It is NOT a claim that the two are the same thing, nor that one predicts the other. We keep the mapping where it illuminates and drop it where it breaks.",16)],
 fills=(TINT,AMBERT,TINT2))
s=slide(prs); title(s,"Special Topic · Week 9 — the full pipeline: transcription → translation → phenotype")
three_stack(s,
 [L("1 · TRANSCRIPTION — deeds → record",17,True,TEAL),
  L("Genomics: DNA → mRNA, a working copy of the active gene. Qur’an: نستنسخ (45:29) — deeds copied into the record “bil-ḥaqq” (in truth); nothing small or great is omitted (18:49). The PARALLEL is faithful copying; the mechanisms are unrelated.",15.5)],
 [L("2 · TRANSLATION — record → verdict",17,True,AMBER),
  L("Genomics: the message (mRNA) is READ and rendered into a protein. Qur’an: on the Day the record is READ out — “Read your record; you suffice as your own reckoner” (17:14) — and the deeds are weighed on the just scales (21:47; an atom’s weight, 99:7–8).",15.5)],
 [L("3 · PHENOTYPE — expressed, in its own context",17,True,NAVY),
  L("Genomics: the protein produces a visible trait, expressed in its own time and environment. Qur’an: the consequence of deeds is manifested in the hereafter — garden or fire — its “phenotype,” deferred and context-specific.",15.5)],
 fills=(TINT,AMBERT,TINT2))
s=slide(prs); title(s,"Special Topic · Week 9 — where it breaks, and the verdict",20)
two_stack(s,
 [L("WHERE THE ANALOGY BREAKS",18,True,RED),
  L("• You author your own code: in biology you don’t choose your genome — on this reading (labelled interpretation), your free deeds are the template you write.",16.5),
  L("• Another context: the genomic phenotype expresses in THIS world; the deed-phenotype expresses in ANOTHER realm, on its own terms.",16.5),
  L("• Moral, not mechanistic — and error-free (bil-ḥaqq) vs mutation-prone copying.",16.5,True,NAVY)],
 [L("THE VERDICT  (computed, then interpreted)",18,True,NAVY),
  L("Computed datum: deeds are transcribed into a complete, truthful record whose consequence unfolds later (45:29; 78:29; 18:49; 50:18; 17:13).",16.5),
  L("Interpretation (labelled): the genomics parallel — transcription → deferred phenotype → context-specific expression — is an illuminating teaching bridge. Honest limit: it is NOT a “scientific miracle”; its worth is a vivid mental model, not evidence. (نسخ here = transcribe, sense-checked vs abrogation.)",16.5,True,TEAL)],
 split=0.5,fillA=REDT,fillB=TINT)
s=slide(prs); title(s,"Special Topic · Week 9 — Appendix: input snippets (Book6, vocalized col 11)",19)
def pkg(refs): return [(e["ref"],e["snip"],e["tag"]) for e in GN if e["ref"] in refs]
appendix(s,[("TRANSCRIPTION — “We were transcribing”",TEAL,TINT,pkg({"45:29","78:29"})),
            ("TRANSLATION — “Read your record!”",AMBER,AMBERT,pkg({"17:14","21:47","17:13"})),
            ("Fidelity & the watchers",NAVY,TINT2,pkg({"18:49","50:18","99:7"}))])
_save(prs,OUT+"SpecialTopic_W09_istinsakh_genomics.pptx"); print("genomics",len(prs.slides))

print("ALL BUILT")

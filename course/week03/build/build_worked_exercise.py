# -*- coding: utf-8 -*-
import importlib.util, os, json, string
spec=importlib.util.spec_from_file_location("c","/tmp/wk3common.py"); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc
WK="/sessions/kind-compassionate-feynman/mnt/RootCourse/week03"
M=json.load(open(os.path.join(WK,'wk3_member_keys.json')))

# ---------------- WORKED EXAMPLE — ءمن morphology by hand ----------------
d=new_doc("Week 3 — Worked Example (ءمن morphology)")
TITLE(d,"Week 3 — Worked Example: the morphology of ءمن (believe)",
      "Reading a root through its surface forms and pattern families. The lesson: the root says WHAT; the pattern says HOW — agent, act, attribute, or mood.")
H(d,"Step 0 — The root and its forms")
P(d,"The root ء-م-ن appears in 879 tokens across 27 distinct surface forms. Think of the root as a lump of clay and the patterns (أوزان) as the moulds: one lump, many shapes.")
H(d,"Step 1 — Tally the surface forms (top of the list)")
table(d,[["surface form","count","share","what it is"],
         ["آمن","363","41%","verb — “he believed” (the act)"],
         ["مؤمنين","145","16.5%","active participle — “believers” (the agent)"],
         ["يؤمن","137","16%","verb (imperfect) — “he believes”"],
         ["إيمان","38","4%","masdar — “faith” (the abstract act)"],
         ["أمن","16","2%","noun — “security / safety” (a second sense)"]])
H(d,"Step 2 — Group the forms into pattern families")
bullet(d,[("Verb (the act): 61% — ",True),("آمن، يؤمن. Faith is most often something DONE.",False)])
bullet(d,[("Active participle (the agent): 26% — ",True),("مؤمن، مؤمنين. The people who believe.",False)])
bullet(d,[("Masdar (the abstract act): 5% — ",True),("إيمان. Faith named as a thing.",False)])
bullet(d,[("Security branch: 5% — ",True),("أمن (security), أمين (trustworthy) — the same root, a second sense.",False)])
H(d,"Step 3 — Read the shape (the unlearn)")
P(d,"The distribution is a claim: faith in the Qur'an is overwhelmingly a VERB — an act — not the abstract noun إيمان. The grammar itself carries the theology. And the root also branches into security: to believe (ءامن) is bound up with being made safe (أمن) and being trustworthy (أمين).")
H(d,"Step 4 — The external company (partners)")
P(d,"Now read the root's partners — the roots it travels with in the same ayah. ءمن's strongest specific partner is صلح (righteous deeds), then عمل (works): faith is almost never named alone — آمنوا وعملوا الصالحات. Its antonym كفر is also a close partner, because belief and disbelief are constantly contrasted.")
H(d,"Model two-sentence reading")
P(d,[("Fact:  ",True),("“61% of ء-م-ن's tokens are verb forms, and its strongest partner is صلح (significance z = 14).”",False)])
P(d,[("Interpretation:  ",True),("“I read faith here as an enacted commitment bound to righteous works, not an abstract belief.”",False)])
H(d,"Now you try")
P(d,"Take رحم (mercy). Tally its forms (top: رحمة, رحيم, رحمن), name the dominant pattern, and find its strongest partner (hint: it is غفر — forgiveness). Then write one fact + one labeled interpretation.")
d.save(os.path.join(WK,"Week3_Worked_Example_morphology.docx")); print("worked example saved")

# ---------------- EXERCISE ----------------
d=new_doc("Week 3 — Exercise (Partners & Forms)")
TITLE(d,"Week 3 — Exercise: Partners & Forms",
      "Two parts: a by-hand morphology analysis (Part 1) and an app partners read (Part 2). Submit the night before class; it gates the debrief.")
H(d,"Your assignment")
P(d,"Find your member number below. Part 1 is your root's forms; Part 2 is its partners. Integrity: use only your own row; every value must be reproducible.")
rows=[["#","Root","Gloss"]]
for rt,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    rows.append([str(m['member']),rt,m['gloss']])
table(d,rows,fontsize=10,widths=[5,12,22])
H(d,"Part 1 — By hand: your root's forms")
bullet(d,"From the app (or the Week-3 data bank), list your root's distinct surface forms and their counts.")
bullet(d,"Identify the dominant form and name its pattern family: verb (act), active participle (agent), masdar (abstract act), or intensive/adjective (attribute).")
bullet(d,"Note any polysemy — does the root branch into a second sense or opposite valence across its forms?")
H(d,"Part 2 — In the app: your root's partners")
bullet(d,"Read the significant-partners list (already frequency/length-controlled — the mechanism is Weeks 4–5).")
bullet(d,"Record the top three partner roots; mark any that is an ANTONYM of your root.")
bullet(d,"Take ONE screenshot of the forms view or the partners panel.")
H(d,"What to submit")
bullet(d,"Part 1: your form tally + the dominant pattern + any polysemy note.")
bullet(d,"Part 2: top-3 partners (one screenshot).")
bullet(d,"Two two-sentence readings (one per part): one computed fact + one labeled interpretation.")
H(d,"The discipline (keep in front of you)")
P(d,"The root says WHAT; the pattern says HOW. A partner is a lead, not a verdict — even an antonym can be a close partner.")
d.save(os.path.join(WK,"Week3_Exercise.docx")); print("exercise saved")

# ---------------- EXERCISE ANSWER KEY ----------------
d=new_doc("Week 3 — Exercise Answer Key (instructor)")
TITLE(d,"Week 3 — Exercise Answer Key (instructor)","All values computed from Book6. z = length-controlled significance.")
rows=[["#","Root","#forms","dominant form (share)","top partners (z)"]]
for rt,m in sorted(M.items(),key=lambda kv:kv[1]['member']):
    tf=m['top_forms'][0]; ps=", ".join(f"{b} ({z})" for b,j,z in m['partners'])
    rows.append([str(m['member']),rt,str(m['nforms']),f"{tf[0]} ({tf[2]}%)",ps])
table(d,rows,fontsize=9,widths=[4,9,8,20,30])
H(d,"Teaching notes")
bullet(d,"Mutual top-partner pairs are striking: رحم↔غفر (mercy & forgiveness) and سمع↔بصر (hearing & seeing) name each other.")
bullet(d,"Dominant-form patterns vary: خلق is 78% one form (a tight concept); شهد spreads thin across 23 forms (a legal-witness family).")
bullet(d,"Full credit if the form tally, the named pattern family, and both readings (fact vs interpretation) are correct.")
d.save(os.path.join(WK,"Week3_Exercise_Answer_Key.docx")); print("exercise key saved")
print("SET 1 DONE")

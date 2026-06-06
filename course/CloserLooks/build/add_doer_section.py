# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/CloserLooks/build")
from _dochelper import P,H,bullet,table
from docx import Document
DOC="/sessions/kind-compassionate-feynman/mnt/RootCourse/CloserLooks/CloserLooks_Methods_and_Data.docx"
doc=Document(DOC)
tgt=None
for p in doc.paragraphs:
    if p.text.strip().startswith("Standing limitations"): tgt=p._p; break
assert tgt is not None
new=[]
def add(el): new.append(el)
F=False; T=True

add(H(doc,"Addendum — the human: diagnosed, and the two-column prescription (doer + deed)",size=15)._p)
add(P(doc,[("Why this addendum. ",T),("Closer Looks #4 and #7 establish the corpus's signature pairing as faith + righteous DEEDS, and the Week-10 prescription leaned on the outer/action register (deeds, prayer, patience, spending). That under-weights the INNER register the corpus places upstream of action. This section restores the balance: goodness of the deed (husn fi'li) AND goodness of the doer (husn fa'ili). All values computed from Book6.",F)])._p)
add(P(doc,[("Claim audited. ",T),("The Qur'an's prescription for the human is essentially a program of outward deeds.",F)])._p)
add(P(doc,[("Method. ",T),("(a) Compare document-frequency of the inner/actor field vs the outer/deed field. (b) Length-aware co-occurrence lift for heart-as-locus, sincerity-gating, and the faith-deeds coupling. (c) Treat the prophetic-mission formula (recite, purify, teach Book & wisdom) as a fixed phrase and test its full co-presence.",F)])._p)
add(P(doc,[("Data - the two registers (doc-freq, verses present). ",T),("The inner register is comparable in weight to the deed register, not subordinate to it:",F)])._p)
add(table(doc,[
 ["Inner register - the DOER","df","Outer register - the DEED","df"],
 ["علم knowledge / teaching","728","عمل righteous deeds","313"],
 ["نفس self (nafs)","270","صبر patience","93"],
 ["ذكر remembrance","264","صلو prayer","90"],
 ["وقي taqwa / guarding","237","نفق spending","86"],
 ["حسن excellence","177","زكو charity / purify","56"],
 ["قلب heart","155","—",""],
 ["نظر considered look","115","—",""],
 ["خلص sincerity","30","—",""],
],widths=[2.7,0.7,2.7,0.7])._tbl)
add(P(doc,[("Data - the heart is named as the locus (lift over chance). ",T),("Disease, faith, and tranquility are seated in the heart, not in the act: قلب-مرض (disease) 21x (12 v); قلب-طمأن (tranquility) 23.5x (7 v); صدر-شرح (expanded breast) 145x (5 v); قلب-ءمن (faith) 2.7x (49 v).",F)])._p)
add(P(doc,[("Data - the doer gates the deed. ",T),("Sincerity conditions the act: خلص-دين (religion) 28.7x (12 v); خلص-عبد (worship) 11.6x (14 v) - \"sincere to Him in religion.\" And the two registers are bound as one: faith-deeds 101 verses, 2.8x (the alladhina amanu wa-'amilu s-salihat formula); excellence-deeds 3.5x - not merely doing, but doing WELL.",F)])._p)
add(P(doc,[("Data - the inner program's institutional source: the prophetic mission. ",T),("The thought/knowledge register is not self-generated; the corpus seats it in the messenger's task. The formula recite, purify, teach the Book and wisdom (تلو, زكو, علم, حكم, كتب) appears as a complete unit in exactly four verses - 2:129, 2:151, 3:164, 62:2 - every element co-present in all four. Pairwise within it: تلو-زكو 7.3x, علم-حكم 3.2x, كتب-حكم 3.7x, رسل-زكو 3.1x. The mission's middle term is تزكية (purify) - the very verb of ash-Shams 91:9.",F)])._p)
add(P(doc,[("Verdict (scoped). ",T),("The claim is corrected. The prescription is two-columned and the inner column is the source:",F)])._p)
add(bullet(doc,[("Doer (inner, upstream): ",T),("faith, taqwa, sincerity, a sound/purified heart (tazkiyat an-nafs), remembrance, knowledge, and reflection.",F)])._p)
add(bullet(doc,[("Deed (outer, downstream): ",T),("righteous works, prayer, patience, and spending - the EVIDENCE of which way the self was turned.",F)])._p)
add(P(doc,[("The two are coupled, never split (faith-deeds), and the inner program is DELIVERED through the prophetic mission's teaching and purification. This tightens the series frame: the object of ash-Shams 91:9-10 is the nafs (the self) - purify IT or corrupt IT - so thought is the root and action the fruit. Husn fa'ili wa fi'li.",F)])._p)
add(P(doc,[("Limitation. ",T),("The explicit \"intention\" root نية is essentially absent (1 ayah); intention is carried as a FIELD (heart / taqwa / sincerity), not one lexeme. Whisper (وسوس) and heart-tremble (وجل) roots are thin (5 v each). The prophetic triad is a 4-verse fixed formula - robust AS a formula (total co-presence), not a high-frequency pattern; its pairwise lifts rest on small support. Field membership is a transparent, non-unique lexical choice, reported in full.",F)])._p)

for el in new: tgt.addprevious(el)
doc.save(DOC)
print("added",len(new),"elements")

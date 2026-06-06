# -*- coding: utf-8 -*-
import sys
sys.path.insert(0,"/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Quran_as_Signal/build")
from st_slides import *
from diagrams import fbox,harrow,vdash,band,isocube,sigrow,matgrid
from pptx.util import Inches,Pt
OUT="/sessions/kind-compassionate-feynman/mnt/RootCourse/TwoBooks/Quran_as_Signal/"
prs=deck()
def two(s,A,B,sp=0.5,fa=TINT,fb=TINT2): two_stack(s,A,B,split=sp,fillA=fa,fillB=fb)
def three(s,A,B,C,f=(TINT,AMBERT,TINT2)): three_stack(s,A,B,C,fills=f)

# 1 TITLE
s=slide(prs)
panel(s,0.42,1.1,12.5,1.5,TINT2,[L("THE TWO BOOKS  ·  a Qur’an-and-science lecture",16,True,TEAL),L("The Qur’an as Signal",32,True,NAVY)],space=7)
fbox(s,0.7,3.1,3.5,1.3,TINT,"AYAH = 1D","a signal (vector)",line=TEAL,tsz=17,ssz=12)
harrow(s,4.4,3.6,0.7,"",color=GREY)
fbox(s,5.3,3.1,3.5,1.3,AMBERT,"SURAH = 2D","an image (matrix)",line=AMBER,tsz=17,ssz=12)
harrow(s,9.0,3.6,0.7,"",color=GREY)
fbox(s,9.9,3.1,2.9,1.3,REDT,"CORPUS = 3D","a volume (tensor)",line=RED,tsz=16,ssz=12)
panel(s,0.42,4.7,12.5,2.5,TINT,[L("A methodological analogy — and a faithful one",17,True,NAVY),
  L("The text’s structure literally admits signal representations: a verse is a sequence, a sūra a matrix, the corpus a tensor. This is exactly what the course’s frequency / distribution / network methods operate on. Audited: ✓ Supported · ✗ Breaks (meaning ≠ signal) · ~ Silent.",16,False,INK)],space=9)

s=slide(prs); title(s,"The Two Books — two revelations of one Author")
three_stack(s,
 [L("عالم التدوين — the WORD (قول الله)",17,True,TEAL),L("The Qur’an: God’s speech, revealed in language. The composed Book — tadwīn, “what is set down.” The Book of SCRIPTURE.",16)],
 [L("عالم التكوين — the ACT (فعل الله)",17,True,AMBER),L("The Universe: God’s deed, revealed in creation. The Book of CREATION — takwīn, “what is brought into being.”",16)],
 [L("One Author · one reader",17,True,NAVY),L("Same SOURCE — Allah. Same primary ADDRESSEE — the human being (insān); the jinn too (a later lecture). Both are āyāt (signs); this series reads them side by side, never collapsed.",16)],
 fills=(TINT,AMBERT,TINT2))
# 2 IDEA (text)
s=slide(prs); title(s,"The idea — climbing the dimensions")
two(s,[L("DATA HAS DIMENSION",18,True,NAVY),L("Signal processing studies data by its shape: 1D signals (audio, a vector), 2D images (a matrix), 3D volumes (a tensor / video). Each dimension brings its own tools.",17)],
 [L("THE QUR’AN HAS THE SAME LADDER",18,True,TEAL),L("An ayah is a 1D sequence; a sūra a 2D collection of ayahs × features; the whole corpus a 3D tensor. The course already “processes” these — frequency, structure, networks.",17,True,NAVY)],sp=0.5,fa=TINT2,fb=TINT)

# 3 VISUAL 1D
s=slide(prs); title(s,"1D — the ayah as a signal")
band(s,0.42,1.2,12.5,0.44,TINT,"AYAH  ·  one axis: token position",TEAL)
sigrow(s,1.0,1.9,11.0,[.4,.7,.3,.9,.5,.8,.35,.6,.95,.45,.7,.5],col=TEAL)
panel(s,0.42,3.5,12.5,3.7,TINT2,[L("A verse is a vector",18,True,NAVY),
  L("Read along ONE axis — position — an ayah is a sequence of roots/tokens: a 1D signal. Its “length” is its number of tokens (1 to 84; median 7).",17),
  L("Doubly so: قرآن means “the recited” — so an ayah is also a literal ACOUSTIC waveform (tajwīd) — a 1D signal the bare text omits.",17,True,TEAL),
  L("Signal tool ↔ course method: spectral / FREQUENCY analysis = Week 1.",16.5,True,AMBER)],space=8)

# 4 VISUAL 2D
s=slide(prs); title(s,"2D — the sūra as an image")
band(s,0.42,1.2,12.5,0.44,AMBERT,"SŪRA  ·  two axes: ayah × feature",AMBER)
matgrid(s,3.4,1.85,6.5,2.0,5,12,[TINT,LTEAL,AMBERT,TEAL,WHITE])
panel(s,0.42,4.1,12.5,3.1,TINT,[L("A sūra is a matrix",18,True,NAVY),
  L("Stack the ayahs (rows) against their features — roots, forms, densities (columns) — and a sūra becomes a 2D image. Its “size” is ayahs × tokens (3–286 ayahs tall).",17),
  L("Signal tool ↔ course method: image STRUCTURE / distribution & concentration = Week 2.",16.5,True,AMBER)],space=9)

# 5 VISUAL 3D
s=slide(prs); title(s,"3D — the corpus as a volume (tensor)")
band(s,0.42,1.2,12.5,0.44,REDT,"CORPUS  ·  three axes: sūra × ayah × token (or revelation-time)",RED)
isocube(s,1.2,1.95,2.6,fill=TINT,line=NAVY)
harrow(s,4.4,3.1,1.1,"stack sūras",color=GREY,lcol=NAVY)
isocube(s,6.0,1.95,2.6,fill=AMBERT,line=AMBER)
panel(s,0.42,4.7,12.5,2.5,TINT2,[L("A volume — and a “video” of revelation",18,True,NAVY),
  L("Stack the sūra-images into a tensor: sūra × ayah × token. Make the THIRD axis revelation-time (nuzūl) and the static muṣḥaf becomes a “video” — recovering the chronology the muṣḥaf order hides.",17),
  L("Signal tool ↔ course method: volumetric / NETWORK & co-occurrence analysis = Weeks 4–6.  (4D = the corpus evolving over revelation-time.)",16.5,True,AMBER)],space=9)

# 6 VISUAL DATA — the real signal sizes
s=slide(prs); title(s,"The data — the shapes of the signals (from Book6)")
finding2(s,
 {"title":"1D — ayah lengths (root-tokens)","cats":["1–2","3–10","11–30","31–60","61+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[769,3829,1576,61,1])],"legend":False},
 {"title":"2D — sūra sizes (# ayahs)","cats":["3–10","11–50","51–100","101–200","201+"],
  "series":[("",[GREY,TEAL,TEAL,AMBER,RED],[19,48,29,15,3])],"legend":False},
 [L("1D signals: short, with rare giants",17.5,True,TEAL),
  L("Most ayahs are 3–10 tokens (median 7); one runs to 84 (the debt verse, 2:282). A signal with a heavy tail.",16)],
 [L("2D images: varied frames",17.5,True,AMBER),
  L("Sūra “images” range 3–286 ayahs tall (median 39). The corpus is a stack of very differently-sized frames.",16)],
 fillA=TINT,fillB=AMBERT)

# 6b DATA — Zipf spectrum (both scales) + dimensions
s=slide(prs); title(s,"The spectrum — Zipf’s law at every scale (real data)")
finding2(s,
 {"title":"Root-frequency spectrum (top 8 of 1700)","cats":["ءله","قول","كون","ربب","ءمن","علم","قوم","ءتي"],
  "series":[("",[NAVY,TEAL,TEAL,AMBER,AMBER,AMBER,GREY,GREY],[2851,1722,1390,980,879,854,660,549])],"legend":False},
 {"title":"Letter-frequency spectrum (×1000)","cats":["ا","ن","م","ل","ي","ء"],
  "series":[("",[NAVY,TEAL,TEAL,AMBER,AMBER,GREY],[35.8,28.0,26.7,26.1,24.7,19.1])],"legend":False,"fmt":"{:.0f}"},
 [L("A heavy-tailed signal",17.5,True,TEAL),
  L("A few units dominate, then a long tail — at the ROOT scale (ءله 2851 … 1700 roots) and the LETTER scale alike. This Zipf/power-law shape is exactly the statistics of natural language and 1/f natural signals.",16)],
 [L("Self-similar across scales",17.5,True,AMBER),
  L("The same heavy-tailed spectrum at letters and roots — a signal that looks alike when you zoom. The corpus tensor: 114 sūras × 6236 ayahs × 51,044 tokens, from 1700 roots.",16)],
 fillA=TINT,fillB=AMBERT)
# 7 VISUAL MAPPING — dimension -> op -> week
s=slide(prs); title(s,"The mapping — signal processing IS the course’s method")
def row(y,dim,dcol,op,wk):
    fbox(s,0.6,y,3.0,1.0,dcol,dim,"",line=NAVY,tsz=16); harrow(s,3.8,y+0.34,1.6,"analyse",color=GREY,lcol=TEAL)
    fbox(s,5.6,y,4.0,1.0,TINT2,op,"",line=TEAL,tsz=15); harrow(s,9.8,y+0.34,1.0,"",color=GREY)
    fbox(s,10.9,y,1.9,1.0,AMBERT,wk,"",line=AMBER,tsz=15)
row(1.45,"1D · ayah",TINT,"frequency / spectral","Week 1")
row(2.75,"2D · sūra",LTEAL,"image structure / distribution","Week 2")
row(4.05,"3D · corpus",AMBERT,"networks / co-occurrence","Wks 4–6")
panel(s,0.42,5.35,12.5,1.85,TINT,[L("The analogy is unusually FAITHFUL",17,True,NAVY),
  L("Unlike a metaphor, this maps the course’s ACTUAL operations: counting along 1D = spectral; reading the 2D layout = image analysis; linking roots across the 3D corpus = graph/volume processing.",16,True,TEAL)],space=8)

# 8 AUDIT (text)
s=slide(prs); title(s,"Audit — supported, broken, and silent")
three(s,[L("✓ SUPPORTED",17,True,TEAL),L("The structures are literally true: an ayah IS a sequence, a sūra a matrix, the corpus a tensor — and the course’s methods are exactly these operations.",16)],
 [L("✗ BREAKS",17,True,RED),L("Meaning is NOT a signal property. A verse is not reducible to its vector; guidance, beauty, address are lost in the numbers. The signal is the carrier, not the message.",16)],
 [L("~ SILENT (surmisable)",17,True,AMBER),L("The choice of 3rd axis (time vs meaning-embedding) is a modeling decision the text doesn’t dictate; recitation adds a real acoustic signal the written corpus omits.",16)],f=(TINT,REDT,AMBERT))

# 9 SYNTHESIS (text)
s=slide(prs); title(s,"Synthesis & discussion — the Two Books")
two(s,[L("THE TWO BOOKS",18,True,NAVY),L("The tools we use to read the Book of Creation’s signals — 1D, 2D, 3D — are the very tools this course turns on the Book of Scripture. Same mathematics of structure; different content. Read side by side, never collapsed.",17,True,TEAL)],
 [L("FOR DISCUSSION",18,True,AMBER),L("• What is gained, and lost, when a verse becomes a vector?  • If revelation-time is the 3rd axis, what does the muṣḥaf order “blur”?  • Is recitation (the acoustic 1D signal) the dimension our text-analysis misses?  • Where must the signal analogy stop?",16.5)],sp=0.5,fa=TINT2,fb=AMBERT)
s=slide(prs); title(s,"Real-world relevance & takeaway")
two(s,[L("REAL-WORLD RELEVANCE",18,True,NAVY),L("The corpus is analysable with the full DSP / image / tensor toolkit — which is exactly what the course’s frequency, distribution, and network methods are.",17,True,TEAL)],
 [L("THE TAKEAWAY",18,True,AMBER),L("Ayah = 1D signal, sūra = 2D image, corpus = 3D tensor; reading the Qur’an quantitatively IS signal processing.",17,True,NAVY)],sp=0.5,fa=TINT,fb=AMBERT)
prs.save(OUT+"Quran_as_Signal_Lecture.pptx")
print(f"slides: {len(prs.slides)} ; visual/data slides: 7")

# -*- coding: utf-8 -*-
"""Build a companion slide deck from an 8-beat lecture-notes .docx.
Reuses the LOCKED st_slides.py engine. One title slide + one slide per module.
Single source of truth: parses the notes docx, so slides always match notes.
Usage: python build_lecture_slides.py <build_dir> <notes.docx> <out.pptx> <series_tag> <deck_title> <spine>
"""
import sys, os
BUILD_DIR, NOTES, OUT, TAG, DECK_TITLE, SPINE = sys.argv[1:7]
sys.path.insert(0, BUILD_DIR)
from st_slides import *  # deck, slide, title, panel, L, two_stack, three_stack, colors
from docx import Document

# ---- parse the notes docx into modules ----
doc = Document(NOTES)
BEATS = ["What it is","Why we do it","How it's done","What we get",
         "Why it matters","In the data","Takeaway","Bridge"]
mods = []          # list of {title, beats:{label:text}}
cur = None
for p in doc.paragraphs:
    t = p.text.strip()
    if t.startswith("Module "):
        cur = {"title": t, "beats": {}}
        mods.append(cur)
    elif cur is not None:
        for b in BEATS:
            if t.startswith(b + ":"):
                cur["beats"][b] = t[len(b)+1:].strip()
                break

# ---- build deck ----
prs = deck()

# Title slide
s = slide(prs)
panel(s, 0.42, 1.20, 12.5, 1.7, TINT2,
      [L(TAG, 16, True, TEAL), L(DECK_TITLE, 26, True, NAVY)], space=7)
panel(s, 0.42, 3.18, 12.5, 2.05, TINT,
      [L("The honest spine", 18, True, NAVY), L(SPINE, 17, True, TEAL)], space=8)
panel(s, 0.42, 5.40, 12.5, 1.78, TINT2,
      [L("How to read these slides", 16, True, NAVY),
       L("Eight beats per module: What it is · Why · How · What we get · Why it matters · "
         "In the data (a real Book6 number) · Takeaway · Bridge. Every figure is computed "
         "live from the corpus; nulls (permutation / Poisson / shuffle) throughout.", 15.5)],
      space=7)

# Module slides
for m in mods:
    b = m["beats"]
    s = slide(prs)
    title(s, m["title"])
    # Concept (left) + Method (right)
    panel(s, 0.42, 1.18, 6.05, 2.68, TINT,
          [L("Concept", 15, True, TEAL),
           L("What it is — " + b.get("What it is",""), 14.5),
           L("Why we do it — " + b.get("Why we do it",""), 14.5)], space=7)
    panel(s, 6.67, 1.18, 6.25, 2.68, TINT2,
          [L("Method & output", 15, True, NAVY),
           L("How it's done — " + b.get("How it's done",""), 14.5),
           L("What we get — " + b.get("What we get",""), 14.5)], space=7)
    # In the data (highlighted) + Why it matters
    panel(s, 0.42, 4.00, 12.5, 2.02, AMBERT,
          [L("In the data  (Book6)", 15, True, AMBER),
           L(b.get("In the data",""), 16, True, NAVY),
           L("Why it matters — " + b.get("Why it matters",""), 14.5)], space=8)
    # Takeaway + Bridge bar
    panel(s, 0.42, 6.16, 12.5, 1.05, TINT,
          [L("Takeaway — " + b.get("Takeaway",""), 15, True, TEAL),
           L("Bridge — " + b.get("Bridge",""), 13.5, False, GREY)], space=5)

prs.save(OUT)
print("deck built:", OUT, "| modules:", len(mods))

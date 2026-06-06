# -*- coding: utf-8 -*-
"""§14a: concept = sense-verified SURFACE FORMS, not raw root. Transparent include/exclude
substrings on normalized surface forms; count āyahs with >=1 passing form. Reproducible."""
import sys
from collections import Counter
sys.path.insert(0,"/sessions/stoic-serene-wozniak/mnt/Downloads/Quran_Root_Explorer_Web_v1.2")
import analysis
_c=analysis.load_corpus("Book6.xlsx"); K=analysis.normalize_letters
# precompute per-ayah (root, surface) pairs
PAIRS=[]
for i in range(len(_c.df)):
    row=[]
    for j,r in enumerate(_c.root_tokens[i]):
        sf=K(_c.surface_tokens[i][j]) if j<len(_c.surface_tokens[i]) else ""
        row.append((K(r),sf))
    PAIRS.append(row)
def count(root, include=None, exclude=None):
    rt=K(root); n=0
    for row in PAIRS:
        ok=False
        for rr,sf in row:
            if rr!=rt: continue
            if include and not any(p in sf for p in include): continue
            if exclude and any(p in sf for p in exclude): continue
            ok=True; break
        if ok: n+=1
    return n
# verified filters (only where the form audit showed conflation)
FILT={
 "علم":dict(exclude=["عالم"]),                       # knowledge, not the worlds
 "سمو":dict(exclude=["اسم","مسم"]),                   # heaven, not name(s)
 "نور":dict(include=["نور","منير"]),                  # light, not fire (نار)
 "قوم":dict(exclude=["قيا","ستقيم","اقيم","اقام"]),    # people, not standing/resurrection
 "حسب":dict(include=["حساب","حسيب"]),                 # reckoning/account, not supposing
 "جنن":dict(include=["جنه","جنا","جنت"]),             # garden, not jinn/madness
 "قلب":dict(exclude=["نقلب","تقلب"]),                 # heart, not turning
 "ملك":dict(exclude=["ملاء","ملائ"]),
 "كبر":dict(include=["ستكبر","تكبر","مستكبر"]),                 # sovereign, not angels
}
def C(root):
    f=FILT.get(K(root),{})
    return count(root, f.get("include"), f.get("exclude"))
if __name__=="__main__":
    print("verified concept counts (raw root -> sense-filtered):")
    for g,r in [("knowledge","علم"),("heaven","سمو"),("light","نور"),("people","قوم"),
                ("reckoning","حسب"),("garden","جنن"),("heart","قلب"),("sovereign","ملك")]:
        raw=count(r); filt=C(r); print(f"  {g:11s} {r}: raw {raw:4d} -> verified {filt:4d}")

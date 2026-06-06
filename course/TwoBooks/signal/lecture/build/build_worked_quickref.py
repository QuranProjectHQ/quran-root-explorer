# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
SIGDIR=os.path.dirname(WK)
SB=json.load(open(os.path.join(SIGDIR,"handson","signal_data_bank.json"),encoding="utf-8"))
z=[r for r in SB if r["translit"]=="zulm"][0]

# ---------- WORKED EXAMPLE ----------
d=new_doc("Two Books · Signal — Worked Example")
TITLE(d,"Two Books · Signal — Worked Example: is the root ẓulm bursty?",
      "One root, walked end to end with live Book6 numbers and the Poisson null. The skill: never read a count without its null, and never read a spectral peak without its frequency.")
H(d,"Step 1 — State the question",size=13)
P(d,"Does ẓulm (ظلم) recur EVENLY across the reading order, or in CLUSTERS? 'Evenly' has a precise null: a memoryless Poisson process, whose Fano factor (variance ÷ mean of per-sūra counts) equals 1.")
H(d,"Step 2 — Pull the live numbers",size=13)
table(d,[["quantity","value (Book6)"],
         ["occurrences (n)",str(z["n"])],
         ["mean gap between occurrences",str(z["mean_gap"])+" āyahs"],
         ["Fano factor",str(z["fano"])],
         ["permutation p","%.4f"%z["p"]],
         ["verdict",z["verdict"]]])
H(d,"Step 3 — Compare to the null",size=13)
bullet(d,"Poisson baseline: Fano = 1 (even arrivals). Observed Fano = %s — about %d× the baseline."%(z["fano"],round(z["fano"])))
bullet(d,"Permutation p ≈ %.4f: a reshuffled order almost never reaches this Fano, so the clustering is real."%z["p"])
bullet(d,"Read the gaps: mean gap %s āyahs, but occurrences arrive in tight runs separated by long empty stretches — the signature of burstiness, not a steady beat."%z["mean_gap"])
H(d,"Step 4 — Place it in the corpus picture",size=13)
P(d,"ẓulm's burstiness is not isolated. Across the whole order, sūra-length shows lag-1 autocorrelation +0.67 (gentle memory), the entropy spectrum has a significant peak at p ≈ 0.0005 — but at the LOWEST frequency, i.e. a slow trend, not a cycle — and the significant wavelet scales are the coarse 32/64/128. All point to the same slow global trend plus bursty thematic repetition.")
H(d,"Step 5 — Report: one fact + one labelled reading",size=13)
P(d,[("Fact:  ",True),("ẓulm occurs %d times with Fano %s (Poisson = 1) at p ≈ %.4f — significantly bursty/clustered."%(z["n"],z["fano"],z["p"]),False)])
P(d,[("Interpretation (labelled):  ",True),("I read ẓulm as a theme that arrives in concentrated passages rather than being sprinkled evenly — coherent repetition, not a transmitted code.",False)])
P(d,[("Guard:  ",True),("burstiness ≠ periodicity. The spectral peak is a low-frequency trend; nothing here is a fixed cycle or a carrier wave.",False)],color=c.GREY if hasattr(c,'GREY') else None)
d.save(os.path.join(WK,"Signal_Worked_Example.docx")); print("signal worked example saved")

# ---------- QUICK REFERENCE ----------
d=new_doc("Two Books · Signal — Quick Reference (1 page)")
TITLE(d,"Two Books · Signal — Quick Reference (1 page)","The signal lens at a glance. Keep this beside the app.")
H(d,"The app in 4 steps",size=13)
bullet(d,"Open Two Books → Signal. Pick the signal (sūra-length, tokens/āyah, or letter-entropy).")
bullet(d,"Read the per-step series; run the permutation / Poisson / circular-shift null for each test.")
bullet(d,"For any peak, read WHERE it sits: low frequency = trend, mid-band = cycle.")
bullet(d,"Record one fact (with its null) + one labelled interpretation.")
H(d,"The measures",size=13)
bullet(d,[("Autocorrelation",True),(" — self-similarity at a lag; lag-1 +0.67 = gentle memory.",False)])
bullet(d,[("Fano factor",True),(" — variance ÷ mean of per-sūra counts; Poisson = 1; > 1 = bursty.",False)])
bullet(d,[("FFT spectrum",True),(" — power by frequency; a low-frequency peak is a TREND, not a cycle.",False)])
bullet(d,[("Wavelet / scalogram",True),(" — energy by SCALE and position; coarse scales 32/64/128 significant.",False)])
bullet(d,[("CV of āyah length",True),(" — spread ÷ mean ≈ 0.75 = wide, speech-like rhythm.",False)])
H(d,"Read honestly",size=13)
bullet(d,"DO compare every statistic to its null before reading it.")
bullet(d,"DON'T call a low-frequency peak 'periodicity' — it is a slow trend.")
bullet(d,"DON'T promote cross-correlation overlap into causation.")
H(d,"Anchor numbers",size=13)
bullet(d,"lag-1 autocorr +0.67 · spectral peak p ≈ 0.0005 (low-freq) · wavelet 32/64/128 · āyah CV ≈ 0.75 · sampled roots Fano 40–61 at p ≈ 0.0002.")
H(d,"Honest spine",size=13)
P(d,"A slow trend across the order + thematic clustering — no fine periodicity, no carrier wave.",size=10)
d.save(os.path.join(WK,"Signal_Quick_Reference.docx")); print("signal quick-ref saved")

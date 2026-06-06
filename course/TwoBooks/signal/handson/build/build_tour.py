# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
B=json.load(open(os.path.join(WK,"signal_data_bank.json"),encoding="utf-8"))
TB=json.load(open(os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json"),encoding="utf-8"))
S=TB["signal"]
# EXERCISE
d=new_doc("Signal — Guided-Tour Exercise")
TITLE(d,"Signal — Guided Tour Exercise (all tabs)",
      "Walk through every tool on the Signal page. Some steps use YOUR assigned root; others are whole-corpus "
      "results everyone records. Submit the night before class.")
H(d,"Your assignment")
rows=[["#","your root","occurrences","first 5 occurrence āyah-indices"]]
for i,b in enumerate(B,1): rows.append([str(i),b["root"],str(b["n"]),", ".join(map(str,b["first5"]))])
table(d,rows)
H(d,"📈 Tab 1: Length signal",size=12)
bullet(d,"Run the autocorrelation. Record the lag-1 value (whole corpus) and say whether neighbouring sūras have related lengths (memory).")
H(d,"🔁 Tab 2: Root recurrence (your root)",size=12)
bullet(d,"Part 1 (by hand): from your first 5 occurrence indices compute the 4 gaps and their mean.")
bullet(d,"Part 2 (app): pick your root; record the Fano factor, the mean gap, the dispersion p, and the verdict (bursty / regular / ~Poisson).")
H(d,"🌊 Tab 3: Entropy spectrum",size=12)
bullet(d,"Run the FFT peak test; record its p. Run the Haar wavelet test; record which scales are significant. Build the Ricker scalogram; note at which scales the bright band sits.")
H(d,"🥁 Tab 4: Verse rhythm",size=12)
bullet(d,"Record the coefficient of variation of āyah lengths (whole corpus).")
H(d,"🔗 Tab 5: Co-recurrence",size=12)
bullet(d,"Cross-correlate your root with one partner root of your choice; record the peak lag and whether the circular-shift test calls it significant.")
H(d,"What to submit")
bullet(d,"Tab 1 lag-1 + memory verdict; Tab 2 your 4 gaps & mean (by hand) + Fano, mean gap, dispersion p, verdict; Tab 3 FFT p + significant wavelet scales; Tab 4 the CV; Tab 5 your pair's peak lag + significance.")
d.save(os.path.join(WK,"Signal_Exercise.docx"))
# ANSWER KEY
d=new_doc("Signal — Guided-Tour Answer Key")
TITLE(d,"Signal — Guided Tour Answer Key (instructor)","All values computed from Book6.")
H(d,"Whole-corpus results")
table(d,[["tool","result","reading"],
  ["Length autocorrelation (lag-1)",f"{S['autocorr_lag1']:+.2f}","positive → long sūras cluster (memory)"],
  ["Entropy-spectrum FFT peak",f"p = {S['fft_peak_p']:.2g}","no fixed periodicity beyond chance"],
  ["Haar wavelet significant scales",", ".join(map(str,S['wavelet_sig_scales']))+" sūras","coarse scales = a slow trend"],
  ["Verse-rhythm CV (āyah length)",f"{S['ayah_len_cv']:.2f}","āyah lengths vary widely"]])
H(d,"Per-root dispersion (tab 2)")
rows=[["#","root","occurrences","mean gap","Fano","disp. p","verdict"]]
for i,b in enumerate(B,1): rows.append([str(i),b["root"],str(b["n"]),str(b["mean_gap"]),str(b["fano"]),f"{b['p']:.3g}",b["verdict"]])
table(d,rows)
H(d,"Teaching point")
nb=sum(1 for b in B if b["fano"]>1.2)
P(d,f"All {nb} of {len(B)} roots are bursty (Fano > 1): content words cluster because the Qur'an develops a "
    "theme across consecutive passages. The FFT shows no fixed periodicity, and the wavelet finds only a "
    "slow coarse-scale trend — ordinary discourse structure, measured honestly, not a hidden signal. "
    "Co-recurrence peaks (tab 5) vary by pair and usually sit near lag 0 (shared themes).")
d.save(os.path.join(WK,"Signal_Exercise_Answer_Key.docx"))
print("signal tour built")

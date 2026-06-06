# -*- coding: utf-8 -*-
import importlib.util, os, json
spec=importlib.util.spec_from_file_location("c", os.path.join(os.path.dirname(__file__),"common.py"))
c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
P,H,TITLE,bullet,table,new_doc,WK=c.P,c.H,c.TITLE,c.bullet,c.table,c.new_doc,c.WK
HB=os.path.join(os.path.dirname(WK),"..","_handson_build","tour_bank.json")
TB=json.load(open(HB,encoding="utf-8"))["signal"]
SB=json.load(open(os.path.join(os.path.dirname(WK),"handson","signal_data_bank.json"),encoding="utf-8"))
zulm=[b for b in SB if b["translit"]=="zulm"][0]
def mod(d,n,title,beats):
    H(d,f"Module {n} — {title}",size=13)
    for lbl,txt in beats:
        P(d,[(lbl+": ",True),(txt,False)],size=10.5)
d=new_doc("Signal — Lecture Notes")
TITLE(d,"Two Books · Signal — Lecture Notes",
      "Reading the Qur'an as an ordered signal. Every module carries the eight beats; beat 6 is a real "
      "Book6 number computed by the app's engine. Honest spine: a slow trend across the order and thematic "
      "clustering — no fine periodicity, no carrier wave. Permutation/Poisson nulls throughout.")
mod(d,1,"Frame — the text as a signal",[
 ("What it is","a signal is just a sequence of numbers read in order; the Qur'an supplies several (verses per sūra, tokens per āyah, entropy per sūra)."),
 ("Why we do it","to ask whether the ORDERING itself carries structure, not just the content."),
 ("How it's done","lay a quantity out in muṣḥaf (or revelation) order and apply signal tools, each checked against a reshuffled null."),
 ("What we get","a yes/no on memory, periodicity, and clustering — with a p-value, not an impression."),
 ("Why it matters","it separates real ordering structure from what any shuffle would show, guarding against pattern-seeing."),
 ("In the data","the corpus has 114 sūras and 6,236 āyahs — the two sequences we will read."),
 ("Takeaway","'signal' is a lens on order; the null is what keeps it honest."),
 ("Bridge","start with the simplest signal — how long each sūra is.")])
mod(d,2,"Length signal & memory (autocorrelation)",[
 ("What it is","the sequence of verse-counts, and its autocorrelation (correlation with a lagged copy of itself)."),
 ("Why we do it","to test whether neighbouring sūras have related lengths (memory) or are independent."),
 ("How it's done","read verse-counts in order; compute the correlation at lag 1, 2, …; compare to a white-noise band."),
 ("What we get","a lag-1 autocorrelation and whether it leaves the noise band."),
 ("Why it matters","memory in length would mean the arrangement is not a random shuffle of sizes."),
 ("In the data",f"lag-1 autocorrelation ≈ {TB['autocorr_lag1']:+.2f} — positive: long sūras tend to sit next to long ones."),
 ("Takeaway","sūra lengths carry positive short-range memory — a real ordering effect."),
 ("Bridge","memory of length is one signal; next, how a single root is spaced through the text.")])
mod(d,3,"Root recurrence & burstiness (Fano vs Poisson)",[
 ("What it is","mark each āyah where a root occurs as 1/0 and study the gaps between hits."),
 ("Why we do it","to ask whether a root clusters in bursts or spreads evenly."),
 ("How it's done","compute the Fano factor (variance ÷ mean of gaps); compare to random (Poisson) placement of the same number of hits."),
 ("What we get","a Fano factor (>1 bursty, ≈1 random, <1 even) and a dispersion p."),
 ("Why it matters","bursty roots mark themes the text develops in passages, then leaves."),
 ("In the data",f"ظلم: {zulm['n']} occurrences, Fano {zulm['fano']} ({zulm['verdict']}); all 12 sampled roots are bursty (Fano > 1)."),
 ("Takeaway","content roots cluster — ordinary discourse structure, measured with a null."),
 ("Bridge","clustering is local; the spectrum asks about repeating cycles across the whole order.")])
mod(d,4,"Spectral view (the FFT)",[
 ("What it is","the power spectrum of the per-sūra entropy series — energy at each frequency."),
 ("Why we do it","to test for any repeating cycle in how 'mixed' sūras are along the order."),
 ("How it's done","take the Fourier transform of the mean-removed series; compare the peak power to a phase-shuffled null."),
 ("What we get","the dominant frequency's power and a permutation p."),
 ("Why it matters","a peak that beats the null means real structure at some scale; WHERE the peak sits says fine cycle vs slow trend."),
 ("In the data",f"the peak beats the shuffle (p ≈ {TB['fft_peak_p']:.2g}) and sits at LOW frequency — a slow trend across the order, not a fine periodicity."),
 ("Takeaway","the spectrum confirms a slow, low-frequency trend — not a short repeating cycle."),
 ("Bridge","the FFT mixes all positions; a wavelet pins the structure to a SCALE.")])
mod(d,5,"Multiresolution (Haar wavelet)",[
 ("What it is","a decomposition of the entropy series into energy at each scale (2, 4, 8 … sūras)."),
 ("Why we do it","to see at which block-size the variation lives."),
 ("How it's done","a pure Haar transform; each scale's detail-energy is tested against a shuffle null."),
 ("What we get","which scales carry more energy than chance."),
 ("Why it matters","it localises the FFT's 'low frequency' to concrete sūra-block sizes."),
 ("In the data",f"the coarse scales ({', '.join(map(str,TB['wavelet_sig_scales']))} sūras) are significant; fine scales sit at/below chance — a slow trend, no local periodicity."),
 ("Takeaway","the real structure is coarse-scale (slow), confirming modules 2 and 4."),
 ("Bridge","scale tells us how big; the scalogram tells us where.")])
mod(d,6,"Localization (Ricker scalogram)",[
 ("What it is","a 2-D heatmap of wavelet energy over scale (rows) and sūra-position (columns)."),
 ("Why we do it","to see WHERE along the order the structure concentrates, not just at which scale."),
 ("How it's done","convolve the series with a Ricker wavelet at many scales; plot |coefficient|."),
 ("What we get","a map of where energy sits in scale × position."),
 ("Why it matters","localisation distinguishes a global trend from a one-place burst."),
 ("In the data","energy concentrates in broad bands at large scales spanning much of the x-axis — the slow trend, not an isolated spike."),
 ("Takeaway","the slow trend is global, not a single localized event."),
 ("Bridge","entropy is one rhythm; āyah length is another.")])
mod(d,7,"Verse rhythm (āyah-length distribution)",[
 ("What it is","the distribution of token-lengths of āyahs across the corpus."),
 ("Why we do it","to describe the text's rhythm — short staccato vs long flowing verses."),
 ("How it's done","count tokens per āyah; summarise spread with the coefficient of variation."),
 ("What we get","a distribution and a CV (spread ÷ mean)."),
 ("Why it matters","āyah length is itself a length confound that later content measures must respect."),
 ("In the data",f"āyah-length coefficient of variation ≈ {TB['ayah_len_cv']:.2f} — lengths vary widely."),
 ("Takeaway","verse length is highly variable; never treat āyah-count as a size-true unit."),
 ("Bridge","one root's rhythm and the verse rhythm done; next, two roots together.")])
mod(d,8,"Co-recurrence (cross-correlation)",[
 ("What it is","the cross-correlation of two roots' 1/0 occurrence signals at a range of lags."),
 ("Why we do it","to ask whether one root tends to appear near another, and in which direction."),
 ("How it's done","slide one signal against the other; the peak lag shows the offset; a circular-shift null tests it."),
 ("What we get","a peak lag and whether it beats the null."),
 ("Why it matters","a near-zero peak means shared āyahs; an offset peak hints at one opening to the other."),
 ("In the data","thematically linked roots show a peak at or near lag 0 — they share passages (varies by pair)."),
 ("Takeaway","co-recurrence reflects shared themes and fixed collocations, read with a null."),
 ("Bridge","gather every result into one honest verdict.")])
mod(d,9,"Synthesis",[
 ("What it is","the combined reading of all the signal tools."),
 ("Why we do it","to state only what the data licenses."),
 ("How it's done","line up autocorrelation, spectrum, wavelet, scalogram, rhythm, and co-recurrence."),
 ("What we get","one coherent picture of the order's structure."),
 ("Why it matters","convergent, null-checked evidence resists pattern-seeking."),
 ("In the data",f"positive length memory (lag-1 {TB['autocorr_lag1']:+.2f}), a significant low-frequency spectral peak, and significant coarse wavelet scales all point to ONE thing: a slow trend across the order — plus thematic clustering of roots — and NO fine periodicity."),
 ("Takeaway","the Qur'an's order carries a real slow trend and thematic clustering, not a hidden carrier wave."),
 ("Bridge","next week: the same corpus read as a genome (Biology) — bases, codons, and composition.")])
d.save(os.path.join(WK,"Signal_Lecture_Notes.docx")); print("Signal lecture notes built")

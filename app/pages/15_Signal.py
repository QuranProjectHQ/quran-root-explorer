"""Two Books · Signal — the Qur'an as a one-dimensional signal.

A companion to the Disjoint-Letters workbench. Here we treat the corpus as an
ordered SIGNAL and apply signal-processing tools — autocorrelation, dispersion,
and spectral analysis — each validated against a permutation / Poisson null so
no apparent structure is taken at face value.

Exploratory scaffold: these are honest, reproducible analyses over the loaded
corpus, not 'miracle' claims. Everything is computed live and guarded with
HAS_REV so the nuzūl (revelation-order) views degrade gracefully.
"""
from __future__ import annotations

import math
from collections import Counter

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from analysis import (COL_SURAH, COL_AYAH, COL_SURAH_NAME, COL_ROOTS,
                      COL_SEGMENTED, normalize_letters)
from state import get_corpus, hero, layer, log_page
from twobooks_stats import shannon_bits

st.set_page_config(page_title="Signal", page_icon="📡", layout="wide")
log_page("signal")
corpus = get_corpus()

NAVY = "#1D3557"; TEAL = "#2A9D8F"; AMBER = "#F77F00"; RED = "#E63946"
GREY = "#9CA3AF"; ICE = "#CADCFC"; PURPLE = "#7209B7"


# ───────────────────────── data ─────────────────────────
@st.cache_data(show_spinner=False)
def _signal_data(_corpus_id):
    df = corpus.df
    su = df[COL_SURAH].astype(int).tolist()
    ay = df[COL_AYAH].astype(int).tolist()
    verses = {}
    ayah_token_len = []          # tokens per ayah, in mushaf order
    letters = {s: Counter() for s in range(1, 115)}
    for i in range(len(df)):
        s = su[i]
        verses[s] = max(verses.get(s, 0), ay[i])
        toks = corpus.seg_tokens[i]
        ayah_token_len.append(len(toks))
        for t in toks:
            nt = normalize_letters(t)
            for ch in nt:
                if ch.strip():
                    letters[s][ch] += 1
    nuz = {int(k): int(v) for k, v in corpus.rev_order_of_surah.items()}
    return verses, ayah_token_len, letters, nuz


VERSES, AYAH_LEN, LETTERS, NUZ = _signal_data(id(corpus))
HAS_REV = len(NUZ) >= 113
if not HAS_REV:
    st.warning("No revelation-order column in this sheet — nuzūl views are hidden; "
               "muṣḥaf-order analyses are fully available.")
NAMEOF = {int(corpus.df[COL_SURAH].iat[i]): str(corpus.df[COL_SURAH_NAME].iat[i])
          for i in range(len(corpus.df))}


def autocorr(x, max_lag):
    x = np.asarray(x, dtype=float)
    x = x - x.mean()
    denom = np.dot(x, x)
    if denom == 0:
        return np.zeros(max_lag + 1)
    out = np.array([np.dot(x[:len(x) - k], x[k:]) / denom
                    for k in range(max_lag + 1)])
    return out


# ───────────────────────── hero ─────────────────────────
hero("📡 Two Books · Signal",
     "Treat the text as an ordered signal — autocorrelation, dispersion, and "
     "spectra — each checked against a permutation/Poisson null.")

st.markdown(
    "<div style='background:#EEF3FB;border-left:5px solid #1D3557;border-radius:8px;"
    "padding:9px 14px;margin:6px 0 14px;font-size:13.5px;color:#1D3557;'>"
    "A <b>signal</b> is just a sequence of numbers in order. The Qur'an gives several: "
    "verse counts per sūra, token lengths per āyah, entropy per sūra. Signal tools ask "
    "whether the ordering carries structure — periodicity, memory, clustering — beyond "
    "what a reshuffled version would show.</div>", unsafe_allow_html=True)

t_len, t_recur, t_spec, t_rhythm, t_xcorr = st.tabs(
    ["📈 Length signal", "🔁 Root recurrence", "🌊 Entropy spectrum",
     "🥁 Verse rhythm", "🔗 Co-recurrence"])


# ═══════════ TAB 1 — LENGTH SIGNAL ═══════════
with t_len:
    layer(1, "Sūra-length sequence and its memory")
    st.caption("Verse counts read off in order form a signal. Its autocorrelation "
               "shows whether neighbouring sūras have related lengths (memory) or are "
               "effectively independent.")
    order = st.radio("Order", ["Muṣḥaf (book)"] + (["Nuzūl (revelation)"] if HAS_REV else []),
                     horizontal=True, key="_sig_len_order")
    if order.startswith("Nuzūl"):
        seq_suras = sorted(range(1, 115), key=lambda s: NUZ.get(s, 999))
        xlab = "revelation order"
    else:
        seq_suras = list(range(1, 115))
        xlab = "sūra number (muṣḥaf)"
    series = [VERSES.get(s, 0) for s in seq_suras]

    fig = go.Figure(go.Scatter(x=list(range(1, 115)), y=series, mode="lines+markers",
                               line=dict(color=NAVY), marker=dict(size=4, color=AMBER),
                               text=[NAMEOF.get(s, "") for s in seq_suras],
                               hoverinfo="text+y"))
    fig.update_layout(height=320, plot_bgcolor="white", font=dict(size=14),
                      xaxis_title=xlab, yaxis_title="verses",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Sūra-length signal")
    st.plotly_chart(fig, width="stretch")

    max_lag = 20
    acf = autocorr(series, max_lag)
    fig = go.Figure(go.Bar(x=list(range(max_lag + 1)), y=acf, marker_color=TEAL))
    ci = 1.96 / math.sqrt(len(series))
    fig.add_hline(y=ci, line=dict(color=RED, dash="dash"))
    fig.add_hline(y=-ci, line=dict(color=RED, dash="dash"),
                  annotation_text="95% white-noise band")
    fig.update_layout(height=300, plot_bgcolor="white", font=dict(size=14),
                      xaxis_title="lag (sūras)", yaxis_title="autocorrelation",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Autocorrelation — bars outside the band = real memory")
    st.plotly_chart(fig, width="stretch")
    lag1 = acf[1]
    st.metric("Lag-1 autocorrelation", f"{lag1:+.3f}",
              "outside white-noise band" if abs(lag1) > ci else "within noise band")
    st.caption("A positive lag-1 means long sūras tend to sit next to long ones — "
               "consistent with the muqaṭṭaʿāt clustering the long sūras into runs.")


# ═══════════ TAB 2 — ROOT RECURRENCE ═══════════
with t_recur:
    layer(1, "Is a root bursty or evenly spread?")
    st.caption("Mark every āyah where a chosen root occurs as a 1, else 0. The gaps "
               "between 1s reveal whether the root clusters (bursty) or spreads "
               "regularly. We compare the dispersion to a Poisson (memoryless) null.")
    freqs = corpus.freq_norm
    top_roots = [r for r, _ in freqs.most_common(400)]
    root = st.selectbox("Root (normalized, top-400 by frequency)", top_roots,
                        key="_sig_root")
    idx = sorted(corpus.index_norm.get(root, []))
    n_ayah = len(corpus.df)
    if len(idx) < 3:
        st.info("Too few occurrences to analyze dispersion.")
    else:
        c1, c2, c3 = st.columns(3)
        c1.metric("Occurrences", len(idx))
        gaps = np.diff(idx)
        fano = gaps.var() / gaps.mean() if gaps.mean() else 0.0
        c2.metric("Fano factor (var/mean of gaps)", f"{fano:.2f}",
                  "bursty (>1)" if fano > 1.2 else "regular (<1)" if fano < 0.8 else "~Poisson")
        c3.metric("Mean gap (āyahs)", f"{gaps.mean():.1f}")

        raster = np.zeros(n_ayah)
        raster[idx] = 1
        fig = go.Figure(go.Scatter(x=idx, y=[1] * len(idx), mode="markers",
                                   marker=dict(size=4, color=PURPLE), hoverinfo="x"))
        fig.update_layout(height=180, plot_bgcolor="white", font=dict(size=13),
                          xaxis_title="āyah index (muṣḥaf)", yaxis=dict(visible=False),
                          margin=dict(l=10, r=10, t=30, b=10),
                          title=f"Occurrence raster of «{root}»")
        st.plotly_chart(fig, width="stretch")

        nd = st.select_slider("Permutations", [1000, 5000, 20000], value=5000,
                              key="_sig_recur_nd")
        if st.button("▶ Test dispersion vs Poisson null", type="primary",
                     key="_sig_recur_btn"):
            st.session_state["_sig_recur_run"] = (root, nd)
        run = st.session_state.get("_sig_recur_run")
        if run and run[0] == root:
            k = len(idx); rng = np.random.default_rng(5)
            out = np.empty(run[1])
            for j in range(run[1]):
                pick = np.sort(rng.choice(n_ayah, size=k, replace=False))
                g = np.diff(pick)
                out[j] = g.var() / g.mean() if g.mean() else 0.0
            p = (np.sum(out >= fano) + 1) / (run[1] + 1)
            st.metric("Burstiness p (vs random placement)", f"{p:.2g}",
                      "✓ more clustered than chance" if p < .05 else "n.s.")
            fig = go.Figure()
            fig.add_trace(go.Histogram(x=out, nbinsx=40, marker_color=ICE, name="null"))
            fig.add_vline(x=fano, line=dict(color=RED, width=3),
                          annotation_text=f"observed Fano={fano:.2f}",
                          annotation_position="top")
            fig.update_layout(height=300, plot_bgcolor="white", font=dict(size=14),
                              xaxis_title="Fano factor", yaxis_title="count",
                              showlegend=False, margin=dict(l=10, r=10, t=40, b=10),
                              title=f"Dispersion of «{root}» vs random placement → p ≈ {p:.2g}")
            st.plotly_chart(fig, width="stretch")


# ═══════════ TAB 3 — ENTROPY SPECTRUM ═══════════
with t_spec:
    layer(1, "Spectral analysis of the per-sūra entropy series")
    st.caption("Compute each sūra's letter-entropy, read the 114 values in order, and "
               "take the power spectrum (FFT). A spike at some frequency would mean a "
               "repeating cycle in how 'mixed' sūras are. We compare the peak to a "
               "phase-shuffled null that destroys ordering but keeps the values.")
    order2 = st.radio("Order", ["Muṣḥaf (book)"] + (["Nuzūl (revelation)"] if HAS_REV else []),
                      horizontal=True, key="_sig_spec_order")
    if order2.startswith("Nuzūl"):
        seq_suras = sorted(range(1, 115), key=lambda s: NUZ.get(s, 999))
    else:
        seq_suras = list(range(1, 115))
    H = np.array([shannon_bits(LETTERS[s].values()) for s in seq_suras])

    Hd = H - H.mean()
    power = np.abs(np.fft.rfft(Hd)) ** 2
    freqs_axis = np.fft.rfftfreq(len(Hd), d=1.0)
    fig = go.Figure(go.Scatter(x=freqs_axis[1:], y=power[1:], mode="lines",
                               line=dict(color=TEAL)))
    fig.update_layout(height=320, plot_bgcolor="white", font=dict(size=14),
                      xaxis_title="frequency (cycles per sūra)", yaxis_title="power",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Power spectrum of the letter-entropy signal")
    st.plotly_chart(fig, width="stretch")

    peak_power = float(power[1:].max())
    _peak_i = int(np.argmax(power[1:])) + 1
    _peak_freq = float(freqs_axis[_peak_i])
    # lowest two non-DC bins = slow drift across the reading order, not a true cycle
    _is_trend = _peak_i <= 2
    nd = st.select_slider("Permutations", [1000, 5000, 20000], value=5000,
                          key="_sig_spec_nd")
    if st.button("▶ Test spectral peak vs shuffled null", type="primary",
                 key="_sig_spec_btn"):
        st.session_state["_sig_spec_run"] = nd
    if st.session_state.get("_sig_spec_run"):
        rng = np.random.default_rng(7)
        nn = st.session_state["_sig_spec_run"]
        out = np.empty(nn)
        base = Hd.copy()
        for j in range(nn):
            rng.shuffle(base)
            out[j] = float((np.abs(np.fft.rfft(base)) ** 2)[1:].max())
        p = (np.sum(out >= peak_power) + 1) / (nn + 1)
        if p < .05:
            _verdict = ("✓ slow trend (low-frequency)" if _is_trend
                        else "✓ periodic cycle beyond chance")
        else:
            _verdict = "✗ no structure beyond chance"
        st.metric("Peak-power p (vs shuffled order)", f"{p:.2g}", _verdict)
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=out, nbinsx=40, marker_color=ICE, name="null"))
        fig.add_vline(x=peak_power, line=dict(color=RED, width=3),
                      annotation_text="observed peak", annotation_position="top")
        fig.update_layout(height=300, plot_bgcolor="white", font=dict(size=14),
                          xaxis_title="max spectral power", yaxis_title="count",
                          showlegend=False, margin=dict(l=10, r=10, t=40, b=10),
                          title=f"Spectral peak vs shuffled order → p ≈ {p:.2g}")
        st.plotly_chart(fig, width="stretch")
        if p < .05 and _is_trend:
            st.caption("The surviving peak sits at the lowest frequency — this is a slow "
                       "trend across the reading order, not a repeating cycle. The entropy "
                       "of sūras drifts gradually; there is no fixed-period carrier wave.")
        elif p < .05:
            st.caption("A mid-band peak survives the shuffle — a genuine repeating cycle "
                       "in how 'mixed' sūras are. Read the peak frequency to find its period.")
        else:
            st.caption("No peak beats the shuffled null — the entropy series behaves like "
                       "ordered noise, not a carrier wave.")


    st.divider()
    layer(2, "Wavelet multiresolution (Haar)")
    st.caption("The FFT asks 'which fixed cycle lengths'; a wavelet decomposition asks "
               "'how much variation lives at each SCALE' (2, 4, 8 … sūras). Pure Haar "
               "transform, no external library. A shuffle null flags any scale carrying "
               "more energy than chance.")

    def _haar_levels(x):
        x = np.asarray(x, dtype=float).copy()
        det = []
        while len(x) > 1:
            a = (x[0::2] + x[1::2]) / np.sqrt(2.0)
            d = (x[0::2] - x[1::2]) / np.sqrt(2.0)
            det.append(d); x = a
        return det

    def _level_energy(series):
        v = np.asarray(series, dtype=float) - np.mean(series)
        n2 = 1 << int(np.ceil(np.log2(len(v))))
        vp = np.zeros(n2); vp[:len(v)] = v
        return np.array([float(np.sum(d * d)) for d in _haar_levels(vp)])

    _en = _level_energy(H)
    _scales = [2 ** (k + 1) for k in range(len(_en))]
    wav_nd = st.select_slider("Permutations", [1000, 5000, 20000], value=5000,
                              key="_sig_wav_nd")
    if st.button("▶ Test scale energies vs shuffled null", type="primary",
                 key="_sig_wav_btn"):
        st.session_state["_sig_wav"] = wav_nd
    if st.session_state.get("_sig_wav"):
        _rng = np.random.default_rng(11); _nn = st.session_state["_sig_wav"]
        _base = np.asarray(H, dtype=float)
        _null = np.empty((_nn, len(_en)))
        for _j in range(_nn):
            _null[_j] = _level_energy(_rng.permutation(_base))
        _pv = [(np.sum(_null[:, k] >= _en[k]) + 1) / (_nn + 1) for k in range(len(_en))]
        _colors = [TEAL if pp < .05 else GREY for pp in _pv]
        _wfig = go.Figure(go.Bar(x=[str(sc) for sc in _scales], y=_en, marker_color=_colors,
                                 text=[f"p={pp:.2g}" for pp in _pv], textposition="outside"))
        _wfig.update_layout(height=340, plot_bgcolor="white", font=dict(size=13),
                            xaxis_title="scale (sūras per detail coefficient)",
                            yaxis_title="detail energy", margin=dict(l=10, r=10, t=30, b=10),
                            title="Haar wavelet energy by scale — green = beyond shuffle null")
        st.plotly_chart(_wfig, width="stretch")
        st.caption("Green bars carry significantly more energy than a shuffled series "
                   "at that scale (p on each bar); grey bars do not. Significant coarse "
                   "scales reflect a slow trend across the reading order; significant fine "
                   "scales would indicate local periodicity.")
    else:
        st.info("Press Run to compare each scale's energy to a shuffled-series null.")


    st.divider()
    layer(3, "Wavelet scalogram (Ricker CWT) — where the structure sits")
    st.caption("A continuous wavelet transform localizes variation in BOTH scale and "
               "position: the heatmap shows, for each scale (rows) and sūra (columns), "
               "how strongly the entropy series varies there. Pure-numpy Ricker wavelet.")
    if st.button("▶ Build the scalogram", type="primary", key="_sig_cwt_btn"):
        st.session_state["_sig_cwt"] = True
    if st.session_state.get("_sig_cwt"):
        def _ricker(points, a):
            t = np.arange(points) - (points - 1) / 2.0
            amp = 2.0 / (np.sqrt(3 * a) * np.pi ** 0.25)
            return amp * (1 - (t / a) ** 2) * np.exp(-(t ** 2) / (2 * a ** 2))
        _x = np.asarray(H, dtype=float) - float(np.mean(H))
        _scales = np.arange(1, 33)
        _cwt = np.zeros((len(_scales), len(_x)))
        for _i, _a in enumerate(_scales):
            _pts = min(int(10 * _a) + 1, len(_x))
            _cwt[_i] = np.convolve(_x, _ricker(_pts, _a), mode="same")
        _xlab = "sūra position (nuzūl)" if order2.startswith("Nuzūl") else "sūra position (muṣḥaf)"
        _cfig = go.Figure(go.Heatmap(z=np.abs(_cwt), x=list(range(1, len(_x) + 1)),
                                     y=[int(a) for a in _scales], colorscale="Viridis",
                                     colorbar=dict(title="|coef|")))
        _cfig.update_layout(height=420, font=dict(size=13), plot_bgcolor="white",
                            xaxis_title=_xlab, yaxis_title="scale (sūras)",
                            margin=dict(l=10, r=10, t=30, b=10),
                            title="Ricker-wavelet scalogram of the entropy series")
        st.plotly_chart(_cfig, width="stretch")
        st.caption("Broad bright bands at large scales spanning the x-axis = the slow "
                   "trend; an isolated bright spot would mark a localized burst of "
                   "variation at a particular place and scale.")


# ═══════════ TAB 4 — VERSE RHYTHM ═══════════
with t_rhythm:
    layer(1, "The rhythm of āyah lengths")
    st.caption("Each āyah has a token length. Their distribution and per-sūra "
               "variability describe the text's 'rhythm' — short staccato sūras vs "
               "long flowing ones.")
    arr = np.array(AYAH_LEN)
    c1, c2, c3 = st.columns(3)
    c1.metric("Median āyah length (tokens)", int(np.median(arr)))
    c2.metric("Mean", f"{arr.mean():.1f}")
    c3.metric("Coefficient of variation", f"{arr.std()/arr.mean():.2f}")
    fig = go.Figure(go.Histogram(x=arr, nbinsx=50, marker_color=NAVY))
    fig.update_layout(height=320, plot_bgcolor="white", font=dict(size=14),
                      xaxis_title="tokens per āyah", yaxis_title="count",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Distribution of āyah lengths across the whole corpus")
    st.plotly_chart(fig, width="stretch")

    su = corpus.df[COL_SURAH].astype(int).tolist()
    per_sura_mean = {}
    per_sura_vals = {}
    for i, s in enumerate(su):
        per_sura_vals.setdefault(s, []).append(AYAH_LEN[i])
    means = [np.mean(per_sura_vals[s]) for s in range(1, 115)]
    fig = go.Figure(go.Bar(x=list(range(1, 115)), y=means, marker_color=AMBER,
                           text=[NAMEOF.get(s, "") for s in range(1, 115)],
                           hoverinfo="text+y"))
    fig.update_layout(height=300, plot_bgcolor="white", font=dict(size=13),
                      xaxis_title="sūra number", yaxis_title="mean āyah length",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Mean āyah length per sūra")
    st.plotly_chart(fig, width="stretch")



# ═══════════ TAB 5 — CO-RECURRENCE (CROSS-CORRELATION) ═══════════
with t_xcorr:
    layer(1, "Do two roots co-occur with a directional lag?")
    st.caption("Mark each root's āyahs as a 1/0 signal, then cross-correlate the two. "
               "A peak at lag 0 means they share āyahs; a peak off zero means one tends "
               "to appear a few āyahs before/after the other. A circular-shift null — "
               "which preserves each signal's own clustering — tests the peak.")
    _xr = [r for r, _ in corpus.freq_norm.most_common(400)]
    _c1, _c2 = st.columns(2)
    a = _c1.selectbox("Root A", _xr, key="_sig_xa")
    b = _c2.selectbox("Root B", _xr, index=min(1, len(_xr) - 1), key="_sig_xb")
    n_ayah = len(corpus.df)
    asig = np.zeros(n_ayah); asig[sorted(corpus.index_norm.get(a, []))] = 1
    bsig = np.zeros(n_ayah); bsig[sorted(corpus.index_norm.get(b, []))] = 1
    if asig.sum() < 3 or bsig.sum() < 3:
        st.info("Need at least 3 occurrences of each root.")
    else:
        av = asig - asig.mean(); bv = bsig - bsig.mean()
        denom = np.sqrt((av * av).sum() * (bv * bv).sum()) or 1.0
        L = 15
        def _xc_vec(x, y):
            full = np.correlate(x, y, mode="full")
            cidx = len(x) - 1
            return full[cidx - L:cidx + L + 1]
        lags = list(range(-L, L + 1))
        xc = list(_xc_vec(av, bv) / denom)
        peak_i = int(np.argmax(np.abs(xc))); peak_lag = lags[peak_i]
        obs = max(abs(v) for v in xc)
        _fig = go.Figure(go.Bar(x=lags, y=xc, marker_color=TEAL))
        _fig.add_vline(x=0, line=dict(color=GREY, dash="dot"))
        _fig.update_layout(height=320, plot_bgcolor="white", font=dict(size=14),
                           xaxis_title="relative lag (āyahs)",
                           yaxis_title="normalized cross-correlation",
                           margin=dict(l=10, r=10, t=30, b=10),
                           title=f"Cross-correlation «{a}» × «{b}»")
        st.plotly_chart(_fig, width="stretch")
        _m1, _m2 = st.columns(2)
        _m1.metric("Peak lag (āyahs)", f"{peak_lag:+d}")
        _m2.metric("Peak correlation", f"{xc[peak_i]:+.3f}")
        _nd = st.select_slider("Permutations", [1000, 5000, 20000], value=5000,
                               key="_sig_xc_nd")
        if st.button("▶ Test the peak vs a circular-shift null", type="primary",
                     key="_sig_xc_btn"):
            st.session_state["_sig_xc"] = (a, b, _nd)
        _run = st.session_state.get("_sig_xc")
        if _run and _run[0] == a and _run[1] == b:
            rng = np.random.default_rng(3); _n = _run[2]
            out = np.empty(_n)
            for j in range(_n):
                sh = np.roll(bsig, int(rng.integers(1, n_ayah)))
                shv = sh - sh.mean()
                d2 = np.sqrt((av * av).sum() * (shv * shv).sum()) or 1.0
                out[j] = float(np.max(np.abs(_xc_vec(av, shv) / d2)))
            p_xc = (np.sum(out >= obs) + 1) / (_n + 1)
            st.metric("Peak |cross-correlation| p", f"{p_xc:.2g}",
                      "✓ beyond chance" if p_xc < .05 else "n.s.")
            _f2 = go.Figure()
            _f2.add_trace(go.Histogram(x=out, nbinsx=40, marker_color=ICE, name="null"))
            _f2.add_vline(x=obs, line=dict(color=RED, width=3),
                          annotation_text=f"observed |peak|={obs:.3f}",
                          annotation_position="top")
            _f2.update_layout(height=300, plot_bgcolor="white", font=dict(size=14),
                              xaxis_title="max |cross-correlation| under circular shift",
                              yaxis_title="count", showlegend=False,
                              margin=dict(l=10, r=10, t=40, b=10),
                              title=f"Peak vs circular-shift null → p ≈ {p_xc:.2g}")
            st.plotly_chart(_f2, width="stretch")
            st.caption("A significant peak means the two roots' āyah positions are "
                       "correlated beyond chance — usually shared themes or fixed "
                       "collocations, not a hidden code.")


# ═══════════════════ EXPORT THIS ANALYSIS ═══════════════════
st.divider()
st.markdown("### ⬇ Export this analysis")
import pandas as _pd
_sig_rows = []
for _s in range(1, 115):
    _sig_rows.append({
        "surah": _s, "name": NAMEOF.get(_s, ""),
        "verses": VERSES.get(_s, 0),
        "revelation_order": NUZ.get(_s, ""),
        "letter_entropy_bits": round(shannon_bits(LETTERS[_s].values()), 4),
    })
_sig_df = _pd.DataFrame(_sig_rows)
st.download_button("⬇ Per-sūra signal series (CSV)",
                   _sig_df.to_csv(index=False).encode("utf-8-sig"),
                   "signal_per_sura.csv", "text/csv", key="_sig_export_csv")
st.caption("Corpus-scoped export. Save any chart via its toolbar camera icon.")

st.caption("Computed live from the loaded corpus | permutation / Poisson nulls | "
           "exploratory scaffold, no 'scientific-miracle' claims. Part of the Two Books "
           "series alongside Disjoint Letters and Biology.")

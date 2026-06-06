"""Two Books · Global FDR — cross-domain multiple-testing summary.

Runs one representative permutation test per Two Books domain (Position ·
Sequence · Semantic · Signal · Biology) via the shared stats kernel, then applies
one Benjamini–Hochberg correction across all of them. Because every test comes
from twobooks_stats, this summary and the per-page tools cannot drift apart.
"""
from __future__ import annotations

import numpy as np
import plotly.graph_objects as go
import streamlit as st

from state import get_corpus, hero, layer, log_page
from twobooks_stats import two_books_battery, benjamini_hochberg

st.set_page_config(page_title="Two Books · FDR", page_icon="📋", layout="wide")
log_page("two_books_fdr")
corpus = get_corpus()

NAVY = "#1D3557"; TEAL = "#2A9D8F"; RED = "#E63946"; ICE = "#CADCFC"; GREY = "#9CA3AF"

hero("📋 Two Books · Global FDR",
     "One Benjamini–Hochberg correction across representative tests from every "
     "domain — Position · Sequence · Semantic · Signal · Biology.")

st.markdown(
    "<div style='background:#EEF3FB;border-left:5px solid #1D3557;border-radius:8px;"
    "padding:9px 14px;margin:6px 0 14px;font-size:13.5px;color:#1D3557;'>"
    "The Two Books section runs many permutation tests across its pages. Here they are "
    "computed together (one shared random draw) and corrected by Benjamini–Hochberg, so "
    "the section-wide false-discovery rate is visible at a glance. Every test uses the "
    "shared <code>twobooks_stats</code> kernel — the page tools and this summary cannot "
    "drift apart. FDR controls for multiplicity, <b>not</b> for the sūra-length confound "
    "flagged on the individual pages.</div>", unsafe_allow_html=True)

layer(1, "Run the cross-domain battery")
nd = st.select_slider("Permutations per test", [1000, 5000, 20000], value=5000,
                      key="_gf_nd")
if st.button("▶ Run the full Two Books battery + BH-FDR", type="primary", key="_gf_btn"):
    st.session_state["_gf"] = nd

if not st.session_state.get("_gf"):
    st.info("Press **Run** to compute every domain's representative test and correct "
            "them together.")
else:
    import pandas as pd
    res = two_books_battery(corpus, ndraw=st.session_state["_gf"])
    labels = list(res)
    ps = [res[k] for k in labels]
    qs = list(benjamini_hochberg(ps))
    surv = [q <= 0.05 for q in qs]
    st.dataframe(pd.DataFrame({
        "test": labels,
        "p (raw)": [f"{p:.2g}" for p in ps],
        "q (BH-FDR)": [f"{q:.2g}" for q in qs],
        "survives 5% FDR": ["✓" if s else "✗" for s in surv],
    }), hide_index=True, width="stretch")

    fig = go.Figure()
    fig.add_trace(go.Bar(y=labels, x=[-np.log10(max(p, 1e-6)) for p in ps],
                         orientation="h", name="−log₁₀ p (raw)", marker_color=ICE))
    fig.add_trace(go.Bar(y=labels, x=[-np.log10(max(q, 1e-6)) for q in qs],
                         orientation="h", name="−log₁₀ q (BH-FDR)", marker_color=TEAL))
    fig.add_vline(x=-np.log10(0.05), line=dict(color=RED, dash="dash"),
                  annotation_text="α = 0.05")
    fig.update_layout(height=460, barmode="group", plot_bgcolor="white", font=dict(size=12),
                      xaxis_title="−log₁₀ (higher = stronger)",
                      margin=dict(l=10, r=10, t=30, b=10),
                      title="Two Books — raw p vs BH-FDR q across all domains")
    st.plotly_chart(fig, width="stretch")
    st.metric("Discoveries surviving 5% FDR", f"{sum(surv)} / {len(surv)}")
    st.caption("Typically: contiguity (both orders) and the Signal/Biology structure tests "
               "survive; per-tag theme and per-tag length do NOT — the muqaṭṭaʿāt index "
               "position, not content. Any entropy 'special' that survives does so largely "
               "through the sūra-length confound (see each page's caption).")

st.caption("Computed live via the shared twobooks_stats kernel | Benjamini–Hochberg FDR | "
           "no fabricated data.")

"""Morphology — attached particles (col 6 segmentation) per input root."""
import streamlit as st

import plotly_charts as PC
from state import (get_corpus, query_controls, compute_all, need_results,
                   hero, layer, per_root_hint, log_page)

st.set_page_config(page_title="Morphology", page_icon="🧬", layout="wide")
log_page("morphology")
corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
from state import needs_recompute
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)
R = need_results()

hero("🧬 Morphology",
     "Prefix/suffix particles attached to each input root, learned from col 6.")
per_root_hint(compact=True)

morph = R["morphology"]

# ── LAYER 1 ──────────────────────────────────────────────────────
layer(1, "Morphology summary")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Input roots analysed", len(R["input_roots"]))
c2.metric("Unique particles found", morph["Particle"].nunique() if not morph.empty else 0)
c3.metric("Total prefix attachments",
          int(morph[morph["Position"] == "prefix"]["Count"].sum()) if not morph.empty else 0)
c4.metric("Total suffix attachments",
          int(morph[morph["Position"] == "suffix"]["Count"].sum()) if not morph.empty else 0)

# ── LAYER 2 — chart ──────────────────────────────────────────────
st.divider()
layer(2, "Particle distribution — all input roots")
st.plotly_chart(PC.chart_morphology(morph), width='stretch')

# ── LAYER 3 — per-root ───────────────────────────────────────────
st.divider()
layer(3, "Drill into one root")
if R["input_roots"]:
    pick = st.selectbox("Pick root", R["input_roots"], key="morph_pick")
    st.plotly_chart(PC.chart_morphology_per_root(morph, pick), width='stretch')
    sub = morph[morph["Input Root"] == pick]
    st.dataframe(sub, width='content', hide_index=True, height=320)

# ── LAYER 4 — full table ─────────────────────────────────────────
st.divider()
layer(4, "Full morphology table")
st.dataframe(morph, width='content', hide_index=True, height=400)
st.caption(
    "Particle attachments are detected by aligning surface forms (col 5) against "
    "tokens in the segmented column (col 6) and noting recognized prefix/suffix "
    "particles within ±2 tokens. The recognised set covers al-, wa, fa, bi, li, ka, "
    "sa, plus pronominal suffixes."
)

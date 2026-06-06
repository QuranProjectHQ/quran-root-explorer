"""Concept Deep-Dive — understand a concept using ALL the data.

A FIRST-CLASS endeavor distinct from Root Exploration (not a tab of it). Seeds a
concept and reads it across the whole corpus by MULTIMODAL FUSION: independent
modalities (semantic ∥ co-location ∥ spatial ∥ morphology ∥ sequence) kept
separate and SYNTHESISED into a six-type relation scheme
(consensus / semantic / co-location / spatial / orthogonal / divergent) — the
SAME fusion vocabulary as the Ayah deep-dive. Spatial is ONE modality, not the
headline.

Guiding principle: القرآن یفسر بعضه بعضا — the part is understood in light of the
whole, and the whole is more than the sum of its parts. Computational DESCRIPTION,
never tafsir. The heavy full report (docx + pdf) is produced by the background
worker `deep_dive.py concept <root>`, not on this page.
"""
from __future__ import annotations

import streamlit as st

import analysis as _A
import deep_dive as DD
import plotly_charts as PC
from state import get_corpus, query_controls, hero, layer, log_page

st.set_page_config(page_title="Concept Deep-Dive", page_icon="🔬", layout="wide")
log_page("concept_deep_dive")
corpus = get_corpus()
st.markdown("<style>section[data-testid='stMain'] [data-testid='stCaptionContainer'],"
            "section[data-testid='stMain'] [data-testid='stCaptionContainer'] *"
            "{color:#111111 !important;font-size:14px !important;}</style>",
            unsafe_allow_html=True)
raw, normalize, top_p, min_w, run = query_controls(corpus)
input_roots = _A.parse_input_roots(raw, normalize)

hero("🔬 Concept Deep-Dive", "understand a concept by multimodal fusion · القرآن یفسر بعضه بعضا")
st.caption("Distinct from Root Exploration: seed a concept, read it across the whole corpus "
           "through several independent lenses at once, and synthesise. "
           "Computational description, not tafsir.")

with st.expander("📐 Method — the three modalities & how this complements Motif analysis"):
    st.markdown(
        "A concept is read through **three INDEPENDENT modalities**, kept separate and "
        "synthesised (never blended — blending dilutes meaning):\n\n"
        "- **semantic** — distributional meaning (concepts used in similar contexts)\n"
        "- **co-location** — shared territory (deployed in the same surahs / regions)\n"
        "- **spatial** — distribution shape (often *null* — reported honestly, never the headline)\n\n"
        "Each related concept is typed by how the modalities **agree**: *consensus* (≥2 high), "
        "*semantic / co-location / spatial* (one high), *orthogonal* (one high, others "
        "independent), *divergent* (one high, another opposed = tension).\n\n"
        "**Where this fits vs 🔺 Motifs:** Motif analysis is the *within-verse* lens "
        "(do these roots share a verse? — directly verifiable, blind beyond the verse). "
        "This consensus lens is the *across-verse* complement (null-gated cross-modal "
        "agreement). Together they yield **latent motifs** — coherent themes the corpus "
        "weaves but never states in a single verse.")

with st.expander("📋 Or paste a word / phrase / ayah to find the concept"):
    _pst = st.text_area("Paste Arabic text — each word is mapped to its root",
                        height=80, key="concept_paste",
                        placeholder="فِي قُلُوبِهِم مَّرَضٌ")
    if _pst.strip():
        _cands = DD.match_pasted_concepts(corpus, _pst)
        if _cands:
            _pick = st.radio("Concepts found — pick one to deep-dive:",
                             [f"{r}  (×{n})" for r, n in _cands],
                             horizontal=True, key="concept_pick")
            input_roots = [_pick.split()[0]]      # override the sidebar query
        else:
            st.caption("No known concept found in that text.")

if not input_roots:
    st.info("Type a concept in the 🔎 Query box (sidebar), or paste text above, to begin.")
    st.stop()

target = input_roots[0]
if len(input_roots) > 1:
    st.caption(f"Analysing the first queried concept **{target}** (others ignored here).")


def _concept(target, normalize, unit):
    cache = st.session_state.setdefault("_concept_cache", {})
    key = (target, normalize, unit)
    if key in cache:
        return cache[key]
    bar = st.progress(0.0, text="Starting deep-dive…")
    try:
        res = DD.concept_deep_dive(target, unit=unit, normalize=normalize, corpus=corpus,
                                   progress=lambda f, m: bar.progress(min(f, 1.0), text=m))
    finally:
        bar.empty()
    cache[key] = res
    return res


if st.button(f"▶  Run deep-dive on  {target}", type="
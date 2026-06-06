"""Ayah-content Deep-Dive — explain an ayah in light of the whole corpus.

A FIRST-CLASS endeavor distinct from Root Exploration (not a tab of it). Decomposes
an ayah into its concepts, then surfaces the corpus's most relevant OTHER ayahs,
each TYPED by how it relates on three INDEPENDENT axes (lexical / semantic-
distributional / spatial-territory):
  direct · resonant · co-located · consensus · orthogonal · divergent.

Computational cross-references with evidence (axis z-scores + shared roots), NOT
tafsir. The heavy full report (docx + pdf) is produced by the background worker
`deep_dive.py ayah <s:a>`, not on this page.
"""
from __future__ import annotations

import streamlit as st

import analysis as _A
import deep_dive as DD
import plotly_charts as PC
from state import get_corpus, hero, log_page

st.set_page_config(page_title="Ayah Deep-Dive", page_icon="🔭", layout="wide")
log_page("ayah_deep_dive")
corpus = get_corpus()
st.markdown("<style>section[data-testid='stMain'] [data-testid='stCaptionContainer'],"
            "section[data-testid='stMain'] [data-testid='stCaptionContainer'] *"
            "{color:#111111 !important;font-size:14px !important;}</style>",
            unsafe_allow_html=True)


def _show_chips(items, n=8):
    items = [str(x) for x in items]
    if not items:
        st.markdown("<span style='font-size:20px;color:#0B1320'>—</span>",
                    unsafe_allow_html=True)
        return
    out = " ".join(
        "<span style='font-size:22px;color:#0B1320;background:#E8EEF6;border-radius:7px;"
        "padding:3px 14px;margin:4px 3px;display:inline-block;font-weight:600'>" + r + "</span>"
        for r in items[:n])
    if len(items) > n:
        out += f" <span style='font-size:14px;color:#444'>+{len(items) - n} more</span>"
    st.markdown(out, unsafe_allow_html=True)

hero("🔭 Ayah-content Deep-Dive", "explain an ayah in light of all relevant ayahs")
st.caption("Distinct from Root Exploration: decompose an ayah into its concepts, then surface "
           "the corpus's most relevant OTHER ayahs — TYPED by how they relate. "
           "Computational cross-references, not tafsir.")

with st.expander("📐 Method — the three axes & how this complements Motif analysis"):
    st.markdown(
        "Each candidate ayah is scored on **three INDEPENDENT axes**: **lexical** (shared "
        "roots), **semantic** (distributional closeness of meaning, even with NO shared "
        "words), **spatial** (shared territory). It is then typed: *consensus* (≥2 axes), "
        "*direct / resonant / co-located* (one), *orthogonal* (one, others independent), "
        "*divergent* (one high, another opposed).\n\n"
        "**Where this fits vs 🔺 Motifs:** Motif analysis is the *within-verse* lens "
        "(roots sharing a verse). This is the *across-verse* complement — it links ayahs "
        "by **resonance** (same meaning, different words) and **territory**, reaching the "
        "thematic/narrative ties co-occurrence cannot see (e.g. Yūsuf's grief ↔ his prison).")

@st.cache_data
def _surah_meta(_cid):
    df = corpus.df
    g = df.groupby(df[_A.COL_SURAH].astype(int))
    name = {int(s): str(sub[_A.COL_SURAH_NAME].iloc[0]) for s, sub in g}
    mx = {int(s): int(sub[_A.COL_AYAH].astype(int).max()) for s, sub in g}
    return name, mx


@st
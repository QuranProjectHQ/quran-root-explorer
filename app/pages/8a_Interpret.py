"""Reading guide — data-driven narrative for THIS session's results.

Every line is computed strictly from numbers in your input session.
No conjecture, no generalisation, no theological interpretation.
"""
from __future__ import annotations

import streamlit as st

from state import (get_corpus, query_controls, compute_all, need_results,
                   hero, layer, per_root_hint, log_page)
import interpret as I

st.set_page_config(page_title="Reading guide", page_icon="🧭", layout="wide")
log_page("interpret")

corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
from state import needs_recompute
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)
R = need_results()

hero("🧭 Reading guide",
     "Plain-English findings from your current session. Every line is a "
     "fact computed from your inputs — no conjecture, no generalisation.")
per_root_hint(compact=True)

st.info(
    "📌 **What this page is.** A summary of the actual numbers in your "
    "current analysis, written as sentences. Use it as a starting point — "
    "the per-page charts (Network, Motifs, Statistics) show the full detail."
)

sections = I.generate(R, corpus)

for section_title, facts in sections.items():
    if not facts:
        continue
    layer(0, section_title)
    for fact in facts:
        st.markdown(f"- {fact}")
    st.markdown("")

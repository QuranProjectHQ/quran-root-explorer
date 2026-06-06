"""Practical Lens — translation tips, teaching parallels, everyday implications.

This page sits on top of the computed analysis. It does NOT add new
calculations. It takes the existing findings — the pair classification
tier, the asymmetry ratio, the per-root profile — and offers concise
practical-application overlays.

Every overlay is opt-in (inside an expander), clearly labeled as
interpretive, and anchored to the numeric finding that triggered it.
The factual layer of the app (Reading Guide, Statistics, Network) is
untouched.
"""
from __future__ import annotations

from itertools import combinations

import pandas as pd
import streamlit as st

from state import (get_corpus, query_controls, compute_all,
                   hero, layer, log_page, needs_recompute)
from pair_classification import classify_lift
from practical_lens import (
    pair_lens, root_lens, asymmetry_lens, available_root_lenses,
    disclaimer_text,
)

st.set_page_config(page_title="Practical Lens", page_icon="🧰", layout="wide")
log_page("practical_lens")

corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)

hero("🧰 Practical Lens",
     "Translation tips · teaching parallels · everyday-life parallels for "
     "the patterns the data reveals.")

# ─── Persistent disclaimer ────────────────────────────────────────
st.warning(disclaimer_text())

R = st.session_state.get("results")
n_corpus = corpus.n_ayahs

if R is None or not R.get("input_roots"):
    st.info("Enter one or more roots in the top input bar — the practical "
            "lens activates as soon as the analysis runs.")
    st.stop()

roots = R["input_roots"]

# ─── Section 1 — pair lenses, one per pair ────────────────────────
if len(roots) >= 2:
    layer(1, "Practical lens for each pair  ·  based on pair classification")
    overlap = R.get("overlap")
    occ = R.get("occurrences")

    n_ayah_for = {}
    if occ is not None and "Input Root" in occ.columns:
        for r in roots:
            sub = occ[occ["Input Root"] == r]
            n_ayah_for[r] = sub[["Surah #", "Ayah #"]].drop_duplicates().shape[0]
    else:
        n_ayah_for = {r: 0 for r in roots}

    for a, b in combinations(roots, 2):
        joint = 0
        if overlap is not None and a in overlap.index and b in overlap.columns:
            try:
                joint = int(overlap.loc[a, b])
            except Exception:
                joint = 0
        nA = n_ayah_for.get(a, 0); nB = n_ayah_for.get(b, 0)
        lift = (joint / n_corpus) / ((nA / n_corpus) * (nB / n_corpus)) \
               if (nA and nB) else 0.0
        tier_id, tier_label, color, tier_desc = classify_lift(lift)
        lens = pair_lens(tier_id)

        with st.expander(
            f"**{a}  ↔  {b}**  ·  lift {lift:.2f}  ·  tier:  {tier_label}",
            expanded=False,
        ):
            st.markdown(
                f"**Computed fact** · joint ayahs: {joint} · ayahs A: {nA} · "
                f"ayahs B: {nB} · lift: {lift:.3f} · tier: **{tier_label}** "
                f"(threshold-based, no interpretation).")
            st.markdown(f"_{tier_desc}_")
            st.divider()
            st.markdown(lens.get("headline", "").replace("[b]","**").replace("[/b]","**"))

            tt = lens.get("translation_tips") or []
            tp = lens.get("teaching_parallels") or []
            ei = lens.get("everyday_implications") or []
            if tt:
                st.markdown("**Translation tips**")
                for t in tt: st.markdown(f"- {t}")
            if tp:
                st.markdown("**Teaching parallels**")
                for t in tp: st.markdown(f"- {t}")
            if ei:
                st.markdown("**Everyday-life parallels**")
                for t in ei: st.markdown(f"- {t}")

            # Asymmetry overlay if ratio is sharp
            asym = asymmetry_lens(nA, nB, a, b)
            if asym:
                st.divider()
                st.markdown(
                    f"### Asymmetry note\n"
                    + asym["headline"].replace("[b]","**").replace("[/b]","**")
                )
                for t in asym.get("translation_tips", []): st.markdown(f"- {t}")
                for t in asym.get("teaching_parallels", []): st.markdown(f"- {t}")
                for t in asym.get("everyday_implications", []): st.markdown(f"- {t}")

# ─── Section 2 — per-root practical lenses ────────────────────────
covered = available_root_lenses()
matching = [r for r in roots if r in covered]
if matching:
    st.divider()
    layer(1, "Per-root practical lens")
    for r in matching:
        L = root_lens(r)
        if L is None:
            continue
        with st.expander(L["headline"], expanded=False):
            st.markdown(f"_{L['rationale']}_")
            st.divider()
            for t in L["applied"]:
                st.markdown(f"- {t}")

# ─── Section 3 — about this page ─────────────────────────────────
st.divider()
with st.expander("About this page  ·  how the practical lens works",
                 expanded=False):
    st.markdown("""
This page does not add new computations.  It looks at the pair-classification
tier that the *Calibration* page already assigns from raw lift, and at the
ratio of ayah counts between input roots, and renders curated practical
overlays — translation, teaching, everyday parallels.

The overlays are short, tier-based, and triggered by structural features of
the data (e.g. "this pair has lift ≥ 10, so render as a bonded dyad in
English").  They do not invent claims that the data doesn't support.

For the strictly factual reading, use the **Reading Guide** page.  For
numeric detail, use **Statistics** or **Network**.
""")

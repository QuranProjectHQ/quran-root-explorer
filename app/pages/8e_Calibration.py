"""Calibration — benchmark your current pair against 12 reference pairs.

A pure-comparison page. Computes pairwise lift for each pair of input
roots, classifies each into one of four tiers using the threshold rules in
pair_classification.py, and shows them alongside 12 famous reference pairs
that were calibrated in earlier studies.

No theological or interpretive claim. Only the tier label that follows
mechanically from the lift threshold.
"""
from __future__ import annotations

from itertools import combinations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from state import (get_corpus, query_controls, compute_all, need_results,
                   hero, layer, log_page, needs_recompute)
import analysis as A
from pair_classification import (
    classify_lift, CALIBRATION_PAIRS, tier_legend,
)

st.set_page_config(page_title="Calibration", page_icon="📏", layout="wide")
log_page("calibration")

corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)

hero("📏 Calibration",
     "How does your pair compare to twelve famous Qurʾanic pairs?")

R = st.session_state.get("results")
n_corpus = corpus.n_ayahs

# ─── Tier legend ──────────────────────────────────────────────────
layer(1, "What the four tiers mean")
legend_df = pd.DataFrame(tier_legend())
st.dataframe(legend_df, hide_index=True, width='stretch')

st.caption(
    "Tiers are assigned purely from the lift value  ·  "
    "lift = P(A & B) ÷ [P(A) · P(B)]  ·  no theological claim, only what "
    "the numbers say about how often two roots share an ayah relative to chance."
)
st.divider()

# ─── Your pair(s) ─────────────────────────────────────────────────
layer(1, "Your current pair(s)")

user_rows: list[dict] = []
if R is None or len(R.get("input_roots", [])) < 2:
    st.info("Enter **two or more roots** in the top input bar to see how "
            "your pair compares to the reference set.")
else:
    roots = R["input_roots"]
    overlap = R.get("overlap")
    occ = R.get("occurrences")

    # individual ayah counts per input root
    n_ayah_for = {}
    if occ is not None and "Input Root" in occ.columns:
        for r in roots:
            sub = occ[occ["Input Root"] == r]
            n_ayah_for[r] = sub[["Surah #", "Ayah #"]].drop_duplicates().shape[0]
    else:
        for r in roots:
            n_ayah_for[r] = 0

    for a, b in combinations(roots, 2):
        joint = 0
        if overlap is not None and a in overlap.index and b in overlap.columns:
            try:
                joint = int(overlap.loc[a, b])
            except Exception:
                joint = 0
        nA = n_ayah_for.get(a, 0); nB = n_ayah_for.get(b, 0)
        if nA == 0 or nB == 0:
            lift = 0.0
        else:
            lift = (joint / n_corpus) / ((nA / n_corpus) * (nB / n_corpus))
        tier_id, tier_label, color, desc = classify_lift(lift)
        user_rows.append({
            "Pair": f"{a}  ↔  {b}",
            "ayahs A": nA,
            "ayahs B": nB,
            "joint": joint,
            "lift": round(lift, 3),
            "tier": tier_label,
            "interpretation": desc,
            "_color": color,
            "_label_x": a, "_label_y": b,
        })

    if user_rows:
        df_query = pd.DataFrame(user_rows).drop(columns=["_color","_label_x","_label_y"])
        st.dataframe(df_query, hide_index=True, width='stretch')

st.divider()

# ─── Reference 12 pairs ───────────────────────────────────────────
layer(1, "Twelve reference pairs  ·  from prior calibration study")
st.caption(
    "These twelve famous Qurʾanic dyads were computed on the same Book6.xlsx, "
    "with the same ayah-level co-occurrence rule.  Use them as a benchmark "
    "for what 'stipulative,' 'embedded,' 'mild,' and 'independent' look like in this corpus."
)
ref_rows = []
for label, a, b, nA, nB, j, lift, _saved_tier, desc in CALIBRATION_PAIRS:
    tier_id, tier_label, color, _ = classify_lift(lift)
    ref_rows.append({
        "Pair": label,
        "A": a, "B": b,
        "ayahs A": nA, "ayahs B": nB,
        "joint": j,
        "lift": lift,
        "tier": tier_label,
        "note": desc,
    })
ref_df = pd.DataFrame(ref_rows).sort_values("lift", ascending=False)
st.dataframe(ref_df, hide_index=True, width='stretch')

st.divider()

# ─── Lift-spectrum visual ─────────────────────────────────────────
layer(1, "Lift spectrum  ·  twelve reference pairs and your pair(s)")

fig = go.Figure()

# Reference pairs as colored dots
fig.add_trace(go.Scatter(
    x=[p[6] + 1e-3 for p in CALIBRATION_PAIRS],   # +epsilon for log-scale safety
    y=[p[0] for p in CALIBRATION_PAIRS],
    mode='markers+text',
    marker=dict(size=14,
                color=[classify_lift(p[6])[2] for p in CALIBRATION_PAIRS],
                line=dict(color='white', width=1)),
    text=[f"  {p[6]:.1f}" for p in CALIBRATION_PAIRS],
    textposition="middle right",
    name="reference pairs",
    hovertemplate="<b>%{y}</b><br>lift = %{x:.2f}<extra></extra>",
))

# User's pair(s) — highlighted stars
if user_rows:
    fig.add_trace(go.Scatter(
        x=[max(r["lift"], 1e-3) for r in user_rows],
        y=[r["Pair"] for r in user_rows],
        mode='markers+text',
        marker=dict(size=22, color=[r["_color"] for r in user_rows],
                    line=dict(color='black', width=2),
                    symbol='star'),
        text=[f"  {r['lift']:.2f}  ← your pair" for r in user_rows],
        textposition="middle right",
        name="your pair",
        hovertemplate="<b>%{y}</b><br>lift = %{x:.2f}<extra></extra>",
    ))

# Tier dividers
for thresh, color, name in [(10.0, "#7209B7", "stipulative ≥ 10"),
                              (2.0,  "#06AED5", "embedded ≥ 2"),
                              (1.0,  "#80B918", "mild ≥ 1")]:
    fig.add_vline(x=thresh, line_dash='dash', line_color=color,
                  annotation_text=name, annotation_position='top')

fig.update_layout(
    xaxis_title="lift  ·  log scale",
    xaxis_type="log",
    yaxis=dict(autorange='reversed'),
    height=600,
    showlegend=False,
    margin=dict(l=210, r=120, t=50, b=50),
)
st.plotly_chart(fig, width='stretch')

st.divider()

# ─── How to read this ─────────────────────────────────────────────
layer(1, "How to read this")
st.markdown("""
- **Stipulative pairs** (lift ≥ 10) — the Qurʾan treats them as a single
  concept in two words. Famous examples: *ʿusr / yusr* (with hardship is
  ease), *dunyā / ākhira* (this-world / hereafter), *rashad / ghayy*
  (guidance / error).
- **Embedded pairs** (lift 2 – 10) — frequent companions, but cross-cutting
  categories, not a single concept. Example: *īmān / kufr*.
- **Mild attraction** (lift 1 – 2) — above chance, but only just.
- **Independent / quarantined pairs** (lift ≤ 1) — different semantic
  neighborhoods. The corpus does not stage these as a binary. Example:
  *ẓulm / ʿadl* (lift 0.9), *silm / ṭaghā* (lift 0.0, zero joint ayahs).

In this corpus, the most common case is **embedded**. Stipulative pairs
are unusual and meaningful. Independent pairs are rarer still and very
meaningful — they tell you the corpus does not treat the two terms as a
straightforward binary.
""")

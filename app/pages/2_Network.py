# re-deploy 1779671310
"""Network analysis — graph-first scrolling page.
All visualizations are visible by scrolling (no hidden tabs).
TEMPORAL section is pinned near the top.
Every chart is wrapped in try/except so one failure can't blank the page."""
import pandas as pd
import streamlit as st

import plotly_charts as PC
import analysis as A
from state import (get_corpus, query_controls, compute_all, need_results,
                   hero, layer, per_root_hint, log_page)

st.set_page_config(page_title="Network", page_icon="🌐", layout="wide")
log_page("network")

# ── Interpretation guide + mobile landscape hint ─────────────────────
st.markdown('<div class="landscape-hint">📱 Tip: rotate your phone sideways (landscape) for a clearer network view.</div>', unsafe_allow_html=True)
with st.expander("📌 How to read this network (1-min)", expanded=False):
    st.markdown(
        "**An edge = these two roots share ayahs.** It does **not** say "
        "they mean the same thing. Two roots can share ayahs because they "
        "are paired contrastively (e.g. mercy vs. wrath), causally, or "
        "thematically — the network does not distinguish these.\n\n"
        "- **Node size / colour** = your input roots vs. partner roots\n"
        "- **Edge thickness** = number of shared ayahs\n"
        "- **Communities** (coloured groups) = roots that cluster together\n"
        "- **Bridges** = single edges that connect otherwise separate groups\n\n"
        "To see *how* two roots actually pair, open the **Ayah Browser** "
        "page and read the verses where they co-occur. The **🧭 Reading "
        "guide** page also lists data-driven facts about your session."
    )

corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
from state import needs_recompute
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)
R = need_results()
g = R["graph"]
ns = R["net_stats"]
has_rev = R.get("has_rev_order", False)


# ─────────────────────────────────────────────────────────────────
# VERSION BANNER — so the user can confirm they're on the latest build
# ─────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="background:linear-gradient(90deg,#E63946 0%,#F77F00 100%);
                color:white; padding:6px 14px; border-radius:8px;
                margin-bottom:6px; font-size:12px; font-weight:700;
                letter-spacing:0.4px;">
      Network v10
    </div>
    """,
    unsafe_allow_html=True,
)

hero("🌐 Root Co-occurrence Network",
     "16 network views — scroll to see all"
     + ("  ·  Revelation-order ✓" if has_rev else "  ·  ⚠️ no revelation-order column"))
per_root_hint(compact=True)


# Helper: safe plotly_chart that won't blank the rest of the page on failure
def safe_chart(fn, *args, **kwargs):
    try:
        fig = fn(*args, **kwargs)
        st.plotly_chart(fig, width='stretch')
    except Exception as e:
        st.error(f"⚠️ Chart `{fn.__name__}` failed: {type(e).__name__}: {e}")


# ─────────────────────────────────────────────────────────────────
# § 1 — NETWORK STATISTICS (always at top)
# ─────────────────────────────────────────────────────────────────
st.markdown("## 📊 Stats")
st.caption("Whole-graph metrics.")
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Nodes", ns["nodes"])
c2.metric("Edges", ns["edges"])
c3.metric("Density", ns["density"])
c4.metric("Modularity", ns["modularity"],
          help="0 = no community structure; >0.3 = clear communities")
c5.metric("Diameter", ns["diameter"])
c6.metric("k-core max", ns["k_core_max"])
c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Mean degree", ns["mean_degree"])
c2.metric("Mean path", ns["mean_shortest_path"])
c3.metric("Assortativity", ns["assortativity"])
c4.metric("Articulation pts", ns["n_articulation_points"])
c5.metric("Bridges", ns["n_bridges"])
c6.metric("Giant comp %", f"{ns['giant_component_pct']}%")

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 2 — TEMPORAL / PHASE ANALYSIS (pinned high — most novel content)
# ─────────────────────────────────────────────────────────────────
st.markdown("## 📜 Temporal")
if not has_rev:
    st.warning("This section needs the revelation-order column in book6. "
               "Without it the rest of the page still works in mushaf order.")
else:
    st.caption(
        "Networks built from phase-filtered ayahs."
    )

    # § 2a — Side-by-side Meccan vs Medinan networks
    st.markdown("### Meccan vs Medinan")
    gm, gd = R["g_meccan"], R["g_medinan"]
    cM1, cM2, cM3 = st.columns(3)
    cM1.metric("Meccan edges", gm.number_of_edges() if gm else 0)
    cM2.metric("Medinan edges", gd.number_of_edges() if gd else 0)
    cM3.metric("Shared edges", len(R["phase_in_both"]),
               help="Co-occurrences that appear in BOTH phases")
    safe_chart(PC.chart_phase_networks, gm, gd)

    # § 2b — 4-stage evolution
    st.markdown("### 4-stage evolution")
    st.caption(
        "Early / Middle / Late Meccan · Medinan."
    )
    def _build(lo, hi):
        return A.build_phase_subgraph(corpus, R["input_roots"], normalize,
                                       lo, hi,
                                       top_partners=top_p, min_weight=min_w)
    safe_chart(PC.chart_4stage_evolution, corpus, _build)

    # § 2c — Phase Diff
    st.markdown("### Phase diff")
    cP1, cP2, cP3 = st.columns(3)
    cP1.metric("⚫ Stable (both)", len(R["phase_in_both"]))
    cP2.metric("🟠 Meccan-only", len(R["phase_only_meccan"]))
    cP3.metric("🔵 Medinan-only", len(R["phase_only_medinan"]))
    safe_chart(PC.chart_phase_diff_graph, R["g_meccan"], R["g_medinan"],
                R["phase_only_meccan"], R["phase_only_medinan"],
                R["phase_in_both"])

    # § 2d — Sankey
    st.markdown("### Phase-flow Sankey")
    st.caption(
        "Meccan ayahs (left) → Medinan ayahs (right). Width = weight."
    )
    safe_chart(PC.chart_sankey_phase_flow, R["g_meccan"], R["g_medinan"])

    # § 2e — Per-pair Meccan/Medinan breakdown
    st.markdown("### Per-pair phase split")
    if not R["pair_phase"].empty:
        st.dataframe(R["pair_phase"], width='content',
                     hide_index=True, height=240)

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 3 — TOPOLOGY — three layouts of the SAME graph
# ─────────────────────────────────────────────────────────────────
st.markdown("## 🕸️ Topology")
st.caption(
    "Same graph, three layouts."
)

st.markdown("### Force-directed")
st.markdown(
    '<div style="background:linear-gradient(90deg,#FFF8E1,#FFFFFF);'
    'border-left:5px solid #E63946;padding:10px 14px;border-radius:8px;'
    'font-size:13.5px;line-height:1.55;color:#1B263B;margin:6px 0;">'
    '<b>Legend.</b> '
    '<span style="background:#E63946;color:#fff;padding:2px 8px;border-radius:8px;font-weight:700;">RED</span> = '
    'your input root(s). '
    '<span style="background:#F77F00;color:#fff;padding:2px 8px;border-radius:8px;font-weight:700;">ORANGE</span> / '
    '<span style="background:#06AED5;color:#fff;padding:2px 8px;border-radius:8px;font-weight:700;">BLUE</span> / '
    '<span style="background:#7209B7;color:#fff;padding:2px 8px;border-radius:8px;font-weight:700;">PURPLE</span> = '
    'distinct <b>Louvain communities</b> (each colour is one cluster of partner roots that travel together). '
    '<b>Node size</b> = weighted degree (more shared ayahs = larger). '
    '<b>Edge thickness</b> = how often the two roots appear together.'
    '</div>',
    unsafe_allow_html=True,
)
safe_chart(PC.chart_network, g, R["communities"])

st.markdown("### Chord")
st.caption("Nodes on a ring, edges as chords.")
safe_chart(PC.chart_chord_diagram, g, R["communities"])

st.markdown("### Adjacency matrix")
st.caption("Roots × roots, cell = ayahs shared.")
safe_chart(PC.chart_adjacency_matrix, g)

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 4 — LEAD-LAG — directed graph + arc diagram
# ─────────────────────────────────────────────────────────────────
st.markdown("## ➡️ Lead-Lag")
dg = R["dg_lead_lag"]
if dg.number_of_edges() == 0:
    st.info("No directional lead-lag relationships above threshold for current roots.")
else:
    st.markdown("### Directed graph")
    st.caption(
        "Arrow A→B means A leads B. Thickness = P(B near A)."
    )
    safe_chart(PC.chart_directed_lead_lag, dg)

    st.markdown("### Arc diagram")
    st.caption("Arcs above = forward; arcs below = reverse.")
    safe_chart(PC.chart_arc_diagram, dg)

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 5 — ROBUSTNESS — articulation, bridges, MST, k-core
# ─────────────────────────────────────────────────────────────────
st.markdown("## 🛡️ Robustness")

st.markdown("### Articulation + bridges")
st.caption(
    "★ = articulation point. Red edge = bridge. Zero of each = robust."
)
safe_chart(PC.chart_robustness_overlay, g, ns["articulation_points"],
            ns["bridge_edges"], R["communities"])
if ns["articulation_points"]:
    st.markdown("**Articulation points:** "
                + " · ".join(f"`{n}`" for n in ns["articulation_points"]))
if ns["bridge_edges"]:
    st.markdown("**Bridge edges:** "
                + " · ".join(f"`{u} — {v}`" for u, v in ns["bridge_edges"]))

st.markdown("### MST backbone")
st.caption("The network's spine.")
safe_chart(PC.chart_mst_backbone, g)

st.markdown("### k-core layers")
st.caption("Inner ring = dense core; outer = peripheral.")
safe_chart(PC.chart_kcore_layered, g)

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 6 — EGO NETWORKS — per-root mini graphs
# ─────────────────────────────────────────────────────────────────
st.markdown("## 🎯 Ego networks")
st.caption(
    "One mini-network per input root."
)
safe_chart(PC.chart_per_root_ego_gallery, g, R["input_roots"], max_neighbors=8)

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 7 — COMMUNITIES — gallery + hierarchy
# ─────────────────────────────────────────────────────────────────
st.markdown("## 🌐 Communities")

st.markdown("### Gallery")
st.caption("One mini-network per community.")
safe_chart(PC.chart_community_subnetworks, g, R["communities"], top_n=12)

st.markdown("### Hierarchy")
st.caption("Parent = community; children = its roots.")
safe_chart(PC.chart_community_dendrogram, g, R["communities"])

st.divider()


# ─────────────────────────────────────────────────────────────────
# § 8 — CENTRALITY & DETAIL TABLES
# ─────────────────────────────────────────────────────────────────
st.markdown("## 📈 Centrality & tables")
metric_pick = st.selectbox(
    "Rank by", ["Weighted Degree", "Degree", "Betweenness",
                "Eigenvector", "Clustering"], key="cent_metric")
safe_chart(PC.chart_centrality, R["centrality"], metric=metric_pick, top=20)

with st.expander("📊 Full centrality table", expanded=False):
    st.dataframe(R["centrality"], width='content',
                 hide_index=True, height=420)

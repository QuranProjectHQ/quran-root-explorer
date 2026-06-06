"""Help — tabbed layout.  Tab 1 = bird's-eye overview.  Tabs 2–6 = deep dives."""
import streamlit as st
from state import inject_css, hero, log_page

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import math


# ─── Case-study charts (real numbers, hard-coded for fast rendering) ──────

@st.cache_data(show_spinner=False)
def _cs_live():
    # Compute the case-study numbers LIVE from the default corpus so the worked
    # example never drifts from the data. Returns None if corpus is unavailable.
    try:
        import math, itertools
        import analysis as A
        from state import load, DEFAULT_XLSX
        if not DEFAULT_XLSX.exists():
            return None
        c = load(str(DEFAULT_XLSX))
        N = c.n_ayahs
        R = ["ظلم", "عدل", "رحم"]
        idx = {r: set(A.search_root(c, r, True)) for r in R}
        surof = {i: int(c.df.iloc[i][A.COL_SURAH]) for r in R for i in idx[r]}
        ayof = {i: int(c.df.iloc[i][A.COL_AYAH]) for r in R for i in idx[r]}
        sur = {r: {surof[i] for i in idx[r]} for r in R}
        freq = {r: {"ayahs": len(idx[r]), "surahs": len(sur[r])} for r in R}
        pairs = {}
        for a, b in itertools.combinations(R, 2):
            inter = idx[a] & idx[b]; uni = idx[a] | idx[b]
            pab = len(inter) / N; pa = len(idx[a]) / N; pb = len(idx[b]) / N
            pairs[(a, b)] = {
                "same_ayah": len(inter), "same_surah": len(sur[a] & sur[b]),
                "pmi": (math.log2(pab / (pa * pb)) if pab > 0 else float("nan")),
                "jaccard": (len(inter) / len(uni) if uni else 0.0),
                "p_b_a": (len(inter) / len(idx[a]) if idx[a] else 0.0),
                "p_a_b": (len(inter) / len(idx[b]) if idx[b] else 0.0),
            }
        size = {}
        su = c.df[A.COL_SURAH].astype(int).tolist(); ay = c.df[A.COL_AYAH].astype(int).tolist()
        for i in range(len(c.df)):
            size[su[i]] = max(size.get(su[i], 0), ay[i])
        touched = {}
        for r in R:
            for i in idx[r]:
                touched.setdefault(surof[i], set()).add(ayof[i])
        allsur = sur["ظلم"] & sur["عدل"] & sur["رحم"]
        dens = sorted([(s, size[s], len(touched[s]), 100 * len(touched[s]) / size[s])
                       for s in allsur], key=lambda x: -x[3])
        g = A.build_network(c, R, True, top_partners=15, min_weight=1)
        tc = A.triad_census(g)
        net = {"nodes": g.number_of_nodes(), "edges": g.number_of_edges(),
               "triangles": tc["triangles (closed triads)"]}
        nameof = {int(c.df[A.COL_SURAH].iat[i]): str(c.df[A.COL_SURAH_NAME].iat[i])
                  for i in range(len(c.df))}
        return {"N": N, "R": R, "freq": freq, "pairs": pairs, "dens": dens,
                "net": net, "nameof": nameof}
    except Exception:
        return None


def _cs_chart_length_norm(dens):
    top = dens[:5] if dens else []
    surahs = [f"S{s}" for s, _, _, _ in top]
    raw = [t for _, _, t, _ in top]
    den = [d for _, _, _, d in top]
    fig = make_subplots(rows=1, cols=2,
                        subplot_titles=["Ranked by RAW touched āyahs",
                                        "Ranked by DENSITY %"], horizontal_spacing=0.13)
    ri = sorted(range(len(top)), key=lambda i: -raw[i])
    di = sorted(range(len(top)), key=lambda i: -den[i])
    fig.add_trace(go.Bar(x=[surahs[i] for i in ri], y=[raw[i] for i in ri],
                         marker_color="#FCBF49"), 1, 1)
    fig.add_trace(go.Bar(x=[surahs[i] for i in di], y=[den[i] for i in di],
                         marker_color="#06AED5"), 1, 2)
    fig.update_yaxes(title_text="touched āyahs", row=1, col=1)
    fig.update_yaxes(title_text="density %", row=1, col=2)
    fig.update_layout(showlegend=False, height=380, paper_bgcolor="#FFFFFF",
                      plot_bgcolor="#F8FAFC", margin=dict(l=30, r=20, t=50, b=40),
                      title=dict(text="Same sūrahs, two rankings — raw vs length-normalized",
                                 x=0.5, xanchor="center", font=dict(size=14)))
    return fig


def _cs_chart_cross_reference(pairs):
    labels = [f"{a} ↔ {b}" for (a, b) in pairs]
    pmi = [pairs[k]["pmi"] for k in pairs]
    jac = [pairs[k]["jaccard"] for k in pairs]
    fig = go.Figure(go.Scatter(x=pmi, y=jac, mode="markers+text", text=labels,
                               textposition="top center",
                               marker=dict(size=22,
                                           color=["#06A77D" if v > 0 else "#E63946" for v in pmi],
                                           line=dict(width=2, color="#1B263B"))))
    fig.add_vline(x=0, line_dash="dot", line_color="gray")
    fig.update_xaxes(title="PMI (bits) — + = above chance")
    fig.update_yaxes(title="Jaccard")
    fig.update_layout(height=380, paper_bgcolor="#FFFFFF", plot_bgcolor="#F8FAFC",
                      margin=dict(l=40, r=20, t=50, b=50), showlegend=False,
                      title=dict(text="PMI × Jaccard — the three pairs", x=0.5,
                                 xanchor="center", font=dict(size=14)))
    return fig


def _cs_chart_motif_uniqueness():
    """3 disconnected dyads vs a closed triad — what motifs detect that
    pair-counts miss."""
    fig = make_subplots(rows=1, cols=2, subplot_titles=[
        '<b>❌ 3 disconnected pairs</b><br><span style="font-size:11px;color:#6B7280;">'
        '3 dyads · count of pair edges = 3 · NOT a motif</span>',
        '<b>✅ Closed triad (triangle)</b><br><span style="font-size:11px;color:#6B7280;">'
        '3 mutually connected nodes · IS a motif</span>'])

    # LEFT: 3 disconnected dyads — show 6 nodes (A-B), (C-D), (E-F)
    import math
    pos_left_nodes = [(-1.3, 0.8), (-0.5, 0.8), (-0.3, 0), (0.3, 0),
                      (-1.3, -0.8), (-0.5, -0.8)]
    pos_left_pairs = [(0,1), (2,3), (4,5)]
    labels_left = ['A','B','C','D','E','F']
    for u,v in pos_left_pairs:
        fig.add_trace(go.Scatter(
            x=[pos_left_nodes[u][0], pos_left_nodes[v][0]],
            y=[pos_left_nodes[u][1], pos_left_nodes[v][1]],
            mode='lines', line=dict(width=3, color='#9CA3AF'),
            hoverinfo='skip', showlegend=False), 1, 1)
    fig.add_trace(go.Scatter(
        x=[p[0] for p in pos_left_nodes], y=[p[1] for p in pos_left_nodes],
        mode='markers+text', text=labels_left, textposition='middle center',
        textfont=dict(size=14, color='white', family='Arial Black'),
        marker=dict(size=44, color='#1D3557',
                    line=dict(width=2, color='#1B263B')),
        hoverinfo='skip', showlegend=False), 1, 1)

    # RIGHT: closed triangle
    angles = [math.pi/2, math.pi/2 + 2*math.pi/3, math.pi/2 + 4*math.pi/3]
    pos_right = [(math.cos(a)*0.9, math.sin(a)*0.9) for a in angles]
    labels_right = ['A','B','C']
    # 3 edges
    for u, v in [(0,1),(1,2),(2,0)]:
        fig.add_trace(go.Scatter(
            x=[pos_right[u][0], pos_right[v][0]],
            y=[pos_right[u][1], pos_right[v][1]],
            mode='lines', line=dict(width=3, color='#E63946'),
            hoverinfo='skip', showlegend=False), 1, 2)
    fig.add_trace(go.Scatter(
        x=[p[0] for p in pos_right], y=[p[1] for p in pos_right],
        mode='markers+text', text=labels_right, textposition='middle center',
        textfont=dict(size=16, color='white', family='Arial Black'),
        marker=dict(size=52, color='#06A77D',
                    line=dict(width=3, color='#1B263B')),
        hoverinfo='skip', showlegend=False), 1, 2)
    fig.update_xaxes(visible=False, range=[-1.6, 1.6])
    fig.update_yaxes(visible=False, range=[-1.4, 1.4])
    fig.update_layout(
        title=dict(text='<b>WHAT A MOTIF IS  ·  the structural pattern pair-counts cannot detect</b>',
                   x=0.5, xanchor='center', font=dict(size=14)),
        height=380, paper_bgcolor='#FFFFFF', plot_bgcolor='#F8FAFC',
        margin=dict(l=20, r=20, t=80, b=20),
        font=dict(family="Arial, 'Segoe UI', sans-serif", color='#1B263B'),
        showlegend=False,
    )
    return fig



def _cs_chart_metric_progression(pairs):
    pv = pairs[("ظلم", "عدل")]
    metrics = ["Raw āyah overlap", "Raw sūrah overlap", "PMI (bits)", "Jaccard"]
    real = [str(pv["same_ayah"]), str(pv["same_surah"]),
            f"{pv['pmi']:+.2f}", f"{pv['jaccard']:.3f}"]
    colors = ["#E63946", "#06AED5", "#E63946" if pv["pmi"] < 0 else "#06A77D", "#9CA3AF"]
    fig = go.Figure(go.Bar(x=metrics, y=[1, 1, 1, 1], marker_color=colors,
                           text=[f"<b>{rv}</b>" for rv in real],
                           textposition="inside", insidetextanchor="middle"))
    fig.update_yaxes(visible=False)
    fig.update_layout(height=300, paper_bgcolor="#FFFFFF", plot_bgcolor="#F8FAFC",
                      margin=dict(l=20, r=20, t=50, b=40), showlegend=False,
                      title=dict(text="ظلم ↔ عدل — one pair, four metrics", x=0.5,
                                 xanchor="center", font=dict(size=14)))
    return fig

st.set_page_config(page_title="Help", page_icon="❓", layout="wide")
log_page("help")
inject_css()

# Top banner + "Back to app" button on every Help screen
top_l, top_r = st.columns([5, 1])
with top_l:
    st.markdown("""
    <div style="background:linear-gradient(135deg,#E63946 0%,#F77F00 100%);
                color:#FFFFFF; padding:16px 22px; border-radius:14px;
                box-shadow:0 6px 18px rgba(230,57,70,0.32); margin:0 0 12px 0;
                border:3px solid #FCBF49;">
      <div style="font-size:21px; font-weight:900; letter-spacing:0.5px;">
        🎯 BRAND NEW HERE?  PICK A TAB BELOW IN ORDER.
      </div>
      <div style="font-size:14px; line-height:1.55; margin-top:5px; color:#FFF8E1;">
        <b>📋 Overview</b> (where am I?) → <b>🧩 Concepts</b> (why it works) →
        <b>🔤 Glossary</b> (what each word means) → <b>📊 How to read each chart</b> →
        <b>🗺️ Page tour</b> → <b>🆘 Troubleshooting</b>.  Five minutes total.
      </div>
    </div>
    """, unsafe_allow_html=True)
with top_r:
    if st.button("🏠 Back to app", key="help_back_app",
                 width='stretch', type="primary",
                 help="Return to the home page"):
        st.switch_page("app.py")

# Shared styling
st.markdown("""
<style>
.help-section{ background:#1D3557; color:white; padding:9px 16px; border-radius:10px;
   font-size:15px; font-weight:800; letter-spacing:0.5px; margin:18px 0 8px 0; }
.help-card{ border:1px solid #E5E7EB; border-radius:10px; padding:11px 16px;
   margin:6px 0; background:#FFFFFF; box-shadow:0 1px 4px rgba(0,0,0,0.05); }
.help-card h4{ margin:0 0 3px 0; color:#E63946; font-size:16px; font-weight:800; }
.help-card .what{ font-size:13.5px; color:#1D3557; }
.help-card .how{ font-size:13px; color:#374151; margin-top:6px;
   background:#FFF8E1; padding:6px 10px; border-radius:6px; border-left:4px solid #FCBF49; }
.glossary-row{ display:grid; grid-template-columns:170px 1fr; gap:10px; padding:9px 12px;
   border-bottom:1px solid #E5E7EB; }
.glossary-row .term{ font-weight:800; color:#7209B7; font-size:14.5px; }
.glossary-row .defn{ font-size:13.5px; color:#1B263B; line-height:1.55; }
.glossary-row .defn b{ color:#E63946; }
.help-analogy{ background:#FFFEF7; border-left:6px solid #FCBF49; border-radius:8px;
   padding:10px 16px; margin:8px 0; font-size:14px; line-height:1.6; color:#1B263B; }
.help-analogy b{ color:#E63946; }
.concept-card{ background:#FFFFFF; border:2px solid #FCBF49; border-radius:10px;
   padding:12px 16px; margin:10px 0; box-shadow:0 2px 8px rgba(252,191,73,0.18); }
.concept-card h4{ color:#7209B7; font-size:17px; font-weight:800;
   margin:0 0 6px 0; }
.concept-card .why{ font-size:14px; color:#1B263B; line-height:1.6; }
.concept-card .why b{ color:#E63946; }
.concept-card .ana{ background:#FFF8E1; border-left:4px solid #E63946;
   padding:8px 12px; margin-top:8px; font-size:13.5px; color:#1D3557; }
.tab-back{ background:#06AED5; color:#fff; padding:6px 14px; border-radius:8px;
   font-size:13px; font-weight:700; display:inline-block; margin:10px 0;
   text-decoration:none !important; }
</style>
""", unsafe_allow_html=True)

# =====================================================================
TABS = st.tabs([
    "📋 Overview",
    "🧩 Concepts",
    "🔤 Glossary",
    "📊 How to read each chart",
    "🗺️ Page tour",
    "📖 Case study",
    "🧭 Two Books",
    "🆘 Troubleshooting",
])

# =====================================================================
# TAB 1 — OVERVIEW (bird's-eye landing — pick a section)
# =====================================================================
with TABS[0]:
    st.markdown('<div class="help-section">📋 OVERVIEW — pick where to go</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div class="help-analogy">
      <b>What this app is:</b> a tool that takes a few Arabic roots you care about
      (e.g. <i>ظلم · عدل · رحم</i>), reads all 6,236 ayahs of the Quran, and reports
      <b>who hangs out with whom</b> — which roots co-occur, in which surahs, how
      strongly, and in what combinations.
    </div>
    """, unsafe_allow_html=True)

    # ─── card-button grid for the OTHER Help tabs ───
    st.markdown("""
    <style>
    .ov-grid{
        display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));
        gap:14px; margin:14px 0;
    }
    .ov-card{
        border-radius:14px; padding:18px 16px;
        box-shadow:0 4px 12px rgba(0,0,0,0.10);
        color:#FFFFFF;
        display:flex; flex-direction:column; justify-content:space-between;
        min-height:155px;
        border:none;
        transition:transform .12s ease, box-shadow .12s ease;
    }
    .ov-card:hover{
        transform:translateY(-2px);
        box-shadow:0 8px 22px rgba(0,0,0,0.20);
    }
    .ov-icon{ font-size:36px; line-height:1; }
    .ov-title{ font-size:18px; font-weight:900; margin-top:6px; letter-spacing:0.3px; }
    .ov-sub  { font-size:13px; opacity:0.95; margin-top:6px; line-height:1.45; }
    .ov-cta  { font-size:11px; font-weight:700; opacity:0.85; margin-top:10px;
               background:rgba(255,255,255,0.18); padding:3px 8px; border-radius:6px;
               display:inline-block; }

    .ov-c1{ background:linear-gradient(135deg,#7209B7 0%,#06AED5 100%); }
    .ov-c2{ background:linear-gradient(135deg,#06AED5 0%,#06A77D 100%); }
    .ov-c3{ background:linear-gradient(135deg,#06A77D 0%,#FCBF49 100%); color:#1B263B; }
    .ov-c4{ background:linear-gradient(135deg,#F77F00 0%,#FCBF49 100%); color:#1B263B; }
    .ov-c-case{ background:linear-gradient(135deg,#1D3557 0%,#7209B7 100%); }
    .ov-c5{ background:linear-gradient(135deg,#E63946 0%,#F77F00 100%); }
    .ov-c3 .ov-cta, .ov-c4 .ov-cta { background:rgba(0,0,0,0.10); color:#1B263B; }

    .ov-section-title{
        font-size:14px; font-weight:800; color:#1D3557;
        background:#F0F4F8; padding:6px 12px; border-radius:8px;
        border-left:4px solid #E63946;
        margin:20px 0 8px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="ov-section-title">📚  HELP SECTIONS — read in order</div>',
                unsafe_allow_html=True)
    st.markdown("""
    <div class="ov-grid">
      <div class="ov-card ov-c1">
        <div>
          <div class="ov-icon">🧩</div>
          <div class="ov-title">Concepts</div>
          <div class="ov-sub">Plain-English foundations: why co-occurrence, networks, PMI, motifs, communities work.  Ten ideas with analogies.</div>
        </div>
        <div class="ov-cta">↑ click "🧩 Concepts" tab above</div>
      </div>
      <div class="ov-card ov-c2">
        <div>
          <div class="ov-icon">🔤</div>
          <div class="ov-title">Glossary</div>
          <div class="ov-sub">Plain-English definitions of every term used in the app.  23 entries — Root · Ayah · Surah · Edge · Weight · PMI · Jaccard …</div>
        </div>
        <div class="ov-cta">↑ click "🔤 Glossary" tab above</div>
      </div>
      <div class="ov-card ov-c3">
        <div>
          <div class="ov-icon">📊</div>
          <div class="ov-title">How to read each chart</div>
          <div class="ov-sub">Every chart type in the app, with a step-by-step reading rule for each.</div>
        </div>
        <div class="ov-cta">↑ click "📊 How to read…" tab above</div>
      </div>
      <div class="ov-card ov-c4">
        <div>
          <div class="ov-icon">🗺️</div>
          <div class="ov-title">Page tour</div>
          <div class="ov-sub">What every page of the app does, and when to use it.  13 pages explained briefly.</div>
        </div>
        <div class="ov-cta">↑ click "🗺️ Page tour" tab above</div>
      </div>
      <div class="ov-card ov-c-case">
        <div>
          <div class="ov-icon">📖</div>
          <div class="ov-title">Case study</div>
          <div class="ov-sub">A worked example with REAL roots (ظلم · عدل · رحم) and REAL numbers from the corpus.  Watch every module add one piece of insight; methodology defended.</div>
        </div>
        <div class="ov-cta">↑ click "📖 Case study" tab above</div>
      </div>
      <div class="ov-card ov-c1">
        <div>
          <div class="ov-icon">🧭</div>
          <div class="ov-title">Two Books</div>
          <div class="ov-sub">How to use the new Disjoint Letters · Signal · Biology · Spatial Patterns · FDR pages, and how to read permutation p-values, BH-FDR, the length confound, and the scalogram.</div>
        </div>
        <div class="ov-cta">↑ click "🧭 Two Books" tab above</div>
      </div>
      <div class="ov-card ov-c5">
        <div>
          <div class="ov-icon">🆘</div>
          <div class="ov-title">Troubleshooting</div>
          <div class="ov-sub">Common errors and their fixes.  Open this only when something is broken.</div>
        </div>
        <div class="ov-cta">↑ click "🆘 Troubleshooting" tab above</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ─── functional jumps back into the app ───
    st.markdown('<div class="ov-section-title">🚀  OR JUMP STRAIGHT INTO THE APP</div>',
                unsafe_allow_html=True)
    jc1, jc2, jc3, jc4 = st.columns(4)
    with jc1:
        if st.button("🏠\n\nHome", key="ov_jump_home",
                     width='stretch', type="primary"):
            st.switch_page("app.py")
    with jc2:
        if st.button("🔍\n\nPer Root Profile", key="ov_jump_perroot",
                     width='stretch', type="primary"):
            st.switch_page("pages/1_Per_Root_Profile.py")
    with jc3:
        if st.button("🌐\n\nNetwork", key="ov_jump_network",
                     width='stretch', type="primary"):
            st.switch_page("pages/2_Network.py")
    with jc4:
        if st.button("📈\n\nStatistics", key="ov_jump_stats",
                     width='stretch', type="primary"):
            st.switch_page("pages/7_Statistics.py")


# =====================================================================
# TAB 2 — CONCEPTS (methodology foundations)
# =====================================================================
with TABS[1]:
    st.markdown('<div class="help-section">🧩 CONCEPTUAL FOUNDATIONS — why this methodology works</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="help-analogy">
      Every method below answers a different question about Arabic roots.
      Read them top-to-bottom; each one builds on the last.
    </div>
    """, unsafe_allow_html=True)

    concepts = [
        ("1️⃣ Co-occurrence — the foundation",
         "The whole app rests on a single simple idea: <b>roots that appear in the same "
         "ayah probably belong to the same idea</b>.  When ظلم (oppression) and عدل "
         "(justice) keep showing up in the same verses, they are clearly part of one "
         "moral conversation — even if we know nothing else about either word.",
         "Like noticing that two friends always show up at the same parties.  You "
         "don't need to know what they talk about to conclude they're connected."),
        ("2️⃣ Networks — co-occurrence at scale",
         "When you have many roots and many co-occurrences, you have a <b>web</b>.  "
         "Drawing roots as dots and co-occurrences as lines turns thousands of "
         "individual facts into one picture you can scan in seconds.  Thick lines = "
         "frequent partners.  Clusters = themes.  Isolated dots = outliers.",
         "Like the constellation pictures astronomers draw — individual stars become "
         "shapes when you connect the dots."),
        ("3️⃣ Why bare counts aren't enough — PMI",
         "<b>PMI = Pointwise Mutual Information</b>, a number-theory tool from "
         "information theory (Church &amp; Hanks, 1989).  It asks: do two roots "
         "co-occur <i>more often than you'd expect by chance</i>?  "
         "<br><br><b>Formula:</b> "
         "<code>PMI(A, B) = log₂( P(A and B) / ( P(A) × P(B) ) )</code>"
         "<br>"
         "<b>Worked example</b> (ayahs N=6,236, A=ظلم in 290, B=عدل in 24, "
         "both in 1):  "
         "<br>• P(A) = 290/6236 = 0.0465  "
         "<br>• P(B) = 24/6236 = 0.00385  "
         "<br>• P(A∩B) = 1/6236 = 0.000160  "
         "<br>• PMI = log₂( 0.000160 / (0.0465 × 0.00385) ) = log₂(0.894) = "
         "<b>−0.16 bits</b>  → slightly weaker than chance.  "
         "<br><br>+ = real association.  0 = chance.  − = they avoid each other.  "
         "<br><b>More:</b> <a href='https://en.wikipedia.org/wiki/Pointwise_mutual_information'>"
         "Wikipedia &middot; PMI</a>",
         "Two celebrities photographed together at one event is a coincidence; "
         "photographed together at 50 events out of 100 each attends is news."),
        ("4️⃣ Why size matters — Jaccard",
         "The <b>Jaccard similarity coefficient</b> (Paul Jaccard, 1901) compares "
         "two sets directly, regardless of how big each is.  "
         "<br><br><b>Formula:</b> "
         "<code>J(A, B) = |A ∩ B| / |A ∪ B|</code>"
         "<br>"
         "<b>Worked example</b> (ظلم: 290 ayahs, رحم: 313 ayahs, both: 17):  "
         "<br>• A ∩ B = 17  "
         "<br>• A ∪ B = 290 + 313 − 17 = 586  "
         "<br>• Jaccard = 17 / 586 = <b>0.029</b>  (small, but non-trivial for "
         "two top-1% roots).  "
         "<br><br>Range: 0 (never together) → 1 (always together).  "
         "<br><b>More:</b> <a href='https://en.wikipedia.org/wiki/Jaccard_index'>"
         "Wikipedia &middot; Jaccard index</a>",
         "Like the overlap between two friends' phone-contact lists, divided by the "
         "total unique contacts in both lists combined."),
        ("5️⃣ Direction matters — Conditional probability P(B|A)",
         "<b>Conditional probability</b> is a foundational concept of probability "
         "theory (Kolmogorov, 1933).  It reads: <i>given that A occurred, what's "
         "the probability B also occurred?</i>  "
         "<br><br><b>Formula:</b> "
         "<code>P(B|A) = |A ∩ B| / |A|</code>"
         "<br>"
         "<b>Worked example</b>:  "
         "<br>• P(رحم | ظلم) = 17 / 290 = <b>0.059</b>  (in 5.9% of ظلم-ayahs, رحم also appears)  "
         "<br>• P(ظلم | رحم) = 17 / 313 = <b>0.054</b>  (almost symmetric — both common)  "
         "<br>• P(عدل | ظلم) = 1 / 290 = <b>0.003</b>  (tiny — but عدل is rare)  "
         "<br>• P(ظلم | عدل) = 1 / 24 = <b>0.042</b>  (much bigger — knowing عدل is there gives 14× more evidence)  "
         "<br><br>The asymmetry shows: <i>direction matters</i>.  "
         "<br><b>More:</b> <a href='https://en.wikipedia.org/wiki/Conditional_probability'>"
         "Wikipedia &middot; Conditional probability</a>",
         "If you know it's raining, the ground is wet 95% of the time.  If you know "
         "the ground is wet, it's raining only sometimes — could be a sprinkler."),
        ("6️⃣ Motifs — closed shapes hide stable meaning",
         "A <b>triad</b> is three roots all mutually connected.  A <b>quad</b> is four.  "
         "A <b>pentad</b> is five.  These closed cliques are not random — they tend to "
         "encode <i>stable semantic packages</i>: a theme that the Quran returns to "
         "again and again as a unit.",
         "In friendships, a stable triangle is rarely accidental — three people who "
         "all know each other usually share a context (school, work, family)."),
        ("7️⃣ Communities — clusters reveal themes (Louvain method)",
         "The <b>Louvain method</b> (Blondel, Guillaume, Lambiotte, Lefebvre, 2008, "
         "Univ. catholique de Louvain) is the standard community-detection algorithm "
         "for graphs.  It maximises a quantity called <b>modularity</b> "
         "(how much denser edges are within groups than across).  "
         "<br><br>It groups roots that connect <i>more densely to each "
         "other than to outsiders</i>.  Each community is, in effect, an automatically-"
         "detected theme.  No human labeled them — the math found them.",
         "Like sociologists detecting cliques in a high school by who texts whom "
         "the most, without ever interviewing anyone."),
        ("8️⃣ Dispersion — concentrated or spread?",
         "<b>Juilland D</b> and entropy answer: is this root <i>everywhere</i> in the "
         "Quran, or <i>concentrated in a few surahs</i>?  Concentrated = the root has "
         "a specific home.  Spread = it's a general-purpose word.",
         "Like the difference between the word <i>quantum</i> (concentrated in physics "
         "books) and the word <i>book</i> (everywhere)."),
        ("9️⃣ Importance per surah — TF-IDF",
         "TF-IDF rewards surahs where a root is over-represented relative to the "
         "rest of the corpus.  A high TF-IDF means the root genuinely <i>belongs</i> "
         "to that surah, not just appears there because the surah is long.",
         "Like asking: which professor uses the word <i>thermodynamics</i> in their "
         "lectures most often <i>relative to everyone else</i>?  Not just whoever lectures most."),
        ("🔟 Putting it together",
         "The home page shows headline counts.  The Network page draws the web.  The "
         "Motifs page extracts the closed cliques.  The Statistics page applies every "
         "metric above to your query and asks <i>do they all agree</i>?  When PMI, "
         "Jaccard, and conditional probability all point the same direction — that's "
         "a robust pattern, not a fluke.",
         "Like a court case where motive, opportunity, and physical evidence all "
         "agree.  One source could be wrong; three independent sources agreeing is hard to ignore."),
        ("1️⃣1️⃣ Two Books — reading the corpus at three scales",
         "The <b>Two Books</b> section reads the same validated corpus three ways, by "
         "<b>scale</b>.  <b>🧭 Position</b> asks where sūras sit (the muqaṭṭaʿāt as a "
         "positional <i>pointer</i> indexing contiguous families — validated at "
         "p≈2×10⁻⁵, NOT a hidden code).  <b>🔤 Sequence</b> works at the character "
         "level (letters≈bases): alphabet usage, letter density, letter entropy.  "
         "<b>🧩 Semantic</b> works at the word/root level (roots≈codons, "
         "words≈proteins): custom-family tests, root entropy, lexical richness.  Every "
         "claim is checked against a <b>permutation null</b>, and length-confounds are "
         "disclosed — most 'special' looking numbers are just length effects.",
         "Like studying a book three ways: where each chapter sits on the shelf "
         "(Position), the letters that spell the words (Sequence), and what the words "
         "mean (Semantic).  Same book, three lenses."),
    ]
    for title, why, analogy in concepts:
        st.markdown(
            f"<div class='concept-card'><h4>{title}</h4>"
            f"<div class='why'>{why}</div>"
            f"<div class='ana'>🌐 <b>Analogy:</b> {analogy}</div></div>",
            unsafe_allow_html=True,
        )

    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 3 — GLOSSARY
# =====================================================================
with TABS[2]:
    st.markdown('<div class="help-section">🔤 GLOSSARY — plain English + analogies</div>',
                unsafe_allow_html=True)
    terms = [
        ("Root", "A 3- or 4-letter Arabic stem (e.g. رحم).  <b>Analogy:</b> the verb “to run” is a root — "
                 "“runner”, “running”, “ran” are its surface forms."),
        ("Surface form", "How a root appears in a specific verse — with prefixes/suffixes."),
        ("Ayah", "A single verse (≈6,236 total)."),
        ("Surah", "A chapter (114 total)."),
        ("Co-occurrence", "Two roots in the same ayah (or same surah).  <b>Analogy:</b> two people in the same photo."),
        ("Network / Graph", "Dots + lines.  Dots = roots, lines = co-occurrences."),
        ("Node", "One dot — one root."),
        ("Edge", "One line — one pair sharing ayahs.  Its weight is the count."),
        ("Weight", "Number of ayahs two roots share."),
        ("Weighted degree", "Sum of all of a root's edge weights — how 'central' it is."),
        ("Community", "A cluster more tightly connected internally than externally — an automatic theme."),
        ("Motif", "A small closed shape — Dyad / Triad / Quad / Pentad.  The <b>within-verse</b> lens: roots that share a verse (directly verifiable, blind beyond the verse).  Lives on the 🔺 <b>Motifs</b> page."),
        ("Clique", "Same as motif — every pair connected."),
        ("Consensus bond", "<b>Across-verse</b> complement to a motif (🔬 Deep Dives).  Two concepts bonded across ≥2 of three INDEPENDENT modalities — <b>meaning · territory · distribution</b>.  Beyond chance (z ≈ +27 vs an alignment null)."),
        ("Multimodal fusion", "Reading a concept/ayah through the three modalities at once and synthesising their <b>agreement vs divergence</b> — kept separate, never blended (blending dilutes meaning)."),
        ("Latent motif", "A consensus triad whose three concepts <b>never share a verse</b> — a theme the corpus weaves but never states together (e.g. لوط·ضيق·صيح).  Invisible to Motif analysis; surfaced only by fusing consensus with the co-occurrence split, then FDR-gated."),
        ("PMI", "Above-chance association in bits.  + = associated, − = avoidant."),
        ("Jaccard", "Shared ÷ union (0 → 1).  Size-corrected similarity."),
        ("P(B|A)", "Given A appears, probability B also appears.  Asymmetric."),
        ("TF-IDF", "Highlights surahs where a root is over-represented."),
        ("Centrality", "Importance in the network — multiple flavors (degree, betweenness, eigenvector)."),
        ("PageRank", "Google's importance algorithm, applied to roots."),
        ("k-core", "Density measure — high k = root sits deep in a tightly-knit group."),
        ("LAYER 1 / 2 / 3 / 4", "Page sections from bird's-eye → fine detail."),
        ("Normalize / Tolerant", "Folds Persian ک / ی to Arabic ك / ي and similar variants."),
        ("Density", "Edges actually present ÷ edges that could exist."),
        ("Louvain method", "<b>Community-detection algorithm</b> (Blondel et al., 2008, Université catholique de Louvain).  Groups nodes that connect more densely internally than externally.  Maximises modularity.  <a href='https://en.wikipedia.org/wiki/Louvain_method'>Wikipedia</a>."),
        ("TF-IDF", "<b>Term Frequency × Inverse Document Frequency</b>.  A numerical statistic from information retrieval (Spärck Jones, 1972) that measures how important a word is in a document relative to a whole corpus.  In this app: how distinctive a root is to a surah after correcting for surahs that mention everything.  <a href='https://en.wikipedia.org/wiki/Tf%E2%80%93idf'>Wikipedia</a>."),
        ("Hypergeometric enrichment", "Statistical test: given that a surah of length L draws K roots from a population of N total, how surprising is it to see k of those K be your input root?  Yields a p-value.  <a href='https://en.wikipedia.org/wiki/Hypergeometric_distribution'>Wikipedia</a>."),
        ("Fano factor", "Variance ÷ mean of a count distribution.  >1 = bursty/clustered, <1 = regular/evenly-paced.  Named after physicist Ugo Fano."),
        ("Shannon entropy", "<b>H = −Σ p log₂ p</b>.  Measure of how spread-out a distribution is (Shannon, 1948).  Used here to score how evenly a root is distributed across surahs."),
        ("Egyptian-standard order", "The 1924 Cairo (Egyptian government) printed Quran's footnoted revelation-order ranking of the 114 surahs — the most widely-accepted modern listing.  Used here for Meccan/Medinan classification (≤86 = Meccan)."),

        # ── Network-tab additions (v10) ──
        ("Modularity", "How clearly a network splits into communities. >0.3 = clear themes; ~0 = no community structure."),
        ("Diameter", "Longest shortest-path between any two nodes — the network's 'farthest hop'."),
        ("Assortativity", "Do hubs link to hubs (+) or to peripherals (−)? Range −1 to +1."),
        ("Articulation point", "A node whose removal would split the graph. A load-bearing root."),
        ("Bridge edge", "An edge whose removal would split the graph. A load-bearing partnership."),
        ("Minimum spanning tree (MST)", "Smallest set of edges that still connects every node — the network's spine."),
        ("k-core (max)", "Largest k where a subgraph exists in which every node has ≥k edges. Measures densest core."),
        ("Chord diagram", "Circular layout — nodes on a ring, edges as chords. Different aesthetic from spring."),
        ("Adjacency matrix", "Network as a square heatmap: row × column = edge weight. Dense diagonal blocks = communities."),
        ("Arc diagram", "Nodes on a baseline, edges as arcs above/below — best view for asymmetric/directed networks."),
        ("Sankey diagram", "Flow viz: width of band = magnitude of flow. Used here for Meccan→Medinan partnership flow."),
        # ── Temporal / revelation-order terms ──
        ("Revelation order", "1..114 — the historical sequence in which surahs were revealed (Egyptian standard order)."),
        ("Mushaf order", "The canonical reading order of surahs in the printed Quran — mostly long→short, not chronological."),
        ("Meccan", "Surah revealed during the Meccan period (revelation order ≤ 86)."),
        ("Medinan", "Surah revealed during the Medinan period (revelation order ≥ 87)."),
        ("Phase network", "Co-occurrence network built only from one phase's ayahs (Meccan or Medinan)."),
        ("Phase diff", "Edges classified by where they appear: in both phases, only Meccan, or only Medinan."),
        ("4-stage evolution", "Four phase-filtered networks: Early/Middle/Late Meccan + Medinan, side by side."),
        ("Gravitational center", "Mean global-ayah-index of a root's occurrences — 'where in the Quran' a concept lives."),
        ("Burstiness (Fano factor)", "Variance ÷ mean of inter-occurrence gaps. High = clustered bursts; low = evenly spread."),
        ("Spread (entropy)", "Shannon entropy of a root's surah distribution. High = pervasive; low = concentrated."),
        ("Lead-lag (directed)", "P(B appears within ±2 mushaf ayahs of A | A appears) — measures who tends to 'open' to whom."),
        ("Ego network", "A single root in the center surrounded by its closest partners and the edges among them."),

        # ── Two Books (Disjoint Letters · Signal · Biology) ──
        ("Muqaṭṭaʿāt (disjoint letters)", "The mysterious letter-openings of 29 sūras (الٓمٓ, حمٓ, قٓ …). This app tests them as a POSITIONAL pointer, not a hidden code."),
        ("Pointer (index)", "The validated reading of the muqaṭṭaʿāt: a tag that groups & places contiguous sūra-families — like a library call number — without describing content."),
        ("Permutation / label-shuffle null", "Re-running a statistic thousands of times on randomly relabeled or reshuffled data to see whether the REAL value is unusual. The p-value is the fraction of shuffles at least as extreme."),
        ("Contiguity", "How tightly a set of sūras sits together in an ordering (muṣḥaf or revelation). Measured as mean pairwise distance; small = tightly clustered."),
        ("KL-divergence", "Kullback–Leibler divergence (bits): how far one distribution sits from a baseline. Here, a sūra's letter mix vs the corpus letter mix."),
        ("Redundancy", "1 − H/H<sub>max</sub>: how far a distribution is from perfectly even. High = a few symbols dominate."),
        ("Lexical richness (type-token ratio)", "Unique roots ÷ total roots in a sūra. Lower in long sūras (vocabulary repeats) — a length confound, not a code."),
        ("Letters ≈ bases · roots ≈ codons · words ≈ proteins", "The Two Books biology metaphor: a mapping that lets sequence-biology statistics be applied to scripture as an analytical lens (not a claim of genetic structure)."),
        ("Enrichment (bearer test)", "Do the sūras whose disjoint-letter opening contains a letter carry that letter at higher density than chance? Tested by permutation."),
        ("Zipf's law", "Frequency ∝ 1/rank — a straight line on log-log axes. Natural-language hallmark; the root (codon) distribution is even steeper (~−1.56) because roots pool word-forms."),
        ("Fano factor (dispersion)", "Variance ÷ mean of inter-occurrence gaps. >1 = bursty/clustered, <1 = regular. Compared here to a Poisson null."),
        ("Autocorrelation", "Correlation of a signal with a lagged copy of itself — detects 'memory' (e.g. long sūras sitting next to long ones)."),
    ]
    for term, defn in terms:
        st.markdown(
            f"<div class='glossary-row'><div class='term'>{term}</div>"
            f"<div class='defn'>{defn}</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 4 — HOW TO READ EACH CHART
# =====================================================================
with TABS[3]:
    st.markdown('<div class="help-section">📊 HOW TO READ EACH KIND OF CHART</div>',
                unsafe_allow_html=True)
    charts = [
        ("🌐 Network diagram",
         "Dots = roots; lines = co-occurrence.  Red dots = your inputs; navy/colored = partners.  Drag, zoom, hover.",
         "Thick edge = many shared ayahs.  Big dot = highly connected."),
        ("📊 Sorted horizontal bar",
         "Each bar = one root or one pair.  Longer = stronger.  Sorted top-to-bottom by strength.",
         "Read the top bar first; the differences are real if the bars look obviously different."),
        ("📈 Small multiples",
         "Grid of tiny same-axis charts, one per root.",
         "Use to compare distributions across roots at a glance."),
        ("🔺 Motif gallery",
         "Each tile is a real motif — a mini-network drawn as a triangle / square / pentagon.",
         "Red node = input root; navy = partner.  Edge number = weight."),
        ("📍 Heat strip",
         "One bar per surah, colored by how many input roots appear in that surah.",
         "Hover any bar to see exactly which roots."),
        ("🎯 PMI vs Jaccard scatter",
         "Each dot = one pair of input roots.  X = PMI, Y = Jaccard.  Four colored quadrants.",
         "Top-right = strong + frequent.  Bottom-right (violet) = 💎 hidden gem (strong but rare)."),
    ]
    for title, what, how in charts:
        st.markdown(
            f"<div class='help-card'><h4>{title}</h4>"
            f"<div class='what'>{what}</div>"
            f"<div class='how'><b>🔍 Read it:</b> {how}</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 5 — PAGE TOUR
# =====================================================================
with TABS[4]:
    st.markdown('<div class="help-section">🗺️ TOUR OF THE PAGES</div>',
                unsafe_allow_html=True)
    pages = [
        ("📖 Home", "Tabs (PROCESS / VISUALIZE / EXPORT / DISPLAY / EXPLORE).",
         "Type roots, press 🚀 Analyze, click per-root cards to drill in."),
        ("🔍 Per Root Profile", "Each input root's own deep dive, or 🔗 ALL TOGETHER combined view.",
         "Combined view defaults to surah-level co-presence — most populated."),
        ("🌐 Network", "GRAPH-FIRST page — 16 distinct network visualisations in 8 sections.",
         "§1 Stats banner · §2 TEMPORAL (Meccan vs Medinan + 4-stage evolution + phase-flow Sankey + phase-diff graph) · §3 Topology (force-directed + chord + adjacency matrix) · §4 Lead-Lag (directed + arc) · §5 Robustness (articulation/bridges + MST + k-core layered) · §6 Ego networks · §7 Communities · §8 Centrality tables."),
        ("🔺 Motifs", "Triads, quads, pentads as visible shapes.",
         "Motif progression view at Layer 3 shows all sizes at once."),
        ("📖 Ayah Browser", "Every matched ayah with diacritized text.",
         "Filter by root, surah, or free text."),
        ("📊 Compare & Heatmaps", "Pair-level overlap at both surah and ayah granularity.",
         "Drill into any pair to see exactly which ayahs they share."),
        ("🧬 Morphology", "Prefix/suffix particles attached to each root.",
         "For grammatical context (al-, wa, fa, bi, li, ka, sa, pronominals)."),
        ("📈 Statistics", "13+ analytical tiles in one place.",
         "Includes PMI, Jaccard, P(B|A), P(A|B), TF-IDF, dispersion, centrality, "
         "k-core, clustering, enrichment, and the metric cross-reference scatter."),
        ("🧩 Topic Modeling", "Discover latent themes from root co-occurrence.",
         "Louvain communities + distributional (PPMI/SVD) topics, with co-clustering "
         "stability — the thematic grouping of the corpus."),
        ("⬇️ Export", "Save your analysis as Excel / PNGs / PDF.",
         "Multi-sheet xlsx + every chart as PNG + a single PDF."),
        ("🔠 Disjoint Letters (Two Books)",
         "Tests al-Muqaṭṭaʿāt as a positional pointer + a hypothesis workbench, "
         "in three scale-categories: Position · Sequence · Semantic.",
         "Run the contiguity null (p≈2×10⁻⁵), build your own sūra family, or probe "
         "letter density, entropy and lexical richness. Each tab has an inline guide."),
        ("📡 Signal (Two Books)",
         "The corpus read as a 1-D signal: length autocorrelation, root recurrence "
         "vs Poisson, entropy spectrum (FFT), verse rhythm.",
         "Use to ask whether ORDERING carries structure beyond a reshuffled corpus."),
        ("🧬 Biology (Two Books)",
         "The genome metaphor — letters≈bases, roots≈codons, words≈proteins: base "
         "composition, codon-usage Zipf, di-codon bias, sequence complexity.",
         "Use to borrow sequence-biology statistics; every test has a permutation null."),
        ("🗺️ Spatial Patterns (Two Books)",
         "The corpus as a GIS point/area landscape — Ripley K, Clark-Evans R, "
         "Moran's I, LISA & Getis-Ord G*, each vs a CSR null; plus latent spatial "
         "archetypes (PCA + k-means with bootstrap stability).",
         "Ask HOW a concept is arranged (clustered/random/regular) and WHERE it "
         "concentrates, across muṣḥaf / 286-band transpose / revelation folds. "
         "Input is a root; its surface forms are extracted, not typed."),
        ("📋 FDR Summary (Two Books)",
         "One Benjamini–Hochberg correction across one representative test per domain "
         "(Position · Sequence · Semantic · Signal · Biology).",
         "Use to see which Two Books findings survive multiple-testing correction."),
    ]
    for title, what, when in pages:
        st.markdown(
            f"<div class='help-card'><h4>{title}</h4>"
            f"<div class='what'><b>What you get:</b> {what}</div>"
            f"<div class='how'><b>When to use:</b> {when}</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 6 — CASE STUDY  (real-numbers walk-through of every module)
# =====================================================================
with TABS[5]:
    st.markdown('<div class="help-section">📖 CASE STUDY — ظلم · عدل · رحم (computed live)</div>',
                unsafe_allow_html=True)
    cs = _cs_live()
    if cs is None:
        st.warning("Live case-study computation needs the default corpus (book6.xlsx) in "
                   "the app folder. Open any analysis page once, then return here.")
    else:
        import pandas as pd
        R = cs["R"]; N = cs["N"]; pairs = cs["pairs"]; nameof = cs["nameof"]
        st.markdown(f"<div class='help-analogy'>Every number on this page is computed "
                    f"<b>live from the loaded corpus</b> ({N:,} āyahs) for three roots — "
                    f"ظلم (oppression), عدل (justice), رحم (mercy). Nothing is hard-coded; "
                    f"if the corpus changes, this page changes with it.</div>",
                    unsafe_allow_html=True)

        st.markdown('<div class="help-section">STEP 1 — FREQUENCY &amp; RARITY</div>',
                    unsafe_allow_html=True)
        st.dataframe(pd.DataFrame([{"root": r, "āyahs": cs["freq"][r]["ayahs"],
                                    "sūrahs": cs["freq"][r]["surahs"]} for r in R]),
                     hide_index=True, width="stretch")
        st.caption("The order-of-magnitude gap (عدل is far rarer than ظلم/رحم) is why later "
                   "modules must normalize — naive counts always favour the bigger root.")

        st.markdown('<div class="help-section">STEP 2 — RAW CO-OCCURRENCE (two granularities)</div>',
                    unsafe_allow_html=True)
        st.dataframe(pd.DataFrame([{"pair": f"{a} ↔ {b}",
                                    "same āyah": pairs[(a, b)]["same_ayah"],
                                    "same sūrah": pairs[(a, b)]["same_surah"]}
                                   for (a, b) in pairs]), hide_index=True, width="stretch")
        st.caption("ظلم ↔ عدل share few/no āyahs but several sūrahs — related ideas often sit "
                   "in adjacent verses, not the same verse. Granularity matters.")

        st.markdown('<div class="help-section">STEP 3 — STATISTICAL ASSOCIATION</div>',
                    unsafe_allow_html=True)
        st.dataframe(pd.DataFrame([{"pair": f"{a} ↔ {b}",
                                    "PMI (bits)": round(pairs[(a, b)]["pmi"], 2),
                                    "Jaccard": round(pairs[(a, b)]["jaccard"], 3),
                                    "P(B|A)": round(pairs[(a, b)]["p_b_a"], 3),
                                    "P(A|B)": round(pairs[(a, b)]["p_a_b"], 3)}
                                   for (a, b) in pairs]), hide_index=True, width="stretch")
        st.plotly_chart(_cs_chart_metric_progression(pairs), width="stretch")
        st.caption("PMI corrects for how common each root is. ظلم ↔ عدل PMI is slightly "
                   "negative — they co-occur a touch LESS than chance at āyah level, "
                   "falsifying the naive 'opposites attract' guess.")

        st.markdown('<div class="help-section">STEP 4 — DENSITY-PER-SŪRAH (length-normalized)</div>',
                    unsafe_allow_html=True)
        dens = cs["dens"]
        st.dataframe(pd.DataFrame([{"sūrah": f"S{s} {nameof.get(s, '')}", "size": sz,
                                    "touched": t, "density %": round(d, 1)}
                                   for s, sz, t, d in dens[:8]]),
                     hide_index=True, width="stretch")
        st.plotly_chart(_cs_chart_length_norm(dens), width="stretch")
        if dens:
            ts, tsz, tt, td = dens[0]
            st.caption(f"Length-normalized winner: S{ts} {nameof.get(ts, '')} at {td:.1f}% "
                       f"density — not the largest sūrah. Ranking by raw count would mislead.")

        st.markdown('<div class="help-section">STEP 5 — NETWORK &amp; MOTIFS</div>',
                    unsafe_allow_html=True)
        net = cs["net"]
        mc1, mc2, mc3 = st.columns(3)
        mc1.metric("Nodes (3 + partners)", net["nodes"])
        mc2.metric("Edges", net["edges"])
        mc3.metric("Closed triads", net["triangles"])
        st.plotly_chart(_cs_chart_motif_uniqueness(), width="stretch")
        st.caption(f"A closed triad — three roots all mutually co-occurring — is structural "
                   f"evidence a single pair cannot give. This network has {net['triangles']}.")

        st.markdown('<div class="help-section" style="background:#06A77D;">SYNTHESIS</div>',
                    unsafe_allow_html=True)
        pz = pairs[("ظلم", "رحم")]; po = pairs[("ظلم", "عدل")]
        st.markdown(f"- **ظلم ↔ رحم** is the strong pairing: {pz['same_ayah']} shared āyahs, "
                    f"{pz['same_surah']} shared sūrahs, PMI {pz['pmi']:+.2f}.")
        st.markdown(f"- **ظلم ↔ عدل** share only {po['same_ayah']} āyah but {po['same_surah']} "
                    f"sūrahs — the same conversation in different verses.")
        st.markdown("- Convergence across raw counts, PMI, Jaccard, density and network is what "
                    "makes a claim defensible: one metric can mislead; several agreeing rarely do.")
        st.caption("Every figure above recomputes from the corpus on load — the data speaks "
                   "for itself.")

    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 7 — TWO BOOKS GUIDE
# =====================================================================
with TABS[6]:
    st.markdown('<div class="help-section">🧭 TWO BOOKS — how to use the new analyses</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="help-analogy">The <b>Two Books</b> section reads the same '
                'corpus at three scales — 🧭 <b>Position</b> (where sūras sit), 🔤 '
                '<b>Sequence</b> (letters≈bases), 🧩 <b>Semantic</b> (roots≈codons, '
                'words≈proteins). Every test is computed live and checked against a '
                'permutation/Poisson null; nothing is a "miracle" claim, and sūra-length '
                'is flagged as a confound throughout.</div>', unsafe_allow_html=True)
    _tb_pages = [
        ("🔠 Disjoint Letters",
         "The al-Muqaṭṭaʿāt pointer explorer + hypothesis workbench, in three categories.",
         "Position — family explorer, contiguity test, leave-one-out robustness, a live "
         "scorecard and a cross-domain FDR battery. Sequence — alphabet, letter-density "
         "enrichment, letter entropy/KL/redundancy. Semantic — build-your-own-family lab, "
         "root entropy/richness, and an embedding-space theme test."),
        ("📡 Signal",
         "The corpus as an ordered one-dimensional signal.",
         "Length signal + autocorrelation; root recurrence vs a Poisson null (Fano "
         "factor); entropy spectrum (FFT, Haar wavelet energies, and a Ricker scalogram); "
         "verse rhythm; and two-root co-recurrence cross-correlation."),
        ("🧬 Biology",
         "The genome metaphor — letters≈bases, roots≈codons, words≈proteins.",
         "Base composition; codon (root) usage with a Zipf fit; di-codon bias vs a "
         "shuffled stream; sequence complexity + a sūra dendrogram; and Markov memory of "
         "the letter stream."),
        ("🗺️ Spatial Patterns",
         "The corpus as a GIS point/area landscape (ecology/geography statistics).",
         "Point-pattern (Ripley K/L, Clark-Evans R, Getis-Ord G* focal, Fano) and "
         "areal (Moran's I, LISA, G* hot/cold, coverage) views vs a CSR null; "
         "rearrangements (muṣḥaf · 286-band ayah-major transpose · revelation); and "
         "unsupervised spatial archetypes with bootstrap stability + a semantic-"
         "alignment check. Root input; surface forms extracted."),
        ("📋 FDR Summary",
         "One Benjamini–Hochberg correction across all five domains.",
         "Runs one representative test per domain via the shared kernel and shows which "
         "survive multiple-testing correction. FDR controls multiplicity, not the "
         "length confound."),
    ]
    for _t, _w, _h in _tb_pages:
        st.markdown(f"<div class='help-card'><h4>{_t}</h4><div class='what'>{_w}</div>"
                    f"<div class='how'><b>🔍 What's inside:</b> {_h}</div></div>",
                    unsafe_allow_html=True)
    st.markdown('<div class="help-section">📊 READING THE TWO BOOKS STATISTICS</div>',
                unsafe_allow_html=True)
    _tb_stats = [
        ("Permutation p-value",
         "Re-runs the statistic on thousands of reshuffled/relabeled copies of the data. "
         "p = the fraction of that null at least as extreme as the observed value. Small "
         "p = unlikely by chance alone."),
        ("Null histogram + red line",
         "The pale histogram is the reshuffled null; the red line is the observed value. "
         "The further into the tail the red line sits, the smaller the p."),
        ("BH-FDR q-value",
         "When many tests run, some clear p&lt;0.05 by luck. Benjamini–Hochberg adjusts to "
         "control the false-discovery rate — read q, not raw p, for the verdict. q "
         "controls multiplicity, NOT confounding."),
        ("Length confound",
         "The muqaṭṭaʿāt are the long sūras, so length-driven metrics (entropy, root "
         "count) can look 'special' purely through length. Read every content result "
         "against the length caveat on the Organization tab."),
        ("Scalogram",
         "A 2-D heatmap over scale (rows) × position (columns). Broad bright bands at "
         "large scales spanning the width = a slow trend; an isolated bright spot = a "
         "localized burst of variation at one place and scale."),
    ]
    for _t, _d in _tb_stats:
        st.markdown(f"<div class='glossary-row'><div class='term'>{_t}</div>"
                    f"<div class='defn'>{_d}</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='tab-back'>↑ Click 📋 Overview tab above to go back</div>",
                unsafe_allow_html=True)


# =====================================================================
# TAB 8 — TROUBLESHOOTING
# =====================================================================
with TABS[7]:
    st.markdown('<div class="help-section">🆘 TROUBLESHOOTING</div>',
                unsafe_allow_html=True)
    st.markdown("""
    - **"No matches" when I type a root** — confirm **Tolerant matching** is ON in the sidebar
      (it should be by default).  Folds Persian ↔ Arabic letter variants.
    - **Want to start over** — click 🔄 START OVER at the top-right of any page.
    - **Want to deep-dive int
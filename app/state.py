# re-deploy 1779770521
"""state.py — v4: simple, bright, always-visible menu."""
from __future__ import annotations

from pathlib import Path

import streamlit as st

import analysis as A


HERE = Path(__file__).resolve().parent
# Try multiple capitalizations so the same code works on case-sensitive
# Linux (HF Spaces, Render) and case-insensitive Windows.
DEFAULT_XLSX = None
for candidate in ("book6.xlsx", "Book6.xlsx", "BOOK6.xlsx",
                  "book5.xlsx", "Book5.xlsx"):
    for base in (HERE, HERE.parent / "data"):   # also look in the repo's data/ folder
        _p = base / candidate
        if _p.exists():
            DEFAULT_XLSX = _p
            break
    if DEFAULT_XLSX is not None:
        break
if DEFAULT_XLSX is None:
    DEFAULT_XLSX = HERE / "book6.xlsx"  # fall through to original error path

# Bump this string any time analysis.normalize_letters / index-building logic
# changes so cached corpora are automatically rebuilt.
NORMALIZE_VERSION = "v4-full-unicode-fold-2026-05"


NAV_SECTIONS = [
    (None, [(None, [("app.py", "Home", "🏠")])]),
    ("🧭 EXPLORE", [
        ("Overview", [
            ("pages/7_Statistics.py", "Statistics", "📈"),
            ("pages/9_Topic_Modeling.py", "Topic Modeling", "🧩"),
        ]),
        ("Concepts", [
            ("pages/5_Compare_Heatmaps.py", "Compare & Heatmaps", "📊"),
            ("pages/2_Network.py", "Network", "🌐"),
            ("pages/3_Motifs.py", "Motifs", "🔺"),
            ("pages/1_Per_Root_Profile.py", "Per-Root Profile", "🔍"),
            ("pages/6_Morphology.py", "Morphology", "🧬"),
            ("pages/4_Ayah_Browser.py", "Ayah Browser", "📖"),
        ]),
        ("Interpret", [
            (["pages/11_Interpret.py", "pages/8a_Interpret.py"], "Interpret", "🧠"),
            (["pages/10_Practical_Lens.py", "pages/8f_Practical_Lens.py"], "Practical Lens", "🔭"),
            (["pages/8_Calibration.py", "pages/8e_Calibration.py"], "Calibration", "🎚️"),
        ]),
    ]),
    ("🔬 DEEP DIVES", [
        (None, [
            ("pages/19_Concept_Deep_Dive.py", "Concept Deep-Dive", "🔬"),
            ("pages/20_Ayah_Deep_Dive.py", "Ayah Deep-Dive", "🔭"),
        ]),
    ]),
    ("📚 TWO BOOKS", [
        (None, [
            ("pages/14_Disjoint_Letters.py", "Disjoint Letters", "🔠"),
            ("pages/15_Signal.py", "Signal", "📡"),
            ("pages/16_Biology.py", "Biology", "🧬"),
            ("pages/18_Spatial_Patterns.py", "Spatial Patterns", "🗺️"),
            ("pages/17_Two_Books_Summary.py", "FDR Summary", "📋"),
        ]),
    ]),
    ("🛠️ HELP & EXPORT", [
        (None, [
            ("pages/0_Help.py", "Help", "❓"),
            (["pages/12_Export.py", "pages/8_Export.py"], "Export", "⬇️"),
            (["pages/13_Usage.py", "pages/9_Usage.py"], "Usage", "📊"),
        ]),
    ]),
]


def render_grouped_nav():
    """Two-level grouped sidebar nav (L1 category → L2 sub-group → page links).
    Version-safe: if st.page_link is missing (<1.31) the default nav stays."""
    if not hasattr(st, "page_link"):
        return
    st.markdown(
        "<style>"
        # VERIFIED LIVE against the rendered DOM (overlap measured in px, not
        # eyeballed). Two root causes defeated every earlier attempt:
        #  (1) the negative margin lived on [data-testid=stElementContainer]
        #      (NOT stPageLink) — it pulled each card up onto its neighbour;
        #  (2) the L1/L2 header markdown OVERFLOWS its auto-sized container, so
        #      the next card began ABOVE the header text => masking.
        # FIX (structural, once and for all): zero the container margins; use ONE
        # small gap as the only row-spacing lever; and give the header containers
        # a real min-height via :has() so a label can never overflow into a card.
        "[data-testid='stSidebarNav']{display:none!important;}"
        "section[data-testid='stSidebar'] [data-testid='stElementContainer']{margin:0!important;}"
        "section[data-testid='stSidebar'] div[data-testid='stVerticalBlock']{gap:3px!important;}"
        "section[data-testid='stSidebar'] [data-testid='stPageLink']{margin:0!important;}"
        "section[data-testid='stSidebar'] [data-testid='stPageLink'] a{"
        "border:0!important;border-left:3px solid #06AED5!important;border-radius:4px!important;"
        "background:#F7F9FB!important;padding:3px 9px!important;margin:0!important;"
        "line-height:1.25!important;box-shadow:none!important;}"
        "section[data-testid='stSidebar'] [data-testid='stElementContainer']:has(.dlnav-h2)"
        "{min-height:16px!important;height:auto!important;overflow:visible!important;}"
        "section[data-testid='stSidebar'] [data-testid='stElementContainer']:has(.dlnav-h1)"
        "{min-height:24px!important;height:auto!important;overflow:visible!important;}"
        ".dlnav-h1{font-size:11px!important;font-weight:800!important;letter-spacing:1px!important;"
        "color:#FFFFFF!important;text-transform:uppercase!important;background:#1D3557!important;"
        "border-radius:6px!important;padding:5px 10px!important;margin:6px 0 0!important;"
        "line-height:1.2!important;display:block!important;white-space:nowrap!important;"
        "overflow:hidden!important;text-overflow:ellipsis!important;}"
        ".dlnav-h2{font-size:10px!important;font-weight:800!important;letter-spacing:.4px!important;"
        "color:#2C3E5C!important;text-transform:uppercase!important;margin:5px 0 0 2px!important;"
        "padding:0!important;line-height:1.1!important;display:block!important;}"
        "</style>",
        unsafe_allow_html=True,
    )
    with st.sidebar:
        st.markdown("<div class='dlnav-h1' style='text-align:center;'>📚 NAVIGATION</div>",
                    unsafe_allow_html=True)
        for l1, subs in NAV_SECTIONS:
            if l1:
                st.markdown(f"<div class='dlnav-h1'>{l1}</div>", unsafe_allow_html=True)
            for l2, items in subs:
                if l2:
                    st.markdown(f"<div class='dlnav-h2'>{l2}</div>", unsafe_allow_html=True)
                for path, label, icon in items:
                    for _p in (path if isinstance(path, (list, tuple)) else [path]):
                        try:
                            st.page_link(_p, label=label, icon=icon)
                            break
                        except Exception:
                            continue
        st.divider()


def inject_css():
    st.markdown("""
    <style>
    /* ===== APP BACKGROUND ===== */
    .stApp { background: #FAFBFD; }
    .main .block-container { padding-top: 1.6rem; padding-bottom: 4rem; max-width: 1400px; }

    /* ===== SIDEBAR: WIDER, WHITE, CLEAN ===== */
    [data-testid="stSidebar"] {
        background: #FFFFFF;
        min-width: 260px !important;
        max-width: 260px !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 0.5rem;
    }

    /* ===== SIDEBAR PAGE NAV — ALWAYS VISIBLE, BIG, READABLE ===== */
    [data-testid="stSidebarNav"] {
        background: #FFF8E1;
        border: 2px solid #FCBF49;
        border-radius: 14px;
        padding: 6px 6px 8px 6px;
        margin: 0 2px 10px 2px;
        box-shadow: 0 2px 8px rgba(252, 191, 73, 0.15);
    }
    [data-testid="stSidebarNav"]::before {
        content: "📚  PAGES";
        display: block;
        color: #1D3557;
        font-size: 12px !important;
        font-weight: 800;
        letter-spacing: 1.2px;
        padding: 4px 8px 6px 8px;
        border-bottom: 1px solid #FCBF49;
        margin-bottom: 4px;
        text-align: center;
    }
    [data-testid="stSidebarNav"] ul { padding: 0 !important; margin: 0 !important; }
    [data-testid="stSidebarNav"] li { list-style: none !important; }
    [data-testid="stSidebarNav"] li a,
    [data-testid="stSidebarNav"] li a span {
        display: block !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        color: #1D3557 !important;
        text-decoration: none !important;
    }
    [data-testid="stSidebarNav"] li a {
        background: #FFFFFF !important;
        padding: 7px 10px !important;
        margin: 2px 0 !important;
        border-radius: 9px !important;
        border-left: 5px solid #06AED5 !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.06);
        transition: all 0.15s ease;
    }
    [data-testid="stSidebarNav"] li a:hover,
    [data-testid="stSidebarNav"] li a:hover span {
        background: #FCBF49 !important;
        color: #1B263B !important;
        border-left-color: #E63946 !important;
        transform: translateX(2px);
    }
    [data-testid="stSidebarNav"] li a[aria-current="page"],
    [data-testid="stSidebarNav"] li a[aria-current="page"] span {
        background: #E63946 !important;
        color: #FFFFFF !important;
        border-left: none !important;
        box-shadow: 0 3px 10px rgba(230, 57, 70, 0.35);
    }

    /* ===== SIDEBAR HEADERS / LABELS ===== */
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #1D3557;
        font-size: 15px !important;
        font-weight: 800 !important;
        margin: 14px 0 6px 0 !important;
        padding: 4px 8px;
        background: #F0F4F8;
        border-radius: 6px;
        border-left: 4px solid #1D3557;
    }
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] label {
        font-size: 13px !important;
        color: #374151 !important;
    }
    [data-testid="stSidebar"] .stCaption,
    [data-testid="stSidebar"] [data-testid="stCaptionContainer"] {
        font-size: 12px !important;
        color: #6B7280 !important;
    }

    /* ===== HERO BANNER ===== */
    .hero-banner {
      background: linear-gradient(135deg, #E63946 0%, #F77F00 50%, #FCBF49 100%);
      color: white; padding: 10px 20px; border-radius: 12px;
      box-shadow: 0 4px 14px rgba(230, 57, 70, 0.22);
      margin-bottom: 10px;
    }
    .hero-banner h1 { color: white !important; margin: 0; font-weight: 800; font-size: 24px !important; }
    .hero-banner p  { color: rgba(255,255,255,0.94); margin: 2px 0 0; font-size: 13px; }
    [data-testid="stMetricValue"] { color: #E63946; font-weight: 800; font-size: 24px !important; }
    [data-testid="stMetricLabel"] { font-weight: 700; font-size: 12px !important; color: #1D3557 !important; }
    [data-testid="stMetric"] { padding: 6px 8px !important; }

    /* ===== QURANIC DIACRITIZED TEXT ===== */
    .quranic-verse {
        direction: rtl; text-align: center;
        font-family: 'Amiri Quran', 'Amiri', 'Scheherazade New', 'Noto Naskh Arabic',
                     'Traditional Arabic', serif;
        font-size: 26px; line-height: 2.1;
        color: #1B263B;
        background: linear-gradient(135deg, #FFFEF7 0%, #FFF8E1 100%);
        border: 2px solid #FCBF49;
        border-radius: 12px;
        padding: 18px 24px; margin: 12px 0;
        box-shadow: 0 4px 12px rgba(252, 191, 73, 0.18);
    }
    .ayah-meta {
        font-size: 12px; color: #6B7280; text-align: center;
        margin-top: -6px; margin-bottom: 12px;
        letter-spacing: 0.5px;
    }
    .arabic-text { direction: rtl; text-align: right; font-size: 19px;
                   font-family: 'Amiri', 'Noto Naskh Arabic', serif;
                   line-height: 1.9; }
    mark.hit { background: #FCBF49; color: #1B263B; padding: 0 4px;
               border-radius: 4px; font-weight: bold; }

    /* ===== LAYER LABELS ===== */
    .layer-label {
        display: inline-block; background: #1D3557; color: white;
        padding: 5px 16px; border-radius: 14px; font-size: 13px;
        font-weight: 800; margin: 10px 0 10px 0; letter-spacing: 0.8px;
        text-transform: uppercase;
    }

    /* ===== PILLS ===== */
    .pill { display:inline-block; padding:4px 14px; border-radius:14px;
            font-size:13px; font-weight:700; margin: 2px 4px 2px 0; }
    .pill-input { background: #E63946; color:white; }
    .pill-rare { background: #7209B7; color:white; }
    .pill-common { background: #06AED5; color:white; }
    .pill-ubiq { background: #FCBF49; color:#1B263B; }

    /* ===== TOP TABS — BIG, ALWAYS-VISIBLE ===== */
    [data-baseweb="tab-list"] {
        gap: 6px !important;
        background: #F0F4F8 !important;
        padding: 8px !important;
        border-radius: 14px !important;
        margin-bottom: 14px;
    }
    [data-baseweb="tab"] {
        font-size: 15px !important;
        font-weight: 700 !important;
        padding: 11px 22px !important;
        border-radius: 10px !important;
        background: white !important;
        color: #1D3557 !important;
        border: 2px solid #E5E7EB !important;
    }
    [data-baseweb="tab"]:hover {
        background: #FCBF49 !important;
        color: #1B263B !important;
        border-color: #F77F00 !important;
    }
    [data-baseweb="tab"][aria-selected="true"] {
        background: #E63946 !important;
        color: white !important;
        border-color: #E63946 !important;
        box-shadow: 0 4px 12px rgba(230, 57, 70, 0.4);
    }

    /* ===== TOP INPUT — COMPACT PILL ROW ===== */
    .top-input-box {
        background: transparent;
        padding: 0;
        max-width: 480px;
        margin: 0 auto 8px auto;
        border: none;
        box-shadow: none;
    }
    .top-input-pill {
        display: inline-block;
        background: linear-gradient(135deg, #E63946 0%, #F77F00 100%);
        color: white;
        padding: 6px 16px;
        border-radius: 18px;
        font-size: 15px;
        font-weight: 800;
        letter-spacing: 0.3px;
        margin-right: 10px;
        box-shadow: 0 3px 8px rgba(230,57,70,0.35);
    }
    .top-input-hint {
        display: inline-block;
        color: #1D3557;
        font-size: 13px;
        font-weight: 600;
    }
    .top-input-hint b { color: #E63946; }

    /* ===== BUTTONS ===== */
    .stButton button {
        font-weight: 600;
        border-radius: 10px;
    }
    .stButton button[kind="primary"] {
        background: #E63946 !important;
        border: none !important;
    }

    /* ===== EXPANDERS / TABLES ===== */
    [data-testid="stExpander"] {
        border: 1px solid #E5E7EB !important;
        border-radius: 10px !important;
        background: white !important;
        margin: 6px 0 !important;
    }
    /* GLOBAL TABLE LAYOUT — every dataframe across the app is compact AND
       flows side-by-side when there is horizontal room, so narrow tables
       stop wasting vertical space and consecutive tables share one row. */
    [data-testid="stDataFrame"],
    [data-testid="stDataFrameResizable"] {
        border-radius: 10px;
        overflow: hidden;
        max-width: 460px !important;
        display: inline-block !important;
        vertical-align: top;
        margin: 4px 10px 4px 0 !important;
    }
    /* When tables are stacked inside columns we still want them tight */
    [data-testid="stVerticalBlock"] > [data-testid="stDataFrame"] {
        margin-bottom: 8px !important;
    }
    hr { margin: 1.2rem 0 !important; opacity: 0.4; }
    /* ===== INSIGHT CALLOUTS ===== */
    .insight-card {
        background: linear-gradient(135deg, #FFF8E1 0%, #FFFFFF 100%);
        border-left: 6px solid #E63946;
        border-radius: 10px;
        padding: 14px 20px;
        margin: 10px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .insight-card .icon { font-size: 22px; }
    .insight-card .headline { font-size: 16px; color: #1D3557; font-weight: 700; margin-bottom: 4px; }
    .insight-card .value { font-size: 28px; color: #E63946; font-weight: 800; line-height: 1.2; }
    .insight-card .sub { font-size: 13px; color: #6B7280; margin-top: 2px; }

    /* ===== MAIN HEADINGS — bigger ===== */
    .main h3, .main .stMarkdown h3 { font-size: 22px !important; color: #1D3557; font-weight: 800; }
    .main h4, .main .stMarkdown h4 { font-size: 18px !important; color: #1D3557; }
    /* ===== BODY ===== */
    .main p, .main .stMarkdown p { font-size: 15px; line-height: 1.55; }

    /* ===== TIGHTER LAYOUTS ===== */
    /* Reduce gap between st.columns */
    [data-testid="stHorizontalBlock"] { gap: 8px !important; }
    /* Metric cards — less padding */
    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 10px;
        padding: 8px 12px !important;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    [data-testid="stMetricValue"] { line-height: 1.1 !important; }
    /* Tighter divider */
    hr { margin: 0.7rem 0 !important; opacity: 0.35; }
    /* Tighter vertical block spacing */
    .element-container { margin-bottom: 0.3rem !important; }
    /* Tighter dataframes */
    [data-testid="stDataFrame"] { margin: 4px 0; }
    /* Smaller plotly chart margins */
    .stPlotlyChart { padding: 0 !important; margin: 4px 0 !important; }
    /* Tighter expanders */
    [data-testid="stExpander"] summary { padding: 6px 12px !important; }
    [data-testid="stExpander"] > div > div { padding: 6px 12px !important; }
    /* Caption tight */
    [data-testid="stCaptionContainer"] { margin: 2px 0 !important; }
    /* st.subheader tighter */
    .main h3 { margin: 6px 0 4px 0 !important; }
    /* Buttons tight rows */
    .stButton { margin: 1px 0 !important; }
    /* Chip rows tighter */
    .pill { margin: 1px 3px 1px 0 !important; padding: 3px 11px !important; }
    /* AGGRESSIVE selectors so Streamlit's own styles can't win */
    .top-input-box input,
    .top-input-box [data-testid="stTextInput"] input,
    .top-input-box [data-testid="stTextInputRootElement"] input,
    .top-input-box .stTextInput input,
    .top-input-box [class*="TextInput"] input {
        font-size: 28px !important;
        font-weight: 900 !important;
        color: #1B263B !important;
        background: linear-gradient(135deg, #FFFEF7 0%, #FFF1A8 100%) !important;
        border: 3px solid #E63946 !important;
        border-top: none !important;
        border-top-left-radius: 0 !important;
        border-top-right-radius: 0 !important;
        border-bottom-left-radius: 12px !important;
        border-bottom-right-radius: 12px !important;
        padding: 14px 18px !important;
        text-align: left !important;
        height: 64px !important;
        min-height: 64px !important;
        line-height: 1.2 !important;
        box-shadow: inset 0 1px 3px rgba(230,57,70,0.12), 0 2px 8px rgba(230,57,70,0.12) !important;
    }
    /* Zero-gap: kill any margins/padding between the banner header and the input wrapper */
    .top-input-box,
    .top-input-box > div,
    .top-input-box [data-testid="stTextInput"],
    .top-input-box [data-testid="stTextInput"] > div,
    .top-input-box [data-testid="stTextInputRootElement"] {
        margin-top: 0 !important; padding-top: 0 !important;
        margin-bottom: 0 !important;
    }
    /* The Streamlit input wrapper itself shouldn't add a border */
    .top-input-box [data-testid="stTextInputRootElement"] {
        border: none !important;
        background: transparent !important;
    }
    .top-input-box input::placeholder,
    .top-input-box [data-testid="stTextInput"] input::placeholder {
        color: #E63946 !important;
        opacity: 0.45 !important;
        font-weight: 700 !important;
        font-size: 22px !important;
        text-align: left !important;
    }
    .top-input-box [data-testid="stTextInput"] input:focus {
        border-color: #F77F00 !important;
        background: linear-gradient(135deg, #FFFFFF 0%, #FFE89A 100%) !important;
        box-shadow: 0 0 0 4px rgba(247,127,0,0.25), 0 4px 14px rgba(230,57,70,0.18) !important;
    }

    .analyze-call { display:none; }  /* deprecated — was wasting vertical space */
    .analyze-call-OLD {
        background: linear-gradient(135deg, #FFFEF7, #FFE89A);
        border: 2px dashed #E63946;
        border-radius: 14px;
        text-align: center;
        font-size: 17px;
        font-weight: 700;
        color: #1D3557;
        padding: 10px 14px;
        margin: 6px auto 8px auto;
        max-width: 600px;
        animation: pulseGlow 2s ease-in-out infinite alternate;
    }
    @keyframes pulseGlow {
        from { box-shadow: 0 0 0 0 rgba(230,57,70,0.35); }
        to   { box-shadow: 0 0 0 8px rgba(230,57,70,0); }
    }

    /* Hide auto-generated "app" entry at top of sidebar nav (redundant) */
    [data-testid="stSidebarNav"] ul li:first-child {
        display: none !important;
    }

    /* ===== CLICKABILITY CUES ===== */
    .stButton button { cursor: pointer !important; }
    .stButton button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
        transition: all 0.12s ease;
    }
    /* COMPACT INPUT REGION — eliminate every wasted pixel */
    /* hero margin tighter */
    .hero-banner { margin-bottom: 2px !important; }
    /* Kill ALL element-container margins inside the home block container */
    .main .block-container > div .element-container {
        margin-bottom: 0 !important; padding-bottom: 0 !important;
        margin-top: 0 !important; padding-top: 0 !important;
    }
    /* Streamlit emits a wrapper around stMarkdown — reset it too */
    .main .block-container [data-testid="stMarkdown"] {
        margin: 0 !important; padding: 0 !important;
    }
    /* The label banner sits flush — collapse the wrapper around it */
    .main .block-container [data-testid="stMarkdown"] + [data-testid="stMarkdown"] {
        margin-top: 0 !important;
    }
    /* Empty paragraphs Streamlit sometimes inserts: hide them */
    .main .block-container p:empty { display: none !important; }
    .main .block-container div:empty { display: none !important; min-height: 0 !important; }
    /* Three header pills — distinct colours, big readable labels */
    .main [data-testid="stExpander"] { margin: 2px 4px 2px 0 !important; }
    .main [data-testid="stExpander"] summary {
        padding: 8px 14px !important;
        min-height: 46px !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        border-radius: 9px !important;
        text-shadow: 0 1px 2px rgba(0,0,0,0.15);
    }
    .main [data-testid="stExpander"] summary p,
    .main [data-testid="stExpander"] summary span {
        font-size: 16px !important; font-weight: 800 !important;
    }
    /* ABOUT expander — blue accent (first column) */
    [data-testid="stHorizontalBlock"] > div:nth-child(1) [data-testid="stExpander"] summary {
        background: linear-gradient(135deg, #1D3557 0%, #06AED5 100%) !important;
        color: #FFFFFF !important;
    }
    [data-testid="stHorizontalBlock"] > div:nth-child(1) [data-testid="stExpander"] summary svg,
    [data-testid="stHorizontalBlock"] > div:nth-child(1) [data-testid="stExpander"] summary p,
    [data-testid="stHorizontalBlock"] > div:nth-child(1) [data-testid="stExpander"] summary span {
        color: #FFFFFF !important;
    }
    /* NEW HERE? expander — orange/red accent (second column) */
    [data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stExpander"] summary {
        background: linear-gradient(135deg, #E63946 0%, #F77F00 100%) !important;
        color: #FFFFFF !important;
    }
    [data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stExpander"] summary svg,
    [data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stExpander"] summary p,
    [data-testid="stHorizontalBlock"] > div:nth-child(2) [data-testid="stExpander"] summary span {
        color: #FFFFFF !important;
    }
    /* HELP button (third column) — gold accent, matches expander height */
    [data-testid="stHorizontalBlock"] > div:nth-child(3) .stButton button[kind="primary"] {
        font-size: 16px !important;
        font-weight: 900 !important;
        min-height: 46px !important;
        height: 46px !important;
        background: linear-gradient(135deg, #FCBF49 0%, #F77F00 100%) !important;
        color: #1B263B !important;
        border: 2px solid #1B263B !important;
        border-radius: 9px !important;
        letter-spacing: 0.5px;
    }
    [data-testid="stHorizontalBlock"] > div:nth-child(3) .stButton button[kind="primary"]:hover {
        background: #E63946 !important;
        color: white !important;
        border-color: #FCBF49 !important;
    }
    /* First-time banner / tip-line collapse */
    .top-input-box { margin: 0 !important; padding: 0 !important; }
    .top-input-box + div { margin-top: 0 !important; padding-top: 0 !important; }
    /* Suggestion-row gap and chip styling */
    .top-input-box ~ div [data-testid="stHorizontalBlock"] {
        gap: 2px !important; margin: 0 !important;
        line-height: 1 !important;
    }
    /* 4-pt vertical gap between the two chip rows */
    .top-input-box ~ div [data-testid="stHorizontalBlock"] + [data-testid="stHorizontalBlock"] {
        margin-top: 4px !important;
    }
    /* 4-pt vertical gap between the input row and the suggestions header */
    .top-input-box + div, .top-input-box ~ [data-testid="stMarkdown"]:first-of-type {
        margin-top: 4px !important;
    }
    .top-input-box ~ div .element-container { margin: 0 !important; padding: 0 !important; }
    .top-input-box ~ div .stButton { margin: 0 !important; padding: 0 !important; }
    /* Condensed chips — 20 per row, line-height 1, very tight */
    .top-input-box ~ div .stButton button {
        font-size: 13px !important;
        font-weight: 700 !important;
        padding: 2px 4px !important;
        min-height: 30px !important;
        height: 30px !important;
        line-height: 1 !important;
        background: linear-gradient(135deg, #FFFEF7 0%, #FFE89A 100%) !important;
        color: #1B263B !important;
        border: 1.5px solid #FCBF49 !important;
        border-radius: 7px !important;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
        letter-spacing: 0 !important;
    }
    .top-input-box ~ div .stButton button:hover {
        background: linear-gradient(135deg, #FCBF49 0%, #F77F00 100%) !important;
        color: white !important;
        border-color: #E63946 !important;
        transform: translateY(-1px);
        transition: all 0.12s ease;
    }
    /* Reduce vertical block padding on home page */
    .main .block-container { padding-top: 0.8rem !important; }
    /* Kill the redundant "(empty)" + bottom info-callout */
        /* ===== HYPERLINK STYLING — distinguish real links from text ===== */
    .main a, .main a:link, .main a:visited {
        color: #06AED5 !important;
        text-decoration: underline !important;
        font-weight: 700;
    }
    .main a:hover {
        color: #1D3557 !important;
        text-decoration: underline !important;
    }
    /* ===== CONTRAST FIXES ===== */
    .hero-banner h1 {
        text-shadow: 0 1px 3px rgba(0,0,0,0.25);
    }
    .layer-label {
        box-shadow: 0 2px 6px rgba(29,53,87,0.30);
    }

    /* Analyze button sized to match the bigger input */
    .top-input-box ~ div .stButton button[kind="primary"] {
        font-size: 22px !important;
        font-weight: 900 !important;
        height: 60px !important;
        min-height: 60px !important;
        border-radius: 12px !important;
        background: #E63946 !important;
        color: white !important;
        border: none !important;
        letter-spacing: 0.5px;
    }
    /* But keep suggestion chips at their compact 38px height (override the above) */
    .top-input-box ~ div div[data-testid="stHorizontalBlock"] .stButton button {
        font-size: 17px !important;
        font-weight: 800 !important;
        height: 38px !important;
        min-height: 38px !important;
        background: linear-gradient(135deg, #FFFEF7 0%, #FFE89A 100%) !important;
        color: #1B263B !important;
        border: 2px solid #FCBF49 !important;
        border-radius: 9px !important;
    }

    /* ───── LANDSCAPE BANNER (portrait phones only) ───── */
    .landscape-hint { display: none; }
    @media (max-width: 700px) and (orientation: portrait) {
        .landscape-hint {
            display: block;
            background: linear-gradient(90deg, #FCBF49 0%, #F77F00 100%);
            color: #1B263B;
            padding: 9px 12px;
            margin: 6px 0 10px 0;
            border-radius: 8px;
            font-weight: 700;
            font-size: 13.5px;
            text-align: center;
            box-shadow: 0 2px 6px rgba(247, 127, 0, 0.25);
        }
    }
    /* ───── HORIZONTAL SCROLL FOR PLOTLY CHARTS ON SMALL SCREENS ─────
       Wraps any chart in a swipeable container so labels stop overlapping. */
    @media (max-width: 720px) {
        [data-testid="stPlotlyChart"] {
            overflow-x: auto !important;
            -webkit-overflow-scrolling: touch;
        }
        [data-testid="stPlotlyChart"] > div {
            min-width: 720px !important;
        }
    }

    /* ───── MOBILE / TOUCH FRIENDLY (iPhone, iPad, Android) ───── */
    /* iOS HIG: minimum tap target is 44pt. Bump chips + button on small screens. */
    @media (max-width: 820px) {
        .top-input-box ~ div .stButton button {
            font-size: 15px !important;
            min-height: 44px !important;
            height: 44px !important;
            padding: 4px 8px !important;
            border-radius: 9px !important;
        }
        .top-input-box ~ div div[data-testid="stHorizontalBlock"] .stButton button {
            font-size: 17px !important;
            min-height: 44px !important;
            height: 44px !important;
        }
        .top-input-box ~ div .stButton button[kind="primary"] {
            font-size: 20px !important;
            min-height: 56px !important;
            height: 56px !important;
        }
        .top-input-box input {
            font-size: 22px !important;
            height: 56px !important;
            min-height: 56px !important;
        }
        .hero-banner h1 { font-size: 26px !important; line-height: 1.15 !important; }
        .hero-banner p  { font-size: 14px !important; }
    }
    @media (max-width: 420px) {
        .top-input-box input {
            font-size: 20px !important;
            height: 52px !important;
            min-height: 52px !important;
        }
        .hero-banner h1 { font-size: 22px !important; }
    }
    </style>
    <script>
    // Stop Streamlit's bare "C" hotkey (clear cache) from intercepting
    // anything the user might type — Ctrl+C copy must keep working.
    (function() {
        if (window.__keyShimInstalled) return;
        window.__keyShimInstalled = true;
        document.addEventListener('keydown', function(e) {
            if (e.ctrlKey || e.metaKey || e.altKey) return;
            if (e.key === 'c' || e.key === 'C') {
                e.stopPropagation();
            }
        }, true);
    })();

    // ── Force big-input styling after Streamlit renders (CSS may not win) ──
    // Responsive: pick font/height based on viewport so iPhone doesn't overflow.
    (function ensureBigInput() {
        function pickSizes() {
            const w = window.innerWidth || document.documentElement.clientWidth;
            if (w < 420)  return { font: '20px', height: '52px', pad: '10px 14px' };
            if (w < 820)  return { font: '22px', height: '56px', pad: '12px 16px' };
            return { font: '28px', height: '64px', pad: '14px 18px' };
        }
        function applyStyle() {
            const root = document.querySelector('.top-input-box');
            if (!root) return false;
            const inp = root.querySelector('input');
            if (!inp) return false;
            const sz = pickSizes();
            inp.style.setProperty('font-size', sz.font, 'important');
            inp.style.setProperty('font-weight', '900', 'important');
            inp.style.setProperty('height', sz.height, 'important');
            inp.style.setProperty('min-height', sz.height, 'important');
            inp.style.setProperty('text-align', 'left', 'important');
            inp.style.setProperty('padding', sz.pad, 'important');
            inp.style.setProperty('border', '3px solid #E63946', 'important');
            inp.style.setProperty('border-top', 'none', 'important');
            inp.style.setProperty('border-radius', '0 0 12px 12px', 'important');
            inp.style.setProperty('background',
                'linear-gradient(135deg, #FFFEF7 0%, #FFF1A8 100%)', 'important');
            inp.style.setProperty('color', '#1B263B', 'important');
            // wrapper should not add its own gap
            const wrap = inp.closest('[data-testid="stTextInput"]');
            if (wrap) {
                wrap.style.setProperty('margin', '0', 'important');
                wrap.style.setProperty('padding', '0', 'important');
            }
            // Mobile keyboard hints (Arabic-friendly)
            inp.setAttribute('autocapitalize', 'off');
            inp.setAttribute('autocorrect', 'off');
            inp.setAttribute('spellcheck', 'false');
            return true;
        }
        let tries = 0;
        const iv = setInterval(function() {
            tries++;
            if (applyStyle() || tries > 60) clearInterval(iv);
        }, 200);
        window.addEventListener('resize', applyStyle);
        window.addEventListener('orientationchange', applyStyle);
    })();

    // ── Anonymous visitor ID + country (for analytics) ──
    // Sets two URL query params on first load so Python can log a country-
    // level visit count. No PII, no cookies, no third-party trackers.
    //   • vid  — random UUID stored in localStorage (stable per browser)
    //   • cc   — two-letter ISO country code (from ipapi.co, cached 7 days)
    (function visitorIdentity() {
        // Streamlit's multipage sidebar strips query params on navigation,
        // so we re-inject vid+cc from localStorage on EVERY page load if
        // the URL is missing them.  One redirect per page nav, no loop:
        // after the redirect the URL has everything localStorage has, so
        // urlMissing* are both false.
        try {
            const params = new URLSearchParams(window.location.search);

            // ── 1. Stable visitor UUID (mint if first ever visit) ──
            let vid = localStorage.getItem('qr_vid');
            if (!vid || vid.length !== 32) {
                vid = (crypto && crypto.randomUUID)
                    ? crypto.randomUUID().replace(/-/g, '')
                    : (Math.random().toString(36) + Math.random().toString(36)).replace(/[^a-z0-9]/g, '').slice(0, 32);
                localStorage.setItem('qr_vid', vid);
            }

            // ── 2. Cached country (7-day TTL) ──
            const cc      = localStorage.getItem('qr_cc');
            const ccTs    = parseInt(localStorage.getItem('qr_cc_ts') || '0', 10);
            const ccFresh = !!(cc && ccTs && (Date.now() - ccTs < 7 * 24 * 3600 * 1000));

            // ── 3. If URL is missing what we have, redirect once ──
            const urlMissingVid = (params.get('vid') !== vid);
            const urlMissingCc  = ccFresh && (params.get('cc') !== cc);
            if (urlMissingVid || urlMissingCc) {
                const p = new URLSearchParams(window.location.search);
                p.set('vid', vid);
                if (ccFresh) p.set('cc', cc);
                const newUrl = window.location.pathname + '?' + p.toString() + window.location.hash;
                // location.replace doesn't pollute the back-stack
                window.location.replace(newUrl);
                return;     // page is being replaced, stop here
            }

            // ── 4. No cached country?  Fetch it now (fire-and-forget). ──
            //   The result lands in localStorage; the NEXT page navigation
            //   will redirect with ?cc=XX attached, and Python will log it.
            if (!ccFresh) {
                fetch('https://ipapi.co/country/', { cache: 'no-store' })
                    .then(function(r){ return r.text(); })
                    .then(function(c){
                        c = (c || '').trim().toUpperCase();
                        if (c.length === 2 && /^[A-Z]{2}$/.test(c)) {
                            localStorage.setItem('qr_cc', c);
                            localStorage.setItem('qr_cc_ts', String(Date.now()));
                            // Optional: also stick it on the current URL so
                            // a Streamlit rerun (e.g. clicking a button)
                            // picks it up without a full nav.
                            const p2 = new URLSearchParams(window.location.search);
                            p2.set('cc', c);
                            window.history.replaceState({}, '',
                                window.location.pathname + '?' + p2.toString() + window.location.hash);
                        }
                    })
                    .catch(function(){});
            }
        } catch (e) { /* analytics must never break the app */ }
    })();

    // ── Per-keystroke autocomplete shim ──
    // Streamlit's text_input only commits on Enter or blur.  On desktop we
    // hook the input element and force a blur + refocus 250 ms after the
    // last keystroke so suggestions update as the user types — no Enter.
    //
    // CRITICAL: On touch devices (iPhone, iPad, Android) blur dismisses the
    // soft keyboard, which makes typing impossible.  We detect touch devices
    // and skip the shim entirely — those users press Enter / Go on the
    // soft keyboard to commit, which is the iOS-native pattern anyway.
    (function installPerKeyShim() {
        const isTouchDevice = ('ontouchstart' in window) ||
                              (navigator.maxTouchPoints > 0) ||
                              (navigator.msMaxTouchPoints > 0);
        if (isTouchDevice) return;   // ← iOS / Android safety
        function findInputAndAttach() {
            const root = document.querySelector('.top-input-box');
            if (!root) return false;
            const inp = root.querySelector('input');
            if (!inp || inp.__perKey) return inp ? true : false;
            inp.__perKey = true;
            let lastCommit = inp.value;
            let timer = null;
            inp.addEventListener('input', function() {
                if (inp.value === lastCommit) return;
                clearTimeout(timer);
                timer = setTimeout(function() {
                    if (inp.value === lastCommit) return;
                    lastCommit = inp.value;
                    // Force Streamlit to commit by blurring then refocusing.
                    inp.blur();
                    setTimeout(function() { inp.focus(); }, 30);
                }, 250);
            });
            return true;
        }
        // Streamlit re-renders frequently; keep retrying until we attach.
        let tries = 0;
        const iv = setInterval(function() {
            tries++;
            if (findInputAndAttach() || tries > 40) clearInterval(iv);
        }, 200);
    })();

    // ── Sticky animated progress ribbon at the very top of the page ──
    // Visible whenever Streamlit is rendering/running anything.
    (function topProgressRibbon() {
        if (window.__topRibbonInstalled) return;
        window.__topRibbonInstalled = true;
        const ribbon = document.createElement('div');
        ribbon.id = '__topProgressRibbon';
        ribbon.style.cssText = 'position:fixed;top:0;left:0;right:0;'
            + 'min-height:34px;padding:8px 18px;'
            + 'background:linear-gradient(90deg,#06AED5 0%,#1D3557 100%);'
            + 'z-index:2147483647;display:block;pointer-events:none;'
            + 'color:#FFFFFF;font-weight:700;font-size:14px;'
            + 'letter-spacing:0.3px;text-align:center;'
            + 'text-shadow:0 1px 2px rgba(0,0,0,0.30);'
            + 'box-shadow:0 2px 8px rgba(0,0,0,0.30);'
            + 'transition:all 0.2s ease;';
        ribbon.innerHTML = '<span id="__ribbonSpinner" style="display:none;'
            + 'width:14px;height:14px;border:3px solid #FFFFFF;'
            + 'border-top-color:transparent;border-radius:50%;'
            + 'vertical-align:middle;margin-right:10px;'
            + 'animation:tprSpin 0.8s linear infinite;"></span>'
            + '<span id="__ribbonText">IDLE — app ready</span>';
        // Insert at <html> level so Streamlit's transforms don't trap us
        (document.documentElement || document.body).appendChild(ribbon);
        const style = document.createElement('style');
        style.textContent = '@keyframes tprShine{0%{background-position:200% 0;}'
            + '100%{background-position:-200% 0;}}'
            + '@keyframes tprSpin{to{transform:rotate(360deg);}}';
        document.head.appendChild(style);
        function check() {
            let running = false;
            document.querySelectorAll('[data-testid="stStatusWidget"]').forEach(w => {
                const t = (w.textContent || '').toLowerCase();
                if (t.indexOf('running') >= 0 || t.indexOf('executing') >= 0) running = true;
            });
            if (!running && document.querySelectorAll('.stSpinner').length > 0) running = true;
            if (!running && document.querySelector('[data-testid="stProgress"]')) running = true;
            const spinner = document.getElementById('__ribbonSpinner');
            const text = document.getElementById('__ribbonText');
            if (running) {
                ribbon.style.background = 'linear-gradient(90deg,#E63946 0%,#FCBF49 50%,#F77F00 100%)';
                ribbon.style.backgroundSize = '200% 100%';
                ribbon.style.animation = 'tprShine 1.2s linear infinite';
                ribbon.style.boxShadow = '0 4px 18px rgba(230,57,70,0.6)';
                ribbon.style.fontWeight = '800';
                if (spinner) spinner.style.display = 'inline-block';
                if (text) text.textContent = 'PROCESSING — please wait...';
            } else {
                ribbon.style.background = 'linear-gradient(90deg,#06AED5 0%,#1D3557 100%)';
                ribbon.style.animation = 'none';
                ribbon.style.boxShadow = '0 2px 8px rgba(0,0,0,0.30)';
                ribbon.style.fontWeight = '700';
                if (spinner) spinner.style.display = 'none';
                if (text) text.textContent = 'IDLE — app ready';
            }
        }
        setInterval(check, 180);
    })();
    </script>
    """, unsafe_allow_html=True)


def hero(title, subtitle=""):
    # Single-line hero. No multi-line, no wasted vertical space.
    sub = f" · <span style='font-weight:600;opacity:0.92;'>{subtitle}</span>" if subtitle else ""
    st.markdown(
        f"<div style='background:linear-gradient(90deg,#E63946,#F77F00,#FCBF49);"
        f"color:#FFFFFF;padding:5px 14px;border-radius:8px;margin:0 0 4px 0;"
        f"font-size:16px;font-weight:800;letter-spacing:0.2px;"
        f"text-shadow:0 1px 2px rgba(0,0,0,0.25);white-space:nowrap;"
        f"overflow:hidden;text-overflow:ellipsis;'>"
        f"{title}{sub}</div>",
        unsafe_allow_html=True,
    )


def layer(n, label):
    st.markdown(f"<span class='layer-label'>LAYER {n} · {label}</span>",
                unsafe_allow_html=True)

def insight(headline: str, value: str = "", sub: str = ""):
    """Big visual takeaway callout used at the top of each page/section."""
    v = f"<div class='value'>{value}</div>" if value else ""
    s = f"<div class='sub'>{sub}</div>" if sub else ""
    st.markdown(
        f"<div class='insight-card'><div class='headline'><span class='icon'>💡</span>  {headline}</div>{v}{s}</div>",
        unsafe_allow_html=True,
    )


def per_root_hint(input_roots=None, compact=False):
    """🔔 High-visibility banner reminding the user where to drill into ONE root.

    Used on the home page (large) and on every deep-dive page (compact).
    With input_roots provided AND not compact, also renders one-click jump
    buttons for each input root that navigate directly to Per Root Profile.
    """
    if compact:
        st.markdown(
            """
            <div style="background:linear-gradient(90deg,#FFF3B0 0%,#FCBF49 100%);
                        border:2px solid #E63946; border-radius:10px;
                        padding:8px 14px; margin:6px 0 10px 0;
                        font-size:13.5px; color:#1D3557; line-height:1.5;">
              <b style="color:#E63946;">👉 Want one root in full detail?</b>
              Open <b style="background:#1D3557; color:#fff; padding:1px 8px;
                            border-radius:5px;">🔍 Per Root Profile</b>
              (left sidebar) and pick the root — every input root has its own page.
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    # Large pulsing callout for the home page
    st.markdown(
        """
        <div style="background: linear-gradient(135deg,#FFF3B0 0%,#FCBF49 100%);
                    border:3px solid #E63946; border-radius:14px;
                    padding:14px 18px; margin:6px 0 14px 0;
                    box-shadow:0 3px 12px rgba(230,57,70,0.22);
                    animation: pulseHint 2.6s ease-in-out infinite;">
          <div style="font-size:17px; font-weight:900; color:#E63946;
                      letter-spacing:0.4px; margin-bottom:6px;">
            👉 WANT THE FULL PROFILE OF JUST ONE ROOT?
          </div>
          <div style="font-size:14.5px; color:#1D3557; line-height:1.6;">
            Click any per-root jump button below, or open
            <b style="background:#1D3557; color:#fff; padding:2px 10px;
                      border-radius:6px;">🔍 Per Root Profile</b>
            from the <b>left-sidebar navigation</b> — every input root has its
            own dedicated page with full charts, ayahs, surface forms, and partners.
          </div>
        </div>
        <style>
          @keyframes pulseHint {
            0%,100% { box-shadow:0 3px 12px rgba(230,57,70,0.22); }
            50%     { box-shadow:0 3px 22px rgba(230,57,70,0.55); }
          }
        </style>
        """,
        unsafe_allow_html=True,
    )

    if input_roots:
        cols = st.columns(min(len(input_roots), 6))
        for i, r in enumerate(input_roots):
            if cols[i % len(cols)].button(
                f"🔍 {r}",
                key=f"perroot_jump_{r}",
                width='stretch',
                help=f"Jump to the Per Root Profile page for '{r}'",
            ):
                st.session_state.profile_root = r
                st.switch_page("pages/1_Per_Root_Profile.py")



def render_quranic_verse(diacritized_text, surah_num=None, ayah_num=None, surah_name=None):
    if not diacritized_text:
        return
    st.markdown(f"<div class='quranic-verse'>{diacritized_text}</div>",
                unsafe_allow_html=True)
    if surah_num is not None:
        meta = f"Surah {surah_num}"
        if surah_name:
            meta += f" ({surah_name})"
        if ayah_num is not None:
            meta += f" · Ayah {ayah_num}"
        st.markdown(f"<div class='ayah-meta'>{meta}</div>", unsafe_allow_html=True)


@st.cache_resource(show_spinner="Loading corpus…")
def load(xlsx_path, _version: str = NORMALIZE_VERSION):
    # _version is part of the cache key, so bumping NORMALIZE_VERSION invalidates
    # any old cached corpus that was indexed with a different normalize_letters.
    return A.load_corpus(xlsx_path)


def get_corpus():
    inject_css()
    render_grouped_nav()
    _stages = None
    if "_app_ready" not in st.session_state:
        _stages = st.empty()
        _stages.markdown(
            '<div style="display:flex;gap:6px;margin:2px 0;flex-wrap:nowrap;font-size:12.5px;font-weight:700;">'
            '<span style="background:#2A9D8F;color:#fff;padding:3px 10px;border-radius:6px;">✓ Booted</span>'
            '<span style="background:#2A9D8F;color:#fff;padding:3px 10px;border-radius:6px;">✓ Started</span>'
            '<span style="background:#E63946;color:#fff;padding:3px 10px;border-radius:6px;">~ Indexing...</span>'
            '<span style="background:#9CA3AF;color:#fff;padding:3px 10px;border-radius:6px;">○ Ready</span>'
            '</div>',
            unsafe_allow_html=True,
        )
    render_start_over_button()
    default = str(DEFAULT_XLSX) if DEFAULT_XLSX.exists() else ""
    with st.sidebar.expander("📂 Data source", expanded=False):
        path = st.text_input("Path to xlsx", value=default)
        up = st.file_uploader("Or upload xlsx", type=["xlsx"])
        if up is not None:
            import tempfile
            tmp = Path(tempfile.gettempdir()) / "quran_uploaded.xlsx"
            tmp.write_bytes(up.getvalue())
            path = str(tmp)
    if not path or not Path(path).exists():
        st.warning("Set a valid path to book6.xlsx (or book5.xlsx) in the sidebar.")
        st.stop()
    c = load(path, NORMALIZE_VERSION)
    # Stages panel cleanup: mark ready, then briefly show final state, then clear
    if "_app_ready" not in st.session_state and _stages is not None:
        # Stages already complete — no value in showing them. Clear the panel.
        _stages.empty()
        st.session_state["_app_ready"] = True
    return c


@st.cache_data(show_spinner=False)
def _all_roots_sorted(corpus_id, normalize, _corpus):
    src = _corpus.index_norm.keys() if normalize else _corpus.index_exact.keys()
    return sorted(src)


def _add_root(r):
    if r and r not in st.session_state.query_roots:
        st.session_state.query_roots.append(r)
    st.session_state["_force_rerun"] = True


def _add_many(roots):
    added = 0
    for r in roots:
        if r and r not in st.session_state.query_roots:
            st.session_state.query_roots.append(r)
            added += 1
    st.session_state["_force_rerun"] = True
    return added


def _replace_with(roots):
    """Replace the entire current selection with a new set (used when user
    types/pastes new roots — old query is fully replaced)."""
    st.session_state.query_roots = list(roots)
    st.session_state["_force_rerun"] = True


def _remove_root(r):
    if r in st.session_state.query_roots:
        st.session_state.query_roots.remove(r)
    st.session_state["_force_rerun"] = True


def _prefix_expansions(p):
    """Return all prefix forms that a typed prefix should be checked against.
    Handles the Arabic surface-form → root-form mismatch where word-initial
    alef (ا) is often a written form of root hamza (ء)."""
    if not p:
        return [p]
    out = [p]
    # If first char is bare alef ا — also try with leading hamza ء
    if p[0] == "ا":
        out.append("ء" + p[1:])
    # If first char is hamza ء — also try with leading alef ا
    if p[0] == "ء":
        out.append("ا" + p[1:])
    return out


def _smart_lookup(prefix, all_roots, normalize):
    from analysis import strip_diacritics, normalize_letters
    p = strip_diacritics(prefix or "").strip()
    if not p:
        return [], ""
    if normalize:
        p = normalize_letters(p)
    tokens = p.split()
    aset = set(all_roots)
    if len(tokens) >= 2:
        full_matches = [t for t in tokens if t in aset]
        return full_matches, "multi"
    # Try every alef↔hamza expansion of the typed prefix
    for cand in _prefix_expansions(p):
        if cand in aset:
            return [cand], "multi"
    matches = []
    seen = set()
    for cand in _prefix_expansions(p):
        for r in all_roots:
            if r.startswith(cand) and r not in seen:
                matches.append(r); seen.add(r)
                if len(matches) >= 12:
                    break
        if len(matches) >= 12:
            break
    return matches, "prefix"


def _random_samples(prefix, all_roots, normalize, k=20):
    """Return up to k random roots whose normalized form starts with `prefix`
    (or any roots if prefix is empty).  Deterministic per prefix so the
    sample doesn't reshuffle on every keystroke or rerun.  When the prefix
    begins with alef ا or hamza ء, both forms are tried (because Arabic
    surface ا is often the written form of root-initial hamza ء)."""
    import random
    from analysis import strip_diacritics, normalize_letters
    p = strip_diacritics(prefix or "").strip()
    if p and normalize:
        p = normalize_letters(p)
    if not p:
        pool = list(all_roots)
    else:
        seen = set()
        pool = []
        for cand in _prefix_expansions(p):
            for r in all_roots:
                if r.startswith(cand) and r not in seen:
                    pool.append(r); seen.add(r)
    if not pool:
        return []
    rng = random.Random(hash(p) ^ 0xA1B2C3)
    rng.shuffle(pool)
    return pool[:k]


def query_controls(corpus):
    # No default-fill: a fresh session / post-reset starts EMPTY.
    if "query_roots" not in st.session_state:
        st.session_state.query_roots = []
    if "prefix_search" not in st.session_state:
        st.session_state.prefix_search = ""

    st.sidebar.header("🔎 Query")
    normalize_pre = st.session_state.get("normalize", False)
    all_roots = _all_roots_sorted(id(corpus), normalize_pre, corpus)
    total = len(all_roots)

    st.sidebar.caption("Type a prefix OR paste multiple roots:")
    st.sidebar.text_input("Search…", key="prefix_search",
                          placeholder="رحم   or   رحم ءله صبر",
                          label_visibility="collapsed")
    prefix = st.session_state.prefix_search

    if prefix.strip():
        matches, mode = _smart_lookup(prefix, all_roots, normalize_pre)
        last_sb = st.session_state.get("_last_processed_sb", "")
        if mode == "multi" and matches and prefix != last_sb:
            if list(matches) != st.session_state.query_roots:
                _replace_with(matches)
                st.session_state["_last_processed_sb"] = prefix
                st.rerun()
            else:
                st.sidebar.caption(f"Already these {len(matches)}.")
                st.session_state["_last_processed_sb"] = prefix
        elif mode == "prefix" and matches:
            st.sidebar.caption(f"{len(matches)} prefix matches:")
            for i in range(0, len(matches), 2):
                pair = matches[i:i + 2]
                cols = st.sidebar.columns(len(pair))
                for col, root in zip(cols, pair):
                    col.button(f"+ {root}", key=f"sug_sb_{root}",
                               on_click=_add_root, args=(root,),
                               width='stretch')
    else:
        st.sidebar.caption(f"{total} roots indexed.")

    # Random sample panel in the sidebar (always visible, narrows by prefix)
    _samples_sb = _random_samples(prefix, all_roots, normalize_pre, k=10)
    if _samples_sb:
        st.sidebar.caption(
            "🎲 random sample" +
            (f" (prefix «{prefix.strip()}»)" if prefix.strip() else " (all roots)")
            + ":")
        for i in range(0, len(_samples_sb), 2):
            pair = _samples_sb[i:i + 2]
            cols = st.sidebar.columns(len(pair))
            for col, root in zip(cols, pair):
                col.button(root, key=f"rnd_sb_{root}",
                           on_click=_add_root, args=(root,),
                           width='stretch')

    st.sidebar.markdown("**Current:**")
    if not st.session_state.query_roots:
        st.sidebar.caption("_(empty)_")
    else:
        for r in list(st.session_state.query_roots):
            c1, c2 = st.sidebar.columns([4, 1])
            c1.markdown(f"<span class='pill pill-input'>{r}</span>",
                        unsafe_allow_html=True)
            c2.button("✕", key=f"rm_sb_{r}", on_click=_remove_root, args=(r,))

    if st.sidebar.button("🗑️ Clear all", key="clearall_sb"):
        st.session_state.query_roots = []; st.rerun()

    st.sidebar.divider()
    # Default tolerant-matching ON so Persian↔Arabic Unicode variants
    # (ک↔ك, ی↔ي, alif-maqsura ى, alef variants, ta-marbuta) all match.
    if "normalize" not in st.session_state:
        st.session_state["normalize"] = True
    normalize = st.sidebar.checkbox("Tolerant matching",
                                    key="normalize",
                                    help="Folds Persian/Arabic letter variants "
                                         "(ک↔ك, ی↔ي, ى→ي, آ/أ/إ→ا, ة→ه) and strips diacritics, "
                                         "so the same root matches no matter which keyboard typed it.")
    st.sidebar.header("🌐 Network")
    top_p = st.sidebar.slider("Top partners", 5, 40,
                              st.session_state.get("top_partners", 15),
                              key="top_partners")
    min_w = st.sidebar.slider("Min edge weight", 1, 10,
                              st.session_state.get("min_weight", 1),
                              key="min_weight")
    run = st.sidebar.button("🚀 Analyze",
                            type="primary", width='stretch')
    raw = " ".join(st.session_state.query_roots)
    return raw, normalize, top_p, min_w, run


def render_top_input_bar(corpus):
    # No default-fill: a fresh session / post-reset starts EMPTY so the user is
    # never presented with a query they didn't ask for.
    if "query_roots" not in st.session_state:
        st.session_state.query_roots = []
    if "prefix_top" not in st.session_state:
        st.session_state.prefix_top = ""

    normalize_pre = st.session_state.get("normalize", False)
    all_roots = _all_roots_sorted(id(corpus), normalize_pre, corpus)

    # Big, attractive, distinct label sitting flush on top of the input box
    st.markdown(
        "<div style='background:linear-gradient(90deg,#E63946 0%,#F77F00 100%); "
        "color:#FFFFFF; font-size:20px; font-weight:900; letter-spacing:0.3px; "
        "padding:10px 18px; border-radius:10px 10px 0 0; margin:0; "
        "text-shadow:0 1px 2px rgba(0,0,0,0.25); text-align:left;'>"
        "✍️  Type one or more <u>characters</u> — suggestions appear instantly &nbsp;·&nbsp; "
        "<b style='font-size:22px; vertical-align:middle;'>press</b> "
        "<b style='background:#FFFFFF; color:#E63946; padding:4px 14px; "
        "border-radius:8px; font-size:24px; font-weight:900; "
        "box-shadow:0 0 0 3px rgba(255,255,255,0.4), 0 2px 6px rgba(0,0,0,0.3); "
        "letter-spacing:0.5px; margin-left:2px; "
        "vertical-align:middle; display:inline-block;'>↵ Enter</b>"
        "<b style='font-size:22px; vertical-align:middle;'> to apply</b>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='top-input-box'>", unsafe_allow_html=True)
    c1, c2 = st.columns([2, 1])
    def _on_input_change():
        # Force a fresh rerun so the suggestions panel reflects the new prefix.
        st.session_state.pop("_last_processed_top", None)

    with c1:
        st.text_input("input", key="prefix_top",
                      placeholder="e.g. رحم ءله صبر",
                      label_visibility="collapsed",
                      on_change=_on_input_change)
    with c2:
        run_top = st.button("🚀 Analyze", key="run_top", type="primary",
                            width='stretch')

    # Auto-focus the input on first session load — cursor blinks immediately
    if not st.session_state.get("_autofocused"):
        st.markdown(
            """
            <script>
            setTimeout(() => {
                const doc = window.parent.document;
                const box = doc.querySelector('.top-input-box');
                if (box) {
                    const inp = box.querySelector('input');
                    if (inp) inp.focus();
                }
            }, 250);
            </script>
            """,
            unsafe_allow_html=True,
        )
        st.session_state["_autofocused"] = True

    prefix = st.session_state.prefix_top
    last_top = st.session_state.get("_last_processed_top", "")
    # Multi-token paste path — replace query immediately
    if prefix.strip() and prefix != last_top:
        matches, mode = _smart_lookup(prefix, all_roots, normalize_pre)
        if mode == "multi" and matches:
            if list(matches) != st.session_state.query_roots:
                _replace_with(matches)
                st.session_state["_last_processed_top"] = prefix
                st.rerun()
            else:
                st.session_state["_last_processed_top"] = prefix

    # ─── ONE tight "Suggestions" panel directly under the input ─────
    # Always visible.  Empty input → 20 random roots.
    # As soon as the user types ≥1 char, the sample is filtered to roots
    # whose normalized form starts with that prefix (and reshuffled — but
    # stably, so re-running with the same prefix gives the same 20 picks).
    samples = _random_samples(prefix, all_roots, normalize_pre, k=30)
    if samples:
        if prefix.strip():
            _hdr = (f"Suggestions for «{prefix.strip()}» "
                    f"({len(samples)} of "
                    f"{sum(1 for r in all_roots if r.startswith(prefix.strip()))} matches):")
        else:
            _hdr = (f"🎲 Suggestions  (random 30 of {len(all_roots)}):  "
                    f"start typing to narrow.")
        st.markdown(
            f"<div style='margin:-2px 0 1px 4px;font-size:13px;color:#1D3557;'>"
            f"{_hdr}</div>", unsafe_allow_html=True)
        # 15 columns × 2 rows of CONDENSED chips → all 30 fit in two lines
        n_cols = 15
        for row_start in range(0, len(samples), n_cols):
            row = samples[row_start:row_start + n_cols]
            scols = st.columns(len(row))
            for i, root in enumerate(row):
                with scols[i]:
                    if st.button(root, key=f"rnd_top_{root}_{row_start}",
                                 width='stretch'):
                        _add_root(root); st.rerun()

    # The input box at the top already shows what's being analysed.
    # We only render compact remove buttons when there are 2+ roots so the
    # user can drop one without retyping. Single-root queries get no extra UI.
    if len(st.session_state.query_roots) >= 2:
        cols = st.columns(min(8, len(st.session_state.query_roots)))
        for i, r in enumerate(list(st.session_state.query_roots)):
            with cols[i % len(cols)]:
                if st.button(f"✕ {r}", key=f"rm_top_{r}", width='stretch'):
                    _remove_root(r); st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
    return run_top


def compute_all(corpus, raw_query, normalize, top_p, min_w):
    input_roots = A.parse_input_roots(raw_query, normalize)
    if not input_roots:
        st.error("No valid roots parsed.")
        st.stop()

    # Generic progress bar — backend computation is shared across pages, so
    # the label stays page-agnostic. Each page renders its OWN progress bar
    # for any page-specific work it does on top of this.
    _prog_holder = st.empty()
    _bar = _prog_holder.progress(0.0, text=f"Analyzing your input ({len(input_roots)} root(s))...")
    TOTAL_STEPS = 29
    _step = {"i": 0}
    def _tick(_label: str):
        _step["i"] += 1
        try:
            pct = int(round(100 * _step["i"] / TOTAL_STEPS))
            _bar.progress(min(_step["i"] / TOTAL_STEPS, 1.0),
                          text=f"Analyzing your input... {pct}%")
        except Exception:
            pass

    _tick("Finding occurrences"); occurrences = A.find_occurrences(corpus, input_roots, normalize)
    _tick("Co-occurrence search"); partners, match_ayahs = A.cooccurrence(corpus, input_roots, normalize)
    _tick("Co-occurrence table"); cooc_tbl = A.cooccurrence_table(partners)
    _tick("Surface forms"); sforms = A.surface_form_table(corpus, input_roots, normalize)
    _tick("Partner motifs"); pmotifs = A.partner_motifs(corpus, input_roots, normalize, top=20)
    _tick("Building network"); g = A.build_network(corpus, input_roots, normalize, top_partners=top_p, min_weight=min_w)
    _tick("Triad census"); triad = A.triad_census(g)
    _tick("Triangles"); tri_tbl = A.triangles_table(g)
    _tick("Summary statistics"); summary = A.summary_stats(corpus, input_roots, occurrences, partners)
    _tick("Centrality"); centrality = A.centrality_table(g)
    _tick("Communities"); communities = A.detect_communities(g)
    _tick("Surah heatmap"); heatmap = A.surah_heatmap(corpus, input_roots, normalize)
    _tick("Overlap matrix"); overlap = A.overlap_matrix(corpus, input_roots, normalize)
    _tick("Overlap by surah"); overlap_surah = A.overlap_matrix_surah(corpus, input_roots, normalize)
    _tick("Morphology"); morphology = A.morphology_breakdown(corpus, input_roots, normalize)
    _tick("Position stats"); position = A.position_stats(corpus, input_roots, normalize)
    _tick("Baseline rarity"); rarity = A.baseline_rarity(corpus, input_roots, normalize)
    _tick("First & last occurrence"); flast = A.first_last_occurrence(corpus, input_roots, normalize)
    # Enriched network attributes (positional, spatial, rhythm, lead-lag)
    _tick("Node attributes"); node_attrs = A.node_attributes(corpus, input_roots, normalize, order="mushaf")
    _tick("Edge attributes"); edge_attrs = A.edge_attributes(corpus, g, normalize)
    _tick("Spatial occurrences"); spatial = A.spatial_occurrences(corpus, input_roots, normalize, order="mushaf")
    _tick("Cumulative trajectories"); trajectories = A.cumulative_trajectories(corpus, input_roots, normalize, order="mushaf")
    _tick("Lead-lag matrix"); ll_matrix = A.lead_lag_matrix(corpus, input_roots, normalize, window=2)
    _tick("Fingerprints"); fingerprints = A.fingerprint_table(corpus, input_roots, normalize,
                                       node_attrs=node_attrs)
    _tick("Network stats"); net_stats = A.network_stats(g)
    _tick("Phase networks (Meccan/Medinan)"); g_meccan, g_medinan = A.phase_networks(corpus, input_roots, normalize,
                                           top_partners=top_p, min_weight=min_w)
    _tick("Graph diff")
    if g_meccan is not None:
        only_meccan, only_medinan, in_both = A.graph_diff(g_meccan, g_medinan)
    else:
        only_meccan, only_medinan, in_both = [], [], []
    _tick("Directed lead-lag graph"); dg_lead_lag = A.directed_lead_lag_graph(corpus, input_roots, normalize,
                                            window=2, min_strength=0.05)
    _tick("Meccan/Medinan pair matrix"); pair_phase = A.meccan_medinan_pair_matrix(corpus, input_roots, normalize)
    R = dict(
        input_roots=input_roots, normalize=normalize, raw_query=raw_query,
        top_partners=top_p, min_weight=min_w,
        occurrences=occurrences, partners=partners, cooc_tbl=cooc_tbl,
        sforms=sforms, pmotifs=pmotifs, graph=g, triad=triad,
        triangles=tri_tbl, summary=summary, match_ayahs=match_ayahs,
        centrality=centrality, communities=communities, heatmap=heatmap,
        overlap=overlap, overlap_surah=overlap_surah,
        morphology=morphology, position=position,
        rarity=rarity, first_last=flast,
        has_diacritized=corpus.has_diacritized,
        # Enriched network results
        node_attrs=node_attrs, edge_attrs=edge_attrs,
        spatial=spatial, trajectories=trajectories,
        lead_lag=ll_matrix, fingerprints=fingerprints,
        # Graph-native additions
        net_stats=net_stats,
        g_meccan=g_meccan, g_medinan=g_medinan,
        phase_only_meccan=only_meccan,
        phase_only_medinan=only_medinan,
        phase_in_both=in_both,
        dg_lead_lag=dg_lead_lag,
        pair_phase=pair_phase,
        has_rev_order=corpus.has_rev_order,
    )
    st.session_state.results = R
    try:
        _bar.progress(1.0, text="Done")
        _prog_holder.empty()
    except Exception:
        pass
    st.toast(f"Analysis complete - {len(input_roots)} root(s), {len(match_ayahs)} ayahs")
    return R




def needs_recompute() -> bool:
    """Strict: only recompute when there is NO results cache yet, or when
    something actively flipped the _force_rerun flag (user added/removed a
    root, clicked Analyze, toggled normalize). Plain page navigation never
    triggers a recompute, so going Network -> Topic Modeling -> Network
    is fast and the original computed R is preserved."""
    if "results" not in st.session_state:
        return True
    if st.session_state.pop("_force_rerun", False):
        return True
    return False


def need_results():
    if "results" not in st.session_state:
        st.info("Use the input bar at the top — add roots and click 🚀 Analyze.")
        st.stop()
    return st.session_state.results


def highlight_text(seg_text, surface_forms):
    if not seg_text:
        return ""
    toks = seg_text.split()
    sset = set(surface_forms)
    out = []
    for t in toks:
        if t in sset:
            out.append(f"<mark class='hit'>{t}</mark>")
        else:
            out.append(t)
    return "<span class='arabic-text'>" + " ".join(out) + "</span>"



def render_start_over_button():
    """Top-of-page "START OVER" button — visible on every page above the hero.
    Clears all session state and switches back to the home page (app.py)."""
    cols = st.columns([7, 2])
    with cols[1]:
        if st.button("🔄  START OVER",
                     key="__start_over__",
                     width='stretch', type="primary",
                     help="Clears your query, view state, and cache, then returns "
                          "to the home page. The most reliable way to begin fresh."):
            keys_to_clear = [
                "query_roots", "profile_root", "combined_submode",
                "prefix_top", "prefix_search", "_force_rerun",
                "_last_processed_top", "_last_processed_sb",
                "_autofocused", "results", "normalize",
                "top_partners", "min_weight",
                "kofn_slider", "show_charts", "display",
                "ayah_root_pick", "ayah_surah_pick", "ayah_search",
                "ayah_pgsize", "ayah_page", "tri_pick", "morph_pick",
                "pair_a", "pair_b", "cent_metric", "net_metric",
            ]
            for k in keys_to_clear:
                if k in st.session_state:
                    del st.session_state[k]
            try:
                st.cache_data.clear()
            except Exception:
                pass
            try:
                st.cache_resource.clear()
            except Exception:
                pass
            st.switch_page("app.py")


def render_top_nav(active="home"):
    pass


def _inject_visitor_shim():
    """Inject the visitor-identity JS via components.html so it actually
    executes.  st.markdown(unsafe_allow_html=True) silently drops <script>
    tags because the HTML is set via innerHTML — script tags added that way
    are inert per the HTML spec.  components.html renders an iframe whose
    scripts DO run; we use window.top to manipulate the parent page URL
    (same-origin, so cross-frame access is allowed)."""
    try:
        from streamlit.components.v1 import html as _components_html
        _components_html(
            """
            <script>
            (function visitorIdentity() {
                try {
                    var w = window.top || window.parent || window;
                    var ls = w.localStorage;
                    var params = new URLSearchParams(w.location.search);

                    // 1. Stable visitor UUID (mint if first ever visit)
                    var vid = ls.getItem('qr_vid');
                    if (!vid || vid.length !== 32) {
                        vid = (w.crypto && w.crypto.randomUUID)
                            ? w.crypto.randomUUID().replace(/-/g, '')
                            : (Math.random().toString(36) + Math.random().toString(36)).replace(/[^a-z0-9]/g, '').slice(0, 32);
                        ls.setItem('qr_vid', vid);
                    }

                    // 2. Cached country (7-day TTL)
                    var cc      = ls.getItem('qr_cc');
                    var ccTs    = parseInt(ls.getItem('qr_cc_ts') || '0', 10);
                    var ccFresh = !!(cc && ccTs && (Date.now() - ccTs < 7 * 24 * 3600 * 1000));

                    // 3. If parent URL is missing what we have, redirect once
                    var needVid = (params.get('vid') !== vid);
                    var needCc  = ccFresh && (params.get('cc') !== cc);
                    if (needVid || needCc) {
                        var p = new URLSearchParams(w.location.search);
                        p.set('vid', vid);
                        if (ccFresh) p.set('cc', cc);
                        w.location.replace(w.location.pathname + '?' + p.toString() + w.location.hash);
                        return;
                    }

                    // 4. Need a country?  Fetch in background — next nav picks it up.
                    if (!ccFresh) {
                        fetch('https://ipapi.co/country/', { cache: 'no-store' })
                            .then(function(r){ return r.text(); })
                            .then(function(c){
                                c = (c || '').trim().toUpperCase();
                                if (/^[A-Z]{2}$/.test(c)) {
                                    ls.setItem('qr_cc', c);
                                    ls.setItem('qr_cc_ts', String(Date.now()));
                                    var p2 = new URLSearchParams(w.location.search);
                                    p2.set('cc', c);
                                    w.history.replaceState({}, '',
                                        w.location.pathname + '?' + p2.toString() + w.location.hash);
                                }
                            })
                            .catch(function(){});
                    }
                } catch (e) { /* analytics must never break the app */ }
            })();
            </script>
            """,
            height=0,
        )
    except Exception:
        pass


def log_page(page_name):
    _inject_visitor_shim()
    try:
        import analytics as _ana
        _ana.track_once_per_session("page_view", {"page": page_name})
    except Exception:
        pass


def log_search(roots):
    try:
        import analytics as _ana
        _ana.track("search", {"roots": [str(r) for r in roots[:8]]})
    except Exception:
        pass


def log_export(fmt):
    try:
        import analytics as _ana
        _ana.track("export", {"format": fmt})
    except Exception:
        pass

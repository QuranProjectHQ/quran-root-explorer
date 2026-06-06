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


if st.button(f"▶  Run deep-dive on  {target}", type="primary"):
    st.session_state["concept_go"] = target
if st.session_state.get("concept_go") != target:
    st.info(f"Ready to analyse **{target}** across the whole corpus. Click ▶ Run to start — "
            "multimodal fusion is a heavy computation, so it waits for your OK "
            "(and re-confirms whenever you change the concept).")
    st.stop()

try:
    res = _concept(target, normalize, "surah")
except Exception as e:
    st.warning(f"⚠️  {e}")
    st.stop()
fld, dist, null, cg = res["field"], res["distribution"], res["null"], res["cross_granularity"]
syn = res.get("synthesis", {}) or {}
rel = res.get("relations", {}) or {}
rbt = rel.get("related_by_type", {})
seq = res.get("sequence", {}) or {}
_REL = {"consensus": "agree on ≥2 modalities (robust)", "semantic": "meaning-mates",
        "co-location": "territory-mates", "spatial": "distribution-shape kin",
        "orthogonal": "one modality only (independent on the rest)",
        "divergent": "close on one, OPPOSED on another (tension)"}


def _chips(items, n=6):
    items = [str(x) for x in items]
    if not items:
        return "<span style='font-size:20px;color:#0B1320'>—</span>"
    out = " ".join(
        "<span style='font-size:22px;color:#0B1320;background:#E8EEF6;border-radius:7px;"
        "padding:3px 14px;margin:4px 3px;display:inline-block;font-weight:600'>" + r + "</span>"
        for r in items[:n])
    if len(items) > n:
        out += (f" <span style='font-size:14px;color:#444'>+{len(items) - n} more "
                f"(full list in the table)</span>")
    return out


def _show_chips(items, n=6):
    st.markdown(_chips(items, n), unsafe_allow_html=True)


layer(1, "MULTIMODAL FUSION  (semantic ∥ co-location ∥ spatial)")
_ct = rel.get("by_relation", {})
_arch = dist.get("archetype")
g = st.columns(6)
g[0].metric("frequency", dist["frequency"], help="total occurrences of the root across the corpus")
g[1].metric("surahs", dist["n_surahs_present"], help="number of surahs the concept appears in")
g[2].metric("semantic", _ct.get("semantic", 0) + _ct.get("consensus", 0),
            help="meaning-mates (distributional neighbours), including consensus bonds")
g[3].metric("co-location", _ct.get("co-location", 0) + _ct.get("consensus", 0),
            help="territory-mates (shared deployment), including consensus bonds")
g[4].metric("consensus", _ct.get("consensus", 0), help="bonds confirmed on ≥2 independent modalities")
g[5].metric("divergent", _ct.get("divergent", 0),
            help="tension: close on one modality, opposed on another (e.g. shared territory, opposed meaning)")
g2 = st.columns(6)
g2[0].metric("orthogonal", _ct.get("orthogonal", 0), help="single-modality bonds; independent on the others")
g2[1].metric("spatial z", null["z"], help="areal-evenness vs a frequency-matched scramble; ≤ −2 = beyond chance (often null)")
g2[2].metric("archetype", (_arch["tag"] if _arch else "—"), help="spatial distribution archetype")
g2[3].metric("stability", (_arch["stability"] if _arch else "—"), help="archetype robustness under feature jitter")
g2[4].metric("in-ayah pos", seq.get("mean_within_ayah_position"),
             help="mean position within the ayah (0 = start, 1 = end) — a sequence-level feature")
g2[5].metric("ayah-final", f"{round((seq.get('ayah_final_share') or 0) * 100)}%",
             help="share of occurrences that END the ayah (rhyme / fawāṣil)")
st.caption(syn.get("reading", ""))
_pts = [dict(label=x["root"], x=x["axes"]["semantic"], y=x["axes"]["co-location"],
             relation=ty, size=x["axes"]["spatial"])
        for ty, lst in rbt.items() for x in lst]
if _pts:
    st.plotly_chart(PC.chart_fusion_scatter(_pts, "semantic", "co-location",
                    f"{target} — multimodal fusion map"), use_container_width=True)

    @st.cache_data
    def _root_sample(_cid):
        K = _A.normalize_letters
        df = corpus.df
        su = df[_A.COL_SURAH].astype(int).to_numpy()
        ay = df[_A.COL_AYAH].astype(int).to_numpy()
        dia = (df[_A.COL_DIACRITIZED].astype(str).tolist()
               if _A.COL_DIACRITIZED in df.columns else df[_A.COL_SEGMENTED].astype(str).tolist())
        samp = {}
        for i in range(len(df)):
            for r in {K(t) for t in corpus.root_tokens[i]}:
                if r not in samp:
                    samp[r] = (f"{int(su[i])}:{int(ay[i])}", dia[i][:70])
        return samp

    import pandas as _pd
    _samp = _root_sample(id(corpus))
    _crows = [{"root": x["root"], "relation": ty,
               "semantic": x["axes"]["semantic"], "co-location": x["axes"]["co-location"],
               "spatial": x["axes"]["spatial"],
               "frequency": int(corpus.freq_norm.get(x["root"], 0)),
               "sample": _samp.get(x["root"], ("—", ""))[0],
               "متن آیه با حرکت": _samp.get(x["root"], ("", ""))[1]}
              for ty, lst in rbt.items() for x in lst]
    st.markdown("**Plotted concepts — root ↔ frequency & sample (match the points above):**")
    st.dataframe(_pd.DataFrame(_crows).sort_values(["relation", "frequency"],
                                                   ascending=[True, False]),
                 use_container_width=True, hide_index=True, height=330)
_cm = syn.get("cross_modal", {})
st.caption("divergence: " + str(_cm.get("divergence", "—")) +
           "　·　verified bonds (root∥surface): " + (", ".join(_cm.get("verified_bonds", [])) or "—"))
with st.expander("relation lists (detail)"):
    for ty in ["consensus", "semantic", "co-location", "spatial", "orthogonal", "divergent"]:
        lst = rbt.get(ty) or []
        if not lst:
            continue
        st.markdown(f"**{ty}** — {_REL[ty]}:")
        _show_chips([x["root"] for x in lst], n=8)

layer(2, "MODALITIES IN DETAIL  (tree → forest)")
st.markdown("**Semantic field** — the meaning-bearing neighbourhood:")
_show_chips(fld["semantic_field"])
if fld["cross_view_consensus"]:
    st.markdown("**Robust bonds** — confirmed by ≥2 independent views:")
    _show_chips([b["root"] for b in fld["cross_view_consensus"]])
st.markdown("**Co-location territory** — shares deployment:")
_show_chips(fld["co_location_neighbours"])

layer(3, "CROSS-GRANULARITY VERIFICATION  (root ∥ surface)")
st.markdown("**Verified at BOTH levels** (robust to granularity):")
_show_chips(cg["verified_both_levels"])
c = st.columns(2)
with c[0]:
    st.markdown("**root-level only**")
    _show_chips(cg["root_level_only"])
with c[1]:
    st.markdown("**surface / sense-only**")
    _show_chips(cg["surface_level_only"])

layer(4, "DISTRIBUTION & SPATIAL  (one modality — often null)")
m = st.columns(3)
m[0].metric("frequency", dist["frequency"])
m[1].metric("surahs present", dist["n_surahs_present"])
arch = dist["archetype"]
m[2].metric("archetype", arch["tag"] if arch else "—")
if arch:
    st.markdown(f"**archetype:** {arch['tag']} — {arch['desc']} · stability {arch['stability']}")
st.markdown(f"**Beyond-chance null** (areal evenness vs frequency-matched scramble): "
            f"real I={null['real']}, null {null['null_mean']}±{null['null_sd']}, "
            f"**z={null['z']}** → _{null['interpretation']}_  "
            f"(this is ONE modality; for many concepts it is null — not the headline).")
if dist["hotspot_surahs"]:
    st.markdown("**top surahs by occurrence:** " +
                ", ".join(f"s{su}×{n}" for su, n in dist["hotspot_surahs"][:8]))

if res["senses"]:
    layer(5, "SURFACE-FORM SENSES  (the sense geography)")
    for s in res["senses"][:6]:
        with st.expander(f"{s['form']}   (×{s['count']})"):
            st.markdown("**co-locators:**")
            _show_chips([r for r, a, p in s["share"]], n=6)

mrows = res["morphology"]
if mrows and isinstance(mrows[0], dict) and "error" not in mrows[0]:
    layer(6, "MORPHOLOGY  (attached particles)")
    import pandas as pd
    st.dataframe(pd.DataFrame(mrows), use_container_width=True, hide_index=True)

st.divider()
layer(7, "REPORT  (Word · three registers)")
if st.button("Generate report", type="primary", key="gen_concept"):
    try:
        import report_dive as RP
        _regs = ["technical", "plain_en", "plain_fa"]
        _b = st.progress(0.0, text="Generating report…")
        _docs = {}
        for _i, _reg in enumerate(_regs):
            _b.progress(_i / len(_regs), text=f"Generating {_reg.replace('_', ' ')}…")
            _docs[_reg] = RP.docx_bytes_from_result(res, _reg)
        _b.empty()
        st.session_state["concept_report"] = {"target": target, "docs": _docs}
    except Exception as e:
        st.warning(f"Report generation unavailable: {e}")
_rep = st.session_state.get("concept_report")
if _rep and _rep.get("target") == target:
    dl = st.columns(3)
    for col, (reg, label) in zip(dl, [("technical", "Technical"),
                                      ("plain_en", "Plain English"),
                                      ("plain_fa", "فارسی / Persian")]):
        col.download_button(f"⬇ {label}", _rep["docs"][reg],
                            file_name=f"concept_{target}_{reg}.docx",
                            mime=("application/vnd.openxmlformats-officedocument"
                                  ".wordprocessingml.document"),
                            key=f"dl_concept_{reg}", use_container_width=True)
    st.caption(f"Generated on demand. Matching PDFs come from the local worker: "
               f"`python deep_dive.py concept {target} --reports`.")

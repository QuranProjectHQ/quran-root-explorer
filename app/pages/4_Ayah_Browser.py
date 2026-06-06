"""Ayah Browser — diacritized Quranic text first, then segmented + word-by-word."""
import streamlit as st

from state import (get_corpus, query_controls, compute_all, need_results,
                   hero, layer, highlight_text, render_quranic_verse, per_root_hint, log_page)

st.set_page_config(page_title="Ayah Browser", page_icon="📖", layout="wide")
log_page("ayahs")
corpus = get_corpus()
raw, normalize, top_p, min_w, run = query_controls(corpus)
from state import needs_recompute
if run or needs_recompute():
    compute_all(corpus, raw, normalize, top_p, min_w)
R = need_results()

hero("📖 Ayah Browser",
     "Every matched ayah — full diacritized Quranic text, segmented form, and word-by-word alignment.")
per_root_hint(compact=True)

occ = R["occurrences"]

layer(1, "How many ayahs match")
c1, c2, c3 = st.columns(3)
c1.metric("Total ayah hits", len(occ))
c2.metric("Unique ayahs",
          occ[["Surah #", "Ayah #"]].drop_duplicates().shape[0] if not occ.empty else 0)
c3.metric("Surahs covered", occ["Surah #"].nunique() if not occ.empty else 0)

st.divider()
layer(2, "Filter & search")
c1, c2, c3 = st.columns(3)
with c1:
    root_pick = st.multiselect("Filter by input root", R["input_roots"],
                               default=R["input_roots"], key="ayah_root_pick")
with c2:
    available_surahs = sorted(occ["Surah #"].unique().tolist()) if not occ.empty else []
    surah_pick = st.multiselect("Filter by surah #", available_surahs,
                                default=available_surahs[:30] if len(available_surahs) > 30 else available_surahs,
                                key="ayah_surah_pick")
with c3:
    free_text = st.text_input("Search inside ayah text", key="ayah_search",
                              placeholder="type any Arabic chars…")

filtered = occ.copy()
if root_pick:
    filtered = filtered[filtered["Input Root"].isin(root_pick)]
if surah_pick:
    filtered = filtered[filtered["Surah #"].isin(surah_pick)]
if free_text:
    from analysis import strip_diacritics
    needle = strip_diacritics(free_text)
    filtered = filtered[filtered["Segmented Ayah"].str.contains(needle, na=False)]

st.caption(f"**{len(filtered)}** rows match.")

st.divider()
layer(3, "Summary table")
cols_for_table = ["Input Root", "Surah #", "Ayah #", "Surah Name",
                  "Surface Form(s)"]
if R.get("has_diacritized"):
    cols_for_table.append("Quranic Text (diacritized)")
st.dataframe(filtered[cols_for_table],
             width='content', hide_index=True, height=360)

st.divider()
layer(4, "Read each ayah — diacritized Quranic text + word-by-word")

page_size = st.select_slider("Rows per page", [10, 25, 50, 100], value=10,
                             key="ayah_pgsize")
total_pages = max(1, (len(filtered) + page_size - 1) // page_size)
page = st.number_input("Page", min_value=1, max_value=total_pages,
                       value=1, step=1, key="ayah_page")
start = (page - 1) * page_size
end = start + page_size
page_rows = filtered.iloc[start:end]

sf_for = {q: R["sforms"][R["sforms"]["Input Root"] == q]["Surface Form (col 5)"].tolist()
          for q in R["input_roots"]}

st.markdown("""
<style>
.ayah-grid{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px;}
.ayah-card{border:1px solid #FCBF49;border-radius:10px;padding:8px 12px;background:#FFFEF7;}
.ayah-card .ar{direction:rtl;text-align:right;font-family:'Amiri','Amiri Quran','Noto Naskh Arabic',serif;font-size:18px;line-height:1.55;color:#1B263B;margin:0 0 4px 0;}
.ayah-card .meta{font-size:11px;color:#6B7280;margin:0;}
</style>
""", unsafe_allow_html=True)
cards = []
for _, row in page_rows.iterrows():
    ar = ""
    if R.get("has_diacritized") and row.get("Quranic Text (diacritized)"):
        ar = row["Quranic Text (diacritized)"]
    else:
        ar = row["Segmented Ayah"]
    meta = (f"S{row['Surah #']}·A{row['Ayah #']} · {row['Surah Name']} · "
            f"input: <b>{row['Input Root']}</b> · surface: {row['Surface Form(s)']}")
    cards.append(f"<div class='ayah-card'><div class='ar'>{ar}</div><div class='meta'>{meta}</div></div>")
st.markdown(f"<div class='ayah-grid'>{''.join(cards)}</div>", unsafe_allow_html=True)

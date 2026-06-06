# -*- coding: utf-8 -*-
"""Provenance: regenerate the app's own ظلم surface-forms donut as a high-res PNG.
Imports the Quran Root Explorer's modules directly (no re-implementation).
Requires kaleido==0.2.1 (bundles its own renderer; no system Chrome needed)."""
import os, sys
APP = os.environ.get("QRE_APP_DIR",
    "/sessions/practical-intelligent-noether/mnt/Downloads/Quran_Root_Explorer_Web_v1.2")
sys.path.insert(0, APP)
import analysis as A, plotly_charts as PC
HERE = os.path.dirname(os.path.abspath(__file__))
corpus = A.load_corpus(os.path.join(APP, "Book6.xlsx"))
ir = A.parse_input_roots("ظلم", True); root = ir[0]
sf = A.surface_form_table(corpus, ir, True)
PC.chart_surface_form_sunburst(sf, root).write_image(
    os.path.join(HERE, "app_zulm_surface_forms.png"), width=900, height=560, scale=2)
print("wrote app_zulm_surface_forms.png")

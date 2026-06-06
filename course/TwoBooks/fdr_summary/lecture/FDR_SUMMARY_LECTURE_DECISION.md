# Two Books · FDR Summary lecture — DECISION DOC (for sign-off)

Per COURSE_STANDARDS §1 and §16a. This is the CAPSTONE of the Two Books series: it
collects one representative permutation test from every Two Books domain into a single
Benjamini–Hochberg correction, so no single p-value is read in isolation. Companion to
the live 📋 Two Books · Global FDR page. Every p computed live from Book6.

**Theme:** multiple-testing discipline. Run many permutation tests across the three pages
(Disjoint Letters · Signal · Biology) and two readings, then correct the whole battery for
multiplicity. The lecture teaches WHY correction is necessary and reads the corrected
verdict honestly.

**The battery (8 representative tests) and live BH-FDR result:**

| test (domain) | raw p | BH q | 5% FDR |
|---|---|---|---|
| Contiguity · muṣḥaf (Position) | 0.0005 | 0.0010 | ✓ |
| Contiguity · nuzūl (Position) | 0.0005 | 0.0010 | ✓ |
| Length autocorrelation (Signal) | 0.0005 | 0.0010 | ✓ |
| Root-entropy special (Semantic) | 0.0005 | 0.0010 | ✓ |
| Letter-entropy special (Sequence) | 0.002 | 0.0032 | ✓ |
| Di-codon adjacency (Biology) | 0.005 | 0.0067 | ✓ |
| Shared theme per tag (Semantic) | 0.049 | 0.056 | ✗ |
| Shared length per tag (Position) | 0.289 | 0.289 | ✗ |

**6 of 8 survive 5% FDR.**

**Modules (8 beats each; beat 6 = real Book6 datum):**
1. Frame — why a cross-domain summary; the danger of cherry-picking one p.
2. The multiplicity problem — run enough tests and some cross 0.05 by chance.
3. Benjamini–Hochberg — rank the p's, compare each to (i/m)·α; control the false-discovery rate.
4. The battery — one representative test per domain, across Position/Sequence/Semantic + Signal + Biology.
5. The survivors — 6 of 8 clear 5% FDR (q ≤ 0.0067).
6. The casualties — shared theme (p 0.049 → q 0.056) and shared length (p 0.289) drop out.
7. Cross-domain reading — the structure is robust across two independent readings and three pages.
8. Synthesis — one corrected dashboard; what the whole Two Books series licenses.

**Honest spine:** after a single Benjamini–Hochberg correction, the geometric and
compositional structure of the corpus is ROBUST across every domain (6/8 survive), while the
borderline shared-theme claim correctly drops out once multiplicity is controlled. Crucial
caveat — stated on the page itself: FDR controls for MULTIPLICITY, **not** for the
sūra-length confound; a surviving test is reproducible, not a miracle. No miracle claims.

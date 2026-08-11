# PP-0183 — PD-L1 Testing
## Knowledge Passport

## 1. Identity

| Field | Value |
|---|---|
| PP ID | PP-0183 |
| Clinical Topic | PD-L1 Testing |
| Domain | Gastric adenocarcinoma — biomarker testing |
| Package role | Foundational PD-L1 testing package |
| Version | 1.0.0 |
| Lifecycle status | GOLD — READY FOR INTEGRATION |
| Audience | Patients, caregivers, clinicians, knowledge-retrieval systems |
| Core question | What is PD-L1 testing, why is it performed, how is it assessed, and how can the result affect immunotherapy selection? |

## 2. Knowledge Classification

**Primary classification:** Diagnostic / Biomarker Testing / Predictive Treatment Selection

**Secondary classifications:**
- Molecular pathology
- Precision oncology
- Immunotherapy biomarker
- Patient education
- Pathology-result interpretation

The package is not a treatment-regimen package and not a detailed assay-methodology package.

## 3. Patient Journey Classification

**Primary journey position:**

Diagnosis → Pathology confirmation → Biomarker testing → Treatment selection

**Typical clinical transition:**

Gastric adenocarcinoma diagnosed
→ tissue available
→ biomarker work-up
→ PD-L1 testing
→ CPS/TAP result
→ integration with HER2/MSI/MMR/CLDN18.2 and clinical setting
→ treatment discussion

## 4. Intended Runtime Usage

The package should be retrieved when a user asks:

- What is PD-L1?
- Why do I need PD-L1 testing?
- When should PD-L1 be tested?
- What sample is used?
- What is PD-L1 IHC?
- What is CPS?
- What does CPS 0 or CPS ≥1 mean?
- Why does CPS ≥5 matter?
- What is TAP?
- Does PD-L1 positive mean immunotherapy will work?
- Does PD-L1 negative mean immunotherapy is impossible?
- How does PD-L1 differ from HER2 or MSI/MMR?
- How should a patient understand a PD-L1 report?

Do not use this package as the sole source for individualized treatment selection or drug-specific immunotherapy recommendations.

## 5. Retrieval / Runtime Relevance

### High-priority retrieval concepts

- PD-L1
- PD-L1 testing
- gastric cancer PD-L1
- IHC
- FFPE
- CPS
- Combined Positive Score
- CPS ≥1
- CPS ≥5
- TAP
- PD-1/PD-L1 inhibitor
- companion diagnostic
- tumor tissue
- biomarker testing
- immunotherapy selection

### Negative retrieval / boundary cues

If the user asks primarily about:
- PD-L1 molecular signaling → retrieve PD-L1 Biology.
- technical IHC procedure → retrieve PD-L1 IHC Testing.
- detailed CPS/TAP scoring → retrieve PD-L1 CPS Scoring.
- drug/regimen selection → retrieve Immune Checkpoint Inhibitors / PP-0215.
- MSI/MMR → retrieve PP-0182.
- HER2 → retrieve PP-0181.
- CLDN18.2 → retrieve PP-0184.

## 6. Clinical Scope

### Core

- Purpose of PD-L1 testing.
- Current NCCN v2.2026 testing context.
- FFPE tumor tissue.
- PD-L1 IHC.
- Qualitative anti-PD-L1 antibody-based assessment.
- Adequacy and minimum tumor-cell concept.
- Companion diagnostic context.
- CPS.
- CPS ≥1.
- Treatment-contextual higher thresholds including CPS ≥5.
- TAP contextual interpretation.
- Positive/negative/inadequate result interpretation.
- Predictive versus prognostic distinction.
- Multi-biomarker context.
- Patient-facing limitations.

### Supporting

- PD-1/PD-L1 checkpoint concept.
- PD-L1 association with selected molecular/clinicopathologic characteristics.
- EBV relationship as context.
- Histologic/molecular subgroup context.
- Current perioperative and advanced-disease treatment-selection examples at conceptual level.

### Explicitly excluded

- Detailed PD-L1 molecular biology.
- Detailed signaling.
- Detailed IHC laboratory methodology.
- Clone-specific protocols.
- Assay validation.
- Detailed CPS/TAP technical scoring.
- Detailed TPS methodology.
- Drug dosing and administration.
- Immunotherapy toxicity.
- Individualized treatment recommendations.
- Detailed HER2/MSI/MMR/CLDN18.2 testing methodology.
- Germline testing.
- NGS workflow.

## 7. Authoritative Sources

### Primary

1. **NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026**
   - PD-L1 testing principles.
   - FFPE tissue.
   - IHC.
   - minimum 100 tumor cells.
   - CPS definition.
   - CPS ≥1.
   - CPS/TAP relationship.
   - treatment-selection context.

### Supporting

2. NCI gastric-cancer treatment PDQ.
3. ACS immunotherapy material for stomach cancer.
4. ESMO/ASCO Global Curriculum 2023.
5. Supplied gastric-cancer clinical source set.

## 8. Evidence Classification

### Established / guideline-supported

- PD-L1 IHC on tumor tissue.
- FFPE specimen.
- Companion-diagnostic concept.
- CPS.
- CPS ≥1 as PD-L1 expression threshold in the NCCN framework.
- Current testing recommendation for newly diagnosed patients who are candidates for PD-1/PD-L1 inhibitor therapy.
- Context-specific use of PD-L1 results in treatment selection.

### Context-dependent

- CPS ≥5.
- TAP.
- Specific treatment-regimen thresholds.
- Associations with EBV and clinicopathologic features.

### Uncertain

- Standalone prognostic significance.
- Universal ability of PD-L1 to predict response.
- Universal interchangeability of scoring systems outside specified contexts.

## 9. Knowledge Graph

### Upstream

PP-0014 Immunotherapy
→ PP-0015 Biomarker Testing
→ PP-0183 PD-L1 Testing

### Parallel biomarker nodes

PP-0181 HER2 Testing
PP-0182 MSI/MMR Testing
PP-0184 CLDN18.2 Testing
PP-0185 TMB
PP-0186 FGFR2 Testing
PP-0187 NGS Biomarker Testing

### Downstream

PP-0183
→ PD-L1 Biology
→ PD-L1 CPS Scoring
→ PD-L1 IHC Testing
→ Companion Diagnostics
→ Immune Checkpoint Inhibitors
→ PP-0215 PD-L1-guided Immunotherapy

## 10. Governance Metadata

| Governance item | Status |
|---|---|
| Source-first verification | PASS |
| Registry verification | PASS |
| Adjacent overlap review | PASS |
| Decision Batch | APPROVED / LOCKED |
| Gold specification | Applied |
| Full-depth rule | Applied |
| Boundary | Required and declared in production response |
| QA | Four-layer QA |
| Integration readiness | Ready |

## 11. Version Control

**Semantic version:** 1.0.0

### Update triggers

A review should be initiated when:
- NCCN changes PD-L1 testing recommendations.
- CPS or TAP definitions change.
- New companion diagnostics materially alter testing requirements.
- New guideline thresholds change treatment-selection interpretation.
- A major assay/scoring standard changes.
- The delegated PD-L1 scoring or IHC packages are formally revised in a way that changes this package's boundary.

## 12. Clinical Safety Rules

1. Never state that PD-L1 positivity guarantees immunotherapy response.
2. Never state that PD-L1 negativity universally excludes immunotherapy.
3. Never equate CPS with simple tumor-cell percentage.
4. Never equate an inadequate specimen with a negative result.
5. Never use a single CPS threshold as a universal treatment algorithm.
6. Never substitute PD-L1 testing for HER2, MSI/MMR or CLDN18.2 testing.
7. Never use PD-L1 alone to provide an individualized treatment recommendation.
8. Use current NCCN v2.2026 as the primary guideline anchor when current recommendations conflict with older wording.

## 13. Boundary Metadata

**Core:** PD-L1 testing purpose, timing, specimen, IHC concept, adequacy, CPS interpretation, current TAP context, result interpretation, predictive/treatment-selection relevance, and patient-facing limitations.

**Supporting:** foundational checkpoint biology, molecular/clinicopathologic associations, EBV context, and treatment-setting examples.

**Explicitly Excluded:** detailed biology, laboratory workflow, scoring methodology, treatment regimens, toxicity, individualized recommendations, and detailed other-biomarker methodologies.

**Delegated-to PP:** PD-L1 Biology, PD-L1 CPS Scoring, PD-L1 IHC Testing, Companion Diagnostics, Immune Checkpoint Inhibitors, PP-0181, PP-0182, PP-0184, PP-0191, PP-0215.

## 14. Final Status

**GOLD — READY FOR INTEGRATION**

# PP-0183 — PD-L1 Testing

## 1. Metadata

| Field | Value |
|---|---|
| PP ID | PP-0183 |
| Title | PD-L1 Testing |
| Clinical domain | Molecular / Biomarker Testing |
| Population | Patients with gastric adenocarcinoma |
| Package type | Patient-facing Clinical Knowledge Object |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Primary guideline anchor | NCCN Gastric Cancer Version 2.2026 |
| Supporting source set | NCI PDQ, ACS, ESMO/ASCO curriculum and supplied gastric-cancer source set |
| Upstream prerequisites | PP-0014 Immunotherapy for Gastric Adenocarcinoma; PP-0015 Biomarker Testing for Gastric Adenocarcinoma |
| Adjacent packages | PP-0181 HER2 Testing; PP-0182 MSI/MMR Testing; PP-0184 CLDN18.2 Testing |
| Downstream / delegated packages | PD-L1 Biology; PD-L1 CPS Scoring; PD-L1 IHC Testing; Companion Diagnostics; Immune Checkpoint Inhibitors; PP-0191 Biomarker Testing for Immunotherapy; PP-0215 PD-L1-guided Immunotherapy |

## 2. Educational Objective

This package answers one patient-centered clinical question:

> **What is PD-L1 testing in gastric adenocarcinoma, why is it performed, when is it needed, how is it assessed, what does the result mean, and how can it affect immunotherapy treatment selection?**

The package is intentionally testing-focused. It explains the clinical meaning of the biomarker result without becoming a detailed laboratory manual, immunotherapy-treatment algorithm, or molecular-biology package.

## 3. Scope

### Included

- PD-L1 as a tumor biomarker and the conceptual PD-1/PD-L1 checkpoint relationship.
- The purpose of PD-L1 testing.
- The current NCCN v2.2026 testing context for newly diagnosed gastric-cancer patients who are candidates for PD-1/PD-L1 inhibitor treatment.
- Tumor tissue and FFPE specimen concepts.
- PD-L1 immunohistochemistry (IHC) as the guideline-described testing modality.
- Anti-PD-L1 antibody-based qualitative assessment.
- Specimen adequacy, including the minimum of 100 tumor cells stated by NCCN.
- Companion-diagnostic and qualified-laboratory context.
- Combined Positive Score (CPS).
- Conceptual CPS calculation and interpretation.
- CPS 0, CPS ≥1, and higher treatment-contextual thresholds such as CPS ≥5.
- Tumor Area Positivity (TAP) as a current 2026 supporting scoring context.
- Distinction between CPS/TAP and TPS.
- Interpretation of positive, negative/low, and inadequate/unevaluable results.
- Predictive/treatment-selection relevance.
- Uncertainty around standalone prognostic significance.
- Relationship with other gastric-cancer biomarkers including HER2, MSI/MMR, CLDN18.2 and EBV at a contextual level.
- Patient-facing limitations and common misconceptions.

### Not Included

Detailed molecular PD-L1 biology, detailed IHC laboratory workflow, assay validation, detailed CPS/TAP scoring methodology, drug-specific immunotherapy algorithms, dosing, toxicity management, individualized treatment decisions, or detailed methodology for other biomarkers.

## 4. Clinical Knowledge Blocks

### CKB-01 — What is PD-L1?

PD-L1 is a protein that can be expressed on tumor cells and immune cells. PD-L1 participates in the PD-1/PD-L1 immune-checkpoint pathway. In gastric cancer, its expression can be measured in tumor tissue and used as a biomarker relevant to selected immunotherapy decisions.

**Patient explanation:** PD-L1 is not a blood marker and is not itself a mutation test. The usual gastric-cancer assessment described by NCCN measures PD-L1 protein expression in tumor tissue using IHC.

### CKB-02 — Why can PD-L1 matter in gastric cancer?

The PD-1/PD-L1 pathway can reduce T-cell activity. Some cancers exploit this pathway to avoid immune attack. Immune-checkpoint inhibitors can interfere with this interaction. PD-L1 testing therefore provides information that may help identify patients for whom selected PD-1/PD-L1 inhibitor strategies are appropriate.

This does not mean that PD-L1 is a guarantee of response.

### CKB-03 — What is the purpose of testing?

The purpose is primarily treatment selection and biomarker characterization. NCCN v2.2026 states that universal PD-L1 testing should be performed for newly diagnosed patients with gastric cancer who are candidates for treatment with PD-1 or PD-L1 inhibitors.

The result becomes one component of the treatment-planning evidence base.

### CKB-04 — When is PD-L1 testing relevant?

Testing should be available early enough to inform treatment planning when checkpoint-inhibitor therapy may be considered. Current NCCN guidance also contains selected perioperative and advanced/recurrent/metastatic contexts in which PD-L1-related thresholds affect treatment recommendations.

The package must not reduce PD-L1 testing to a metastatic-only concept.

### CKB-05 — What specimen is used?

NCCN describes PD-L1 assessment on formalin-fixed paraffin-embedded (FFPE) tumor tissue. Suitable tumor material may originate from diagnostic or surgical tissue, provided the specimen is adequate for the assay.

This package does not replace the separate biopsy-strategy or endoscopic-diagnosis packages.

### CKB-06 — How is PD-L1 measured?

The NCCN biomarker section describes a qualitative IHC assay using anti-PD-L1 antibodies to detect PD-L1 protein in FFPE gastric adenocarcinoma tissue.

IHC is therefore the core testing concept.

Detailed antibody-clone selection, staining protocols, analytic validation, controls, troubleshooting and laboratory workflow are delegated to PD-L1 IHC Testing.

### CKB-07 — Why does specimen adequacy matter?

NCCN states that at least 100 tumor cells must be present on the PD-L1-stained slide for the specimen to be considered adequate for PD-L1 evaluation.

This creates an important patient-facing distinction:

> **An inadequate specimen is not the same as a valid PD-L1-negative result.**

### CKB-08 — What is a companion diagnostic?

NCCN states that a companion diagnostic test should be used on FFPE tissue as an aid in identifying patients for treatment with PD-1/PD-L1 inhibitors, and that PD-L1 testing should be performed in CLIA-approved laboratories.

At patient level, a companion diagnostic is a test linked to a treatment decision. Detailed regulatory and assay-specific companion-diagnostic science is delegated.

### CKB-09 — What is CPS?

The Combined Positive Score (CPS) is the principal PD-L1 scoring concept described by NCCN for gastric cancer.

Conceptually:

**CPS = PD-L1-staining tumor cells + PD-L1-staining relevant immune cells, divided by total viable tumor cells, multiplied by 100.**

The important point is that CPS is not simply the percentage of tumor cells that stain for PD-L1.

### CKB-10 — Which cells contribute to CPS?

NCCN describes the numerator as PD-L1-staining cells, including:

- tumor cells;
- lymphocytes;
- macrophages.

The denominator is the total number of viable tumor cells evaluated.

The exact technical scoring process belongs to PD-L1 CPS Scoring.

### CKB-11 — What does CPS ≥1 mean?

NCCN considers a specimen to have PD-L1 expression when CPS is ≥1.

This is a biomarker interpretation threshold. It does not independently prescribe treatment.

### CKB-12 — Why can CPS ≥5 also appear?

Different treatment strategies can use different PD-L1 thresholds. NCCN v2.2026 includes contexts in which CPS ≥5 is associated with stronger evidence or treatment relevance, while CPS ≥1 is used in other contexts.

Therefore there is no single universal statement of the form:

> “CPS above one number always means immunotherapy.”

The treatment-specific meaning is delegated to immunotherapy and PD-L1-guided treatment packages.

### CKB-13 — What is TAP?

Tumor Area Positivity (TAP) is another PD-L1-related scoring approach recognized in the current NCCN context. NCCN states that CPS and TAP have high concordance and may be interchangeable in specified circumstances, including identification of patients likely to benefit from selected therapies such as tislelizumab-jsgr or durvalumab.

TAP is included here only as a current interpretive context. Detailed TAP methodology belongs to PD-L1 CPS/Scoring or PD-L1 IHC specialist packages.

### CKB-14 — What about TPS?

Tumor Proportion Score (TPS) may appear in research or trial literature. NCCN notes that TPS is not included as the principal scoring framework in its gastric-cancer guideline.

Patients should therefore not assume that every PD-L1 score uses the same scoring system.

### CKB-15 — What does a PD-L1-positive result mean?

A positive result means that PD-L1 expression meets the relevant assay/scoring definition. In gastric cancer, the result may support consideration of selected PD-1/PD-L1 inhibitor strategies.

It does not mean that treatment will definitely work.

### CKB-16 — What does a low or negative result mean?

A result below a treatment-relevant threshold indicates that PD-L1 expression does not meet that threshold.

It does not mean:

- the tumor has no PD-L1 molecules at all;
- the patient has no possible treatment options;
- immunotherapy is universally impossible;
- the tumor is biologically incapable of immune interaction.

The clinical consequence depends on the treatment context.

### CKB-17 — What does an inadequate result mean?

If the specimen is not adequate for valid interpretation, the result should not be treated as a biologically negative result.

NCCN's minimum tumor-cell requirement is therefore clinically important.

### CKB-18 — Is PD-L1 a predictive or prognostic biomarker?

Its most established role in this package is predictive/treatment-selection related.

NCCN states that the prognostic significance of PD-L1 in gastric cancer remains unclear. Studies have reported favorable, unfavorable and null associations.

Therefore PD-L1 should not be presented as a simple standalone prognosis marker.

### CKB-19 — How does PD-L1 relate to MSI/MMR?

PD-L1 and MSI/MMR are different biomarkers. A gastric tumor can have PD-L1 expression, MSI-H/dMMR, both, or neither.

They may both contribute to immunotherapy selection, but the tests answer different biological questions.

Detailed MSI/MMR testing is owned by PP-0182.

### CKB-20 — How does PD-L1 relate to HER2?

HER2 is a separate biomarker used for HER2-directed treatment selection. PD-L1 testing does not replace HER2 testing.

Detailed HER2 testing is owned by PP-0181.

### CKB-21 — How does PD-L1 relate to CLDN18.2?

CLDN18.2 is a separate biomarker with a distinct testing and treatment pathway. PD-L1 status does not substitute for CLDN18.2 assessment.

Detailed CLDN18.2 testing is owned by PP-0184.

### CKB-22 — How does PD-L1 relate to EBV?

NCCN and the supplied source set describe associations between PD-L1 expression and certain molecular/clinicopathologic characteristics, including EBV-positive tumors. This is contextual rather than a replacement for EBV testing.

Detailed EBV-associated gastric cancer and EBV testing are owned by PP-0168.

### CKB-23 — Does a high CPS guarantee immunotherapy benefit?

No. PD-L1 is an imperfect predictive biomarker. A higher score may be clinically relevant in particular treatment contexts, but it does not guarantee response.

### CKB-24 — Does a negative PD-L1 result rule out all immunotherapy?

No. Treatment relevance depends on the specific regimen, disease setting, other biomarkers and clinical factors.

### CKB-25 — Does PD-L1 testing replace tissue diagnosis?

No. PD-L1 testing is a biomarker assessment performed on tumor tissue. It does not establish the diagnosis of gastric adenocarcinoma by itself.

### CKB-26 — Does PD-L1 testing replace other biomarkers?

No. Gastric-cancer precision treatment may require multiple independent biomarkers, including HER2, MSI/MMR, CLDN18.2 and PD-L1.

### CKB-27 — How should a patient read a PD-L1 report?

A patient should identify:

1. specimen and adequacy;
2. assay/IHC context;
3. scoring system used;
4. CPS or other reported score;
5. whether the score meets the clinically relevant threshold;
6. whether the result is being used for a specific treatment decision;
7. whether other biomarkers also need to be considered.

The report should be interpreted together with the treatment setting rather than in isolation.

## 5. Common Misconceptions

### Myth 1 — “PD-L1 is a mutation.”
**Fact:** PD-L1 testing in this context measures protein expression, typically by IHC.

### Myth 2 — “PD-L1 is a blood test.”
**Fact:** The NCCN-described gastric-cancer assessment uses tumor tissue, including FFPE tissue.

### Myth 3 — “CPS is just the percentage of tumor cells that are positive.”
**Fact:** CPS incorporates PD-L1-staining tumor cells and relevant immune cells relative to viable tumor cells.

### Myth 4 — “CPS ≥1 means immunotherapy is mandatory.”
**Fact:** CPS informs treatment selection; it does not independently prescribe treatment.

### Myth 5 — “CPS ≥5 is the definition of PD-L1 positivity.”
**Fact:** NCCN defines PD-L1 expression at CPS ≥1; higher thresholds can have treatment-specific significance.

### Myth 6 — “High CPS guarantees response.”
**Fact:** PD-L1 is an imperfect predictive biomarker.

### Myth 7 — “PD-L1 negative means no immunotherapy is possible.”
**Fact:** Treatment eligibility depends on the specific regimen, setting and other factors.

### Myth 8 — “PD-L1 positive means the cancer has a worse prognosis.”
**Fact:** Standalone prognostic significance remains uncertain.

### Myth 9 — “PD-L1 replaces MSI/MMR.”
**Fact:** They are different biomarkers.

### Myth 10 — “PD-L1 replaces HER2 or CLDN18.2 testing.”
**Fact:** These are separate biomarker pathways.

### Myth 11 — “Inadequate tissue means PD-L1 negative.”
**Fact:** Inadequate testing is not a valid negative biomarker result.

### Myth 12 — “Every PD-L1 score uses the same scoring system.”
**Fact:** CPS is the core gastric-cancer framework in NCCN, while TAP and TPS have distinct contexts.

## 6. Key Messages

1. PD-L1 testing is a tumor-tissue biomarker test used mainly to inform selected immunotherapy decisions.
2. NCCN v2.2026 describes PD-L1 testing for newly diagnosed gastric-cancer patients who are candidates for PD-1/PD-L1 inhibitor treatment.
3. The core test is PD-L1 IHC on FFPE tumor tissue.
4. CPS is the principal gastric-cancer PD-L1 scoring concept.
5. CPS is not simply tumor-cell staining percentage.
6. NCCN defines PD-L1 expression at CPS ≥1.
7. Higher thresholds such as CPS ≥5 can have different treatment-specific relevance.
8. TAP is a current 2026 supporting scoring context in specified treatment settings.
9. An inadequate specimen is not the same as a negative result.
10. PD-L1 is not a standalone guarantee of immunotherapy benefit or prognosis.
11. PD-L1 testing complements, rather than replaces, other biomarker tests.
12. Final treatment decisions require integration of the PD-L1 result with disease setting, regimen and other clinical/biomarker information.

## 7. Clinical Importance

PD-L1 testing is important because modern gastric-cancer treatment can be biomarker guided. A PD-L1 result can alter the set of immunotherapy strategies that are considered, but the result must be interpreted within the exact treatment context.

The current NCCN v2.2026 framework is especially important because it includes both broad testing recommendations and context-specific CPS/TAP thresholds.

## 8. Knowledge Graph

### Prerequisites

- PP-0014 — Immunotherapy for Gastric Adenocarcinoma
- PP-0015 — Biomarker Testing for Gastric Adenocarcinoma
- PP-0007 — Understanding Your Pathology Report
- PP-0177 — Endoscopic Biopsy Strategy

### Related

- PP-0180 — Gastric Cancer Molecular Classification
- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0184 — CLDN18.2 Testing
- PP-0185 — Tumor Mutational Burden
- PP-0187 — NGS Biomarker Testing
- PP-0191 — Biomarker Testing for Immunotherapy

### Downstream / delegated

- PD-L1 Biology
- PD-L1 CPS Scoring
- PD-L1 IHC Testing
- Companion Diagnostics
- Immune Checkpoint Inhibitors
- PP-0215 — PD-L1-guided Immunotherapy

## 9. Patient Explanation

> **PD-L1 testing is a test performed on a sample of your gastric-cancer tissue to measure a protein called PD-L1. The result can help your cancer team decide whether certain immunotherapy treatments may be appropriate. The test is usually performed by immunohistochemistry (IHC), and the result may be reported as a Combined Positive Score (CPS). A higher or positive score can be relevant to some treatment choices, but it does not guarantee that immunotherapy will work. The result also does not replace other important tests such as HER2 or MSI/MMR testing.**

## 10. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold package after approved/locked PP-0183 Decision Batch. |

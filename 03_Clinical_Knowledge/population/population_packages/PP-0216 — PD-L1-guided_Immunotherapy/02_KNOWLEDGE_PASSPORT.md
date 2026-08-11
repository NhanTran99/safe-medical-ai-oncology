# 02_KNOWLEDGE_PASSPORT — PP-0216 PD-L1-guided Immunotherapy

## 1. Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0216 |
| PP ID | PP-0216 |
| Title | PD-L1-guided Immunotherapy |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Last Updated | 2026-08-09 |

---

# 2. Knowledge Classification

## Clinical Domain

Gastric adenocarcinoma → Biomarker-guided immunotherapy → Treatment selection.

## Primary Clinical Question

> What does a PD-L1 result mean for immunotherapy treatment in gastric cancer?

## Knowledge Type

Clinical educational knowledge object.

## Package Function

Biomarker-to-treatment interpretation.

This package is positioned after PD-L1 testing and before downstream treatment-specific, response-assessment and safety packages.

## Educational Level

Patient-facing with clinically precise terminology.

## Clinical Complexity

High.

The topic requires understanding of:

- PD-L1;
- CPS;
- threshold-dependent evidence;
- HER2 interaction;
- MSI-H/dMMR independence;
- treatment setting;
- trial interpretation;
- guideline positioning;
- limitations.

## Patient Journey Stage

Primarily:

**Treatment selection**

with interfaces to:

- biomarker testing;
- treatment initiation;
- treatment response;
- toxicity;
- shared decision-making.

---

# 3. Intended Runtime Usage

## Primary Runtime Uses

1. Explain the clinical meaning of a PD-L1 result.
2. Help a patient understand CPS.
3. Explain why different CPS thresholds can matter.
4. Explain why PD-L1 is not a guarantee of response.
5. Connect PD-L1 to checkpoint-inhibitor treatment evidence.
6. Prevent interpretation of PD-L1 as a stand-alone prescription.
7. Explain interaction with HER2 and MSI-H/dMMR.
8. Support patient questions before an oncology consultation.
9. Provide structured retrieval for PD-L1-guided treatment concepts.
10. Preserve the boundary between biomarker testing and treatment application.

## Retrieval Intent

Use when a user asks:

- “What does my PD-L1 CPS mean?”
- “Why does CPS 1 matter?”
- “Why does CPS 5 matter?”
- “Does PD-L1 decide immunotherapy?”
- “Can I receive immunotherapy if PD-L1 is low?”
- “Why is PD-L1 checked with HER2?”
- “Why is MSI/MMR also tested?”
- “What is the difference between CPS 1 and CPS 5?”
- “Does high PD-L1 mean immunotherapy will work?”

---

# 4. Clinical Scope

## Core Knowledge Units

### KU-01
PD-L1 as a treatment-selection biomarker.

### KU-02
CPS as the principal gastric-cancer PD-L1 scoring concept.

### KU-03
Clinical meaning of CPS ≥1.

### KU-04
Clinical meaning of CPS ≥5.

### KU-05
Selected CPS ≥10 trial context.

### KU-06
PD-L1-guided first-line therapy in advanced disease.

### KU-07
HER2-positive + PD-L1-guided treatment.

### KU-08
HER2-negative + PD-L1-guided treatment.

### KU-09
Landmark evidence:
- CheckMate-649;
- KEYNOTE-062;
- KEYNOTE-811;
- KEYNOTE-859;
- RATIONALE-305 / tislelizumab context.

### KU-10
Selected perioperative PD-L1-guided context.

### KU-11
PD-L1 and MSI-H/dMMR as parallel biomarker pathways.

### KU-12
PD-L1 and multi-biomarker treatment selection.

### KU-13
Patient-facing interpretation and limitations.

### KU-14
Common misconceptions and clinical safety.

---

# 5. Evidence Classification

## Established / Guideline-supported

- PD-L1 is clinically relevant to selected gastric-cancer immunotherapy strategies.
- CPS is a key gastric-cancer PD-L1 scoring framework.
- Current NCCN Version 2.2026 uses CPS ≥1 for selected first-line checkpoint-inhibitor combinations.
- Several current regimens have category 1 positioning at CPS ≥5.
- PD-L1-guided checkpoint inhibition is strongly anchored in advanced/unresectable/recurrent/metastatic treatment.
- HER2-positive disease can incorporate PD-L1-guided pembrolizumab treatment.
- HER2-negative disease has several PD-L1-guided checkpoint-inhibitor + chemotherapy options.
- MSI-H/dMMR can define an immunotherapy-relevant pathway independent of PD-L1.
- PD-L1 is not an individual response guarantee.

## Context-dependent

- Exact treatment regimen.
- Exact threshold.
- Monotherapy versus combination.
- HER2-positive versus HER2-negative context.
- First-line versus later-line treatment.
- Perioperative application.
- TAP versus CPS.
- Regulatory indication.
- Prior ICI exposure.

## Emerging / Uncertain

- Optimal use of PD-L1 in evolving perioperative strategies.
- Interpretation of borderline values across different regimens.
- Dynamic changes in PD-L1 during treatment.
- Whether repeat testing should routinely change treatment.
- Use of PD-L1 alone for post-ICI treatment sequencing.

---

# 6. Authoritative Sources

## Primary Current Guideline

**NCCN Gastric Cancer Version 2.2026**

Primary authority for:

- current PD-L1 testing framework;
- CPS;
- TAP;
- current first-line treatment positioning;
- CPS thresholds;
- HER2-positive and HER2-negative pathways;
- MSI-H/dMMR independence from PD-L1;
- selected perioperative context.

## Primary Evidence Synthesis

**NCI Gastric Cancer Treatment PDQ**

Used for:

- CheckMate-649;
- KEYNOTE-062;
- clinical trial interpretation;
- evidence-level context.

## Supporting Patient-facing Source

**American Cancer Society — Immunotherapy for Stomach Cancer**

Used for:

- basic checkpoint-inhibitor mechanism;
- patient-facing immunotherapy concepts;
- selected perioperative context.

## Governance / Architecture Sources

- CORE_WORKING_RULES v1.7
- FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1
- PP Registry.xlsx
- approved Discussion Gold reference
- approved Gold artifact references

---

# 7. Governance Metadata

| Field | Value |
|---|---|
| Governance Authority | CORE_WORKING_RULES |
| Structural Authority | FREEZE GOLD POPULATION PACKAGE SPECIFICATION |
| Discussion Authority | Approved PP Discussion Gold reference |
| Clinical Evidence Authority | Supplied project clinical Source Files |
| Execution Authority | Project Coordinator explicit PP request |
| Gold Depth Rule | Absolute; reference is minimum |
| Production Status | GOLD |
| QA Status | PASS |
| Repository Status | READY FOR INTEGRATION |

The governance framework requires Source-First retrieval, explicit overlap checking and immediate four-artifact production after approval/lock.

---

# 8. Knowledge Graph

## Prerequisite

- PP-0014 Immunotherapy for Gastric Adenocarcinoma
- PP-0015 Biomarker Testing for Gastric Adenocarcinoma
- PP-0016 HER2 Testing for Gastric Adenocarcinoma
- PP-0017 PD-L1 Testing for Gastric Adenocarcinoma
- PP-0181 HER2 Testing
- PP-0182 MSI/MMR Testing
- PP-0183 PD-L1 Testing
- PP-0192 Biomarker Testing for Immunotherapy
- PP-0213 Immunotherapy in Gastric Cancer
- PP-0214 Immune Checkpoint Inhibitors
- PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy

## Related

- PP-0208 Palliative Systemic Therapy
- PP-0209 Targeted Therapy in Gastric Cancer
- PP-0210 HER2-targeted Therapy
- PP-0211 CLDN18.2-targeted Therapy
- PP-0212 Anti-angiogenic Therapy
- PP-0217 Response Assessment
- PP-0218 RECIST-based Assessment
- PP-0219 Post-treatment Imaging
- PP-0231 Treatment-related Toxicity and Supportive Care
- TMB and molecular biomarker packages

## Downstream

- checkpoint-inhibitor treatment-specific packages;
- response-assessment packages;
- immune-related toxicity packages;
- recurrent/metastatic treatment packages;
- treatment-sequencing/resistance packages.

---

# 9. Boundary Map

## Upstream

**PP-0183 — PD-L1 Testing**

Answers:

> How is PD-L1 assessed and what does the laboratory result report?

## This Package

**PP-0216 — PD-L1-guided Immunotherapy**

Answers:

> What does the PD-L1 result mean for immunotherapy treatment?

## Parallel Biomarker Branch

**PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy**

Answers:

> What does MSI-H/dMMR mean for immunotherapy?

The MSI-H/dMMR pathway may operate independently of PD-L1.

## Adjacent Treatment Branches

- PP-0210 HER2-targeted Therapy
- PP-0211 CLDN18.2-targeted Therapy
- PP-0212 Anti-angiogenic Therapy
- PP-0213 Immunotherapy in Gastric Cancer
- PP-0214 Immune Checkpoint Inhibitors

---

# 10. Safety / Runtime Rules

1. Never convert CPS into an individualized response probability.
2. Never state that PD-L1 positivity guarantees benefit.
3. Never state that PD-L1 negativity universally excludes immunotherapy.
4. Never use a CPS threshold from one trial as a universal treatment rule.
5. Always distinguish PD-L1 testing from PD-L1-guided treatment application.
6. Consider MSI-H/dMMR as an independent immunotherapy-relevant pathway.
7. Integrate HER2 and other treatment-relevant biomarkers.
8. Avoid individualized prescribing.
9. Do not provide drug dosing from this package.
10. Do not replace current clinical guidance with this educational package.

---

# 11. Runtime Terminology

| Term | Runtime Meaning |
|---|---|
| PD-L1 | Immune-regulatory ligand used as a treatment-selection biomarker in selected contexts |
| CPS | Combined Positive Score |
| CPS ≥1 | Important treatment-relevant threshold in selected current regimens |
| CPS ≥5 | Stronger category 1 positioning for several current regimens |
| CPS ≥10 | Selected trial threshold; not universal current threshold |
| TAP | Tumor Area Positivity |
| ICI | Immune checkpoint inhibitor |
| MSI-H | Microsatellite instability-high |
| dMMR | Deficient mismatch repair |
| HER2 | Human epidermal growth factor receptor 2 |

---

# 12. Version Control

## Version

1.0.0

## Change Type

Initial Gold production.

## Production Basis

- approved PP-0216 Decision Batch;
- locked Gold workflow;
- supplied clinical Source Files;
- current governance documents;
- approved Gold discussion/artifact reference.

---

# 13. Change History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold package after Decision Batch approval and lock. |

---

# 14. Final Status

**GOLD — READY FOR INTEGRATION**

The Knowledge Passport is structurally aligned with the locked Gold Population Package Specification and the PP-0216 approved scope.

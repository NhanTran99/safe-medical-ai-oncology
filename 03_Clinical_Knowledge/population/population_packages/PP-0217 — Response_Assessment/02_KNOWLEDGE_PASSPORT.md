# 02_KNOWLEDGE_PASSPORT — PP-0217 Response Assessment

## 1. Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0217 |
| PP ID | PP-0217 |
| Title | Response Assessment |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Last Updated | 2026-08-09 |

---

# 2. Knowledge Classification

## Clinical Domain

Gastric adenocarcinoma → Treatment response → Clinical reassessment.

## Primary Clinical Question

> How is treatment response assessed in gastric cancer, and how is the assessment used to understand whether treatment is helping, controlling, or failing to control the disease?

## Knowledge Type

Clinical educational knowledge object.

## Package Function

Clinical integration of treatment-response information.

## Educational Level

Patient-facing with clinically precise terminology.

## Clinical Complexity

High.

The topic requires integration of:

- baseline disease status;
- longitudinal comparison;
- clinical information;
- imaging;
- standardized response criteria;
- treatment setting;
- disease distribution;
- treatment intent;
- immunotherapy-specific interpretation;
- clinical reassessment.

## Patient Journey Stage

Primarily:

**Treatment monitoring / reassessment**

with interfaces to:

- treatment selection;
- treatment continuation;
- treatment change;
- surgery;
- surveillance;
- recurrence management.

---

# 3. Intended Runtime Usage

## Primary Runtime Uses

1. Explain what “response assessment” means.
2. Explain why response is assessed over time.
3. Explain why baseline matters.
4. Explain CR/PR/SD/PD at high level.
5. Explain why RECIST is useful without replacing clinical judgment.
6. Explain why stable disease may be meaningful.
7. Explain why progression does not automatically mean treatment options are exhausted.
8. Explain the difference between response assessment and treatment decision.
9. Explain response assessment in perioperative and advanced disease.
10. Explain why immunotherapy can require specialized response interpretation.
11. Help patients understand what a restaging or response report means.
12. Support safe clinical-information retrieval without creating individualized treatment recommendations.

## Retrieval Intent

Use when a user asks:

- “How do doctors know if my treatment is working?”
- “What does response assessment mean?”
- “What does stable disease mean?”
- “What does progressive disease mean?”
- “What is restaging after treatment?”
- “Why do I need another CT after chemotherapy?”
- “What is RECIST?”
- “Does a stable scan mean treatment failed?”
- “If the cancer progressed, are there no more treatments?”
- “How is response assessed during immunotherapy?”

---

# 4. Clinical Scope

## Core Knowledge Units

### KU-01
Definition and purpose of treatment response assessment.

### KU-02
Baseline disease assessment.

### KU-03
Longitudinal comparison.

### KU-04
Clinical + imaging + relevant laboratory integration.

### KU-05
High-level CR/PR/SD/PD interpretation.

### KU-06
Role of standardized response criteria.

### KU-07
Response assessment in neoadjuvant/perioperative treatment.

### KU-08
Response assessment in advanced/metastatic treatment.

### KU-09
Peritoneal-disease reassessment.

### KU-10
Stable disease interpretation.

### KU-11
Progression interpretation.

### KU-12
Measurement error and uncertainty.

### KU-13
High-level immunotherapy-specific response assessment.

### KU-14
Response assessment versus treatment decision.

### KU-15
Response versus prognosis, cure and surveillance.

### KU-16
Patient-facing interpretation and questions.

---

# 5. Evidence Classification

## Established / guideline-supported

- Treatment response assessment is explicitly incorporated into current gastric-cancer treatment pathways.
- NCCN uses treatment-response assessment and restaging in selected disease settings.
- Restaging may use CT and, in selected peritoneal-only disease, diagnostic laparoscopy/washings, PCI ± biopsy, FDG-PET/CT and EGD.
- Standardized response frameworks such as RECIST are used to characterize changes in solid tumors.
- Clinical interpretation should not be reduced to a single standardized measurement.
- Response assessment supports treatment reassessment.

## Context-dependent

- Exact timing of assessment.
- Imaging modality.
- Need for endoscopy, biopsy or laparoscopy.
- Use of formal RECIST.
- Interpretation of stable disease.
- Interpretation of progression.
- Surgical decision-making after neoadjuvant treatment.
- Immune-specific response criteria.

## Emerging / specialized

- iRECIST and immune-specific response interpretation.
- Pseudo-progression.
- Complex response patterns during immunotherapy.

---

# 6. Authoritative Sources

## Primary Current Guideline

**NCCN Gastric Cancer Version 2.2026**

Primary authority for:

- treatment-response assessment in gastric-cancer pathways;
- restaging;
- selected peritoneal-only disease reassessment;
- post-neoadjuvant assessment;
- treatment continuation/change pathways.

## Primary Evidence Synthesis

**NCI Gastric Cancer Treatment PDQ**

Used for:

- disease/treatment framework;
- gastric-cancer treatment context;
- treatment pathway evidence.

## Professional Framework

**ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, Edition 2023**

Used for:

- response evaluation framework;
- RECIST concepts;
- clinical versus trial response assessment;
- measurement limitations;
- iRECIST and immunotherapy-response concepts.

## Supporting Patient-facing Sources

- NCI;
- American Cancer Society.

---

# 7. Governance Metadata

| Field | Value |
|---|---|
| Governance Authority | CORE_WORKING_RULES |
| Structural Authority | FREEZE GOLD POPULATION PACKAGE SPECIFICATION |
| Discussion Authority | Approved PP Discussion Gold reference |
| Clinical Evidence Authority | Supplied project clinical Source Files |
| Execution Authority | Project Coordinator explicit PP request |
| Gold Depth Rule | Absolute; approved reference is minimum |
| Production Status | GOLD |
| QA Status | PASS |
| Repository Status | READY FOR INTEGRATION |

---

# 8. Knowledge Graph

## Prerequisite

- PP-0058 RECIST
- PP-0059 RECIST 1.1
- PP-0060 Target Lesions
- PP-0061 Measurable Disease
- PP-0062 Non-target Lesions
- PP-0063 Complete Response
- PP-0064 Partial Response
- PP-0065 Stable Disease
- PP-0066 Progressive Disease
- PP-0067 Response Assessment Algorithm
- PP-0068 Follow-up Imaging

## Related

- PP-0203 Perioperative Chemotherapy
- PP-0205 Adjuvant Therapy
- PP-0206 Neoadjuvant Therapy
- PP-0207 Chemoradiation
- PP-0208 Palliative Systemic Therapy
- PP-0213 Immunotherapy in Gastric Cancer
- PP-0214 Immune Checkpoint Inhibitors
- PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy
- PP-0216 PD-L1-guided Immunotherapy
- PP-0232 Multidisciplinary Management

## Downstream

- PP-0218 RECIST-based Assessment
- PP-0219 Post-treatment Imaging
- PP-0220 Surveillance After Gastric Cancer Treatment
- PP-0221 Recurrence Detection
- PP-0222 Management of Recurrent Gastric Cancer
- PP-0223 Metastatic Gastric Cancer
- PP-0224 Peritoneal Carcinomatosis
- PP-0225 Peritoneal Carcinoma as Only Disease
- PP-0231 Treatment-related Toxicity and Supportive Care

---

# 9. Boundary Map

## Foundational Layer

PP-0058–PP-0068 provide the component knowledge needed to understand formal response assessment.

## Clinical Integration Layer

**PP-0217 — Response Assessment**

Owns:

> What does treatment response assessment mean clinically, how is information compared over time, and how does the result inform reassessment?

## Formal Standardization Layer

**PP-0218 — RECIST-based Assessment**

Owns:

> How is response formally assigned using RECIST and related standardized criteria?

## Imaging Layer

**PP-0219 — Post-treatment Imaging**

Owns:

> How is post-treatment imaging performed and followed longitudinally?

## Follow-up Layer

**PP-0220 — Surveillance After Gastric Cancer Treatment**

Owns post-treatment surveillance.

## Recurrence Layer

**PP-0221 — Recurrence Detection**

Owns detection of recurrence.

---

# 10. Runtime Safety Rules

1. Never treat a response category as an automatic treatment prescription.
2. Never equate stable disease with treatment failure.
3. Never equate progression with exhaustion of all treatment options.
4. Never equate complete response with guaranteed cure.
5. Never use a single scan as the complete clinical assessment.
6. Always preserve the distinction between clinical response assessment and formal RECIST calculation.
7. Do not provide individualized treatment changes from this package.
8. Do not reproduce detailed RECIST methodology from this package.
9. Do not provide detailed iRECIST algorithms from this package.
10. Do not replace clinician interpretation with a response category.

---

# 11. Runtime Terminology

| Term | Runtime Meaning |
|---|---|
| Response assessment | Structured evaluation of how disease has changed during/after treatment |
| Restaging | Reassessment of disease extent/status after treatment or at a clinically relevant point |
| CR | Complete Response |
| PR | Partial Response |
| SD | Stable Disease |
| PD | Progressive Disease |
| RECIST | Response Evaluation Criteria in Solid Tumors |
| iRECIST | Immune-adapted response assessment framework used in appropriate immunotherapy settings |
| Baseline | Disease state used as a reference for subsequent assessment |
| Longitudinal assessment | Comparison across multiple time points |

---

# 12. Evidence / Knowledge Limits

This package does not establish:

- a universal assessment interval;
- a universal imaging modality;
- a universal definition for every disease pattern outside the delegated standardized criteria;
- an individualized treatment response;
- an individualized prognosis.

Such conclusions require patient-specific information and current clinical assessment.

---

# 13. Version Control

## Version

1.0.0

## Change Type

Initial Gold production.

## Production Basis

- approved and locked PP-0217 Decision Batch;
- supplied clinical Source Files;
- PP Registry;
- governance framework;
- approved Gold Discussion reference.

---

# 14. Final Status

**GOLD — READY FOR INTEGRATION**

The Knowledge Passport is aligned with the locked Gold Population Package architecture and preserves the clinical-integration ownership of PP-0217 without absorbing formal RECIST or imaging packages.

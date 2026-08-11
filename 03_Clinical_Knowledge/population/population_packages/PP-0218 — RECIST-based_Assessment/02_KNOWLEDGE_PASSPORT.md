# Knowledge Passport

---

# Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0218 |
| Population Package ID | PP-0218 |
| Clinical Knowledge Object | CKO-PP-0218 |
| Title | RECIST-based Assessment |
| Clinical Domain | Gastric Cancer — Treatment Response |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Last Updated | 2026-08-09 |

---

# Knowledge Classification

| Field | Value |
|---|---|
| Knowledge Type | Applied Clinical Assessment Knowledge |
| Educational Category | Treatment Response Assessment — RECIST-based Application |
| Educational Level | Intermediate / patient-facing technical |
| Clinical Complexity | High |
| Intended Audience | Patients, caregivers, clinicians, oncology educators, knowledge systems |
| Reading Level | Plain language with controlled technical terminology |
| Knowledge Granularity | Atomic integrated clinical question |
| Knowledge Scope | Application of RECIST 1.1 |

---

# Primary Clinical Question

> **How is a RECIST-based assessment constructed from measurable disease, target lesions, non-target disease and new lesions to produce an overall response assessment?**

---

# Patient Journey Classification

| Stage | Applicable |
|---|---|
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up / Response Assessment | ✓ |
| Survivorship |  |
| Palliative Care | ✓ |

**Reason:**

Patients may encounter RECIST-based response results during systemic treatment, clinical trials, advanced disease management and treatment reassessment. The package explains how the standardized result is constructed while preserving the distinction between RECIST assessment and broader clinical decision-making.

---

# Intended Runtime Usage

## Primary Runtime Role

- Explain a RECIST-based response result.
- Explain how target and non-target disease contribute to assessment.
- Explain why a response category is assigned.
- Support interpretation of treatment-response terminology.

## Secondary Runtime Role

- Clinical trial terminology support.
- Imaging-response education.
- Patient question generation.
- Prerequisite retrieval for response assessment.
- Interface between foundational RECIST packages and clinical response assessment.

---

# Typical Trigger Questions

- How is RECIST used to assess my tumor?
- How are target lesions selected?
- Why are only some tumors measured?
- What is the sum of diameters?
- What happens to tumors that are not target lesions?
- What does a new lesion mean under RECIST?
- How does RECIST decide CR, PR, SD or PD?
- What is the nadir?
- Why are lymph nodes treated differently?
- Can a tumor shrink and still be classified as progression?
- Does RECIST progression automatically mean treatment stops?
- Does a RECIST result determine my treatment?
- What is the difference between RECIST and iRECIST?

---

# Retrieval Priority

**Very High**

**Reason:**

PP-0218 is the applied layer between foundational RECIST concepts and clinical response assessment. PP-0058 and PP-0059 explicitly defer technical criteria, target lesions, measurable disease, response categories and implementation details to later Population Packages. fileciteturn19file15turn19file5

ESMO-ASCO directly identifies the implementation competencies required for RECIST, including target-lesion selection, measurement, non-target disease, new lesions, lymph nodes, response categories, confirmation and limitations. fileciteturn19file0

---

# Clinical Scope

## Included

- Application of RECIST 1.1.
- Appropriate response-assessment context.
- Baseline assessment.
- Measurable and non-measurable disease in application.
- Target-lesion selection.
- Maximum five target lesions and maximum two per organ.
- Target-lesion measurements.
- Sum of longest diameters.
- Longitudinal comparison.
- Nadir concept.
- Non-target disease.
- New lesions.
- Lymph-node considerations.
- CR/PR/SD/PD as integrated outputs.
- Overall RECIST-based assessment.
- Progression.
- Measurement error.
- Context-dependent response confirmation.
- Clinical-trial endpoint context.
- Individual-patient limitation of RECIST.
- iRECIST interface.

---

# Explicitly Excluded

- General definition-only explanation of RECIST.
- General definition-only explanation of RECIST 1.1.
- Detailed CT/MRI/PET acquisition.
- Detailed post-treatment imaging methodology.
- Detailed radiology workflow.
- Full iRECIST algorithm.
- Full pseudo-progression algorithm.
- Treatment selection.
- Treatment dosing.
- Treatment-after-progression algorithm.
- Individualized prognosis.
- Pathological response.
- Surveillance.
- Recurrence detection.

---

# Authority Hierarchy

## Governance Authority

CORE_WORKING_RULES and locked project governance.

## Structural Authority

FREEZE GOLD POPULATION PACKAGE SPECIFICATION and approved Gold artifact architecture.

## Discussion Authority

Approved Discussion Gold reference.

## Clinical Evidence Authority

Supplied project clinical materials.

## Primary Direct Response-Evaluation Source

ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, Edition 2023.

The ESMO-ASCO source directly identifies RECIST competencies including measurable/non-measurable disease, target lesions, sum of diameters, non-target disease, new lesions, lymph nodes, response categories, confirmation, PD, iRECIST and individual-patient limitations. fileciteturn19file0

---

# Evidence Classification

## Established / Standardized

- RECIST as a standardized solid-tumor response framework.
- RECIST 1.1.
- Target-lesion selection.
- Measurable/non-measurable disease.
- Sum of target-lesion diameters.
- Non-target disease assessment.
- New-lesion assessment.
- CR/PR/SD/PD.
- Lymph-node-specific considerations.
- Measurement error.
- Clinical-trial response assessment.

## Context-dependent

- Timing of assessment.
- Response confirmation.
- Individual applicability.
- Interpretation outside a clinical-trial endpoint.
- Use in specific gastric-cancer treatment settings.

## Specialized / Delegated

- iRECIST algorithm.
- Pseudo-progression.
- Detailed imaging methodology.
- Treatment-after-progression algorithms.

---

# Knowledge Graph

## Upstream

PP-0058 → RECIST

PP-0059 → RECIST 1.1

PP-0060 → Target Lesions

PP-0061 → Measurable Disease

PP-0062 → Non-target Lesions

PP-0063 → Complete Response

PP-0064 → Partial Response

PP-0065 → Stable Disease

PP-0066 → Progressive Disease

PP-0067 → Response Assessment Algorithm

PP-0068 → Follow-up Imaging

## Clinical Interface

PP-0217 → Response Assessment

**PP-0218 → RECIST-based Assessment**

## Downstream / Adjacent

PP-0219 → Post-treatment Imaging

PP-0220 → Surveillance After Gastric Cancer Treatment

PP-0221 → Recurrence Detection

PP-0222 → Management of Recurrent Gastric Cancer

PP-0223 → Metastatic Gastric Cancer

PP-0231 → Treatment-related Toxicity and Supportive Care

PP-0232 → Multidisciplinary Management of Gastric Cancer

## Immunotherapy Interface

PP-0213 → Immunotherapy in Gastric Cancer

PP-0214 → Immune Checkpoint Inhibitors

PP-0215 → MSI-H/dMMR Gastric Cancer and Immunotherapy

PP-0216 → PD-L1-guided Immunotherapy

iRECIST → specialized immune-response framework

---

# Boundary Map

## PP-0058

**Owns:** What RECIST is.

## PP-0059

**Owns:** What RECIST 1.1 is.

## PP-0217

**Owns:** Clinical meaning of treatment response assessment.

## PP-0218

**Owns:** How RECIST 1.1 is applied to disease findings to produce an integrated RECIST-based response assessment.

## PP-0219

**Owns:** Post-treatment imaging methodology and imaging-process interpretation.

This separation prevents conceptual duplication and preserves package atomicity.

---

# Runtime Safety Rules

1. Never equate RECIST response with treatment prescription.
2. Never equate PD with exhaustion of all treatment options.
3. Never equate CR with cure.
4. Never equate RECIST with TNM staging.
5. Never equate radiologic response with pathological response.
6. Never treat non-target disease as irrelevant.
7. Never treat target-lesion shrinkage alone as the complete response assessment.
8. Never apply RECIST identically to every cancer setting.
9. Never substitute PP-0218 for detailed iRECIST.
10. Never substitute PP-0218 for post-treatment imaging methodology.
11. Preserve the distinction between trial endpoint standardization and individual-patient clinical judgment.

---

# Future Update Triggers

Review PP-0218 if:

- RECIST 1.1 is revised or superseded.
- RECIST Working Group publishes a major technical revision.
- ESMO/ASCO updates response-assessment recommendations.
- iRECIST is substantially revised.
- Major evidence changes how response assessment is applied in gastric cancer.
- PP-0219 imaging architecture changes.
- PP-0060–0067 ownership changes.
- Governance or Gold Specification changes.

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production following Approved + Locked PP-0218 Decision Batch |

---

# Final Status

**GOLD — READY FOR INTEGRATION**

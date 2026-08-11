# PP-0181 — HER2 Testing
# Knowledge Passport

## 1. Identity

| Field | Value |
|---|---|
| PP ID | PP-0181 |
| Clinical Topic | HER2 Testing |
| Population | Gastric adenocarcinoma |
| Knowledge Product Type | Patient-centered Population Package |
| Package Role | Foundational HER2 testing and interpretation |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Biomarker Testing / Precision Oncology |
| Evidence Currency | Based on project Source Materials available for this production cycle |
| Governance Status | Locked |
| Runtime intent | Patient/caregiver education and clinically governed retrieval |
| Primary clinical question | How is HER2 tested and interpreted in gastric adenocarcinoma, and what does the result mean? |

---

# 2. Knowledge Classification

## Primary Classification

**Diagnostic / Biomarker Testing Knowledge**

## Secondary Classifications

- Pathology
- Molecular Oncology
- Precision Oncology
- Treatment Selection
- Patient Education

## Knowledge Granularity

**Atomic specialized biomarker package**

The package is deliberately narrower than:

- general biomarker testing;
- molecular classification;
- HER2 biology;
- HER2-targeted treatment.

It is broader than a purely technical IHC or ISH/FISH laboratory package because it must provide the complete patient-facing testing-to-interpretation pathway.

---

# 3. Patient Journey Classification

## Primary Journey Position

**Diagnosis → Pathology → Biomarker Testing → Treatment Selection**

## Clinical Journey

**Tumor tissue**

↓

**HER2 test**

↓

**IHC**

↓

**0 / 1+ / 2+ / 3+**

↓

**ISH/FISH if IHC 2+**

↓

**HER2 status**

↓

**Treatment relevance**

## Patient Questions Answered

- Why is HER2 tested?
- When is HER2 tested?
- What sample is used?
- What does IHC mean?
- What do 0, 1+, 2+, and 3+ mean?
- Why does 2+ need another test?
- What is FISH/ISH?
- What does HER2-positive mean?
- What does HER2-negative mean?
- Can HER2 results differ between samples?
- Does HER2-positive automatically determine treatment?
- How does HER2 relate to other biomarkers?

---

# 4. Intended Runtime Usage

## Use Case A — Explain a HER2 Test

Retrieve the definition, purpose, specimen and testing pathway.

## Use Case B — Explain a HER2 Report

Retrieve IHC scoring, 0/1+/2+/3+, equivocal results and ISH/FISH interpretation.

## Use Case C — Explain Why Additional Testing Is Needed

Retrieve the IHC 2+ → ISH/FISH pathway.

## Use Case D — Explain HER2-Positive Status

Retrieve positive criteria and treatment-selection relevance without generating a treatment prescription.

## Use Case E — Correct a Misconception

Use the Common Misconceptions section to distinguish:

- 1+ from positive;
- 2+ from positive;
- negative from inadequate;
- HER2 from prognosis;
- HER2 testing from treatment.

---

# 5. Retrieval / Runtime Relevance

## High-Priority Retrieval Concepts

- HER2 testing
- HER2 IHC
- ERBB2
- IHC 0
- IHC 1+
- IHC 2+
- IHC 3+
- equivocal HER2
- ISH
- FISH
- ERBB2 amplification
- HER2-positive
- HER2-negative
- gastric-specific HER2 scoring
- biopsy specimen
- surgical specimen
- HER2 heterogeneity
- repeat biomarker testing

## Retrieval Safety Rules

When answering from this package:

1. Do not convert IHC 2+ into HER2-positive without ISH/FISH.
2. Do not describe IHC 1+ as HER2-positive.
3. Do not use breast-cancer HER2 scoring rules as a substitute for gastric criteria.
4. Do not infer an individualized treatment plan from HER2 status alone.
5. Do not treat a failed/inadequate test as a negative result.
6. Do not describe HER2 status as a definitive prognostic label.
7. Do not replace the broader biomarker assessment with HER2 testing alone.

---

# 6. Clinical Scope

## Included

- HER2 definition
- HER2/ERBB2 relationship
- purpose of testing
- timing
- specimen concepts
- biopsy versus surgical specimen
- IHC
- gastric-specific IHC scoring
- 0/1+/2+/3+
- equivocal results
- ISH/FISH
- ERBB2 amplification
- positive/negative interpretation
- heterogeneity
- repeat-testing concept
- predictive versus prognostic role
- treatment-selection relevance
- relationship with other biomarkers
- patient-facing terminology
- common misconceptions

## Excluded

- detailed receptor signaling
- technical IHC protocols
- technical ISH/FISH protocols
- NGS methodology
- variant classification
- treatment regimens
- drug dosing
- resistance
- toxicities
- individualized treatment decisions
- individualized prognosis

---

# 7. Authoritative Sources

## Primary Source Set

### 1. NCCN Gastric Cancer v2.2026

Primary guideline source for:

- HER2 testing timing;
- IHC-first strategy;
- ISH/FISH reflex testing;
- IHC scoring;
- biopsy/surgical specimen criteria;
- ERBB2 amplification criteria;
- repeat biomarker testing;
- NGS context;
- prognostic uncertainty.

### 2. NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer

Supporting guideline edition/source in the project materials for:

- HER2 positivity;
- IHC/ISH testing;
- clinicopathologic associations;
- treatment-selection relevance.

## Supporting Sources

### 3. American Cancer Society — Stomach Cancer

Patient-facing source for:

- why HER2 is tested;
- IHC;
- FISH;
- 0/1+/2+/3+ simplified explanation;
- relationship to HER2-directed treatment.

### 4. ESMO-ASCO Global Curriculum / relevant project source material

Supporting oncology framework for:

- biomarker-driven treatment;
- pathology and molecular testing concepts;
- clinical integration.

### 5. NCI materials

Used where applicable for gastric-cancer diagnostic/treatment context and terminology.

---

# 8. Evidence Classification

## Established / Guideline-Supported

- HER2 testing has a defined role in gastric adenocarcinoma.
- NCCN recommends HER2 testing when advanced/metastatic disease is documented or suspected at diagnosis.
- IHC is used first.
- IHC 0 and 1+ are negative.
- IHC 2+ is equivocal.
- IHC 3+ is positive.
- IHC 2+ should be clarified with ISH/FISH.
- ERBB2 amplification is assessed by ISH/FISH.
- HER2-positive status has treatment-selection relevance.
- Gastric-specific scoring criteria apply.
- Repeat biomarker testing may be considered at progression.

## Supported / Context-Dependent

- HER2 heterogeneity.
- Differences between biopsy and surgical specimens.
- Differences between specimens over time.
- NGS as a broader molecular-testing approach.
- Histologic associations with HER2 positivity.

## Uncertain / Do Not Overclaim

- Independent prognostic meaning of HER2 positivity in gastric cancer.
- Universal need for repeat testing.
- Universal superiority of one specimen type.
- Universal replacement of IHC/ISH by NGS.

---

# 9. Evidence Hierarchy

1. Current NCCN Gastric Cancer guideline.
2. Current project guideline materials.
3. CAP/ASCP/ASCO HER2 testing framework as represented within the project sources.
4. ESMO-ASCO oncology curriculum.
5. ACS patient-facing material.
6. NCI patient/PDQ material.
7. Underlying cited literature where required for context.

---

# 10. Knowledge Graph

## Prerequisite

- PP-0013 Targeted Therapy
- PP-0015 Biomarker Testing
- PP-0178 Histopathologic Classification
- PP-0179 Lauren Classification
- PP-0180 Molecular Classification

## Current Node

**PP-0181 HER2 Testing**

## Related

- PP-0182 MSI/MMR Testing
- PP-0183 PD-L1 Testing
- PP-0184 CLDN18.2 Testing
- PP-0185 TMB
- PP-0186 FGFR2 Testing
- PP-0187 NGS Biomarker Testing
- PP-0188 Molecular Subtypes
- PP-0189 Genomic Test Results

## Downstream

- HER2 Biology
- HER2 IHC Testing
- HER2 ISH/FISH Testing
- HER2-targeted Therapy
- Trastuzumab
- T-DXd
- HER2 Resistance
- Cardiac Monitoring
- HER2 Toxicities
- Combination Therapy
- Companion Diagnostics

---

# 11. Clinical Interpretation Rules

## Rule 1

**IHC 0 → negative**

## Rule 2

**IHC 1+ → negative**

## Rule 3

**IHC 2+ → equivocal → ISH/FISH**

## Rule 4

**IHC 3+ → positive**

## Rule 5

**IHC 2+ + ISH/FISH positive → positive**

## Rule 6

**IHC 2+ + ISH/FISH negative → not HER2-positive by this pathway**

## Rule 7

A negative result is not equivalent to an inadequate test.

## Rule 8

HER2 status does not independently determine treatment.

## Rule 9

HER2 status is not equivalent to prognosis.

## Rule 10

Gastric-specific HER2 criteria must be preserved.

---

# 12. Clinical Boundary

### Core

Complete patient-facing HER2 testing and interpretation pathway.

### Supporting

Foundational biology, molecular context, specimen limitations, heterogeneity and NGS context.

### Explicitly Excluded

Detailed laboratory methodology, drug treatment, resistance, toxicity, individualized decision-making and detailed regulatory content.

### Delegated

Dedicated HER2 biology, IHC, ISH/FISH, treatment, drug, resistance, toxicity, companion-diagnostic and molecular-report packages.

---

# 13. Evidence Confidence

| Domain | Confidence |
|---|---|
| IHC-first HER2 testing | High |
| IHC 0/1+/2+/3+ interpretation | High |
| IHC 2+ → ISH/FISH | High |
| ERBB2 amplification criteria | High |
| HER2-positive treatment relevance | High |
| Biopsy/surgical specimen distinction | High |
| Repeat testing at progression | Moderate-to-high, context-dependent |
| HER2 prognostic significance | Uncertain |
| Universal NGS replacement | Not supported |

---

# 14. Governance Metadata

| Field | Value |
|---|---|
| Source-first rule | Applied |
| Adjacent-PP overlap check | Completed |
| Decision Batch | Approved / Locked |
| Gold structure | Locked |
| Full-depth rule | Applied |
| Boundary | Required and included |
| ZIP package | Required |
| Artifact set | 4 Markdown files |
| QA layers | Content / Clinical / Educational / Governance |

---

# 15. Version Control

**Version:** 1.0.0

### Versioning rule

Minor changes to clinical content without architecture change should use a minor version update when governed as such.

Major architecture changes require explicit governance approval.

---

# 16. Change History

| Version | Change |
|---|---|
| 1.0.0 | Initial Gold production following PP-0181 approval/lock |

---

# 17. Final Status

**GOLD — READY FOR INTEGRATION**

This passport establishes PP-0181 as the foundational HER2 testing package and preserves downstream ownership for detailed HER2 biology, testing methodology and treatment.

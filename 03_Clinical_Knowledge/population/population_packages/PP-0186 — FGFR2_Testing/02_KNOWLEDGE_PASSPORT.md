# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0186 |
| Population Package ID | PP-0186 |
| Clinical Knowledge Object | CKO-PP-0186 |
| Title | FGFR2 Testing |
| Clinical Domain | Molecular Biomarker Testing |
| Clinical Domain Code | MBT |
| Population Batch | Gastric Cancer Molecular Biomarkers |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Status | Approved — Gold |

---

# Knowledge Classification

| Field | Value |
|---|---|
| Knowledge Type | Foundational / Applied Medical Knowledge |
| Educational Category | Molecular Biomarker Testing |
| Educational Level | Introductory to Intermediate |
| Clinical Complexity | Intermediate — Conceptual |
| Intended Audience | General public, patients with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic — Single Educational Question |
| Knowledge Scope | FGFR2 testing and interpretation |

---

# Patient Journey Classification

| Stage | Applicable |
|---|---|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | |
| Palliative Care | ✓ |

**Reason:**

FGFR2 testing belongs primarily to molecular characterization and treatment-decision contexts in patients with established gastric cancer. The package explains what the test means and how its result should be understood conceptually, while leaving treatment selection to downstream treatment packages.

---

# Primary Runtime Role

- Explain FGFR2 testing in plain language.
- Clarify what an FGFR2-related test can measure.
- Prevent confusion between FGFR2, FGFR2 amplification, FGFR2b expression, and NGS.
- Explain the role of assay context.
- Explain what positive, negative, and indeterminate results mean conceptually.
- Prevent overinterpretation of FGFR2 results.

---

# Secondary Runtime Roles

- Molecular biomarker education.
- Precision-oncology education.
- Preparation for understanding molecular reports.
- Clarification of FGFR2 versus broader molecular testing.
- Explanation of the relationship between biomarker testing and potential targeted-therapy relevance.
- Identification of evidence limitations in the current project source base.

---

# Typical Trigger Questions

- What is FGFR2?
- What is FGFR2 testing?
- Why was FGFR2 tested?
- Is FGFR2 the same as FGFR2b?
- Is FGFR2 the same as FGFR2 amplification?
- Is FGFR2 testing the same as NGS?
- What does FGFR2-positive mean?
- What does FGFR2-negative mean?
- What does an indeterminate FGFR2 result mean?
- Can FGFR2 be tested from blood?
- Does a positive FGFR2 result mean I need targeted therapy?
- Does FGFR2 determine prognosis?
- Does FGFR2 replace other biomarker testing?
- Why does the test method matter?

---

# Retrieval Priority

**High**

**Reason:**

FGFR2 is explicitly registered as a dedicated Population Package between TMB and NGS Biomarker Testing. The package is intended to provide a biomarker-specific educational layer while avoiding duplication of NGS methodology, molecular-report interpretation, and targeted-therapy treatment decisions.

The retrieval layer must also preserve the important evidence limitation: the supplied project Source Files do not establish a universal FGFR2-specific gastric-cancer testing algorithm or positivity threshold.

---

# Knowledge Graph

## Prerequisites

- PP-0002 — What is Gastric Cancer?
- PP-0003 — What is Gastric Adenocarcinoma?
- PP-0026 — Biomarker Testing
- PP-0180 — Gastric Cancer Molecular Classification
- PP-0185 — Tumor Mutational Burden (TMB)

## Related

- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0184 — CLDN18.2 Testing
- PP-0185 — Tumor Mutational Burden (TMB)
- PP-0187 — NGS Biomarker Testing
- PP-0188 — Molecular Subtypes of Gastric Cancer
- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0190 — Biomarker Testing for Targeted Therapy
- PP-0191 — Biomarker Testing for Immunotherapy
- PP-0208 — Targeted Therapy in Gastric Cancer

## Next / Downstream

**PP-0186 FGFR2 Testing**
→ **PP-0187 NGS Biomarker Testing**
→ **PP-0189 Genomic Test Results / How to Read a Molecular Report**
→ **PP-0190 Biomarker Testing for Targeted Therapy**
→ **PP-0208 Targeted Therapy in Gastric Cancer**

This is a knowledge-graph relationship, not a mandatory clinical sequence.

---

# Clinical Scope

## Core

- FGFR2 as a molecular biomarker topic.
- Meaning of FGFR2 testing.
- Molecular-feature distinctions.
- Conceptual positive/negative/indeterminate result interpretation.
- Assay dependence.
- Specimen/tumor-material concepts.
- Relationship to general biomarker testing.
- Relationship to NGS.
- Potential clinical relevance.
- Patient-facing interpretation.
- Evidence limitations.

## Supporting

- Basic molecular context.
- Gene alteration versus amplification versus protein expression.
- Selected blood-based genomic-testing context.
- Relationship with other gastric-cancer biomarkers.
- Molecular characterization context.

---

# Explicitly Excluded

- Detailed FGFR2 signaling.
- Detailed receptor biology.
- Detailed FGFR2 resistance mechanisms.
- FGFR2b-specific testing algorithm.
- Exact IHC scoring.
- Exact FISH criteria.
- Exact NGS thresholds.
- Universal FGFR2 testing.
- Companion-diagnostic criteria.
- Repeat-testing schedules.
- Prognostic algorithms.
- Resistance-monitoring algorithms.
- Detailed liquid-biopsy methodology.
- NGS laboratory methodology.
- Variant interpretation.
- Treatment selection.
- Drug dosing.
- Drug toxicity.
- Treatment sequencing.
- Complete molecular classification.

---

# Authoritative Sources

## Primary Project Source

**NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2026**

Relevant source-supported framework:

- pathologic review and biomarker testing are important in gastric cancer;
- biomarker assessment may use IHC, ISH, targeted PCR, and NGS depending on the molecular question;
- NGS may be considered later when sufficient tumor tissue is available;
- broader genomic testing can assess multiple molecular events;
- blood-based ctDNA testing may provide genomic information in selected advanced/metastatic settings.

**Important source limitation:**

The supplied NCCN source does not provide a sufficiently detailed FGFR2-specific testing algorithm, assay, or positivity threshold for PP-0186.

---

# Supporting Sources

- Other supplied gastric-cancer NCCN materials for general biomarker-testing architecture.
- Supplied NCI and ACS gastric-cancer educational materials where relevant to patient-facing molecular-testing context.
- Supplied ESMO-ASCO Global Curriculum 2023 for general oncology education.

These supporting materials do not override the FGFR2-specific evidence limitation.

---

# Evidence Classification

## Evidence Model

**Guideline-grounded educational synthesis with an explicit FGFR2-specific evidence gap.**

---

## Evidence Hierarchy

### Level I — Direct Gastric-Cancer Guideline

- NCCN Gastric Cancer Version 2.2026.

### Supporting

- NCI educational materials.
- American Cancer Society educational materials.
- ESMO-ASCO Global Curriculum 2023.

### Evidence Gap

No supplied project source currently establishes a complete FGFR2-specific testing algorithm or threshold.

---

# Intended Knowledge Boundaries

## Core

FGFR2 testing meaning, molecular-feature distinctions, result interpretation, assay context, specimen context, relationship with NGS, potential clinical relevance, and evidence limitations.

## Supporting

Basic FGFR2 molecular context, relationship with other biomarkers, and selected blood-based genomic-testing context.

## Explicitly Excluded

Detailed assay methodology, exact thresholds, detailed NGS methodology, variant interpretation, targeted-therapy management, prognostic/resistance algorithms, and universal testing recommendations.

## Delegated

- PP-0180 — Gastric Cancer Molecular Classification.
- PP-0187 — NGS Biomarker Testing.
- PP-0188 — Molecular Subtypes of Gastric Cancer.
- PP-0189 — Genomic Test Results / How to Read a Molecular Report.
- PP-0190 — Biomarker Testing for Targeted Therapy.
- PP-0208 — Targeted Therapy in Gastric Cancer.
- PP-0181–PP-0185 — adjacent biomarker-specific packages.

---

# Governance Metadata

| Field | Value |
|---|---|
| Source-First Verification | Complete |
| PP Registry Verification | Complete |
| Discussion Reference Verification | Complete |
| Gold Specification Verification | Complete |
| Adjacent PP Overlap Check | Complete |
| Boundary Defined | Complete |
| Evidence Gap Declared | Complete |
| Knowledge Graph | Complete |
| Runtime Ready | Yes |
| Repository Ready | Yes |
| Gold Specification Compliance | Yes |

---

# Version Control

| Item | Value |
|---|---|
| Current Version | 1.0.0 |
| Major Version | 1 |
| Minor Version | 0 |
| Patch Version | 0 |

---

# Future Update Triggers

Review this Knowledge Passport if:

- NCCN adds FGFR2-specific gastric-cancer testing recommendations.
- A validated FGFR2-specific assay becomes part of the guideline testing framework.
- A consensus FGFR2 positivity threshold is established.
- A companion diagnostic is established for an FGFR2-directed treatment context.
- Major gastric-cancer evidence establishes a clinically actionable FGFR2 testing algorithm.
- NGS guidance changes the reporting of FGFR2-related findings.
- Molecular-report governance changes.
- Targeted-therapy package boundaries change.
- Population Package governance changes.

---

# Quality Status

| Check | Result |
|---|---|
| Identity Complete | PASS |
| Classification Complete | PASS |
| Patient Journey Classification Complete | PASS |
| Scope Defined | PASS |
| Evidence Limitation Declared | PASS |
| Boundary Defined | PASS |
| Knowledge Graph Complete | PASS |
| Governance Metadata Complete | PASS |
| Versioning Complete | PASS |

---

# Final Status

**APPROVED — GOLD**

This Knowledge Passport is the official governance metadata for **PP-0186 — FGFR2 Testing** and conforms to the locked Gold Population Package architecture.

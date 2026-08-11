# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0013 |
| Population Package ID | PP-0013 |
| Clinical Knowledge Object | CKO-PP-0013 |
| Title | Targeted Therapy for Gastric Adenocarcinoma |
| Clinical Domain | Understanding Cancer |
| Clinical Domain Code | UC |
| Population Batch | Understanding Cancer |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Status | Approved |

---

# Knowledge Classification

| Field | Value |
|-------|-------|
| Knowledge Type | Foundational Medical Knowledge |
| Educational Category | Core Oncology Patient Education |
| Educational Level | Introductory |
| Clinical Complexity | Basic to Intermediate |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Treatment Concept |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✗ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason**

Targeted therapy is a precision medicine approach used during treatment planning and active treatment for selected patients whose tumors demonstrate actionable biomarkers.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding targeted therapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before biomarker-specific and drug-specific Population Packages.

## Typical Trigger Questions

- What is targeted therapy?
- How is targeted therapy different from chemotherapy?
- Why do I need biomarker testing?
- What is HER2?
- Who can receive targeted therapy?
- Can everyone receive targeted therapy?
- What are the benefits of targeted therapy?
- Does targeted therapy have side effects?

## Retrieval Priority

High

**Reason**

Targeted therapy is one of the principal systemic treatment modalities in modern gastric cancer care and serves as prerequisite knowledge for precision oncology Population Packages.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0001 What is Cancer?
- PP-0002 What is Gastric Cancer?
- PP-0003 What is Gastric Adenocarcinoma
- PP-0004 Causes and Risk Factors
- PP-0005 Symptoms
- PP-0006 Diagnosis
- PP-0007 Pathology Report
- PP-0008 Cancer Staging
- PP-0009 Treatment Overview
- PP-0010 Surgery for Gastric Adenocarcinoma
- PP-0011 Chemotherapy for Gastric Adenocarcinoma
- PP-0012 Radiotherapy for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| Future PP | Biomarker Testing |
| Future PP | HER2 Testing |
| Future PP | HER2-targeted Therapy |
| Future PP | CLDN18.2-targeted Therapy |
| Future PP | VEGFR2-targeted Therapy |
| Future PP | Immunotherapy |
| Future PP | Precision Medicine |
| Future PP | Systemic Therapy |

---

## Recommended Next Population Package

**PP-0014**

Immunotherapy for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of targeted therapy
- Difference from chemotherapy
- Role of biomarker testing
- General treatment principles
- Major biomarker examples (overview only)
- Clinical situations where targeted therapy may be used
- Expected benefits
- General limitations
- Common side effects (overview)
- General patient expectations

---

## Explicitly Excluded

- Drug-specific indications
- Trastuzumab
- Ramucirumab
- Zolbetuximab
- HER2 testing methodology
- CLDN18.2 testing methodology
- Biomarker interpretation
- Treatment-line selection
- Drug dosing
- Combination regimens
- Resistance mechanisms
- Toxicity management

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer
2. JNCCN Gastric Cancer Guideline Discussion

---

## Supporting Sources

- National Cancer Institute (NCI PDQ)
- American Cancer Society (ACS)
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level 1

- NCCN Gastric Cancer Guidelines
- JNCCN Gastric Cancer Guideline Discussion

### Level 1 (Patient Education)

- National Cancer Institute (NCI)
- American Cancer Society (ACS)

### Supporting

- ESMO Clinical Practice Guidelines

No secondary literature was required.

---

# Governance Metadata

| Field | Value |
|-------|-------|
| Clinical Governance | Enabled |
| Evidence Traceability | Complete |
| Scope Boundary | Defined |
| Knowledge Graph | Complete |
| Runtime Ready | Yes |
| Repository Ready | Yes |

---

# Version Control

| Item | Value |
|------|-------|
| Current Version | 1.0.0 |
| Major Version | 1 |
| Minor Version | 0 |
| Patch Version | 0 |

---

# Change History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Targeted Therapy for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises biomarker-directed therapy recommendations.
- JNCCN publishes major updates affecting targeted therapy.
- New targeted treatment classes become standard of care.
- NCI or ACS substantially updates patient education.
- Population Graph architecture changes.
- Governance specification changes.
- Runtime retrieval strategy changes.

---

# Quality Status

| Check | Result |
|-------|--------|
| Identity Complete | PASS |
| Classification Complete | PASS |
| Scope Clearly Defined | PASS |
| Knowledge Graph Complete | PASS |
| Runtime Metadata Complete | PASS |
| Governance Metadata Complete | PASS |
| Versioning Complete | PASS |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0013 — Targeted Therapy for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0016 |
| Population Package ID | PP-0016 |
| Clinical Knowledge Object | CKO-PP-0016 |
| Title | HER2 Testing for Gastric Adenocarcinoma |
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
| Knowledge Scope | Biomarker-specific Testing Concept |

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

HER2 testing is one of the core biomarker assessments performed during treatment planning for appropriate patients with gastric adenocarcinoma and directly supports precision oncology.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding HER2 testing.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before HER2-targeted therapy Population Packages.

## Typical Trigger Questions

- What is HER2?
- What is HER2 testing?
- Why do I need HER2 testing?
- When is HER2 testing performed?
- What does HER2-positive mean?
- What does HER2-negative mean?
- Can HER2 testing be repeated?
- How does HER2 affect treatment?

## Retrieval Priority

High

**Reason**

HER2 testing is one of the most frequently discussed biomarker tests in gastric adenocarcinoma and is directly linked to treatment selection.

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
- PP-0013 Targeted Therapy for Gastric Adenocarcinoma
- PP-0014 Immunotherapy for Gastric Adenocarcinoma
- PP-0015 Biomarker Testing for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0015 | HER2 testing is a specific biomarker test within the overall biomarker testing framework |
| PP-0013 | HER2 testing identifies patients who may benefit from HER2-targeted therapy |
| PP-0007 | HER2 testing is performed using pathology specimens |
| Future PP | HER2-targeted Therapy |
| Future PP | HER2 Biology |
| Future PP | HER2 IHC Testing |
| Future PP | HER2 ISH/FISH Testing |
| Future PP | Companion Diagnostics |

---

## Recommended Next Population Package

**PP-0017**

PD-L1 Testing for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of HER2
- Definition of HER2 testing
- Clinical purpose of HER2 testing
- Timing of testing
- General specimen sources
- HER2-positive and HER2-negative (plain-language overview)
- Relationship between HER2 status and treatment selection
- Repeat testing (overview only)
- General patient expectations

---

## Explicitly Excluded

- HER2 molecular biology
- HER2 signaling pathway
- IHC methodology
- ISH/FISH methodology
- HER2 scoring system
- Technical pathology workflow
- Companion diagnostics
- HER2-targeted medicines
- Drug dosing
- Treatment sequencing

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

# Evidence Hierarchy

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for HER2 Testing for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises HER2 testing recommendations.
- JNCCN publishes major updates regarding HER2-directed treatment.
- HER2 testing standards are revised by major oncology organizations.
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

This Knowledge Passport is the official governance metadata for **PP-0016 — HER2 Testing for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
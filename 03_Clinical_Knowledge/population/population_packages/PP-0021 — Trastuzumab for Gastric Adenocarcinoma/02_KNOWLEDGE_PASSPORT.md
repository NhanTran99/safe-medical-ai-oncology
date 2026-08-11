# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0021 |
| Population Package ID | PP-0021 |
| Clinical Knowledge Object | CKO-PP-0021 |
| Title | Trastuzumab for Gastric Adenocarcinoma |
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
| Clinical Complexity | Intermediate |
| Intended Audience | Newly diagnosed patients, caregivers, general public |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Individual Therapeutic Agent |

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

Trastuzumab is an established HER2-targeted medicine used in appropriate patients with HER2-positive gastric adenocarcinoma and represents a major application of precision oncology.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding trastuzumab.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before detailed treatment administration and toxicity Population Packages.

## Typical Trigger Questions

- What is trastuzumab?
- Why do I need trastuzumab?
- Why must my cancer be HER2-positive?
- How does trastuzumab work?
- Is trastuzumab chemotherapy?
- What are the benefits of trastuzumab?
- What side effects may occur?
- Who can receive trastuzumab?

## Retrieval Priority

High

**Reason**

Trastuzumab is the foundational HER2-targeted medicine introduced after HER2 testing and HER2-targeted therapy concepts.

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
- PP-0016 HER2 Testing for Gastric Adenocarcinoma
- PP-0017 PD-L1 Testing for Gastric Adenocarcinoma
- PP-0018 MSI-H / dMMR Testing for Gastric Adenocarcinoma
- PP-0019 CLDN18.2 Testing for Gastric Adenocarcinoma
- PP-0020 HER2-targeted Therapy for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0020 | Trastuzumab is a major HER2-targeted therapy |
| PP-0016 | HER2 testing determines eligibility for trastuzumab |
| PP-0015 | Biomarker testing forms the basis for trastuzumab selection |
| Future PP | Trastuzumab Deruxtecan |
| Future PP | Cardiac Monitoring |
| Future PP | Infusion Therapy |
| Future PP | HER2 Resistance |
| Future PP | Targeted Therapy Side Effects |
| Future PP | ToGA Trial |

---

## Recommended Next Population Package

**PP-0022**

Trastuzumab Deruxtecan for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of trastuzumab
- Drug class
- Relationship with HER2 testing
- General indication
- General mechanism of action
- General treatment setting
- Potential benefits
- General limitations
- Overview of common side effects
- General patient expectations

---

## Explicitly Excluded

- Molecular pharmacology
- Drug dosing
- Infusion procedures
- Premedication
- Cardiac monitoring
- Management of adverse effects
- Treatment sequencing
- Resistance mechanisms
- Clinical trial interpretation

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Trastuzumab for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises trastuzumab recommendations.
- New evidence changes the standard role of trastuzumab.
- JNCCN publishes major HER2-targeted therapy updates.
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

This Knowledge Passport is the official governance metadata for **PP-0021 — Trastuzumab for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0022 |
| Population Package ID | PP-0022 |
| Clinical Knowledge Object | CKO-PP-0022 |
| Title | Trastuzumab Deruxtecan (T-DXd) for Gastric Adenocarcinoma |
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

Trastuzumab deruxtecan (T-DXd) is an advanced HER2-targeted therapy considered for appropriate patients with HER2-positive gastric adenocarcinoma and represents an important development in precision oncology.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding trastuzumab deruxtecan (T-DXd).

## Secondary Runtime Role

- Prerequisite knowledge retrieval before ADC mechanism, toxicity and treatment monitoring Population Packages.

## Typical Trigger Questions

- What is trastuzumab deruxtecan?
- What is T-DXd?
- How is T-DXd different from trastuzumab?
- Why do I need HER2 testing first?
- Who may receive T-DXd?
- What are the benefits of T-DXd?
- What side effects may occur?
- Why is careful monitoring required?

## Retrieval Priority

High

**Reason**

T-DXd is an important HER2-directed medicine that builds upon HER2 testing, HER2-targeted therapy and trastuzumab concepts.

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
- PP-0021 Trastuzumab for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0021 | T-DXd is a distinct HER2-targeted medicine following trastuzumab concepts |
| PP-0020 | T-DXd is an advanced HER2-targeted therapy |
| PP-0016 | HER2 testing determines eligibility for T-DXd |
| Future PP | Antibody-Drug Conjugates (ADC) |
| Future PP | ADC Mechanism of Action |
| Future PP | ILD / Pneumonitis |
| Future PP | HER2 Resistance |
| Future PP | DESTINY-Gastric Trial |
| Future PP | Infusion Therapy |

---

## Recommended Next Population Package

**PP-0023**

Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of trastuzumab deruxtecan
- Drug class
- Relationship with HER2 testing
- Relationship with trastuzumab
- General indication
- General mechanism of action (overview)
- General treatment setting
- Potential benefits
- General limitations
- Overview of important side effects
- General patient expectations

---

## Explicitly Excluded

- ADC molecular pharmacology
- Payload mechanism
- Linker technology
- Drug dosing
- Infusion procedures
- Premedication
- ILD/pneumonitis management
- Detailed adverse-effect management
- Treatment sequencing
- DESTINY-Gastric clinical trial interpretation

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Trastuzumab Deruxtecan (T-DXd) for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises T-DXd recommendations.
- New HER2-directed therapies change the treatment landscape.
- JNCCN publishes major updates regarding T-DXd.
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

This Knowledge Passport is the official governance metadata for **PP-0022 — Trastuzumab Deruxtecan (T-DXd) for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0024 |
| Population Package ID | PP-0024 |
| Clinical Knowledge Object | CKO-PP-0024 |
| Title | ADC Mechanism of Action for Gastric Adenocarcinoma |
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
| Knowledge Scope | Therapeutic Mechanism |

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

Understanding the mechanism of action of antibody-drug conjugates (ADCs) helps patients understand why biomarker testing is necessary, how precision oncology differs from conventional chemotherapy, and why ADCs are used only for selected patients.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding the mechanism of action of antibody-drug conjugates (ADCs).

## Secondary Runtime Role

- Prerequisite knowledge retrieval before Payload Mechanism, Linker Technology and Bystander Effect Population Packages.

## Typical Trigger Questions

- How do ADCs work?
- How does an antibody-drug conjugate deliver medicine?
- Why are ADCs considered targeted therapy?
- Why is biomarker testing needed before ADC treatment?
- What does the antibody do?
- What is the linker?
- What is the payload?
- Why are ADCs different from chemotherapy?

## Retrieval Priority

High

**Reason**

The ADC mechanism forms the conceptual bridge between ADC technology and individual ADC medicines, enabling patients to understand the rationale behind biomarker-guided treatment.

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
- PP-0022 Trastuzumab Deruxtecan (T-DXd) for Gastric Adenocarcinoma
- PP-0023 Antibody-Drug Conjugates (ADC) for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0023 | Introduces the ADC platform before explaining its mechanism |
| PP-0022 | T-DXd is a practical example of this mechanism |
| PP-0015 | Biomarker testing enables ADC target recognition |
| PP-0020 | Demonstrates how targeted therapies recognize specific biomarkers |
| Future PP | Payload Mechanism |
| Future PP | Linker Technology |
| Future PP | Bystander Effect |
| Future PP | ADC Toxicities |
| Future PP | Resistance to ADC Therapy |

---

## Recommended Next Population Package

**PP-0025**

Payload Mechanism in Antibody-Drug Conjugates

---

# Clinical Scope

## Included

- Overall ADC mechanism
- Role of the antibody
- Role of the linker
- Role of the payload
- General target recognition
- General drug delivery process
- Relationship with biomarker testing
- Why ADCs are more selective than chemotherapy
- General patient expectations

---

## Explicitly Excluded

- Payload pharmacology
- Linker chemistry
- Intracellular trafficking
- Lysosomal degradation
- Drug release chemistry
- Bystander effect
- Individual ADC medicines
- Drug dosing
- Infusion procedures
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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for ADC Mechanism of Action for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises ADC-related recommendations.
- New ADC technologies significantly alter current therapeutic concepts.
- JNCCN publishes major updates regarding ADC mechanisms.
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

This Knowledge Passport is the official governance metadata for **PP-0024 — ADC Mechanism of Action for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
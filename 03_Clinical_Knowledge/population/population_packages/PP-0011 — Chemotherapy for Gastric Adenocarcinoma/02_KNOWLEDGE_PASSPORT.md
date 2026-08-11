# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0011 |
| Population Package ID | PP-0011 |
| Clinical Knowledge Object | CKO-PP-0011 |
| Title | Chemotherapy for Gastric Adenocarcinoma |
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

Chemotherapy is a core treatment modality that supports treatment planning, active systemic treatment, recurrence management, metastatic disease management and palliative care.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response regarding chemotherapy.

## Secondary Runtime Role

- Prerequisite knowledge retrieval before regimen-specific or treatment-specific Population Packages.

## Typical Trigger Questions

- What is chemotherapy?
- Why do I need chemotherapy?
- How does chemotherapy work?
- When is chemotherapy used?
- Will I receive chemotherapy before surgery?
- Will I need chemotherapy after surgery?
- How is chemotherapy given?
- Why is chemotherapy given in cycles?
- Why are several chemotherapy medicines used together?
- What are the common side effects of chemotherapy?

## Retrieval Priority

High

**Reason**

Chemotherapy is one of the principal treatment modalities for gastric adenocarcinoma and serves as a prerequisite concept for multiple downstream treatment Population Packages.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0001 What is Cancer?
- PP-0002 What is Gastric Cancer?
- PP-0003 What is Gastric Adenocarcinoma?
- PP-0004 Causes and Risk Factors
- PP-0005 Symptoms
- PP-0006 Diagnosis
- PP-0007 Pathology Report
- PP-0008 Cancer Staging
- PP-0009 Treatment Overview
- PP-0010 Surgery for Gastric Adenocarcinoma

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0010 | Surgery is commonly combined with chemotherapy in localized disease |
| PP-0012 | Radiotherapy may be combined with systemic treatment in selected patients |
| Future PP | Neoadjuvant Therapy |
| Future PP | Adjuvant Therapy |
| Future PP | Systemic Therapy |
| Future PP | Targeted Therapy |
| Future PP | Immunotherapy |
| Future PP | Chemotherapy Side Effects |
| Future PP | Nutrition During Treatment |
| Future PP | Supportive Care |

---

## Recommended Next Population Package

**PP-0012**

Radiotherapy for Gastric Adenocarcinoma

---

# Clinical Scope

## Included

- Definition of chemotherapy
- Role of chemotherapy in gastric adenocarcinoma
- Goals of treatment
- General mechanism of action
- Clinical settings in which chemotherapy is used
- Treatment cycles
- Combination chemotherapy
- Expected benefits
- Common side effects (overview)
- General patient expectations

---

## Explicitly Excluded

- Individual chemotherapy drugs
- Specific chemotherapy regimens (FLOT, CAPOX, FOLFOX, SOX, etc.)
- Drug dosing
- Regimen selection
- Detailed toxicity management
- Supportive medications
- Laboratory monitoring
- Targeted therapy
- Immunotherapy
- HIPEC
- Intraperitoneal chemotherapy
- Nutrition management
- Treatment response assessment

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
- ESMO Clinical Practice Guidelines (terminology and consensus support)

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
| 1.0.0 | 2026-08-04 | Initial Knowledge Passport for Chemotherapy for Gastric Adenocarcinoma |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises systemic therapy recommendations.
- JNCCN publishes major changes affecting chemotherapy principles.
- NCI or ACS substantially updates patient education regarding chemotherapy.
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

This Knowledge Passport is the official governance metadata for **PP-0011 — Chemotherapy for Gastric Adenocarcinoma** and conforms to the **Gold Population Package Specification v1.0**.
# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0031 |
| Population Package ID | PP-0031 |
| Clinical Knowledge Object | CKO-PP-0031 |
| Title | Upper Endoscopy |
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
| Educational Category | Cancer Diagnosis & Diagnostic Procedures |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients undergoing evaluation for stomach disease, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Foundational Diagnostic Procedure |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision |  |
| Active Treatment |  |
| Follow-up |  |
| Survivorship |  |
| Palliative Care |  |

**Reason:**

Upper endoscopy is a core diagnostic procedure performed before a definitive diagnosis is established and serves as a prerequisite concept for biopsy, pathology and gastric cancer diagnosis.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Diagnostic procedure education
- Patient reassurance before investigation
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is an upper endoscopy?
- Why do I need an upper endoscopy?
- What happens during an upper endoscopy?
- Does an upper endoscopy mean I have cancer?
- What can doctors see during an upper endoscopy?
- Will the doctor take a biopsy?
- Is upper endoscopy used to diagnose stomach cancer?

---

## Retrieval Priority

**High**

**Reason:**

Upper endoscopy is one of the most frequently discussed diagnostic procedures in gastric cancer care and serves as the foundation for several subsequent Population Packages.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0030

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0030 | Introduces stomach cancer screening |
| Gastric Cancer Symptoms | Explains symptoms leading to endoscopy |
| Biopsy During Upper Endoscopy | Expands tissue sampling |
| Gastric Cancer Diagnosis | Explains diagnostic workflow |
| Pathology | Explains microscopic examination |
| Gastric Cancer Staging | Explains staging after diagnosis |

---

## Recommended Next Population Package

**PP-0032**

**Biopsy During Upper Endoscopy**

---

# Clinical Scope

## Included

- Definition of upper endoscopy
- Purpose of the examination
- Organs examined
- Common indications
- Detection of abnormalities
- Role in stomach cancer evaluation
- Basic explanation of biopsy
- General expectations during the examination
- Initial explanation of results

---

## Explicitly Excluded

- Preparation before endoscopy
- Sedation protocols
- Technical performance
- Endoscopic classification systems
- Biopsy techniques
- Pathology interpretation
- Diagnosis confirmation
- Cancer staging
- Treatment planning
- Complication management
- Post-procedure care

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Screening for Stomach Cancer
   - Gastric Cancer Treatment

2. American Cancer Society (ACS)
   - Stomach Cancer
   - Diagnostic evaluation

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level 1

- National Cancer Institute (NCI PDQ)

### Level 1

- American Cancer Society (ACS)

### Supporting

- NCCN
- JNCCN
- ESMO

No lower-level evidence was required.

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
| 1.0.0 | 2026-08-04 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises recommendations regarding upper endoscopy.
- ACS updates patient education on diagnostic procedures.
- NCCN or ESMO introduces major revisions affecting endoscopic evaluation.
- Population Graph architecture changes.
- Governance specification changes.

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

This Knowledge Passport is the official governance metadata for **PP-0031** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
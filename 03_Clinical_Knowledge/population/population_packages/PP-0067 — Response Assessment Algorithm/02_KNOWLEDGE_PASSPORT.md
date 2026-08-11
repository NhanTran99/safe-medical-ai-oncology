# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0067 |
| Population Package ID | PP-0067 |
| Clinical Knowledge Object | CKO-PP-0067 |
| Title | Response Assessment Algorithm |
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
| Educational Category | Treatment Response Assessment Workflow |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Response Assessment Algorithm |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients often know the response categories (CR, PR, SD and PD) but do not understand **how doctors determine these results**. This Population Package explains the standardized assessment workflow while avoiding unnecessary technical complexity.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Treatment response education
- RECIST workflow explanation
- Imaging interpretation support
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- How do doctors determine treatment response?
- How do doctors know whether treatment is working?
- How are CR, PR, SD and PD determined?
- Do doctors compare my scans?
- Is one scan enough to determine treatment response?
- What happens during response assessment?

---

## Retrieval Priority

**Very High**

**Reason:**

This Population Package serves as the conceptual bridge connecting the foundational RECIST terminology packages (CR, PR, SD and PD) into a single patient-friendly explanation of the overall response assessment process.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0066

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0058 | Introduces RECIST |
| PP-0059 | Introduces RECIST 1.1 |
| PP-0060 | Target Lesions |
| PP-0062 | Non-target Lesions |
| PP-0063 | Complete Response (CR) |
| PP-0064 | Partial Response (PR) |
| PP-0065 | Stable Disease (SD) |
| PP-0066 | Progressive Disease (PD) |
| PP-0068 | Follow-up Imaging |

---

## Recommended Next Population Package

**PP-0068**

**Follow-up Imaging**

---

# Clinical Scope

## Included

- Standardized response assessment workflow
- Comparison of current and previous evaluations
- Assessment of existing and new lesions
- Classification into CR, PR, SD and PD
- Integration with comprehensive clinical decision-making

---

## Explicitly Excluded

- RECIST technical algorithm
- Measurement rules
- Target and non-target lesion criteria
- Treatment recommendations
- Prognosis
- Survival statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
2. American Cancer Society (ACS)

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines
- RECIST 1.1 Working Group publication

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- National Cancer Institute (NCI PDQ)
- American Cancer Society (ACS)

### Supporting

- NCCN
- JNCCN
- ESMO
- RECIST 1.1 Working Group publication

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
| 1.0.0 | 2026-08-05 | Initial Gold Release Knowledge Passport |

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

This Knowledge Passport is the official governance metadata for **PP-0067** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
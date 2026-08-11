# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0076 |
| Population Package ID | PP-0076 |
| Clinical Knowledge Object | CKO-PP-0076 |
| Title | Understanding Your CT Report |
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
| Educational Category | Imaging Results |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Understanding Your CT Report |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Many patients receive electronic access to their CT reports before discussing them with their doctor. This Population Package explains the purpose of the report, who writes it, and why it should always be interpreted within the broader clinical context rather than in isolation.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging report education
- Patient counseling
- Health literacy support
- Clinical workflow explanation
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a CT report?
- Who wrote my CT report?
- Should I worry about what my report says?
- Can I interpret my CT report myself?
- Is my CT report my diagnosis?
- Why do I need to discuss the report with my doctor?

---

## Retrieval Priority

**Very High**

**Reason:**

Patients frequently access imaging reports through electronic health record portals before meeting their clinician. Understanding the purpose and limitations of the report helps reduce anxiety and improves communication during follow-up consultations.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0075

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0069 | CT Scan |
| PP-0075 | After a CT Scan |
| PP-0077 | Common Terms in a CT Report |
| Cancer Diagnosis | Related |
| Pathology Report | Related |

---

## Recommended Next Population Package

**PP-0077**

**Common Terms in a CT Report**

---

# Clinical Scope

## Included

- Definition of CT report
- Radiologist's role
- Purpose of the report
- Clinical context
- Appropriate patient interpretation

---

## Explicitly Excluded

- Detailed radiology terminology
- Imaging findings
- Cancer staging
- Treatment recommendations
- AI interpretation
- Second opinion

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
2. American Cancer Society (ACS)

---

## Supporting Sources

- NCCN Clinical Practice Guidelines
- JNCCN Gastric Cancer Guideline Discussion
- ESMO Clinical Practice Guidelines
- American College of Radiology (ACR)
- Radiological Society of North America (RSNA)

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
- ACR
- RSNA

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
| 1.0.0 | 2026-08-06 | Initial Gold Release Knowledge Passport |

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

This Knowledge Passport is the official governance metadata for **PP-0076** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
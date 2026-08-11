# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0075 |
| Population Package ID | PP-0075 |
| Clinical Knowledge Object | CKO-PP-0075 |
| Title | After a CT Scan |
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
| Educational Category | Post-Imaging Care |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | After a CT Scan |

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

Patients commonly wonder what they should do after leaving the CT department, when they can resume normal activities, and when results will become available. This Population Package provides a simple explanation while intentionally separating result interpretation and clinical decision-making into future Population Packages.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Post-imaging education
- Patient counseling
- Discharge education
- Imaging workflow explanation
- Knowledge graph integration

---

## Typical Trigger Questions

- What happens after a CT scan?
- Can I go home after my CT?
- Can I return to normal activities?
- Who reads my CT scan?
- When are CT images reviewed?
- Should I call my doctor if I feel unwell afterward?

---

## Retrieval Priority

**Very High**

**Reason:**

Questions about recovery, discharge and result processing are among the most common immediately after CT examinations and complete the patient's understanding of the CT imaging journey.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0074

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0069 | CT Scan |
| PP-0072 | Contrast Agent |
| PP-0073 | Preparing for a CT Scan |
| PP-0074 | What Happens During a CT Scan? |
| PP-0076 | Understanding Your CT Report |

---

## Recommended Next Population Package

**PP-0076**

**Understanding Your CT Report**

---

# Clinical Scope

## Included

- General post-CT expectations
- Returning to daily activities
- Brief observation after contrast when appropriate
- Radiologist review process
- Following discharge instructions
- When to contact the healthcare team

---

## Explicitly Excluded

- CT interpretation
- CT report findings
- Exact result timing
- Contrast reactions
- Treatment decisions
- Radiation safety

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

This Knowledge Passport is the official governance metadata for **PP-0075** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
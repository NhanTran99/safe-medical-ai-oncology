# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0051 |
| Population Package ID | PP-0051 |
| Clinical Knowledge Object | CKO-PP-0051 |
| Title | Bone Metastasis |
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
| Educational Category | Metastatic Disease – Bone Metastasis |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Bone Metastasis |

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

Bone metastasis is an important form of distant metastatic disease that may be identified during staging or follow-up of gastric cancer. This Population Package provides the conceptual foundation before introducing bone imaging, bone biopsy, skeletal complications or treatment strategies.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Metastatic disease education
- Organ-specific metastasis education
- Medical terminology explanation
- Patient reassurance
- Prerequisite knowledge retrieval

---

## Typical Trigger Questions

- What is bone metastasis?
- Has my stomach cancer spread to my bones?
- Is bone metastasis the same as bone cancer?
- Can stomach cancer spread to bones?
- Does everyone with stomach cancer develop bone metastasis?
- How do doctors know whether cancer has spread to the bones?

---

## Retrieval Priority

**Very High**

**Reason:**

Bone metastasis is a recognized site of distant spread in gastric cancer and serves as prerequisite knowledge for future Population Packages covering bone imaging, skeletal-related events, bone-modifying agents and orthopedic management.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0050

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0045 | Introduces the M Category |
| PP-0046 | Defines metastasis |
| PP-0047 | Explains pathways of gastric cancer spread |
| PP-0050 | Lung metastasis |
| PP-0052 | Brain metastasis |
| Understanding Your Pathology Report | Clinical interpretation |

---

## Recommended Next Population Package

**PP-0052**

**Brain Metastasis**

---

# Clinical Scope

## Included

- Definition of bones
- Definition of bone metastasis
- Relationship between gastric cancer and bones
- Difference between primary bone cancer and bone metastasis
- Relationship between bone metastasis and metastatic gastric cancer
- Importance of appropriate medical evaluation

---

## Explicitly Excluded

- Primary bone cancer
- Osteosarcoma
- Chondrosarcoma
- Ewing sarcoma
- M1 classification
- Bone scan
- PET-CT
- MRI
- Bone biopsy
- Skeletal-related events (SREs)
- Bone-modifying agents
- Radiation therapy
- Orthopedic surgery
- Systemic therapy
- Prognostic statistics

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI PDQ)
   - Gastric Cancer Treatment
   - Gastric Cancer (Health Professional)

2. American Cancer Society (ACS)
   - Stomach Cancer

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

### Level I

- National Cancer Institute (NCI PDQ)

### Level I

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
| 1.0.0 | 2026-08-05 | Initial Gold Release Knowledge Passport |

---

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCI substantially revises educational content regarding bone metastasis.
- ACS updates patient education concerning metastatic gastric cancer involving the skeleton.
- NCCN or ESMO revises recommendations affecting skeletal metastatic disease.
- AJCC introduces major conceptual changes affecting metastatic staging.
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

This Knowledge Passport is the official governance metadata for **PP-0051** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
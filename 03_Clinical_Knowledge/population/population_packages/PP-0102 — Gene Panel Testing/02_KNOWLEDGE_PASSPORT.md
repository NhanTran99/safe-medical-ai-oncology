# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0102 |
| Population Package ID | PP-0102 |
| Clinical Knowledge Object | CKO-PP-0102 |
| Title | Gene Panel Testing |
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
| Educational Category | Molecular Diagnostics |
| Educational Level | Introductory |
| Clinical Complexity | Basic |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Gene Panel Testing |

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

Patients increasingly encounter gene panel testing when discussing molecular profiling and precision oncology. Understanding this concept helps distinguish the testing target (gene panel) from the sequencing technology (NGS).

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on gene panel testing

---

## Secondary Runtime Role

- Molecular diagnostics education
- Precision oncology education
- Patient counseling
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is gene panel testing?
- Is a gene panel the same as NGS?
- Why are only certain genes tested?
- Why do different cancers have different panels?
- Does everyone need gene panel testing?
- How does gene panel testing help doctors?

---

## Retrieval Priority

**Very High**

**Reason:**

Gene panel testing is one of the most frequently used clinical implementations of molecular diagnostics and represents a critical concept immediately following NGS in patient education.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0101

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0101 | Next-Generation Sequencing (NGS) |
| PP-0099 | Molecular Testing |
| PP-0098 | Precision Medicine |
| PP-0097 | Biomarker Testing |
| PP-0103 | Whole Genome Sequencing (WGS) |

---

## Recommended Next Population Package

**PP-0103**

**Whole Genome Sequencing (WGS)**

---

# Clinical Scope

## Included

- Definition
- Clinical purpose
- Relationship with NGS
- Clinical role
- Patient interpretation

---

## Explicitly Excluded

- Whole genome sequencing
- Whole exome sequencing
- RNA sequencing
- Variant interpretation
- Disease-specific panels
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI)
2. NCCN Clinical Practice Guidelines
3. American Society of Clinical Oncology (ASCO)
4. College of American Pathologists (CAP)
5. Association for Molecular Pathology (AMP)

---

## Supporting Sources

- American Cancer Society (ACS)
- ESMO Clinical Practice Guidelines
- JNCCN

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Evidence Hierarchy

### Level I

- NCI
- NCCN
- ASCO
- CAP
- AMP

### Supporting

- ACS
- ESMO
- JNCCN

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

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0102** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
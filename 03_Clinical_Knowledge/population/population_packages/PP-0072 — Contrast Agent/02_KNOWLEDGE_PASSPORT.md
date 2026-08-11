# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0072 |
| Population Package ID | PP-0072 |
| Clinical Knowledge Object | CKO-PP-0072 |
| Title | Contrast Agent (Contrast Dye / Contrast Material) |
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
| Educational Category | Medical Imaging |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate (Conceptual) |
| Intended Audience | General public, patients diagnosed with gastric cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Contrast Agent (Contrast Dye / Contrast Material) |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | ✓ |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | ✓ |
| Palliative Care | ✓ |

**Reason:**

Patients commonly ask why they are being given a contrast injection and whether it is part of their cancer treatment. This Population Package provides a simple conceptual explanation while intentionally avoiding detailed discussions of safety, adverse reactions or specific contrast agents.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational educational response

---

## Secondary Runtime Role

- Imaging education
- Contrast terminology explanation
- Patient counseling
- Examination preparation support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is contrast dye?
- Why do I need contrast?
- Does every CT or MRI use contrast?
- Does contrast treat cancer?
- Why did my doctor recommend contrast?
- Why was I asked about allergies or kidney disease?

---

## Retrieval Priority

**Very High**

**Reason:**

Questions about contrast agents are among the most common before CT and MRI examinations. This package serves as the conceptual foundation for future packages addressing contrast safety and preparation.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0071

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0069 | CT Scan |
| PP-0070 | MRI |
| PP-0071 | PET/CT |
| PP-0073 | Preparing for a CT Scan |
| Contrast Allergy | Future package |
| Contrast and Kidney Function | Future package |

---

## Recommended Next Population Package

**PP-0073**

**Preparing for a CT Scan**

---

# Clinical Scope

## Included

- Definition of contrast agent
- Purpose during imaging
- Imaging modalities that may use contrast
- Individualized use of contrast
- Basic explanation of pre-contrast assessment

---

## Explicitly Excluded

- Contrast pharmacology
- Types of contrast agents
- Contrast allergy
- Kidney safety
- Contrast administration
- Management of adverse reactions
- Detailed preparation instructions

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

This Knowledge Passport is the official governance metadata for **PP-0072** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
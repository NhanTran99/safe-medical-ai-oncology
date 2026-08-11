# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0144 |
| Population Package ID | PP-0144 |
| Clinical Knowledge Object | CKO-PP-0144 |
| Title | BS Evidence Codes (Strong Benign Evidence) |
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
| Educational Category | Clinical Genomics |
| Educational Level | Introductory |
| Clinical Complexity | Advanced Introductory |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | BS Evidence Codes (Strong Benign Evidence) |

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

Patients undergoing genetic testing may encounter variant classifications supported by different levels of evidence. This Population Package explains the meaning of **Strong Benign Evidence** and its relationship to Supporting Benign Evidence.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on BS Evidence Codes

## Secondary Runtime Role

- ACMG evidence-code education
- Benign evidence education
- Evidence-strength education
- Variant interpretation education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What are BS Evidence Codes?
- What does Strong Benign Evidence mean?
- Is BS stronger than BP?
- Does BS mean a variant is definitely benign?
- Why are different evidence strengths used?

---

# Retrieval Priority

**Very High**

**Reason:**

BS Evidence Codes form the foundational conceptual layer preceding the individual BS1–BS4 criteria and the benign evidence-combination framework.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0143

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0143 | BP7 |
| PP-0136 | BP Evidence Codes |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BS1
- BS2
- BS3
- BS4
- BA1
- Benign Evidence Combination Rules
- Bayesian ACMG Framework
- ClinGen BS Specifications

---

# Clinical Scope

## Included

- BS definition
- Strong Benign Evidence
- Evidence-strength hierarchy
- Relationship between BS and BP
- Overall role in variant interpretation
- Patient implications

---

## Explicitly Excluded

- BS1
- BS2
- BS3
- BS4
- BA1
- ACMG benign evidence combination rules
- Bayesian framework
- ClinGen BS specifications
- Gene-specific implementation
- Laboratory workflow
- Treatment recommendations

These topics are intentionally delegated to independent Population Packages.

---

# Authoritative Sources

## Primary Sources

1. ACMG
2. AMP
3. ClinGen SVI
4. CAP
5. NCI
6. NCCN
7. ASCO

## Supporting Patient-Education Sources

- ACS
- ESMO

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

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
| Current-Use Status | Current Evidence Category |

---

# Runtime Safety Rule

The Safe Medical AI System must distinguish:

**Strong Benign Evidence**

from:

**Final Benign Classification**

The system must not automatically state that a variant is benign solely because BS evidence is present without considering the applicable evidence framework and overall evidence.

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
| 1.0.0 | 2026-08-08 | Initial Gold Release Knowledge Passport |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0144** and is fully compliant with the locked **Gold Population Package Specification v1.0**.
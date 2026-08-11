# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0142 |
| Population Package ID | PP-0142 |
| Clinical Knowledge Object | CKO-PP-0142 |
| Title | BP6 (Reputable Source Recently Reports Variant as Benign, but the Evidence Is Not Available for Independent Evaluation) |
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
| Knowledge Scope | BP6 (Historical ACMG/AMP Criterion and Current Governance Status) |

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

Patients may encounter variant classifications originating from laboratories, databases, publications, or other genetic resources. This Population Package explains the historical meaning of **BP6** and why a reported benign classification should not automatically be treated as independently verified evidence.

---

# Intended Runtime Usage

## Primary Runtime Role

- Historical education on BP6
- Current governance education regarding BP6

---

## Secondary Runtime Role

- ACMG evidence-code education
- Evidence-quality education
- Variant interpretation education
- Database classification education
- Independent evidence evaluation education
- Patient counseling
- Knowledge graph integration

---

## Typical Trigger Questions

- What is BP6?
- What does BP6 mean?
- Why is BP6 no longer used?
- Can a reputable database saying "benign" prove a variant is benign?
- Why does independent evidence matter?
- Why did ClinGen recommend removing BP6?

---

# Retrieval Priority

**High**

**Reason:**

BP6 is important for understanding the historical evolution of the ACMG/AMP framework and the distinction between a **source assertion** and **independently evaluable evidence**.

However, BP6 must not be retrieved or presented as a currently recommended standalone benign evidence criterion.

---

# Knowledge Graph

## Prerequisite Population Packages

PP-0001 → PP-0141

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0141 | BP5 |
| PP-0136 | BP Evidence Codes |
| PP-0116 | ACMG Evidence Codes |
| PP-0115 | ACMG Variant Classification Framework |
| PP-0108 | Variant Classification |

---

## Future Population Packages

- BP7
- ClinVar
- Clinical Variant Databases
- Evidence Quality
- Independent Evidence Evaluation
- ACMG/ClinGen Evidence Governance

---

# Clinical Scope

## Included

- Historical BP6 definition
- Reputable source
- Reported benign classification
- Independent evidence evaluation
- Current ClinGen governance position
- Patient implications

---

## Explicitly Excluded

- ClinVar star ratings
- Detailed database submission rules
- Database curation methodology
- Bayesian framework
- ACMG evidence combination rules
- Detailed laboratory workflow
- Gene-specific BP6 specifications
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

---

## Supporting Sources

- ACS
- ESMO

---

# Evidence Classification

## Evidence Model

Authoritative Educational Synthesis

---

## Historical Framework

**ACMG/AMP 2015**

BP6 was originally defined as a Supporting Benign Evidence criterion concerning a reputable source reporting a variant as benign when the evidence was not available to the laboratory for independent evaluation.

---

## Current Governance

**ClinGen SVI**

BP6 is **not recommended for use**.

The current governance principle is to prioritize underlying primary evidence that can be independently evaluated rather than relying solely on assertions from reputable sources.

---

# Governance Metadata

| Field | Value |
|-------|-------|
| Clinical Governance | Enabled |
| Historical Status Preserved | Yes |
| Current Governance Status | Not for use |
| Evidence Traceability | Complete |
| Scope Boundary | Defined |
| Knowledge Graph | Complete |
| Runtime Ready | Yes |
| Repository Ready | Yes |

---

# Runtime Safety Rule

The Safe Medical AI System must distinguish:

**Historical definition**

> BP6 was an ACMG/AMP Supporting Benign Evidence criterion.

from:

**Current governance**

> BP6 is not recommended for use.

The system must **not** generate patient-facing advice implying that BP6 can currently be applied as a standalone benign evidence criterion.

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

This Knowledge Passport is the official governance metadata for **PP-0142** and is fully compliant with the locked **Gold Population Package Specification v1.0**.

BP6 is retained as **historical educational knowledge**, while its current governance status is explicitly recorded as **not recommended for use**.
# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0236 |
| Population Package ID | PP-0236 |
| Clinical Knowledge Object | CKO-PP-0236 |
| Title | Liquid Biopsy |
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
| Clinical Complexity | Intermediate |
| Intended Audience | General public, patients diagnosed with cancer, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Liquid Biopsy |

---

# Patient Journey Classification

| Stage | Applicable |
|---------|------------|
| Before Diagnosis | |
| During Diagnosis | ✓ |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Follow-up | ✓ |
| Survivorship | |
| Palliative Care | ✓ |

**Reason:**

Patients may encounter liquid biopsy when molecular information is needed during cancer diagnosis or treatment planning, particularly when tumor tissue is limited or difficult to obtain. Liquid biopsy may also provide molecular information about tumor evolution during advanced disease and treatment.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on Liquid Biopsy

---

## Secondary Runtime Role

- Clinical genomics education
- Molecular diagnostics education
- Patient counseling
- Shared decision-making support
- Explanation of blood-based molecular testing
- Knowledge graph integration

---

## Typical Trigger Questions

- What is a liquid biopsy?
- Is liquid biopsy the same as a normal biopsy?
- Is liquid biopsy the same as ctDNA?
- Why would my doctor use a blood test to look at my cancer genes?
- When is liquid biopsy useful in gastric cancer?
- Can liquid biopsy replace a tissue biopsy?
- What can liquid biopsy find?
- Can liquid biopsy help choose treatment?
- What does a negative liquid biopsy mean?
- Can a liquid biopsy show that my cancer has changed?

---

# Retrieval Priority

**Very High**

**Reason:**

Liquid biopsy is an important bridge between conventional tissue-based molecular testing and the specialized ctDNA package. It explains how blood-based tumor genomic information can complement tissue testing, particularly when tissue is limited or difficult to obtain, while establishing the safety boundary that a negative result does not exclude tumor presence.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0233 — Clinical Genomics
- PP-0235 — Somatic Genetic Testing

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0101 | Next-Generation Sequencing (NGS) |
| PP-0102 | Gene Panel Testing |
| PP-0103 | Whole Genome Sequencing (WGS) |
| PP-0104 | Whole Exome Sequencing (WES) |
| PP-0107 | Variant Interpretation |
| PP-0234 | Germline Genetic Testing |
| PP-0235 | Somatic Genetic Testing |

---

## Recommended Next Population Package

**PP-0237**

**Circulating Tumor DNA (ctDNA)**

---

# Clinical Scope

## Included

- Definition of liquid biopsy
- Blood/plasma-based liquid biopsy in gastric cancer
- Difference between liquid biopsy and tissue biopsy
- Relationship between liquid biopsy and ctDNA
- Clinical situations where liquid biopsy may be considered
- Limited tissue / inability to undergo traditional biopsy
- Detection of tumor-associated genomic alterations
- Potential identification of targetable alterations
- Tumor-clone evolution
- Treatment-response context
- Limitations of negative results
- Patient-facing interpretation

---

## Explicitly Excluded

- Detailed ctDNA biology
- Detailed ctDNA analytical workflow
- Longitudinal ctDNA monitoring protocols
- Circulating tumor cells (CTC)
- Sequencing methodology
- Bioinformatics pipelines
- Variant interpretation
- Variant classification
- Disease-specific treatment algorithms
- Detailed biomarker-specific treatment recommendations
- Unsupported liquid-biopsy technologies

These topics require dedicated Population Packages.

---

# Clinical Boundary

## Liquid Biopsy vs ctDNA

Liquid biopsy is the broader clinical concept.

ctDNA is an important tumor-derived molecular application within liquid biopsy.

PP-0236 introduces this relationship.

PP-0112 provides the dedicated ctDNA knowledge layer.

---

## Liquid Biopsy vs Tissue Biopsy

Liquid biopsy is complementary to tissue-based assessment.

It should not be represented as a universal replacement for tissue diagnosis.

---

## Negative Result Boundary

A negative liquid-biopsy result does **not** establish that:

- the patient has no cancer;
- the tumor has no genetic alterations;
- no actionable alteration exists.

The result must be interpreted according to the assay's capabilities and the clinical context.

---

# Authoritative Sources

## Primary Sources

1. NCCN Gastric Cancer Clinical Practice Guidelines
2. ESMO/ASCO Global Curriculum / molecular-testing framework
3. NCI cancer genetics and molecular-testing resources where relevant

---

## Supporting Sources

- Other approved Core Materials supplied for the Population Package project

---

# Evidence Classification

## Evidence Model

**Authoritative Educational Synthesis**

---

## Evidence Hierarchy

### Level I

- NCCN
- ESMO/ASCO
- NCI

### Supporting

- Other approved project Core Materials

The package does not introduce a new clinical algorithm beyond what is supported by the approved Core Materials.

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
|-------|-------|
| Current Version | 1.0.0 |
| Major Version | 1 |
| Minor Version | 0 |
| Patch Version | 0 |

---

# Change History

| Version | Date | Description |
|----------|------|-------------|
| 1.0.0 | 2026-08-08 | Initial Gold Release Knowledge Passport following locked PP-0236 decision |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0111** and is fully compliant with the locked **Gold Population Package Specification v1.0**.

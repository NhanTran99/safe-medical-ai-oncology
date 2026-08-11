# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0237 |
| Population Package ID | PP-0237 |
| Clinical Knowledge Object | CKO-PP-0237 |
| Title | Circulating Tumor DNA (ctDNA) |
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
| Knowledge Scope | Circulating Tumor DNA (ctDNA) |

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

ctDNA is encountered primarily in molecular characterization, treatment decision-making, and selected monitoring contexts. It can provide blood-based genomic information when tissue is limited and may provide information about molecular tumor evolution over time. It is not a universal diagnostic replacement or a universal surveillance test.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on circulating tumor DNA (ctDNA)

---

## Secondary Runtime Role

- Clinical genomics education
- Liquid biopsy education
- Molecular testing education
- Precision oncology education
- Patient counseling
- Shared decision-making support
- Knowledge graph integration

---

## Typical Trigger Questions

- What is ctDNA?
- What does circulating tumor DNA mean?
- Is ctDNA the same as liquid biopsy?
- Where does ctDNA come from?
- What can ctDNA testing detect?
- Why would my doctor order a ctDNA test?
- Can ctDNA replace a tissue biopsy?
- Can ctDNA show whether treatment is working?
- What does a negative ctDNA result mean?
- Can ctDNA detect treatment resistance?
- Can ctDNA be measured more than once?

---

# Retrieval Priority

**Very High**

**Reason:**

ctDNA is a key bridge between **liquid biopsy**, **somatic genetic testing**, and **clinical genomics**. It provides an important patient-facing explanation of how tumor-derived molecular information can be obtained from blood and why that information may be relevant when tissue is limited or when tumor molecular evolution is being assessed.

---

# Knowledge Graph

## Prerequisite Population Packages

- **PP-0099 — Molecular Testing**
- **PP-0101 — Next-Generation Sequencing (NGS)**
- **PP-0102 — Gene Panel Testing**
- **PP-0107 — Variant Interpretation**
- **PP-0233 — Clinical Genomics**
- **PP-0235 — Somatic Genetic Testing**
- **PP-0236 — Liquid Biopsy**

---

## Related Population Packages

| PP | Relationship |
|----|--------------|
| PP-0097 | Biomarker Testing |
| PP-0099 | Molecular Testing |
| PP-0101 | Next-Generation Sequencing (NGS) |
| PP-0102 | Gene Panel Testing |
| PP-0107 | Variant Interpretation |
| PP-0233 | Clinical Genomics |
| PP-0235 | Somatic Genetic Testing |
| PP-0236 | Liquid Biopsy |
| Precision Medicine | Related clinical application |
| Treatment Response | Related clinical application |

---

## Recommended Next Population Package

**Future specialized package — Molecular Monitoring / ctDNA-MRD, if separately defined.**

---

# Clinical Scope

## Included

- Definition of ctDNA
- Relationship with cfDNA
- Conceptual biological origin
- Blood-based genomic information
- Detection of mutations, genomic alterations, and gene fusions
- Selected clinical situations for ctDNA testing
- Limited tissue / inability to undergo traditional biopsy
- Potentially targetable alterations
- Tumor molecular evolution
- Treatment-response and resistance concepts
- Longitudinal molecular information
- Tissue versus ctDNA testing
- Negative-result interpretation
- Limitations
- Patient-facing education

---

## Explicitly Excluded

- Detailed cfDNA biology
- Blood collection and plasma-processing protocols
- cfDNA extraction
- Library preparation
- Sequencing chemistry
- Digital PCR methodology
- Bioinformatics
- Variant calling
- Variant interpretation
- Variant classification
- ACMG/ClinGen frameworks
- Circulating tumor cells (CTCs)
- Exosomes and other liquid-biopsy analytes
- Detailed MRD algorithms
- Detailed recurrence-surveillance algorithms
- Disease-specific ctDNA thresholds
- Numerical assay sensitivity/specificity thresholds
- Treatment-switch algorithms
- Individualized interpretation of patient-specific ctDNA results

These topics are intentionally delegated to other Population Packages or future specialized clinical-application packages.

---

# Authoritative Sources

## Primary Sources

1. **NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2026**
   - Direct gastric-cancer guidance on liquid biopsy and ctDNA.
   - Supports blood-based ctDNA genomic testing, detection of mutations/alterations/fusions, potential targetable alterations, tumor-clone evolution, selected use when tissue is limited or traditional biopsy is not possible, and cautious interpretation of negative results.

2. **NCCN Gastric Cancer Clinical Practice Guidelines in Oncology — Liquid Biopsy section**
   - Direct source for the clinical boundary and safety interpretation of ctDNA in gastric cancer.

---

## Supporting Sources

- **PP-0236 — Liquid Biopsy Discussion Batch**
  - Locked architecture and boundary between liquid biopsy and ctDNA.
- **ESMO/ASCO Global Curriculum 2023**
  - Supporting framework for molecular oncology and genomic testing education.
- **NCI / ACS gastric cancer educational materials**
  - Supporting patient-education context.

---

# Evidence Classification

## Evidence Model

**Authoritative Educational Synthesis**

---

## Evidence Hierarchy

### Level 1

- NCCN Clinical Practice Guidelines in Oncology
- ESMO/ASCO oncology education framework

### Level 2

- NCI
- ACS

### Supporting Internal Governance Sources

- Locked PP-0236 Discussion Batch
- Locked Gold Population Package Specification v1.0

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

# Future Update Trigger

This Knowledge Passport should be reviewed if:

- NCCN substantially revises gastric-cancer guidance concerning ctDNA or liquid biopsy.
- Major oncology guidelines change the clinical role of blood-based genomic testing.
- Major evidence changes the interpretation of ctDNA in gastric cancer.
- Clinical use of ctDNA monitoring, resistance assessment, or MRD becomes sufficiently established to require a scope update.
- A dedicated downstream Population Package is created for ctDNA monitoring/MRD.
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

This Knowledge Passport is the official governance metadata for **PP-0237** and is compliant with the locked **Gold Population Package Specification v1.0**.

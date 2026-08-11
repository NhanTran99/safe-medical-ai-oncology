# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|-------|-------|
| Knowledge Passport ID | KP-PP-0234 |
| Population Package ID | PP-0234 |
| Clinical Knowledge Object | CKO-PP-0234 |
| Title | Germline Genetic Testing |
| Clinical Domain | Risk & Prevention / Understanding Cancer |
| Clinical Domain Code | RP / UC |
| Population Batch | Understanding Cancer / Risk & Prevention |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Status | Approved |

---

# Knowledge Classification

| Field | Value |
|-------|-------|
| Knowledge Type | Foundational Medical Knowledge |
| Educational Category | Hereditary Cancer / Cancer Genetics |
| Educational Level | Introductory |
| Clinical Complexity | Intermediate |
| Intended Audience | General public, patients diagnosed with cancer, people with suspected hereditary cancer risk, caregivers |
| Reading Level | Plain Language |
| Knowledge Granularity | Atomic (Single Educational Question) |
| Knowledge Scope | Germline Genetic Testing |

---

# Primary Educational Question

> **What is Germline Genetic Testing and when might it be appropriate in gastric cancer care?**

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

Germline testing may be considered before cancer develops in people with suspected inherited risk, after cancer diagnosis when hereditary susceptibility is suspected, or during cancer care when a tumor result raises the possibility of a germline finding. The package therefore spans the patient journey rather than a single treatment stage.

---

# Intended Runtime Usage

## Primary Runtime Role

- Foundational education on germline genetic testing.
- Hereditary cancer risk education.
- Explanation of why inherited genetic testing may be considered.

---

## Secondary Runtime Role

- Patient counseling support
- Health-literacy support
- Shared decision-making support
- Distinction between germline and somatic testing
- Knowledge graph integration
- Retrieval support for hereditary gastric-cancer questions

---

# Typical Trigger Questions

- What is germline genetic testing?
- Is germline testing the same as tumor genetic testing?
- Why would I need inherited genetic testing?
- Can someone without cancer have germline testing?
- Does my family history matter?
- Why is genetic testing relevant to gastric cancer?
- What is a multigene panel?
- What happens before genetic testing?
- What does a VUS mean?
- What does a negative genetic test mean?
- Can genetic testing find something unexpected?
- Can my genetic result affect my family?
- Why do I need a germline test after tumor sequencing?

---

# Retrieval Priority

**Very High**

**Reason:**

Germline genetic testing is a core bridge between hereditary cancer risk, clinical genomics, variant interpretation, somatic testing, genetic counseling, and family-risk workflows.

It is also a critical safety boundary because tumor-derived findings that may be germline require appropriate confirmation rather than automatic labeling as inherited.

---

# Knowledge Graph

## Prerequisite Population Packages

- PP-0015 — Biomarker Testing for Gastric Adenocarcinoma
- PP-0016 — HER2 Testing for Gastric Adenocarcinoma
- PP-0107 — Variant Interpretation
- PP-0233 — Clinical Genomics
- Molecular / genomic testing fundamentals

---

## Related Population Packages

| PP / Topic | Relationship |
|------------|--------------|
| PP-0097 | Biomarker Testing |
| PP-0107 | Variant Interpretation |
| PP-0233 | Clinical Genomics |
| PP-0235 | Somatic Genetic Testing |
| Hereditary Gastric Cancer | Disease context |
| Genetic Counseling | Counseling/support process |
| Cascade Genetic Testing | Family-testing workflow |
| Variant Classification | Downstream interpretation |
| Molecular Tumor Profiling | Related genomic testing |

---

## Recommended Next Population Package

**PP-0235 — Somatic Genetic Testing**

---

# Clinical Scope

## Included

- Definition of germline genetic testing
- Germline vs somatic testing
- Gastric-cancer relevance
- Affected and unaffected individuals
- Personal and family history
- Conceptual testing approaches
- Single-gene testing
- Multigene panels
- Pretest education and informed consent at conceptual level
- Pathogenic/likely pathogenic results
- VUS
- Negative results
- Unexpected/secondary findings
- Family implications
- Confirmatory germline testing after suspicious tumor findings
- Limitations

---

## Explicitly Excluded

- Detailed genetic counseling methodology
- Detailed HDGC eligibility criteria
- CDH1 management
- CTNNA1 management
- ACMG/AMP evidence codes
- Detailed variant interpretation
- Detailed sequencing methodology
- Cascade-testing workflow
- Disease-specific surveillance algorithms
- Treatment recommendations

These subjects remain delegated to independent Population Packages or clinical guidance.

---

# Authoritative Sources

## Primary Sources

1. National Cancer Institute (NCI) — Genetics of Gastric Cancer (PDQ)
2. National Cancer Institute (NCI) — Hereditary Diffuse Gastric Cancer (PDQ)
3. National Cancer Institute (NCI) — Cancer Genetics Risk Assessment and Counseling (PDQ)
4. ESMO/ASCO — Global Curriculum in Medical Oncology, Edition 2023
5. NCCN — Gastric Cancer Guidelines, Version 2.2026

---

## Supporting Sources

- American Cancer Society educational materials
- Ministry of Health of Vietnam — gastric cancer guidance where relevant to local context
- Disease-specific hereditary cancer guidance as delegated to downstream packages

---

# Evidence Classification

## Evidence Model

**Authoritative Educational Synthesis**

---

## Evidence Hierarchy

### Level I

- NCI PDQ
- ESMO/ASCO Global Curriculum
- NCCN Clinical Practice Guidelines

### Supporting

- American Cancer Society
- Vietnamese Ministry of Health gastric cancer guidance
- Disease-specific hereditary cancer guidance

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
| 1.0.0 | 2026-08-08 | Initial Revised Gold Release following locked PP-0234 discussion |

---

# Final Status

**APPROVED**

This Knowledge Passport is the official governance metadata for **PP-0234 — Germline Genetic Testing** and is aligned with the locked Gold Population Package structure.

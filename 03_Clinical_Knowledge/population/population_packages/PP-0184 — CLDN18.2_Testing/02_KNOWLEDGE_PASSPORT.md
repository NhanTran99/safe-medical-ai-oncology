# 02_KNOWLEDGE_PASSPORT — PP-0184: CLDN18.2 Testing

## 1. Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0184 |
| PP ID | PP-0184 |
| Population Package Title | CLDN18.2 Testing for Gastric Adenocarcinoma |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Artifact Role | Knowledge Passport |
| Clinical Domain | Diagnosis / Biomarker Testing / Precision Oncology |
| Population | Patients with gastric adenocarcinoma |
| Primary Clinical Question | What is CLDN18.2 testing, when is it used, how is it interpreted, and why can it affect targeted-treatment selection? |
| Last Updated | 2026-08-09 |

---

## 2. Knowledge Classification

### Knowledge Type

**Foundational biomarker-testing knowledge product**

### Primary Function

Explain the clinical purpose and interpretation of CLDN18.2 testing.

### Knowledge Level

**Foundational → intermediate**

The package is patient-facing but includes clinically exact biomarker terminology and threshold interpretation.

### Clinical Role

**Treatment-selection biomarker**

### Biomarker Class

**Tumor protein-expression biomarker assessed by IHC**

### Primary Specimen

**Tumor tissue**

### Primary Assessment Method

**Qualitative immunohistochemistry (IHC)**

---

## 3. Patient Journey Classification

| Dimension | Classification |
|---|---|
| Journey stage | Diagnosis → Pathology → Biomarker testing → Treatment selection |
| Immediate trigger | Advanced/recurrent disease and consideration of CLDN18.2-directed treatment |
| Main patient question | “Why am I being tested for CLDN18.2?” |
| Main result | CLDN18.2-positive / CLDN18.2-negative |
| Main downstream consequence | Whether CLDN18.2-directed therapy may be clinically relevant |
| Relationship to treatment | Predictive / treatment-selection context |
| Relationship to prognosis | Not a standalone prognostic package |

---

## 4. Intended Runtime Usage

This package is intended to support:

1. Patient education before or after biomarker testing.
2. Explanation of a CLDN18.2 pathology result.
3. Explanation of why tissue testing is needed.
4. Explanation of the ≥75% threshold.
5. Explanation of 2+/3+ membranous staining.
6. Explanation of why CLDN18.2 testing is performed in advanced disease.
7. Explanation of why CLDN18.2 status is interpreted with HER2, PD-L1, MSI/MMR and other clinical information.
8. Explanation of the relationship between CLDN18.2 positivity and zolbetuximab consideration.
9. Correction of common misconceptions about CLDN18.2.
10. Retrieval by clinical knowledge systems when the user asks about CLDN18.2 testing, positivity, IHC, or biomarker-guided treatment selection.

---

## 5. Retrieval / Runtime Relevance

### High-priority retrieval concepts

- CLDN18.2
- Claudin 18 isoform 2
- CLDN18.2 testing
- CLDN18.2 IHC
- CLDN18.2 positive
- CLDN18.2 negative
- 75% viable tumor cells
- 2+ / 3+ staining
- membranous staining
- gastric adenocarcinoma
- zolbetuximab
- biomarker testing
- targeted therapy
- FFPE tumor tissue
- biopsy specimen
- surgical specimen

### Common patient-language retrieval variants

- “What is CLDN18.2?”
- “Why do I need CLDN18.2 testing?”
- “Is CLDN18.2 a blood test?”
- “What does CLDN18.2 positive mean?”
- “What does CLDN18.2 negative mean?”
- “What does 75% mean on CLDN18.2?”
- “What does 2+ or 3+ mean?”
- “Can CLDN18.2 positive mean I get zolbetuximab?”
- “Is CLDN18.2 the same as HER2?”
- “Is CLDN18.2 the same as PD-L1?”

### Exclusion-trigger concepts

If the user asks primarily about:

- detailed CLDN18.2 molecular biology;
- IHC laboratory procedure;
- detailed pathology scoring;
- zolbetuximab dosing or toxicity;
- HER2 testing methodology;
- PD-L1 CPS;
- MSI/MMR methodology;

the runtime should retrieve the corresponding specialized PP rather than treating PP-0184 as the primary source.

---

## 6. Knowledge Graph

### Prerequisite

- PP-0013 — Targeted Therapy for Gastric Adenocarcinoma
- PP-0015 — Biomarker Testing for Gastric Adenocarcinoma
- PP-0006 — How Is Gastric Adenocarcinoma Diagnosed?
- PP-0007 — Understanding Your Pathology Report
- Biopsy/pathology foundations where required by the active project graph

### Parallel

- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0180 — Gastric Cancer Molecular Classification

### Downstream

- CLDN18.2 Biology
- CLDN18.2 IHC Testing
- CLDN18.2 Scoring
- CLDN18.2-targeted Therapy
- Zolbetuximab
- Companion Diagnostics

### Conceptual graph

```text
Biomarker Testing
        |
        v
CLDN18.2 Testing
        |
        +----> CLDN18.2-positive / negative interpretation
        |
        +----> CLDN18.2 Biology
        |
        +----> CLDN18.2 IHC Testing
        |
        +----> CLDN18.2 Scoring
        |
        +----> CLDN18.2-targeted Therapy
        |
        +----> Zolbetuximab
        |
        +----> Companion Diagnostics
```

Parallel biomarker branches remain separate:

```text
                +--> HER2 Testing
Biomarker -----+--> PD-L1 Testing
Testing        +--> MSI/MMR Testing
                +--> CLDN18.2 Testing
```

---

## 7. Clinical Scope

### Core

- CLDN18.2 identity and basic clinical significance.
- Purpose of testing.
- Current testing context.
- Timing.
- Tumor specimen.
- Biopsy/surgical specimen.
- FFPE context.
- IHC.
- Membranous staining.
- 2+/3+ intensity.
- ≥75% viable tumor-cell threshold.
- Positive/negative interpretation.
- Treatment-selection relevance.
- Relationship to zolbetuximab.
- Relationship to HER2, PD-L1 and MSI/MMR.
- Core limitations and misconceptions.

### Supporting

- Prevalence range.
- Histologic associations.
- Tumor heterogeneity concept.
- EBV relationship as an uncertain association.
- SPOTLIGHT and GLOW as evidence explaining why the biomarker has treatment relevance.
- Companion-diagnostic concept.

### Explicitly excluded

- Detailed molecular biology.
- Detailed IHC laboratory methods.
- Detailed scoring methodology.
- Detailed drug treatment.
- Drug toxicity management.
- Individualized treatment selection.
- Other biomarker methodology.

---

## 8. Authoritative Sources

### Primary guideline source

**NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026**

Most important sections:

- Principles of Pathologic Review and Biomarker Testing (GAST-B)
- CLDN18.2 assessment
- Systemic therapy for unresectable locally advanced, recurrent or metastatic disease

### Additional core source

**NCI Gastric Cancer Treatment (PDQ®)**

Used to support the treatment context and evidence surrounding zolbetuximab in CLDN18.2-positive disease.

### Project source set

The PP Registry identifies the CLDN18.2 testing package primary source set as:

**NCCN + JNCCN + NCI PDQ + ACS + ESMO**

The current artifact prioritizes the directly relevant guideline and NCI evidence contained in the project Source Files.

---

## 9. Evidence Classification

### Level 1 — Direct guideline / high-authority clinical evidence

- NCCN v2.2026 CLDN18.2 testing criteria.
- NCCN v2.2026 treatment context.
- NCI PDQ treatment evidence.

### Level 2 — Randomized clinical-trial evidence summarized by authoritative sources

- SPOTLIGHT.
- GLOW.

### Level 3 — Supporting clinicopathologic evidence

- prevalence;
- histologic associations;
- molecular-marker relationships;
- EBV association.

### Evidence handling rule

Where the source distinguishes established guideline-supported facts from uncertain associations, the package preserves that distinction.

---

## 10. Governance Metadata

| Field | Value |
|---|---|
| Governance framework | CORE_WORKING_RULES v1.6 |
| Artifact specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0 |
| Discussion reference | PP Discussion depth and format example |
| Execution trigger | Approved / Locked PP-0184 Decision Batch |
| Production mode | Gold 4-artifact package |
| Boundary rule | Mandatory, clean four-part boundary |
| Depth rule | Absolute full-depth; not compacted; equal to or deeper than Gold reference |
| Evidence rule | Source-first; no unsupported clinical expansion |
| Package sequence rule | User-controlled explicit PP request |
| QA framework | Four-layer Content / Clinical / Educational / Governance QA |

---

## 11. Version Control

### Version

**1.0.0**

### Production basis

Approved and locked PP-0184 Decision Batch.

### Change policy

- Minor content update without architecture change → MINOR.
- Corrective factual/traceability update without scope change → PATCH.
- Architecture/scope change → MAJOR only after explicit governance decision.

---

## 12. Change History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold Knowledge Passport production. |

---

## 13. Final Status

**GOLD — READY FOR INTEGRATION**

Artifact is designed for repository integration as the Knowledge Passport component of PP-0184.

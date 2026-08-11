# PP-0188 — Molecular Subtypes of Gastric Cancer
## Knowledge Passport

**KP ID:** KP-PP-0188  
**PP ID:** PP-0188  
**Version:** 1.0.0  
**Status:** GOLD — LOCKED / READY FOR INTEGRATION  
**Last Updated:** 2026-08-09

---

# 1. Identity

| Field | Value |
|---|---|
| PP ID | PP-0188 |
| Clinical Topic | Molecular Subtypes of Gastric Cancer |
| CKO | CKO-PP-0188 |
| Knowledge Passport | KP-PP-0188 |
| Population Wave | Wave 1 |
| Version | 1.0.0 |
| Lifecycle Status | Gold / Ready for Integration |
| Primary Clinical Domain | Gastric Cancer — Molecular Classification |
| Intended Audience | Patients, caregivers, patient-facing clinical education runtime |

---

# 2. Knowledge Classification

## 2.1 Knowledge Type

**Clinical education / disease understanding / molecular classification**

## 2.2 Primary Clinical Question

> What major molecular-subtyping frameworks have been developed for gastric cancer, what are their defining biological and clinical characteristics, how do TCGA and ACRG compare, and what do these classifications mean clinically?

## 2.3 Atomic Knowledge Unit

This package owns the **molecular-subtype landscape and comparison of major gastric-cancer molecular-subtyping frameworks**.

It does not own detailed testing methodology or treatment selection.

## 2.4 Clinical Complexity

**Moderate–High**

Reason:

- multiple classification systems;
- overlapping terminology;
- molecular biology;
- prognostic associations;
- important distinction between research classification and clinical biomarkers.

## 2.5 Educational Level

**Patient-centered with clinically accurate molecular terminology**

---

# 3. Patient Journey Classification

## Primary Journey Stage

**Diagnosis → Molecular Characterization / Risk Context**

## Secondary Journey Stages

- Prognosis understanding
- Treatment planning context
- Precision-oncology education

## Important Journey Boundary

The package provides context for molecular findings but does not prescribe treatment.

---

# 4. Intended Runtime Usage

This PP is intended to support patient questions such as:

- “What is a molecular subtype of gastric cancer?”
- “What are the TCGA subtypes?”
- “What are the ACRG subtypes?”
- “What is the difference between TCGA and ACRG?”
- “Is MSI a molecular subtype?”
- “Does molecular subtype replace Lauren classification?”
- “Does molecular subtype replace stage?”
- “Does my molecular subtype tell me what treatment I need?”
- “Why can two gastric cancers behave differently?”

---

# 5. Retrieval / Runtime Relevance

## High-priority retrieval concepts

- gastric cancer molecular subtypes
- molecular classification gastric cancer
- TCGA
- ACRG
- EBV subtype
- MSI subtype
- genomically stable
- chromosomal instability
- MSS/EMT
- MSS/TP53+
- MSS/TP53−
- gastric cancer heterogeneity
- molecular subtype prognosis
- molecular subtype recurrence
- TCGA vs ACRG

## Retrieval disambiguation

When a query mentions:

- **EBV testing** → retrieve PP-0168 for detailed testing; PP-0188 for TCGA subtype context.
- **MSI/MMR testing** → retrieve PP-0182 for testing; PP-0188 for subtype context.
- **HER2 / PD-L1 / CLDN18.2 / TMB / FGFR2** → retrieve the corresponding biomarker PP; PP-0188 only supplies subtype-level context.
- **NGS report interpretation** → retrieve PP-0189.
- **targeted/immunotherapy treatment selection** → retrieve PP-0190 / PP-0191 and relevant treatment PPs.

---

# 6. Knowledge Graph

## Prerequisites

- PP-0003 — What is Gastric Adenocarcinoma?
- PP-0007 — Understanding Your Pathology Report
- PP-0008 — Understanding Cancer Staging (TNM Staging)
- PP-0178 — Histopathologic Classification
- PP-0179 — Lauren Classification
- PP-0180 — Gastric Cancer Molecular Classification

## Closely Related

- PP-0168 — EBV-associated Gastric Cancer + EBV Testing
- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0184 — CLDN18.2 Testing
- PP-0185 — Tumor Mutational Burden (TMB)
- PP-0186 — FGFR2 Testing
- PP-0187 — NGS Biomarker Testing

## Downstream

- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0190 — Biomarker Testing for Targeted Therapy
- PP-0191 — Biomarker Testing for Immunotherapy

---

# 7. Clinical Scope

## Core

- TCGA molecular classification;
- EBV, MSI, GS, CIN;
- ACRG molecular classification;
- MSI, MSS/EMT, MSS/TP53+, MSS/TP53−;
- subtype biology;
- selected clinical phenotype;
- prognosis and recurrence associations;
- TCGA–ACRG comparison;
- non-equivalence;
- relationship with pathology, Lauren classification, and TNM stage;
- distinction between subtype and individual biomarker;
- current implementation limits.

## Supporting

- selected gene examples;
- immune biology;
- genomic instability;
- recurrence-pattern context;
- retrospective treatment-response evidence;
- translational precision-oncology context.

## Explicitly Excluded

- detailed assay methodology;
- variant interpretation;
- molecular report interpretation;
- detailed classifier algorithms;
- treatment algorithms;
- individualized prognostic prediction;
- routine universal TCGA/ACRG testing.

---

# 8. Authoritative Sources

## Primary clinical / governance anchor

1. **NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026** — current guideline context for gastric-cancer molecular characterization and clinically actionable biomarker testing.

## Primary molecular-subtyping evidence

2. **Cancer Genome Atlas Research Network. Comprehensive molecular characterization of gastric adenocarcinoma. Nature. 2014;513:202–209.**  
   Foundational TCGA molecular characterization.

3. **Sohn BH, et al. Clinical significance of four molecular subtypes of gastric cancer identified by The Cancer Genome Atlas project. Clin Cancer Res. 2017;23:4441–4449. doi:10.1158/1078-0432.CCR-16-2211.**  
   Clinical validation of TCGA subtypes, survival associations, and retrospective chemotherapy-response analysis. [S1]

4. **Cristescu R, et al. Molecular analysis of gastric cancer identifies subtypes associated with distinct clinical outcomes. Nat Med. 2015. doi:10.1038/nm.3850.**  
   Foundational ACRG molecular classification, independent validation, prognosis and recurrence patterns. [S2]

---

# 9. Evidence Classification

## Tier A — Foundational / High-authority

- TCGA gastric molecular characterization.
- ACRG molecular classification.
- Current NCCN clinical framework.

## Tier B — Independent validation

- Sohn et al. TCGA clinical validation in MD Anderson and Samsung Medical Center cohorts.
- ACRG validation in SMC-2, Singapore, and TCGA gastric cohorts.

## Tier C — Exploratory / Translational

- retrospective subtype-associated chemotherapy benefit;
- subtype-specific biological hypotheses;
- possible simplified classifier development.

## Interpretation rule

Tier C evidence must not be converted into routine treatment recommendations.

---

# 10. Governance Metadata

| Field | Value |
|---|---|
| Governance Status | LOCKED |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0 |
| Working Rules | CORE_WORKING_RULES v1.6 |
| Artifact Set | CKO + KP + Primary Evidence Package + QA |
| Boundary Required | Yes |
| Final QA Language | PASS — GOLD — READY FOR INTEGRATION |
| Source-first rule | Applied |
| Adjacent-package overlap check | Applied |
| Patient-facing safety boundary | Applied |

---

# 11. Boundary

**Core = major molecular-subtyping frameworks of gastric cancer; TCGA and ACRG classification systems; subtype definitions; biological characteristics; key clinical/prognostic and recurrence associations; comparison and non-equivalence of TCGA and ACRG; relationship of molecular subtype to histology, stage, and individual biomarkers; research-versus-clinical implementation distinction.**

**Supporting = immune biology, genomic instability, selected gene examples, recurrence-pattern context, exploratory treatment-response evidence, molecular heterogeneity and precision-oncology context.**

**Explicitly Excluded = detailed histopathology/WHO/Lauren classification, individual biomarker assay methodology, NGS technical methodology, variant interpretation, genomic-report interpretation, detailed subtype prediction algorithms, universal TCGA/ACRG testing, individualized prognosis, subtype-specific treatment prescription, routine subtype-guided chemotherapy/immunotherapy, hereditary/germline classification, longitudinal molecular monitoring.**

**Delegated-to PP = PP-0168, PP-0181, PP-0182, PP-0183, PP-0184, PP-0185, PP-0186, PP-0187, PP-0189, PP-0190, PP-0191, and relevant treatment Population Packages.**

---

# 12. Version Control

**Version:** 1.0.0

**Change type:** Initial Gold production after full Decision Batch approval/lock.

**Change impact:** New knowledge package; no prior PP-0188 artifact superseded.

---

# 13. Final Status

**Knowledge Passport Status: PASS — GOLD — READY FOR INTEGRATION.**

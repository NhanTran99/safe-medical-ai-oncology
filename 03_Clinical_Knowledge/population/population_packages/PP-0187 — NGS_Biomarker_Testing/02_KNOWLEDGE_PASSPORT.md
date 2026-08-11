# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

---

# Identity

| Field | Value |
|---|---|
| Population Package ID | PP-0187 |
| Title | NGS Biomarker Testing |
| Domain | Gastric Cancer — Molecular Biomarker Testing |
| Package Type | Patient-facing Population Package |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Atomic Knowledge Type | Clinical molecular-testing platform |
| Primary Educational Question | What is NGS biomarker testing, what can it test for in gastric cancer, and when may it be useful? |

---

# Knowledge Classification

## Primary Classification

**Molecular Diagnostics / Biomarker Testing / Next-Generation Sequencing**

## Secondary Classifications

- Precision Oncology
- Genomic Testing
- Multigene Panel Testing
- Somatic Molecular Testing
- Gastric Cancer Biomarker Testing

## Knowledge Type

**Conceptual + clinical-use + patient-education**

The package is not a technical laboratory manual and is not a treatment algorithm.

---

# Patient Journey Classification

| Journey Stage | Relevance |
|---|---|
| Diagnosis | Supporting |
| Molecular characterization | **Core** |
| Risk/prognostic assessment | Supporting, not primary |
| Treatment selection | Downstream relationship |
| Treatment monitoring | Supporting only |
| Recurrence surveillance | Out of scope |

The primary role of PP-0187 is to explain the molecular-testing layer that can sit between clinical/pathologic assessment and downstream interpretation or treatment decisions.

---

# Intended Runtime Usage

PP-0187 should be retrieved when the user asks:

- What is NGS?
- Why would someone with gastric cancer have NGS?
- What can an NGS test look for?
- What is a multigene panel?
- Is NGS the same as a biomarker?
- Can NGS test several biomarkers at once?
- Can NGS test HER2/MSI/TMB/other genomic findings?
- When might NGS be considered?
- Can NGS be performed from blood?
- What does a negative NGS test mean?
- Does NGS replace biopsy?
- Does NGS automatically determine treatment?

PP-0187 should not be the primary retrieval target for detailed variant interpretation, genomic-report reading, or drug selection.

---

# Retrieval / Runtime Relevance

## High-Relevance Retrieval Concepts

- NGS
- next-generation sequencing
- molecular profiling
- genomic profiling
- multigene panel
- genomic biomarker testing
- gastric cancer NGS
- validated NGS
- tissue NGS
- blood-based genomic testing
- comprehensive genomic profiling

## Related Retrieval Concepts

- HER2 amplification
- MSI
- TMB
- gene fusion
- mutation
- amplification
- deletion
- FGFR2
- BRAF
- NTRK
- RET
- ctDNA

## Do Not Conflate

- NGS ≠ biomarker
- NGS ≠ gene panel
- NGS ≠ genomic report interpretation
- NGS ≠ variant interpretation
- NGS ≠ germline testing
- NGS ≠ treatment selection
- NGS ≠ ctDNA
- NGS ≠ molecular classification

---

# Knowledge Graph

## Upstream

- PP-0097 — Biomarker Testing
- PP-0099 — Molecular Testing
- PP-0101 — Next-Generation Sequencing
- PP-0102 — Gene Panel Testing
- PP-0110 — Somatic Genetic Testing
- PP-0180 — Gastric Cancer Molecular Classification

## Parallel / Adjacent

- PP-0181 — HER2 Testing
- PP-0182 — MSI/MMR Testing
- PP-0183 — PD-L1 Testing
- PP-0184 — CLDN18.2 Testing
- PP-0185 — Tumor Mutational Burden (TMB)
- PP-0186 — FGFR2 Testing
- PP-0112 — Circulating Tumor DNA

## Downstream

- PP-0188 — Molecular Subtypes of Gastric Cancer
- PP-0189 — Genomic Test Results / How to Read a Molecular Report
- PP-0190 — Biomarker Testing for Targeted Therapy
- PP-0191 — Biomarker Testing for Immunotherapy
- PP-0208 — Targeted Therapy in Gastric Cancer

---

# Clinical Scope

## Core Clinical Concept

NGS is a molecular-testing technology capable of evaluating multiple genes and molecular events in parallel. In gastric cancer, NGS can provide broader genomic information than a test focused on one biomarker.

The package explains:

**clinical question**
→ **specimen**
→ **validated molecular test**
→ **NGS / multigene profiling**
→ **molecular findings**
→ **interpretation**
→ **clinical relevance**

PP-0187 owns the NGS/molecular-profiling layer and only introduces the downstream layers conceptually.

---

# Evidence Classification

## Established / Guideline-Supported

The supplied NCCN v2.2026 source directly supports:

- universal MSI testing by PCR/NGS or MMR testing by IHC in newly diagnosed patients;
- NGS consideration through a validated assay;
- IHC/ISH/targeted gene PCR as preferred initial approaches to biomarker assessment;
- consideration of NGS through a CLIA-approved laboratory later in the clinical course when sufficient tumor tissue is available;
- NGS's ability to assess multiple mutations and other molecular events such as amplification, deletions, TMB and MSI;
- selected blood-based NGS-based comprehensive genomic profiling/MGPT when tissue is limited or biopsy is not feasible in appropriate advanced/metastatic disease contexts.

## Context-Dependent

- broader molecular profiling;
- repeat molecular assessment;
- tumor molecular evolution;
- potential identification of targetable alterations;
- treatment relevance of findings.

## Not Established by This Package

- universal comprehensive NGS for every gastric-cancer patient;
- one universal NGS panel;
- a single commercial assay as preferred;
- exact analytical thresholds;
- universal treatment decisions from NGS findings.

---

# Authoritative Sources

## Primary

1. **NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2026**
   - Principles of Pathologic Review and Biomarker Testing
   - NGS Biomarker Testing
   - Liquid Biopsy / ctDNA section
   - Gastric-cancer biomarker framework

## Supporting Project Sources

- NCI gastric-cancer materials supplied in the project.
- ACS gastric-cancer materials supplied in the project.
- ESMO/ASCO curriculum material supplied in the project.
- Project governance and Gold artifact references.

The package prioritizes the supplied guideline evidence for gastric-cancer-specific clinical claims.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0 |
| Discussion Standard | Approved PP Discussion depth and format example |
| Execution Rule | User-controlled explicit PP sequence |
| Evidence Rule | Source-first; no unsupported clinical filling |
| Package Structure | CKO + Knowledge Passport + Primary Evidence Package + QA |
| Boundary Rule | Required, four-part ownership format |
| QA Framework | Content / Clinical / Educational / Governance |

---

# Scope Ownership

## Core Ownership

PP-0187 owns:

- NGS as a clinical testing platform;
- broader genomic/multigene profiling;
- molecular-event classes detectable in principle;
- clinical context for NGS consideration;
- specimen adequacy at conceptual level;
- validated testing;
- conceptual interpretation of positive/negative results;
- limitations of broader genomic testing.

## Supporting Ownership

PP-0187 may explain relationships to:

- HER2;
- MSI;
- TMB;
- FGFR2;
- BRAF;
- NTRK;
- RET;
- ctDNA;
- precision oncology.

These are examples or relationships, not duplicated biomarker packages.

## Explicit Exclusions

Technical NGS workflow, variant interpretation, report reading, germline counseling, individualized treatment, commercial assays, and detailed ctDNA monitoring are excluded.

## Delegation

| Topic | Delegated Package |
|---|---|
| Variant interpretation | PP-0106 |
| ctDNA biology/monitoring | PP-0112 |
| HER2 testing | PP-0181 |
| MSI/MMR | PP-0182 |
| PD-L1 | PP-0183 |
| CLDN18.2 | PP-0184 |
| TMB | PP-0185 |
| FGFR2 | PP-0186 |
| Molecular subtypes | PP-0188 |
| Genomic report interpretation | PP-0189 |
| Biomarker testing for targeted therapy | PP-0190 |
| Biomarker testing for immunotherapy | PP-0191 |
| Targeted therapy | PP-0208 and downstream packages |

---

# Runtime Safety / Interpretation Guardrails

1. Do not present NGS as universally required.
2. Do not present NGS as universally superior to IHC/ISH/PCR.
3. Do not equate a molecular finding with treatment eligibility.
4. Do not equate negative NGS with absence of cancer or absence of all genomic alterations.
5. Do not equate tumor NGS with germline testing.
6. Do not interpret an NGS result without the appropriate downstream clinical context.
7. Do not provide individualized treatment recommendations from this package alone.
8. Do not substitute NGS for biopsy/pathology/staging.

---

# Version Control

| Version | Date | Status | Change |
|---|---|---|---|
| 1.0.0 | 2026-08-09 | GOLD | Initial production after PP-0187 Decision Batch lock |

---

# Change History

Initial Gold package created after the Project Coordinator approved and locked the PP-0187 Decision Batch.

---

# Final Status

**GOLD — READY FOR INTEGRATION**

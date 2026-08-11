# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0175 |
| PP ID | PP-0175 |
| Title | Gastric Cancer Diagnostic Work-up |
| Version | 1.0.0 |
| Status | Approved / Gold |

## Knowledge Classification

| Field | Value |
|---|---|
| Clinical Domain | Diagnosis |
| Educational Level | Intermediate |
| Clinical Complexity | Intermediate–High |
| Patient Journey Stage | Suspicion → Diagnosis → Initial Staging |
| Knowledge Granularity | Atomic diagnostic-work-up pathway package |
| Primary Clinical Question | How is gastric cancer evaluated after it is suspected or detected, and how are the tests combined to confirm diagnosis and determine disease extent? |

## Patient Journey Classification

### Primary Stage

Diagnostic evaluation after clinical suspicion or an abnormal finding.

### Secondary Stage

Initial disease characterization and staging preparation.

### Downstream Transition

Diagnostic work-up → confirmed diagnosis → clinical staging → treatment-planning readiness.

## Intended Runtime Usage

### Primary Runtime Usage

Explain the integrated process that follows suspicion of gastric cancer.

### Secondary Runtime Usage

- Explain why multiple tests may be required.
- Explain the role of endoscopy and biopsy.
- Explain why imaging follows or accompanies tissue confirmation.
- Explain selected roles of CT, PET/CT, EUS and laparoscopy.
- Explain why diagnosis and staging are related but different.
- Route detailed test-specific questions to downstream PPs.
- Prevent universal-test or universal-sequence misconceptions.

## Retrieval / Runtime Relevance

**Very High**

### Retrieval Tags

gastric cancer diagnosis; diagnostic work-up; gastric cancer tests; EGD; upper endoscopy; biopsy; pathology; CT; PET/CT; EUS; staging laparoscopy; Siewert; biomarker testing; gastric cancer staging; diagnostic pathway

# Knowledge Graph

## Prerequisite

- PP-0019 — Symptoms
- PP-0170 — High-Risk Screening
- PP-0171 — Endoscopic Screening
- PP-0172 — Serum Pepsinogen Screening
- PP-0173 — High-Incidence Populations
- PP-0174 — Screening Harms and False Results

## Related

- PP-0165 — Atrophic Gastritis
- PP-0166 — Intestinal Metaplasia
- PP-0167 — Pernicious Anemia
- PP-0169 — Gastric Adenomas
- PP-0176 — Endoscopic Diagnosis
- PP-0177 — Biopsy Strategy
- PP-0178 — Histopathology
- PP-0179 — Lauren Classification
- PP-0180 — Molecular Classification

## Next / Downstream

- PP-0176
- PP-0177
- PP-0178
- PP-0179
- PP-0180
- PP-0181+
- Dedicated staging/imaging packages
- Treatment packages

# Clinical Scope

## Core

The integrated gastric-cancer diagnostic work-up from clinical suspicion through diagnostic confirmation, disease characterization and initial staging assessment, including clinical assessment, upper endoscopy as the diagnostic entry point, tissue confirmation, cross-sectional imaging, selected EUS/PET-CT/laparoscopy, Siewert/location assessment, and the interface with pathology and clinically relevant biomarker testing.

## Supporting

Laboratory/organ-function assessment, nutritional assessment, family-history and H. pylori context, multidisciplinary interpretation, and patient-facing explanation of why multiple tests may be needed.

## Explicitly Excluded

Detailed endoscopic diagnosis, detailed biopsy technique, histopathologic classification, Lauren classification, molecular classification, biomarker-specific testing/interpretation, detailed CT/PET/EUS/laparoscopy methodology, full TNM/stage-group teaching, individualized diagnostic interpretation, and all treatment selection or treatment-management recommendations.

## Delegated-to PP

PP-0176 Endoscopic Diagnosis, PP-0177 Endoscopic Biopsy Strategy, PP-0178 Histopathologic Classification, PP-0179 Lauren Classification, PP-0180 Molecular Classification, PP-0181+ Biomarker Testing, dedicated staging/imaging packages, PP-0192–0194 Endoscopic Resection/EMR/ESD, and downstream Gastric Cancer Treatment packages.

# Authoritative Sources

1. NCCN Clinical Practice Guidelines in Oncology: Gastric Cancer, Version 2.2026
2. Vietnam Ministry of Health — Hướng dẫn chẩn đoán và điều trị ung thư dạ dày, Quyết định 3127/QĐ-BYT (2020)
3. American Cancer Society — Stomach Cancer / Tests for Stomach Cancer, revised February 27, 2026
4. NCI — Stomach Cancer Diagnosis / related gastric-cancer clinical materials in the supplied source set
5. PP Registry / Population Registry — PP-0175 identity and adjacent-package ownership
6. CORE_WORKING_RULES v1.6
7. FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0
8. Approved PP Discussion depth and format example
9. Approved Gold Population Package artifact examples

# Evidence Classification

## Established / directly source-supported

- Gastric-cancer work-up includes clinical assessment, endoscopy/biopsy and additional tests for characterization and staging.
- Histopathology is the definitive diagnostic basis in the supplied Vietnam guideline.
- CT contributes to assessment of disease extent.
- EUS can assess local depth and nearby nodes.
- PET/CT and MRI can provide additional imaging information in selected contexts.
- Staging laparoscopy is used selectively.
- NCCN integrates relevant biomarker testing into the gastric-cancer work-up.
- Early gastric cancer may require specialized endoscopic/pathologic assessment.

## Context-dependent

- Which tests are required for an individual patient.
- When PET/CT is useful.
- When EUS is needed.
- When staging laparoscopy is indicated.
- Which biomarker tests are appropriate for the disease context.
- Whether additional testing is needed after a nondiagnostic or discordant result.

## Not established universally

- One identical test sequence for every patient.
- One universal imaging set for all patients.
- One universal PET/CT indication independent of disease context.
- One universal EUS indication for every gastric-cancer patient.
- One universal staging-laparoscopy requirement.
- Treatment decisions based solely on one diagnostic test.

# Governance Metadata

| Field | Value |
|---|---|
| Source-First Verification | Completed |
| Relevant Clinical Sources | Identified |
| Adjacent PP Overlap Review | Completed |
| Decision Batch | Approved / Locked |
| Gold Specification | Compliant |
| Artifact Depth | Full-depth / non-compacted |
| Evidence Traceability | Complete |
| Boundary | Declared in production response |
| QA | PASS — GOLD |
| Repository Readiness | Ready |

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Full-depth Gold production after locked Decision Batch |

# Change History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold artifact after PP-0175 approval/lock |

# Final Status

**APPROVED — GOLD — READY FOR INTEGRATION**

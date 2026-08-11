# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0177 |
| PP ID | PP-0177 |
| Title | Endoscopic Biopsy Strategy |
| Version | 1.0.0 |
| Status | Approved / Gold |

## Knowledge Classification

| Field | Value |
|---|---|
| Clinical Domain | Diagnosis |
| Domain Focus | Endoscopic Tissue Acquisition |
| Educational Level | Intermediate |
| Clinical Complexity | Intermediate–High |
| Patient Journey Stage | Endoscopic Diagnosis → Tissue Acquisition → Pathology |
| Knowledge Granularity | Specialized gastric-cancer endoscopic biopsy strategy |
| Primary Clinical Question | How should suspicious gastric findings be sampled so that tissue is adequate and representative for diagnosis and downstream testing? |

## Patient Journey Classification

### Primary Stage

Tissue acquisition after a suspicious endoscopic finding.

### Secondary Stage

Specimen adequacy, representativeness and resolution of sampling limitations.

### Downstream Transition

Biopsy → pathology → histologic classification → molecular/biomarker testing → staging/treatment planning.

## Intended Runtime Usage

### Primary Runtime Usage

Explain why gastric-cancer biopsies are taken and what makes a biopsy adequate.

### Secondary Runtime Usage

- Explain targeted versus random/mapping biopsy.
- Explain the multiple-biopsy principle.
- Explain the NCCN 6–8 recommendation.
- Explain why biopsy site matters.
- Explain why ulcerated lesions require particular attention.
- Explain adequate and representative tissue.
- Explain negative versus inadequate biopsy.
- Explain why diffuse/microscopic disease can be missed.
- Explain why repeat sampling may sometimes be necessary.
- Explain why biopsy tissue may need to support molecular testing.
- Route pathology interpretation to PP-0178 and biomarker interpretation to downstream packages.
- Route HDGC-specific surveillance to PP-0159.
- Route EMR/ESD procedure details to PP-0192–0194.

## Retrieval / Runtime Relevance

**Very High**

### Retrieval Tags

gastric cancer biopsy; endoscopic biopsy; biopsy strategy; targeted biopsy; random biopsy; mapping biopsy; 6–8 biopsies; standard-size forceps; larger forceps; biopsy adequacy; representative tissue; ulcerated lesion; superficial biopsy; false-negative biopsy; nondiagnostic biopsy; diffuse gastric cancer; linitis plastica; signet-ring cell; HDGC biopsy; molecular testing tissue; biomarker specimen

# Clinical Scope

## Core

Gastric-cancer-specific endoscopic tissue-acquisition strategy, including when suspicious gastric findings should be sampled, targeted versus context-specific random/mapping sampling, multiple-biopsy principles, the NCCN 6–8 biopsy recommendation, standard-size forceps, representative sampling, biopsy-site considerations, ulcerated-lesion sampling, tissue adequacy for histologic and molecular interpretation, limitations of superficial or nonrepresentative sampling, negative versus inadequate/nondiagnostic biopsy, repeat/additional sampling as a context-dependent response, and the diagnostic interface with larger endoscopic specimens.

## Supporting

Larger-forceps yield considerations, multiple-lesion sampling, specimen site documentation, microscopic/diffuse disease as a sampling limitation, selected post-treatment biopsy limitations, and patient-facing preparation for biopsy-result discordance.

## Explicitly Excluded

General endoscopy preparation, sedation/anesthesia, detailed forceps mechanics, pathology laboratory processing, histopathologic classification, Lauren classification, molecular classification, individual biomarker interpretation, EUS-guided FNA, H. pylori testing algorithms, precursor-lesion management, HDGC surveillance protocols, EMR/ESD technique, treatment selection, and individualized diagnostic recommendations.

## Delegated-to PP

PP-0175 Gastric Cancer Diagnostic Work-up, PP-0176 Endoscopic Diagnosis of Gastric Cancer, PP-0178 Histopathologic Classification, PP-0179 Lauren Classification, PP-0180 Gastric Cancer Molecular Classification, PP-0181–PP-0187 Biomarker/NGS Testing, PP-0159 HDGC Endoscopic Surveillance, PP-0192–PP-0194 Endoscopic Resection/EMR/ESD, and dedicated EUS/staging and treatment packages.

# Authoritative Sources

1. NCCN Gastric Cancer v2.2026 — GAST-A, supplied project source
2. NCI Hereditary Diffuse Gastric Cancer (PDQ®), supplied project source
3. American Cancer Society — Stomach Cancer, supplied project source
4. NCI stomach-cancer diagnostic/screening materials, supplied project source
5. Vietnam Ministry of Health — Hướng dẫn chẩn đoán và điều trị ung thư dạ dày, supplied project source
6. PP Registry.xlsx — PP identity and adjacent ownership
7. CORE_WORKING_RULES v1.6
8. FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.0
9. PP Discussion depth and format example.md
10. Approved Gold Population Package examples

# Evidence Classification

## Established / guideline-supported

- Suspicious gastric lesions should be biopsied.
- Multiple biopsies are recommended for gastric-cancer diagnostic sampling.
- NCCN specifies 6–8 biopsies using standard-size endoscopy forceps.
- Adequate biopsy material should support histologic and molecular interpretation.
- Ulcerated lesions require particular attention to adequate tissue.
- Larger forceps may improve biopsy yield.
- Selected small lesions may be evaluated with a larger specimen obtained by EMR/ESD.

## Strong supporting evidence

- The site of biopsy matters in ulcerating gastric lesions.
- Biopsy number has been studied in gastric and esophageal carcinoma.
- Diffuse gastric cancer may be missed by superficial biopsy.
- In HDGC surveillance, microscopic signet-ring-cell disease can be missed by targeted/random sampling, and random biopsy has an important selected role.

## Context-dependent

- Random/mapping biopsy.
- Sampling of normal-appearing mucosa.
- Larger forceps.
- Repeat/additional biopsy.
- Excisional endoscopic sampling.
- Post-treatment biopsy.

## Not established universally in the supplied source set

- One universal biopsy algorithm for every lesion.
- One universal edge-versus-base sampling formula for every ulcer.
- One universal repeat-biopsy interval.
- One universal random-biopsy protocol for ordinary gastric-cancer diagnosis.
- A guarantee that 6–8 biopsies will detect every gastric cancer.
- A rule that a negative biopsy always excludes cancer.

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
| 1.0.0 | 2026-08-09 | Full-depth Gold production after locked PP-0177 Decision Batch |

# Change History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold artifact after PP-0177 approval/lock |

# Final Status

**APPROVED — GOLD — READY FOR INTEGRATION**

# Quality Assurance Report

## Identity

| Field | Value |
|---|---|
| QA Report ID | QA-PP-0177 |
| PP ID | PP-0177 |
| Title | Endoscopic Biopsy Strategy |
| Version | 1.0.0 |
| Status | PASS — GOLD |

# Layer 1 — Content QA

| Criterion | Result |
|---|---|
| Atomic clinical question | PASS |
| Approved PP identity | PASS |
| Full-depth CKO structure | PASS |
| Full-depth Knowledge Passport | PASS |
| Full-depth Evidence Package | PASS |
| Granular knowledge blocks | PASS |
| Patient Explanation per block | PASS |
| Clinical Importance per block | PASS |
| Key Concepts per block | PASS |
| Common Misconceptions | PASS |
| Key Messages | PASS |
| Knowledge Graph | PASS |
| Revision History | PASS |
| Included scope | PASS |
| Not Included scope | PASS |

# Layer 2 — Clinical QA

| Criterion | Result |
|---|---|
| Source-first clinical grounding | PASS |
| NCCN v2.2026 GAST-A represented | PASS |
| NCCN 6–8 biopsy recommendation represented | PASS |
| Standard-size forceps represented | PASS |
| Adequate histologic/molecular material represented | PASS |
| Ulcerated-lesion emphasis represented | PASS |
| Larger-forceps yield consideration represented | PASS |
| Biopsy-site importance represented | PASS |
| Targeted versus random/mapping distinction | PASS |
| HDGC limitation appropriately bounded | PASS |
| Diffuse/linitis plastica limitation | PASS |
| Negative versus inadequate biopsy distinction | PASS |
| Repeat/additional sampling concept | PASS |
| Tissue adequacy for downstream testing | PASS |
| Routine biopsy versus EMR/ESD distinction | PASS |
| Post-treatment biopsy limitation | PASS |
| No universal unsupported protocol | PASS |
| No individualized procedural advice | PASS |
| No treatment recommendation | PASS |

# Layer 3 — Educational QA

| Criterion | Result |
|---|---|
| Patient-centered framing | PASS |
| Plain-language explanation | PASS |
| Medical terminology explained | PASS |
| One-concept-per-block architecture | PASS |
| Sampling strategy logically sequenced | PASS |
| Targeted/random distinction clear | PASS |
| Adequacy/representativeness distinction clear | PASS |
| Negative/inadequate distinction clear | PASS |
| Diagnostic limitations explicit | PASS |
| Common misconceptions addressed | PASS |
| Appropriate uncertainty | PASS |
| No alarmist wording | PASS |
| No individualized medical advice | PASS |

# Layer 4 — Governance QA

| Criterion | Result |
|---|---|
| CORE_WORKING_RULES v1.6 | PASS |
| Source-first rule | PASS |
| User-controlled PP sequence | PASS |
| Single locked Decision Batch | PASS |
| Discussion template adherence | PASS |
| Adjacent PP overlap check | PASS |
| Immediate Gold production | PASS |
| Gold Specification v1.0 | PASS |
| Four artifacts complete | PASS |
| Full-depth / non-compacted production | PASS |
| Boundary structure compliant | PASS |
| Knowledge Graph included | PASS |
| Evidence traceability included | PASS |
| Semantic versioning | PASS |
| Repository-ready structure | PASS |

# Full-Depth Compliance Check

This package was produced under the project's **absolute full-depth rule**.

The CKO contains **40 granular Clinical Knowledge Blocks**, each independently structured as:

1. Patient Explanation;
2. Clinical Importance;
3. Key Concepts.

The CKO additionally contains:

- Metadata;
- Educational Objectives;
- Scope;
- Included;
- Not Included;
- Common Misconceptions;
- Key Messages;
- Knowledge Graph;
- Prerequisite PPs;
- Related PPs;
- Next / Downstream PPs;
- Revision History.

The Knowledge Passport independently covers:

- Identity;
- Knowledge Classification;
- Patient Journey Classification;
- Intended Runtime Usage;
- Retrieval / Runtime Relevance;
- Clinical Scope;
- Authoritative Sources;
- Evidence Classification;
- Governance Metadata;
- Version Control;
- Change History;
- Final Status.

The Primary Evidence Package independently covers:

- Identity;
- Clinical Question;
- Educational Intent;
- Scope;
- Primary Evidence Sources;
- Supporting Sources;
- Evidence Hierarchy;
- Evidence Matrix;
- Evidence Notes;
- Clinical Claims Summary;
- Evidence Consistency Review;
- Evidence Gaps;
- Out-of-Scope Topics;
- Future Update Triggers;
- Source Traceability;
- Boundary Verification;
- Evidence Package Decision;
- Final Evidence Status.

The QA Report independently evaluates all four QA layers and contains a dedicated full-depth compliance audit.

**The package is explicitly non-compacted. It is designed to match or exceed the approved Gold reference depth and does not shorten or merge decision granularity to reduce length.**

# Boundary QA

**Boundary: Core = gastric-cancer-specific endoscopic tissue-acquisition strategy, including when suspicious gastric findings should be sampled, targeted versus context-specific random/mapping sampling, multiple-biopsy principles, the NCCN 6–8 biopsy recommendation, standard-size forceps, representative sampling, biopsy-site considerations, ulcerated-lesion sampling, tissue adequacy for histologic and molecular interpretation, limitations of superficial or nonrepresentative sampling, negative versus inadequate/nondiagnostic biopsy, repeat/additional sampling as a context-dependent response, and the diagnostic interface with larger endoscopic specimens; Supporting = larger-forceps yield considerations, multiple-lesion sampling, specimen site documentation, microscopic/diffuse disease as a sampling limitation, selected post-treatment biopsy limitations, and patient-facing preparation for biopsy-result discordance; Explicitly Excluded = general endoscopy preparation, sedation/anesthesia, detailed forceps mechanics, pathology laboratory processing, histopathologic classification, Lauren classification, molecular classification, individual biomarker interpretation, EUS-guided FNA, H. pylori testing algorithms, precursor-lesion management, HDGC surveillance protocols, EMR/ESD technique, treatment selection, and individualized diagnostic recommendations; Delegated-to PP = PP-0175 Gastric Cancer Diagnostic Work-up, PP-0176 Endoscopic Diagnosis of Gastric Cancer, PP-0178 Histopathologic Classification, PP-0179 Lauren Classification, PP-0180 Gastric Cancer Molecular Classification, PP-0181–PP-0187 Biomarker/NGS Testing, PP-0159 HDGC Endoscopic Surveillance, PP-0192–PP-0194 Endoscopic Resection/EMR/ESD, and dedicated EUS/staging and treatment packages.**

# Architecture QA

The package occupies the correct layer between endoscopic diagnosis and pathology:

**PP-0175 — overall diagnostic work-up**

→ **PP-0176 — endoscopic visualization/localization/characterization**

→ **PP-0177 — endoscopic tissue-acquisition strategy**

→ **PP-0178 — histopathologic classification**

→ **PP-0179 — Lauren classification**

→ **PP-0180 — molecular classification**

→ **PP-0181+ — biomarker/NGS testing**

Selected high-risk surveillance sampling remains owned by **PP-0159**, while endoscopic resection remains owned by **PP-0192–0194**.

# Final QA Decision

## PASS

All four Gold artifacts are complete, full-depth, source-grounded, clinically bounded, and aligned with the approved/locked PP-0177 Decision Batch.

# QA Final Status

**PASS — GOLD — READY FOR INTEGRATION.**

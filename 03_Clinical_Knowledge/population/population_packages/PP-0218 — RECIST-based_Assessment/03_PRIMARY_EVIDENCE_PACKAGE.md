# Primary Evidence Package

---

# Identity

| Field | Value |
|---|---|
| Evidence Package ID | EP-PP-0218 |
| Population Package ID | PP-0218 |
| Title | RECIST-based Assessment |
| Version | 1.0.0 |
| Evidence Status | GOLD |
| Last Updated | 2026-08-09 |

---

# Clinical Question

> **How is a RECIST-based assessment constructed from measurable disease, target lesions, non-target disease and new lesions to produce an overall response assessment?**

---

# Educational Intent

Provide a clinically accurate, patient-facing explanation of how RECIST 1.1 is applied in practice.

The package intentionally sits between:

- foundational RECIST terminology;
- individual response-component packages;
- clinical response assessment;
- post-treatment imaging.

The Evidence Package therefore emphasizes the **integration of components into an overall RECIST-based result** rather than repeating definition-only material.

---

# Scope

## Core

- assessment context;
- baseline;
- measurable/non-measurable disease;
- target-lesion selection;
- target-lesion measurement;
- sum of longest diameters;
- longitudinal comparison;
- nadir;
- non-target disease;
- new lesions;
- lymph-node considerations;
- CR/PR/SD/PD;
- overall assessment;
- progression;
- response confirmation;
- measurement error;
- clinical-trial endpoint role;
- individual-patient limitation.

## Supporting

- RECIST vs RECIST 1.1;
- foundational PP relationships;
- imaging interface;
- gastric-cancer treatment context;
- iRECIST interface;
- patient-facing interpretation.

## Excluded

- detailed imaging acquisition;
- detailed radiology workflow;
- complete iRECIST;
- pseudo-progression algorithm;
- treatment decisions;
- prognosis;
- pathology response;
- surveillance;
- recurrence detection.

---

# Primary Evidence Source

## ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — Edition 2023

The supplied ESMO-ASCO source is the strongest direct source for PP-0218.

Its RECIST competency section explicitly requires understanding of:

- RECIST's purpose in harmonizing response definitions;
- application to solid tumors in locally advanced/metastatic settings;
- original RECIST versus RECIST v1.1;
- measurement error;
- imaging modality considerations;
- measurable versus non-measurable disease;
- CR, PR, SD, PD, early death and non-evaluable categories;
- target-lesion selection;
- maximum five lesions and maximum two per organ;
- sum of longest diameters;
- non-target disease;
- new lesions;
- lymph-node rules;
- response confirmation in selected single-arm trials;
- persistent PD once established;
- iRECIST;
- confirmed/unconfirmed progression and pseudo-progression;
- clinical judgment for individual-patient benefit. fileciteturn19file0

---

# Supporting Project Sources

## PP-0058 — RECIST

PP-0058 establishes the foundational definition and explicitly excludes:

- RECIST 1.1 technical criteria;
- target lesions;
- non-target lesions;
- measurable disease;
- CR/PR/SD/PD;
- sum of diameters;
- iRECIST.

This confirms that PP-0218 can own the downstream applied layer without rewriting PP-0058. fileciteturn19file15

## PP-0059 — RECIST 1.1

PP-0059 establishes RECIST 1.1 conceptually and explicitly excludes:

- target lesions;
- non-target lesions;
- measurable disease;
- number of target lesions;
- lymph-node measurement;
- CR/PR/SD/PD;
- sum of diameters;
- iRECIST.

This provides direct architectural justification for PP-0218 as the applied technical-assessment layer. fileciteturn19file5

## PP Registry

The Registry explicitly places:

- PP-0217 — Response Assessment;
- PP-0218 — RECIST-based Assessment;
- PP-0219 — Post-treatment Imaging;

in sequence and identifies PP-0218 as the dedicated RECIST package. fileciteturn19file3

---

# Evidence Hierarchy

## Level 1 — Direct professional response-assessment framework

ESMO-ASCO 2023.

## Level 1 / supporting

RECIST 1.1 Working Group framework as cited by ESMO-ASCO.

## Disease-specific context

NCCN Gastric Cancer Version 2.2026 and supplied gastric-cancer treatment materials.

## Educational architecture

PP-0058, PP-0059, PP Registry and locked project governance.

---

# Evidence Matrix

| Clinical Claim | Supporting Source | Status |
|---|---|---|
| RECIST was developed to harmonize tumor-response definitions | ESMO-ASCO 2023 | Established |
| RECIST applies to solid tumors in appropriate advanced/local-advanced response settings | ESMO-ASCO 2023 | Established |
| RECIST 1.1 is the revised framework | ESMO-ASCO + PP-0059 | Established |
| Measurement error affects response assessment | ESMO-ASCO 2023 | Established |
| Measurable and non-measurable disease are distinguished | ESMO-ASCO 2023 | Established |
| Up to 5 target lesions and 2 per organ are selected under RECIST 1.1 | ESMO-ASCO 2023 | Established |
| Sum of longest diameters contributes to assessment | ESMO-ASCO 2023 | Established |
| Non-target disease contributes to overall assessment | ESMO-ASCO 2023 | Established |
| New lesions contribute to progression assessment | ESMO-ASCO 2023 | Established |
| Lymph nodes have special RECIST considerations | ESMO-ASCO 2023 | Established |
| CR/PR/SD/PD are response categories | ESMO-ASCO 2023 | Established |
| Response confirmation can be required in selected single-arm trials | ESMO-ASCO 2023 | Context-dependent |
| Once RECIST PD is established, RECIST outcome remains PD | ESMO-ASCO 2023 | Established |
| iRECIST exists for trials testing immunotherapeutics | ESMO-ASCO 2023 | Established |
| Individual-patient treatment benefit cannot be determined from RECIST alone | ESMO-ASCO 2023 | Established |
| PP-0218 is distinct from PP-0058/0059 | PP-0058/0059 + Registry | Governance/architecture |
| PP-0218 is distinct from post-treatment imaging | Registry + project boundary | Governance/architecture |

---

# Evidence Note 1 — RECIST as a Standardized Endpoint Framework

ESMO-ASCO frames RECIST as an initiative designed to harmonize tumor-response definitions and create credible endpoints that can be used uniformly across centres and compared across trials.

Therefore PP-0218 should explain RECIST as a standardized **assessment method**, not as a biologic truth detector.

---

# Evidence Note 2 — Target-lesion Selection

The supplied ESMO-ASCO material specifies:

- maximum five target lesions;
- maximum two per organ.

The purpose is standardization of quantitative assessment.

This does not imply that other disease sites cease to matter.

---

# Evidence Note 3 — Sum of Longest Diameters

RECIST tracks the evolution of the sum of longest diameters of selected target lesions.

This creates a reproducible quantitative signal for longitudinal comparison.

The package therefore owns the concept and its role in overall assessment, while avoiding unnecessary duplication of a standalone target-lesion package.

---

# Evidence Note 4 — Non-target Disease

ESMO-ASCO explicitly requires understanding of how non-target disease is evaluated and integrated into the overall response assessment.

This is central to PP-0218.

A target-lesion sum is therefore not synonymous with the final RECIST response.

---

# Evidence Note 5 — New Lesions

New lesions are a separate axis of assessment.

Their appearance can establish progression according to RECIST.

This prevents the common patient misunderstanding:

> “If the original tumors got smaller, I must have responded.”

---

# Evidence Note 6 — Lymph Nodes

Lymph nodes require special attention.

ESMO-ASCO identifies specific rules for lymph nodes, including the significance of smaller nodes and nodes that disappear and later reappear.

Detailed technical rules remain within the RECIST technical architecture, while PP-0218 integrates the lymph-node component into overall assessment.

---

# Evidence Note 7 — Response Categories

CR, PR, SD and PD are the principal standard response categories.

PP-0218 does not replace the individual response-category packages.

Its ownership is:

> **How these categories are reached after integrating target, non-target and new-lesion information.**

---

# Evidence Note 8 — Progression

Progression can result from:

- target-disease increase meeting the applicable criteria;
- unequivocal non-target progression;
- new malignant lesions.

ESMO-ASCO explicitly notes that once PD is observed according to RECIST, the RECIST outcome remains PD regardless of what happens afterwards. fileciteturn19file0

---

# Evidence Note 9 — Measurement Error

Measurement error is explicitly recognized as an important issue.

Therefore:

- standardized methods matter;
- baseline/follow-up imaging choice matters;
- small changes near thresholds require careful interpretation.

This is a central limitation, not a minor technical footnote.

---

# Evidence Note 10 — Response Confirmation

ESMO-ASCO specifies confirmation of complete/partial response in single-arm trials when response is a primary endpoint.

The rationale is to reduce the possibility that an apparent response represents measurement error.

This is **not** a universal rule that every clinical response must always be confirmed.

---

# Evidence Note 11 — iRECIST

ESMO-ASCO identifies iRECIST as a specialized framework for trials testing immunotherapeutics.

PP-0218 therefore needs only an interface-level explanation:

**RECIST 1.1** is the conventional standardized framework.

**iRECIST** addresses specialized immune-response assessment in relevant trials.

The full iRECIST algorithm is excluded.

---

# Evidence Note 12 — Individual Patient

The most important clinical safety principle is:

> RECIST is an assessment framework, not an autonomous treatment decision system.

ESMO-ASCO states that for an individual patient, treatment benefit should be based on medical judgment synthesizing clinical, imaging and laboratory information. fileciteturn19file0

This principle should be preserved in all runtime use.

---

# Clinical Integration Model

```text
Baseline disease
      ↓
Identify measurable / non-measurable disease
      ↓
Select target lesions
      ↓
Measure target lesions
      ↓
Calculate / track sum of diameters
      ↓
Assess non-target disease
      ↓
Check for new lesions
      ↓
Apply RECIST rules
      ↓
CR / PR / SD / PD
      ↓
Overall RECIST-based assessment
      ↓
Broader clinical interpretation
      ↓
Treatment decision
```

The final arrow is deliberately outside PP-0218 ownership.

---

# Clinical Context Matrix

| Context | Role of PP-0218 |
|---|---|
| Locally advanced solid tumor | Standardized response-assessment framework where appropriate |
| Metastatic gastric cancer | Response assessment during systemic treatment |
| Clinical trial | Standardized endpoint assessment |
| Neoadjuvant gastric cancer | Conceptual interface; detailed imaging/surgical decisions delegated |
| Adjuvant setting | Limited/context-dependent because measurable residual disease may not be present |
| Immunotherapy trial | RECIST/iRECIST interface |
| Surveillance | Out of scope |
| Recurrence detection | Out of scope |

---

# Evidence Limitations

## Limitation 1 — RECIST is not universal

Not every patient or disease situation is best represented by RECIST.

## Limitation 2 — Measurement error

Measurements have uncertainty.

## Limitation 3 — Non-target disease

Some disease cannot be reduced to a single quantitative target-lesion sum.

## Limitation 4 — Treatment biology

Radiologic change may not capture every biologic effect of therapy.

## Limitation 5 — Immunotherapy

Immune-related response patterns may require specialized frameworks.

## Limitation 6 — Individual clinical benefit

RECIST cannot independently establish individual patient benefit.

## Limitation 7 — Pathology

Radiologic response and pathologic response are different endpoints.

---

# Evidence Gaps

1. No single RECIST schedule applies to every gastric-cancer treatment setting.
2. Exact imaging modality and acquisition are context-dependent.
3. Individual interpretation requires patient-specific imaging and clinical data.
4. Detailed iRECIST rules require a dedicated framework.
5. Treatment selection after progression is outside RECIST itself.
6. Prognostic interpretation requires outcomes beyond response classification.

---

# Boundary and Delegation Matrix

| Topic | Ownership |
|---|---|
| What is RECIST? | PP-0058 |
| What is RECIST 1.1? | PP-0059 |
| Target Lesions | PP-0060 |
| Measurable Disease | PP-0061 |
| Non-target Lesions | PP-0062 |
| Complete Response | PP-0063 |
| Partial Response | PP-0064 |
| Stable Disease | PP-0065 |
| Progressive Disease | PP-0066 |
| Response Assessment Algorithm | PP-0067 |
| Follow-up Imaging | PP-0068 |
| Clinical Response Assessment | PP-0217 |
| **RECIST-based Assessment** | **PP-0218** |
| Post-treatment Imaging | PP-0219 |
| Surveillance | PP-0220 |
| Recurrence Detection | PP-0221 |
| Recurrent Disease Management | PP-0222 |
| Metastatic Gastric Cancer | PP-0223 |
| Treatment Toxicity | PP-0231 |
| Multidisciplinary Management | PP-0232 |

---

# Source Traceability

## Source A — ESMO-ASCO 2023

Primary direct response-assessment source.

Supports:

- RECIST purpose;
- setting;
- measurement error;
- measurable/non-measurable disease;
- target-lesion selection;
- sum of diameters;
- non-target disease;
- new lesions;
- lymph nodes;
- CR/PR/SD/PD;
- response confirmation;
- PD persistence;
- iRECIST;
- individual-patient limitation. fileciteturn19file0

## Source B — PP-0058

Supports the foundational scope boundary and confirms technical content was intentionally excluded from the introductory RECIST package. fileciteturn19file15

## Source C — PP-0059

Supports the architectural distinction between conceptual RECIST 1.1 education and technical implementation. fileciteturn19file5

## Source D — PP Registry

Supports PP-0217 / PP-0218 / PP-0219 package ownership and sequence. fileciteturn19file3

---

# Future Update Triggers

Review when:

- RECIST 1.1 changes;
- RECIST Working Group publishes a major revision;
- ESMO/ASCO updates response-assessment competencies;
- iRECIST changes;
- major gastric-cancer evidence changes response-assessment practice;
- PP-0219 changes imaging ownership;
- PP-0060–0067 boundaries change;
- governance changes.

---

# Evidence Package Decision

**GOLD — EVIDENCE TRACEABLE — READY FOR INTEGRATION**

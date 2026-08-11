# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0219 |
| Population Package ID | PP-0219 |
| Clinical Knowledge Object | CKO-PP-0219 |
| Title | Post-treatment Imaging |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment Response / Imaging / Post-treatment Assessment |
| Clinical Domain Code | TRA-IMG |
| Population Wave | Wave 1 |
| Audience | Patients, caregivers, general oncology learners |
| Reading Level | Plain language with essential medical terminology explained |
| Knowledge Granularity | Atomic clinical educational package |
| Scope Status | APPROVED / LOCKED |
| Source Strategy | Project Source Files first |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / post-treatment imaging literacy.

## Educational Category

Treatment assessment / imaging / restaging.

## Educational Level

Intermediate conceptual clinical education.

## Clinical Complexity

Intermediate-to-advanced conceptual level, because the package connects imaging, restaging, response assessment and treatment context while deliberately delegating technical implementation.

## Atomic Clinical Question

> **How is imaging used after treatment for gastric cancer to reassess the disease, support restaging, and inform the next clinical assessment?**

## Primary Function

This PP is the **post-treatment imaging reassessment node**.

It explains the clinical role of imaging after a treatment milestone, including:

- why imaging is performed;
- when it is performed;
- what imaging modality may be selected;
- how the scan is compared with baseline/prior imaging;
- what findings may be seen;
- how findings connect with restaging and response assessment;
- why imaging does not independently determine treatment.

---

# Patient Journey Classification

| Stage | Applicable |
|---|---|
| Before Diagnosis | |
| During Diagnosis | |
| Treatment Decision | ✓ |
| Active Treatment | ✓ |
| Immediate Post-treatment Assessment | ✓ |
| Follow-up | ✓ |
| Long-term Surveillance | Supporting distinction only |
| Recurrence Assessment | Supporting distinction only |
| Survivorship | |
| Palliative Care | Context-dependent |

### Reason

Patients may encounter post-treatment imaging after:

- perioperative/systemic treatment;
- neoadjuvant treatment;
- selected immunotherapy pathways;
- surgery or other treatment milestones;
- treatment when the disease state needs to be reassessed.

The PP is primarily positioned between treatment and subsequent response/restaging or management assessment.

---

# Intended Runtime Usage

## Primary Runtime Role

Post-treatment imaging education.

## Secondary Runtime Roles

- Restaging education.
- Imaging-report orientation.
- Treatment-response education.
- RECIST interface explanation.
- Patient preparation for oncology/radiology discussions.
- Clarification of the difference between reassessment and surveillance.
- Explanation of why additional testing may be required.

## Typical Trigger Questions

- Why do I need a scan after chemotherapy?
- Why am I having a CT after neoadjuvant treatment?
- When should I have imaging after treatment?
- What is a restaging scan?
- Why are they comparing my new scan with the old one?
- What does residual disease on a scan mean?
- What does no evidence of disease on CT mean?
- Why would I need PET/CT after treatment?
- Why would I need MRI instead of CT?
- Why do I need endoscopy and biopsy after imaging?
- What does a new spot on my post-treatment scan mean?
- Is post-treatment imaging the same as surveillance?
- Is RECIST the same as my CT scan?
- Does a good scan mean I am cured?

## Retrieval Priority

**Very High** for users asking about imaging after treatment, restaging, response assessment, or post-treatment scan interpretation.

### Reason

PP-0219 is the dedicated bridge between treatment and imaging-based reassessment. It prevents the runtime system from collapsing:

- post-treatment imaging;
- response assessment;
- RECIST;
- surveillance;
- recurrence detection

into one undifferentiated concept.

---

# Retrieval / Runtime Relevance

## High-Priority Terms

- post-treatment imaging
- post-treatment scan
- restaging
- restaging scan
- reassessment after treatment
- CT after chemotherapy
- CT after neoadjuvant therapy
- imaging after surgery
- imaging after immunotherapy
- imaging after treatment
- baseline scan
- follow-up scan
- compare scans
- treatment response imaging
- residual disease
- persistent disease
- new lesion
- new finding
- indeterminate finding
- treatment-related changes
- radiologic response
- metabolic response
- no evidence of disease

## Modality Terms

- CT
- contrast CT
- chest abdomen pelvis CT
- PET/CT
- FDG-PET/CT
- MRI
- contrast
- oral contrast
- IV contrast

## Clinical Context Terms

- perioperative therapy
- neoadjuvant therapy
- preoperative therapy
- MSI-H
- dMMR
- immunotherapy
- immune checkpoint inhibitor
- surgery
- resectability
- restaging
- response assessment

## Assessment Terms

- RECIST
- RECIST 1.1
- response assessment
- complete response
- partial response
- stable disease
- progressive disease
- iRECIST

## Downstream Terms

- surveillance
- recurrence
- recurrence detection
- recurrent gastric cancer
- next treatment
- multidisciplinary review

---

# Clinical Scope

## Core Ownership

PP-0219 owns the clinical educational layer connecting a treatment milestone to post-treatment imaging and reassessment.

It owns:

1. purpose of post-treatment imaging;
2. clinical-question framing;
3. treatment-context-dependent timing;
4. post-treatment restaging;
5. clinical-level modality selection;
6. CT role;
7. selected PET/CT role;
8. selected MRI role;
9. baseline/prior comparison;
10. longitudinal interpretation;
11. residual/persistent findings;
12. new and indeterminate findings;
13. treatment-related imaging changes;
14. imaging-to-response interface;
15. imaging limitations;
16. multidisciplinary interpretation;
17. patient-facing interpretation;
18. distinction from surveillance and recurrence detection.

## Supporting Ownership

PP-0219 may introduce:

- contrast-enhanced imaging;
- EGD/biopsy interface;
- laparoscopy interface;
- radiologic/metabolic response;
- immunotherapy-specific response-assessment considerations;
- measurement uncertainty;
- imaging-report terminology.

## Explicitly Excluded

- detailed imaging methodology;
- detailed RECIST/iRECIST rules;
- long-term surveillance schedules;
- recurrence algorithms;
- pathology;
- treatment selection;
- individualized interpretation.

---

# Knowledge Units

## KU-01 — Post-treatment imaging definition

Post-treatment imaging is imaging performed after a treatment milestone to answer a defined clinical question about the current disease state.

## KU-02 — Restaging

Restaging reassesses disease extent after treatment and may inform whether disease is resectable, unresectable or metastatic in the relevant pathway.

## KU-03 — Timing

Timing is treatment-context dependent.

## KU-04 — CT

CT is a major modality for relevant gastric-cancer post-treatment assessment/restaging.

## KU-05 — PET/CT

FDG-PET/CT may be used when clinically indicated.

## KU-06 — MRI

MRI can serve as an alternative in selected circumstances.

## KU-07 — Baseline comparison

Post-treatment findings are interpreted against prior/baseline imaging.

## KU-08 — Residual abnormality

Residual imaging abnormality does not automatically equal viable tumor.

## KU-09 — New finding

A new finding requires clinical interpretation and does not automatically equal recurrence.

## KU-10 — Treatment-related change

Treatment may alter imaging appearance.

## KU-11 — RECIST interface

Imaging supplies information used in standardized response assessment; RECIST is not synonymous with the scan.

## KU-12 — Additional assessment

Endoscopy, biopsy or laparoscopy may be needed in selected situations.

## KU-13 — Clinical integration

Imaging is integrated with symptoms, examination, laboratory findings, pathology, treatment history and clinical judgment.

## KU-14 — Surveillance distinction

Post-treatment assessment is distinct from long-term surveillance.

## KU-15 — Recurrence distinction

Recurrence detection is a downstream clinical concept.

---

# Evidence Classification

## Established / Guideline-Supported

- Gastric-cancer pathways include post-treatment assessment and restaging.
- Chest/abdomen/pelvis CT with oral and IV contrast is a major restaging approach in relevant NCCN pathways.
- FDG-PET/CT may be used when clinically indicated.
- Selected treatment pathways include EGD and biopsy as part of response assessment.
- A treatment-specific post-therapy assessment window can be defined; NCCN gives an example of approximately 5–8 weeks after preoperative therapy in the specified pathway.
- CT with contrast may be considered when pre-treatment findings require more accurate anatomic assessment after treatment.
- Follow-up/surveillance is distinct from post-treatment assessment.
- Imaging modality and measurement error matter in response assessment.
- RECIST does not replace comprehensive clinical judgment.

## Context-Dependent

- Exact imaging timing.
- CT versus PET/CT versus MRI.
- Need for contrast.
- Need for EGD/biopsy.
- Need for additional imaging.
- Interpretation of residual abnormality.
- Interpretation of new or indeterminate findings.
- Imaging assessment after immunotherapy.
- Need for multidisciplinary review.

## Not Owned by This PP

- Detailed modality methodology.
- RECIST technical criteria.
- iRECIST algorithm.
- Surveillance schedules.
- Recurrence algorithms.
- Treatment selection.
- Individualized prognosis.

---

# Authoritative Sources

## Primary Project Sources

1. **Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology**
   - GAST-3: response assessment and additional management.
   - GAST-4: post-preoperative treatment assessment in specified pathways.
   - GAST-6: post-treatment assessment and restaging.
   - GAST-7: follow-up/surveillance distinction.
   - Relevant discussion sections.

2. **ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology — Edition 2023**
   - Response evaluation / RECIST.
   - Imaging modality and measurement error.
   - Individual-patient clinical judgment.
   - Multidisciplinary imaging review.
   - iRECIST context for immunotherapy trials.

## Supporting Project Sources

3. **NCI — Treatment of Stomach Cancer**
   - Patient-facing treatment/assessment context.

4. **ACS — Stomach Cancer**
   - Patient-facing gastric-cancer treatment and follow-up context.

5. **ACS — Immunotherapy for Stomach Cancer**
   - Immunotherapy context relevant to response assessment.

6. **NCI / PDQ gastric-cancer materials**
   - General treatment and disease-course context.

7. **Approved project Gold Discussion reference**
   - `PP Discussion depth and format example.md`
   - Used for structure, reasoning depth, boundary treatment and patient-facing architecture.

8. **PP Registry**
   - Used to preserve ownership relationships and adjacent package boundaries.

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 / locked execution standard |
| Discussion Reference | PP Discussion depth and format example.md |
| Source Strategy | Source-First |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Boundary | Required once in final production response |
| Package Structure | CKO + KP + Primary Evidence Package + QA |
| ZIP Required | Yes |
| User Sequence Authority | Project Coordinator explicit PP request |

---

# Knowledge Graph

## Prerequisite

**PP-0068 — Follow-up Imaging**

Provides foundational understanding of repeated imaging and longitudinal comparison.

**PP-0069 — CT Scan**

Provides CT-specific modality knowledge.

**PP-0070 — MRI**

Provides MRI-specific modality knowledge.

**PP-0071 — PET/CT**

Provides PET/CT-specific modality knowledge.

**PP-0072 — Contrast Agent**

Provides contrast-specific knowledge.

**PP-0217 — Response Assessment**

Provides the broader clinical response-assessment concept.

**PP-0218 — RECIST-based Assessment**

Provides formal standardized response assessment.

## Related

- PP-0203 — Perioperative Chemotherapy
- PP-0204 — FLOT
- PP-0205 — Adjuvant Therapy
- PP-0206 — Neoadjuvant Therapy
- PP-0207 — Chemoradiation
- PP-0213 — Immunotherapy in Gastric Cancer
- PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy
- PP-0231 — Treatment-related Toxicity and Supportive Care
- PP-0232 — Multidisciplinary Management of Gastric Cancer

## Next / Downstream

- PP-0220 — Surveillance After Gastric Cancer Treatment
- PP-0221 — Recurrence Detection
- PP-0222 — Management of Recurrent Gastric Cancer

---

# Boundary Map

| Topic | PP-0219 Ownership | Other Ownership |
|---|---|---|
| Repeated/follow-up imaging concept | Supporting | PP-0068 |
| Post-treatment imaging event | Core | PP-0219 |
| CT technical methodology | Excluded | PP-0069 |
| MRI technical methodology | Excluded | PP-0070 |
| PET/CT technical methodology | Excluded | PP-0071 |
| Contrast safety | Supporting only | PP-0072 |
| Clinical response assessment | Interface | PP-0217 |
| RECIST technical assessment | Excluded | PP-0218 |
| Long-term surveillance | Excluded | PP-0220 |
| Recurrence detection | Excluded | PP-0221 |
| Recurrent disease management | Excluded | PP-0222 |
| Treatment selection | Excluded | Treatment-specific PPs |
| Multidisciplinary governance | Supporting | PP-0232 |

---

# Safety / Runtime Rules

1. Never interpret a generic post-treatment imaging statement as an individualized diagnosis.
2. Never equate “no evidence of disease” with guaranteed cure.
3. Never equate a new finding with recurrence without clinical confirmation.
4. Never recommend or stop treatment based solely on an imaging phrase.
5. Never provide a universal imaging schedule when the treatment context is unknown.
6. Never imply that PET/CT is universally superior to CT.
7. Never imply that MRI universally replaces CT.
8. Never collapse RECIST into imaging itself.
9. Never collapse post-treatment assessment into long-term surveillance.
10. Never use this PP as a substitute for radiologist or oncology review.
11. Preserve treatment-specific uncertainty.
12. For immunotherapy, acknowledge specialized response-assessment frameworks without reproducing iRECIST technical algorithms.
13. Where source evidence is context-dependent, retain the context.
14. Where additional testing may be needed, present it as a possible clinical pathway rather than a universal requirement.

---

# Version Control

| Item | Value |
|---|---|
| Current Version | 1.0.0 |
| Major | 1 |
| Minor | 0 |
| Patch | 0 |

---

# Change History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold release after PP-0219 Decision Batch approval/lock. |

---

# Future Update Triggers

Review PP-0219 when:

1. NCCN materially changes post-treatment assessment or restaging pathways.
2. NCCN changes the recommended role of CT, PET/CT or MRI.
3. New gastric-cancer treatment pathways materially change the timing or purpose of post-treatment imaging.
4. New immunotherapy response-assessment frameworks alter clinical practice.
5. RECIST or iRECIST undergoes a major conceptual revision.
6. ESMO/ASCO changes recommendations about imaging in response assessment.
7. New evidence changes the interpretation of radiologic/metabolic complete response.
8. The PP Registry changes adjacent ownership.
9. A new dedicated PP is created that assumes any currently delegated topic.
10. Governance or Gold specification changes.

---

# Final Status

**GOLD — READY FOR INTEGRATION**

# PP-0231 — Treatment-related Toxicity and Supportive Care — Knowledge Passport

**Artifact:** `02_KNOWLEDGE_PASSPORT.md`  
**Version:** v1.0.0  
**Status:** GOLD — READY FOR INTEGRATION

---

# 1. Identity

| Field | Value |
|---|---|
| PP ID | PP-0231 |
| Title | Treatment-related Toxicity and Supportive Care |
| Domain | Gastric Cancer — Treatment Safety / Supportive Care |
| Knowledge Type | Cross-cutting clinical education |
| Audience | Patients, caregivers, clinicians, knowledge-retrieval systems |
| Patient Journey Position | Treatment → toxicity recognition → supportive management → treatment continuity/modification → long-term effects |
| Status | GOLD |
| Version | v1.0.0 |
| Source Authority | Project Source Files + locked governance |

---

# 2. Knowledge Classification

**Primary classification:** Treatment safety / supportive care.

**Secondary classifications:**

- adverse-event recognition;
- treatment toxicity;
- symptom management;
- patient safety;
- treatment tolerance;
- supportive care;
- long-term treatment sequelae;
- multidisciplinary toxicity management.

**Atomicity principle:**

PP-0231 owns the **toxicity/supportive-management problem space**, not the treatment-selection problem space.

---

# 3. Clinical Domain

Gastric adenocarcinoma treatment-related toxicity across:

- chemotherapy;
- radiotherapy;
- targeted therapy;
- immunotherapy;
- combination treatment.

The package is intentionally cross-cutting so that toxicity knowledge is retrievable regardless of which treatment package established the upstream treatment exposure.

---

# 4. Patient Journey Classification

**Primary journey:** Treatment.

**Secondary journeys:**

- treatment monitoring;
- patient safety;
- survivorship;
- long-term follow-up;
- supportive care.

Canonical pathway:

**Treatment exposure**

→ **potential toxicity**

→ **recognition**

→ **clinical assessment**

→ **severity**

→ **supportive/preventive management**

→ **monitoring**

→ **continue / delay / modify / stop when clinically indicated**

→ **recovery / chronic sequela management**

---

# 5. Intended Runtime Usage

Retrieve PP-0231 when a user asks:

- what side effects a gastric-cancer treatment can cause;
- how treatment toxicity is recognized;
- how side effects are assessed;
- whether a symptom may be treatment-related;
- why toxicity grading matters;
- how chemotherapy toxicity is supported;
- how radiation toxicity is supported;
- how targeted-therapy toxicity is recognized;
- how immunotherapy-related toxicity differs;
- whether toxicity can affect treatment continuation;
- what supportive care means in the setting of treatment toxicity;
- what long-term treatment effects may require support.

Do not use PP-0231 as the primary retrieval node for:

- selecting a cancer treatment;
- regimen sequencing;
- detailed dosing;
- detailed response assessment;
- RECIST;
- surveillance;
- recurrence detection;
- general survivorship;
- general palliative care;
- general best supportive care.

---

# 6. Clinical Scope

## Core

- Treatment-related toxicity definition.
- Toxicity recognition.
- Clinical assessment.
- Severity/grading concepts.
- Patient-reported toxicity.
- Acute versus chronic toxicity.
- Chemotherapy toxicity.
- Radiotherapy toxicity.
- Targeted-therapy toxicity.
- Immunotherapy toxicity.
- Prevention/prophylaxis.
- Supportive management.
- Monitoring.
- Treatment delay/modification/cessation interface.
- Toxicity-related patient safety.
- Multidisciplinary toxicity management.

## Supporting

- Nutrition/hydration interface.
- Rehabilitation.
- Psychologic impact.
- Quality of life.
- Long-term treatment sequelae.
- Relative-dose-intensity interface.
- Survivorship/follow-up interface.

## Excluded

- Treatment selection.
- Treatment sequencing.
- Individualized dosing.
- Full CTCAE tables.
- Drug-specific dose-reduction algorithms.
- Complete ICI-toxicity protocols.
- Radiation planning.
- Detailed nutrition.
- Detailed rehabilitation.
- Detailed cancer-pain management.
- General BSC.
- General palliative care.
- Individualized clinical decisions.

---

# 7. Knowledge Units

## KU-01 — Toxicity definition

Treatment-related toxicity is a treatment-associated adverse effect or sequela requiring recognition and, when clinically significant, assessment and management.

## KU-02 — Causality

A symptom during treatment is not automatically caused by treatment.

## KU-03 — Assessment

History, examination and appropriate diagnostic tests help identify cause and severity.

## KU-04 — Grading

Standardized systems such as CTCAE support communication and management.

## KU-05 — Prevention

Evidence-based prophylactic strategies can reduce toxicity.

## KU-06 — Supportive management

Supportive care can reduce symptom burden and support treatment delivery.

## KU-07 — Chemotherapy toxicity

Includes gastrointestinal, hematologic, neurologic, mucosal, skin and constitutional domains.

## KU-08 — Radiotherapy toxicity

Includes skin, GI, fatigue, hematologic and nutritional/hydration effects, with possible late effects.

## KU-09 — Targeted therapy toxicity

Toxicity is target/drug specific; selected gastric-cancer examples include hypertension, bleeding, thrombosis, GI perforation, pulmonary toxicity and GI/laboratory effects.

## KU-10 — Immunotherapy toxicity

Immune-related adverse events have a distinctive multi-organ spectrum.

## KU-11 — Treatment modification

Clinically significant toxicity can result in monitoring, delay, modification or cessation.

## KU-12 — Long-term toxicity

Some effects persist after treatment and intersect with survivorship and long-term follow-up.

## KU-13 — Multidisciplinary care

Toxicity may require oncology, nursing, pharmacy, nutrition, rehabilitation and specialty input.

## KU-14 — Patient safety

Patients should report important new or worsening symptoms and follow treatment-team contact instructions.

---

# 8. Evidence Classification

## Established / guideline-supported

- toxicity assessment;
- toxicity grading;
- prevention;
- supportive management;
- patient education;
- patient-reported toxicity;
- multidisciplinary toxicity management;
- treatment delay/modification/cessation when toxicity is unacceptable;
- acute versus chronic toxicity.

Primary source: ESMO-ASCO 2023.

## Gastric-cancer-specific supported

- chemotherapy toxicity domains;
- gastric radiation toxicity;
- selected targeted-therapy toxicities;
- immune-related toxicity in gastric-cancer treatment;
- treatment-specific adverse-event context.

Primary sources: NCCN, NCI, ACS.

## Context-dependent

- exact management;
- dose modification;
- prophylaxis choice;
- monitoring frequency;
- specialist referral;
- treatment continuation.

These require individual clinical context.

---

# 9. Authoritative Sources

### Tier 1 — Project governance

- CORE_WORKING_RULES v1.7.
- FREEZE GOLD POPULATION PACKAGE SPECIFICATION.
- PP Registry.
- approved Gold Discussion example.

### Tier 2 — Disease-specific guidance

- NCCN Gastric Cancer.
- NCI Gastric Cancer Treatment / PDQ.

### Tier 3 — Oncology education / patient evidence

- ESMO-ASCO 2023.
- American Cancer Society gastric-cancer treatment materials.

---

# 10. Evidence-to-Knowledge Mapping

| Knowledge domain | Primary source | Use |
|---|---|---|
| General systemic toxicity management | ESMO-ASCO | Core framework |
| Toxicity grading | ESMO-ASCO | Core |
| Prophylaxis | ESMO-ASCO | Core |
| Patient-reported toxicity | ESMO-ASCO | Core |
| Multidisciplinary management | ESMO-ASCO | Core |
| Treatment modification | ESMO-ASCO | Core |
| Gastric chemotherapy | ACS/NCI/NCCN | Gastric-specific examples |
| Gastric radiation toxicity | ACS | Gastric-specific examples |
| Targeted therapy | NCCN/NCI/ACS | Drug-class examples |
| Immunotherapy toxicity | NCCN/ESMO-ASCO/ACS | High-priority safety domain |
| Survivorship interface | ACS/NCCN | Boundary/supporting |

---

# 11. Knowledge Graph

## Upstream

Treatment-strategy and treatment-specific PPs establish the treatment exposure.

## PP-0231

Owns the toxicity-management layer.

## Downstream

- PP-0229 Survivorship.
- PP-0230 Long-term Follow-up.
- PP-0232 Multidisciplinary Management.

## Parallel/supportive relationships

- PP-0227 Palliative Care.
- PP-0228 Best Supportive Care.
- dedicated nutrition;
- rehabilitation;
- cancer pain;
- immunotherapy-toxicity packages.

---

# 12. Boundary Map

| Neighbor | Ownership distinction |
|---|---|
| PP-0203–0208 | Treatment strategy; PP-0231 owns treatment toxicity |
| PP-0209–0216 | Therapy-specific treatment; PP-0231 owns toxicity |
| PP-0217 | Response assessment, not toxicity assessment |
| PP-0218 | RECIST, not toxicity |
| PP-0219 | Imaging, not toxicity |
| PP-0227 | Palliative-care architecture |
| PP-0228 | Broad best supportive care |
| PP-0229 | Survivorship |
| PP-0230 | Long-term follow-up |
| PP-0232 | Overall MDT architecture |

---

# 13. Safety / Runtime Rules

1. Do not diagnose an individual.
2. Do not infer causality from one symptom.
3. Do not prescribe treatment.
4. Do not tell patients to stop cancer therapy.
5. Do not provide individualized dose modifications.
6. Do not reproduce complete toxicity protocols.
7. Preserve treatment-specific context.
8. Distinguish toxicity from progression and unrelated illness.
9. Direct real-world management to the treating team.
10. Preserve evidence uncertainty.

---

# 14. Retrieval Rules

### High-priority retrieval triggers

`toxicity`, `side effects`, `adverse effects`, `treatment side effects`, `chemotherapy toxicity`, `radiation toxicity`, `targeted therapy toxicity`, `immunotherapy side effects`, `immune-related adverse events`, `neuropathy`, `myelosuppression`, `diarrhea`, `nausea`, `supportive care`, `dose delay`, `dose modification`, `treatment intolerance`.

### Avoid over-retrieval

Do not retrieve PP-0231 as the primary package for general:

- palliative care;
- survivorship;
- follow-up;
- recurrence;
- response assessment.

---

# 15. Version Control

| Version | Date | Status | Change |
|---|---|---|---|
| v1.0.0 | 2026-08-09 | GOLD | Initial production from locked Decision Batch |

---

# 16. Final Status

**GOLD — READY FOR INTEGRATION**

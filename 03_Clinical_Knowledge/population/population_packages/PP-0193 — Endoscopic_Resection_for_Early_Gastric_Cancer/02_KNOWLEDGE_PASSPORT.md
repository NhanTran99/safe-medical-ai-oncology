# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0193 |
| PP ID | PP-0193 |
| Title | Endoscopic Resection for Early Gastric Cancer |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Early Gastric Cancer / Endoscopic Therapy |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / early gastric cancer treatment strategy / therapeutic endoscopy.

## Atomic Clinical Question

> **When can endoscopic resection be used to treat early gastric cancer, and how is its curative role determined?**

## Primary Function

PP-0193 is the **endoscopic-resection strategy node** in the gastric-cancer knowledge graph.

It sits between:

**early gastric cancer identification and staging**

and

**modality-specific endoscopic treatment / post-resection pathology / downstream management**.

The package teaches the clinical reasoning required to understand why some early gastric cancers can be treated endoscopically while others require surgery or additional treatment.

It does not function as a technical EMR/ESD manual or an individualized treatment algorithm.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment selection for early gastric cancer |
| Secondary journey stage | Pathologic staging / post-procedure decision |
| Decision point | Whether endoscopic resection may be appropriate and how curative status is determined |
| Typical trigger | Early gastric cancer is diagnosed or suspected and local endoscopic treatment is being discussed |
| Upstream need | Endoscopic assessment, biopsy, staging and pathology |
| Downstream need | EMR/ESD execution, post-ER pathology, surveillance or additional treatment |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “Can early gastric cancer be removed through an endoscope?”
- “When is endoscopic resection used for stomach cancer?”
- “What is EMR?”
- “What is ESD?”
- “Why would my doctor choose ESD?”
- “Why does tumor depth matter for endoscopic treatment?”
- “Why does the pathology after endoscopic resection matter?”
- “What does curative resection mean?”
- “Why would I still need surgery after an endoscopic resection?”
- “Do I need follow-up after endoscopic removal of early gastric cancer?”

## Secondary Runtime Use

Retrieve when the user needs a bridge between:

- early-stage gastric cancer;
- endoscopic treatment;
- pathology;
- and subsequent treatment/surveillance decisions.

## Do Not Use as a Substitute For

- detailed EMR technique;
- detailed ESD technique;
- individualized eligibility determination;
- individualized surgical recommendations;
- individualized interpretation of pathology;
- detailed TNM staging;
- detailed EUS methodology;
- detailed surveillance or recurrence algorithms.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- endoscopic resection
- gastric cancer endoscopic resection
- early gastric cancer
- early-stage gastric cancer
- ER
- EMR
- endoscopic mucosal resection
- ESD
- endoscopic submucosal dissection
- Tis
- T1a
- T1b
- superficial gastric cancer
- curative resection
- non-curative resection
- endoscopic treatment
- stomach-preserving treatment
- en-bloc resection
- resection margin
- lymphovascular invasion
- tumor depth
- gastric lesion size
- ulceration
- endoscopic treatment eligibility
- post-ER pathology

## Patient-Facing Retrieval Terms

- remove stomach cancer without surgery
- remove gastric cancer through endoscopy
- avoid gastrectomy
- early stomach cancer treatment
- ESD versus EMR
- pathology after ESD
- pathology after EMR
- need surgery after ESD
- need surgery after EMR
- follow-up after endoscopic resection

## Clinical Retrieval Terms

- Tis
- T1a
- intramucosal carcinoma
- superficial submucosal invasion
- lymph-node metastasis
- differentiated type
- positive margin
- negative margin
- lymphovascular invasion
- curative endoscopic resection
- expanded indication

---

# Knowledge Graph

## Prerequisites

### PP-0020 — Endoscopy

Provides the basic concept of upper gastrointestinal endoscopy and how the stomach is visualized.

### PP-0021 — Biopsy

Provides the foundational concept of obtaining tissue before definitive treatment.

### PP-0025 — Endoscopic Ultrasound (EUS)

Provides the detailed EUS context that may be relevant when assessing depth of invasion before endoscopic treatment.

### PP-0027 — Staging Work-up

Provides the broader staging framework.

### PP-0178 — Histopathologic Classification

Provides pathology terminology needed to understand the post-resection specimen.

### PP-0179 — Lauren Classification

Provides additional histologic context where relevant.

---

## Related

- Early vs Advanced Gastric Cancer.
- Stages of Gastric Cancer.
- Pathology Report.
- EMR.
- ESD.
- Gastrectomy.
- Surgical Treatment.
- Multidisciplinary Team.
- Treatment by Stage.
- Treatment Sequence.
- Follow-up After Treatment.

---

## Next / Downstream

### EMR

Owns the modality-specific knowledge of endoscopic mucosal resection.

### ESD

Owns the modality-specific knowledge of endoscopic submucosal dissection.

### Post-ER Pathology / Pathology Report

Owns detailed interpretation of the resection specimen.

### Gastrectomy / Surgical Management

Owns surgical treatment when endoscopic therapy is unsuitable or insufficient.

### Surveillance After Gastric Cancer Treatment

Owns detailed post-treatment surveillance.

### Recurrence Detection

Owns detailed recurrence evaluation.

### Treatment by Stage / Treatment Sequence

Owns broader downstream treatment planning.

---

# Clinical Scope

## Core Ownership

PP-0193 owns the **clinical strategy of endoscopic resection for selected early gastric cancer**.

It specifically owns:

1. the role of ER as treatment;
2. the role of ER as an important staging/pathologic assessment procedure;
3. selection concepts based on depth, histology, size and ulceration;
4. the importance of lymph-node risk;
5. the relationship between pre-ER assessment and final pathology;
6. EMR and ESD as the two ER modalities at strategic level;
7. NCCN's current preference for ESD in the ER framework;
8. complete/en-bloc resection as a clinically important concept;
9. the post-ER curative/non-curative decision bridge;
10. the conceptual ER-versus-gastrectomy distinction;
11. high-level procedural risk and expertise considerations;
12. the transition to surveillance or additional management.

## Supporting Ownership

The package may provide limited context on:

- EUS;
- endoscopic signs of deeper invasion;
- expanded endoscopic indications;
- gastrointestinal pathology expertise;
- high-incidence Asian experience;
- surveillance rationale.

These topics are included only to make the core ER strategy understandable.

## Explicit Exclusions

PP-0193 does not own:

- detailed EMR procedural technique;
- detailed ESD procedural technique;
- procedural device settings;
- detailed complication management;
- full pathology interpretation;
- complete staging methodology;
- detailed surgery;
- systemic therapy;
- individualized treatment.

---

# Authoritative Sources

## Primary Clinical Source

### NCCN Gastric Cancer, Version 2.2026

Primary disease-specific source for:

- ER as a treatment option for selected early-stage Tis/T1a disease;
- ER comprising EMR/ESD;
- ESD preference in the ER framework;
- pre-ER staging importance;
- curative-resection concepts;
- specimen pathology;
- post-ER surveillance.

## Primary Patient-Facing Clinical Source

### NCI — Gastric Cancer Treatment (PDQ)

Primary supporting patient-facing source for:

- selected early-stage EMR experience;
- favorable-risk features;
- relationship between intramucosal and submucosal disease and nodal risk;
- careful patient selection;
- experienced endoscopist;
- surveillance;
- evidence context.

## Supporting Clinical Source Set

- American Cancer Society — Stomach Cancer.
- Relevant gastric-cancer clinical source materials in the project Source File set.
- Project pathology and staging materials where needed for terminology and interfaces.

---

# Evidence Classification

## Established / Guideline-Supported

- ER is a primary treatment option for selected early-stage Tis/T1a gastric tumors.
- ER includes EMR and ESD.
- ESD is preferred within the current NCCN ER framework.
- Accurate staging is particularly important when ER is being considered.
- ER can provide important staging/pathologic information.
- Curative assessment depends on the integrated pathology of the resection specimen.
- Depth of invasion is a central determinant of suitability.
- Lesion size, histologic differentiation, ulceration, margins and lymphovascular invasion contribute to curative assessment.
- Experienced endoscopists and appropriate centers are important.
- Follow-up endoscopy remains necessary after ER.

## Supported but Context-Dependent

- Whether a specific Tis/T1a lesion qualifies for ER.
- Whether EMR or ESD is preferable for a particular lesion.
- Whether an expanded endoscopic-resection indication applies.
- Whether additional surgery is appropriate after non-curative ER.
- Whether EUS adds useful pre-treatment information for a particular patient.
- Whether a patient can safely avoid gastrectomy.

## Emerging / Not Owned as Standard

No emerging intervention is converted into a standard recommendation by this PP.

Where evidence or practice is context-dependent, the package retains that uncertainty rather than presenting a universal rule.

---

# Runtime Safety / Interpretation Guardrails

## Guardrail 1

**Early stage does not automatically equal ER eligibility.**

## Guardrail 2

**A small lesion is not automatically suitable for endoscopic treatment.**

## Guardrail 3

**Negative margins alone do not define curative treatment.**

## Guardrail 4

**ER is not the same as a diagnostic biopsy.**

## Guardrail 5

**A non-curative ER result does not mean the procedure was useless.**

## Guardrail 6

**ESD is preferred in the NCCN framework, but this does not mean it is universally appropriate for every lesion.**

## Guardrail 7

**Individual treatment decisions require the patient's complete clinical and pathology context.**

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example.md / approved PP-0112 Discussion |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Evidence Basis | Project Source Files |
| Source-First Status | PASS |
| Adjacent-PP Overlap Check | Completed at Discussion stage |
| Boundary | Declared in production response and reflected in artifact scope |

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0193 Decision Batch. |

---

# Change History

## 1.0.0

Initial release.

The package establishes the endoscopic-resection strategy layer and deliberately separates:

**ER strategy**

from

**EMR technique**

and

**ESD technique**

and from:

**post-ER pathology**

and:

**downstream surgery / surveillance / recurrence management**.

---

# Final Status

**GOLD — READY FOR INTEGRATION**

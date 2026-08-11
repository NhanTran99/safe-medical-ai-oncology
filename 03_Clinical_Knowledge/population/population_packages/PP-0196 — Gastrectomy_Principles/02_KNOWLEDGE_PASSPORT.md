# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0196 |
| PP ID | PP-0196 |
| Title | Gastrectomy Principles |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Gastric Cancer / Surgery |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |
| Decision Status | APPROVED / LOCKED |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / gastric-cancer surgical principles / treatment-planning literacy.

## Atomic Clinical Question

> **What is gastrectomy for gastric cancer, when is surgical resection considered, what principles determine how much of the stomach is removed, why are lymph nodes removed, what does an adequate cancer operation aim to achieve, and what should patients understand about surgical approaches, reconstruction, risks, and life after gastrectomy?**

## Primary Function

This PP is the **surgical-principles umbrella node** for gastric-cancer gastrectomy.

It explains the clinical logic behind:

- deciding whether surgery is appropriate;
- deciding the extent of gastric resection;
- achieving adequate oncologic margins;
- including regional lymphadenectomy;
- preserving uninvolved organs where possible;
- selecting an appropriate surgical approach;
- understanding postoperative consequences.

It does not own detailed procedure-specific surgical knowledge.

---

# Clinical Position in the Knowledge Graph

**Early gastric cancer / endoscopic treatment**

↓

**PP-0195 — ESD**

↓

**PP-0196 — Gastrectomy Principles**

↓

**PP-0197 — Subtotal Gastrectomy**

**PP-0198 — Total Gastrectomy**

**PP-0199 — Lymphadenectomy**

↓

**PP-0200 — D1**

**PP-0201 — D2**

This hierarchy is important because PP-0196 must provide enough context to understand gastrectomy while not absorbing the detailed downstream surgical packages.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment selection / surgical planning |
| Secondary journey stage | Postoperative pathology / recovery / survivorship |
| Decision point | Considering or reviewing gastrectomy |
| Typical trigger | Surgeon recommends gastrectomy or patient receives postoperative information |
| Downstream need | Procedure-specific understanding, pathology, systemic treatment, nutrition, surveillance |

---

# Intended Runtime Usage

Retrieve this PP when a user asks:

- “What is gastrectomy?”
- “Why do I need surgery for gastric cancer?”
- “Why do I need part of my stomach removed?”
- “Why do I need the whole stomach removed?”
- “How does the doctor decide how much stomach to remove?”
- “What is the difference between subtotal and total gastrectomy?”
- “Why are lymph nodes removed?”
- “What are D1 and D2?”
- “Why is the spleen usually not removed?”
- “What does R0 resection mean?”
- “What does a negative margin mean?”
- “Why does tumor location affect surgery?”
- “What happens if the cancer involves another organ?”
- “What is en-bloc resection?”
- “Why do I need staging before surgery?”
- “Can a CT scan miss spread?”
- “What is staging laparoscopy?”
- “Can I have laparoscopic or robotic surgery?”
- “Is minimally invasive surgery better?”
- “Why does surgeon experience matter?”
- “Will I need chemotherapy before or after surgery?”
- “What happens after the stomach is removed?”
- “Why will my eating change?”
- “What is dumping syndrome?”
- “Why do I need vitamin B12 or iron monitoring?”
- “Could I need a feeding tube?”
- “Why might I need surgery if the cancer cannot be cured?”
- “What is palliative gastrectomy?”
- “What should I ask my surgeon?”

---

# Retrieval Tags

## Primary Tags

- gastrectomy
- gastric cancer surgery
- stomach cancer surgery
- surgical principles
- curative gastrectomy
- subtotal gastrectomy
- total gastrectomy
- gastric resection
- R0 resection
- surgical margins
- lymphadenectomy
- D1
- D2
- en-bloc resection

## Secondary Tags

- resectability
- staging
- staging laparoscopy
- open gastrectomy
- laparoscopic gastrectomy
- robotic gastrectomy
- splenectomy
- reconstruction
- palliative surgery
- nutrition
- dumping syndrome
- vitamin B12
- iron deficiency
- postoperative pathology
- surgical expertise

---

# Runtime Decision Logic

## Query Type A — “What is gastrectomy?”

Retrieve:

- definition;
- partial/subtotal versus total;
- oncologic purpose;
- high-level reconstruction.

Do not retrieve detailed operative technique.

---

## Query Type B — “Why do I need surgery?”

Retrieve:

- localized/resectable disease;
- curative intent;
- complete resection;
- margins;
- lymphadenectomy;
- multimodality context.

Avoid individualized recommendations.

---

## Query Type C — “Why subtotal instead of total?”

Retrieve:

- tumor location;
- ability to obtain adequate margins;
- distal gastric cancer;
- evidence that subtotal can have comparable outcomes with fewer complications in appropriate distal disease;
- preservation principle.

Delegate detailed subtotal procedure to PP-0197.

---

## Query Type D — “Why total gastrectomy?”

Retrieve:

- diffuse disease;
- proximal/cardia location;
- inability to achieve adequate margins with partial resection;
- high-level functional/nutritional consequences.

Delegate detailed total gastrectomy to PP-0198.

---

## Query Type E — “Why remove lymph nodes?”

Retrieve:

- regional lymphatic spread;
- oncologic completeness;
- staging;
- D1/D2 conceptual distinction.

Delegate detailed anatomy to PP-0199/PP-0200/PP-0201.

---

## Query Type F — “What is D2?”

Retrieve only the conceptual definition and expertise requirement.

Do not substitute this PP for PP-0201.

---

## Query Type G — “Can I have laparoscopic/robotic surgery?”

Retrieve:

- selected-case principle;
- surgeon expertise;
- oncologic adequacy;
- T4b/bulky N2 limitation.

Do not issue a patient-specific recommendation.

---

## Query Type H — “Will the spleen be removed?”

Retrieve:

- routine splenectomy not indicated;
- exceptions for involvement/extensive hilar adenopathy;
- spleen-preservation rationale.

---

## Query Type I — “What does R0 mean?”

Retrieve:

- R0;
- R1;
- R2;
- relationship to negative margins.

Do not equate R0 with a guarantee that recurrence can never occur.

---

## Query Type J — “What happens after gastrectomy?”

Retrieve:

- reconstruction concept;
- eating changes;
- nutritional monitoring;
- dumping syndrome;
- pathology;
- downstream treatment interface.

Delegate detailed nutrition management to dedicated packages.

---

# Clinical Scope

## Core Clinical Concepts

### 1. Surgical intent

- curative;
- palliative.

### 2. Oncologic completeness

- R0;
- R1;
- R2;
- negative microscopic margins.

### 3. Surgical extent

- distal;
- subtotal;
- proximal;
- total.

### 4. Regional control/staging

- lymphadenectomy;
- D1;
- D2;
- lymph-node assessment.

### 5. Local advancement

- T4b;
- en-bloc resection;
- adjacent-organ involvement.

### 6. Surgical approach

- open;
- laparoscopic;
- robotic.

### 7. Postoperative consequences

- altered eating;
- dumping;
- micronutrient deficiencies;
- weight/nutritional changes.

---

# Clinical Claim Classification

## Established / Guideline-Supported

- Surgery is a primary treatment option for localized gastric cancer.
- Complete resection with negative microscopic margins is the standard surgical goal.
- R0, R1, and R2 describe different degrees of residual disease.
- Resectable T1b–T3 disease generally requires adequate gastric resection and lymphadenectomy in the cited NCCN framework.
- T4b tumors may require en-bloc resection of involved structures.
- Regional lymphadenectomy is part of gastric resection.
- D2 requires appropriate training and expertise.
- Routine splenectomy is not indicated.
- Selected minimally invasive approaches can have comparable oncologic outcomes in appropriately selected patients.
- Minimally invasive approaches are generally not recommended for T4b or bulky N2 disease in the cited NCCN framework.
- Gastrectomy can cause eating dysfunction and nutritional deficiencies.
- Nutritional monitoring is important after total gastrectomy.

---

# Context-Dependent Claims

The following must not be presented as universal rules:

- subtotal versus total gastrectomy;
- proximal versus distal gastrectomy;
- open versus minimally invasive surgery;
- exact lymphadenectomy extent;
- adjacent-organ resection;
- feeding-tube placement;
- palliative gastric resection;
- perioperative treatment sequence;
- reconstruction choice.

These depend on clinical context, disease extent, patient fitness, surgeon expertise, and the overall treatment plan.

---

# Emerging / Evidence-Context Notes

This PP is primarily based on established guideline and PDQ principles.

Study-level comparisons of open versus minimally invasive surgery should be communicated as evidence from selected patient populations and experienced centers rather than as a universal superiority claim.

Evidence concerning extensive surgery in metastatic/peritoneal disease should remain highly contextual and should not be generalized to routine curative gastrectomy.

---

# Patient-Facing Safety Rules

## Rule 1

Never state:

> “You need a total gastrectomy.”

unless the user is quoting a documented clinician recommendation and the answer is only explaining terminology.

Use:

> “Your surgical team may recommend…”

---

## Rule 2

Never state:

> “R0 means you are cured.”

Use:

> “R0 means no residual microscopic disease was identified at the time of resection; it does not guarantee that cancer can never recur.”

---

## Rule 3

Never state:

> “D2 is always better.”

Use:

> “D2 is a more extensive lymph-node dissection and should be performed by appropriately experienced teams when indicated.”

---

## Rule 4

Never state:

> “Laparoscopic surgery is always safer.”

Use:

> “Minimally invasive surgery may offer recovery advantages in selected patients, but the approach must still achieve appropriate cancer surgery.”

---

## Rule 5

Never state:

> “Total gastrectomy always requires splenectomy.”

Use:

> “Routine splenectomy is not recommended unless there is a specific oncologic reason.”

---

# Boundary Runtime Rules

## Upstream

### PP-0195 — ESD

Owns selected early gastric cancers treated by endoscopic submucosal dissection.

PP-0196 begins when the clinical pathway moves to surgical resection.

---

## Sibling / Downstream

### PP-0197

Owns detailed subtotal gastrectomy.

### PP-0198

Owns detailed total gastrectomy.

### PP-0199

Owns detailed lymphadenectomy.

### PP-0200

Owns D1.

### PP-0201

Owns D2.

---

# Knowledge Graph Runtime

## Prerequisites

- gastric cancer diagnosis;
- disease staging;
- treatment overview;
- endoscopic resection concepts.

## Related

- ESD;
- EMR;
- staging;
- pathology;
- lymphadenectomy;
- perioperative chemotherapy;
- FLOT;
- adjuvant therapy;
- nutrition;
- surveillance.

## Downstream

- subtotal gastrectomy;
- total gastrectomy;
- lymphadenectomy;
- D1;
- D2;
- perioperative treatment;
- postoperative treatment;
- survivorship.

---

# Update Triggers

Review this PP when:

1. NCCN changes the principles of surgery.
2. Major gastric-cancer surgical guidelines change.
3. The recommended extent of lymphadenectomy changes.
4. Resection/margin definitions change.
5. Minimally invasive surgery recommendations change.
6. Evidence changes regarding subtotal versus total gastrectomy.
7. Spleen-preservation recommendations change.
8. Post-gastrectomy nutritional recommendations change.
9. The Project Coordinator changes the adjacent PP architecture.
10. A new dedicated PP assumes ownership of a currently supporting topic.

---

# Governance

| Item | Status |
|---|---|
| Source-First | PASS |
| Locked Decision Batch | APPROVED / LOCKED |
| Gold Specification | Applied |
| Discussion Template | Applied |
| Adjacent PP overlap review | Completed |
| Boundary | Explicit |
| Knowledge Graph | Defined |
| Evidence traceability | Required |
| QA | PASS — GOLD |

---

# Repository Metadata

| Field | Value |
|---|---|
| Package ID | PP-0196 |
| Artifact set | CKO + KP + EP + QA |
| Version | 1.0.0 |
| Lifecycle | GOLD — READY FOR INTEGRATION |
| Repository family | Population_Packages |
| Package filename | PP-0196_Gastrectomy_Principles_GOLD_v1.0.0.zip |

---

# Final Runtime Statement

This Knowledge Passport defines PP-0196 as the **principles-level surgical umbrella**.

It must remain deep enough to explain why gastrectomy is performed and how its major principles fit together.

It must remain bounded enough that PP-0197, PP-0198, PP-0199, PP-0200, and PP-0201 retain their own atomic ownership.

The package must never be shortened into a simple definition of gastrectomy.

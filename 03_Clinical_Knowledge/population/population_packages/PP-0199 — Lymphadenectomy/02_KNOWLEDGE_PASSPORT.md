# PP-0199 — Lymphadenectomy

## Knowledge Passport

**KP ID:** KP-PP-0199  
**PP ID:** PP-0199  
**Version:** 1.0.0  
**Clinical Domain:** Gastric Cancer — Surgical Oncology  
**Educational Level:** Patient-facing clinical education  
**Clinical Complexity:** Intermediate  
**Patient Journey Stage:** Treatment selection → surgery → pathology → staging → treatment planning

---

# 1. Identity

PP-0199 is the parent/general knowledge package for lymphadenectomy in gastric cancer.

Its atomic question is:

> **What is lymphadenectomy in gastric cancer, why are regional lymph nodes removed, how is the extent described, why do node yield and nodal positivity matter, and why must the extent of lymph-node surgery be interpreted together with oncologic benefit, surgical risk and expertise?**

---

# 2. Classification

**Primary domain:** Surgical oncology  
**Subdomain:** Gastric resection and regional lymph-node management  
**Knowledge type:** Foundational-to-intermediate clinical concept  
**Audience:** Patients, caregivers, clinicians and downstream retrieval systems  
**Primary patient need:** Understand why lymph nodes are removed and how the result affects staging and treatment discussions.

---

# 3. Runtime Purpose

PP-0199 should be retrieved when the user asks:

- What is lymphadenectomy?
- Why are lymph nodes removed in gastric cancer?
- What is D1?
- What is D2?
- What is the difference between D1 and D2?
- How many lymph nodes should be examined?
- Why is 16 lymph nodes important?
- What does a positive lymph node mean?
- How does lymph-node involvement affect staging?
- Why is D2 more extensive?
- Does D2 mean spleen removal?
- Does D2 mean pancreas removal?
- Why does surgical experience matter?
- Why might lymphadenectomy differ between curative and palliative surgery?

PP-0199 should not be the primary retrieval target when the user asks for detailed D1 anatomy, detailed D2 anatomy, sentinel-node technique, or individualized treatment.

---

# 4. Retrieval Intent Clusters

## Cluster A — Definition

**Query examples:**

- lymphadenectomy meaning
- gastric cancer lymph node removal
- what is lymphadenectomy
- regional lymphadenectomy

**Retrieve:**

Definition + purpose + relationship to gastrectomy.

---

## Cluster B — Why Lymph Nodes Are Removed

**Query examples:**

- why remove lymph nodes in stomach cancer
- why lymphadenectomy
- why are nodes removed during gastrectomy
- gastric cancer spreads to lymph nodes

**Retrieve:**

Regional spread + oncologic role + staging role.

---

## Cluster C — D1/D2 Orientation

**Query examples:**

- D1 lymphadenectomy
- D2 lymphadenectomy
- D1 vs D2
- more extensive lymph node dissection

**Retrieve:**

Conceptual hierarchy and high-level distinction.

**Do not retrieve PP-0199 alone for:**

Detailed D1 or D2 station-level questions.

Route to PP-0200 or PP-0201.

---

## Cluster D — Node Count

**Query examples:**

- how many lymph nodes after gastrectomy
- 16 lymph nodes gastric cancer
- lymph node yield gastric cancer
- number of lymph nodes examined

**Retrieve:**

≥16 goal + distinction between yield and anatomical extent.

---

## Cluster E — Positive Nodes

**Query examples:**

- positive lymph nodes gastric cancer
- how many nodes are cancerous
- N category lymph nodes
- what does N2 mean

**Retrieve:**

Node positivity + N staging relationship.

Route detailed N-category questions to PP-0044.

---

## Cluster F — Surgical Expertise

**Query examples:**

- why D2 needs experienced surgeon
- gastric cancer high volume center
- D2 surgery expertise

**Retrieve:**

NCCN expertise/center-volume concept.

---

## Cluster G — Spleen/Pancreas

**Query examples:**

- does D2 remove spleen
- D2 pancreas removal
- spleen lymphadenectomy gastric cancer

**Retrieve:**

Misconception correction + NCCN organ-preservation principle.

---

## Cluster H — Palliative Context

**Query examples:**

- lymphadenectomy palliative surgery
- do palliative gastrectomy patients need lymph nodes removed
- gastric cancer bleeding surgery lymph nodes

**Retrieve:**

Curative versus palliative distinction.

---

# 5. Runtime Decision Tree

## Step 1 — Is the question about lymph-node surgery generally?

If yes:

→ PP-0199.

## Step 2 — Is the question about D1 in detail?

If yes:

→ PP-0200.

## Step 3 — Is the question about D2 in detail?

If yes:

→ PP-0201.

## Step 4 — Is the question about sentinel lymph nodes?

If yes:

→ PP-0202.

## Step 5 — Is the question about N category?

If yes:

→ PP-0044 plus PP-0199 as supporting context.

## Step 6 — Is the question about gastrectomy extent?

If yes:

→ PP-0196/0197/0198 depending on the requested operation.

## Step 7 — Is the question about treatment after nodal findings?

Route to the relevant treatment package.

---

# 6. Knowledge Units

## Unit 1 — Definition

Lymphadenectomy = surgical removal of relevant regional lymph nodes.

## Unit 2 — Oncologic purpose

Regional lymphadenectomy is part of curative gastric-cancer surgery.

## Unit 3 — Staging purpose

Removed nodes are examined for metastasis.

## Unit 4 — Extent

D0/D1/D1+/D2/D2+ describe different extents.

## Unit 5 — Yield

Number of nodes examined is a separate dimension.

## Unit 6 — Nodal positivity

Number of positive nodes contributes to N category.

## Unit 7 — Evidence balance

More extensive dissection is not automatically better.

## Unit 8 — Expertise

D2 requires appropriate expertise and experienced centers.

## Unit 9 — Organ preservation

D2 does not automatically require spleen or pancreas removal.

## Unit 10 — Palliative distinction

Palliative gastric resection does not necessarily require lymphadenectomy.

---

# 7. Critical Runtime Normalization Rules

### Rule 1

“Lymph node removal” → normalize to lymphadenectomy when the gastric-cancer surgical context is clear.

### Rule 2

“D2” → do not normalize to “16 lymph nodes.”

### Rule 3

“16 lymph nodes” → interpret as node-yield concept, not D2.

### Rule 4

“4 positive nodes” → interpret as nodal positivity, not total node count.

### Rule 5

“D2 surgery” → retrieve D2 conceptual content from PP-0199 only when the question is general; route detailed questions to PP-0201.

### Rule 6

“D1+” → retain as an extension concept; do not infer the detailed indication algorithm from the label alone.

### Rule 7

“D2+” → retain as selected extended lymphadenectomy concept; do not treat as routine.

### Rule 8

“Lymphadenectomy after gastrectomy” → PP-0199, with PP-0197/0198 as the operation-specific context.

---

# 8. Knowledge Graph

## Prerequisites

- PP-0042 — TNM Staging System
- PP-0044 — N Category
- PP-0196 — Gastrectomy Principles
- PP-0197 — Subtotal Gastrectomy
- PP-0198 — Total Gastrectomy

## Related

- PP-0193 — Endoscopic Resection for Early Gastric Cancer
- PP-0194 — EMR
- PP-0195 — ESD
- PP-0200 — D1 Lymphadenectomy
- PP-0201 — D2 Lymphadenectomy
- PP-0202 — Sentinel Lymph Node
- pathology-report and stage-grouping packages

## Next

- PP-0200 — D1 Lymphadenectomy
- PP-0201 — D2 Lymphadenectomy
- PP-0202 — Sentinel Lymph Node

---

# 9. Boundary Matrix

| Topic | PP-0199 | Dedicated package |
|---|---|---|
| General lymphadenectomy | CORE | — |
| Why regional nodes are removed | CORE | — |
| D0 concept | CORE | — |
| D1 concept | CORE orientation | PP-0200 |
| D1 detailed anatomy | EXCLUDED | PP-0200 |
| D1+ concept | SUPPORTING | PP-0200 / relevant downstream |
| D2 concept | CORE orientation | PP-0201 |
| D2 detailed anatomy | EXCLUDED | PP-0201 |
| D2+ concept | SUPPORTING | PP-0201 / relevant downstream |
| ≥16 nodes | CORE | — |
| Node yield vs extent | CORE | — |
| Positive nodes | CORE | PP-0044 for staging detail |
| N category | Supporting interface | PP-0044 |
| Sentinel node | Conceptual interface | PP-0202 |
| Gastrectomy technique | EXCLUDED | PP-0196–0198 |
| Chemotherapy | EXCLUDED | PP-0203 onward |
| Individual prognosis | EXCLUDED | Prognosis packages |

---

# 10. Evidence Retrieval Priority

## Priority 1 — Current NCCN source

Use for:

- regional lymphadenectomy;
- D0/D1/D2 classification;
- D2 expertise;
- ≥16-node goal;
- organ-preservation principles;
- palliative distinction;
- current treatment context.

## Priority 2 — NCI PDQ

Use for:

- regional lymphadenectomy with gastrectomy;
- stage I/II/III surgical context;
- D2 evidence uncertainty;
- morbidity context.

## Priority 3 — Vietnamese gastric-cancer guideline

Use for:

- D1/D1+/D2/D2+ descriptions;
- nodal station orientation;
- stage-linked lymphadenectomy examples;
- skip metastasis concept.

## Priority 4 — ACS

Use for:

- patient-facing explanation;
- lymph-node removal as part of gastrectomy;
- D1/D2 patient-level orientation;
- experience/center context.

---

# 11. Evidence Calibration Rules

### Established / guideline-supported

- regional lymphadenectomy is integrated into appropriate gastric-cancer surgery;
- D1 and D2 represent different anatomical extents;
- D2 is more extensive than D1;
- D2 requires appropriate expertise;
- NCCN uses a goal of examining at least 16 nodes in localized resectable disease;
- positive nodes contribute to N staging;
- routine splenectomy is not recommended;
- routine prophylactic pancreatectomy is not recommended;
- palliative gastric resection does not require lymphadenectomy.

### Context-dependent

- exact extent selected for a particular patient;
- D1 versus D1+ versus D2;
- D2 use in specific disease settings;
- D2+;
- splenectomy in selected tumor/nodal situations;
- regional variation in surgical practice;
- interpretation of historical D1/D2 trials.

### Do not overclaim

- more nodes always means better survival;
- D2 is always required;
- ≥16 nodes proves D2;
- negative nodes guarantee cure;
- D2 guarantees complete eradication of cancer;
- palliative surgery requires oncologic lymphadenectomy.

---

# 12. Patient-Facing Retrieval Templates

## Template A — “What is lymphadenectomy?”

Lymphadenectomy is surgery to remove relevant regional lymph nodes. In gastric cancer, it is commonly performed as part of an oncologic stomach operation so that regional disease can be treated and the removed nodes can be examined for cancer.

## Template B — “What is D2?”

D2 is a more extensive regional lymph-node dissection than D1. The exact nodal groups are defined anatomically and are covered in detail by the dedicated D2 package.

## Template C — “Does 16 nodes mean D2?”

No. Sixteen refers to a goal for the number of lymph nodes examined. D1 and D2 describe the anatomical extent of the dissection.

## Template D — “Why are my lymph nodes negative?”

Negative nodes mean no metastatic cancer was identified in the examined regional nodes. This is useful staging information, but it does not by itself guarantee cure.

---

# 13. Retrieval Safety Rules

1. Do not provide detailed operative D1/D2 instructions from PP-0199.
2. Do not infer stage from node count alone.
3. Do not infer D2 from ≥16 nodes.
4. Do not infer prognosis from lymphadenectomy extent alone.
5. Do not state that D2 always improves survival.
6. Do not state that D2 requires splenectomy.
7. Do not state that D2 requires pancreatectomy.
8. Do not treat palliative surgery as curative surgery.
9. Do not provide treatment-regimen recommendations.
10. Do not provide individualized surgical recommendations.

---

# 14. QA Runtime Checks

Before returning PP-0199 content, verify:

- PP ID = PP-0199.
- Title = Lymphadenectomy.
- General lymphadenectomy question is being answered.
- D1/D2 detail is delegated.
- ≥16-node concept is separated from D1/D2.
- positive-node count is separated from node yield.
- current guideline evidence is prioritized.
- palliative distinction is preserved.
- organ-preservation principle is preserved.
- no individualized treatment recommendation appears.

---

# 15. Revision History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production. |

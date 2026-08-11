# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0194 |
| PP ID | PP-0194 |
| Title | EMR (Endoscopic Mucosal Resection) |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Early Gastric Cancer / Endoscopic Therapy |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |
| Last Updated | 2026-08-09 |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / treatment-modality literacy / early gastric cancer endoscopic therapy.

## Atomic Clinical Question

> **What is endoscopic mucosal resection (EMR), when can it be used for early gastric cancer, how is the EMR specimen assessed, and what are the limitations of EMR compared with other endoscopic or surgical treatment?**

## Primary Function

PP-0194 is a **modality-specific treatment-education node**.

It sits below:

**Endoscopic Resection for Early Gastric Cancer**

and above:

**Detailed procedural EMR technique.**

It explains:

- what EMR is;
- why it can be therapeutic;
- which favorable clinical characteristics support consideration;
- what the resection specimen must show;
- how curative status is assessed;
- why EMR may be followed by surveillance or additional treatment;
- how EMR differs from ESD and surgery.

It does not provide an individualized treatment recommendation.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment selection / Early gastric cancer |
| Secondary journey stage | Pathology-guided post-treatment assessment |
| Decision point | Considering or reviewing EMR for selected early gastric cancer |
| Typical trigger | Patient is told that an early gastric lesion may be treated endoscopically |
| Upstream need | Confirmation that the lesion is potentially suitable for endoscopic treatment |
| Downstream need | Pathology-based curative assessment and follow-up/additional treatment |
| Treatment modality | Endoscopic mucosal resection |
| Main patient concern | Whether EMR can remove the cancer adequately while preserving the stomach |

---

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

- “What is EMR for stomach cancer?”
- “What is endoscopic mucosal resection?”
- “Can EMR treat early gastric cancer?”
- “Why was EMR recommended for my stomach lesion?”
- “Why do I need EMR instead of surgery?”
- “What makes a gastric cancer suitable for EMR?”
- “What does the EMR pathology report mean?”
- “What does a positive margin after EMR mean?”
- “Why does depth of invasion matter after EMR?”
- “What does lymphovascular invasion mean after EMR?”
- “Was my EMR curative?”
- “Why might I need surgery after EMR?”
- “What is the difference between EMR and ESD?”
- “Why is ESD preferred?”
- “Can EMR preserve my stomach?”
- “What should I ask my doctor before EMR?”

## Secondary Runtime Use

Retrieve when a patient needs an explanation of the transition:

**early gastric cancer**

→ **endoscopic treatment**

→ **EMR**

→ **pathology**

→ **curative/non-curative assessment**

→ **surveillance or additional treatment**.

## Do Not Use as a Substitute For

- individualized EMR eligibility assessment;
- individualized staging;
- individualized EUS interpretation;
- individualized pathology interpretation;
- individualized treatment selection;
- individualized surgical recommendation;
- detailed procedural instruction;
- emergency complication management;
- detailed post-procedure recovery advice.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- EMR
- endoscopic mucosal resection
- gastric EMR
- stomach EMR
- endoscopic resection
- early gastric cancer
- early gastric adenocarcinoma
- Tis
- T1a
- superficial gastric cancer
- mucosal gastric cancer
- endoscopic treatment
- endoscopic removal
- en-bloc resection
- complete resection
- curative resection
- non-curative resection
- positive margin
- deep margin
- lateral margin
- submucosal invasion
- lymphovascular invasion
- LVI
- GI pathology
- EMR pathology
- EMR specimen
- EMR versus ESD
- EMR versus surgery

## Selection / Clinical Context Retrieval Terms

- ≤2 cm
- differentiated
- well differentiated
- moderately differentiated
- ulceration
- nonulcerated
- T1a
- superficial submucosal invasion
- ≤500 μm
- lymph-node metastasis
- nodal risk
- EUS before treatment
- experienced endoscopist
- high-volume center

## Post-EMR Retrieval Terms

- pathology after EMR
- curative EMR
- incomplete EMR
- positive margin
- residual disease
- additional treatment
- gastrectomy after EMR
- surveillance after endoscopic resection
- follow-up endoscopy

---

# Knowledge Graph

## Prerequisites

### PP-0192 — Endoscopic Resection for Early Gastric Cancer

Provides the umbrella treatment strategy and the high-level rationale for endoscopic resection in early gastric cancer.

### PP-0176 — Endoscopic Diagnosis of Gastric Cancer

Provides the diagnostic endoscopy context and the conceptual recognition of suspicious gastric lesions.

### PP-0177 — Endoscopic Biopsy Strategy

Provides the diagnostic tissue-acquisition context and explains the difference between biopsy material and a larger resection specimen.

### PP-0178 — Histopathologic Classification

Provides the pathology concepts needed to understand histologic type, differentiation, invasion, LVI, and margins.

---

## Related

### ESD-specific package

Complementary endoscopic resection modality.

### EUS / staging packages

Provide detailed pre-treatment staging methodology.

### Gastrectomy / surgical packages

Provide the surgical treatment pathway when endoscopic treatment is unsuitable or non-curative.

### Surveillance packages

Provide detailed post-treatment monitoring.

---

## Next / Downstream

### ESD-specific package

Provides modality-specific knowledge about endoscopic submucosal dissection and its greater en-bloc resection capability.

### Gastrectomy principles / surgical packages

Provide the treatment pathway when EMR/ER is inadequate or non-curative.

### Surveillance after Gastric Cancer Treatment

Provides detailed follow-up after definitive treatment.

---

# Clinical Scope

## Core Ownership

PP-0194 owns the **patient-facing clinical knowledge of EMR itself**.

It explains:

1. what EMR is;
2. where EMR fits within endoscopic resection;
3. why EMR can preserve the stomach;
4. which early gastric cancer characteristics support consideration;
5. why depth and nodal risk matter;
6. why size, histology and ulceration matter;
7. why the EMR specimen is essential;
8. what pathology elements are required;
9. what complete/curative resection means;
10. what non-curative/incomplete EMR means;
11. why additional treatment may be required;
12. how EMR compares with ESD and surgery;
13. why experienced centers matter;
14. why surveillance remains necessary;
15. what questions a patient should ask.

## Supporting Ownership

PP-0194 may introduce, without owning detailed methodology:

- pre-treatment EUS/staging context;
- diagnostic biopsy versus EMR specimen;
- en-bloc resection concept;
- historical Asian EMR experience;
- high-level complication context;
- center-volume/expertise;
- pathology review;
- surveillance rationale;
- patient decision-support questions.

## Explicit Exclusions

PP-0194 does not own:

- detailed EMR technique;
- detailed ESD technique;
- detailed anesthesia/sedation;
- detailed complication management;
- detailed pathology methodology;
- complete TNM staging methodology;
- detailed EUS methodology;
- gastrectomy technique;
- lymphadenectomy technique;
- biomarker testing;
- systemic therapy;
- individualized treatment;
- individualized prognosis;
- individualized pathology interpretation.

---

# Evidence Classification

## Established / Guideline-Supported

- EMR is an established endoscopic treatment modality for selected early gastric cancer.
- Classic favorable-risk EMR experience includes Tis/T1a tumors, ≤2 cm, predominantly differentiated histology, and absence of ulcerative findings.
- Intramucosal disease has lower nodal-metastasis risk than submucosal disease.
- Appropriate patient selection and experienced endoscopists are important.
- EMR specimens allow assessment of invasion depth, differentiation, LVI, and margins.
- Current NCCN curative ER features include small size, superficial invasion, favorable differentiation, complete excision, negative lateral/deep margins, and no LVI.
- ESD provides greater en-bloc excision capability and is preferred within the current NCCN ER framework.
- Expanded indications described in the current NCCN discussion primarily apply to ESD and should not automatically be transferred to EMR.
- Non-curative features can lead to consideration of additional therapy.
- Follow-up surveillance remains necessary after definitive endoscopic treatment.

## Context-Dependent

- Whether a specific lesion is appropriate for EMR.
- Whether EMR or ESD is the more suitable endoscopic modality.
- Whether additional endoscopic treatment is sufficient after a non-curative result.
- Whether surgery is required.
- Whether historical Asian outcomes apply directly to a particular healthcare setting.
- Exact surveillance timing for an individual patient.

## Not Owned by This PP

- Individual treatment decisions.
- Individual pathology interpretation.
- Individual staging.
- Detailed technical procedure.
- Detailed complication management.

---

# Authoritative Project Source Set

## Primary Sources

### 1. Gastric Cancer v2.2026 — NCCN Clinical Practice Guidelines in Oncology

Primary disease-specific source.

Relevant content includes:

- Principles of Endoscopic Staging and Therapy;
- EMR/ESD in small lesions;
- endoscopic-resection treatment pathway;
- curative-resection features;
- EMR/ESD treatment criteria;
- ESD preference;
- expanded ESD indications;
- incomplete/non-curative resection features;
- pathology requirements for EMR specimens;
- post-treatment surveillance;
- center expertise.

Relevant source location:

- GAST-A 1–4;
- PDF pages 18–21;
- GAST-B pathology table, PDF page 22.

### 2. Gastric Cancer Treatment (PDQ®) — NCI

Primary supporting treatment source.

Relevant content includes:

- stage 0 EMR;
- stage I selected EMR;
- classic good-risk features;
- nodal-risk rationale;
- prospective EMR evidence;
- recurrence and disease-free survival observations;
- incomplete/non-evaluable resection outcomes.

Relevant source location:

- PDF pages 17–19.

### 3. Treatment of Stomach Cancer — NCI

Primary patient-facing source.

Relevant content includes:

- definition of EMR;
- EMR as removal of carcinoma in situ and early-stage cancer from the digestive tract lining;
- treatment decision-making with the cancer care team.

Relevant source location:

- PDF page 1.

### 4. Vietnamese Guideline — Hướng dẫn chẩn đoán và điều trị ung thư dạ dày

Regional clinical source.

Relevant content includes:

- cTis/cT1a endoscopic treatment;
- EMR and ESD;
- absolute and expanded endoscopic indications;
- low nodal-risk principle;
- en-bloc removal;
- pathology review;
- curative-resection criteria;
- additional surgery when endoscopic resection is not curative.

Relevant source location:

- PDF pages 13–14.

---

# Gold Artifact Reference Sources

## Approved Discussion Reference

**PP Discussion depth and format example.md**

Used for:

- discussion architecture;
- decision depth;
- boundary reasoning;
- scope ownership;
- recommendation style.

## Completed Gold Artifact Reference

**PP-0189 — Genomic Test Results / How to Read a Molecular Report**

Used for:

- CKO structure;
- Knowledge Passport structure;
- Evidence Package structure;
- QA structure;
- Knowledge Graph depth;
- evidence-traceability pattern;
- patient-facing explanation depth.

## Adjacent Clinical Artifact Reference

**PP-0193 — Endoscopic Resection for Early Gastric Cancer**

Used as a practical neighboring artifact reference for:

- endoscopic-resection architecture;
- treatment-pathway organization;
- ER-versus-modality boundary;
- patient-facing depth.

It is not treated as an independent clinical evidence source.

---

# Evidence Gaps

The supplied source set does not provide sufficient detail for:

1. A complete step-by-step EMR procedural manual.
2. Universal EMR device or electrosurgical settings.
3. Universal complication rates specific to EMR.
4. Detailed EMR anesthesia/sedation protocols.
5. Universal individual-patient EMR eligibility rules.
6. A universal post-EMR surveillance schedule that supersedes current clinical guidance.
7. Individualized pathology interpretation.

These gaps are intentionally not filled with unsupported general medical knowledge.

They do not block the package because PP-0194 is a patient-facing clinical-education package rather than a procedural manual or individualized decision tool.

---

# Out-of-Scope / Delegation Map

| Topic | Ownership / Delegation |
|---|---|
| Endoscopic-resection strategy | PP-0192 |
| Endoscopic diagnosis | PP-0176 |
| Endoscopic biopsy strategy | PP-0177 |
| Histopathologic classification | PP-0178 |
| Detailed EUS/staging | Dedicated EUS/staging PPs |
| EMR technique | Dedicated procedural content outside this PP |
| ESD-specific modality | Dedicated ESD PP |
| Gastrectomy principles | Dedicated surgical PP |
| Subtotal/total gastrectomy | Dedicated surgical PPs |
| Lymphadenectomy | Dedicated surgical PPs |
| Systemic treatment | Downstream treatment PPs |
| Surveillance | Dedicated surveillance PP |
| Recurrence management | Dedicated recurrence PPs |

---

# Future Update Triggers

PP-0194 should be reviewed when there are material changes in:

1. NCCN endoscopic-resection indications.
2. Current definitions of curative endoscopic resection.
3. The role of EMR versus ESD.
4. Accepted thresholds for superficial submucosal invasion.
5. Evidence regarding EMR outcomes.
6. Evidence regarding recurrence after EMR.
7. Recommendations for pathology reporting of EMR specimens.
8. Recommendations for post-ER surveillance.
9. Major changes in guideline recommendations in high-incidence Asian settings.
10. Changes in the PP Registry's ownership of EMR, ESD, or related surgical packages.

---

# Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked PP-0194 EMR Decision Batch. |

---

# Governance Metadata

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example.md |
| Artifact Reference | PP-0189 Gold 4-MD package; adjacent ER artifact reference |
| Decision Status | APPROVED / LOCKED |
| Artifact Status | GOLD |
| Boundary | Required in final production response |
| Evidence Basis | Project Source Files; no silent substitution with external evidence |
| Execution Identity | PP-0194 — EMR, per Project Coordinator's explicit locked correction |

---

# Final Status

**GOLD — READY FOR INTEGRATION**

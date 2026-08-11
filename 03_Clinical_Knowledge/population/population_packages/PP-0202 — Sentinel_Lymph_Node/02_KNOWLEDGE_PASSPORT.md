# PP-0202 — Sentinel Lymph Node
## Knowledge Passport

## 1. Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0202 |
| PP ID | PP-0202 |
| Title | Sentinel Lymph Node |
| Version | 1.0.0 |
| Package Type | Patient-facing clinical knowledge product |
| Clinical Domain | Gastric Cancer — Surgical Management / Regional Nodal Assessment |
| Status | GOLD — READY FOR INTEGRATION |

---

## 2. Knowledge Classification

### Primary Knowledge Type

**Specialized clinical concept / regional nodal assessment strategy**

### Educational Question

> What is a sentinel lymph node in gastric cancer, why might sentinel-node assessment be considered, how does it differ from D1/D2 lymphadenectomy, and what are its principal limitations?

### Atomicity

One clinical educational question.

The package does not become a general lymphadenectomy package, an endoscopic-treatment package, or a systemic-treatment package.

---

## 3. Patient Journey Classification

| Dimension | Classification |
|---|---|
| Disease phase | Primarily localized/early gastric cancer context; concept may interface with other surgical settings |
| Clinical journey | Treatment planning / surgical decision context |
| Main patient need | Understanding regional nodal assessment |
| Primary uncertainty addressed | What a sentinel node means and why accuracy matters |
| Main safety issue | False-negative interpretation |
| Downstream interface | Pathology, surgery, staging, subsequent treatment |

---

## 4. Intended Runtime Usage

This package should be retrieved when a user asks:

- “What is a sentinel lymph node?”
- “What is sentinel lymph-node biopsy in stomach cancer?”
- “Is a sentinel node the same as D1?”
- “Is a sentinel node the same as D2?”
- “Why would my doctor consider a sentinel node?”
- “Can a sentinel node replace lymph-node dissection?”
- “What does a negative sentinel node mean?”
- “What does a positive sentinel node mean?”
- “Why is false-negative risk important?”
- “Is sentinel-node surgery standard for gastric cancer?”
- “Can evidence from breast cancer be applied to stomach cancer?”
- “Why is sentinel-node assessment discussed in early gastric cancer?”

---

## 5. Retrieval / Runtime Relevance

### High-priority retrieval blocks

1. Definition.
2. D1/D2 distinction.
3. Early gastric cancer context.
4. False-negative risk.
5. Negative-result interpretation.
6. Evidence gap.
7. Patient questions.

### Secondary retrieval blocks

- pathology interface;
- institutional expertise;
- multidisciplinary interpretation;
- clinical-trial context;
- EMR/ESD interface.

### Runtime escalation

Escalate individualized questions to the treating team, particularly:

- “Should I have a sentinel-node biopsy?”
- “Can I avoid D2?”
- “If my sentinel node is negative, can I skip lymphadenectomy?”
- “Was my surgery adequate?”
- “What should my surgeon do next?”

---

## 6. Clinical Scope

### Core

- sentinel-node concept;
- selective regional nodal assessment;
- lymphatic drainage concept;
- D1/D2 distinction;
- early gastric cancer context;
- false-negative risk;
- result interpretation at conceptual level;
- evidence-dependent patient selection;
- pathology interface;
- patient-facing communication.

### Supporting

- conceptual mapping;
- institutional expertise;
- multidisciplinary context;
- early gastric cancer/endoscopic-treatment interface;
- clinical-trial context.

### Explicitly Excluded

- operative technique;
- tracer/dye protocol;
- injection protocol;
- nuclear medicine;
- fluorescence protocol;
- detailed pathology methodology;
- unsupported numerical accuracy claims;
- universal eligibility thresholds;
- individualized treatment algorithms;
- systemic treatment;
- detailed D1/D2 technique.

### Delegated

See final Boundary and Knowledge Graph.

---

## 7. Evidence Classification

### A. Established from the current project Source Materials

- Regional lymph-node involvement is clinically important in gastric cancer.
- Gastric resection for curative disease includes regional lymph-node management.
- D1 and D2 represent different extents of lymph-node removal.
- D2 extends beyond the D1 field.
- D2 requires substantial training and experience.
- Selected early gastric cancers may be candidates for endoscopic treatment.
- Early disease does not automatically eliminate the regional nodal question.
- Pathological nodal findings contribute to staging and downstream treatment.

### B. Conceptually relevant but requiring dedicated gastric sentinel-node evidence

- exact definition of a gastric sentinel-node protocol;
- mapping method;
- selection criteria;
- diagnostic accuracy;
- false-negative rate;
- sentinel-node navigation surgery;
- oncologic equivalence;
- long-term recurrence outcomes;
- long-term survival outcomes.

### C. Not supported by the current source set

- universal gastric sentinel-node indication;
- exact detection-rate percentage;
- exact sensitivity/specificity;
- exact false-negative threshold;
- universal T-stage cutoff;
- universal tumor-size cutoff;
- universal tracer/injection protocol;
- universal statement that sentinel-node surgery replaces D1/D2.

---

## 8. Source Governance

### Primary gastric source

**NCCN Gastric Cancer v2.2026**

Used for:

- regional lymphadenectomy framework;
- D1/D2 definitions;
- surgical context;
- early gastric cancer treatment context;
- expertise and organ-preservation context.

### Supporting gastric sources

- NCI Gastric Cancer Treatment PDQ;
- ACS Stomach Cancer;
- Vietnamese gastric-cancer diagnostic/treatment guideline;
- project-supplied gastric cancer prevention/treatment materials where relevant.

### Non-gastric sentinel-node material

The supplied ESMO-ASCO curriculum contains sentinel-node concepts in other malignancies.

These are **not** used as gastric-cancer evidence.

This distinction is mandatory.

---

## 9. Retrieval Safety Rules

1. Never infer gastric sentinel-node accuracy from another cancer.
2. Never convert a conceptual sentinel-node explanation into a treatment recommendation.
3. Never state that negative sentinel-node findings prove absence of all regional nodal disease.
4. Never state that sentinel-node assessment universally replaces D1/D2.
5. Never invent gastric-specific numerical thresholds.
6. Never infer eligibility from T stage, tumor size, ulceration, or histology without source support.
7. Never use D1/D2 terminology as if it were a sentinel-node classification.
8. Never provide operative instructions from this PP.
9. Always disclose the evidence gap when the user asks for technical or numerical details not supported by the current source set.
10. Escalate individualized surgical decisions.

---

## 10. Knowledge Graph

### Prerequisites

- PP-0199 — Lymphadenectomy
- PP-0200 — D1 Lymphadenectomy
- PP-0201 — D2 Lymphadenectomy

### Related

- PP-0193 — Endoscopic Resection for Early Gastric Cancer
- PP-0194 — EMR
- PP-0195 — ESD
- PP-0196 — Gastrectomy Principles
- PP-0197 — Subtotal Gastrectomy
- PP-0198 — Total Gastrectomy

### Downstream

- PP-0203 — Perioperative Chemotherapy
- pathology/staging interfaces;
- subsequent treatment packages.

---

## 11. Boundary

**Core =** Sentinel-node concept, selective regional nodal assessment, lymphatic-drainage rationale, D1/D2 distinction, early-gastric-cancer context, false-negative concept, conceptual result interpretation, evidence-dependent patient selection, pathology interface, patient-facing questions.

**Supporting =** Conceptual mapping, institutional expertise, multidisciplinary interpretation, EMR/ESD interface, clinical-trial context.

**Explicitly Excluded =** Detailed mapping technique, tracer/dye protocols, injection methods, nuclear medicine, operative instructions, detailed pathology processing, unsupported numerical performance claims, universal eligibility thresholds, individualized surgical algorithms, D1/D2 technique, D2+, gastrectomy technique, systemic therapy.

**Delegated-to PP =** PP-0199, PP-0200, PP-0201, PP-0193, PP-0194, PP-0195, PP-0196, PP-0197, PP-0198, PP-0203 onward and future dedicated sentinel-node technical/evidence packages if separately defined.

---

## 12. Governance Metadata

| Field | Value |
|---|---|
| Clinical Reviewer | Project-governed workflow |
| Evidence Status | Source-grounded with explicit sentinel-node evidence gap |
| QA Status | PASS — GOLD |
| Repository Status | Ready for integration |
| Version | 1.0.0 |
| Source-First | PASS |
| Gold Depth | PASS |
| Boundary | PASS |
| Knowledge Graph | PASS |

---

## 13. Change History

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold Passport after approved PP-0202 scope lock. |

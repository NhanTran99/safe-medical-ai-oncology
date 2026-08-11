# 02_KNOWLEDGE_PASSPORT.md
# Knowledge Passport — PP-0224 Peritoneal Carcinomatosis

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0224 |
| PP ID | PP-0224 |
| Title | Peritoneal Carcinomatosis |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Advanced / Metastatic Gastric Cancer |
| Audience | Patients, caregivers, clinicians, knowledge-retrieval systems |
| Language | English source artifact; patient-facing clinical style |

## Knowledge Classification

| Dimension | Classification |
|---|---|
| Knowledge Type | Patient-facing disease-state education / metastatic-site specialization |
| Atomic Clinical Question | What is peritoneal carcinomatosis in gastric cancer, how is it characterized, what problems can it cause, and why does it matter? |
| Clinical Complexity | High |
| Primary Journey Stage | Diagnosis / staging / metastatic disease characterization |
| Secondary Journey Stage | Treatment planning / longitudinal metastatic management |
| Primary Function | Specialized knowledge node between foundational peritoneal metastasis and downstream peritoneal-only disease / HIPEC packages |
| Evidence Sensitivity | High and guideline-update sensitive |
| Patient Safety Sensitivity | High |

## Intended Runtime Usage

Retrieve PP-0224 when a user asks:

- “What is peritoneal carcinomatosis?”
- “What does peritoneal spread mean in gastric cancer?”
- “What is peritoneal metastasis versus carcinomatosis?”
- “What is positive peritoneal cytology?”
- “Why do I need a staging laparoscopy?”
- “What is PCI?”
- “What does ascites have to do with peritoneal cancer?”
- “Can CT miss peritoneal metastases?”
- “Does peritoneal disease mean Stage IV?”
- “Why is HIPEC being discussed?”
- “Why does peritoneal disease need a multidisciplinary team?”

## Do Not Use as a Substitute For

- interpretation of an individual CT/PET/operative report;
- individualized PCI scoring;
- pathology/cytology interpretation;
- HIPEC eligibility determination;
- individualized surgery recommendation;
- systemic treatment selection;
- individualized prognosis.

## Retrieval / Runtime Relevance

### Primary Retrieval Terms

- peritoneal carcinomatosis
- peritoneal metastasis
- gastric cancer peritoneal spread
- peritoneal disease
- peritoneal implants
- peritoneal deposits
- peritoneal nodules
- peritoneal plaques
- malignant ascites
- positive peritoneal cytology
- peritoneal washings
- staging laparoscopy
- diagnostic laparoscopy
- PCI
- Peritoneal Cancer Index

### Clinical Terms

- peritoneal burden
- extraperitoneal metastasis
- cytoreduction
- systemic therapy
- multidisciplinary tumor board
- HIPEC
- PIPAC
- intraperitoneal chemotherapy
- occult peritoneal metastasis
- M1 disease

## Patient Journey

### Trigger

Peritoneal disease may be suspected or established:

- during initial staging;
- during evaluation of advanced/metastatic disease;
- at recurrence;
- during staging laparoscopy;
- through imaging;
- through positive peritoneal cytology;
- because of symptoms such as ascites or abdominal distension.

### Immediate Knowledge Need

The patient needs to understand:

1. what the finding means;
2. whether it represents spread of gastric cancer;
3. how the disease is characterized;
4. why additional tests may be needed;
5. why treatment depends on more than the presence of peritoneal disease.

### Decision Interface

The knowledge node connects:

**Peritoneal disease**
+
**PCI / burden**
+
**cytology**
+
**extraperitoneal disease**
+
**response**
+
**patient fitness**
→
**multidisciplinary treatment planning**

## Scope Map

### Core

Peritoneal carcinomatosis as a disease-state concept; peritoneal deposits; positive cytology; symptoms; ascites; diagnostic characterization; laparoscopy; washings; PCI; burden; prognosis concepts; systemic-treatment architecture; selected cytoreduction; MDT; patient-facing misconceptions.

### Supporting

Anatomy; bowel complications; nutrition; imaging limitations; pathology interface; HIPEC/PIPAC context.

### Not Included

Detailed PCI scoring; surgical technique; cytology laboratory methodology; ascites procedures; detailed systemic regimens; detailed HIPEC/PIPAC evidence and technique; dedicated peritoneal-only algorithm; individualized treatment.

## Boundary

**Core =** Peritoneal carcinomatosis as a clinically significant manifestation of gastric-cancer spread to the peritoneal surfaces; distinction from foundational peritoneal metastasis; conceptual disease biology; visible peritoneal deposits; positive peritoneal cytology; symptoms and ascites; diagnostic characterization; imaging limitations; diagnostic laparoscopy at conceptual level; peritoneal washings; biopsy when indicated; Peritoneal Cancer Index (PCI) as a measure of disease extent; clinical significance and prognosis concepts; systemic-treatment architecture; selected cytoreductive-surgery concepts; multidisciplinary assessment; clinical-trial context; patient-facing explanations and misconceptions.

**Supporting =** Peritoneal anatomy; malignant ascites context; bowel obstruction as a complication; nutritional and symptom burden; pathology interface; CT/PET-CT interface; limitations of imaging; selected cytoreductive concepts; conceptual PCI interpretation; higher- versus lower-burden framework; HIPEC as downstream context; PIPAC as investigational context; quality-of-life considerations.

**Explicitly Excluded =** Detailed peritoneal anatomy; detailed PCI scoring methodology; detailed laparoscopy/operative technique; cytology laboratory methodology; detailed biopsy methodology; ascites procedural management; bowel-obstruction procedural algorithms; detailed systemic regimens/dosing; detailed biomarker-directed therapy; detailed cytoreductive-surgery technique; HIPEC technical protocol and dedicated evidence synthesis; PIPAC technical protocol; the dedicated peritoneal-only disease treatment algorithm; detailed palliative/supportive-care protocols; individualized treatment or prognosis.

**Delegated-to PP =** PP-0048 Peritoneal Metastasis for the foundational concept; PP-0223 Metastatic Gastric Cancer for the overall metastatic-disease framework; PP-0225 Peritoneal Carcinoma as Only Disease for the dedicated peritoneal-only pathway; PP-0226 HIPEC for HIPEC/intraperitoneal-treatment detail; PP-0227 Palliative Care; PP-0228 Best Supportive Care; PP-0231 Treatment-related Toxicity and Supportive Care; PP-0232 Multidisciplinary Management; plus relevant dedicated diagnostic, pathology, imaging, organ-specific and complication-specific packages.

## Knowledge Units

### KU-01 — Definition

Peritoneal carcinomatosis is a clinically significant pattern of gastric-cancer involvement of the peritoneal surfaces.

### KU-02 — Relationship to peritoneal metastasis

Peritoneal metastasis is the broader concept; carcinomatosis describes more clinically extensive/multifocal involvement.

### KU-03 — Positive cytology

Tumor cells can be detected in peritoneal washings even without visible implants; NCCN considers positive cytology M1 disease.

### KU-04 — Diagnostic limitations

Imaging may not fully characterize small-volume or occult peritoneal disease.

### KU-05 — Laparoscopy

Diagnostic laparoscopy can directly inspect the peritoneal cavity and facilitate washings and biopsy when indicated.

### KU-06 — PCI

PCI is a structured measure of peritoneal disease extent.

### KU-07 — Symptoms

Peritoneal disease may cause abdominal distension, pain/discomfort, early satiety, nausea, vomiting, altered bowel function and ascites.

### KU-08 — Burden

Burden depends on distribution and extent, not simply on the presence or absence of peritoneal disease.

### KU-09 — Extraperitoneal disease

Peritoneal-only disease is distinct from peritoneal disease accompanied by distant metastases elsewhere.

### KU-10 — Systemic therapy

Systemic therapy remains a central management component for appropriate patients.

### KU-11 — Cytoreduction

Selected patients may be evaluated for cytoreduction when complete removal of visible disease may be feasible.

### KU-12 — HIPEC

HIPEC is a specialized downstream treatment and not an automatic consequence of peritoneal carcinomatosis.

### KU-13 — PIPAC

PIPAC is investigational in the supplied NCCN framework and belongs to specialized downstream discussion.

### KU-14 — Multidisciplinary care

Peritoneal disease decisions often require coordinated multidisciplinary review.

### KU-15 — Prognosis

Peritoneal disease is an adverse prognostic feature, but individual prognosis depends on multiple clinical factors.

## Evidence Maturity

### Established / guideline-supported

- Peritoneal disease is a clinically important metastatic pattern.
- Positive peritoneal cytology is M1 disease in the NCCN staging framework.
- Diagnostic laparoscopy and peritoneal washings have roles in selected staging/evaluation contexts.
- PCI is used to characterize peritoneal disease extent.
- Peritoneal-only disease has a dedicated NCCN pathway.
- Systemic therapy is central in the dedicated pathway.
- Selected patients may be considered for cytoreduction and IC/HIPEC.
- Multidisciplinary discussion is important.

### Context-dependent

- Need for diagnostic laparoscopy after imaging.
- PET/CT.
- Biopsy.
- Cytoreductive surgery.
- IC/HIPEC.
- Clinical-trial participation.

### Investigational / update-sensitive

- PIPAC.
- Prophylactic intraperitoneal approaches in non-metastatic disease.
- Broader use of HIPEC outside carefully selected circumstances.

## Evidence Hierarchy

1. NCCN Gastric Cancer v2.2026.
2. NCCN Gastric Cancer v2.2025.
3. NCI Treatment of Stomach Cancer.
4. NCI Gastric Cancer Treatment PDQ®.
5. ACS Stomach Cancer.
6. ESMO-ASCO oncology curriculum.
7. Project PP Registry and approved PP artifacts.
8. Governance and Gold reference materials.

## Runtime Routing

### Route upstream to PP-0048

When the question is simply:

> What is peritoneal metastasis?

### Route to PP-0223

When the question is:

> What does metastatic gastric cancer mean overall?

### Route to PP-0225

When the question is:

> What happens when the peritoneum is the only metastatic site?

### Route to PP-0226

When the question is:

> What is HIPEC, how does it work, who may be considered, and what is the evidence?

### Route to PP-0227 / PP-0228

When the question is:

> How are symptoms or advanced-disease supportive needs managed?

### Route to PP-0232

When the question is:

> How does the multidisciplinary team decide?

## Boundary Ownership Matrix

| Topic | PP-0224 | Owner / Delegate |
|---|---|---|
| Peritoneal metastasis definition | Supporting | PP-0048 |
| Peritoneal carcinomatosis | Core | PP-0224 |
| Positive cytology | Core | PP-0224; specialized only-disease context PP-0225 |
| Laparoscopy | Core conceptual | Dedicated diagnostic/surgical packages for technique |
| PCI | Core conceptual | PP-0225/0226 for decision-specific detail |
| Peritoneal-only disease | Excluded as dedicated algorithm | PP-0225 |
| Systemic treatment | Architecture | PP-0208 and therapy-specific PPs |
| Cytoreduction | Supporting | PP-0225/0226 |
| HIPEC | Context only | PP-0226 |
| PIPAC | Investigational context | PP-0226 / relevant future package |
| Palliative care | Supporting | PP-0227 |
| Best supportive care | Supporting | PP-0228 |
| Toxicity | Excluded in detail | PP-0231 |
| MDT | Supporting | PP-0232 |

## Knowledge Graph

### Prerequisites

PP-0046, PP-0047, PP-0048, PP-0008, PP-0027, PP-0223.

### Related

PP-0217, PP-0218, PP-0219, PP-0208, PP-0232.

### Downstream

PP-0225 → PP-0226 → PP-0227/0228 → PP-0231 → PP-0232.

## Governance Metadata

| Control | Result |
|---|---|
| Explicit PP request | PASS |
| PP-specific Source-First search | PASS |
| Governance review | PASS |
| Gold Discussion reference | PASS |
| Adjacent PP review | PASS |
| Approved + Locked Decision Batch | PASS |
| Gold structure | PASS |
| Gold depth | PASS |
| Evidence traceability | PASS |
| Boundary integrity | PASS |
| Knowledge Graph | PASS |
| Clinical safety | PASS |
| Final QA | PASS |

## Final Runtime Principle

> **PP-0224 is the specialized clinical disease-state map for peritoneal carcinomatosis. It explains what the disease is, how it is recognized and characterized, what clinical problems it creates, and how it interfaces with management. It does not absorb the dedicated peritoneal-only treatment pathway or HIPEC package.**

## Revision History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after Approved + Locked Decision Batch. |

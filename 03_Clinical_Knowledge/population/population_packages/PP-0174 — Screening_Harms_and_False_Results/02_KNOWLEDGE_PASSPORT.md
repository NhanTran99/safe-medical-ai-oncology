# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0174 |
| PP ID | PP-0174 |
| Title | Screening Harms and False Results |
| Version | 1.0.0 |
| Status | Approved / Gold |

## Knowledge Classification

| Field | Value |
|---|---|
| Clinical Domain | Risk & Prevention |
| Domain Code | RP-SCREENING-HARM |
| Educational Level | Intermediate |
| Clinical Complexity | Intermediate |
| Patient Journey Stage | Screening / Post-screening interpretation |
| Knowledge Granularity | Atomic screening-harm package |
| Primary Clinical Question | What can go wrong with gastric-cancer screening, and what do false-positive or false-negative results mean? |

## Patient Journey Classification

### Primary Stage

**Screening**

### Secondary Stage

**Interpretation of an abnormal or negative screening result**

### Downstream Transition

**Abnormal screening result → diagnostic work-up**

## Intended Runtime Usage

### Primary Runtime Usage

Provide a patient-facing explanation of the limitations and potential harms of gastric-cancer screening.

### Secondary Runtime Usage

- Explain false-positive results.
- Explain false-negative results.
- Clarify that screening is not diagnosis.
- Explain why additional testing may follow an abnormal result.
- Explain procedural and radiation-related harms.
- Explain overdiagnosis and overtreatment.
- Support balanced understanding of screening benefits and harms.

## Retrieval / Runtime Relevance

**Very High**

### Retrieval Intent

Use PP-0174 when the user asks:

- “Can gastric-cancer screening be harmful?”
- “What happens if my screening test is positive?”
- “Can screening miss cancer?”
- “What is a false-positive result?”
- “Is endoscopy for screening completely safe?”
- “Can screening find something that did not need treatment?”
- “Why do I need more tests after a positive screening test?”

### Retrieval Tags

- gastric cancer screening harms
- false positive
- false negative
- positive predictive value
- screening complications
- endoscopy complications
- perforation
- bleeding
- aspiration pneumonia
- cardiopulmonary events
- photofluorography
- radiation
- premedication
- overdiagnosis
- overtreatment
- screening benefit harm
- screening safety
- abnormal screening result

## Knowledge Graph

### Prerequisite

- PP-0170 — Gastric Cancer Screening in High-Risk Individuals
- PP-0171 — Endoscopic Screening for Gastric Cancer
- PP-0172 — Serum Pepsinogen Screening
- PP-0173 — Screening in High-Incidence Populations

### Related

- PP-0165 — Atrophic Gastritis and Gastric Cancer
- PP-0166 — Intestinal Metaplasia and Gastric Cancer
- PP-0167 — Pernicious Anemia and Gastric Cancer
- PP-0169 — Gastric Adenomas and Cancer Risk

### Next

- PP-0175 — Gastric Cancer Diagnostic Work-up
- PP-0176 — Endoscopic Diagnosis of Gastric Cancer
- PP-0177 — Endoscopic Biopsy Strategy
- PP-0178+ — Histopathologic Classification

## Clinical Scope

### Core

- False-positive and false-negative screening results
- Screening result versus diagnosis
- Patient-facing PPV concept
- Downstream consequences of abnormal screening
- False reassurance
- Rare but serious endoscopic complications
- Photofluorography radiation exposure
- Premedication adverse effects
- Overdiagnosis and overtreatment
- Screening-center experience
- Population-dependent benefit–harm balance
- Evidence limitations

### Supporting

- Anxiety and uncertainty
- Time/resource burden
- Interval/missed cancer concept
- Conceptual sensitivity/specificity
- Population context inherited from PP-0173
- Patient decision-making context

### Explicitly Excluded

- Detailed endoscopy technique
- Detailed serum-pepsinogen biology/cutoffs
- Detailed diagnostic work-up
- Diagnostic endoscopy technique
- Biopsy technique
- Pathology
- Universal sensitivity/specificity
- Universal PPV/NPV
- Universal complication rates
- Universal screening age/interval
- Individualized screening recommendations
- Individualized result interpretation
- Detailed treatment harms
- Detailed cost-effectiveness

### Delegated-to PP

| Topic | Owner |
|---|---|
| High-risk screening eligibility | PP-0170 |
| Endoscopic screening | PP-0171 |
| Serum pepsinogen screening | PP-0172 |
| High-incidence population strategy | PP-0173 |
| Atrophic gastritis | PP-0165 |
| Intestinal metaplasia | PP-0166 |
| Pernicious anemia | PP-0167 |
| Gastric adenomas | PP-0169 |
| Diagnostic work-up | PP-0175 |
| Diagnostic endoscopy | PP-0176 |
| Biopsy strategy | PP-0177 |
| Histopathology | PP-0178+ |
| Detailed treatment harms | Downstream treatment packages |
| Detailed economics | Future dedicated package if explicitly defined |

## Authoritative Sources

### Primary

1. NCI — Stomach (Gastric) Cancer Screening PDQ, Health Professional Version.

### Supporting

2. NCI — Screening for Stomach Cancer, patient-facing source.
3. NCI — Stomach (Gastric) Cancer Prevention PDQ.
4. NCCN Gastric Cancer Version 2.2026, where relevant for current clinical framework.
5. Approved adjacent Population Packages.
6. PP Registry and locked governance documents.

## Evidence Classification

### Established / directly source-supported

- False-positive testing is the most frequent reported harm in the NCI screening review.
- Endoscopic screening can have rare but serious complications.
- Photofluorography involves low-dose radiation exposure.
- Premedication can cause adverse effects.
- Overdiagnosis can lead to overtreatment.
- Screening-center experience can affect some complication risks.
- PPV can be low even in high-risk populations.

### Supported but context-dependent

- The downstream burden of abnormal screening results.
- The importance of false reassurance after a negative result.
- Population-dependent benefit–harm balance.
- Generalizability limitations between high- and low-incidence settings.

### Not established universally

- One false-positive rate for all screening modalities.
- One false-negative rate for all screening modalities.
- One universal PPV or NPV.
- One universal complication rate.
- One universal overdiagnosis rate.
- One universal benefit–harm threshold.

## Governance Metadata

| Field | Value |
|---|---|
| Clinical Governance | Enabled |
| Source-First Verification | Completed |
| Decision Batch | Approved / Locked |
| Adjacent Boundary Review | Completed |
| Evidence Traceability | Complete |
| Knowledge Graph | Complete |
| Gold Specification Compliance | Yes |
| Runtime Ready | Yes |
| Repository Ready | Yes |
| QA Status | PASS — GOLD |

## Version Control

| Item | Value |
|---|---|
| Current Version | 1.0.0 |
| Major | 1 |
| Minor | 0 |
| Patch | 0 |

## Change History

| Version | Date | Description |
|---|---|---|
| 1.0.0 | 2026-08-09 | Gold production after approved PP-0174 Decision Batch |

## Final Status

**APPROVED — GOLD — READY FOR INTEGRATION**

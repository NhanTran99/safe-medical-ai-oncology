# 02_KNOWLEDGE_PASSPORT — PP-0201 D2 Lymphadenectomy

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0201 |
| PP ID | PP-0201 |
| Title | D2 Lymphadenectomy |
| Version | 1.0.0 |
| Status | GOLD |
| Decision | APPROVED / LOCKED |

## Classification

| Field | Value |
|---|---|
| Clinical Domain | Gastric Cancer — Surgical Treatment |
| Domain Code | GC-SURG-LND-D2 |
| Educational Level | Patient-facing clinical education |
| Clinical Complexity | Intermediate–advanced |
| Patient Journey Stage | Treatment / Surgical Planning / Pathology Interpretation |
| Package Type | Atomic Population Package |
| Primary Question | What is D2 lymphadenectomy, when is it considered, and what should patients understand about its benefits, risks, and limitations? |

## Intended Runtime Usage

This package supports patient-facing questions about D2 lymphadenectomy.

Use it to explain:

- D2 definition;
- D1-to-D2 extension;
- source-specific nodal terminology;
- clinical context;
- evidence comparing D2 and D1;
- surgical expertise;
- organ preservation;
- node examination and staging;
- minimally invasive context;
- patient questions.

Do not use it to generate individualized surgical recommendations.

## Retrieval Tags

D2 lymphadenectomy; D2; gastric cancer surgery; stomach cancer surgery; extended lymphadenectomy; regional lymph nodes; D1 versus D2; left gastric artery; common hepatic artery; celiac artery; splenic artery; lymph-node dissection; gastric lymph nodes; 16 lymph nodes; lymph-node yield; gastric cancer staging; spleen preservation; pancreas preservation; laparoscopic D2; robotic D2.

## Related Population Packages

- PP-0199 — Lymphadenectomy
- PP-0200 — D1 Lymphadenectomy
- PP-0202 — Sentinel Lymph Node
- PP-0196 — Gastrectomy Principles
- PP-0197 — Subtotal Gastrectomy
- PP-0198 — Total Gastrectomy
- PP-0193 — Endoscopic Resection for Early Gastric Cancer
- PP-0194 — EMR
- PP-0195 — ESD

## Boundary

**Core =** D2-specific anatomical extent; D1-versus-D2 distinction; NCCN vessel-based D2 definition; source-attributed Vietnamese station framework; clinical role/context of D2; D1-versus-D2 evidence; East/West practice context; surgical expertise and high-volume-center importance; modern organ-preservation principles; lymph-node examination/staging interface; patient-facing interpretation and misconceptions.

**Supporting =** minimally invasive D2; historical D2 morbidity; local/regional recurrence context; postoperative-treatment interface; group 10/11 and splenic-preservation context; D2+ as a high-level boundary.

**Explicitly Excluded =** general lymphadenectomy; detailed D1 content; step-by-step D2 operative technique; vessel dissection/skeletonization; instruments/ports/robotic workflow; detailed splenectomy/pancreatectomy technique; D2+ operative strategy; sentinel-node methodology; detailed gastrectomy technique; detailed TNM algorithms; systemic-treatment selection; individualized surgical/treatment recommendations; individualized prognosis.

**Delegated-to PP =** PP-0199 Lymphadenectomy; PP-0200 D1 Lymphadenectomy; PP-0196 Gastrectomy Principles; PP-0197 Subtotal Gastrectomy; PP-0198 Total Gastrectomy; PP-0193–PP-0195 Endoscopic Resection/EMR/ESD; PP-0202 Sentinel Lymph Node; PP-0203 onward downstream perioperative/adjuvant/neoadjuvant/chemoradiation/systemic-treatment packages; any future dedicated D2+ package.


## Clinical Question

> What is D2 lymphadenectomy in gastric cancer, what additional lymph-node territory does it include beyond D1, when is it considered, why does surgical expertise matter, and what should patients understand about its benefits, risks, and limitations?

## Knowledge Model

### Definition

D2 is a broader anatomical extent of regional lymph-node dissection beyond D1.

### Anatomical model

NCCN defines D2 as D1 plus lymph nodes along the left gastric, common hepatic, celiac, and splenic arteries.

### Station model

The supplied Vietnamese guideline describes D2 using its station-based framework.

### Clinical model

D2 is primarily associated with curative/resectable gastric-cancer surgery in selected disease contexts.

### Evidence model

D2 has potential advantages in regional disease control and staging, but historical and modern comparative evidence does not justify a universal superiority claim.

### Quality model

D2 requires substantial expertise and is best performed in experienced centers.

### Safety model

Routine splenectomy and prophylactic pancreatectomy are not part of modern D2.

### Staging model

D2 extent and node counts are distinct variables.

## Evidence Classification

### Established / Guideline-Supported

- D2 is an anatomical extension of D1.
- NCCN defines D2 by additional nodal territories along four major arteries.
- The supplied Vietnamese guideline provides a station-based D2 framework.
- D2 requires significant training and expertise.
- NCCN identifies D2 as standard for curable gastric cancer in East Asian practice.
- D2 is recommended but not universally required in Western practice.
- Routine prophylactic pancreatectomy is not recommended.
- Routine splenectomy is not indicated without disease-specific involvement.
- ≥16 lymph nodes is a separate examination goal in the surgical framework.
- Palliative gastric resection does not necessarily require lymph-node dissection.

### Supported but Context-Dependent

- D2 may reduce local/regional recurrence compared with D1.
- D2 may improve gastric-cancer-specific outcomes in some settings.
- D2 safety depends strongly on surgical expertise and organ-preserving technique.
- Minimally invasive D2 can be appropriate in selected experienced settings.
- D2 status can influence postoperative treatment planning.

### Not Established / Must Not Be Overclaimed

- D2 always improves overall survival.
- D2 is always better than D1.
- D2 is always more dangerous than D1.
- D2 means at least 16 nodes.
- D2 automatically requires spleen or pancreas removal.
- D2 is appropriate for every gastric-cancer patient.
- Node count alone identifies D2.

## Primary Guideline Sources

1. NCCN Guidelines Version 2.2026 — Gastric Cancer.
2. Vietnamese gastric-cancer diagnosis and treatment guideline supplied in the project Source Files.

## Supporting Sources

1. NCI — Gastric Cancer Treatment PDQ.
2. American Cancer Society — Stomach Cancer.

## Evidence Hierarchy

| Rank | Source | Role |
|---|---|---|
| 1 | NCCN Gastric Cancer v2.2026 | Primary D2 definition, evidence, surgical-quality anchor |
| 2 | Vietnamese gastric-cancer guideline | Station-based classification and clinical context |
| 3 | NCI Gastric Cancer Treatment PDQ | Independent government clinical context |
| 4 | ACS Stomach Cancer | Patient-facing supporting context |

## Governance

| Field | Value |
|---|---|
| Governance Standard | CORE_WORKING_RULES v1.7 |
| Gold Specification | FREEZE GOLD POPULATION PACKAGE SPECIFICATION v1.1 |
| Discussion Reference | PP Discussion depth and format example |
| Decision Status | APPROVED / LOCKED |
| QA Status | PASS — GOLD — READY FOR INTEGRATION |
| Repository Status | Ready for integration |
| Evidence Basis | Project Source Files |

## Runtime Safety Rules

1. Do not recommend D2 for an individual patient.
2. Do not infer D2 from lymph-node count.
3. Do not equate D2 with routine splenectomy or pancreatectomy.
4. Do not describe D2 as universally superior to D1.
5. Do not describe historical D2 morbidity as automatically representing modern D2.
6. Preserve the East Asian versus Western practice distinction.
7. Preserve source-specific terminology for station classification.
8. Route detailed postoperative treatment questions to downstream treatment packages.
9. Route operative technique questions outside this patient-facing package.
10. Refer individual surgical decisions to the treating multidisciplinary team.

## Version Control

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Gold production after approved/locked Decision Batch. |

## Final Status

**GOLD — READY FOR INTEGRATION**


## Extended Knowledge Passport

### Patient Journey Placement

**Before PP-0201**

The patient should understand:

- gastrectomy principles;
- general lymphadenectomy;
- D1 lymphadenectomy.

**PP-0201**

The patient learns:

- D2 anatomy;
- D1 versus D2;
- clinical role;
- evidence;
- expertise;
- organ preservation;
- staging interface.

**After PP-0201**

The patient may need:

- sentinel lymph-node information;
- pathology interpretation;
- perioperative/adjuvant treatment;
- follow-up.

### Knowledge Granularity

| Level | Content |
|---|---|
| Level 1 | D2 definition |
| Level 2 | D1-to-D2 anatomy |
| Level 3 | Clinical context |
| Level 4 | D1/D2 evidence |
| Level 5 | Surgical quality and organ preservation |
| Level 6 | Patient interpretation and downstream interface |

### Concept Relationships

| Concept | Relationship |
|---|---|
| D1 | D2 includes D1 |
| D2+ | Broader extension beyond D2 |
| Gastrectomy | D2 is performed with appropriate gastric resection |
| Pathology | Examines removed lymph nodes |
| N stage | Uses regional nodal findings |
| Postoperative treatment | May be influenced by lymphadenectomy extent |
| Sentinel lymph node | Separate strategy |
| Minimally invasive surgery | Access approach, not lymphadenectomy extent |

### Retrieval Rules

1. For “What is D2?” retrieve the anatomical definition.
2. For “D1 versus D2,” retrieve the anatomical distinction plus evidence context.
3. For “Is D2 better?” retrieve the comparative evidence and uncertainty.
4. For “Does D2 remove the spleen?” retrieve the organ-preservation rule.
5. For “Does D2 mean 16 nodes?” retrieve the node-count distinction.
6. For “Why D2 for my cancer?” do not generate an individualized recommendation.
7. For postoperative-treatment questions, route downstream.
8. For operative-technique questions, route outside this PP.

### Evidence Priority

1. Locked PP-0201 Decision Batch.
2. NCCN Gastric Cancer v2.2026.
3. Vietnamese gastric-cancer guideline.
4. NCI PDQ.
5. ACS.

### Source-Specific Terminology Rule

The NCCN anatomical definition is the primary D2 definition.

The Vietnamese station framework is preserved with attribution.

The runtime must not silently merge source-specific station terminology into an unsupported universal map.

### Safety Rules

- No individualized D1/D2 recommendation.
- No operative instructions.
- No numerical learning-curve claims.
- No inference from node count alone.
- No universal D2 superiority claim.
- No routine splenectomy/pancreatectomy implication.
- No postoperative treatment prescription.
- No individualized prognosis.

### Evidence Limitations

The source set supports the approved D2 scope strongly.

It does not support:

- a complete operative atlas;
- a universal D2+ algorithm;
- individualized surgical selection;
- a universal cross-guideline station map.

### Update Logic

Review if:

- NCCN changes D2 definition;
- Vietnamese guideline changes station classification;
- randomized D1/D2 evidence materially changes;
- D2 surgical-quality standards change;
- a dedicated D2+ package is created;
- the Project Coordinator changes adjacent package ownership.

### Runtime Escalation

Escalate to the treating team when the user asks:

- whether they personally should have D2;
- whether a specific node count proves D2;
- whether they personally need splenectomy;
- whether they personally need postoperative chemotherapy;
- whether a pathology result changes their treatment.

### Integration Notes

This package should retrieve cleanly for:

- “D2 lymphadenectomy”
- “D2 dissection”
- “D1 vs D2”
- “extended lymph-node dissection”
- “16 lymph nodes”
- “spleen removal”
- “pancreas removal”
- “D2 surgery”
- “laparoscopic D2”
- “why D2”
- “D2 pathology”

### Gold Compliance

- Atomic: PASS
- Patient-centered: PASS
- Evidence-based: PASS
- Traceable: PASS
- Reusable: PASS
- Maintainable: PASS
- Scalable: PASS
- Boundary declared: PASS
- Knowledge graph: PASS
- Runtime safety: PASS
- Versioned: PASS

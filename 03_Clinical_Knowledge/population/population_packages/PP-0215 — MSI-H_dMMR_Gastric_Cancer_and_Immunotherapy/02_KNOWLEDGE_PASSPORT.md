# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| Knowledge Passport ID | KP-PP-0215 |
| Population Package ID | PP-0215 |
| Title | MSI-H/dMMR Gastric Cancer and Immunotherapy |
| Version | 1.0.0 |
| Status | Approved — GOLD |
| Last Updated | 2026-08-09 |

---

# Classification

| Field | Classification |
|---|---|
| Clinical Domain | Gastric Cancer / Precision Oncology / Immunotherapy |
| Domain Code | GC-IMMUNO-BIOMARKER |
| Educational Level | Intermediate clinical education / patient-facing |
| Clinical Complexity | High |
| Patient Journey Stage | Diagnosis → Biomarker Interpretation → Treatment Selection → Treatment |
| Knowledge Type | Biomarker-defined treatment application |
| Population | Gastric/EGJ adenocarcinoma with MSI-H/dMMR phenotype |
| Primary Clinical Question | What does MSI-H/dMMR mean in gastric cancer, and why does it matter for immunotherapy? |

---

# Intended Runtime Usage

This package is intended to serve as a specialized knowledge node after MSI/MMR testing and alongside the broader gastric-cancer immunotherapy and immune-checkpoint-inhibitor packages.

It should be retrieved when a user asks questions such as:

- “What does MSI-H mean for my stomach cancer?”
- “What does dMMR mean?”
- “Why does MSI-H make immunotherapy more useful?”
- “Do I need PD-L1 if my tumor is MSI-H?”
- “Can MSI-H gastric cancer be treated with immunotherapy?”
- “What evidence supports immunotherapy for MSI-H gastric cancer?”
- “Can MSI-H/dMMR tumors receive immunotherapy before surgery?”
- “Does MSI-H mean Lynch syndrome?”

It should not be used as the primary source for:

- how MSI/MMR testing is technically performed;
- detailed PD-L1 scoring;
- detailed TMB testing;
- detailed germline testing;
- immune-related toxicity management;
- RECIST or formal response assessment;
- individualized treatment prescribing.

---

# Retrieval Tags

- gastric cancer
- gastric adenocarcinoma
- gastroesophageal junction adenocarcinoma
- MSI-H
- microsatellite instability-high
- dMMR
- mismatch repair deficiency
- MMR
- MSS
- pMMR
- MSI-H immunotherapy
- dMMR immunotherapy
- pembrolizumab
- nivolumab
- nivolumab plus ipilimumab
- checkpoint inhibitor
- immune checkpoint inhibitor
- NEONIPIGA
- KEYNOTE-059
- KEYNOTE-061
- KEYNOTE-062
- KEYNOTE-158
- CheckMate-649
- perioperative immunotherapy
- neoadjuvant immunotherapy
- PD-L1-independent
- biomarker-defined immunotherapy
- Lynch syndrome bridge
- predictive biomarker

---

# Related Population Packages

| Relationship | PP | Role |
|---|---|---|
| Prerequisite | PP-0182 | MSI/MMR Testing |
| Broader upstream | PP-0014 | Immunotherapy for Gastric Adenocarcinoma |
| Broader treatment | PP-0213 | Immunotherapy in Gastric Cancer |
| General mechanism | PP-0214 | Immune Checkpoint Inhibitors |
| Parallel biomarker pathway | PP-0216 | PD-L1-guided Immunotherapy |
| Related biomarker | TMB-specific PP | TMB testing/interpretation |
| Genetics bridge | Hereditary/genetic-testing PPs | Lynch syndrome and germline assessment |
| Response | PP-0217 | Response Assessment |
| Response methodology | PP-0218 | RECIST-based Assessment |
| Imaging | PP-0219 | Post-treatment Imaging |
| Safety | PP-0231 | Treatment-related Toxicity and Supportive Care |

---

# Governance

## Primary Guideline Sources

1. **NCCN Clinical Practice Guidelines in Oncology — Gastric Cancer, Version 2.2026**
   - Primary disease-specific treatment and biomarker source.
   - Provides MSI-H/dMMR treatment positioning, trial evidence, and perioperative context.

2. **NCI Gastric Cancer Treatment PDQ**
   - Supporting clinical-treatment context and patient-facing framing.

3. **NCI Cancer Genetics Risk Assessment and Counseling PDQ**
   - Supporting hereditary/genetic-counselling bridge.

4. **ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology, 2023**
   - Supporting cross-cutting oncology and biomarker concepts.

5. **American Cancer Society — Immunotherapy for Stomach Cancer**
   - Supporting patient-facing immunotherapy explanation.

6. **American Cancer Society — Stomach Cancer**
   - Supporting patient-facing biomarker/treatment context.

---

# Evidence Classification

## Established / guideline-supported

- MSI-H/dMMR is a clinically meaningful gastric-cancer phenotype.
- MSI-H/dMMR has important immunotherapy relevance.
- MSI-H/dMMR can be associated with favorable prognostic characteristics.
- Selected checkpoint-inhibitor strategies are recommended independently of PD-L1 status.
- Pembrolizumab has substantial MSI-H/dMMR evidence.
- Nivolumab plus chemotherapy has substantial MSI-H subgroup evidence.
- Nivolumab plus ipilimumab has a particularly strong MSI-H subgroup signal.
- Selected MSI-H/dMMR tumors may be considered for neoadjuvant/perioperative immunotherapy.

## Context-dependent

- Exact checkpoint inhibitor.
- Monotherapy versus combination.
- First-line versus subsequent-line treatment.
- Neoadjuvant versus perioperative use.
- Role of surgery after complete response.
- Dostarlimab use.
- Other evolving perioperative strategies.

## Emerging / evidence-limited

- Optimal perioperative immunotherapy regimen.
- Optimal treatment duration.
- Optimal strategy after complete response.
- Universal sequencing after checkpoint-inhibitor failure.
- Detailed mechanisms of acquired resistance.

---

# Runtime Safety Rules

## Rule 1 — Do not equate MSI-H with PD-L1 positivity

These are distinct biomarkers.

## Rule 2 — Do not equate MSI-H with TMB-H

They are biologically related but clinically distinct.

## Rule 3 — Do not equate tumor dMMR with Lynch syndrome

A tumor finding can trigger hereditary assessment but does not itself establish inherited disease.

## Rule 4 — Do not convert population-level efficacy into an individual guarantee

A high response rate does not mean that every MSI-H/dMMR tumor will respond.

## Rule 5 — Do not turn this package into an individualized treatment recommendation

Treatment depends on stage, resectability, prior treatment, other biomarkers, health status, preferences, and guideline-defined context.

## Rule 6 — Preserve evidence hierarchy

Gastric/EGJ-specific randomized evidence should not be silently merged with tumor-agnostic or non-gastric MSI-H/dMMR evidence.

---

# Boundary

## Core

MSI-H/dMMR gastric-cancer phenotype; conceptual biology; MSI-H versus MSS/pMMR; clinical/prognostic context; immunotherapy rationale; biomarker-treatment relationship; PD-L1 independence in selected contexts; advanced/metastatic checkpoint-inhibitor evidence; selected perioperative/neoadjuvant immunotherapy; landmark trials; response depth/durability; limitations; patient-facing interpretation.

## Supporting

TMB relationship; PD-L1 relationship; EBV context; hereditary/genetic-counselling bridge; treatment-line context; evidence-quality distinctions; conceptual resistance; selected cross-tumor MSI-H evidence.

## Explicitly Excluded

Detailed MSI/MMR testing methodology; PCR/IHC/NGS assay workflows; detailed mismatch-repair biochemistry; PD-L1 testing/scoring; TMB testing; detailed Lynch syndrome/germline testing; general ICI pharmacology; dosing; detailed toxicity management; formal response criteria; detailed imaging; surgical technique; universal sequencing; individualized treatment; individualized prognosis; detailed molecular resistance mechanisms.

## Delegated-to PP

PP-0182 MSI/MMR Testing; PP-0183 PD-L1 Testing; TMB-specific testing/interpretation packages; PP-0213 Immunotherapy in Gastric Cancer; PP-0214 Immune Checkpoint Inhibitors; PP-0216 PD-L1-guided Immunotherapy; PP-0217 Response Assessment; PP-0218 RECIST-based Assessment; PP-0219 Post-treatment Imaging; PP-0231 Treatment-related Toxicity and Supportive Care; hereditary/genetic-testing packages; downstream treatment-sequencing and resistance packages.

---

# Evidence Provenance

All clinical content is grounded primarily in the supplied gastric-cancer Source Materials.

The dominant disease-specific source is:

**NCCN Gastric Cancer Version 2.2026.**

Key source-supported areas include:

- MSI-H/dMMR clinical context.
- KEYNOTE-059.
- KEYNOTE-061.
- KEYNOTE-062.
- KEYNOTE-158.
- CheckMate-649.
- NEONIPIGA.
- selected perioperative evidence.
- current NCCN treatment positioning.

No external source is silently substituted for the project Source Materials.

---

# Knowledge Graph Position

```text
PP-0182 MSI/MMR Testing
        ↓
PP-0215 MSI-H/dMMR Gastric Cancer and Immunotherapy
        ↓
MSI-H/dMMR-specific treatment applications

Parallel:
PP-0213 Immunotherapy in Gastric Cancer
        ↓
PP-0214 Immune Checkpoint Inhibitors
        ↓
PP-0215 MSI-H/dMMR-specific application

Parallel biomarker pathway:
PP-0183 PD-L1 Testing
        ↓
PP-0216 PD-L1-guided Immunotherapy
```

---

# Governance Status

| Item | Status |
|---|---|
| Decision Batch | Approved + Locked |
| Gold Structure | Locked |
| Gold Depth | Mandatory / Absolute |
| Evidence Basis | Source-first |
| Boundary | Locked for production |
| Adjacent overlap | Reviewed |
| Clinical content | Source-grounded |
| Artifact status | Approved — GOLD |
| QA status | PASS — GOLD — READY FOR INTEGRATION |

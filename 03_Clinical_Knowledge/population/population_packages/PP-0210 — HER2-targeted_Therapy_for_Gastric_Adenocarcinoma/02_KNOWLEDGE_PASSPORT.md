# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

  -----------------------------------------------------------------------
  Field                               Value
  ----------------------------------- -----------------------------------
  KP ID                               KP-PP-0210

  PP ID                               PP-0210

  Title                               HER2-targeted Therapy for Gastric
                                      Adenocarcinoma

  Version                             1.0.0

  Status                              GOLD --- READY FOR INTEGRATION

  Clinical Domain                     Treatment / Precision Oncology /
                                      Targeted Therapy

  Audience                            Patients, caregivers, general
                                      oncology learners

  Language                            English source artifact;
                                      patient-facing plain-language style
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / HER2-directed treatment literacy.

## Atomic Clinical Question

> **What is HER2-targeted therapy for gastric adenocarcinoma, how does
> HER2 status connect to treatment, what are the major HER2-directed
> treatment approaches, and what should patients understand about
> benefit, limitations, safety, and treatment context?**

## Primary Function

This PP is the **HER2-specific treatment-modality node** between HER2
testing / biomarker-directed treatment selection and downstream
drug-specific packages.

It teaches:

-   why HER2 is treatment-relevant;
-   how a HER2 result connects to treatment;
-   what HER2-targeted therapy means;
-   the roles of trastuzumab and T-DXd;
-   the relationship with chemotherapy and selected immunotherapy;
-   treatment-line context;
-   benefits and limitations;
-   patient-facing safety concepts.

It does not own the detailed management of any single HER2-directed
drug.

------------------------------------------------------------------------

# Patient Journey Classification

  -----------------------------------------------------------------------
  Dimension                           Classification
  ----------------------------------- -----------------------------------
  Primary journey stage               Treatment planning

  Secondary journey stage             Systemic treatment / precision
                                      oncology

  Decision point                      HER2-directed treatment becomes a
                                      potential option after relevant
                                      biomarker characterization

  Typical trigger                     Patient receives a clinically
                                      relevant HER2 result or is offered
                                      HER2-directed treatment

  Upstream dependency                 HER2 testing and biomarker-directed
                                      treatment selection

  Downstream need                     Drug-specific treatment, toxicity,
                                      monitoring, resistance and trial
                                      packages
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Intended Runtime Usage

## Primary Runtime Use

Retrieve when a user asks:

-   "What is HER2-targeted therapy?"
-   "Why does HER2 matter for treatment?"
-   "What does HER2-positive mean for treatment?"
-   "What is trastuzumab in gastric cancer?"
-   "What is T-DXd?"
-   "Why is trastuzumab combined with chemotherapy?"
-   "Can HER2 treatment be combined with immunotherapy?"
-   "What happens after trastuzumab stops working?"
-   "What are the benefits and risks of HER2-targeted treatment?"
-   "Why might I receive T-DXd after trastuzumab?"

## Secondary Runtime Use

Retrieve when a patient understands their HER2 result but needs a
modality-level explanation before entering a drug-specific package.

## Do Not Use as a Substitute For

-   HER2 IHC/ISH/FISH interpretation;
-   detailed biomarker testing;
-   individualized treatment selection;
-   trastuzumab dosing or administration;
-   T-DXd dosing or administration;
-   detailed cardiac monitoring;
-   detailed ILD/pneumonitis management;
-   detailed HER2 resistance mechanisms;
-   individualized prognosis.

------------------------------------------------------------------------

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

-   HER2-targeted therapy
-   HER2 targeted treatment
-   HER2-positive gastric cancer
-   HER2-positive gastric adenocarcinoma
-   HER2-positive GEJ adenocarcinoma
-   HER2 treatment
-   HER2-directed therapy
-   anti-HER2 therapy
-   precision treatment
-   targeted treatment

## Trastuzumab Retrieval Terms

-   trastuzumab
-   Herceptin
-   trastuzumab plus chemotherapy
-   ToGA
-   HER2 antibody
-   HER2 monoclonal antibody

## T-DXd Retrieval Terms

-   trastuzumab deruxtecan
-   T-DXd
-   fam-trastuzumab deruxtecan-nxki
-   antibody-drug conjugate
-   ADC
-   DESTINY-Gastric01
-   DESTINY-Gastric02

## Combination Retrieval Terms

-   HER2 chemotherapy
-   trastuzumab chemotherapy
-   HER2 immunotherapy
-   pembrolizumab trastuzumab chemotherapy
-   KEYNOTE-811

## Safety Retrieval Terms

-   trastuzumab cardiac
-   HER2 cardiac monitoring
-   T-DXd ILD
-   T-DXd pneumonitis
-   HER2 targeted toxicity

## Resistance Retrieval Terms

-   HER2 resistance
-   trastuzumab resistance
-   T-DXd resistance
-   HER2 progression
-   HER2 treatment after progression

------------------------------------------------------------------------

# Runtime Classification Rules

## Rule 1 --- Broad HER2-targeted question

If the user asks:

> "What is HER2-targeted therapy?"

Retrieve PP-0210.

## Rule 2 --- Testing question

If the user asks:

> "How is HER2 tested?"

Route to HER2 Testing.

## Rule 3 --- Drug-specific question

If the user asks:

> "How does trastuzumab work?"

Route to Trastuzumab.

If the user asks:

> "How does T-DXd work?"

Route to T-DXd / ADC packages.

## Rule 4 --- Treatment-selection question

If the user asks:

> "Which HER2 treatment should I receive?"

Use PP-0190 plus the appropriate HER2 therapy package.

Do not make an individualized recommendation from PP-0210 alone.

## Rule 5 --- Safety-specific question

If the user asks:

> "How is T-DXd lung toxicity managed?"

Route to ILD/Pneumonitis.

If the user asks:

> "How is trastuzumab cardiac toxicity monitored?"

Route to Cardiac Monitoring.

## Rule 6 --- Resistance question

If the user asks:

> "Why did my HER2 treatment stop working?"

Use PP-0210 for the basic concept and route detailed mechanisms to HER2
Resistance.

------------------------------------------------------------------------

# Retrieval / Knowledge Graph

## Prerequisites

### HER2 Biology

Provides the foundational biological concept.

### HER2 Testing

Provides the clinically relevant HER2 result.

### Biomarker-Directed Treatment Selection

Provides the broader biomarker-to-treatment decision framework.

### Targeted Therapy in Gastric Cancer

Provides the modality-level targeted-therapy concept.

------------------------------------------------------------------------

## Related

-   Biomarker Testing for Targeted Therapy
-   Biomarker Testing for Immunotherapy
-   Molecular Testing
-   Molecular Report Literacy
-   Companion Diagnostics
-   Chemotherapy
-   Immunotherapy
-   Combination Therapy
-   Treatment Response
-   Gastric Cancer Treatment
-   Advanced Gastric Cancer
-   EGJ Adenocarcinoma
-   Precision Oncology

------------------------------------------------------------------------

## Downstream

-   Trastuzumab
-   Trastuzumab Deruxtecan (T-DXd)
-   Antibody-Drug Conjugates
-   ADC Mechanism of Action
-   ToGA Trial
-   DESTINY-Gastric Trial
-   HER2 Resistance
-   Cardiac Monitoring
-   HER2-targeted Therapy Toxicities
-   Combination Therapy
-   Infusion Therapy
-   ILD/Pneumonitis

------------------------------------------------------------------------

# Knowledge Graph Traversal Examples

## Traversal 1 --- Definition

**User:** "What is HER2-targeted therapy?"

→ PP-0210.

## Traversal 2 --- Testing

**User:** "What does HER2 3+ mean?"

→ HER2 Testing.

Then:

→ PP-0210 for treatment implications.

## Traversal 3 --- Initial treatment

**User:** "Why am I getting trastuzumab with chemotherapy?"

→ PP-0210 for modality-level explanation.

→ Trastuzumab for drug-specific information.

→ Chemotherapy package for chemotherapy details.

## Traversal 4 --- T-DXd

**User:** "Why am I being offered T-DXd after trastuzumab?"

→ PP-0210 for treatment-family context.

→ T-DXd for detailed drug-specific context.

## Traversal 5 --- Cardiac safety

**User:** "Why does my doctor check my heart before trastuzumab?"

→ PP-0210 for general safety concept.

→ Cardiac Monitoring for detailed monitoring.

## Traversal 6 --- Lung safety

**User:** "What is ILD from T-DXd?"

→ PP-0210 for awareness.

→ ILD/Pneumonitis for detailed clinical management.

------------------------------------------------------------------------

# Clinical Scope

## Core Runtime Knowledge

-   HER2 as a treatment target.
-   HER2 testing as an upstream prerequisite.
-   HER2-positive treatment relevance.
-   Trastuzumab.
-   T-DXd.
-   HER2 + chemotherapy.
-   Selected HER2 + immunotherapy.
-   Treatment-line context.
-   Benefit.
-   Limitations.
-   Resistance.
-   Major safety awareness.

## Supporting Runtime Knowledge

-   HER2 heterogeneity.
-   Predictive versus prognostic distinction.
-   ADC concept.
-   EGJ inclusion.
-   Biosimilar concept.
-   Patient questions.
-   Clinical trial context.

## Not Owned

-   Detailed HER2 testing.
-   Detailed drug administration.
-   Detailed toxicity.
-   Detailed resistance.
-   Individual treatment recommendation.

------------------------------------------------------------------------

# Authoritative Sources

## Primary Guideline

**NCCN Clinical Practice Guidelines in Oncology --- Gastric Cancer,
Version 2.2026**

Role:

-   disease-specific treatment architecture;
-   HER2-positive advanced disease;
-   trastuzumab;
-   T-DXd;
-   KEYNOTE-811;
-   ToGA;
-   DESTINY-Gastric evidence.

## Primary Professional Evidence Synthesis

**NCI Gastric Cancer Treatment (PDQ®)**

Role:

-   ToGA;
-   KEYNOTE-811;
-   trastuzumab;
-   T-DXd;
-   patient-facing interpretation of treatment evidence.

## Patient-Facing Treatment Sources

**NCI Treatment of Stomach Cancer**

Role:

-   targeted therapy;
-   biomarker-treatment relationship;
-   patient-facing treatment context.

**American Cancer Society --- Stomach Cancer**

Role:

-   HER2 testing;
-   trastuzumab;
-   T-DXd;
-   patient-facing targeted-treatment explanation.

## Supporting Professional Source

**ESMO-ASCO Recommendations for a Global Curriculum in Medical Oncology,
2023**

Role:

-   precision oncology;
-   biomarker-treatment context;
-   multidisciplinary interpretation.

------------------------------------------------------------------------

# Evidence Classification

## Established / Guideline-Supported

-   HER2 is a treatment-relevant biomarker in selected gastric/GEJ
    adenocarcinoma.
-   Trastuzumab + chemotherapy is an established treatment approach for
    appropriate HER2-positive advanced disease.
-   ToGA provides randomized phase III evidence for trastuzumab +
    chemotherapy.
-   T-DXd is an important subsequent HER2-directed treatment in selected
    previously treated HER2-positive advanced disease.
-   DESTINY-Gastric01 and DESTINY-Gastric02 provide supporting clinical
    evidence.
-   KEYNOTE-811 supports selected combination treatment involving
    trastuzumab, chemotherapy, and pembrolizumab.
-   HER2-directed treatments have clinically important adverse effects.

## Context-Dependent

-   Which HER2-directed treatment is appropriate.
-   First-line versus subsequent-line treatment.
-   Choice of chemotherapy backbone.
-   Addition of immunotherapy.
-   T-DXd after prior trastuzumab.
-   Repeat biomarker assessment.
-   Clinical-trial participation.

## Not Owned by This PP

-   HER2 testing methodology.
-   Detailed drug dosing.
-   Detailed toxicity management.
-   Detailed resistance biology.
-   Individualized treatment selection.

------------------------------------------------------------------------

# Governance Metadata

  -----------------------------------------------------------------------
  Field                               Value
  ----------------------------------- -----------------------------------
  Governance Standard                 CORE_WORKING_RULES v1.7

  Gold Specification                  FREEZE GOLD POPULATION PACKAGE
                                      SPECIFICATION v1.1

  Discussion Reference                PP Discussion depth and format
                                      example.md

  Decision Status                     APPROVED / LOCKED

  Artifact Status                     GOLD

  Boundary                            Required in final production
                                      response

  Evidence Basis                      Project Source Files
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Version Control

  -----------------------------------------------------------------------
  Version                 Date                    Change
  ----------------------- ----------------------- -----------------------
  1.0.0                   2026-08-09              Initial Gold production
                                                  after approved/locked
                                                  PP-0210 Decision Batch.

  -----------------------------------------------------------------------

------------------------------------------------------------------------

# Change History

## 1.0.0

Initial release.

Scope locked around:

**HER2 result**

→ **HER2-targeted therapy**

→ **drug-specific downstream packages**

The package deliberately avoids absorbing HER2 testing,
trastuzumab-specific management, T-DXd-specific management, resistance,
cardiac monitoring, or toxicity ownership.

------------------------------------------------------------------------

# Final Status

**GOLD --- READY FOR INTEGRATION**

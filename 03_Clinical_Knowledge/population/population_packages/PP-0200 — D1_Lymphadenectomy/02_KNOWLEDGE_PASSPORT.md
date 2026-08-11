# 02_KNOWLEDGE_PASSPORT --- PP-0200 D1 Lymphadenectomy

## Identity

  Field      Value
  ---------- --------------------
  KP ID      KP-PP-0200
  PP ID      PP-0200
  Title      D1 Lymphadenectomy
  Version    1.0.0
  Status     GOLD
  Decision   APPROVED / LOCKED

## Classification

  ---------------------------------------------------------------------
  Field                              Value
  ---------------------------------- ----------------------------------
  Clinical Domain                    Gastric Cancer --- Surgical
                                     Treatment

  Domain Code                        GC-SURG-LND-D1

  Educational Level                  Patient-facing clinical education

  Clinical Complexity                Intermediate

  Patient Journey Stage              Treatment / Surgical Planning /
                                     Pathology Interpretation

  Package Type                       Atomic Population Package

  Primary Question                   What is D1 lymphadenectomy in
                                     gastric cancer, what regional
                                     nodes does it include, and how
                                     should patients understand its
                                     role?
  ---------------------------------------------------------------------

## Intended Runtime Usage

This package is intended to support patient-facing Medical AI responses
about D1 lymphadenectomy.

The runtime should use this package to explain:

-   the meaning of D1;
-   the regional nodal field;
-   the relationship to gastrectomy;
-   the difference between D1, D1+, and D2;
-   the difference between anatomical extent and node count;
-   the significance of lymph-node examination;
-   the relationship to early gastric cancer and endoscopic treatment;
-   patient questions about surgery and pathology.

The runtime should not use this package to generate individualized
surgical recommendations.

## Retrieval Tags

D1 lymphadenectomy; D1; gastric cancer surgery; stomach cancer surgery;
regional lymph nodes; perigastric lymph nodes; lymph-node dissection;
gastrectomy; D1+; D2; lymph-node yield; 16 lymph nodes; pathological
staging; gastric cancer staging; early gastric cancer; regional
lymphadenectomy; surgical pathology.

## Related Population Packages

-   PP-0199 --- Lymphadenectomy
-   PP-0196 --- Gastrectomy Principles
-   PP-0197 --- Subtotal Gastrectomy
-   PP-0198 --- Total Gastrectomy
-   PP-0193 --- Endoscopic Resection for Early Gastric Cancer
-   PP-0194 --- EMR
-   PP-0195 --- ESD
-   PP-0201 --- D2 Lymphadenectomy
-   PP-0202 --- Sentinel Lymph Node

## Boundary

### Core

-   D1 lymphadenectomy as a defined regional/perigastric lymph-node
    dissection performed with gastrectomy.
-   Source-supported D1 anatomical definition.
-   D1 nodal territory and the supplied station-based description of
    groups 1--7.
-   Relationship of D1 to gastrectomy and oncologic resection.
-   D1 versus D1+ versus D2 at conceptual/comparative level.
-   Selected clinical contexts in which D1 may be considered, with
    source attribution.
-   D1 in early gastric cancer and its relationship to endoscopic
    resection.
-   Distinction between anatomical extent, lymph nodes examined, and
    lymph nodes positive.
-   The ≥16-node examination goal as a separate nodal-yield concept.
-   Relationship between lymph-node assessment and pathological staging.
-   Curative versus palliative context.
-   Patient-facing interpretation, questions, and common misconceptions.
-   Source-supported evidence uncertainty and regional practice
    differences.

### Supporting

-   High-level nodal anatomy.
-   D1+ as an extension of D1.
-   D2 as a comparative reference.
-   Surgical experience and center expertise.
-   Open versus selected minimally invasive context.
-   Spleen/pancreas preservation concepts.
-   Historical D1-versus-D2 evidence context.
-   Pathology interface and staging concepts.

### Explicitly Excluded

-   Detailed D2 anatomy or operative technique.
-   Sentinel lymph-node mapping or biopsy methodology.
-   EMR/ESD technique or detailed eligibility algorithms.
-   Step-by-step lymph-node dissection.
-   Vessel ligation, skeletonization, port placement, instruments,
    robotic workflow, or other operative instructions.
-   Detailed pathology processing.
-   Detailed TNM staging outside the D1/staging interface.
-   Chemotherapy, radiotherapy, immunotherapy, targeted therapy, or
    treatment sequencing.
-   Individualized treatment recommendations or individualized
    prognosis.
-   Detailed postoperative complication management.

### Delegated-to PP

-   PP-0199 --- Lymphadenectomy: general lymphadenectomy framework.
-   PP-0196 --- Gastrectomy Principles.
-   PP-0197 --- Subtotal Gastrectomy.
-   PP-0198 --- Total Gastrectomy.
-   PP-0193 --- Endoscopic Resection for Early Gastric Cancer.
-   PP-0194 --- EMR.
-   PP-0195 --- ESD.
-   PP-0201 --- D2 Lymphadenectomy.
-   PP-0202 --- Sentinel Lymph Node.
-   Downstream treatment and perioperative therapy packages according to
    the Project Coordinator's authoritative execution sequence.

## Clinical Question

> What is D1 lymphadenectomy in gastric cancer, which regional lymph
> nodes does it include, when may it be used, how does it differ from
> D1+ and D2, and what does it mean for staging and oncologic surgery?

## Knowledge Model

### Foundational concept

D1 is an anatomical extent of regional lymph-node dissection.

### Anatomical concept

The current NCCN source describes D1 through the regional/perigastric
nodal field associated with the greater and lesser omenta and specified
gastric nodal regions.

### Station-based concept

The supplied Vietnamese guideline describes D1 as groups 1--7.

### Extension concept

D1+ and D2 represent broader nodal fields.

### Quality/staging concept

The ≥16-node examination goal is distinct from the anatomical definition
of D1.

### Clinical-selection concept

D1 is not a universal operation for every gastric cancer patient.

### Patient-safety concept

D1 should not be interpreted as an instruction to remove the spleen,
pancreas, or other organs.

## Evidence Classification

### Established / Guideline-Supported

-   Gastric resection with curative intent includes regional lymph-node
    assessment/removal.
-   NCCN defines D1 anatomically.
-   The supplied Vietnamese guideline defines D1 as groups 1--7.
-   NCCN defines D2 as D1 plus additional nodal groups along named
    arteries of the celiac axis.
-   NCCN gives a goal of examining at least 16 lymph nodes in the
    resection framework.
-   Selected mucosal early gastric cancers may be candidates for EMR/ESD
    when criteria are met.
-   Routine splenectomy is not indicated without a specific reason.
-   Palliative gastric surgery does not necessarily require lymph-node
    dissection.

### Supported but Context-Dependent

-   D1 versus D1+ selection in early disease.
-   Regional differences in D1/D2 practice.
-   Minimally invasive approaches in selected cases.
-   Comparative D1/D2 outcomes.
-   Exact interpretation of the appropriate lymphadenectomy extent for
    an individual patient.

### Not Established / Must Not Be Overclaimed

-   D1 equals exactly 16 nodes.
-   A node count alone identifies the anatomical extent of surgery.
-   D1 is always safer than D2.
-   D2 is always superior to D1.
-   Every early gastric cancer requires D1.
-   D1 guarantees cure.
-   D1 automatically requires splenectomy or pancreatectomy.

## Primary Guideline Sources

1.  NCCN Guidelines Version 2.2026 --- Gastric Cancer.
2.  Vietnamese gastric-cancer diagnosis and treatment guideline supplied
    in the project Source Files.

## Supporting Sources

1.  American Cancer Society --- Stomach Cancer.
2.  NCI --- Gastric Cancer Treatment PDQ.

## Governance

  ---------------------------------------------------------------------
  Field                              Value
  ---------------------------------- ----------------------------------
  Governance Standard                CORE_WORKING_RULES v1.7

  Gold Specification                 FREEZE GOLD POPULATION PACKAGE
                                     SPECIFICATION v1.1

  Discussion Reference               PP Discussion depth and format
                                     example

  Decision Status                    APPROVED / LOCKED

  QA Status                          PASS --- GOLD --- READY FOR
                                     INTEGRATION

  Repository Status                  Ready for integration

  Evidence Basis                     Project Source Files
  ---------------------------------------------------------------------

## Version Control

  -----------------------------------------------------------------------
  Version                 Date                    Change
  ----------------------- ----------------------- -----------------------
  1.0.0                   2026-08-09              Initial Gold production
                                                  after approved/locked
                                                  Decision Batch.

  -----------------------------------------------------------------------

## Runtime Safety Rules

1.  Do not convert this package into individualized surgical advice.
2.  Do not infer D1 from node count alone.
3.  Do not describe D1 as universally appropriate for every early
    gastric cancer.
4.  Do not claim D1 guarantees complete cancer removal.
5.  Do not imply that D1 requires routine splenectomy.
6.  Do not substitute this package for the operative report or pathology
    report.
7.  Preserve source attribution when explaining context-dependent
    indications.
8.  Escalate individualized questions to the treating clinical team.

## Final Status

**GOLD --- READY FOR INTEGRATION**

# Extended Knowledge Passport

## Patient Journey Placement

### Before PP-0200

The patient may need to understand:

-   gastric-cancer surgery;
-   subtotal versus total gastrectomy;
-   general lymphadenectomy.

These are covered by prerequisite packages.

### PP-0200

The patient learns:

-   what D1 specifically means;
-   how D1 differs from D1+ and D2;
-   why nodes are removed;
-   how node examination relates to staging.

### After PP-0200

The patient may need:

-   D2 lymphadenectomy;
-   sentinel-node concepts;
-   postoperative/perioperative treatment;
-   pathology interpretation;
-   follow-up.

## Knowledge Granularity

### Level 1 --- Definition

D1 is a defined anatomical regional lymph-node dissection.

### Level 2 --- Anatomy

D1 covers specified regional/perigastric nodal territories.

### Level 3 --- Clinical Context

D1 is used in selected surgical contexts rather than universally.

### Level 4 --- Interpretation

Node counts and pathological findings must be distinguished from the
anatomical extent of surgery.

## Concept Relationships

  -----------------------------------------------------------------------
  Concept                             Relationship
  ----------------------------------- -----------------------------------
  Gastrectomy                         D1 is performed with gastric
                                      resection in the NCCN definition

  Lymphadenectomy                     D1 is one extent of lymphadenectomy

  D1+                                 Extension of D1

  D2                                  Broader extent than D1

  Sentinel lymph node                 Separate specialized approach

  EMR/ESD                             Potential alternative for selected
                                      early lesions

  Pathology                           Provides node examination and
                                      positivity data

  N stage                             Uses regional nodal metastasis
                                      information

  Systemic therapy                    Downstream treatment domain
  -----------------------------------------------------------------------

## Evidence Retrieval Rules

When answering a D1 question:

1.  Retrieve the D1 anatomical definition first.
2.  If the user asks about node count, retrieve the ≥16-node
    distinction.
3.  If the user asks about D1 versus D2, retrieve only the comparative
    material needed.
4.  If the user asks whether D1 is needed for early disease, retrieve
    the endoscopic/surgical context.
5.  If the user asks about an individual operation, do not infer from
    generic information; request or defer to operative/pathology
    documentation.
6.  If the user asks about treatment after D1, route to downstream
    treatment packages.

## Evidence Priority Rules

### Priority 1

NCCN current guideline content.

### Priority 2

Supplied Vietnamese guideline when the question concerns its
station-based framework or recommendations.

### Priority 3

NCI PDQ.

### Priority 4

ACS patient-facing explanation.

When sources use simplified language differently, preserve the more
precise current guideline distinction and explicitly identify the
source-specific wording when necessary.

## Safety Boundary

This package is educational.

It does not authorize:

-   individualized surgical selection;
-   individualized staging;
-   individualized treatment selection;
-   operative instructions;
-   interpretation of an individual pathology report without the actual
    report.

## Search Synonyms

-   D1
-   D1 dissection
-   D1 lymphadenectomy
-   D1 lymph node dissection
-   perigastric lymphadenectomy
-   regional lymphadenectomy
-   gastric lymph-node dissection
-   stomach cancer lymph nodes
-   16 lymph nodes
-   D1 versus D2
-   D1+
-   lymph-node yield
-   positive lymph nodes
-   gastric cancer nodal staging

## Evidence Limitations

The project Source Materials provide strong support for the approved D1
scope.

They do not provide a complete modern operative manual for each numbered
station.

Therefore the package intentionally avoids procedural detail.

## Update Logic

Update the Knowledge Passport if:

-   the governing NCCN version changes;
-   the project adopts a new primary guideline;
-   the Vietnamese classification is revised;
-   PP-0201 or PP-0202 boundaries change;
-   the Project Coordinator changes the D1 package ownership.

## Integration Notes

The package is suitable for retrieval in patient questions involving:

-   "D1 lymphadenectomy"
-   "How many lymph nodes are removed?"
-   "What does D1 mean?"
-   "Why are lymph nodes removed?"
-   "D1 versus D2"
-   "16 lymph nodes"
-   "positive lymph nodes after gastrectomy"

The runtime should preserve uncertainty where the evidence is
context-dependent.

## Gold Compliance Checklist

-   Atomic topic: PASS
-   Patient-centered: PASS
-   Evidence-based: PASS
-   Traceable: PASS
-   Reusable: PASS
-   Maintainable: PASS
-   Scalable: PASS
-   Boundary declared: PASS
-   Knowledge graph defined: PASS
-   Runtime safety rules: PASS
-   Versioned: PASS

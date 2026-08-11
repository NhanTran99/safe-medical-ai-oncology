# Clinical Knowledge Object (CKO)

## Metadata

| Field | Value |
|---|---|
| CKO ID | CKO-PP-0218 |
| Population Package ID | PP-0218 |
| Title | RECIST-based Assessment |
| Clinical Domain | Gastric Cancer — Treatment Response |
| Version | 1.0.0 |
| Audience | Patients, caregivers, clinicians, oncology educators, knowledge systems |
| Reading Level | Patient-facing with clinically precise technical explanation |
| Last Updated | 2026-08-09 |

---

# Educational Objectives

After reading this Population Package, the reader should be able to:

- Explain what a RECIST-based assessment does in practice.
- Understand why baseline assessment is needed.
- Distinguish measurable from non-measurable disease at a practical level.
- Understand what target lesions are and why only selected lesions are measured formally.
- Understand the role of the maximum five target lesions and maximum two per organ under RECIST 1.1.
- Understand how target-lesion measurements are combined and followed over time.
- Understand the role of the sum of target-lesion longest diameters.
- Understand that non-target disease is assessed separately and can affect the overall assessment.
- Understand why new lesions can determine progression.
- Understand the special RECIST considerations for lymph nodes.
- Understand how CR, PR, SD and PD emerge from the integrated RECIST assessment.
- Understand why RECIST-based assessment is longitudinal.
- Understand why measurement error matters.
- Understand the context-dependent role of response confirmation.
- Understand why RECIST was developed primarily to standardize response endpoints, especially in clinical trials.
- Understand the distinction between a RECIST result and the broader clinical treatment decision.
- Understand at a high level how RECIST-based assessment interfaces with iRECIST.

---

# Scope

## Core

PP-0218 owns the **application layer** of RECIST 1.1:

- assessment context;
- baseline assessment;
- measurable versus non-measurable disease as used in assessment;
- target-lesion selection;
- target-lesion measurement;
- sum of longest diameters;
- longitudinal comparison;
- non-target disease;
- new lesions;
- lymph-node-specific RECIST considerations;
- integrated CR/PR/SD/PD classification;
- overall RECIST-based assessment;
- progression determination;
- selected response-confirmation rules;
- measurement error;
- clinical-trial endpoint context;
- distinction between RECIST result and individual-patient treatment decisions.

## Supporting

- relationship to PP-0058 RECIST;
- relationship to PP-0059 RECIST 1.1;
- relationship to PP-0060–0067 foundational response packages;
- imaging as the information source;
- iRECIST interface;
- selected gastric-cancer treatment contexts;
- patient questions and misconceptions.

## Not Included

This package does not own:

- general definition-only teaching of RECIST;
- general definition-only teaching of RECIST 1.1;
- detailed post-treatment imaging acquisition;
- CT/MRI/PET acquisition protocols;
- detailed radiology workflow;
- detailed iRECIST algorithm;
- pseudo-progression algorithm;
- treatment-after-progression algorithms;
- treatment selection or dosing;
- prognosis;
- pathological response;
- surveillance;
- recurrence detection.

---

# Knowledge Block 1 — What Is a RECIST-based Assessment?

## Patient Explanation

A RECIST-based assessment is a structured way of using the RECIST framework to describe how solid-tumor disease has changed during treatment.

It is more than asking:

> “Did the biggest tumor get smaller?”

The assessment can consider:

- selected target lesions;
- other non-target disease;
- new lesions;
- changes over time;
- specific rules for some types of lesions, including lymph nodes.

The result can be classified as complete response, partial response, stable disease or progressive disease when the applicable RECIST framework is used.

## Clinical Importance

RECIST provides standardized rules for converting imaging findings into a reproducible response assessment.

ESMO-ASCO identifies RECIST as a harmonized response framework developed particularly to create credible and uniform endpoints across multicentre clinical trials. fileciteturn19file0

---

# Knowledge Block 2 — When Is RECIST Used?

RECIST applies to solid tumors and is especially important in locally advanced or metastatic disease and clinical-trial response assessment.

It is not a universal method for every cancer situation.

In gastric cancer, the appropriate response-assessment approach depends on:

- disease setting;
- treatment intent;
- whether disease is measurable;
- the type of treatment;
- whether standardized response assessment is appropriate.

RECIST should not be confused with cancer staging or surveillance.

---

# Knowledge Block 3 — Why Does Baseline Matter?

A later response assessment needs a reference point.

Baseline describes the disease state against which subsequent measurements are compared.

The baseline assessment may identify:

- measurable disease;
- non-measurable disease;
- candidate target lesions;
- relevant disease sites.

The same patient can therefore have a baseline assessment and several later assessments, allowing disease change to be followed longitudinally.

---

# Knowledge Block 4 — Measurable and Non-measurable Disease

Not every manifestation of cancer can be treated as a target lesion for formal measurement.

RECIST distinguishes between:

### Measurable disease

Disease that can be assessed according to the applicable measurement rules.

### Non-measurable disease

Disease that does not meet the requirements for formal target-lesion measurement.

This distinction does **not** mean that non-measurable disease is clinically unimportant.

Non-target disease can still contribute to the overall RECIST assessment.

---

# Knowledge Block 5 — What Are Target Lesions?

Target lesions are selected lesions used for formal quantitative measurement.

RECIST 1.1 allows:

- up to **5 target lesions in total**;
- up to **2 target lesions per organ**.

The purpose is standardization.

It does not mean that a patient's other lesions are ignored clinically.

It means that a standardized subset is selected for formal quantitative tracking while other disease is assessed through the appropriate non-target framework.

---

# Knowledge Block 6 — How Are Target Lesions Measured?

For target lesions, RECIST 1.1 uses standardized lesion measurements.

For most target lesions, the relevant measurement is the **longest diameter**.

The measurements are recorded consistently so that subsequent examinations can be compared.

The important concept is not simply:

> “How large is the tumor?”

but:

> **“How has the standardized measurement of the selected target disease changed from the reference assessment?”**

Detailed imaging acquisition and modality-specific measurement workflow are delegated to PP-0219.

---

# Knowledge Block 7 — What Is the Sum of Target-lesion Diameters?

The longest diameters of the selected target lesions are combined into a **sum of diameters**.

That sum provides a standardized quantitative representation of the selected target disease.

The sum can then be compared across assessments.

Conceptually:

**Selected target lesions**

→ **measure relevant diameters**

→ **sum measurements**

→ **compare over time**

→ **contribute to response classification**

This is one of the central quantitative components of RECIST-based assessment.

---

# Knowledge Block 8 — Why Is the Nadir Important?

During longitudinal assessment, the smallest recorded target-lesion measurement after treatment begins can become an important reference for evaluating subsequent increase.

This is commonly referred to as the **nadir**.

The nadir should not be confused with the original baseline.

The baseline is the initial reference.

The nadir is the lowest relevant measurement reached after treatment and may become important when evaluating subsequent progression.

The exact RECIST algorithm is supported by the dedicated response-algorithm architecture and is not expanded into a separate mathematical manual here.

---

# Knowledge Block 9 — What Happens to Non-target Disease?

Not all disease is selected as a target lesion.

Non-target disease is assessed separately.

Examples can include:

- lesions that cannot be measured according to target-lesion rules;
- measurable lesions not selected as target lesions;
- other clinically relevant disease manifestations.

Non-target disease may remain stable, improve, worsen or become unequivocally progressive.

Therefore:

> **A RECIST assessment does not depend only on the target-lesion sum.**

The non-target component must also be considered when determining the overall response.

---

# Knowledge Block 10 — What Happens If New Lesions Appear?

New lesions are important because the appearance of new malignant disease can indicate progression.

The assessment therefore asks two different questions:

1. What happened to disease that was already being followed?
2. Has new disease appeared?

A patient can therefore have target lesions that have decreased in size but still have progressive disease if new disease is identified according to the applicable RECIST rules.

This is why:

> **Tumor shrinkage alone does not guarantee an overall response.**

---

# Knowledge Block 11 — Why Do Lymph Nodes Need Special Attention?

Lymph nodes have specific RECIST considerations.

RECIST 1.1 uses a special approach to lymph-node measurement, including a distinction between nodes that are considered pathologically enlarged and smaller nodes.

ESMO-ASCO specifically highlights lymph nodes as requiring special attention and notes that specific rules apply to nodes that disappear and later reappear. fileciteturn19file0

The detailed technical threshold rules belong to the formal RECIST component architecture; PP-0218 explains their role in the integrated assessment.

---

# Knowledge Block 12 — How Does RECIST Produce CR, PR, SD and PD?

RECIST integrates information from:

- target-lesion measurements;
- non-target disease;
- new lesions;
- applicable special lesion rules.

The resulting overall assessment can be categorized as:

### Complete Response (CR)

All applicable RECIST disease findings meet the criteria for complete response.

### Partial Response (PR)

The disease meets the applicable criteria for partial response.

### Stable Disease (SD)

The disease does not meet the criteria for either response or progression.

### Progressive Disease (PD)

The disease meets the applicable criteria for progression.

The individual response categories are explained in greater depth by PP-0063–PP-0066.

PP-0218 owns the **integration process that leads to the overall category**.

---

# Knowledge Block 13 — Why Target-lesion Shrinkage Alone Is Not Enough

Consider two simplified situations.

### Situation A

Target lesions decrease substantially.

No new disease is identified.

Non-target disease does not meet progression criteria.

→ A response may be classified depending on the full RECIST rules.

### Situation B

Target lesions decrease.

A new malignant lesion appears.

→ The overall assessment may be **progressive disease**.

The lesson is:

> **RECIST assesses the whole defined disease picture, not only the change in the largest tumor.**

---

# Knowledge Block 14 — What Is Progressive Disease Under RECIST?

Progressive disease is not simply:

> “The tumor looks a little bigger.”

RECIST uses standardized criteria to determine progression.

Progression can arise from:

- sufficient increase in target disease according to the applicable rules;
- unequivocal progression of non-target disease;
- new malignant lesions.

Once progression is established according to RECIST, the RECIST outcome remains PD even if subsequent changes occur.

ESMO-ASCO explicitly identifies this longitudinal principle. fileciteturn19file0

---

# Knowledge Block 15 — Why Does Measurement Error Matter?

Measurements are not perfectly exact.

Potential sources of variability include:

- lesion shape;
- image quality;
- modality differences;
- reader variability;
- small changes near measurement thresholds;
- differences between examinations.

ESMO-ASCO explicitly identifies measurement error as an important issue and emphasizes the importance of imaging modality at baseline and follow-up. fileciteturn19file0

Therefore:

> **RECIST uses standardized rules partly to reduce inconsistency, but standardized rules cannot eliminate all measurement uncertainty.**

---

# Knowledge Block 16 — Why Should Baseline and Follow-up Assessments Be Comparable?

A meaningful longitudinal comparison depends on reliable measurements.

If assessment conditions differ substantially, apparent change can be harder to interpret.

Therefore response assessment should use an appropriate and consistent imaging approach whenever possible.

The detailed modality and imaging-protocol questions are owned by PP-0219.

---

# Knowledge Block 17 — When Does Response Need Confirmation?

Response confirmation is **context-dependent**.

ESMO-ASCO notes that complete or partial response needs confirmation in single-arm trials when response is a primary endpoint, helping reduce the risk that an apparent response reflects measurement error alone. fileciteturn19file0

This should not be simplified into:

> “Every response in every patient must always be confirmed.”

The requirement depends on the assessment context and protocol.

---

# Knowledge Block 18 — RECIST Was Developed Especially for Clinical Trials

RECIST was developed to harmonize response definitions and provide credible endpoints that can be used consistently across centres and trials.

This is especially important because:

- different hospitals need a common language;
- multicentre trials need standardized endpoints;
- treatment effects need to be compared consistently.

ESMO-ASCO explicitly frames RECIST within this clinical-trial purpose. fileciteturn19file0

---

# Knowledge Block 19 — Does a RECIST Result Decide My Treatment?

No.

A RECIST result provides standardized information about disease change.

For an individual patient, treatment benefit should be assessed using broader medical judgment that integrates:

- clinical status;
- imaging;
- laboratory data;
- treatment context;
- patient-specific circumstances.

ESMO-ASCO explicitly emphasizes this distinction. fileciteturn19file0

Therefore:

**RECIST result**

≠

**automatic treatment order**

---

# Knowledge Block 20 — RECIST and iRECIST

RECIST 1.1 is widely used for standardized response assessment.

For clinical trials testing immunotherapeutics, a specialized framework called **iRECIST** was developed to address immune-related response patterns.

PP-0218 should therefore recognize the interface:

**RECIST 1.1**

↔

**iRECIST**

but does not own the complete iRECIST algorithm.

Detailed immune-specific progression confirmation and pseudo-progression rules are delegated.

ESMO-ASCO explicitly identifies iRECIST as a response framework for trials testing immunotherapeutics. fileciteturn19file0

---

# Knowledge Block 21 — RECIST Is Not Cancer Staging

RECIST and cancer staging answer different questions.

### Staging

> How extensive is the cancer at a defined point in the disease course?

### RECIST-based assessment

> How has defined solid-tumor disease changed under the response-assessment framework?

A RECIST response category should therefore not be substituted for TNM stage.

---

# Knowledge Block 22 — RECIST Is Not Pathological Response

Radiologic response and pathological response are different constructs.

A tumor can:

- appear smaller on imaging;
- show extensive treatment effect under the microscope;
- or show different degrees of radiologic and pathological change.

PP-0218 does not assign or interpret pathological tumor-regression grades.

That knowledge belongs to the pathology/treatment-response architecture.

---

# Knowledge Block 23 — RECIST Is Not Surveillance

RECIST-based assessment is primarily concerned with standardized response evaluation.

Surveillance asks a different question:

> What follow-up is appropriate after treatment, and how should recurrence or new disease be monitored?

Surveillance is delegated to PP-0220.

---

# Common Misconceptions

## Myth 1
“RECIST measures every tumor.”

**Fact:** RECIST uses selected target lesions for formal quantitative assessment while also assessing non-target disease and new lesions.

## Myth 2
“The five target lesions are simply the five biggest tumors.”

**Fact:** RECIST 1.1 uses standardized selection rules, including a maximum of five total and two per organ.

## Myth 3
“If a lesion is not measured, it does not matter.”

**Fact:** Non-target disease can contribute to the overall response assessment.

## Myth 4
“If the target tumors shrink, the patient automatically has a response.”

**Fact:** New lesions and non-target disease can alter the overall classification.

## Myth 5
“Stable disease means the scan was useless.”

**Fact:** SD is a defined RECIST outcome representing disease that does not meet response or progression criteria.

## Myth 6
“Progression means the doctor must immediately stop treatment.”

**Fact:** RECIST provides an assessment; the treatment decision requires broader clinical judgment.

## Myth 7
“RECIST is the same as staging.”

**Fact:** RECIST evaluates treatment-related disease change; staging and response assessment serve different purposes.

## Myth 8
“Complete response means cure.”

**Fact:** CR is a standardized response category and does not by itself establish permanent cure.

## Myth 9
“RECIST and iRECIST are the same.”

**Fact:** iRECIST is a specialized framework developed for trials involving immunotherapeutics.

## Myth 10
“A small measurement change always represents real tumor growth or shrinkage.”

**Fact:** Measurement error and imaging variability can affect assessment.

---

# Key Messages

- RECIST-based assessment is an **integrated process**, not a measurement of one tumor.
- Baseline disease provides the reference for later comparison.
- Only selected lesions are used as target lesions for formal quantitative tracking.
- RECIST 1.1 permits up to five target lesions in total and two per organ.
- Target-lesion measurements are combined as a sum of longest diameters.
- Non-target disease remains clinically relevant.
- New lesions can determine progression.
- Lymph nodes have special RECIST considerations.
- CR, PR, SD and PD are outputs of the integrated assessment process.
- Measurement error is an important limitation.
- Response confirmation is context-dependent.
- RECIST is particularly important for standardized response assessment in clinical trials.
- A RECIST result does not automatically determine an individual's treatment.
- iRECIST provides a specialized framework for selected immunotherapy trials.
- RECIST is not staging, pathological response, prognosis or surveillance.

---

# Patient Questions to Ask

1. Was my disease assessed using RECIST 1.1?
2. Which lesions were selected as target lesions?
3. What was my baseline measurement?
4. What is my current sum of target-lesion diameters?
5. Has the sum changed meaningfully from the relevant reference?
6. What happened to my non-target disease?
7. Were any new lesions identified?
8. Were lymph nodes assessed according to RECIST-specific rules?
9. What is my overall RECIST category: CR, PR, SD or PD?
10. Could measurement uncertainty affect the interpretation?
11. Does the RECIST result need confirmation in my clinical context?
12. Does my clinical condition agree with the imaging assessment?
13. If I am receiving immunotherapy, is an immune-specific response framework relevant?
14. What does this result mean for my overall treatment plan?
15. Which parts of the decision depend on information beyond RECIST?

---

# Knowledge Graph

## Upstream / Foundational

- PP-0058 — RECIST
- PP-0059 — RECIST 1.1
- PP-0060 — Target Lesions
- PP-0061 — Measurable Disease
- PP-0062 — Non-target Lesions
- PP-0063 — Complete Response
- PP-0064 — Partial Response
- PP-0065 — Stable Disease
- PP-0066 — Progressive Disease
- PP-0067 — Response Assessment Algorithm
- PP-0068 — Follow-up Imaging

## Clinical Integration

- PP-0217 — Response Assessment
- **PP-0218 — RECIST-based Assessment**

## Downstream / Adjacent

- PP-0219 — Post-treatment Imaging
- PP-0220 — Surveillance After Gastric Cancer Treatment
- PP-0221 — Recurrence Detection
- PP-0222 — Management of Recurrent Gastric Cancer
- PP-0223 — Metastatic Gastric Cancer
- PP-0231 — Treatment-related Toxicity and Supportive Care
- PP-0232 — Multidisciplinary Management of Gastric Cancer

## Immunotherapy Interface

- PP-0213 — Immunotherapy in Gastric Cancer
- PP-0214 — Immune Checkpoint Inhibitors
- PP-0215 — MSI-H/dMMR Gastric Cancer and Immunotherapy
- PP-0216 — PD-L1-guided Immunotherapy
- iRECIST — specialized response-assessment framework

---

# Boundary

**Core =** Application of RECIST 1.1 to create an integrated response assessment: assessment context; baseline; measurable/non-measurable disease in application; target-lesion selection; target-lesion measurement; sum of longest diameters; longitudinal comparison; non-target disease; new lesions; lymph-node-specific considerations; integrated CR/PR/SD/PD classification; overall RECIST-based assessment; progression determination; selected response-confirmation rules; measurement error; clinical-trial endpoint context; distinction between RECIST outcome and individual-patient clinical decision-making.

**Supporting =** Relationship to RECIST/RECIST 1.1 foundational packages; target/measurable/non-target disease concepts; imaging as the measurement source; gastric-cancer treatment-response context; iRECIST interface; patient-facing interpretation; common misconceptions.

**Explicitly Excluded =** Detailed RECIST definition-only teaching; detailed post-treatment imaging acquisition; CT/MRI/PET technical protocols; detailed radiology workflow; full iRECIST/pseudo-progression algorithm; treatment-after-progression algorithms; treatment selection/dosing; prognosis; pathological response; surveillance; recurrence detection; individualized RECIST interpretation.

**Delegated-to PP =** PP-0058 RECIST; PP-0059 RECIST 1.1; PP-0060 Target Lesions; PP-0061 Measurable Disease; PP-0062 Non-target Lesions; PP-0063 Complete Response; PP-0064 Partial Response; PP-0065 Stable Disease; PP-0066 Progressive Disease; PP-0067 Response Assessment Algorithm; PP-0068 Follow-up Imaging; PP-0217 Response Assessment; PP-0219 Post-treatment Imaging; PP-0220 Surveillance After Gastric Cancer Treatment; PP-0221 Recurrence Detection; PP-0222 Management of Recurrent Gastric Cancer; PP-0223 Metastatic Gastric Cancer; PP-0231 Treatment-related Toxicity and Supportive Care; PP-0232 Multidisciplinary Management of Gastric Cancer; dedicated iRECIST/immune-response package if defined in the authoritative Project Coordinator sequence.

---

# Clinical Safety Boundary

A RECIST category is a standardized assessment result, not an individualized treatment prescription.

A patient should not start, stop or change cancer treatment solely because of a RECIST label.

Individual decisions require the complete clinical context, including symptoms, performance status, imaging, laboratory findings, treatment intent, prior treatment and patient-specific circumstances.

# 02_KNOWLEDGE_PASSPORT.md

# Knowledge Passport

## Identity

| Field | Value |
|---|---|
| KP ID | KP-PP-0198 |
| PP ID | PP-0198 |
| Title | Total Gastrectomy |
| Version | 1.0.0 |
| Status | GOLD — READY FOR INTEGRATION |
| Clinical Domain | Treatment / Surgical Oncology / Gastric Cancer |
| Audience | Patients, caregivers, and general oncology learners |
| Language | English source artifact; patient-facing plain-language style |

---

# Knowledge Classification

## Knowledge Type

Patient-facing clinical education / gastric-cancer surgical literacy.

## Atomic Clinical Question

> **What is total gastrectomy, when and why might the entire stomach need to be removed for gastric cancer, and what should a patient expect after living without a stomach?**

## Primary Function

This PP is the **total-gastrectomy surgical node** between general gastrectomy principles/subtotal gastrectomy and dedicated lymphadenectomy, treatment, and survivorship nodes.

It should be retrieved when the user needs to understand the meaning, rationale, broad conduct, and long-term consequences of complete stomach removal in gastric cancer.

---

# Patient Journey Classification

| Dimension | Classification |
|---|---|
| Primary journey stage | Treatment / Surgical treatment |
| Secondary journey stage | Recovery / Survivorship |
| Decision point | Understanding why total gastrectomy is recommended and what follows it |
| Typical trigger | Patient is considering or has undergone total gastrectomy |
| Upstream need | Understanding general gastrectomy and subtotal versus total choice |
| Downstream need | Lymphadenectomy, systemic therapy, nutrition/survivorship and follow-up |

---

# Intended Runtime Usage

## Primary Runtime Use
- “What is total gastrectomy?”
- “Why do I need my whole stomach removed?”
- “Why can't they just remove part of my stomach?”
- “What happens when the whole stomach is removed?”
- “Will I still be able to eat?”
- “Why do I need small meals after gastrectomy?”
- “Will I need vitamin B12 after total gastrectomy?”
- “Will my spleen be removed?”
- “Do they remove lymph nodes during total gastrectomy?”
- “Can total gastrectomy be done laparoscopically?”
- “What is life like without a stomach?”
- “What are the long-term problems after total gastrectomy?”
- “Can total gastrectomy cure gastric cancer?”
- “Can total gastrectomy be used for diffuse gastric cancer?”
- “Why is total gastrectomy used for some cardia tumors?”

## Secondary Runtime Use

Retrieve when explaining the surgical branch after endoscopic resection is not appropriate, when explaining why subtotal versus total gastrectomy is selected, or when linking surgery to downstream treatment and survivorship.

## Do Not Use as a Substitute For

- Detailed operative instruction.
- D1/D2 lymph-node station mapping.
- Reconstruction technique.
- Individualized nutritional prescriptions.
- Chemotherapy, FLOT, immunotherapy or targeted-therapy selection.
- Individualized prognosis.
- Detailed surveillance or recurrence management.

---

# Retrieval / Runtime Relevance

## High-Priority Retrieval Terms

- `total gastrectomy`
- `complete stomach removal`
- `entire stomach removed`
- `gastrectomy without stomach`
- `total vs subtotal gastrectomy`
- `subtotal versus total`
- `diffuse gastric cancer surgery`
- `cardia gastric cancer surgery`
- `proximal gastric cancer`
- `negative microscopic margin`
- `R0 gastric resection`
- `regional lymphadenectomy`
- `spleen preservation`
- `feeding tube total gastrectomy`
- `laparoscopic total gastrectomy`
- `robotic gastrectomy`
- `life without a stomach`
- `eating after gastrectomy`
- `small frequent meals`
- `postprandial fullness`
- `dumping syndrome`
- `vitamin B12 after gastrectomy`
- `iron deficiency after gastrectomy`
- `vitamin D calcium zinc gastrectomy`
- `weight loss after gastrectomy`
- `quality of life after gastrectomy`
- `gastric cancer survivorship`

## Question-to-Retrieval Mapping

| User question cluster | Retrieval focus |
|---|---|
| Why total rather than subtotal? | total vs subtotal; adequate margins; tumor location; diffuse involvement |
| What happens anatomically? | entire stomach removed; reconstruction; esophagus to small intestine |
| What happens nutritionally? | B12; iron; vitamin D; calcium; zinc; nutritional monitoring |
| What about lymph nodes? | regional lymphadenectomy; D1/D2; lymph-node management |
| What about surgical approach? | open; laparoscopic; robotic; selected cases |
| What about the spleen? | routine splenectomy; spleen involvement; hilar adenopathy |
| What about long-term function? | postprandial fullness; dumping syndrome; diarrhea; reflux; eating restrictions |
| What about treatment after surgery? | perioperative therapy; adjuvant therapy; chemoradiation; downstream treatment |

---

# Knowledge Graph

## Prerequisite PPs

- PP-0196 — Gastrectomy Principles: general oncologic gastrectomy framework.
- PP-0197 — Subtotal Gastrectomy: partial gastric resection and stomach-preservation branch.

## Adjacent / Related PPs

- PP-0199 — Lymphadenectomy.
- PP-0200 — D1 Lymphadenectomy.
- PP-0201 — D2 Lymphadenectomy.
- PP-0202 — Sentinel Lymph Node.
- PP-0228 — Gastric Cancer Survivorship.
- PP-0229 — Long-term Follow-up.

## Downstream PPs

- PP-0203 — Perioperative Chemotherapy.
- PP-0204 — FLOT.
- PP-0205 — Adjuvant Therapy.
- PP-0206 — Neoadjuvant Therapy.
- PP-0207 — Chemoradiation.
- PP-0220 — Surveillance After Gastric Cancer Treatment.

## Cross-Branch Relationships

| PP relationship | Knowledge branch | Relationship |
|---|---|---|
| PP-0193–0195 | Endoscopic resection branch | May precede surgical treatment when endoscopic treatment is not appropriate or adequate. |
| PP-0198 | Total gastrectomy | Current package. |
| PP-0199–0202 | Lymphatic surgery branch | Integrated into the oncologic operation but separately owned. |
| PP-0203–0207 | Perioperative/adjuvant treatment branch | May be combined with surgery depending on stage and clinical plan. |
| PP-0228–0229 | Survivorship/follow-up branch | Owns detailed long-term management beyond the educational consequences described here. |

---

# Runtime Answer Calibration

## Definition request

Start with entire stomach removal, then explain that this is an oncologic operation used selectively.

## Why-question

Lead with tumor location/extent and ability to achieve adequate resection with negative margins.

## Subtotal comparison

Use the central preservation principle; do not imply that total is automatically more effective.

## Diffuse disease

Explain that diffuse gastric involvement is a strong source-supported context for total gastrectomy.

## Cardia/EGJ

Explain selected proximal/cardia use while preserving the boundary around Siewert classification and esophageal cancer.

## Lymph-node question

Explain the role of regional lymphadenectomy and redirect technical D1/D2 content.

## Spleen question

State that routine splenectomy is not indicated; mention involvement/hilar adenopathy as exceptions.

## Reconstruction question

Explain digestive continuity conceptually; do not teach anastomotic technique.

## Eating question

Explain loss of gastric reservoir, smaller amounts and more frequent meals.

## Nutritional question

Explain lifelong risk/monitoring and named deficiencies without prescribing a personal regimen.

## Surgical approach question

Explain selected open/minimally invasive approaches and surgeon expertise.

## Prognosis question

Do not derive individual prognosis from operation type.

## Treatment question

Explain the surgery-treatment interface and defer regimen selection to downstream PPs.

## Surveillance question

Explain that follow-up is needed and defer detailed schedule to PP-0220/0229.

---

# Boundary Enforcement Rules

- Do not answer total-gastrectomy questions by importing the full PP-0197 subtotal-gastrectomy content.
- Do not treat total gastrectomy as automatically more oncologically effective than subtotal gastrectomy.
- Do not turn a selected cardia/proximal indication into a universal rule.
- Do not treat the spleen as routinely removed.
- Do not teach D1/D2 station anatomy inside PP-0198.
- Do not teach reconstruction technique inside PP-0198.
- Do not convert survivorship information into individualized prescriptions.
- Do not convert the surgery node into a chemotherapy or immunotherapy node.
- Do not use operation type alone to predict prognosis.
- Do not use general medical knowledge to create numeric thresholds not present in the Source Materials.

---

# Governance Metadata

| Field | Value |
|---|---|
| Primary guideline | NCCN Gastric Cancer v2.2026 |
| Primary treatment source | NCI Gastric Cancer Treatment PDQ |
| Patient-facing support | ACS Stomach Cancer |
| Long-term survivorship source | NCCN Gastric Cancer v2.2026 survivorship section |
| Source-first verified | Yes |
| Approved Decision Batch | Locked |
| Gold depth standard | Mandatory minimum |
| Boundary format | Core / Supporting / Explicitly Excluded / Delegated-to PP |
| Repository readiness | Ready |
| Version | 1.0.0 |

---

# Revision History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-09 | Initial Approved-GOLD production after Decision Batch lock. |
# Extended Runtime Semantics and Retrieval Design

## Retrieval Intent Cluster A — Procedure Definition

| Query pattern | Intended retrieval behavior |
|---|---|
| what is total gastrectomy | Retrieve definition + purpose + basic consequences |
| whole stomach removed | Retrieve definition + reconstruction concept |
| total stomach surgery | Retrieve definition + patient explanation |
| total gastrectomy meaning | Retrieve definition + selection context |

## Retrieval Intent Cluster B — Why Total?

| Query pattern | Intended retrieval behavior |
|---|---|
| why remove whole stomach | Retrieve tumor-location/extent + margin logic |
| why not subtotal | Retrieve total-versus-subtotal boundary |
| diffuse stomach cancer surgery | Retrieve diffuse-disease rationale |
| cardia tumor surgery | Retrieve conditional proximal/cardia explanation |
| tumor near cardia | Retrieve location/extent logic without inventing a universal rule |

## Retrieval Intent Cluster C — Postoperative Life

| Query pattern | Intended retrieval behavior |
|---|---|
| eating after total gastrectomy | Retrieve meal-capacity/adaptation block |
| life without stomach | Retrieve functional and nutritional blocks |
| weight loss after gastrectomy | Retrieve weight/nutrition context |
| B12 after gastrectomy | Retrieve B12 risk + monitoring concept |
| dumping syndrome after gastrectomy | Retrieve dumping concept + referral to management |
| diarrhea/reflux after gastrectomy | Retrieve long-term symptom context |

## Retrieval Intent Cluster D — Surgical Approach

| Query pattern | Intended retrieval behavior |
|---|---|
| open vs laparoscopic total gastrectomy | Retrieve approach comparison |
| robotic total gastrectomy | Retrieve selected-case/expertise statement |
| minimally invasive gastrectomy | Retrieve NCCN selection conditions |
| feeding tube total gastrectomy | Retrieve selected-support concept |

## Retrieval Intent Cluster E — Boundary Questions

| Query pattern | Ownership |
|---|---|
| D2 lymph node stations | PP-0201 |
| D1 lymphadenectomy | PP-0200 |
| lymphadenectomy overview | PP-0199 |
| FLOT after gastrectomy | PP-0204 |
| perioperative chemotherapy | PP-0203 |
| surveillance schedule | PP-0220/0229 |
| recurrence treatment | PP-0221/0222 |
| metastatic gastric cancer | PP-0223 |

---

# Runtime Safety Rules

- Never infer that total gastrectomy is necessary from tumor location alone without the qualifying language used by the source.
- Never interpret the operation as a stage label.
- Never equate total gastrectomy with metastatic disease.
- Never promise cure because an operation is described as curative intent.
- Never give a personal vitamin/mineral dose from this PP.
- Never state that every patient needs a feeding tube.
- Never state that every patient needs the same postoperative diet.
- Never state that every patient will have dumping syndrome.
- Never state that every patient will lose the same amount of weight.
- Never state that minimally invasive surgery is universally better.
- Never treat a negative margin as proof that recurrence is impossible.
- Never absorb D1/D2 technical content into PP-0198.
- Never absorb EGJ/esophagectomy algorithms into PP-0198.
- Never use the hereditary diffuse gastric cancer source to create an individualized prophylactic-gastrectomy recommendation.

---

# Knowledge Graph Edge Semantics

| Edge | Meaning |
|---|---|
| PP-0196 → PP-0198 | General gastrectomy principles provide prerequisite context for the total-gastrectomy branch. |
| PP-0197 ↔ PP-0198 | Subtotal and total are sibling resection nodes whose boundaries must remain distinct. |
| PP-0198 → PP-0199 | Total gastrectomy introduces regional lymphadenectomy as an integrated but separately owned concept. |
| PP-0199 → PP-0200/0201 | General lymphadenectomy branches to D1/D2. |
| PP-0198 → PP-0203–0207 | Surgery interfaces with perioperative/adjuvant treatment packages. |
| PP-0198 → PP-0228/0229 | Surgery creates long-term survivorship and follow-up needs. |
| PP-0198 ↔ PP-0193–0195 | Endoscopic resection and surgical resection are alternative/transition pathways in selected early disease. |

---

# Knowledge Normalization Rules

- “Total gastrectomy”, “complete stomach removal” and “removal of the entire stomach” should normalize to the same PP concept.
- “Partial gastrectomy” and “subtotal gastrectomy” should not normalize to PP-0198; they belong to PP-0197 when the question is specifically subtotal gastrectomy.
- “Gastrectomy” without an extent qualifier should normally retrieve PP-0196 first, then route to PP-0197 or PP-0198 when the extent becomes clear.
- “Total gastrectomy with D2” should retrieve PP-0198 for the operation context and PP-0201 for detailed D2 knowledge.
- “Total gastrectomy after FLOT” should retrieve PP-0198 for surgery and PP-0204 for FLOT.
- “Nutrition after total gastrectomy” should retrieve PP-0198 for consequences and PP-0228/0229 for detailed survivorship management.
- “Cardia cancer” should not automatically normalize to PP-0198 because the clinical question may belong to the EGJ/esophageal branch.

---

# Runtime Answer Templates

## Short definition

“Total gastrectomy is surgery that removes the entire stomach. It is used in selected gastric cancers when this extent of resection is needed to remove the cancer appropriately.”

## Why total

“The decision depends mainly on where the tumor is, how far it extends, and whether adequate cancer removal can be achieved while leaving part of the stomach.”

## Why not subtotal

“A subtotal operation may be appropriate when enough stomach can remain while still achieving adequate cancer removal. When that is not possible, total gastrectomy may be needed.”

## Life after surgery

“After the stomach is removed, the digestive tract is reconstructed. Eating remains possible, but meal size, frequency and nutritional follow-up change substantially.”

## Nutritional issue

“Long-term deficiencies including B12, iron, vitamin D, calcium and zinc can occur after gastrectomy, so lifelong monitoring may be needed.”

## Spleen

“The spleen is not routinely removed. NCCN reserves splenectomy for selected circumstances such as spleen involvement or extensive hilar adenopathy.”

## Minimally invasive

“Laparoscopic or robotic surgery can be considered in selected patients when appropriate expertise is available; it is not universally recommended.”

## Prognosis

“Total gastrectomy alone cannot determine an individual prognosis. Prognosis depends on stage, pathology, biology and the overall treatment plan.”

# Extended Runtime Disambiguation

## Gastrectomy vs Total Gastrectomy

Use PP-0196 when the user asks about gastrectomy generally. Use PP-0198 when the user explicitly asks about complete stomach removal or total gastrectomy.

## Total vs Subtotal

Use PP-0197 when the question is specifically about preserving part of the stomach or subtotal resection. Use PP-0198 when the question centers on complete stomach removal and its consequences.

## Surgery vs Survivorship

Use PP-0198 for the educational consequences of total stomach removal. Route detailed nutritional monitoring, supplementation, bone-health protocols and long-term follow-up to the relevant survivorship packages.

## Surgery vs Treatment Regimen

Use PP-0198 for the operation and its role in the treatment pathway. Route chemotherapy, FLOT, immunotherapy, targeted therapy and chemoradiation questions to their dedicated PPs.

## Surgery vs EGJ

Use PP-0198 for the conceptual relevance of proximal/cardia tumors. Route detailed Siewert classification, esophageal resection and EGJ treatment decisions to the dedicated EGJ/esophageal branch.

## Surgery vs Lymphadenectomy

Use PP-0198 for the fact that regional lymph-node management accompanies curative gastric surgery. Route D1/D2 station and technical questions to PP-0199–0201.

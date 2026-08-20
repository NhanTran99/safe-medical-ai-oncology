# B06 Situation Navigation Mapping (Phase 6 Stage 2 Track 3, B06)

## What this is

`b06_situation_navigation_mapping.json` is the single authoritative source
for the Chat UI's Situation -> Topic navigation layer (B06). It is
**navigation metadata only**:

```text
Approved Situation (5, locked)
  -> relevant existing case_id(s) (EC-NNNN)
```

It is consumed by `api/main.py` (`_load_situation_mapping()`) and rendered
by `api/chat_ui.py`, which uses it to filter the existing 239-entry
navigation `CATALOG` when a patient selects a Situation.

## What this is NOT

- **not** a second PP/case authority — every `case_id` in this file must
  already exist in `evaluation_case_manifest_projection.json`
  (`EvaluationCaseResolver`'s manifest projection remains the sole PP/case
  authority; this file only *references* that identity, never redefines
  it);
- **not** a clinical knowledge source — it carries no clinical content,
  only `(situation_id, case_id)` pairs and the five Situation labels;
- **not** a replacement for `controlled_question` — the existing governed
  Question Starter text is unchanged and untouched by this file;
- **not** a runtime-inferred mapping — there is no LLM classification, no
  keyword matching, and no heuristic at request time; the mapping is a
  static, explicit, version-controlled list, read as-is by the runtime.

## The five approved Situations (locked, B06 Strategy/Scope)

1. I was recently diagnosed
2. I'm receiving treatment
3. I'm preparing for surgery
4. I'm concerned about recurrence
5. I'm in follow-up

No sixth Situation exists in this artifact. The repository's earlier,
pre-B06 Chat UI additionally displayed a sixth, unmapped, purely
presentational string ("I want to understand my cancer") introduced in
Track 1C; that string is explicitly out of B06's approved Situation scope
(see the B06 Strategy/Scope material) and is not represented here.

## Mapping methodology and its limits

Every relationship in `mappings` was reviewed against the governed PP
content actually stored in the repository — each PP's `01_CKO.md`
Educational Objectives (or, for the older CKO template variant, its
Clinical Question / Purpose / Scope-Included sections) — using the locked
B06 D02 Minimum Relevance Rule: a mapping is included only where a
reasonable patient in that Situation could plausibly want to learn about,
understand, or ask a question about that Topic, within the PP's existing
governed scope, **and** the governed content itself (not the title alone)
supports that relationship. Relationships are many-to-many (D01) with no
primary/secondary ordering (D04); a Topic with no defensible relationship
to any of the five Situations is simply absent from `mappings` (D07)
rather than forced into one for numeric coverage (D03).

Two content signals were deliberately **not** treated as sufficient
evidence on their own, because review showed they are boilerplate rather
than discriminating: the CKO `Audience` metadata field (it reads
"patients, caregivers, general public" even on deeply technical ACMG
variant-evidence-code entries) and the generic closing objective present
on almost every PP ("feel more confident discussing X with the healthcare
team"). A mapping was only retained where the *substantive* educational
objectives specifically tied the topic to a Situation-relevant patient
question (e.g. "why HER2 testing is performed" supports "I'm receiving
treatment"; "understand that the ACMG framework evaluates scientific
evidence rather than making treatment decisions" does not).

Categories of PP left deliberately unmapped after content review: ACMG
variant-classification evidence codes and the variant-interpretation/
classification glossary (technical laboratory-report reference content,
not patient-journey-situational); molecular-mechanism sub-topics narrower
than their own governed treatment-overview PP (e.g. ADC payload/linker/
bystander-effect chemistry, once the ADC mechanism-of-action overview
already answers "how does my treatment work"); sequencing-technology
comparison topics (NGS vs. WGS vs. WES vs. gene panel — methodology
comparison, not tied to a specific treatment decision in the governed
content); raw TNM sub-category and RECIST technical criteria definitions;
population screening/prevention epidemiology topics explicitly framed
around risk reduction for people who are not yet diagnosed; and a small
number of items where the governed content's framing was procedural/
clinical-workflow-oriented rather than patient-entry-oriented (see the
correction change log below).

### v1.0 -> v2.0 correction (content-grounded review)

v1.0 was authored primarily from `pp_title` labels. v2.0 reviewed every
v1.0 mapping (and the v1.0 unmapped set) against actual governed PP
content. This section uses precise, non-overlapping terminology:

- a **relationship pair** is one `(situation_id, case_id)` entry in
  `mappings`;
- a **PP-level Situation membership change** ("moved") describes a
  `case_id` whose set of Situations changed between versions; each such
  move is *represented as* one removed relationship pair plus one added
  relationship pair for that `case_id` — it is not a third, independent
  kind of operation, and is never added on top of the removed/added
  pair counts below.

**Relationship-pair accounting (exact, machine-verified):**

| | Count |
|---|---|
| v1.0 total relationship pairs (X) | 174 |
| v2.0 total relationship pairs (Y) | 167 |
| Unchanged relationship pairs (U) | 162 |
| Removed relationship pairs (R) | 12 |
| Added relationship pairs (A) | 5 |

Invariant: `U + R = X` (162 + 12 = 174) and `U + A = Y` (162 + 5 = 167),
therefore `Y = X - R + A` (174 - 12 + 5 = 167).

**PP-level accounting:** v1.0 mapped 153 unique PP; v2.0 maps 146 unique
PP. Of the 12 removed relationship pairs, 9 belong to PP that lost their
only Situation membership (**pure removals**, 9 PP: `EC-0030`, `EC-0154`,
`EC-0160`, `EC-0162`, `EC-0163`, `EC-0164`, `EC-0169`, `EC-0234`,
`EC-0235`) and 3 belong to PP whose *only* Situation changed (**moved**,
see below). Of the 5 added relationship pairs, 2 belong to PP newly
mapped for the first time (**pure additions**, 2 PP: `EC-0024`,
`EC-0042`) and 3 are the add-half of the 3 moves. Unique-PP arithmetic:
`153 - 9 + 2 = 146`, matching the actual v2.0 count exactly.

**Pure removals** (title suggested a relationship the actual content did
not support): `EC-0030` Stomach Cancer Screening, `EC-0162` Smoking,
`EC-0163` Diet, `EC-0164` Obesity, `EC-0169` Gastric Adenomas (all
explicitly framed around prevention/risk-reduction for the not-yet-
diagnosed population, not post-diagnosis understanding); `EC-0234`
Germline Genetic Testing, `EC-0235` Somatic Genetic Testing (content is a
testing-modality comparison, not concretely tied to a Situation);
`EC-0154` Hereditary Gastric Cancer Risk Assessment and `EC-0160`
H. pylori and Gastric Cancer Prevention (borderline — repository content
did not clearly settle a patient-entry framing; removed rather than
retained on insufficient evidence).

**Moved** (3 PP-level Situation memberships moved, corresponding to
exactly 3 of the 12 removed relationship pairs and 3 of the 5 added
relationship pairs — not an additional 3 relationship-pair operations):
`EC-0165` Atrophic Gastritis, `EC-0166` Intestinal Metaplasia, `EC-0167`
Pernicious Anemia — each moved from SIT-01 "I was recently diagnosed" to
SIT-05 "I'm in follow-up", since their governed content is explicitly
framed around a person already diagnosed with the precursor condition
needing ongoing surveillance, not a newly-diagnosed-with-cancer framing.

**Pure additions** (content review found a defensible relationship the
title-only pass missed): `EC-0024` ADC Mechanism of Action (its
Educational Objectives directly explain the treatment the patient is
receiving); `EC-0042` TNM Staging System (a patient-facing staging
overview parallel to the already-mapped `EC-0008`, consistent with how
other duplicate-topic PP pairs in this manifest are both mapped).

This remains a reviewable, correctable baseline, not a clinically
validated taxonomy: the mapping is data, not code, so it can be corrected
in place (adding, removing, or moving a `{situation_id, case_id}` entry)
without any runtime code change, subject to the same review process as
any other governed content change. `tests/test_situation_navigation_mapping.py`
enforces the structural invariants (every referenced `case_id` and
`situation_id` is valid, no duplicate entries) on every change.

## Schema

```json
{
  "artifact_type": "B06_SITUATION_NAVIGATION_MAPPING",
  "artifact_version": "2.0",
  "description": "...",
  "review_methodology": "...",
  "source_manifest": "<same frozen manifest identity as the case manifest projection>",
  "source_manifest_version": "...",
  "source_manifest_sha256": "...",
  "situations": [ { "situation_id": "SIT-01", "label": "I was recently diagnosed" }, ... ],
  "mappings": [ { "situation_id": "SIT-01", "case_id": "EC-0001" }, ... ]
}
```

`source_manifest`/`source_manifest_version`/`source_manifest_sha256` are
copied from `evaluation_case_manifest_projection.json` purely for
traceability (so this file's `case_id` references can be audited back to
the same frozen manifest identity) — they do not make this file a second
manifest.

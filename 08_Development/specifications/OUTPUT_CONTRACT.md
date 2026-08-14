# OUTPUT_CONTRACT.md

Status: **LOCKED — Phase 5 Implementation Readiness**
Decision: **IR13 APPROVED**
Purpose: Governed runtime interface defining what constitutes a valid Safe Medical AI output.

## 1. Purpose and Boundary

This document defines the contract between response generation and output validation.

It specifies:
- required runtime inputs;
- evidence requirements;
- canonical output structure;
- provenance/traceability requirements;
- safety/governance constraints;
- validation and failure states.

It does NOT define:
- clinical knowledge content;
- retrieval algorithm;
- LLM provider/model;
- UI design;
- deployment policy;
- medical policy.

## 2. Runtime Input Contract

Response generation may operate only on validated runtime inputs.

Required conceptual inputs:

1. User request / intent
2. Navigation Context
3. Runtime Evidence Package
4. Applicable safety/governance context
5. Response/delivery constraints

Generation must not treat uncontrolled model knowledge as a substitute for the Runtime Evidence Package.

## 3. Evidence Contract

Meaningful clinical factual claims must have a traceable evidence basis in the Runtime Evidence Package.

The runtime must distinguish:

```text
Evidence sufficient
vs
Evidence insufficient
```

When evidence is insufficient for a required claim, the system must use a controlled insufficiency/fallback behavior rather than silently supplementing the claim from model knowledge.

## 4. Canonical Output Structure

The runtime output concept contains:

```text
Response
├── content
├── evidence / provenance references
├── safety / validation metadata
├── uncertainty / limitation state
└── delivery status
```

The exact implementation schema may be represented as typed runtime models, but field-level JSON/schema details are an implementation specification and must remain consistent with this contract.

## 5. Provenance and Traceability

Clinical knowledge output must support traceability:

```text
Response claim
→ Runtime Evidence Package
→ Knowledge Asset / Population Package
→ Primary Evidence / controlled source
→ controlled repository state
```

Provenance references must be preserved through generation and validation.

## 6. Safety and Governance Constraints

The output contract must support explicit handling of:

- insufficient evidence;
- uncertainty;
- conflicting evidence;
- unsafe or disallowed requests;
- out-of-scope requests;
- validation failure.

A successful LLM generation call is not sufficient to make an output valid.

## 7. Validation Contract

Validation is a controlled gate after generation.

Conceptual validation sequence:

```text
Structural
→ Evidence
→ Safety
→ Governance
→ Output Contract
→ Final Decision
```

The implementation must preserve the separation between:
- generation;
- validation;
- final delivery decision.

## 8. Controlled Outcomes

The system must support three controlled outcomes:

### PASS
Mandatory output requirements are satisfied and the response may proceed to delivery.

### FAIL
A mandatory requirement fails. The generated content must not be delivered as a normal clinical answer.

### SAFE FALLBACK
The system returns a constrained response appropriate to the identified failure/insufficiency state.

The exact user-facing wording is implementation/delivery work and must remain consistent with the safety framework.

## 9. Relationship to Other Controlled Specifications

```text
Runtime Evidence Package
= evidence/context supplied to generation

OUTPUT_CONTRACT
= requirements for a valid generated output

OUTPUT_VALIDATION_FRAMEWORK
= how the generated output is evaluated
```

These are separate controlled components and must not be merged.

## 10. Traceability / Audit Requirements

A final delivered clinical response must be auditable to the extent defined by the project governance and runtime evidence architecture.

At minimum, the implementation should preserve:
- request/interaction trace identifier;
- evidence/provenance references;
- validation outcome;
- relevant failure/fallback state.

## 11. Deferred Implementation Details

The following are intentionally not locked here:

- exact JSON field names beyond the conceptual contract;
- exact Pydantic model layout;
- exact API serialization format;
- UI presentation;
- LLM provider/model;
- retrieval engine.

These must be decided in implementation specifications without weakening this contract.

## 12. Acceptance Principle

An output is valid only when the mandatory contract and validation requirements are satisfied.

```text
Generation success ≠ Output validity
Output validity = Contract + Evidence + Safety + Validation
```

This document is authoritative for the Phase 5 runtime output contract.

# TASK #008 — IMPLEMENTATION SPECIFICATION
## Validation Boundary
### Version 1.0 — Implementation Handoff

---

# 1. Purpose

Implement the locked Task #008 Validation boundary:

```text
CandidateResponse
      ↓
Validation
      ↓
ValidationResult
```

This specification implements only the decisions approved and locked through
Task #008 Architecture / Scope Gate B1–B4.

**No implementation is authorized outside this scope.**

---

# 2. Authoritative Baseline

Branch:

`phase5/task002-scaffolding`

Current authoritative remote baseline:

`8fdf22298d573903ab9f4f146173e2f526095e30`

Task #007 is CLOSED / PASS / REMOTE VERIFIED.

The existing implemented pipeline is:

```text
Repository
  ↓
Population / PP
  ↓
canonical Gold artifacts
  ↓
Retrieval
  ↓
Runtime Evidence Package
  ↓
Runtime Integration
  ↓
GenerationContext
  ↓
Generation
  ↓
Candidate Response
```

Task #008 adds:

```text
Candidate Response
  ↓
Validation
  ↓
ValidationResult
```

Do not modify upstream retrieval/evidence/integration/generation contracts unless
a genuine compatibility blocker is discovered and explicitly escalated.

---

# 3. Locked Scope

## 3.1 Core

Task #008 must implement:

- Validation input boundary;
- CandidateResponse evaluation;
- authoritative RTEP/evidence inspection;
- validation outcome semantics;
- ValidationResult;
- traceability preservation;
- immutable validation state;
- explicit failure behavior;
- deterministic, atomic validation;
- tests protecting the architectural boundary.

## 3.2 Supporting

May include:

- validation models;
- validation policy/version representation;
- structured findings/reasons;
- README/documentation;
- helper functions internal to the validation package;
- test fixtures needed to prove locked behavior.

## 3.3 Explicitly Excluded

Do not implement:

- retrieval/re-retrieval;
- repository access;
- filesystem access;
- web search;
- semantic retrieval;
- embeddings;
- vector DB;
- reranking;
- deduplication;
- provenance repair;
- evidence enrichment;
- LLM judge;
- provider switching/retry;
- response regeneration;
- clinical reasoning;
- diagnosis;
- treatment recommendation;
- patient-specific clinical safety adjudication;
- final clinical approval;
- human approval workflow;
- deployment;
- monitoring;
- UI;
- production safety infrastructure.

## 3.4 Delegated / Downstream

- Final response/final delivery behavior;
- clinical/safety adjudication beyond this validation contract;
- production deployment and operational monitoring.

If a requirement belongs here, flag it rather than expanding Task #008.

---

# 4. Architecture Boundary

Validation is a downstream evaluator.

```text
Generation
    ↓
CandidateResponse
    ↓
Validation
    ↓
ValidationResult
```

Validation may inspect:

```text
CandidateResponse
RTEP
traceability context
validation policy/version
```

Validation may NOT initiate upstream operations.

Dependency direction must remain one-way:

```text
generation → validation
integration/evidence → validation (read-only)
```

Do not introduce reverse dependencies from upstream modules into validation.

---

# 5. Input Contract

Implement one typed validation input boundary.

Conceptual contents:

```text
ValidationInput
├── candidate_response
├── authoritative RTEP / evidence context
├── traceability context
└── validation policy/version
```

Requirements:

- typed;
- immutable;
- explicit;
- no raw repository request;
- no raw retrieval request;
- no hidden global state.

CandidateResponse remains the subject being evaluated.

RTEP remains authoritative evidence.

---

# 6. Output Contract

Implement one authoritative:

```text
ValidationResult
```

Minimum semantic contents:

```text
ValidationResult
├── outcome
├── validated candidate reference
├── findings / reasons
├── traceability
└── validation metadata
```

Do not convert ValidationResult into a FinalResponse.

Do not mutate CandidateResponse.

---

# 7. Outcome Vocabulary

Validation outcome values must be disjoint from:

- RetrievalOutcome;
- RTEPAssemblyOutcome;
- RuntimeIntegrationOutcome;
- GenerationOutcome.

At minimum the semantic vocabulary must distinguish:

```text
VALID
INVALID
SAFE_FALLBACK
```

Additional technical failure values may be introduced only when necessary to
represent the locked B3 failure taxonomy without semantic ambiguity.

Do not reuse upstream enum literals if that creates vocabulary collision.

---

# 8. Failure Semantics

## 8.1 Invalid input

Malformed/missing required validation input:

```text
INVALID_INPUT
```

No partial ValidationResult.

## 8.2 Missing evidence

If evidence is required but no authoritative RTEP/evidence context exists:

```text
MISSING_EVIDENCE
```

No retrieval is attempted.

## 8.3 Insufficient evidence

RTEP exists but does not satisfy the validation prerequisite:

```text
INSUFFICIENT_EVIDENCE
```

No retrieval, reranking, enrichment or repair.

## 8.4 Invalid candidate

Malformed CandidateResponse:

```text
INVALID_CANDIDATE
```

Validation must not repair the candidate.

## 8.5 Validation mechanism failure

If the validation mechanism itself fails technically:

```text
VALIDATION_FAILURE
```

Never convert technical failure to VALID.

## 8.6 Empty evidence

EMPTY evidence must remain distinguishable from invalid candidate and clinical
failure.

Do not automatically label EMPTY as clinically unsafe.

Its handling must follow the locked validation contract.

## 8.7 Safe fallback

`SAFE_FALLBACK` means only that the candidate cannot be used and the contract
permits a downstream fallback state.

It does NOT authorize Validation to generate a clinical alternative.

---

# 9. Failure Precedence

Use deterministic precedence so one invocation has one authoritative outcome.

Recommended locked order:

```text
1. INVALID_INPUT
2. MISSING_EVIDENCE / INSUFFICIENT_EVIDENCE
3. INVALID_CANDIDATE
4. VALIDATION_FAILURE
5. VALID / SAFE_FALLBACK
```

Do not allow a later success state to override an earlier prerequisite failure.

---

# 10. Atomicity

Each validation invocation returns exactly one authoritative result.

Forbidden states:

```text
VALID + hidden failure
INVALID + partial approval
SAFE_FALLBACK + hidden VALID
```

No partially approved CandidateResponse may escape the validation boundary.

---

# 11. Determinism

Given the same:

```text
CandidateResponse
+
authoritative RTEP/evidence
+
traceability context
+
validation policy/version
```

the semantic validation outcome must be deterministic.

No random acceptance.

No hidden external retrieval.

No provider-dependent validation.

---

# 12. Traceability

ValidationResult must preserve enough identifiers to trace:

```text
CandidateResponse
    ↓
Generation
    ↓
Runtime Integration
    ↓
RTEP
    ↓
Retrieval
```

Do not fabricate provenance or identifiers.

Do not silently discard authoritative traceability.

---

# 13. Immutability

Validation must not mutate:

- CandidateResponse;
- RTEP;
- EvidenceItem;
- evidence provenance;
- generation metadata;
- integration metadata.

Behavioral tests must prove that post-validation mutation attempts are rejected
or cannot leak through the ValidationResult.

---

# 14. Evidence-Support Boundary

When validation evaluates whether a CandidateResponse is supported by evidence:

- inspect only authoritative RTEP/evidence already supplied;
- preserve original evidence ordering;
- preserve provenance;
- do not retrieve additional evidence;
- do not rerank;
- do not deduplicate;
- do not repair provenance;
- do not enrich evidence.

Validation is an evaluator, not a research/retrieval agent.

---

# 15. Clinical / Safety Boundary

This task must explicitly preserve:

```text
VALID ≠ clinically safe
```

VALID means:

> CandidateResponse satisfies the locked Validation contract.

It does not mean:

- diagnosis is correct;
- treatment is appropriate;
- patient-specific recommendation is safe;
- clinical approval has occurred.

Clinical/safety adjudication and final approval remain outside Task #008.

---

# 16. Implementation Surface

Create an isolated package under:

```text
08_Development/implementation/src/safe_medical_ai/validation/
```

Expected conceptual surface:

```text
validation/
├── __init__.py
├── models.py
├── validation.py
└── README.md
```

This is a target surface, not permission to create unnecessary files.

Use the smallest coherent implementation that satisfies the locked contract.

One explicit public validation entry point is required.

---

# 17. Tests

At minimum test:

### Contract
- ValidationInput required fields;
- ValidationResult required fields;
- outcome vocabulary;
- immutability.

### Success
- valid CandidateResponse;
- traceability preservation;
- evidence preservation.

### Evidence states
- missing evidence;
- empty evidence;
- insufficient evidence.

### Candidate states
- malformed candidate;
- invalid candidate.

### Technical failure
- validation mechanism failure.

### SAFE_FALLBACK
- correct semantic state;
- no accidental clinical answer generation.

### Atomicity
- one authoritative result;
- no partial approval.

### Determinism
- repeated identical inputs produce the same semantic outcome.

### Boundary protection
Static/behavioral checks proving validation does not use:

- RepositorySource;
- RetrievalService;
- `.retrieve(`;
- filesystem APIs;
- web search;
- vector DB;
- embeddings;
- LLM provider;
- generation retry;
- evidence repair;
- clinical reasoning.

### Regression
All existing tests from Task #002–#007 must continue to pass.

---

# 18. Acceptance Criteria

Task #008 implementation is PASS only when all are true:

1. Validation boundary implemented.
2. Typed ValidationInput implemented.
3. Typed ValidationResult implemented.
4. Outcome vocabulary is disjoint.
5. Locked failure semantics implemented.
6. Atomicity implemented.
7. Determinism implemented.
8. Traceability preserved.
9. CandidateResponse remains immutable.
10. RTEP/evidence remains immutable.
11. No hidden retrieval/recovery path.
12. No clinical safety adjudication introduced.
13. SAFE_FALLBACK does not generate a clinical alternative.
14. Architectural boundary tests pass.
15. New validation tests pass.
16. Full regression suite passes.
17. `git diff --check` passes.
18. Only authorized `08_Development/**` scope changes.
19. No governance/clinical/project-management files are modified.
20. No unauthorized Git history changes are made.

---

# 19. Automatic Rejection Conditions

Reject the implementation if it introduces:

- retrieval;
- re-retrieval;
- repository access;
- semantic/vector retrieval;
- embeddings;
- reranking;
- deduplication;
- provenance repair;
- evidence enrichment;
- LLM judge;
- response regeneration;
- provider switching/retry;
- clinical reasoning;
- diagnosis/treatment logic;
- clinical safety adjudication;
- final approval;
- deployment;
- monitoring;
- UI;
- unauthorized governance changes.

---

# 20. Git / Commit Boundary

Claude must:

- inspect the current implementation first;
- implement only this specification;
- run the required tests;
- run `git diff --check`;
- verify scope;
- export a working-tree patch;
- report exact changed files;
- report exact test results;
- report blockers/ambiguities.

Claude must NOT:

- commit;
- push;
- rebase;
- rename/recreate the authoritative branch;
- alter locked governance;
- modify unrelated local materials.

Controlled sequence remains:

```text
Claude implementation
→ patch export
→ ChatGPT review
→ VS Code apply
→ full verification
→ explicit staging
→ staged diff review
→ controlled commit
→ push
→ remote verification
→ closeout
```

Never use:

```text
git add .
```

---

# 21. Required Claude Final Report

Return:

1. implementation summary;
2. exact changed file list;
3. exact tests added/modified;
4. test commands;
5. complete test result;
6. `git diff --check` result;
7. scope verification;
8. prohibited-functionality confirmation;
9. patch path;
10. blockers or decisions requiring governance review.

Do not claim commit, push, remote verification or task closure unless actually
performed.

---

# 22. Task #008 Completion Definition

After Claude implementation:

**IMPLEMENTATION COMPLETE — PENDING CHATGPT REVIEW**

After ChatGPT review PASS:

**READY FOR VS CODE APPLY**

Task #008 becomes:

**CLOSED / PASS / REMOTE VERIFIED**

only after:

- patch applied;
- full tests PASS;
- staged diff reviewed;
- controlled commit;
- push;
- remote SHA verified;
- closeout recorded.

The next IR artifact will then be created **once**, as:

`PHASE_5_IMPLEMENTATION_READINESS_DECISION_RECORD_v11.0.md`

It will contain the complete Task #008 B1–B4 locked decision set plus the
implementation closeout, using the v6.0 record format.

---

# 23. Locked Decision Provenance

This specification is authorized by:

- Task #008 B1 — Validation Boundary;
- Task #008 B2 — Validation Contract;
- Task #008 B3 — Validation Failure / Safety Semantics;
- Task #008 B4 — Implementation Surface + Tests + Acceptance.

All four batches are **APPROVED / LOCKED**.

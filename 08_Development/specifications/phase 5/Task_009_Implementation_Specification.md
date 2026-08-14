# Task #009 — Implementation Specification

**Phase:** Phase 5
**Task:** #009 — Safety Enforcement Boundary
**Architecture/Scope Gate:** B1–B4 APPROVED and LOCKED
**Implementation status:** Not started

## 1. Objective

Implement the governed Safety Enforcement boundary that converts an incoming request and governed safety context into one immutable, traceable `SafetyDecision`.

The implementation must be deterministic, fail closed, and must not invoke downstream runtime layers.

## 2. Controlled Contract

### Risk classes

```text
LOW
MODERATE
HIGH
EMERGENCY
```

### Safety actions

```text
ALLOW
ALLOW_WITH_WARNING
ASK_CLARIFICATION
REDIRECT
ESCALATE
REJECT
```

No additional action values may be introduced without reopening the architecture gate.

## 3. Implementation Surface

```text
08_Development/implementation/src/safe_medical_ai/safety/
├── __init__.py
├── models.py
├── enforcement.py
└── README.md
```

Tests:

```text
08_Development/implementation/tests/
├── test_safety_models.py
└── test_safety_enforcement.py
```

Implementation changes are confined to `08_Development/**`.

## 4. Typed Models

`SafetyDecision` must preserve at minimum:

```text
request_id
decision_id
policy_version
risk_class
reason_code
action
timestamp
```

Models must be immutable.

## 5. Deterministic Entry Point

Provide one authoritative public enforcement entry point, e.g.:

```text
evaluate_safety(...) -> SafetyDecision
```

Exact Python naming may follow repository conventions.

The Safety module must not invoke:

```text
RepositorySource
RetrievalService
assemble_runtime_evidence_package
integrate_runtime_context
LLMAdapter
generate_candidate_response
validate_candidate_response
```

## 6. Policy Boundary

Safety rules must be associated with an explicit policy version.

Missing, malformed, unavailable, or failed policy evaluation must never default to `ALLOW`.

## 7. Action Semantics

- `ALLOW`: normal governed pipeline may proceed.
- `ALLOW_WITH_WARNING`: proceed only with warning preserved.
- `ASK_CLARIFICATION`: terminate current execution; new information requires fresh evaluation.
- `REDIRECT`: terminate unsafe route; reformulated route requires fresh evaluation.
- `ESCALATE`: terminate automated normal delivery; do not claim human review completion.
- `REJECT`: hard termination; no Retrieval, Generation, or automatic delivery.
- `EMERGENCY`: highest-precedence termination of the normal pipeline.

## 8. Failure Semantics

Fail closed for:

- missing/unavailable policy;
- malformed policy;
- decision evaluation failure;
- unavailable required safety context;
- invalid decision construction;
- escalation mechanism failure.

No failure may silently become `ALLOW`.

## 9. Cross-Boundary Contract

Only `ALLOW` and `ALLOW_WITH_WARNING` may enter the normal downstream runtime path.

The Safety layer must not construct or mutate:

```text
RTEP
GenerationContext
CandidateResponse
ValidationResult
```

A downstream `VALID` result can never override a restrictive Safety Decision.

`EMPTY_EVIDENCE` behavior cannot be used to bypass Safety Enforcement.

## 10. Required Tests

### Model tests
- controlled vocabulary;
- required fields;
- immutability;
- invalid input rejection.

### Enforcement tests
- LOW/MODERATE/HIGH/EMERGENCY;
- authorization/default-deny;
- prohibited/restricted requests;
- warning preservation;
- clarification termination;
- redirect re-evaluation;
- escalation termination;
- rejection termination;
- emergency precedence.

### Failure tests
- missing/malformed policy;
- evaluation exception;
- invalid decision;
- escalation failure;
- all failure paths prove non-ALLOW behavior.

### Traceability tests
Verify `request_id`, `decision_id`, `policy_version`, `risk_class`, `reason_code`, and `timestamp`.

### Cross-boundary tests
Prove:

```text
REJECT → no Retrieval
ESCALATE → no Generation
ASK_CLARIFICATION → no normal pipeline
REDIRECT → fresh evaluation required
ALLOW → normal path may proceed
```

### Static architecture tests
Prove no repository/filesystem access, retrieval invocation, RTEP assembly, runtime integration, LLM/provider invocation, generation, validation, vector search, network access, or clinical reasoning.

## 11. E2E Acceptance Scenarios

1. Safe educational request → `ALLOW` → existing pipeline may proceed.
2. Warning-required request → `ALLOW_WITH_WARNING` → warning preserved.
3. Prohibited request → `REJECT` → no downstream generation/delivery.
4. Emergency request → emergency disposition → normal pipeline terminated.
5. Escalation-required request → `ESCALATE` → no automatic clinical answer.
6. Ambiguous request → `ASK_CLARIFICATION` → current execution terminated.
7. Safety-engine failure → fail closed → never `ALLOW`.

## 12. Regression Gate

Run:

```bash
uv sync --extra dev
uv run pytest 08_Development/implementation/tests -v
```

Acceptance requires all Task #002–#008 tests plus all Task #009 tests to pass, with no unrelated regression and `git diff --check` clean.

## 13. Scope Prohibitions

Do not implement:

- clinical diagnosis;
- treatment recommendation/prescription;
- autonomous clinical decision-making;
- evidence retrieval;
- LLM safety adjudication;
- vector search;
- external clinical-service integration;
- human escalation workflow implementation;
- production incident management;
- a new general runtime orchestration engine.

## 14. Technical Acceptance Criteria

Task #009 passes only when:

1. Safety models are immutable.
2. Six-action vocabulary is enforced.
3. Risk classes are enforced.
4. Decision is deterministic.
5. Policy version is traceable.
6. Emergency/reject/escalation semantics pass.
7. Clarification/redirect semantics pass.
8. Fail-closed behavior passes.
9. No downstream safety bypass exists.
10. Cross-boundary and E2E tests pass.
11. Full Task #002–#008 regression passes.
12. Static architecture checks pass.
13. `git diff --check` passes.
14. Scope verification passes.
15. No governance/clinical knowledge materials are modified.

## 15. Git / Handoff Boundary

```text
Implementation Specification
→ implementation
→ review
→ patch
→ controlled VS Code apply
→ tests
→ commit
→ push
→ remote verification
→ closeout
```

Do not claim commit/push/remote verification before evidence is provided.

## 16. Closeout

After technical acceptance:

- formally close Task #009;
- record implementation and acceptance evidence;
- synchronize the two Phase 5 governance/IR Markdown records together at **v11.0**, preserving the established v6.0 format;
- record Task #009 B1–B4 decisions and implementation evidence;
- reassess Phase 5 closure.

Do not create a further task unless acceptance identifies a genuine architecture-level gap preventing Phase 5 acceptance.

## 17. Final Scope Guard

Task #009 is intended to be the final missing runtime Safety Enforcement boundary required for Phase 5 closure. Enhancements or future features are not sufficient grounds for another task.

**Implementation handoff: READY.**

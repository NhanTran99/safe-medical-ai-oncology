# Controlled Evaluation Runtime (CER)

## Scope

Thin orchestration only:

`Safety → Retrieval → RTEP Assembly → Runtime Integration → Generation → Validation`

The package composes existing locked boundaries and does not redefine their
contracts or behavior.

## Provider boundary

The LLM provider remains injected through the existing `LLMAdapter`. CER does
not select a vendor/model, create credentials, or commit secrets.

Therefore a CER run using a test/deterministic adapter is **development /
controlled evaluation plumbing evidence**, not clinical validation.

## Required caller inputs

The caller must provide:
- explicit request and retrieval navigation;
- explicit safety input;
- explicit RTEP assembly metadata;
- positional evidence provenance;
- validation policy version;
- an injected `LLMAdapter`.

CER never invents provenance or safety decisions.

## Safety

Only explicit `ALLOW` or `ALLOW_WITH_WARNING` proceeds to generation.
All other safety actions stop the run.

## Boundary

`CEROutcome.COMPLETED` means the orchestration completed and the downstream
Validation boundary returned `VALID`. It does **not** mean clinical validation,
clinical safety approval, deployment authorization, or regulatory authorization.

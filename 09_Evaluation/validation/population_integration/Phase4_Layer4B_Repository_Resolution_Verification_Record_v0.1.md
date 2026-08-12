# Phase 4 Layer 4B --- Repository Resolution Verification Record v0.1

Date: 2026-08-12

## Scope

Layer 4B verifies deterministic resolution of every governed Population
Package from the integration manifest to the immutable Phase-3
repository snapshot.

## Immutable repository baseline

Repository: `NhanTran99/safe-medical-ai-oncology`

Branch: `main`

Immutable Phase-3 commit: `a838a9423fc3d14c46f8cd176bafed3b691e65c0`

Baseline snapshot: `PHASE3_BASELINE_a838a94.zip`

Baseline snapshot SHA-256:
`93f9e4ed6aa69eea54c9c1e76b1577500d658a8f403597a7778ba7a9b6a099e7`

## Deterministic repository checks

-   Manifest PP rows: **239 / 239 --- PASS**
-   Unique PP IDs: **239 / 239 --- PASS**
-   Repository PP folders in immutable snapshot: **239 / 239 --- PASS**
-   Manifest repository paths resolved to snapshot folders: **239 / 239
    --- PASS**
-   Missing manifest paths: **0**
-   Unexpected repository PP folders: **0**

Canonical artifact counts in the immutable snapshot:

-   `01_CKO.md`: **239 / 239 --- PASS**
-   `02_KNOWLEDGE_PASSPORT.md`: **239 / 239 --- PASS**
-   `03_PRIMARY_EVIDENCE_PACKAGE.md`: **239 / 239 --- PASS**
-   `04_QA_REPORT.md`: **239 / 239 --- PASS**

Total: **956 / 956 canonical Gold artifacts --- PASS**

## Conclusion

Every manifest Population Package resolves to exactly one repository
folder in the immutable Phase-3 snapshot, and every PP folder contains
all four canonical Gold artifacts.

**Layer 4B --- Repository Resolution: PASS**

This record is a formal Phase-4 evidence artifact. It does not modify
the immutable Phase-3 baseline.

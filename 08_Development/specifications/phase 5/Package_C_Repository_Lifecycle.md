# Phase 5 Governance — Package C Decision Record
Status: LOCKED — approved by Project Coordinator
Purpose: Consolidated record of Package C decisions.

## Locked Decisions

### C1 — Git release/tag and baseline
- Do not create Git tags/releases automatically.
- Verified commit is the authoritative repository milestone.
- A tag/release is optional and requires explicit approved release intent.
- Exact tag/version naming syntax is deferred.
- Controlled closeout remains:
  inventory → classify → canonical paths → explicit git add → staged diff review → commit → verify → push → remote verify.
- Never use `git add .` for controlled closeout.

### C2 — Archive and historical materials
- CONTROLLED = authoritative current project state.
- ARCHIVE = historical material preserved for traceability, not active authority.
- WORKING = evolving local material.
- Generic `archive/` is not automatically pushed.
- Controlled Git archive is reserved for historical material needing repository-level reproducibility/audit/governance traceability.
- `LONG_TERM_ROADMAP v2.0` = CONTROLLED.
- `Closing note Phase 2` = CONTROLLED historical governance record.
- Historical Layer 3 v0.1 = ARCHIVE; newer authoritative verification evidence remains active.
- Copyright/source materials remain subject to redistribution restrictions.

### C3 — Accidental artifact and Population Wave
- `tatus` = accidental artifact; disposition is DELETE in a separate controlled cleanup operation.
- Population Wave is a controlled set of verified/integrated PP units, not a Git tag and not a replacement for PP/asset versioning.
- Distinguish:
  - PP/Knowledge Asset version
  - Population Wave version
  - Git commit
- Wave lifecycle:
  population completed → Gold/QA verification → integration verification → wave manifest finalized → controlled commit → remote verification → optional tag/release.
- Wave manifest should contain Wave ID/version, PP IDs, PP/asset versions, verification state, repository baseline commit, integration evidence reference, and optional release/tag.
- PP correction must not overwrite historical wave state; it may create a new controlled wave/amendment state.
- Exact numbering/tag syntax remains deferred.

## Deferred
- Exact Git tag naming.
- Exact semantic version numbering.
- Exact Population Wave manifest schema.

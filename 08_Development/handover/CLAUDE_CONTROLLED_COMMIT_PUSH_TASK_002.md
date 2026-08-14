# CLAUDE CONTROLLED COMMIT & PUSH — TASK #002

You are executing a controlled Git closeout for the already-completed
Task #002 Implementation Scaffolding.

## 1. OBJECTIVE

Add the approved Task #002 scaffolding hygiene rule, stage only the
authorized Task #002 files, review the staged diff, commit, push to the
existing working branch, and verify the remote result.

This is NOT an implementation task.

## 2. CURRENT BRANCH

Work only on the existing Claude working branch:

`claude/project-understanding-vukdbc`

Do not create a new branch.

Do not create a tag or release.

## 3. FIRST ACTION — REPOSITORY CHECK

Before changing anything, run and report:

```bash
git branch --show-current
git status --short
git rev-parse HEAD
git rev-parse origin/main
```

If the current branch is not `claude/project-understanding-vukdbc`, STOP.

If unexpected modified/untracked files exist outside the approved
Task #002 candidate set, STOP and report them.

## 4. CREATE .gitignore

Create repository-root `.gitignore` containing, at minimum:

```gitignore
.venv/
.pytest_cache/
__pycache__/
*.py[cod]
*.egg-info/
.env
```

Keep `.env.example` trackable.

Do not use `.gitignore` to hide controlled source/project materials.

## 5. APPROVED COMMIT SCOPE

Only these paths may enter the commit:

```text
.gitignore
pyproject.toml
uv.lock
.env.example
08_Development/**
```

Before staging, inspect the candidate set.

Do NOT use:

```bash
git add .
git add -A
```

Use explicit path-based staging only.

## 6. STAGED DIFF REVIEW

After staging:

```bash
git status --short
git diff --cached --stat
git diff --cached --check
git diff --cached
```

Verify every staged file belongs to the approved scope.

If any unauthorized path is staged, STOP and remove it from staging.

## 7. TESTS

Before committing, run the approved baseline test command:

```bash
uv sync --extra dev
uv run pytest 08_Development/implementation/tests -v
```

Expected result: baseline tests PASS.

If tests fail, STOP. Do not commit a failing baseline.

## 8. COMMIT

Only after the staged diff and tests pass, create ONE commit.

Suggested commit message:

`feat(phase5): establish implementation scaffolding`

Do not amend existing commits.

## 9. PUSH

Push ONLY the existing working branch:

```bash
git push origin claude/project-understanding-vukdbc
```

Do not push to main.

Do not create a pull request.

Do not create a tag/release.

## 10. REMOTE VERIFICATION

After push, verify:

```bash
git status --short
git rev-parse HEAD
git ls-remote origin refs/heads/claude/project-understanding-vukdbc
```

The local HEAD and remote branch SHA must match.

## 11. FINAL REPORT

Return:

# Controlled Commit & Push Report — Task #002

1. Branch
2. Pre-closeout state
3. `.gitignore` created
4. Files staged
5. Staged diff review result
6. Tests and exact result
7. Commit SHA
8. Push result
9. Remote verification result
10. Final working-tree state
11. Any warnings/issues

Explicitly confirm:

- no unauthorized paths committed;
- no main branch modified;
- no tag/release created.

## 12. STOP

After remote verification, STOP.

Do not begin Task #003 or any retrieval/runtime implementation.

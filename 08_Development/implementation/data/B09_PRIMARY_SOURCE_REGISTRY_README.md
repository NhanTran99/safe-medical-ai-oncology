# B09 Primary Source Registry (Phase 6 Stage 2 Track 3, B09)

## What this is

`b09_primary_source_registry.json` is the single authoritative source for
the Chat UI's evidence-transparency "Sources" display (B09). It is a
**display-only lookup**:

```text
Approved population_id (PP-NNNN)
  -> human-readable Primary Source Set string, copied verbatim
```

It is consumed by `api/main.py` (`_load_primary_source_registry()`) and
rendered by `api/chat_ui.py`, which shows the resolved source labels next
to a substantive answer, or an honest "Evidence information unavailable"
fallback when no mapping exists.

## Where the data came from

Every entry is copied byte-for-byte from the governed Population Registry
workbook's `Population Registry2` sheet, `Primary Source Set` column
(239/239 PP coverage, verified against `evaluation_case_manifest_projection.json`
to cover exactly the same 239 `population_id` values `EvaluationCaseResolver`
can ever resolve — no gaps, no extras). No value in this file was expanded,
normalized, inferred, or invented: where the Registry recorded an
abbreviation (e.g. `"NCCN"`) or an inconsistent trailing character, that is
exactly what is stored here.

## What this is NOT

- **not** a second PP/case authority — the `population_id` used to look up
  an entry is always the one already resolved by `EvaluationCaseResolver`
  for the case actually executed; this file only maps that identity to a
  display string, never re-derives or re-validates it;
- **not** a source-extraction/parsing layer over PP markdown — the values
  here come only from the structured Registry column, never from parsing
  `01_CKO.md` / `02_KNOWLEDGE_PASSPORT.md` / `03_PRIMARY_EVIDENCE_PACKAGE.md`
  prose;
- **not** a claim-level citation engine — one Primary Source Set string per
  PP, not a per-sentence/per-claim citation;
- **not** a runtime-inferred mapping — there is no LLM classification, no
  heuristic, no fuzzy matching; the mapping is a static, explicit,
  version-controlled list, read as-is by the runtime.

## How a raw value becomes displayed source labels

Each Registry value is a single string joining organization/guideline
abbreviations with the Registry's own `" + "` separator (e.g.
`"NCI + ACS + NCCN Patient + ESMO"`). `api/main.py`'s
`_format_primary_source_set()` splits on that exact separator and trims
surrounding whitespace only — it never expands an abbreviation to a full
guideline name and never removes/rewrites any other character (a small
number of Registry values end in a stray `.`; that character is preserved
in the resulting label rather than silently corrected, since correcting it
would be a rewrite of governed data).

## Missing-mapping behavior

If a `population_id` genuinely used for generation (i.e. the RTEP had real,
non-empty evidence) has no entry in this file, the Chat UI shows
`Evidence information unavailable` — never a fabricated source, never the
PP ID itself. See `_resolve_primary_source_set()` in `api/main.py` for the
exact three-state contract (`None` / `[]` / populated list) this file
feeds into.

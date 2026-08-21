#!/usr/bin/env python3
"""B10 dev-time campaign execution runner — Coverage / Reproducibility Gap.

Thin orchestration only: for each externally supplied `case_id`, calls the
existing `campaign.execute_case()` (the same governed path `/cer/evaluate`
and `/chat/query` already use) and durably records the result via the
existing `campaign.record_execution_result()`. This script implements NO
CER, retrieval, evidence, provider, or validation logic of its own.

It makes NO decision about which case_ids to run, how many, or whether
the resulting set is representative or exhaustive of the governed 239-PP
population -- that selection is always supplied externally by the caller
(`--case-id` / `--case-ids-file`), never defaulted, sampled, or invented
here. There is no hard-coded output location either: `--output` is a
required argument.

Follows the same dev-time script convention as
`scripts/generate_evaluation_case_manifest_projection.py`: this script is
never imported by the FastAPI runtime, and requires no new CLI framework
or service (plain `argparse`, plain synchronous execution).

A per-case execution failure (safety block, retrieval failure, generation
failure, unresolved case_id, etc.) is recorded like any other outcome and
does NOT stop the run -- `execute_case()` already returns a typed result
unconditionally, including for failures, and this script preserves that
behavior for every supplied case_id (it never skips or discards one).

Provider selection is entirely the existing, unmodified behavior of
`execute_case()`/`_select_provider()`: the deterministic provider unless
the caller's own environment has `SMA_OPENAI_API_KEY` configured. This
script adds no provider-selection flag or logic of its own.

Usage:
    uv run python 08_Development/implementation/scripts/run_campaign_execution.py \\
        --case-id EC-0001 --case-id EC-0002 \\
        --output path/chosen/by/caller.jsonl

    uv run python 08_Development/implementation/scripts/run_campaign_execution.py \\
        --case-ids-file path/to/case_ids.txt \\
        --output path/chosen/by/caller.jsonl \\
        --request-text "What is the governed evidence for this case?"
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# This script (unlike generate_evaluation_case_manifest_projection.py) needs
# to import the runtime package itself (`safe_medical_ai.campaign`), which is
# not installed into the environment as a package -- the existing test suite
# reaches it via pytest's own `pythonpath` ini setting (see pyproject.toml),
# a pytest-only mechanism. A plain script has no such mechanism, so the
# adjacent `src/` directory is added to `sys.path` explicitly here.
_HERE = Path(__file__).resolve().parent
_SRC = _HERE.parent / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from safe_medical_ai.campaign import (  # noqa: E402
    execute_case,
    read_execution_results,
    record_execution_result,
    summarize_campaign_coverage,
)

#: Fixed, non-clinical placeholder used only when neither `--request-text`
#: nor a resolvable governed `controlled_question` (see
#: `_load_controlled_questions`) is available for a supplied case_id.
#: Mirrors the existing test suite's own convention of plain non-clinical
#: placeholder request text (e.g. "test question", "irrelevant question"
#: in tests/test_campaign.py and tests/test_track2_case_execution.py) --
#: never an invented clinical question.
_DEFAULT_REQUEST_TEXT = "Controlled coverage execution."

_DEFAULT_PROJECTION_PATH = (
    _HERE.parent / "data" / "evaluation_case_manifest_projection.json"
)


def _load_controlled_questions(projection_path: Path) -> dict[str, str]:
    """Best-effort `case_id -> controlled_question` lookup.

    Reuses the exact same governed manifest projection
    `EvaluationCaseResolver` and the Chat UI's navigation catalog already
    read (`api/main.py`'s `_load_navigation_catalog()`) -- never a new or
    second source of question text. Returns `{}` if the projection cannot
    be read; that is not fatal here, since `--request-text` or the fixed
    non-clinical default still let every supplied case_id be executed,
    and a genuinely unresolvable case_id still fails closed inside
    `execute_case()` itself, exactly as it does everywhere else in this
    system.
    """
    try:
        raw = json.loads(projection_path.read_text(encoding="utf-8"))
    except Exception:
        return {}
    return {
        entry["case_id"]: entry["controlled_question"]
        for entry in raw.get("cases", [])
        if entry.get("case_id") and entry.get("controlled_question")
    }


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "B10 dev-time campaign execution runner. Executes an "
            "externally supplied set of approved case_ids through the "
            "existing governed campaign.execute_case() path and durably "
            "records each result. Selects, samples, and invents nothing."
        )
    )
    parser.add_argument(
        "--case-id",
        action="append",
        default=[],
        metavar="EC-NNNN",
        help="One approved case_id to execute. Repeatable.",
    )
    parser.add_argument(
        "--case-ids-file",
        type=Path,
        default=None,
        help=(
            "Path to a text file with one case_id per line "
            "(blank lines and lines starting with '#' are ignored)."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help=(
            "Required. Where durable JSON Lines execution results are "
            "appended (campaign.record_execution_result()). Never "
            "defaulted to any location -- the caller always supplies it."
        ),
    )
    parser.add_argument(
        "--request-text",
        type=str,
        default=None,
        help=(
            "Request text used for every supplied case_id. If omitted, "
            "each case_id's own existing governed controlled_question "
            "(from evaluation_case_manifest_projection.json) is used when "
            "resolvable, otherwise a fixed non-clinical placeholder text "
            "is used."
        ),
    )
    parser.add_argument(
        "--projection-path",
        type=Path,
        default=None,
        help=(
            "Override path to evaluation_case_manifest_projection.json "
            "(used only to look up each case_id's controlled_question "
            "when --request-text is not supplied). Defaults to the "
            "existing repository-standard location."
        ),
    )
    return parser.parse_args(argv)


def _collect_case_ids(args: argparse.Namespace) -> list[str]:
    """Return exactly the case_ids the caller supplied -- no selection,
    no sampling, no default set. Order and duplicates from the caller's
    own input are preserved unchanged."""
    case_ids: list[str] = list(args.case_id)
    if args.case_ids_file is not None:
        for line in args.case_ids_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            case_ids.append(line)
    return case_ids


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    case_ids = _collect_case_ids(args)

    if not case_ids:
        print(
            "No case_id supplied. This runner never selects, samples, "
            "defaults, or invents a case set -- pass one or more "
            "--case-id, and/or --case-ids-file.",
            file=sys.stderr,
        )
        return 2

    controlled_questions: dict[str, str] = (
        {}
        if args.request_text is not None
        else _load_controlled_questions(args.projection_path or _DEFAULT_PROJECTION_PATH)
    )

    for case_id in case_ids:
        request_text = (
            args.request_text
            or controlled_questions.get(case_id)
            or _DEFAULT_REQUEST_TEXT
        )
        result = execute_case(case_id, request_text)
        captured = record_execution_result(result, args.output)
        print(
            f"{case_id}: "
            f"case_resolution={captured.case_resolution_outcome.value} "
            f"cer_outcome={captured.cer_outcome.value if captured.cer_outcome else None} "
            f"capture={captured.evidence_capture_status.value if captured.evidence_capture_status else None}"
        )

    summary = summarize_campaign_coverage(read_execution_results(args.output))
    print("\n--- Coverage summary (this --output file only) ---")
    print(f"total_execution_records={summary.total_execution_records}")
    print(f"distinct_case_ids={summary.distinct_case_ids}")
    print(f"distinct_population_ids={summary.distinct_population_ids}")
    print(f"case_resolution_outcome_counts={summary.case_resolution_outcome_counts}")
    print(f"cer_outcome_counts={summary.cer_outcome_counts}")
    print(f"validation_outcome_counts={summary.validation_outcome_counts}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

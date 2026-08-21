"""Tests for the B10 dev-time campaign execution runner script
(scripts/run_campaign_execution.py).

Uses only the deterministic provider (the existing test-suite default,
see conftest.py) -- no test in this file makes a real external API call.
The script is not part of the importable `safe_medical_ai` package (it is
a plain dev-time script, following the same convention as
`scripts/generate_evaluation_case_manifest_projection.py`), so it is
loaded here by file path via `importlib`, exactly the standard technique
for testing a script that is not itself an installed module.
"""

import importlib.util
import json
from pathlib import Path

import pytest

_SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "scripts" / "run_campaign_execution.py"
)


def _load_script_module():
    spec = importlib.util.spec_from_file_location("run_campaign_execution", _SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


runner = _load_script_module()


# --- case_id set is always externally supplied, never invented -------------


def test_collect_case_ids_returns_exactly_the_supplied_case_ids():
    args = runner._parse_args(["--case-id", "EC-0001", "--case-id", "EC-0003", "--output", "out.jsonl"])

    assert runner._collect_case_ids(args) == ["EC-0001", "EC-0003"]


def test_collect_case_ids_reads_a_case_ids_file(tmp_path):
    case_ids_file = tmp_path / "case_ids.txt"
    case_ids_file.write_text("EC-0001\n# a comment\n\nEC-0003\n", encoding="utf-8")
    args = runner._parse_args(
        ["--case-ids-file", str(case_ids_file), "--output", "out.jsonl"]
    )

    assert runner._collect_case_ids(args) == ["EC-0001", "EC-0003"]


def test_collect_case_ids_combines_flag_and_file_supplied_ids(tmp_path):
    case_ids_file = tmp_path / "case_ids.txt"
    case_ids_file.write_text("EC-0003\n", encoding="utf-8")
    args = runner._parse_args(
        ["--case-id", "EC-0001", "--case-ids-file", str(case_ids_file), "--output", "out.jsonl"]
    )

    assert runner._collect_case_ids(args) == ["EC-0001", "EC-0003"]


def test_main_requires_the_output_argument():
    with pytest.raises(SystemExit):
        runner._parse_args(["--case-id", "EC-0001"])


def test_main_returns_nonzero_and_writes_nothing_when_no_case_id_supplied(tmp_path):
    output_path = tmp_path / "results.jsonl"

    exit_code = runner.main(["--output", str(output_path)])

    assert exit_code != 0
    assert not output_path.exists()


# --- executes each supplied case through the existing governed harness -----


def test_main_executes_every_supplied_case_id_through_the_existing_harness(tmp_path):
    output_path = tmp_path / "results.jsonl"

    exit_code = runner.main(
        ["--case-id", "EC-0001", "--case-id", "EC-0003", "--output", str(output_path)]
    )

    assert exit_code == 0
    lines = output_path.read_text(encoding="utf-8").strip().splitlines()
    recorded_case_ids = {json.loads(line)["case_id"] for line in lines}
    assert recorded_case_ids == {"EC-0001", "EC-0003"}


def test_main_preserves_a_per_case_failure_without_aborting_the_run(tmp_path):
    # A normal execution failure for one supplied case_id (unresolved) must
    # not stop the run or cause the well-formed case_id to be skipped --
    # execute_case()'s own unconditional-return behavior is preserved.
    output_path = tmp_path / "results.jsonl"

    exit_code = runner.main(
        ["--case-id", "EC-9999", "--case-id", "EC-0001", "--output", str(output_path)]
    )

    assert exit_code == 0
    lines = output_path.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2
    recorded = {json.loads(line)["case_id"]: json.loads(line) for line in lines}
    assert recorded["EC-9999"]["case_resolution_outcome"] == "UNKNOWN_CASE"
    assert recorded["EC-0001"]["case_resolution_outcome"] == "RESOLVED"


def test_main_honors_the_explicitly_supplied_output_path(tmp_path):
    custom_path = tmp_path / "a" / "nested" / "location.jsonl"

    exit_code = runner.main(["--case-id", "EC-0001", "--output", str(custom_path)])

    assert exit_code == 0
    assert custom_path.exists()


def test_main_uses_the_governed_controlled_question_by_default(tmp_path, monkeypatch):
    # No --request-text supplied: the runner must call execute_case() with
    # EC-0001's own existing governed controlled_question from the
    # manifest projection, never invent question text of its own. Spy on
    # execute_case() (as imported into the runner module) to capture the
    # exact request_text it was actually called with.
    output_path = tmp_path / "results.jsonl"
    projection = json.loads(runner._DEFAULT_PROJECTION_PATH.read_text(encoding="utf-8"))
    expected_question = next(
        entry["controlled_question"] for entry in projection["cases"] if entry["case_id"] == "EC-0001"
    )

    real_execute_case = runner.execute_case
    captured_request_text = {}

    def spy(case_id, request_text, **kwargs):
        captured_request_text[case_id] = request_text
        return real_execute_case(case_id, request_text, **kwargs)

    monkeypatch.setattr(runner, "execute_case", spy)

    runner.main(["--case-id", "EC-0001", "--output", str(output_path)])

    assert captured_request_text["EC-0001"] == expected_question


def test_main_honors_an_explicit_request_text_override(tmp_path):
    # B12: the override value must be real, on-topic text for EC-0001 --
    # a semantically meaningless placeholder is no longer sufficient once
    # the selected-PP request-relevance boundary exists. Using EC-0001's
    # own real controlled_question here still fully exercises the
    # override plumbing (--request-text bypassing the default
    # controlled_question lookup) since main() would otherwise look this
    # same value up itself when --request-text is omitted -- the override
    # is verified by the CLI argument path taken, not by the override
    # text differing in content from the default.
    output_path = tmp_path / "results.jsonl"

    exit_code = runner.main(
        [
            "--case-id",
            "EC-0001",
            "--output",
            str(output_path),
            "--request-text",
            "What is Cancer?",
        ]
    )

    assert exit_code == 0
    recorded = json.loads(output_path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert recorded["case_resolution_outcome"] == "RESOLVED"


# --- evidence_package_id / provider identity reach the durable record ------


def test_main_recorded_results_carry_evidence_package_id(tmp_path):
    output_path = tmp_path / "results.jsonl"

    runner.main(["--case-id", "EC-0001", "--output", str(output_path)])

    recorded = json.loads(output_path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert recorded["evidence_package_id"]


def test_main_recorded_results_carry_provider_identity(tmp_path):
    output_path = tmp_path / "results.jsonl"

    runner.main(["--case-id", "EC-0001", "--output", str(output_path)])

    recorded = json.loads(output_path.read_text(encoding="utf-8").strip().splitlines()[0])
    assert recorded["provider_name"] == "DeterministicLocalProvider"
    # The deterministic provider has no configured model -- never fabricated.
    assert recorded["provider_model"] is None


# --- coverage summary is printed over the recorded output ------------------


def test_main_prints_a_coverage_summary_reflecting_the_recorded_output(tmp_path, capsys):
    output_path = tmp_path / "results.jsonl"

    runner.main(["--case-id", "EC-0001", "--case-id", "EC-0003", "--output", str(output_path)])

    captured = capsys.readouterr()
    assert "total_execution_records=2" in captured.out
    assert "distinct_case_ids=2" in captured.out
    assert "distinct_population_ids=2" in captured.out

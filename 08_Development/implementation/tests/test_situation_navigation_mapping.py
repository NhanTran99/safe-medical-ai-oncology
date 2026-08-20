"""Tests for the B06 governed Situation navigation mapping artifact.

`data/b06_situation_navigation_mapping.json` is navigation metadata only
(see `data/B06_SITUATION_NAVIGATION_MAPPING_README.md`): it must never
become a second PP/case authority, must reference only `case_id`s that
already exist in the real 239-entry manifest projection
(`EvaluationCaseResolver`'s sole authority), and must carry no clinical
content of its own.
"""

import json
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parents[1] / "data"
_MAPPING_PATH = _DATA_DIR / "b06_situation_navigation_mapping.json"
_PROJECTION_PATH = _DATA_DIR / "evaluation_case_manifest_projection.json"

_LOCKED_SITUATION_LABELS = (
    "I was recently diagnosed",
    "I'm receiving treatment",
    "I'm preparing for surgery",
    "I'm concerned about recurrence",
    "I'm in follow-up",
)


def _load_mapping() -> dict:
    return json.loads(_MAPPING_PATH.read_text(encoding="utf-8"))


def _load_valid_case_ids() -> set[str]:
    projection = json.loads(_PROJECTION_PATH.read_text(encoding="utf-8"))
    return {c["case_id"] for c in projection["cases"]}


def test_mapping_artifact_exists_and_parses():
    mapping = _load_mapping()

    assert mapping["artifact_type"] == "B06_SITUATION_NAVIGATION_MAPPING"


def test_mapping_declares_a_content_grounded_review_methodology():
    # B06 correction pass: the artifact must document (as governance/audit
    # metadata, not clinical content) that mappings were reviewed against
    # actual governed PP content rather than pp_title alone.
    mapping = _load_mapping()

    assert "review_methodology" in mapping
    assert isinstance(mapping["review_methodology"], str)
    assert len(mapping["review_methodology"]) > 0


def test_mapping_declares_exactly_the_five_locked_situations():
    # B06 Test A: exactly the five approved Situations, no sixth, no
    # renaming/merging/splitting.
    mapping = _load_mapping()

    labels = tuple(s["label"] for s in mapping["situations"])
    assert labels == _LOCKED_SITUATION_LABELS

    situation_ids = [s["situation_id"] for s in mapping["situations"]]
    assert len(situation_ids) == 5
    assert len(set(situation_ids)) == 5


def test_every_mapping_references_a_valid_case_id():
    # B06 Test B / Test J: no invalid case_id, and -- critically -- the
    # mapping only ever *references* case_ids that already exist in the
    # real manifest projection. It never introduces one of its own, so it
    # cannot become a second PP/case authority.
    mapping = _load_mapping()
    valid_case_ids = _load_valid_case_ids()

    referenced = {m["case_id"] for m in mapping["mappings"]}
    assert referenced.issubset(valid_case_ids)
    assert len(referenced) > 0


def test_every_mapping_references_a_valid_situation_id():
    mapping = _load_mapping()
    valid_situation_ids = {s["situation_id"] for s in mapping["situations"]}

    for entry in mapping["mappings"]:
        assert entry["situation_id"] in valid_situation_ids


def test_mapping_entries_are_carried_from_bare_ids_only_no_second_authority():
    # B06 D06: the mapping is metadata that *references* PP/case identity,
    # never a place that redefines/duplicates it (no pp_title, no
    # controlled_question, no clinical content anywhere in this file).
    mapping = _load_mapping()

    for entry in mapping["mappings"]:
        assert set(entry.keys()) == {"situation_id", "case_id"}


def test_no_duplicate_mapping_entries():
    # B06 Test C support: many-to-many is fine, but the SAME
    # (situation_id, case_id) pair must not be listed twice.
    mapping = _load_mapping()

    pairs = [(m["situation_id"], m["case_id"]) for m in mapping["mappings"]]
    assert len(pairs) == len(set(pairs))


def test_mapping_uses_genuine_many_to_many_relationships():
    # B06 Test C / D01: at least one PP/Topic is mapped to more than one
    # Situation (many-to-many is actually exercised, not merely allowed).
    mapping = _load_mapping()

    case_id_situation_counts: dict[str, int] = {}
    for entry in mapping["mappings"]:
        case_id_situation_counts[entry["case_id"]] = (
            case_id_situation_counts.get(entry["case_id"], 0) + 1
        )

    assert any(count > 1 for count in case_id_situation_counts.values())


def test_mapping_does_not_force_full_239_coverage():
    # B06 D03/D07: coverage must never be forced to reach 239/239 -- an
    # unmapped PP is an expected, honest outcome, not a defect.
    mapping = _load_mapping()
    valid_case_ids = _load_valid_case_ids()

    referenced = {m["case_id"] for m in mapping["mappings"]}
    assert referenced != valid_case_ids
    assert len(referenced) < len(valid_case_ids)


def test_mapping_never_uses_the_unapproved_sixth_situation_as_a_catch_all():
    # B06 D03: the pre-B06 sixth Track 1C string must not appear anywhere
    # in this governed artifact.
    mapping = _load_mapping()

    labels = {s["label"] for s in mapping["situations"]}
    assert "I want to understand my cancer" not in labels


def test_relationship_and_pp_level_counts_are_internally_consistent():
    # Patch 0022 accounting-reconciliation guard: derive relationship-pair
    # count, unique PP count, and unique Situation count directly from the
    # artifact every time, rather than trusting a prose report's numbers.
    # This does not freeze any specific count (D07/D03: coverage is not a
    # target number) -- it only checks the counts are self-consistent with
    # each other, which is exactly the invariant a future accounting
    # narrative must also satisfy.
    mapping = _load_mapping()

    pairs = [(m["situation_id"], m["case_id"]) for m in mapping["mappings"]]
    total_pairs = len(pairs)
    unique_situations = {s for s, _ in pairs}
    unique_pp = {c for _, c in pairs}

    assert len(mapping["situations"]) == 5
    assert unique_situations.issubset({s["situation_id"] for s in mapping["situations"]})
    # Every mapped PP has at least one relationship pair, and a PP with
    # more than one Situation contributes more than one pair -- so the
    # pair count can never be smaller than the unique-PP count.
    assert total_pairs >= len(unique_pp)

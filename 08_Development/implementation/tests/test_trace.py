"""Baseline test: trace-ID foundation."""

from safe_medical_ai.trace import get_trace_id, new_trace_id, set_trace_id


def test_new_trace_id_is_unique():
    assert new_trace_id() != new_trace_id()


def test_set_and_get_trace_id():
    trace_id = set_trace_id("fixed-value")
    assert trace_id == "fixed-value"
    assert get_trace_id() == "fixed-value"


def test_set_trace_id_generates_when_absent():
    trace_id = set_trace_id()
    assert trace_id == get_trace_id()
    assert len(trace_id) > 0

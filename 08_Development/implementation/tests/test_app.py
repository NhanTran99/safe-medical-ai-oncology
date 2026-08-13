"""Baseline test: the FastAPI scaffold boots and serves a health check."""

from fastapi.testclient import TestClient

from safe_medical_ai.api.main import app


def test_health_endpoint_ok():
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert "x-trace-id" in response.headers


def test_health_endpoint_propagates_incoming_trace_id():
    client = TestClient(app)
    response = client.get("/health", headers={"x-trace-id": "test-trace-123"})

    assert response.headers["x-trace-id"] == "test-trace-123"

from fastapi.testclient import TestClient

from safe_medical_ai.api.main import app


client = TestClient(app)


def test_controlled_cer_endpoint_completes():
    # Track 2: the endpoint now takes an approved case_id (EC-0002 ->
    # PP-0002), not a client-supplied population_id.
    response = client.post(
        "/cer/evaluate",
        json={
            "request_text": "What is gastric cancer?",
            "case_id": "EC-0002",
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert body["outcome"] == "COMPLETED"
    assert body["safety"] == "ALLOW"
    assert body["retrieval"] == "FOUND"
    assert body["retrieval_results"] == 1
    assert body["assembly"] == "PASS"
    assert body["integration"] == "PASS"
    assert body["generation"] == "PASS"
    assert body["validation"] == "VALID"

    assert body["boundary"]["formal_validation"] == "NOT STARTED"
    assert body["boundary"]["execution_authorization"] == "NOT GRANTED"

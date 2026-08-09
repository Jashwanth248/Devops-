from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/healthz").status_code == 200


def test_ready():
    assert client.get("/readyz").json()["ready"] is True


def test_metrics():
    assert "http_requests_total" in client.get("/metrics").text

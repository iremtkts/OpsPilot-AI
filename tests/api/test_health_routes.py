from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_returns_service_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readiness_returns_application_check() -> None:
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.json()["status"] == "ready"
    assert response.json()["checks"]["application"] == "ok"


def test_version_returns_current_version() -> None:
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["version"] == "0.1.0"

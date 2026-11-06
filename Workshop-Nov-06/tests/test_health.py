import psycopg
from fastapi.testclient import TestClient

import app


class FakeConnection:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def execute(self, query):
        assert query == "SELECT 1"
        return self

    def fetchone(self):
        return (1,)


def test_health_success(monkeypatch):
    monkeypatch.setenv("POSTGRES_PASSWORD", "test_only")

    def fake_connect(**kwargs):
        assert kwargs["password"] == "test_only"
        return FakeConnection()

    monkeypatch.setattr(psycopg, "connect", fake_connect)

    client = TestClient(app.app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": "v2",
        "database": "ok",
    }


def test_health_database_failure(monkeypatch):
    monkeypatch.setenv("POSTGRES_PASSWORD", "test_only")

    def fake_connect(**kwargs):
        raise psycopg.OperationalError("Connection failed")

    monkeypatch.setattr(psycopg, "connect", fake_connect)

    client = TestClient(app.app)
    response = client.get("/health")

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Database unavailable"
    }

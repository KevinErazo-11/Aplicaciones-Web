import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_health_check(client):
    response = client.get(reverse("health-check"))

    assert response.status_code == 200

    data = response.json()
    assert data["status"] == "ok"
    assert data["database"] == "ok"
    assert data["service"] == "md-marketing-api"
    assert data["version"] == "1.0.0"
    assert "timestamp" in data

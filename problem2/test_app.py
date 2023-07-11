import pytest
import json

from app import app
from app import weather_data
# defining fixture


@pytest.fixture(autouse=True)
def client():
    with app.test_client() as client:
        yield client

# tests


def test_read(client):
    print(weather_data)
    initial_length = len(weather_data)
    response = client.get("/")
    # parsing as json
    data = response.get_json()
    assert response.status_code == 200
    assert initial_length == len(data["msg"])


def test_create(client):
    initial_length = len(weather_data)
    payload = {"Mumbai": {
        "temperature": 10,
        "weather": "Rainy"}
    }
    response = client.post("/", json=payload)
    print(weather_data)
    assert response.status_code == 200
    assert len(weather_data) == initial_length+1


def test_update(client):
    payload = {"Sydney": {
        "temperature": 10,
        "weather": "Rainy"}
    }
    response = client.put("/Austin", json=payload)
    data = response.get_json()
    assert response.status_code == 200
    assert "msg" in data
    assert data["msg"] == "City Updated Successfully"


def test_delete(client):
    initial_length = len(weather_data)
    response = client.delete("/Sydney")
    assert response.status_code == 200
    assert len(weather_data) == initial_length-1

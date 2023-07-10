import pytest
import json
from app import app
def test_app():
    with app.test_client() as client:
        response = client.get("/")
        # getting response in json format
        data = response.get_json()

        # checking if msg key exists in json response
        assert "msg" in data

        # if key exists then checking the value matches of key or not
        assert data["msg"] == "Hi"

def test_weather():
    with app.test_client() as client:
        response = client.get("/weather/Austin")

        data = response.get_json()
        # print(data)
        assert "msg" in data
        assert data["msg"]["temperature"] == 32 and data["msg"]["weather"] == "Hot"
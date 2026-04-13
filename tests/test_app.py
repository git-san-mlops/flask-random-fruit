import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_random_fruit():
    client = app.test_client()
    response = client.get("/random-fruit")
    assert response.status_code == 200
    assert "fruit" in response.get_json()
import pytest
from src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home():
    response = client.get("/")

    assert response.status_code==200
    assert response.json()== {"msg": "Hello World!"}
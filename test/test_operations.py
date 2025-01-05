import pytest
import json
from src.app import lambda_handler
# from src.app import app
# from fastapi.testclient import TestClient

# client = TestClient(app)

def test_home():
    response = lambda_handler(None, None)

    print(response)
    assert response["statusCode"]==200
    assert json.loads(response["body"])["message"]== "Hello World!"
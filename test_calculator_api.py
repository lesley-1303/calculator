# import pytest
# from fastapi.testclient import TestClient
# from api import app

# @pytest.fixture
# def client():
#     return TestClient(app)

# def test_add(client):
#     response = client.post("/add", json={"a": 1, "b": 2})
#     assert response.status_code == 200
#     assert response.json().get("result") == 3
    
# def test_subtract(client):
#     response = client.post("/subtract", json={"a": 5, "b": 3})
#     assert response.status_code == 200
#     assert response.json().get("result") == 2
    
# def test_multiply(client):
#     response = client.post("/multiply", json={"a": 4, "b": 5})
#     assert response.status_code == 200
#     assert response.json().get("result") == 20
    
# def test_divide(client):
#     response = client.post("/divide", json={"a": 15, "b": 3})
#     assert response.status_code == 200
#     assert response.json().get("result") == 5
    
# def test_divide_by_zero(client):
#     response = client.post("/divide", json={"a": 1, "b": 0})
#     assert response.status_code == 400
#     assert response.json().get("detail") == "Cannot divide by zero."
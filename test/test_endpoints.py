from fastapi import status
from fastapi.testclient import TestClient

import utils
from main import app

client = TestClient(app)

user_endpoint = "/users"
name = utils.get_random_name()
password = utils.get_random_password()
token = "d5db3efc8f838dc63c3b523f6b09c5c167a2e4928899e93c6bfbe14f7247951c"


def test_create_user():
    payload = {
        "name": name,
        "password": password,
        "age": 31
    }
    response = client.post(user_endpoint, json=payload)
    response_json = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert response_json["name"] == name
    assert response_json["password"] == password
    response = client.post(user_endpoint, json=payload)
    assert response.status_code == status.HTTP_409_CONFLICT
    response = client.post(user_endpoint)
    response_json = response.json()
    assert response_json["name"] != ""
    assert response_json["password"] != ""


def test_find_user():
    response = client.get(f"{user_endpoint}?name=asbdt&password=YawXHpeb")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    response = client.get(f"{user_endpoint}?name={name}&password={password}")
    response_json = response.json()
    assert response_json["name"] == name
    response = client.get(f"{user_endpoint}?token={token}")
    response_json = response.json()
    assert response_json["name"] == "innocentHare9"

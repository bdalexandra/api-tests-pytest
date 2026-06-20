"""Тесты авторизации Reqres.in. Требует REQRES_API_KEY в .env."""
import requests
import pytest
import os

INVALID_KEY = "invalid_api_key_for_testing"


@pytest.mark.auth
def test_login_success(login_token):
    assert "Authorization" in login_token
    assert login_token["Authorization"].startswith("Bearer ")


@pytest.mark.auth
def test_login_wrong_api_key():
    headers = {"x-api-key": INVALID_KEY}
    response = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"},
        headers=headers,
    )
    assert response.status_code == 403
    assert "error" in response.json()


@pytest.mark.auth
def test_login_missing_password(api_key):
    response = requests.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in"},
        headers=api_key,
    )
    data = response.json()
    assert response.status_code == 400
    assert "token" not in data


@pytest.mark.auth
def test_get_user_by_id(api_key):
    response = requests.get("https://reqres.in/api/users/2", headers=api_key)
    data = response.json()
    assert response.status_code == 200
    assert data["data"]["id"] == 2
    assert "email" in data["data"]

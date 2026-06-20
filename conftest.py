import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_posts(base_url):              # фикстура, зависящая от другой фикстуры
    return f"{base_url}/posts"

@pytest.fixture
def test_users():
    return [
    {"name": "Alice", "age": 25},
    {"name": "Bob",   "age": 30},
    {"name": "Eve",   "age": 35}
]

@pytest.fixture
def user_names(test_users):
    return [user["name"] for user in test_users]

@pytest.fixture
def auth_headers():
    """Фикстура с заголовками авторизации"""
    token = "test-token-abc"
    return {"Authorization": f"Bearer {token}"}

@pytest.fixture
def auth_session(auth_headers):
    """Фикстура с готовым клиентом (необязательно, но удобно)"""
    return {"headers": auth_headers}

@pytest.fixture
def api_key():
    headers = {"x-api-key": os.getenv("REQRES_API_KEY")}
    return headers

@pytest.fixture
def login_token(api_key):
    user_eve_holt = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post("https://reqres.in/api/login", json=user_eve_holt, headers=api_key)
    data = response.json()
    # print("STATUS:", response.status_code)
    # print("BODY:", data)
    token = data["token"]
    return {"Authorization": f"Bearer {token}"}

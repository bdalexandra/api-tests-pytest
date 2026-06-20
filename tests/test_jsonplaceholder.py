"""Тесты REST API JSONPlaceholder — CRUD-операции, не требует API-ключа."""
import requests
import pytest


@pytest.mark.api
def test_get_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10


@pytest.mark.api
def test_get_user_structure(base_url):
    """Проверка структуры ответа: name, email, address."""
    response = requests.get(f"{base_url}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert "name" in data
    assert "email" in data
    assert "address" in data


@pytest.mark.api
def test_get_posts(api_posts):
    response = requests.get(api_posts)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 100


@pytest.mark.api
def test_get_post_by_id(api_posts):
    response = requests.get(f"{api_posts}/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert "userId" in data


@pytest.mark.api
def test_get_nonexistent_post(api_posts):
    response = requests.get(f"{api_posts}/99999")
    assert response.status_code == 404


@pytest.mark.api
def test_get_comments(api_posts):
    response = requests.get(f"{api_posts}/1/comments")
    data = response.json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert all("email" in item for item in data)


@pytest.mark.api
def test_create_post(api_posts):
    new_post = {
        "title": "My test post",
        "body": "This is a test body",
        "userId": 1,
    }
    response = requests.post(api_posts, json=new_post)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == new_post["title"]
    assert data["id"] == 101


@pytest.mark.api
def test_create_todo(base_url):
    payload = {"title": "pytest lesson", "completed": False}
    response = requests.post(f"{base_url}/todos", json=payload)
    data = response.json()
    assert response.status_code == 201
    assert data["title"] == payload["title"]
    assert data["completed"] == payload["completed"]
    assert data["id"] == 201


@pytest.mark.api
def test_update_post(api_posts):
    payload = {"title": "Updated title"}
    response = requests.put(f"{api_posts}/1", json=payload)
    data = response.json()
    assert response.status_code == 200
    assert data["title"] == "Updated title"


@pytest.mark.api
def test_delete_post(api_posts):
    response = requests.delete(f"{api_posts}/1")
    assert response.status_code == 200
    # В реальном API здесь была бы проверка:
    # assert requests.get(f"{api_posts}/1").status_code == 404

import pytest

def users_count(user_names):
    count = len(user_names)
    print(f"Всего {count} пользователя")
    return count

def test_users_count(user_names):
    assert users_count(user_names) == 3

def test_user_names(user_names):
    assert user_names[0] == "Alice"
    assert user_names[1] == "Bob"
    assert user_names[2] == "Eve"

def test_alice_age(test_users):
    assert test_users[0]["age"] == 25

# Гибкая функция 
# def get_age_by_name(test_users, name):
#     for user in test_users:
#         if user["name"] == name:
#             return user["age"]
#     return None  

def test_all_adults(test_users):
    for user in test_users:
        assert user["age"] >= 18
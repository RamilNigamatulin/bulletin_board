import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_payload():
    return {
        "first_name": "Test_first_name",
        "last_name": "Test_last_name",
        "email": "test@example.ru",
        "password": "test_password",
    }


@pytest.fixture
def advertisements_payload():
    return {
        "title": "Test_title",
        "price": 123,
    }


@pytest.fixture
def new_token(user_payload, client):
    client.post("/users/register/", user_payload)
    login_payload = {
        "email": user_payload["email"],
        "password": user_payload["password"],
    }
    response = client.post("/users/token/", login_payload)
    return response

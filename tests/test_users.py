import pytest
from rest_framework import status

from tests.pytest_fixture import client, new_token, user_payload


@pytest.mark.django_db
def test_register_user(user_payload, client):
    response = client.post("/users/register/", user_payload)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data["first_name"] == user_payload["first_name"]
    assert data["last_name"] == user_payload["last_name"]
    assert data["email"] == user_payload["email"]


@pytest.mark.django_db
def test_reset_password(user_payload, client):
    client.post("/users/register/", user_payload)
    reset_payload = {"email": user_payload["email"]}
    response = client.post("/users/reset_password/", reset_payload)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_obtain_token(user_payload, new_token):
    data = new_token.data

    assert new_token.status_code == status.HTTP_200_OK
    assert "access" in data
    assert "refresh" in data


@pytest.mark.django_db
def test_refresh_token(user_payload, client, new_token):
    refresh_token = new_token.data["refresh"]
    refresh_payload = {
        "refresh": refresh_token,
    }
    response = client.post("/users/token/refresh/", refresh_payload)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert "access" in data

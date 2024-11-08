import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from advertisements.models import Advertisement
from tests.pytest_fixture import advertisements_payload, client, new_token, user_payload

User = get_user_model()


@pytest.mark.django_db
def test_list_advertisements(client):
    response = client.get("/advertisements/")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_advertisements(advertisements_payload, new_token, client):
    access_token = new_token.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = client.post("/advertisements/create/", advertisements_payload)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data["title"] == advertisements_payload["title"]
    assert data["price"] == advertisements_payload["price"]


@pytest.mark.django_db
def test_retrieve_advertisement(advertisements_payload, new_token, client):
    access_token = new_token.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    advertisement = Advertisement.objects.create(**advertisements_payload)
    response = client.get(f"/advertisements/{advertisement.id}/")
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data["title"] == advertisements_payload["title"]
    assert data["price"] == advertisements_payload["price"]


@pytest.mark.django_db
def test_update_advertisement(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])

    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    update_title = "update_test_title"
    update_price = 456

    response = client.put(
        f"/advertisements/{advertisement.id}/update/",
        {"title": update_title, "price": update_price},
    )
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data["title"] == update_title
    assert data["price"] == update_price


@pytest.mark.django_db
def test_delete_advertisement(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])

    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    response = client.delete(f"/advertisements/{advertisement.id}/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT

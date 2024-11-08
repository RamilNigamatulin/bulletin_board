import pytest
from django.contrib.auth import get_user_model
from rest_framework import status

from advertisements.models import Advertisement, Review
from tests.pytest_fixture import advertisements_payload, client, new_token, user_payload

User = get_user_model()


@pytest.mark.django_db
def test_list_review(new_token, client):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    response = client.get("/reviews/")

    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_create_review(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])

    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    review_payload = {"text": "Тест отзыв", "advertisement": advertisement.id}
    response = client.post("/reviews/create/", data=review_payload)
    data = response.data

    assert response.status_code == status.HTTP_201_CREATED
    assert data["text"] == review_payload["text"]
    assert data["advertisement"] == review_payload["advertisement"]


@pytest.mark.django_db
def test_retrieve_review(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])
    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    review_payload = {"text": "Тест отзыв", "advertisement": advertisement}
    review = Review.objects.create(**review_payload)

    response = client.get(f"/reviews/{review.id}/")
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data["text"] == review_payload["text"]
    assert data["advertisement"] == advertisement.id


@pytest.mark.django_db
def test_update_review(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])
    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    review_payload = {"text": "Тест отзыв", "advertisement": advertisement}
    review = Review.objects.create(author=user, **review_payload)
    update_text = "Смена тест отзыва"

    response = client.put(
        f"/reviews/{review.id}/update/",
        {"text": update_text, "advertisement": advertisement.id},
    )
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert data["text"] == update_text


@pytest.mark.django_db
def test_delete_review(advertisements_payload, new_token, client, user_payload):
    access_token = new_token.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    user = User.objects.get(email=user_payload["email"])
    advertisement = Advertisement.objects.create(author=user, **advertisements_payload)
    review_payload = {"text": "Тест отзыв", "advertisement": advertisement}
    review = Review.objects.create(author=user, **review_payload)

    response = client.delete(f"/reviews/{review.id}/delete/")

    assert response.status_code == status.HTTP_204_NO_CONTENT

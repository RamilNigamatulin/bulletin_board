from django.urls import path

from advertisements.apps import AdvertisementsConfig
from advertisements.views import (AdvertisementCreateAPIView,
                                  AdvertisementDestroyAPIView,
                                  AdvertisementListAPIView,
                                  AdvertisementRetrieveAPIView,
                                  AdvertisementUpdateAPIView, ReviewListAPIView, ReviewRetrieveAPIView,
                                  ReviewUpdateAPIView, ReviewDestroyAPIView, ReviewCreateAPIView,
                                  ReviewListAdvertisementAPIView)

app_name = AdvertisementsConfig.name

urlpatterns = [
    path("advertisements/", AdvertisementListAPIView.as_view(), name="list_advertisements",),
    path( "advertisements/<int:pk>/", AdvertisementRetrieveAPIView.as_view(), name="retrieve_advertisement",),
    path( "advertisements/<int:pk>/update/", AdvertisementUpdateAPIView.as_view(), name="update_advertisement",),
    path( "advertisements/<int:pk>/delete/", AdvertisementDestroyAPIView.as_view(), name="delete_advertisement",),
    path( "advertisements/create/", AdvertisementCreateAPIView.as_view(), name="create_advertisement",),

    path("reviews/", ReviewListAPIView.as_view(), name="list_reviews",),
    path("reviews/<int:pk>/", ReviewRetrieveAPIView.as_view(), name="retrieve_review",),
    path("reviews/<int:pk>/update/", ReviewUpdateAPIView.as_view(), name="update_review",),
    path("reviews/<int:pk>/delete/", ReviewDestroyAPIView.as_view(), name="delete_review",),
    path("reviews/create/", ReviewCreateAPIView.as_view(), name="create_review",),
    path("reviews/advertisement/<int:advertisement_id>/", ReviewListAdvertisementAPIView.as_view(), name="list_reviews_by_advertisement",),
]
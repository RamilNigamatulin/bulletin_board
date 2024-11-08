from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny

from advertisements.models import Advertisement, Review
from advertisements.paginators import AdvertisementPaginator
from advertisements.permissions import isAuthorOrSuperuser
from advertisements.serializers import (
    AdvertisementDetailSerializer,
    AdvertisementSerializer,
    ReviewSerializer,
)


class AdvertisementCreateAPIView(CreateAPIView):
    """Создаем новое объявление."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        """Привязываем автора к объявлению."""
        advertisement = serializer.save()
        advertisement.author = self.request.user
        advertisement.save()


class AdvertisementListAPIView(ListAPIView):
    """Выводим список всех объявлений."""

    queryset = Advertisement.objects.all().order_by("-created_at")
    serializer_class = AdvertisementSerializer
    filterset_fields = ("title",)
    pagination_class = AdvertisementPaginator
    permission_classes = (AllowAny,)


class AdvertisementUpdateAPIView(UpdateAPIView):
    """Редактируем объявление."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (isAuthorOrSuperuser,)


class AdvertisementRetrieveAPIView(RetrieveAPIView):
    """Выводим одно объявление."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementDestroyAPIView(DestroyAPIView):
    """Удаляем объявление."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewListAPIView(ListAPIView):
    """Выодим список отзывов с фильтрацией по дате создания."""

    queryset = Review.objects.all().order_by("-created_at")
    serializer_class = ReviewSerializer
    pagination_class = AdvertisementPaginator


class ReviewDestroyAPIView(DestroyAPIView):
    """Удаляем отзыв."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewUpdateAPIView(UpdateAPIView):
    """Редактируем отзыв."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewCreateAPIView(CreateAPIView):
    """Создаем новый отзыв."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """Привязываем автора к отзыву."""
        review = serializer.save()
        review.author = self.request.user
        review.save()


class ReviewRetrieveAPIView(RetrieveAPIView):
    """Выводим один отзыв."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListAdvertisementAPIView(ListAPIView):
    """Выводим все отзывы выбранного объявления."""

    serializer_class = ReviewSerializer
    pagination_class = AdvertisementPaginator

    def get_queryset(self):
        advertisement_id = self.kwargs.get("advertisement_id")
        return Review.objects.filter(advertisement=advertisement_id).order_by(
            "-created_at"
        )

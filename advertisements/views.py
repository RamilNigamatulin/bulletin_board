from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny

from advertisements.models import Advertisement, Review
from advertisements.paginators import AdvertisementPaginator
from advertisements.permissions import isAuthorOrSuperuser
from advertisements.serializers import AdvertisementSerializer, ReviewSerializer, AdvertisementDetailSerializer


class AdvertisementCreateAPIView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def perform_create(self, serializer):
        """ Привязываем автора к объявлению."""
        advertisement = serializer.save()
        advertisement.author = self.request.user
        advertisement.save()


class AdvertisementListAPIView(ListAPIView):
    queryset = Advertisement.objects.all().order_by('-created_at')
    serializer_class = AdvertisementSerializer
    filterset_fields = ('title',)
    pagination_class = AdvertisementPaginator
    permission_classes = (AllowAny,)


class AdvertisementUpdateAPIView(UpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (isAuthorOrSuperuser,)


class AdvertisementRetrieveAPIView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementDetailSerializer


class AdvertisementDestroyAPIView(DestroyAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    pagination_class = AdvertisementPaginator


class ReviewDestroyAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewUpdateAPIView(UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (isAuthorOrSuperuser,)


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        """ Привязываем автора к отзыву."""
        review = serializer.save()
        review.author = self.request.user
        review.save()


class ReviewRetrieveAPIView(RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewListAdvertisementAPIView(ListAPIView):
    """Выводит все отзывы выбранного объявления."""
    serializer_class = ReviewSerializer
    pagination_class = AdvertisementPaginator

    def get_queryset(self):
        advertisement_id = self.kwargs.get('advertisement_id')
        return Review.objects.filter(advertisement=advertisement_id).order_by('-created_at')

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from advertisements.models import Advertisement, Review


class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementDetailSerializer(ModelSerializer):
    """Добавляет новую строку в сериализатор для подсчета количества отзывов."""
    count_review = SerializerMethodField()

    def get_count_review(self, advertisement):
        return Review.objects.filter(advertisement=advertisement.id).count()

    class Meta:
        model = Advertisement
        fields = ("title", "price", "description", "author", "created_at", "count_review",)


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

from django.contrib import admin

from advertisements.models import Advertisement, Review


@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "author",
        "created_at",
    )
    list_filter = (
        "id",
        "title",
        "author",
    )


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "author",
        "created_at",
        "advertisement",
    )
    list_filter = (
        "id",
        "text",
        "author",
        "advertisement",
    )

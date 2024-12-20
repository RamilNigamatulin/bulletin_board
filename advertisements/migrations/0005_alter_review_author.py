# Generated by Django 4.2 on 2024-10-23 04:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("advertisements", "0004_review_advertisement"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="author",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор отзыва",
            ),
        ),
    ]

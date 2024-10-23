from django.db import models

from users.models import User


class Advertisement(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Название товара",
        help_text="Введите название товара",
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Введите цену товара",
    )
    description = models.TextField(
        verbose_name="Описание товара",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name="автор объявления",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания объявления",
    )
    image = models.ImageField(
        verbose_name="Изображение объявления",
        help_text="Загрузите изображение объявления",
        upload_to="photo/advertisements/",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(
        verbose_name="Текст отзыва",
        help_text="Введите текст отзыва",
    )
    author = models.ForeignKey(
        User,
        verbose_name="Автор отзыва",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания отзыва",
    )
    advertisement = models.ForeignKey(
        Advertisement,
        verbose_name="Объявление",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.text[:50]

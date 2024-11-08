from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None

    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя пользователя",
        help_text="Введите имя пользователя",
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия пользователя",
        help_text="Введите фамилию пользователя",
        blank=True,
        null=True,
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        unique=True,
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        help_text="Введите адрес электронной почты",
        unique=True,
    )
    image = models.ImageField(
        verbose_name="Изображение профиля",
        help_text="Загрузите изображение профиля",
        upload_to="photo/users/",
        blank=True,
        null=True,
    )
    user_role = models.CharField(
        max_length=50,
        verbose_name="Роль пользователя",
        choices=(
            ("ADMIN", "Администратор"),
            ("USER", "Пользователь"),
        ),
        blank=True,
        null=True,
    )
    token = models.CharField(
        max_length=50,
        verbose_name="Токен для восстановления пароля",
        blank=True,
        null=True,
    )
    uid = models.UUIDField(
        verbose_name="UID для восстановления пароля",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

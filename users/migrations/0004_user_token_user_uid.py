# Generated by Django 4.2 on 2024-10-28 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="token",
            field=models.CharField(
                blank=True,
                max_length=50,
                null=True,
                verbose_name="Токен для восстановления пароля",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="uid",
            field=models.UUIDField(
                blank=True, null=True, verbose_name="UID для восстановления пароля"
            ),
        ),
    ]
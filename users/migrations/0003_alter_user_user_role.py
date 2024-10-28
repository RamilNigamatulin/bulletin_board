# Generated by Django 4.2 on 2024-10-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_role",
            field=models.CharField(
                blank=True,
                choices=[("ADMIN", "Администратор"), ("USER", "Пользователь")],
                max_length=50,
                null=True,
                verbose_name="Роль пользователя",
            ),
        ),
    ]
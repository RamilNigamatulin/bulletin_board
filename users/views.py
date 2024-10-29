import secrets
import uuid

from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from config.settings import EMAIL_HOST_USER


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        if user.is_superuser:
            user.user_role = "ADMIN"
        else:
            user.user_role = "USER"
        user.save()

class PasswordResetAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        user = get_object_or_404(User, email=email)
        host = self.request.get_host()
        uid = uuid.uuid4()
        token = secrets.token_hex(16)
        user.token = token
        user.uid = uid
        user.save()
        url = f"http://{host}/users/reset_password/confirm/{user.uid}/{user.token}/"
        send_mail(
            "Восстановление пароля",
            f"Привет! Для восстановления пароля перейдите по ссылкe: {url} и укажите новый пароль.",
            EMAIL_HOST_USER,
            [user.email]
        )
        return Response({"message": "На Вашу электронную почту направлено сообщение для изменения пароля"})


class PasswordResetConfirmAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, uid, token):
        new_password_1 = request.data.get("new_password_1")
        new_password_2 = request.data.get("new_password_2")

        if new_password_1 != new_password_2:
            return Response({"Ошибка": "Пароли не совпадают"})

        user = get_object_or_404(User, uid=uid, token=token)
        user.set_password(new_password_1)
        user.uid = None  # Очищение поля uid
        user.token = None  # Очищение поля token
        user.save()
        return Response({"message": "Ваш пароль успешно изменен"})

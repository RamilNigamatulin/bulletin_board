import random
import string

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from config.settings import EMAIL_HOST_USER
from users.models import User
from users.serializers import UserSerializer, PasswordResetSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PasswordResetAPIView(APIView):
    pass
    #
    # def generate_random_password(self, length=9):
    #     characters = string.ascii_letters + string.digits + string.punctuation
    #     password = ''.join(random.choices(characters, k=length))
    #     return password
    #
    # def post(self, request):
    #     serializer = PasswordResetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         email = serializer.validated_data['email']
    #         try:
    #             user = User.objects.get(email=email)
    #         except User.DoesNotExist:
    #             return Response({"detail": "Пользователь с таким email не найден."}, status=status.HTTP_400_BAD_REQUEST)
    #
    #         new_password = self.generate_random_password()
    #         user.set_password(new_password)
    #         user.save()
    #
    #         send_mail(
    #             subject='Восстановление пароля',
    #             message=f'Привет, Ваш новый пароль для входа в Вашу учетную запись: {new_password}',
    #             from_email=EMAIL_HOST_USER,
    #             recipient_list=[user.email],
    #             fail_silently=False,
    #         )
    #
    #         return Response({"detail": "Новый пароль отправлен на вашу почту."}, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmAPIView(APIView):
    pass

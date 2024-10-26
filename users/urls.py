from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, PasswordResetAPIView, PasswordResetConfirmAPIView

app_name = UsersConfig.name


urlpatterns = [
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("reset_password/", PasswordResetAPIView.as_view(), name="password_reset"),
    path("reset_password/confirm/", PasswordResetConfirmAPIView.as_view(), name="password_reset_confirm"),
]

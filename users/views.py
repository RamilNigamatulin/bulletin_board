from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, PasswordResetSerializer


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
    pass



class PasswordResetConfirmAPIView(APIView):
    pass


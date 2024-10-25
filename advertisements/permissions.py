from rest_framework.permissions import BasePermission


class isAuthorOrSuperuser(BasePermission):
    """Проверяет, является ли автором объявления или администратором."""
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return request.user == view.get_object().author

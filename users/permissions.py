from rest_framework.permissions import BasePermission

from users.models import User


class UserDeletePermission(BasePermission):
    message = 'You can not delete another user!'

    def has_permission(self, request, view):
        user_id = view.kwargs.get('pk')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return True
        else:
            if request.user.id == user.id or request.user.role == User.Roles.ADMIN:
                return True
            return False

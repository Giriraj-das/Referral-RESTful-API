from rest_framework.permissions import BasePermission

from ref_codes.models import RefCode
from users.models import User


class RefCodeDeletePermission(BasePermission):
    message = 'Removing referral code for another user not allowed.'

    def has_permission(self, request, view):
        ref_code_id = view.kwargs.get('pk')
        try:
            ref_code_user = RefCode.objects.get(pk=ref_code_id)
        except RefCode.DoesNotExist:
            return True
        else:
            if request.user.id == ref_code_user.user_id or request.user.role == User.Roles.ADMIN:
                return True
            return False


class CodeByEmailPermission(BasePermission):
    message = 'You can not get code another user. Please use your email.'

    def has_permission(self, request, view):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return True
        else:
            if request.user.id == user.id or request.user.role == User.Roles.ADMIN:
                return True
            return False

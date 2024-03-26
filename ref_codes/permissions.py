from rest_framework.permissions import BasePermission

from ref_codes.models import RefCode


class RefCodeDeletePermission(BasePermission):
    message = 'Removing referral code for another user not allowed.'

    def has_permission(self, request, view):
        ref_code_id = request.parser_context['kwargs']['pk']
        ref_code_user = RefCode.objects.get(pk=ref_code_id).user_id

        if request.user.id == ref_code_user:
            return True
        return False

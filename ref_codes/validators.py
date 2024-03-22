import secrets
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


def check_datetime(value: datetime):
    if value < datetime.now() + timedelta(hours=1):
        raise ValidationError('Set the value at least 1 hour more than now.')


# def only_one_active_code(value: bool):
#     if :
#         raise ValidationError('Set different value')

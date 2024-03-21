from django.db import models
from django.contrib.auth.models import AbstractUser

from users.validators import check_datetime


class RefCode(models.Model):
    code = models.CharField(max_length=43)
    is_active = models.BooleanField()
    valid_to = models.DateTimeField(validators=[check_datetime])

    class Meta:
        verbose_name = "RefCode"
        verbose_name_plural = "RefCodes"

    def __str__(self):
        return self.code


class User(AbstractUser):

    class Roles(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        USER = 2, 'User'

    role = models.PositiveSmallIntegerField(choices=Roles.choices, default=Roles.USER)
    ref_codes = models.ManyToManyField(RefCode, default=[])

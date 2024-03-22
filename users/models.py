from django.db import models
from django.contrib.auth.models import AbstractUser

from ref_codes.models import RefCode


class User(AbstractUser):

    class Roles(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        USER = 2, 'User'

    role = models.PositiveSmallIntegerField(choices=Roles.choices, default=Roles.USER)
    ref_codes = models.ManyToManyField(RefCode, default=[])

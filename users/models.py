from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class Roles(models.IntegerChoices):
        ADMIN = 1, 'Admin'
        USER = 2, 'User'

    email = models.EmailField(unique=True)
    role = models.PositiveSmallIntegerField(choices=Roles.choices, default=Roles.USER)
    referer_user = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'role']

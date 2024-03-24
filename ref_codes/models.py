from django.db import models
from django.utils import timezone

from users.models import User


class RefCode(models.Model):
    code = models.CharField(max_length=8, blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    valid_to = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.is_active:
            RefCode.objects.filter(user=self.user).update(is_active=False)

        super().save(force_insert, force_update, using, update_fields)

    def is_valid(self):
        return self.valid_to >= timezone.now()

    class Meta:
        verbose_name = "RefCode"
        verbose_name_plural = "RefCodes"

    def __str__(self):
        return self.code

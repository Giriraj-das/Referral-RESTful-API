from django.db import models

from ref_codes.validators import check_datetime


class RefCode(models.Model):
    code = models.CharField(max_length=43)
    is_active = models.BooleanField()
    valid_to = models.DateTimeField(validators=[check_datetime])

    class Meta:
        verbose_name = "RefCode"
        verbose_name_plural = "RefCodes"

    def __str__(self):
        return self.code

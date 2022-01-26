from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class FacilityUser(models.Model):
    facility_name = models.CharField(verbose_name="施設名", max_length=200)
    address = models.CharField(verbose_name="施設住所", max_length=150)
    password = models.CharField(verbose_name="パスワード", max_length=32)

    def __str__(self):
        return self.facility_name
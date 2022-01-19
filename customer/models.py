from re import T
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="名前", max_length=200)
    age = models.PositiveSmallIntegerField(
        verbose_name='年齢',
        validators=[MinValueValidator(0), MaxValueValidator(150)],
    )
    gender = models.CharField(verbose_name='性別', max_length=3, blank=True)
    address = models.CharField(verbose_name="住所", max_length=150)
    carry_address = models.CharField(verbose_name="送り先住所", max_length=150)

    def __str__(self):
        return self.name


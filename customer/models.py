# import email
# from re import T
from tabnanny import verbose
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

GENDER_CHOICES = [
    ('女性', '女性'),
    ('男性', '男性'),
]

class User(models.Model):
    verbose
    name = models.CharField(verbose_name="名前", max_length=200)
    age = models.PositiveSmallIntegerField(
        verbose_name='年齢',
        validators=[MinValueValidator(0), MaxValueValidator(150)],
    )
    gender = models.CharField(verbose_name='性別', max_length=2,choices=GENDER_CHOICES)
    email = models.EmailField(verbose_name="メールアドレス")
    address = models.CharField(verbose_name="住所", max_length=150)
    carry_address = models.CharField(verbose_name="送り先住所", max_length=150)
    is_carryed = models.BooleanField(verbose_name="送迎中判定",default=False,)
    facility_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ('利用者')


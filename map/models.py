from django.db import models

# Create your models here.
#施設モデル
class Facility(models.Model):
    facility_name = models.CharField(max_length=200)#施設名
    password = models.CharField(max_length=200)#パスワード
    address = models.CharField(max_length=255)#住所

    class Meta:
        verbose_name_plural = 'Facility'
    
    def __str__(self):
        return self.name

#引受人モデル
# class Underwriter(models.Model):
#     username = models.CharField(max_length=200)#氏名
#     password = models.CharField(max_length=255)#パスワード
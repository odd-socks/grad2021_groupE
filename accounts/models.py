from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #拡張ユーザーモデル
    pass

    class Meta:
        verbose_name_plural = 'CustomUser'
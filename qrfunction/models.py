from django.db import models
from django.forms import DateField, EmailField, TimeField, DateTimeField, EmailField
# from customer.models import *
from customer.models import User
# Create your models here.

class qrfunction(models.Model):
    class Meta:
        verbose_name_plural = 'qrfunction'

class CarryLog(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name="メールアドレス")

    def __str__(self):
        return self.email 
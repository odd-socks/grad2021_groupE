from django.db import models
# from customer.models import *
from customer.models import User
# Create your models here.

class qrfunction(models.Model):
    class Meta:
        verbose_name_plural = 'qrfunction'

    # def __str__(self):
    #     return self.name
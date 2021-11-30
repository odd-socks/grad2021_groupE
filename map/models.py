from accounts.models import CustomUser
from django.db import models
# Create your models here.
class Facility(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 20)
    address = models.CharField(max_length = 150)

    class Meta:
        verbose_name_plural = 'Facility'
    
    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 150)
    facility = models.ForeignKey(Facility, to_field = 'id', on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'User'
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 150)
    facility = models.ForeignKey(Facility, to_field = 'id', on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = 'User'
    
    def __str__(self):
        return self.name
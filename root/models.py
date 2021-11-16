from accounts.models import CustomUser
from django.db import models
# Create your models here.
class Root(models.Model):
    name = models.ForeignKey(CustomUser, on_delete = models.PROTECT)
    address = models.CharField(max_length = 100)
    lat = models.FloatField()
    lon = models.FloatField()

    class Meta:
        verbose_name_plural = 'Root'
    
    def __str__(self):
        return self.address
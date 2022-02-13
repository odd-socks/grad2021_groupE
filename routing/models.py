from django.db import models
from routing.models import *


class Routing(models.Model):
    name        = models.CharField(max_length=255)
    route       = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    waypoints   = models.CharField(max_length=255)
    facility_id = models.IntegerField()
    user_id     = models.ForeignKey("customer.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Routing'
    
    def __str__(self):
        return self.name
from django.db import models



class Routing(models.Model):
    name        = models.CharField(max_length=255)
    route       = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    waypoints   = models.CharField(max_length=255)
    facility_id = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Routing'
    
    def __str__(self):
        return self.name
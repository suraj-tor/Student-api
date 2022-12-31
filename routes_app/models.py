from django.db import models
from vehicle_app.models import *
from driver_app.models import *

# Create your models here.
class RoutesModel(models.Model):
    route_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    from_place = models.CharField(max_length=100)
    to_place = models.CharField(max_length=100)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE, related_name="route_bus")
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="route_driver")
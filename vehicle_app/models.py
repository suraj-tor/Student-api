from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    seats = models.IntegerField(default=30)
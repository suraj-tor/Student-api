from django.db import models
from routes_app.models import *

# Create your models here.
class StudentModel(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    division = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)
    bus_stop = models.CharField(max_length=100)
    route_id = models.ForeignKey(RoutesModel, on_delete=models.CASCADE, related_name="student_route")
    # vehicle_id = models.ForeignKey(Bus, on_delete=models.CASCADE)


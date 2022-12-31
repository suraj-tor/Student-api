from django.db import models
from routes_app.models import *

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.IntegerField()
    division = models.CharField(max_length=10)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)
    bus_stop = models.CharField(max_length=100)
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE, related_name="student_route")
    
    def __str__(self) -> str:
        return f"{self.student_id} -- {self.name} -- {self.grade} -- {self.division} -- {self.roll_no} -- {self.address} -- {self.bus_stop} -- {self.route_id}"

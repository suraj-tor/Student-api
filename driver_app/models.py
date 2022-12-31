from django.db import models

# Create your models here.
class Driver(models.Model):
    driver_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name}"
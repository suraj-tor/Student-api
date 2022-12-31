from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
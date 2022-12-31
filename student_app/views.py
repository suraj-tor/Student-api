from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentSerializers

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
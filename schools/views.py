from django.shortcuts import render
from rest_framework import viewsets
from .models import School, Student
from django.shortcuts import get_object_or_404
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.decorators import action

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

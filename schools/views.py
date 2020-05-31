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
    
    def get_queryset(self):
        school_id = self.kwargs.get('school_pk', None)
        if school_id:
            return Student.objects.filter(school = school_id)
        return super(StudentViewSet, self).get_queryset()
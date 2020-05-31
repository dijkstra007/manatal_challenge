from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from rest_framework import viewsets
from .models import School, Student
from django.shortcuts import get_object_or_404
from .serializers import SchoolSerializer, StudentSerializer
from rest_framework.decorators import action
from faker import Faker
import random

# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.all()
        school_id = self.kwargs.get('school_pk', None)

        if school_id:
            queryset = Student.objects.filter(school = school_id)
        first_name = self.request.query_params.get('first_name', None)

        if first_name:
            queryset=queryset.filter(first_name__contains=first_name)

        last_name = self.request.query_params.get('last_name', None)
        if last_name:
            queryset=queryset.filter(last_name__contains=last_name)

        address = self.request.query_params.get('address', None)
        if address:
            queryset=queryset.filter(address__contains=address)

        order_by_age = self.request.query_params.get('order_by_age', None)
        if order_by_age:
            order_sign = '' if order_by_age == 'asc' else '-'
            queryset = queryset.order_by(order_sign + 'age')

        return queryset

def generate_fake_student(request):
    fake = Faker()

    full_name = fake.name()
    first_name, last_name = full_name.split(' ')

    age = random.randint(10, 100)

    n_schools = School.objects.count()
    index = random.randint(0, n_schools - 1)
    school = School.objects.all()[index]

    address = fake.address()

    fake_student = Student(first_name = first_name, last_name = last_name , age = age, school = school, address = address)
    fake_student.save()
    print('-------------------------------------')
    print(first_name, last_name, age, school, address)
    print('-------------------------------------')
    return HttpResponse("studetns named %s is generated in database." % full_name)



# name = models.CharField(max_length=20)
#     max_student = models.IntegerField(default=0)
#     address = models.TextField(blank=True)

def generate_fake_school(request):
    fake = Faker()

    name = fake.company()

    max_student = random.randint(5, 10)

    address = fake.address()

    fake_school = School(name = name, max_student = max_student , address = address)
    fake_school.save()
    print('-------------------------------------')
    print(name, max_student, address)
    print('-------------------------------------')
    return HttpResponse("school named %s is generated in database" % name)
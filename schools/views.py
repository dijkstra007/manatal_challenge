from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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
    items_per_page = 3

    def get_queryset(self):
        queryset_list = School.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset_list=queryset_list.filter(name__contains=name)

        min_capacity = self.request.query_params.get('min_capacity', None)
        if min_capacity:
            min_capacity = int(min_capacity)
            queryset_list=queryset_list.filter(max_student__gte=min_capacity)

        max_capacity = self.request.query_params.get('max_capacity', None)
        if max_capacity:
            max_capacity = int(max_capacity)
            queryset_list=queryset_list.filter(max_student__lte=max_capacity)

        address = self.request.query_params.get('address', None)
        if address:
            queryset_list=queryset_list.filter(address__contains=address)

        order_by_max_student = self.request.query_params.get('order_by_max_student', None)
        if order_by_max_student:
            order_sign = '' if order_by_max_student == 'asc' else '-'
            queryset_list = queryset_list.order_by(order_sign + 'max_student')

        paginator = Paginator(queryset_list, self.items_per_page)
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = queryset_list
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

        return queryset
    

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    items_per_page = 3
    def get_queryset(self):
        queryset_list = Student.objects.all()
        
        school_id = self.kwargs.get('school_pk', None)
        if school_id:
            queryset_list = Student.objects.filter(school = school_id)
        first_name = self.request.query_params.get('first_name', None)

        if first_name:
            queryset_list=queryset_list.filter(first_name__contains=first_name)

        last_name = self.request.query_params.get('last_name', None)
        if last_name:
            queryset_list=queryset_list.filter(last_name__contains=last_name)

        min_age = self.request.query_params.get('min_age', None)
        if min_age:
            min_age = int(min_age)
            queryset_list=queryset_list.filter(age__gte=min_age)

        max_age = self.request.query_params.get('max_age', None)
        if max_age:
            max_age = int(max_age)
            queryset_list=queryset_list.filter(age__lte=max_age)

        address = self.request.query_params.get('address', None)
        if address:
            queryset_list=queryset_list.filter(address__contains=address)

        order_by_age = self.request.query_params.get('order_by_age', None)
        if order_by_age:
            order_sign = '' if order_by_age == 'asc' else '-'
            queryset_list = queryset_list.order_by(order_sign + 'age')

        paginator = Paginator(queryset_list, self.items_per_page)
        page = self.request.GET.get('page')
        try:
            queryset = paginator.page(page)
        except PageNotAnInteger:
            queryset = queryset_list
        except EmptyPage:
            queryset = paginator.page(paginator.num_pages)

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
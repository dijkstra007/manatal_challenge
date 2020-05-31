from django.db import models
from django.utils import timezone
import uuid
import datetime

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.IntegerField(default=0)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    address = models.TextField(blank=True)


    def __str__(self):
        return self.first_name + self.last_name


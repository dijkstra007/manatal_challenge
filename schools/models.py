from django.db import models
from django.utils import timezone
import uuid
import datetime

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=20)
    max_student = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


    def __str__(self):
        return self.choice_text
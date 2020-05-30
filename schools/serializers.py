from .models import School, Student
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ("id", "name", "max_student")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ("student_id", "first_name", "last_name", "school")

    def create(self, validated_data):
        number_of_students = Student.objects.filter(
            school=validated_data.get('school')).count()
        limit_number_of_student = School.objects.get(
            pk=validated_data.get('school').id).max_student
        if number_of_students >= limit_number_of_student:
            raise serializers.ValidationError("this school is full. please join to another school.")
        return Student.objects.create(**validated_data)

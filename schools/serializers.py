from .models import School, Student
from rest_framework import serializers
from .utils import get_n_students_and_max_students

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ("id", "name", "max_student", "address")


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ("url", "student_id", "first_name", "last_name","age", "school", "address")

    def create(self, validated_data):
        n_students, max_students = get_n_students_and_max_students(validated_data.get('school'))
        if n_students >= max_students:
            raise serializers.ValidationError("this school is full. please join to another school.")
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        n_students, max_students = get_n_students_and_max_students(validated_data.get('school'))
        if n_students >= max_students:
            raise serializers.ValidationError("this school is full. please join to another school.")

        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.school = validated_data.get('school', instance.school)
        instance.save()

        return instance

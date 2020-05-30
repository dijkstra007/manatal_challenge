from .models import School, Student
from rest_framework import serializers


class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = ("id", "name", "max_student")


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ("url", "student_id", "first_name", "last_name", "school")

    def create(self, validated_data):
        number_of_students = Student.objects.filter(
            school=validated_data.get('school')).count()
        limit_number_of_student = School.objects.get(
            pk=validated_data.get('school').id).max_student
        if number_of_students >= limit_number_of_student:
            raise serializers.ValidationError("this school is full. please join to another school.")
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        number_of_students = Student.objects.filter(
            school=validated_data.get('school')).count()
        limit_number_of_student = School.objects.get(
            pk=validated_data.get('school').id).max_student
        if number_of_students >= limit_number_of_student:
            raise serializers.ValidationError("this school is full. please join to another school.")

        instance.student_id = validated_data.get('student_id', instance.student_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.school = validated_data.get('school', instance.school)
        instance.save()

        return instance

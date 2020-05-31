from .models import School


def get_n_students_and_max_students(school):
    n_students = Student.objects.filter(
        school=school).count()
    max_students = School.objects.get(
        pk=school.id).max_student

    return n_students, max_students
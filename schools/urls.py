from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers
from . import views
router = routers.DefaultRouter()
router.register('schools', views.SchoolViewSet)
router.register('students', views.StudentViewSet)

#/school/{school_id}/students
schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', views.StudentViewSet, basename='school-students')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(schools_router.urls)),
    path('gen_fake_student/', views.generate_fake_student, name='fake_student'),
    path('gen_fake_school/', views.generate_fake_school, name='fake_school'),
    
]

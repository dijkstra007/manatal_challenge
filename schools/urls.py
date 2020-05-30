from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('schools', views.SchoolViewSet)
router.register('students', views.StudentViewSet)
urlpatterns = [
    path('', include(router.urls))
]

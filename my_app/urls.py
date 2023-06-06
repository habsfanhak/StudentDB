from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('register/student/', views.registerStudent, name='registerStudent'),
    path('register/course/', views.registerCourse, name='registerCourse'),
    path('register/grade/', views.registerCourse, name='registerGrade'),
]
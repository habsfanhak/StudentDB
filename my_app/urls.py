from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('register/student/', views.registerStudent, name='registerStudent'),
    path('register/course/', views.registerCourse, name='registerCourse'),
    path('register/grade/', views.registerGrade, name='registerGrade'),
    path('students/', views.students, name='students'),
    path('students/<int:pk>', views.student, name='student')
]
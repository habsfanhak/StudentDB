from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Student(models.Model):
    student_number = models.AutoField(primary_key=True)
    email = models.CharField(max_length=264)
    student_name = models.CharField(max_length=264)
    def __str__(self):
        return str(str(self.student_number) + " - " + self.student_name)
    
class Course(models.Model):
    course_id = models.CharField(max_length=264, primary_key=True)
    course_name = models.CharField(max_length=264)
    course_description = models.CharField(max_length=264)
    def __str__(self):
        return str(self.course_id + " - " + self.course_name)
    
class Grade(models.Model):
    grade_id = models.AutoField(primary_key=True)
    student_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    result = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
from django.db import models

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
        return str(str(self.course_id) + " - " + self.course_description)
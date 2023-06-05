from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=264)
    def __str__(self):
        return str(str(self.student_number) + " - " + self.student_name)
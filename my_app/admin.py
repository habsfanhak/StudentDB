from django.contrib import admin

# Register your models here.
from django.contrib import admin
from my_app.models import Student, Course

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "student_name", "email")
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "course_name", "course_description")
admin.site.register(Course, CourseAdmin)
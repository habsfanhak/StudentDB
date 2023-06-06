from django.contrib import admin

# Register your models here.
from django.contrib import admin
from my_app.models import Student, Course, Grade

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "student_name", "email")
admin.site.register(Student, StudentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_id", "course_name", "course_description")
admin.site.register(Course, CourseAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ("grade_id", "course_id", "student_number", "result")
admin.site.register(Grade, GradeAdmin)
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from my_app.models import Student

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "student_name")
admin.site.register(Student, StudentAdmin)
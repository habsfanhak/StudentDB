from django.shortcuts import render
from .form import StudentForm, CourseForm
from .models import Student, Course
from django.contrib import messages

# Create your views here.
def home(request):
    context={}
    return render(request, "home.html", context)

def registerStudent(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                email=form.cleaned_data['email'],
                student_name=form.cleaned_data['student_name']
            )
            student.save()
            messages.success(request, 'Student added.')

    return render(request, 'registerStudent.html', {"form": form})

def registerCourse(request):
    form = CourseForm()

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            course = Course(
                course_id=form.cleaned_data['course_id'],
                course_name=form.cleaned_data['course_name'],
                course_description=form.cleaned_data['course_description']
            )
            course.save()
            messages.success(request, 'Course added.')

    return render(request, 'registerCourse.html', {"form": form})
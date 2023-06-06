from django.shortcuts import render
from .form import StudentForm, CourseForm, GradeForm
from .models import Student, Course
from django.contrib import messages
from django.db import IntegrityError

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
            course_id = form.cleaned_data['course_id']
            course_name = form.cleaned_data['course_name']
            course_description = form.cleaned_data['course_description']

            try:
                Course.objects.create(
                    course_id=course_id,
                    course_name=course_name,
                    course_description=course_description
                )
                messages.success(request, 'Course added.')

            except IntegrityError:
                messages.error(request, f"A course with ID {course_id} already exists.")

    return render(request, 'registerCourse.html', {"form": form})

def registerGrade(request):
    form = GradeForm()

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course_id']
            student_number = form.cleaned_data['student_number']
            result = form.cleaned_data['result']


            Course.objects.create(
                course_id=course_id,
                student_number=student_number,
                result=result
            )
            messages.success(request, 'Course added.')

    return render(request, 'registerCourse.html', {"form": form})

from django.shortcuts import render, get_object_or_404
from .form import StudentForm, CourseForm, GradeForm
from .models import Student, Course, Grade
from django.contrib import messages
from django.db import IntegrityError
from django.views.generic import ListView

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


            Grade.objects.create(
                course_id=course_id,
                student_number=student_number,
                result=result
            )
            messages.success(request, 'Grade registered.')

    return render(request, 'registerGrade.html', {"form": form})

def students(request):
    data = Student.objects.all()
    context = {'data': data}

    return render(request, 'students.html', context)

def student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    grades = Grade.objects.filter(student_number=student)
    dynamic_width = 0
    gpa = 0
    for grade in grades:
        dynamic_width += grade.result
        if grade.result >= 80:
            gpa += 4
        elif grade.result >= 75:
            gpa += 3.5
        elif grade.result >= 70:
            gpa += 3
        elif grade.result >= 65:
            gpa += 2.5
        elif grade.result >= 60:
            gpa += 2
        elif grade.result >= 55:
            gpa += 1.5
        elif grade.result >= 50:
            gpa += 1
        
    
    if len(grades) > 0:
        dynamic_width/=len(grades)
        gpa/=len(grades)
    dynamic_width/=2

    if (gpa > 4):
        gpa = 4

    return render(request, 'student.html', {'student': student, 'grades': grades, 'dynamic_width' : dynamic_width, 'gpa' : gpa})
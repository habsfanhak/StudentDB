from django import forms
from .models import Student, Course, Grade
from django.core import validators

class StudentForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseForm(forms.Form):
    course_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class GradeForm(forms.Form):
    def validate_result(value):
        if not value.isdigit():
            raise validators.ValidationError('Enter a valid number.')
        elif int(value) > 100:
            raise validators.ValidationError('Number must not exceed 100.')
    student_number = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    course_id = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    result = forms.CharField(validators=[validate_result], widget=forms.TextInput(attrs={'class': 'form-control'}))


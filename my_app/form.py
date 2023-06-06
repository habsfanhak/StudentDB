from django import forms
from .models import Student, Course

class StudentForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseForm(forms.Form):
    course_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class GradeForm(forms.ModelForm):
    student_number = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    course_id = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    result = forms.NumberInput(attrs={'class': 'form-control'}),
from django import forms

class StudentForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    student_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class CourseForm(forms.Form):
    course_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    course_description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
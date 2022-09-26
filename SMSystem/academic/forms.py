from django import forms 
from .models import Student


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name', 'email', 'roll', 'classname']
    labels = {
      'name': 'Name', 
      'email': 'Email', 
      'roll': 'Roll', 
      'classname': 'Class ', 
    }
    widgets = {
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'roll': forms.NumberInput(attrs={'class': 'form-control'}),
      

    }
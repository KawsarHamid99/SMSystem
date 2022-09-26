from django import forms

from .models import Marks


class MarksForm(forms.ModelForm):
  class Meta:
    model = Marks
    fields = ['student_subject', 'subject_marks']
    labels = {
      'student_subject': 'Subject', 
      'subject_marks': 'Edit Marks', 
    
    }
    widgets = {
      'student_subject': forms.TextInput(attrs={'class': 'form-control'}),
      'subject_marks': forms.NumberInput(attrs={'class': 'form-control'}),
      

    }
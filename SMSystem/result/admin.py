from django.contrib import admin
from .models import Marks
# Register your models here.

@admin.register(Marks)
class marksAdmin(admin.ModelAdmin):
    list_display=["students_name","students_roll","student_email","students_class","student_subject",'student_subjectCode',"subject_marks","subject_grade"]
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','roll',"email","classname"]

@admin.register(ClassModel)
class ClassModelAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['name',"subject_code","written_by"]


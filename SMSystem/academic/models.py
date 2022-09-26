
from cgitb import text
import email
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.
class ClassModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=80)
    roll=models.IntegerField(unique=True,null=False)
    classname=models.ForeignKey(ClassModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '(' + str(self.roll) + ")"
    
class Subject(models.Model):
    name=models.CharField(max_length=70)
    subject_code=models.IntegerField()
    classname=models.ManyToManyField(ClassModel)
    def written_by(self):
        return ",".join([str(p) for p in self.classname.all()])

    def __str__(self):
        return self.name











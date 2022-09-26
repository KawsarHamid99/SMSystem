import re
from django.shortcuts import render
from .models import ClassModel,Student,Subject
from django.views.generic import View

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

from result.models import Marks


# Create your views here.
def home(request):
    data=ClassModel.objects.get(name="NINE")
    data2=ClassModel.objects.get(name="SIX")
    student=Student.objects.all()
    print("-------------------------------------------------------")
    print(data.subject_set.all())

    for stu in data.student_set.all():
        roll=0
        marks=Marks.objects.filter(students_roll=stu.roll)
        if marks is not None:
            print("hello")
        for sub in data.subject_set.all():
            pass
            #student_data,created=Marks.objects.get_or_create(students_name=stu.name,students_roll=stu.roll,student_email=stu.email,students_class=stu.classname,student_subject=sub.name,student_subjectCode=sub.subject_code,subject_marks=0,subject_grade='F')
            #Marks.objects.all().delete()
    return render(request,"academic/home.html",{"students":student})


def view_student(request,id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))



class view_studentClass(View):
    def get(self,request,id):
        student=Student.objects.get(pk=id)
        return HttpResponseRedirect(reverse('index'))




class addclass(View):
    def get(self,request):
        form = StudentForm()
        return render(request, 'academic/addStudents.html', {'form': StudentForm()})

    def post(self,request):
        form = StudentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_roll = form.cleaned_data['roll']
            new_classname = form.cleaned_data['classname']
            new_student = Student(
                name = new_name,
                email = new_email,
                roll = new_roll,
                classname = new_classname,
                )
            new_student.save()
            
            data=ClassModel.objects.get(name=new_classname)
            print(data.name)

            for sub in data.subject_set.all():
                student_data=Marks.objects.create(students_name=new_name,students_roll=new_roll,student_email=new_email,students_class=new_classname,student_subject=sub.name,student_subjectCode=sub.subject_code,subject_marks=0,subject_grade='F')


            return render(request, 'academic/addStudents.html', {'form': StudentForm(),'success': True})






class editClass(View):
    def get(self,request,id):
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'academic/updateStudentInfo.html', {'form': form})
    
    def post(self,request,id):
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'academic/updateStudentInfo.html', {'form': form,'success': True})


class DeleteClass(View):
    def post(self,request,id):
        student = Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect(reverse('home'))







#trash

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_email = form.cleaned_data['email']
            new_roll = form.cleaned_data['roll']
            new_classname = form.cleaned_data['classname']


            new_student = Student(
                name = new_name,
                email = new_email,
                roll = new_roll,
                classname = new_classname,
                )
            new_student.save()
            return render(request, 'academic/addStudents.html', {'form': StudentForm(),'success': True})
    else:
        form = StudentForm()
        return render(request, 'academic/addStudents.html', {'form': StudentForm()})



def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('home'))





def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'academic/updateStudentInfo.html', {'form': form,'success': True})
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'academic/updateStudentInfo.html', {'form': form})





    
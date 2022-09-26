from unicodedata import name
from django.shortcuts import render,HttpResponse
from .models import Marks
from django.db.models import Q 
from academic.models import Student
from .forms import MarksForm

# Create your views here.
def grade():
    Marks.objects.filter(subject_marks__gte=80).update(subject_grade="A+")
    Marks.objects.filter(subject_marks__gte=70,subject_marks__lte=80).update(subject_grade="A")
    Marks.objects.filter(subject_marks__gte=65,subject_marks__lte=70).update(subject_grade="A-")
    Marks.objects.filter(subject_marks__gte=50,subject_marks__lte=65).update(subject_grade="B")
    Marks.objects.filter(subject_marks__gte=40,subject_marks__lte=50).update(subject_grade="C")
    Marks.objects.filter(subject_marks__gte=33,subject_marks__lte=40).update(subject_grade="D")
    Marks.objects.filter(subject_marks__lte=33).update(subject_grade="F")


def result(request,id):
    print(id)

    data=Marks.objects.filter(students_roll=id) 
    info=Student.objects.get(roll=id)
    print("--------------------------------------------------")
    print(data)
    grade()
    sum=0

    # grade Claculation 

    length=len(data)
    GPA=""
    for i in data:
        if not i.subject_grade=='F':
            if i.subject_grade=="A+":
                sum=sum+5
            elif i.subject_grade=="A":
                sum=sum+4
            elif i.subject_grade=="A-":
                sum=sum+3.5
            elif i.subject_grade=="B":
                sum=sum+3
            elif i.subject_grade=="C":
                sum=sum+2
            elif i.subject_grade=="D":
                sum=sum+1
        else:
            GPA="F"
            sum=0
            break
    gpa= "{0:.2f}".format(sum/length)
    
    return render(request,"result/resultView.html",{'marks':data,'info':info,"gpa":gpa})






def edit(request, id,roll):
    if request.method == 'POST':
        student = Marks.objects.get(student_subjectCode=id,students_roll=roll)
        form = MarksForm(request.POST, instance=student)
        if form.is_valid():
            print(form.cleaned_data['subject_marks'])
            
            form.save()
            data=Marks.objects.filter(student_subjectCode=id,students_roll=roll)
            for i in data:
                print(data)
            grade()
            return render(request, 'result/updateResult.html', {'form': form,'success': True})
    else:
        student = Marks.objects.get(student_subjectCode=id,students_roll=roll)
        form = MarksForm(instance=student)
        return render(request, 'result/updateResult.html', {'form': form})



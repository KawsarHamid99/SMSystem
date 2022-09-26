from django.db import models

# Create your models here.
class Marks(models.Model):
    students_name=models.CharField(max_length=80)
    students_roll=models.IntegerField()
    student_email=models.EmailField()
    students_class=models.CharField(max_length=70)
    student_subject=models.CharField(max_length=70)
    student_subjectCode=models.IntegerField()
    subject_marks=models.FloatField()
    subject_grade=models.CharField(max_length=60)

    def __str__(self):
        return self.students_name

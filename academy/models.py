from django.conf import settings
from django.db import models
from django.utils import timezone


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)


class Lecturer(models.Model):
    lecturer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    course = models.CharField(max_length=150)
    student = models.ManyToManyField(Student)
    teacher = models.OneToOneField(Lecturer, on_delete=models.CASCADE)

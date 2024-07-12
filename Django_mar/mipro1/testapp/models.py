from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    class Meta:
        abstract = True
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher(ContactInfo):
    subject = models.CharField(max_length=30)
    salary = models.FloatField() 
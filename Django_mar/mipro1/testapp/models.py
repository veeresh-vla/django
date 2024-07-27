from django.db import models

# Create your models here.

#1.Abstract Base Class model inheritance:
#class ContactInfo(models.Model):
    #name = models.CharField(max_length=30)
    #email = models.EmailField()
    #address = models.CharField(max_length=30)
#   
#class Student(ContactInfo):
    #rollno = models.IntegerField()
    #marks = models.IntegerField()
#class Teacher(ContactInfo):
    #subject = models.CharField(max_length=30)
    #salary = models.FloatField() 


#2).Multi table inheritance:
#class ContactInfo1(models.Model):
    #name = models.CharField(max_length=30)
    #email = models.EmailField()
    #address = models.CharField(max_length=30)
#class Student1(ContactInfo1):
    #rollno=models.IntegerField()
    #marks=models.IntegerField()
#class Teacher1(ContactInfo1):
    #subject = models.CharField(max_length=30)
    #salary = models.FloatField()

#3).Multi level inheritance
#class Person(models.Model):
    #name = models.CharField(max_length=30)
    #age = models.IntegerField()
#class Employee(Person):
    #eno = models.IntegerField()
    #esal = models.FloatField()
#class Manager(Employee):
    #exp = models.IntegerField()
    #team_size = models.IntegerField()
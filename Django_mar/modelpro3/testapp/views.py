from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    student_list=Student.objects.all()
    #student_list=Student.objects.filter(marks__lt=5)
    #student_list = Student.objects.filter(name__startswith='A')
    #student_list = Student.objects.all().order_by('marks')#Ascending order of  marks
    #student_list = Student.objects.all().order_by('-marks')#Descending order
    return render(request,'testapp/std.html',{'student_list':student_list})


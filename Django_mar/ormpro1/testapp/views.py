from django.shortcuts import render
from testapp.models import Employee

# Create your views here.
def retrieve_view(request):
    emp_list = Employee.objects.all()   
    #emp_list = Employee.objects.filter(esal__lt=11000)
    #emp_list = Employee.objects.filter(ename__startswith='P')
    #emp_list = Employee.objects.filter(ename__startswith='A')
    #emp_list = Employee.objects.filter(ename__startswith='S') & Employee.objects.filter(esal__lt=15000)
    #emp_list = Employee.objects.all().values_list('ename','esal')
    #return render(request,'testapp/specificcolumns.html', {'emp_list':emp_list})
    #emp_list = Employee.objects.all().order_by('eno')#acending order    
    #emp_list = Employee.objects.all().order_by('-eno')#decending order

    return render(request,'testapp/index.html',{'emp_list':emp_list})  

from django.db.models import Avg,Max,Min,Sum,Count
def aggregate_view(request):
    avg = Employee.objects.all().aggregate(Avg('esal'))
    max = Employee.objects.all().aggregate(Max('esal'))
    min = Employee.objects.all().aggregate(Min('esal'))
    sum = Employee.objects.all().aggregate(Sum('esal'))
    count = Employee.objects.all().aggregate(Count('esal'))
    my_dict = {'avg':avg['esal__avg'], 'max':max['esal__max'], 'min':min['esal__min'],'sum':sum['esal__sum'], 'count':count['esal__count']}
    return render(request,'testapp/aggregate.html',my_dict)
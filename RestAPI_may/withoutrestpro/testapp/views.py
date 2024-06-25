from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data={
    'eno':101,
    'ename':'lucky',
    'esal':15000,
    'eaddr':'Hyd'
    }
    resp='<h1><u>Employees Details<br></u></h1>','<h3>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h3>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

#Django View Function to send HTTPResponse with JSON Data
import json
def emp_data_jsonview(request):
    emp_data = {
    'eno':101,
    'ename':'Veeresh',
    'esal':13000,
    'eaddr':'Ymg'
    }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')


#Django View Function to send JsonResponse directly:
from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data = {
    'eno':101,
    'ename':'Lilly',
    'esal':14000,
    'eaddr':'Hyd'
    }
    return JsonResponse(emp_data)


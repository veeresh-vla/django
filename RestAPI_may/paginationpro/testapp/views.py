from django.shortcuts import render
from rest_framework import generics
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer

# Create your views here.

class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Middleware application to show meaningful response if view function raises any error.

def home_page_view(request):
    print(10/0)
    return HttpResponse('<h1>This is from view function</h1>')
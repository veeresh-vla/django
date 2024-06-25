from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish2(request):
    return HttpResponse('<h1>This is from SECOND APP</h1>')
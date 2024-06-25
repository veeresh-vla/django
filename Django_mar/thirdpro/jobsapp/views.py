from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyd(request):
    h='<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(h)
def bng(request):
    b='<h1>Banglore Jobs Information</h1>'
    return HttpResponse(b)
def mum(request):
    m='<h1Mumbai Jobs Information</h1>'
    return HttpResponse(m)
def delhi(request):
    d='<h1>Delhi Jobs Information</h1>'
    return HttpResponse(d)
def pune(request):
    p='<h1>Pune Jobs Information</h1>'
    return HttpResponse(p)
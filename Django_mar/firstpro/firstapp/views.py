from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wish(response):
    s='<h1 style="text"=red><i>Hi Welcome To Django Nice To Meet You</h1></i>'
    return HttpResponse(s)

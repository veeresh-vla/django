from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import datetime
def timeinfo(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Friend Good Evening...!</h1>'
    msg+='<h2>Now The Server Time is:'+str(date)+'</h2>'
    return HttpResponse(msg)

from django.shortcuts import render
from django.http import HttpResponce
# Create your views here.
import datetime
 
 def info_view(request):
    time=datetime.datetime.now()
    name='Django'
    prerequisite='Python'
    my_dict={'time':time,'name':name,'prerequisite':prerequisite}
    return render(repuest,'testapp/results.html',my_dict)


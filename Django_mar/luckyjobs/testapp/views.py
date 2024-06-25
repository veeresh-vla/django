from django.shortcuts import render
from testapp.models import HydJobs,PuneJobs,BglJobs
# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobs_view(request):
    jobs_list=HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})

def punejobs_view(request):
    jobs_list=PuneJobs.objects.all()
    return render(request,'testapp/punejobs.html',{'jobs_list':jobs_list})

def bgljobs_view(request):
    jobs_list=BglJobs.objects.all()
    return render(request,'testapp/bgljobs.html',{'jobs_list':jobs_list})
from django.shortcuts import render

# Create your views here.
def wish(request):
 return render(request,'templatetestapp/wish.html')
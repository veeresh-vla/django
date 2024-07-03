from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

@login_required
def java_page_view(request):
    return render(request,'testapp/javaexams.html')

@login_required
def python_page_view(request):
    return render(request,'testapp/pythonexams.html')

@login_required
def aptitude_page_view(request):
    return render(request,'testapp/aptitudeexams.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    return render(request,'testapp/signup.html',{'form':form})

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)#to hash password
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})

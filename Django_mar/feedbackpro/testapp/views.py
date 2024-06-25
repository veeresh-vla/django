from django.shortcuts import render
from testapp.forms import FeedBackForm

# Create your views here.
def feedback_view(request):
    submitted=False
    name=''
    if request.method =='POST':
        form=FeedBackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing FeedBackInformation') 
            print('*'*57)
            print('Name:',form.cleaned_data['name'])
            print('Rollno:',form.cleaned_data['rollno'])
            print('Email:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            submitted=True
            name=form.cleaned_data['name']
    form = FeedBackForm()
    return render(request,'testapp/feedback.html',{'form':form,'submitted':submitted,'name':name})
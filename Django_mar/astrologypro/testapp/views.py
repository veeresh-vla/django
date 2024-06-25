from django.shortcuts import render
import datetime,random
# Create your views here.
def result_view(request):
    msg_list=[
         'The golden days a head',
 'Better to sleep more time even in class also',
 'Tomorrow will be the best day of your life',
 'Tomorrow is the perfect day to propose your GF',
 'Very soon you will get the job'
    ]
    names_list= ['sunny', 'kareena','samantha','samyuktha','radhika']
    time=datetime.datetime.now()
    h=int(time.strftime('%H'))
    if h<12:
        s='GOOD MORNING'
    elif h<16:
        s='GOOD AFTERNOON'
    elif h<21:
        s='GOOD EVENING'
    else:
        s='GOOD NIGHT'
    name=random.choice(names_list)
    msg=random.choice(msg_list)
    my_dict={'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astro.html',my_dict)
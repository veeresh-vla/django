from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def page_count_view(request):
    print('Cookies from client:',request.COOKIES)
    count = int(request.COOKIES.get('count',0))
    count += 1
    response = render(request,'testapp/counter.html',{'count':count})
    response.set_cookie('count',count)
    return response
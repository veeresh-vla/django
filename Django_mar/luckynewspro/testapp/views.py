from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')
def movies_view(request):
    head_msg = 'MOVIES INFORMATION'
    sub_msg1 = 'Pushpa-2 release on 15th August 2024'
    sub_msg2 = 'Devara will release on 10th october 2024'
    sub_msg3 = 'The Family Star movie release on 05th April 2024'
    type = 'movies'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def sports_view(request):
    head_msg = 'SPORTS INFORMATION'
    sub_msg1 = '2021 IPL title winner CSK'
    sub_msg2 = '2022 IPL title winner GT'
    sub_msg3 = '2023 IPL title winner CSK'
    type = 'sports'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_view(request):
    head_msg = 'POLITICS INFORMATION'
    sub_msg1 = '2010 AP CM was N Kiran Kumar Reddy'
    sub_msg2 = '2014 AP CM was N Chandrababu Naiudu'
    sub_msg3 = '2019 AP CM  was YS Jagan Mohan Reddy'
    type = 'politics'
    my_dict = {'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
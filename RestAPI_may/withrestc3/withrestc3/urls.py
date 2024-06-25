"""
URL configuration for withrestc3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('apilist/', views.EmployeeListAPIView.as_view()),
    path('apicreate/', views.EmployeeCreateAPIView.as_view()),
    path('apiretrieve/<int:pk>/', views.EmployeeRetrieveAPIView.as_view()),
    path('apiupdate/<int:id>/', views.EmployeeUpdateAPIView.as_view()),
    path('apidelete/<int:id>/', views.EmployeeDestroyAPIView.as_view()),
    path('apilist-create/', views.EmployeeListCreateAPIView.as_view()),
    path('apiretrieve-update/<int:id>/', views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('apiretrieve-destroy/<int:id>/', views.EmployeeRetrieveDestroyAPIView.as_view()),
    path('apiretrieve-update-destroy/<int:id>/', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    path('api/', views.EmployeeListCreateModelMixin.as_view()),
    path('api/<int:pk>/', views.EmployeeRetrieveUpdateDestroyModelMixin.as_view())

]

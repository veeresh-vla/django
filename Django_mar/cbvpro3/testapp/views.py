from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company

# Create your views here.

#ListView
class CompanyListView(ListView):
    model=Company
    #template_file='testapp/base.html'
    #context_object_name='Company'

#DetailView
class CompanyDetailView(DetailView):
    model=Company
    #template_file='testapp/companydetail.html'
    #context_object_name='Company'

#CreateView
class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'
    #tempalte_file='testapp/.html'
    #context_object_name='Company'

#UpdateView
class CompanyUpdateView(UpdateView):
    model = Company
    fields = ('location','ceo')

#DeleteView
from django.urls import reverse_lazy
class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('list')

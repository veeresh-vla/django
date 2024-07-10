from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Book

# Create your views here.

#ListView1
class BookListView(ListView):
    model = Book
    template_name = 'testapp/book_list1.html'
    context_object_name = 'books'

#ListView2
class BookListView2(ListView):
    model = Book
    template_name = 'testapp/book_list2.html'
    context_object_name = 'books'

#DetailView
class BookDetailsView(DetailView):
    model=Book

#CreateBook
class BookCreateView(CreateView):
    model = Book
    fields = ('title','author','pages','price')


#UpdateView
class BookUpdateView(UpdateView):
    model = Book
    fields =('title','author','pages','price',)

#DeleteView
from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'testapp/book_conform_delete.html'
    success_url = reverse_lazy('listbooks')

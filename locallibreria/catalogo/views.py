from django.shortcuts import render
from . models import Book, Author, BookInstance, Genre
from django.views import generic

#importamos información para formularios
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    num_Books = Book.objects.all().count()
    num_Instances = BookInstance.objects.all().count()

    num_Instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_Books, 'num_instances': num_Instances, 
        'num_instances_available': num_Instances_available, 'num_authors': num_authors},
    )


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial ={'date_of_death': '05/10/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class AuthorDelete(DeleteView):
    model = Author
    sucess_url = reverse_lazy('authors')


class AuthorDetailView(generic.DetailView):
    model=Author


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
class BookDetailView(generic.DetailView):
    model = Book

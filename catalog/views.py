from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .import models
from django.views import generic


def index(request):
    num_books = models.Books.objects.count()
    num_instances = models.BookInstance.objects.count()
    num_instances_available = models.BookInstance.objects.filter(status=2).count()
    num_authors = models.Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render (request, 'catalog/index.html', {'num_books': num_books, 'num_instances': num_instances,
                                                   'num_instances_available': num_instances_available,
                                                   'num_authors': num_authors, 'num_visits': num_visits})


class BookListView(generic.ListView):
    model = Books
    paginate_by = 2



class DetailBook(generic.DetailView):
    model = Books


class Author(generic.ListView):
    model = Author
    paginate_by = 3


def detail_authors(request, id):
    ...



def user(request, id, name):
    return HttpResponse(f'<h1>user id: {id} name: {name}</h1>')


def user_details(request, id):
    return HttpResponse(f'<h1>Detail information for user id: {id}</h1>')


def book(request, id):
    book = Books.objects.get(id=id)
    title = book.title
    return HttpResponse(f'<h1>Detail informations for book id: {id} name: {title}</h1>')


def genre(request, id):
    genre = Genre.objects.get(id=id)
    return HttpResponse(f'this information about genre {genre.name}')



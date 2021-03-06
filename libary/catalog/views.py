from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    num_genre = Genre.objects.all().count()

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_genre': num_genre},
    )


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book


class AuthorListView(ListView):
    model = Author

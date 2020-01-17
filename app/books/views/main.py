from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def book_list_view(request):
    books = Book.objects.order_by('title')
    context = {
        'books': books
    }
    return render(request, 'books/main.html', context)

from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book


def book_list_view(request):
    if request.user.is_authenticated:
        books = Book.objects.order_by('title')
        context = {
            'books': books
        }
        return render(request, 'books/main.html', context)
    else:
        return redirect('members:login')

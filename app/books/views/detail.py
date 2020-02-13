from django.shortcuts import render

from books.models import Book


def book_detail_view(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    context = {
        'book': book,
    }
    return render(request, 'book_detail_info.html', context)

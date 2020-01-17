from django.shortcuts import render

from books.models import Book


def book_detail_view(request, book_pk):
    selected_book = Book.objects.filter(pk=book_pk)


    context = {

    }

    return render(request, 'book_detail_info.html', context)

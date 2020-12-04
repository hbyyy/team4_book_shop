# Create your views here.
from django.shortcuts import redirect

from books.models import Book
from members.models import User
from rental.models import Rental


def rental_view(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    Rental.objects.create(book=book, user=request.user)
    return redirect('books:book-list')


def return_view(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    user = User.objects.get(pk=request.user.id)
    rental = Rental.objects.get(book=book, user=user)
    rental.delete()
    return redirect('books:book-list')

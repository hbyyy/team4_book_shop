from django.shortcuts import redirect, get_object_or_404

from books.models import Book
from reservation.models import Reservation


def reservation_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Reservation.objects.create(book=book, user=request.user)
    return redirect('books:book-list')


def reservation_cancel_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    reservation.delete()
    return redirect('books:book-list')

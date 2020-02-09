from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from books.models import Book


def main_page_view(request):
    if request.user.is_authenticated:
        books = Book.objects.order_by('title')
        user =request.user
        if user.ban_date < timezone.now():
            user.ban_date = None
            user.save()

        context = {
            'books': books,
            'current_date': timezone.now(),
            'ban_date': user.ban_date
        }
        return render(request, 'books/main.html', context)
    else:
        return redirect('members:login')

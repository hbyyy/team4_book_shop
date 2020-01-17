from django.urls import path

from .views import detail, create, request, main

app_name = 'books'
urlpatterns = [
    path('detail/', detail.book_detail_view, name='detail'),
    path('book-create/', create.book_create_view, name='book-create'),
    path('book-request/', request.book_request_view, name='book-request'),
    path('book-list/', main.book_list_view, name='book-list'),
]

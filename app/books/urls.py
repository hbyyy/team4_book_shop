from django.urls import path

from .views import detail, create, request, main

app_name = 'books'
urlpatterns = [
    path('detail/<int:book_pk>', detail.book_detail_view, name='detail'),
    path('book-create/', create.book_create_view, name='book-create'),
    path('book-request/', request.book_request_view, name='book-request'),
    path('book-list/', main.main_page_view, name='book-list'),
    path('book-request-save/', request.book_request_save_view, name='book-request-save'),
    path('book-request-confirm/', request.book_request_confirm, name='book-request-list'),
    path('book-request-confirm/<int:bookrequest_pk>/', request.book_request_confirm, name='book-request-confirm'),
]

from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('<int:book_pk>', views.rental_view, name='rental'),
    path('<int:book_pk>/return', views.return_view, name='return')
]
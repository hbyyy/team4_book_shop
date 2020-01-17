from django.urls import path
from . import views

app_name = 'rental'
urlpatterns = [
    path('<int:book_pk>', views.rental_view, name='rental'),
]
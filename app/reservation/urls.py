from django.urls import path

from . import views

app_name = 'reservation'
urlpatterns = [
    path('<int:pk>/', views.reservation_view, name='reservation'),
    path('<int:pk>/cancel/', views.reservation_cancel_view, name='reservation-cancel')
]

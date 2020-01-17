from django.contrib import admin

# Register your models here.
from reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

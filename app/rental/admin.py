from django.contrib import admin

# Register your models here.
from rental.models import Rental


@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    pass

from datetime import timedelta

from django.db import models


# Create your models here.
from django.utils import timezone


class Reservation(models.Model):
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE)
    user = models.ForeignKey('members.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=3)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'reservation : {self.book}, {self.user}'
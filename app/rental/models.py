from datetime import timedelta

from django.db import models
# Create your models here.
from django.utils import timezone


class Rental(models.Model):
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE)
    user = models.ForeignKey('members.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    is_extended = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.end_data = self.start_date + timedelta(days=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'rental : {self.book}, {self.user}'

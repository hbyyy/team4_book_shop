from datetime import timedelta

from django.db import models
# Create your models here.
from django.utils import timezone

from members.models import User


class Rental(models.Model):
    book = models.OneToOneField('books.Book', on_delete=models.CASCADE)
    user = models.ForeignKey('members.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    is_extended = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(days=1)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        now = timezone.now()
        if self.end_date < now:
            rate_timedelta = now - self.end_date
            self.user.ban_date = now + rate_timedelta
            self.user.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f'rental : {self.book}, {self.user}'

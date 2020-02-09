# from datetime import timedelta, datetime
from datetime import timedelta, datetime

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
        start_date = self.start_date

        #금요일에 빌리면 반납시간은 월요일 10시로 설정
        if self.start_date.weekday() == 4:
            end_date = datetime(year=start_date.year,
                                month=start_date.month,
                                day=(start_date + timedelta(days=3)).day,
                                hour=10 - 9,
                                tzinfo=timezone.utc)
        # 그 외에는 반납시간은 다음날 10시로 설정
        else:
            end_date = datetime(year=start_date.year,
                                month=start_date.month,
                                day=(start_date + timedelta(days=1)).day,
                                hour=10 - 9,
                                tzinfo=timezone.utc)
            self.end_date = end_date
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

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    ban_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

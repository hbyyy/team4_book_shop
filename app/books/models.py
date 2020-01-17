from django.db import models


# Create your models here.
from config import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    book_intro = models.TextField()
    image = models.ImageField(upload_to='books/image')

    def __str__(self):
        return self.title

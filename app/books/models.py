from django.db import models


# Create your models here.
from config import settings


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    book_intro = models.TextField()
    image = models.ImageField(upload_to='books/image', null=True)

    def __str__(self):
        return self.title


class BookRequest(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    book_intro = models.TextField()
    image = models.ImageField(upload_to='books/image', null=True)
    create_date = models.DateTimeField('CREATE DATE', auto_now_add=True)

    def __str__(self):
        return self.title
from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    book_intro = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

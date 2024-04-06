from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)


class BookCategory(models.Model):
    name = models.CharField(max_length=255)


class Publisher(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    image = models.ImageField(upload_to="images/book/")
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(BookCategory)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

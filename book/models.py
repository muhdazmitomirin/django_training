from django.db import models

from django.utils.timezone import now
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=100, null=True)
    published_date = models.DateField(default=now, null=True)
    author = models.ForeignKey(Author)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title




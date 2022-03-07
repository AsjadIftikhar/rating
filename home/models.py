from django.db import models
from isbn_field import ISBNField


class Book(models.Model):
    # isbn = ISBNField()
    pdf = models.FileField()
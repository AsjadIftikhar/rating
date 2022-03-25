from django.db import models
from django.contrib.auth.models import User



class Book(models.Model):
    pdf = models.FileField()


class CustomerHistory(models.Model):

    # Link to default user model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Books(models.Model):

    ASIN = models.CharField(max_length=255, unique=True, null=True)
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255, null=True)

    # count of total words
    total_words = models.IntegerField(null=True)
    # percentage of profane words
    profane_percentage = models.FloatField(null=True)

    customer_history = models.ManyToManyField(CustomerHistory, related_name='books', blank=True)

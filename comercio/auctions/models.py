from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    pass

class CreateListings(models.Model):
    n_title = models.CharField(max_length=20)
    n_description = models.CharField(max_length=100)
    n_date = models.DateField()
    n_price = models.IntegerField()
    n_category = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return super().__str__()
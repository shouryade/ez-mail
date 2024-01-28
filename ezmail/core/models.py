from django.db import models

# Create your models here.


class User(models.Model):
    """
    User model for storing user information
    """

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.username

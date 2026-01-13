from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    user_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.user_name
from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    email = models.EmailField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

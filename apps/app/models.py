from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser mst have is_active=True')
        return super().create_superuser(username, email, password, **extra_fields)

class User(AbstractUser):

    first_name = None
    last_name = None

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


"""

- AbstractUser vs AbstractBaseUser

    `AbstractUser`: Use this option if you are happy with the existing fields on the user model and just want to remove the username field.
    `AbstractBaseUser`: Use this option if you want to start from scratch by creating your own, completely new user model.


- AbstractUser
  Here, we:
    1. Created a new class called `CustomUser` that subclasses `AbstractUser`
    2. Removed the `username` field
    3. Made the `email` field required and unique
    4. Set the `USERNAME_FIELD` -- which defines the unique identifier for the `User` model -- to `email`
    5. Specified that all objects for the class come from the `CustomUserManager`

"""

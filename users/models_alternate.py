from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


"""

- AbstractUser vs AbstractBaseUser

    `AbstractUser`: Use this option if you are happy with the existing fields on the user model and just want to remove the username field.
    `AbstractBaseUser`: Use this option if you want to start from scratch by creating your own, completely new user model.


- AbstractBaseUser
  Here, we:
    1. Created a new class called `CustomUser` that subclasses `AbstractBaseUser`
    2. Added fields for `email`, `is_staff`, `is_active`, and `date_joined`
    3. Set the `USERNAME_FIELD` -- which defines the unique identifier for the `User` model -- to `email`
    4. Specified that all objects for the class come from the `CustomUserManager`

"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Represents a "user profile" inside our system.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a user's full name"""

        return self.name

    def get_abbr_name(self):
        """Used to get the short name"""

        return self.name

    def __str__(self):
        """Used to convert an object to text"""

        return self.email


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom User Manager"""

    def create_user(self, email, name, password=None):
        """Creates a new User Profile Object"""

        if not email:
            raise ValueError('Email is a required field')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates a superuser with the given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(self._db)

        return user

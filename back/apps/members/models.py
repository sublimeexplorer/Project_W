"""
Defines the database schema for the app.
Contains Django model classes that represent database tables.
In this case, it would likely include user-related models like CustomUser or UserProfile.


models.Model:
- When you create a class that inherits from models.Model, Django automatically creates a corresponding database table.


AbstractUser:
- This is a built-in Django class that inherits from AbstractBaseUser and includes fields and methods for a fully featured user model.
- It's part of Django's authentication system.
- AbstractUser provides a complete implementation of a User model, including fields like username, email, first_name, last_name, etc.
- It's called "abstract" because it's not meant to be used directly as a model, but rather to be subclassed.
- When you want to customize the User model in your Django project, you typically subclass AbstractUser rather than creating a User model from scratch.

Certainly! The AbstractUser and models.Model are both important classes in Django, but they serve different purposes:

models.Model:


This is the base class for all Django model classes.
It's used to define a Python class that represents a database table.
When you create a class that inherits from models.Model, Django automatically creates a corresponding database table.
It provides the core functionality for interacting with the database, including methods for saving, querying, and deleting records.
You use this as a base class for most of your custom models in Django.


AbstractUser:


This is a built-in Django class that inherits from AbstractBaseUser and includes fields and methods for a fully featured user model.
It's part of Django's authentication system.
AbstractUser provides a complete implementation of a User model, including fields like username, email, first_name, last_name, etc.
It's called "abstract" because it's not meant to be used directly as a model, but rather to be subclassed.
When you want to customize the User model in your Django project, you typically subclass AbstractUser rather than creating a User model from scratch.

Key differences:

Purpose:

models.Model is a general-purpose base class for all models.
AbstractUser is specifically designed for user authentication and management.


Fields:

models.Model doesn't come with any predefined fields.
AbstractUser comes with a set of fields commonly used for user accounts.


Usage:

You use models.Model as a base class for most of your custom models.
You subclass AbstractUser when you want to customize the User model while retaining Django's built-in user functionality.


Authentication:

models.Model doesn't provide any authentication methods.
AbstractUser includes methods for password hashing, permissions, and other user-related functionality.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class Member(AbstractUser):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('trainer', 'Trainer'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(Member, on_delete=models.CASCADE)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    body_fat_percentage = models.FloatField(null=True, blank=True)
    fitness_goal = models.CharField(max_length=100, blank=True)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.

class Employee(models.Model):
    employee_regNo = models.TextField(unique=True)
    employee_name = models.TextField()
    employee_email = models.TextField()
    employee_mobile = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now=True)

class Account(models.Model):
    USERNAME_FIELD = 'email'
    username = models.TextField()
    email = models.EmailField()
    password = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    # def __str__(self):
    #     return self.username
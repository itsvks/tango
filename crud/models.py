from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    age = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)

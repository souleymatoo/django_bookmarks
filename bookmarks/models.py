from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link(models.Model):
    url = models.URLField(unique=True)

class Users(models.Model):
    username = models.TextField(max_length=255)
    password = models.CharField(max_length=30)
    email = models.EmailField()

class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
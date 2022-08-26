from django.db import models
from django.utils import timezone
import hashlib

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    ingredients = models.TextField(max_length=1080)
    instructions = models.TextField(max_length=1080)

    def __str__(self) -> str:
        return self.title

class Test(models.Model):
    name = models.CharField(max_length=255)
    location = models.TextField(max_length=1080)

    def __str__(self) -> str:
        return self.name

class Celebrity(models.Model):
    name = models.CharField(max_length=255, unique=True)
    taboo1 = models.CharField(max_length=255)
    taboo2 = models.CharField(max_length=255)
    taboo3 = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=255)

class Contact(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class AppUser(models.Model):
    email = models.EmailField(max_length=64, unique=True)
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64, default="")
    api_key = models.CharField(max_length=64, unique=True, default=hashlib.sha256(str(timezone.now).encode()).hexdigest())
    image = models.CharField(max_length=255, default="")
    website = models.CharField(max_length=255, default="")
    settings = models.TextField(max_length=1024, default="") 
    about = models.TextField(max_length=1024, default="")
    created_at = models.DateTimeField(default=timezone.now)

class Post(models.Model):
    user = models.CharField(max_length=64, unique=True)
    likes = models.TextField(default="")
    text = models.TextField(default="")
    comments = models.TextField(default="")
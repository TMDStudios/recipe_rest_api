from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
import hashlib

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

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
    username = models.CharField(max_length=64, unique=True, validators=[alphanumeric])
    password = models.CharField(max_length=64, blank=True, default="", validators=[alphanumeric])
    api_key = models.CharField(max_length=64, blank=True, default=hashlib.sha256(str(timezone.now()).encode()).hexdigest())
    image = models.CharField(max_length=255, blank=True, default="")
    website = models.CharField(max_length=255, blank=True, default="")
    settings = models.TextField(max_length=1024, blank=True, default="") 
    about = models.TextField(max_length=1024, blank=True, default="")
    created_at = models.DateTimeField(blank=True, default=timezone.now())

    def save(self, *args, **kwargs):
        preHash = str(timezone.now())+self.username
        self.api_key = hashlib.sha256(preHash.encode()).hexdigest()
        super(AppUser, self).save(*args, **kwargs)

class Post(models.Model):
    user = models.CharField(max_length=64, blank=True, default="Anonymous")
    title = models.CharField(max_length=255, blank=True, default="")
    likes = models.TextField(blank=True, default="")
    text = models.TextField(blank=True, default="")
    comments = models.TextField(blank=True, default="")

class Word(models.Model):
    word = models.CharField(max_length=64)
    level = models.IntegerField()
    sentence = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.word
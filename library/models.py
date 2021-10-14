from django.db import models

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
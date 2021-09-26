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
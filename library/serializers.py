from rest_framework import serializers
from .models import Recipe, Test

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["pk", "title", "author", "ingredients", "instructions"]

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["name", "location"]
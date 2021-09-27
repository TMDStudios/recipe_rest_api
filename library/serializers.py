from rest_framework import serializers
from .models import Recipe, Test, Celebrity

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["pk", "title", "author", "ingredients", "instructions"]

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["name", "location"]

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ["name", "taboo1", "taboo2", "taboo3"]
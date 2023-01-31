from rest_framework import serializers
from .models import Recipe, Test, Celebrity, Person, Contact, AppUser, Post, Word

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ["pk", "title", "author", "ingredients", "instructions"]

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["pk", "name", "location"]

class CelebritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebrity
        fields = ["pk", "name", "taboo1", "taboo2", "taboo3"]

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name"]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["pk", "name", "location", "mobile", "email"]

class AppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ["id", "email", "username", "password", "image", "website", "settings", "about"]

class NewAppUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ["id", "email", "username", "password", "image", "website", "settings", "about", "created_at"]
        extra_kwargs = {
            'password': {'write_only': True},
            'api_key': {'write_only': True},
            'settings': {'write_only': True}
        }

class PostSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(PostSerializer, self).__init__(*args, **kwargs)
        if self.context['request'].method == "PUT":
            self.fields.pop('user')

    class Meta:
        model = Post
        fields = "__all__"

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["word", "level", "sentence"]
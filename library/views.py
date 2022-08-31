from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Recipe, Test, Celebrity, Person, Contact, AppUser, Post
from .serializers import CelebritySerializer, PersonSerializer, RecipeSerializer, TestSerializer, ContactSerializer, AppUserSerializer, NewAppUserSerializer, PostSerializer
from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

def home(request):
    recipes = Recipe.objects.all()
    recipes = recipes.order_by('-id')
    context = {}
    context['recipes'] = recipes
    
    return render(request, 'home.html', context)

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class CelebrityList(generics.ListCreateAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer

class CelebrityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Celebrity.objects.all()
    serializer_class = CelebritySerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class AppUserList(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = NewAppUserSerializer

class GetUser(APIView):
    def get(self, request, api_key, *args, **kwargs):
        try:
            user = AppUser.objects.all().filter(api_key=api_key)
            serializer = AppUserSerializer(user[0])
            return Response(serializer.data)
        except IndexError:
            return JsonResponse({}, safe=False)

def login(request, username, password):
    user = get_object_or_404(AppUser, username=username)

    if password == user.password:
        return HttpResponse(user.api_key)
    
    return HttpResponse("Unable to log in")

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

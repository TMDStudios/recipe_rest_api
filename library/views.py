from rest_framework import generics
from .models import Recipe, Test, Celebrity, Person, Contact
from .serializers import CelebritySerializer, PersonSerializer, RecipeSerializer, TestSerializer, ContactSerializer
from django.shortcuts import render

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
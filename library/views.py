from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
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
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
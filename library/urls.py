from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("recipes/", views.RecipeList.as_view()),
    path("recipes/<int:pk>", views.RecipeDetail.as_view()),
    path("test/", views.TestList.as_view()),
    path("test/<int:pk>", views.TestDetail.as_view())
]
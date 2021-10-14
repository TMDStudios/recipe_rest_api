from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("recipes/", views.RecipeList.as_view()),
    path("recipes/<int:pk>", views.RecipeDetail.as_view()),
    path("test/", views.TestList.as_view()),
    path("test/<int:pk>", views.TestDetail.as_view()),
    path("celebrities/", views.CelebrityList.as_view()),
    path("celebrities/<int:pk>", views.CelebrityDetail.as_view()),
    path("people/", views.PersonList.as_view()),
    path("contacts/", views.ContactList.as_view()),
    path("contacts/<int:pk>", views.ContactDetail.as_view()),
]
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("recipes/<int:pk>", views.RecipeDetail.as_view()),
    path("recipes/", views.RecipeList.as_view()),
    path("test/", views.TestList.as_view()),
    path("test/<int:pk>", views.TestDetail.as_view()),
    path("celebrities/", views.CelebrityList.as_view()),
    path("celebrities/<int:pk>", views.CelebrityDetail.as_view()),
    path("people/", views.PersonList.as_view()),
    path("contacts/", views.ContactList.as_view()),
    path("contacts/<int:pk>", views.ContactDetail.as_view()),
    path("users/", views.AppUserList.as_view()),
    path("users/<slug:api_key>", views.GetUser.as_view()),
    path("user-data/", views.allUserData, name='userData'),
    path("user-data/<int:pk>", views.userData, name='userData'),
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>", views.PostList.as_view()),
]
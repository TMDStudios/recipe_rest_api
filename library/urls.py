from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("recipes/<int:pk>", views.RecipeDetail.as_view()),
    path("test/<int:pk>", views.TestDetail.as_view()),
    path("word/<int:pk>", views.WordDetail.as_view()),
    path("celebrities/<int:pk>", views.CelebrityDetail.as_view()),
    path("contacts/<int:pk>", views.ContactDetail.as_view()),
    path("users/<slug:api_key>", views.GetUser.as_view()),
    # path("users/<int:pk>", views.AppUserDetail.as_view()),
    path("posts/<int:pk>", views.PostDetail.as_view()),
    path("recipes/", views.RecipeList.as_view()),
    path("test/", views.TestList.as_view()),
    path("words/", views.WordList.as_view()),
    path("celebrities/", views.CelebrityList.as_view()),
    path("people/", views.PersonList.as_view()),
    path("contacts/", views.ContactList.as_view()),
    path("users/", views.AppUserList.as_view()),
    path("posts/", views.PostList.as_view()),
    path("login/<slug:username>/<slug:password>", views.login, name="login"),
    path("login/<slug:username>/", views.noPwLogin, name="login"),
]
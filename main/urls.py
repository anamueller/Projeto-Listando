from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include  #add include


app_name = "main"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register")
]
from django.urls import path
from . import views
from .views import HomeView

app_name = "main"   


urlpatterns = [
    path('', HomeView.as_view(),  name='home'),
    path("register", views.register_request, name="register")
]
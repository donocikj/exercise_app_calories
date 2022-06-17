from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="calories_app-home"),
]
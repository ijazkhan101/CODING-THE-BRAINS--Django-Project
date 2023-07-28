
from django import views
from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = "myapp"

urlpatterns = [
    path("index/", views.index, name='index'),
    path("home/", views.home, name='home'),
]

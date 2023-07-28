
from django.contrib import admin
from django.urls import path, include
from .views import *
app_name = "myapp"

urlpatterns = [
    path("index/", index, name='index'),
    path("home/", home, name='home'),
]

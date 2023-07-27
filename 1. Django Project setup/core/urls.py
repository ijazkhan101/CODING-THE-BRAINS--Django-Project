
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("firstApp/", include("firstApp.urls")),
    path("secondApp/", include("secondApp.urls")),
    path("myapp/", include("myapp.urls")),
]

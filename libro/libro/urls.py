# Archivo urls
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^', include('applications.home.urls')),
    path('admin/', admin.site.urls),
]

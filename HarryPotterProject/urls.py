"""
URL configuration for HarryPotterProject project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Ruta del administrador de Django
    path('admin/', admin.site.urls),

    # Ruta principal de la aplicación personajes
    path('', include('personajes.urls')),
]


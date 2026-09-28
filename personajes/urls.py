from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_personajes, name='lista_personajes'),
    path('personaje/<int:indice>/', views.detalle_personaje, name='detalle_personaje'),
]


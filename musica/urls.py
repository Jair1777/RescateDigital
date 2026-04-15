from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_musica, name='inicio_musica'),
    path('genero/<slug:slug>/', views.detalle_genero, name='detalle_genero'),
]

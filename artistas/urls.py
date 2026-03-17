from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_artistas, name='artistas_lista'),
    path('<int:artista_id>/', views.detalle_artista, name='artista_detalle'),
]

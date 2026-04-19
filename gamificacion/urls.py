from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name='juegos_lista'),
    path('quiz/<int:quiz_id>/', views.jugar_quiz, name='jugar_quiz'),
    path('ranking/', views.ranking, name='ranking'),
    path('desafio-velocidad/', views.desafio_velocidad, name='desafio_velocidad'),
    path('album/', views.album_cromos, name='album_cromos'),
]

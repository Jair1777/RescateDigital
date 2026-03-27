from django.shortcuts import render, get_object_or_404
from .models import Artista
from gamificacion.models import Quiz

def lista_artistas(request):
    artistas = Artista.objects.all().order_by('nombre')
    return render(request, 'artistas/lista.html', {'artistas': artistas})

def detalle_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    # Buscamos el quiz que contenga el nombre del artista en el titulo
    quiz = Quiz.objects.filter(titulo__icontains=artista.nombre).first()
    return render(request, 'artistas/detalle.html', {'artista': artista, 'quiz': quiz})

from django.shortcuts import render, get_object_or_404
from .models import Artista

def lista_artistas(request):
    artistas = Artista.objects.all().order_by('nombre')
    return render(request, 'artistas/lista.html', {'artistas': artistas})

def detalle_artista(request, artista_id):
    artista = get_object_or_404(Artista, id=artista_id)
    return render(request, 'artistas/detalle.html', {'artista': artista})

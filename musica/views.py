from django.shortcuts import render, get_object_or_404
from .models import GeneroMusical, Cancion, RecursoEducativo

def inicio_musica(request):
    generos = GeneroMusical.objects.prefetch_related('canciones').all()
    todas_canciones = Cancion.objects.select_related('genero', 'compositor').all()
    recursos = RecursoEducativo.objects.all()[:5]
    context = {
        'generos': generos,
        'todas_canciones': todas_canciones,
        'recursos': recursos,
    }
    return render(request, 'musica/inicio.html', context)

def detalle_genero(request, slug):
    genero = get_object_or_404(GeneroMusical, slug=slug)
    canciones = genero.canciones.all()
    recursos = genero.recursos_educativos.all()
    context = {
        'genero': genero,
        'canciones': canciones,
        'recursos': recursos,
    }
    return render(request, 'musica/genero.html', context)

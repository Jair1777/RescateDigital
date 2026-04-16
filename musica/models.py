from django.db import models
from django.utils.translation import get_language
from artistas.models import Artista

class GeneroMusical(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL amigable para el género.")
    
    descripcion_historica = models.TextField()
    descripcion_historica_en = models.TextField(blank=True)
    descripcion_historica_fr = models.TextField(blank=True)
    
    caracteristicas_musicales = models.TextField()
    caracteristicas_musicales_en = models.TextField(blank=True)
    caracteristicas_musicales_fr = models.TextField(blank=True)
    
    imagen_representativa = models.ImageField(upload_to='musica/generos/', null=True, blank=True)

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    @property
    def translated_descripcion_historica(self):
        return self.get_translated('descripcion_historica')

    @property
    def translated_caracteristicas_musicales(self):
        return self.get_translated('caracteristicas_musicales')

    def __str__(self):
        return self.nombre

class Cancion(models.Model):
    titulo = models.CharField(max_length=200)
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE, related_name='canciones')
    compositor = models.ForeignKey(Artista, on_delete=models.SET_NULL, null=True, blank=True, related_name='canciones_musica_lojana')
    
    descripcion = models.TextField(blank=True)
    descripcion_en = models.TextField(blank=True)
    descripcion_fr = models.TextField(blank=True)
    
    archivo_audio = models.FileField(upload_to='musica/audios/', null=True, blank=True)
    url_youtube = models.URLField(max_length=500, blank=True, null=True, help_text="Link de YouTube para reproducir si no hay archivo físico.")
    fecha_lanzamiento = models.CharField(max_length=100, blank=True, help_text="Época o año relativo.")

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    @property
    def translated_descripcion(self):
        return self.get_translated('descripcion')

    def __str__(self):
        return f"{self.titulo} - {self.genero.nombre}"

class RecursoEducativo(models.Model):
    TIPO_OPCIONES = [
        ('articulo', 'Artículo'),
        ('referencia', 'Referencia Cultural'),
        ('explicacion', 'Explicación'),
    ]
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50, choices=TIPO_OPCIONES, default='articulo')
    genero = models.ForeignKey(GeneroMusical, on_delete=models.SET_NULL, null=True, blank=True, related_name='recursos_educativos')
    
    contenido = models.TextField()
    contenido_en = models.TextField(blank=True)
    contenido_fr = models.TextField(blank=True)

    def get_translated(self, field_name):
        lang = get_language()
        if lang == 'en':
            attr = f"{field_name}_en"
            val = getattr(self, attr, None)
            if val: return val
        elif lang == 'fr':
            attr = f"{field_name}_fr"
            val = getattr(self, attr, None)
            if val: return val
        return getattr(self, field_name)

    @property
    def translated_contenido(self):
        return self.get_translated('contenido')

    def __str__(self):
        return self.titulo

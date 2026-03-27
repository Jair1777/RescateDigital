from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    periodo_vida = models.CharField(max_length=200, blank=True, help_text="Ej: 1 de marzo de 1876 – 1935")
    biografia = models.TextField()
    composiciones_resumen = models.TextField(blank=True)
    obras_destacadas_resumen = models.TextField(blank=True)
    legado_resumen = models.TextField(blank=True)
    imagen_perfil = models.ImageField(upload_to='artistas/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class ObraDestacada(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    archivo_audio = models.FileField(upload_to='audios/', null=True, blank=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='obras')

    def __str__(self):
        return f'{self.titulo} - {self.artista.nombre}'

class HitoLineaTiempo(models.Model):
    anio = models.IntegerField()
    evento = models.CharField(max_length=300)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='hitos')

    class Meta:
        ordering = ['anio']

    def __str__(self):
        return f'{self.anio}: {self.evento[:50]}'

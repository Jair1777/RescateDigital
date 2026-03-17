from django.db import models

class Quiz(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='preguntas')
    texto_pregunta = models.CharField(max_length=300)

    def __str__(self):
        return self.texto_pregunta

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=200)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.texto} ({"Correcta" if self.es_correcta else "Incorrecta"})'

class Logro(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    puntos_requeridos = models.IntegerField()
    icono = models.ImageField(upload_to='logros/', null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} ({self.puntos_requeridos} pts)'

from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    puntos_acumulados = models.IntegerField(default=0)
    ranking = models.IntegerField(default=0)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return f'{self.username} - {self.puntos_acumulados} pts'

class Notificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones')
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    icono = models.CharField(max_length=50, default='fas fa-bell text-primary')

    def __str__(self):
        return f"Notificación para {self.usuario.username}: {self.mensaje}"

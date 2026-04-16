from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    puntos_acumulados = models.IntegerField(default=0)
    ranking = models.IntegerField(default=0)
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)

    def __str__(self):
        return f'{self.username} - {self.puntos_acumulados} pts'

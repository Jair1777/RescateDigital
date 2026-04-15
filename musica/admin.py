from django.contrib import admin
from .models import GeneroMusical, Cancion, RecursoEducativo

@admin.register(GeneroMusical)
class GeneroMusicalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug')
    prepopulated_fields = {'slug': ('nombre',)}

@admin.register(Cancion)
class CancionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'compositor')
    list_filter = ('genero', 'compositor')

@admin.register(RecursoEducativo)
class RecursoEducativoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'genero')
    list_filter = ('tipo', 'genero')

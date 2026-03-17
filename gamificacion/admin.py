from django.contrib import admin
from .models import Quiz, Pregunta, Opcion, Logro

class OpcionInline(admin.TabularInline):
    model = Opcion
    extra = 3

@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('texto_pregunta', 'quiz')
    inlines = [OpcionInline]

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Logro)
class LogroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'puntos_requeridos')
    search_fields = ('nombre',)

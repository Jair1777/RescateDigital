import os
import django
from django.utils.text import slugify

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from musica.models import GeneroMusical

generos = [
    {
        "nombre": "Pasillo",
        "descripcion": "El género más representativo del Ecuador, caracterizado por su tono melancólico y poético."
    },
    {
        "nombre": "Pasacalle",
        "descripcion": "Un ritmo alegre y festivo, a menudo considerado el segundo himno de las ciudades ecuatorianas."
    },
    {
        "nombre": "Villancico",
        "descripcion": "Cancionero tradicional de Navidad, muy arraigado en la fe y cultura lojana."
    },
    {
        "nombre": "Guitarra Clásica",
        "descripcion": "Obras de concierto interpretadas con maestría académica sobre las seis cuerdas."
    }
]

for g in generos:
    obj, created = GeneroMusical.objects.get_or_create(
        nombre=g['nombre'],
        defaults={
            'slug': slugify(g['nombre']),
            'descripcion_historica': g['descripcion'],
            'caracteristicas_musicales': "Ritmo, armonía y melodía tradicional lojana."
        }
    )
    if created:
        print(f"Género creado: {g['nombre']}")

print("Carga de géneros finalizada.")

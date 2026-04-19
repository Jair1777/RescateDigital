import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Cromo
from artistas.models import Artista

def create_cromos():
    cromos_data = [
        {
            "nombre": "Estudiante de Conservatorio",
            "descripcion": "El inicio de todo gran músico. Has dado tu primer paso en la historia lojana.",
            "descripcion_en": "The beginning of every great musician. You have taken your first step in Loja history.",
            "puntos_requeridos": 0,
            "icono": "fas fa-guitar",
            "rareza": "Común",
            "color_borde": "#a8a8a8"
        },
        {
            "nombre": "Salvador Bustamante Celi",
            "descripcion": "Considerado el padre de la música académica en Loja. Esencia: La Devoción.",
            "descripcion_en": "Considered the father of academic music in Loja. Essence: Devotion.",
            "puntos_requeridos": 20,
            "icono": "fas fa-user-tie",
            "rareza": "Rara",
            "color_borde": "#4a90e2",
            "artista": "Salvador Bustamante Celi"
        },
        {
            "nombre": "Segundo Cueva Celi",
            "descripcion": "El maestro de la elegancia y compositor de Pequeña Ciudadana.",
            "descripcion_en": "The master of elegance and composer of Pequeña Ciudadana.",
            "puntos_requeridos": 50,
            "icono": "fas fa-music",
            "rareza": "Rara",
            "color_borde": "#4a90e2",
            "artista": "Segundo Cueva Celi"
        },
        {
            "nombre": "Guitarra de Oro",
            "descripcion": "Símbolo de maestría de los más grandes guitarristas andinos.",
            "descripcion_en": "Symbol of mastery of the greatest Andean guitarists.",
            "puntos_requeridos": 100,
            "icono": "fas fa-award",
            "rareza": "Épica",
            "color_borde": "#9b59b6"
        },
        {
            "nombre": "Benjamín Carrión",
            "descripcion": "Más que músico, el arquitecto cultural del Ecuador. 'Una gran cultura'.",
            "descripcion_en": "More than a musician, the cultural architect of Ecuador. 'A great culture'.",
            "puntos_requeridos": 150,
            "icono": "fas fa-landmark",
            "rareza": "Legendaria",
            "color_borde": "#f39c12",
            "artista": "Benjamín Carrión"
        }
    ]

    for c_data in cromos_data:
        artista_obj = None
        if "artista" in c_data:
            artista_obj = Artista.objects.filter(nombre=c_data["artista"]).first()
            
        Cromo.objects.get_or_create(
            nombre=c_data["nombre"],
            defaults={
                "nombre_en": c_data.get("nombre_en", ""),
                "descripcion": c_data["descripcion"],
                "descripcion_en": c_data.get("descripcion_en", ""),
                "puntos_requeridos": c_data["puntos_requeridos"],
                "icono": c_data["icono"],
                "rareza": c_data["rareza"],
                "color_borde": c_data["color_borde"],
                "artista": artista_obj
            }
        )
        print(f"Cromo añadido: {c_data['nombre']}")

if __name__ == '__main__':
    create_cromos()
    print("¡Cromos poblados con éxito!")

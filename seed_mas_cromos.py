import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Cromo
from artistas.models import Artista

def seed_mas_cromos():
    nuevos_cromos = [
        {
            "nombre": "El Rondín Bohemio",
            "descripcion": "El instrumento que acompañaba las serenatas a medianoche en las antiguas calles de Loja.",
            "descripcion_en": "The instrument that accompanied midnight serenades in the old streets of Loja.",
            "puntos_requeridos": 30,
            "icono": "fas fa-music",
            "rareza": "Común",
            "color_borde": "#7f8c8d"
        },
        {
            "nombre": "Manuel de Jesús Lozano",
            "descripcion": "El Juglar de Loja, maestro del violín y creador de los romances más honestos.",
            "descripcion_en": "The Juglar of Loja, master of the violin and creator of the most honest romances.",
            "puntos_requeridos": 80,
            "icono": "fas fa-user-tie",
            "rareza": "Rara",
            "color_borde": "#3498db",
            "artista": "Manuel de Jesús Lozano"
        },
        {
            "nombre": "Marcos Ochoa Muñoz",
            "descripcion": "El guía disciplinado. Formó a generaciones de jóvenes lojanos.",
            "descripcion_en": "The disciplined guide. Trained generations of young people from Loja.",
            "puntos_requeridos": 120,
            "icono": "fas fa-chalkboard-teacher",
            "rareza": "Rara",
            "color_borde": "#3498db",
            "artista": "Marcos Ochoa Muñoz"
        },
        {
            "nombre": "Partitura Secreta",
            "descripcion": "Un manuscrito perdido que aguarda ser interpretado por una orquesta moderna.",
            "descripcion_en": "A lost manuscript waiting to be performed by a modern orchestra.",
            "puntos_requeridos": 160,
            "icono": "fas fa-scroll",
            "rareza": "Épica",
            "color_borde": "#9b59b6"
        },
        {
            "nombre": "Emiliano Ortega Espinosa",
            "descripcion": "El poeta paisajista que le dio voz literaria a los valles lojanos.",
            "descripcion_en": "The landscape poet who gave a literary voice to the Loja valleys.",
            "puntos_requeridos": 200,
            "icono": "fas fa-feather-alt",
            "rareza": "Épica",
            "color_borde": "#9b59b6",
            "artista": "Emiliano Ortega Espinosa"
        },
        {
            "nombre": "David Pacheco Ochoa",
            "descripcion": "El vigor de las bandas comunitarias. Creador del icónico pasacalle festivo.",
            "descripcion_en": "The vigor of community bands. Creator of the iconic festive pasacalle.",
            "puntos_requeridos": 250,
            "icono": "fas fa-drum",
            "rareza": "Épica",
            "color_borde": "#9b59b6",
            "artista": "David Pacheco Ochoa"
        },
        {
            "nombre": "El Violín de las Almas",
            "descripcion": "Un violín artesanal tallado en madera pura. Representa el espíritu libre lojano.",
            "descripcion_en": "An artisan violin carved from pure wood. It represents the free spirit of Loja.",
            "puntos_requeridos": 300,
            "icono": "fas fa-viola",
            "rareza": "Legendaria",
            "color_borde": "#f39c12"
        },
        {
            "nombre": "Carlos Bonilla Chávez",
            "descripcion": "Elevó la guitarra académica ecuatoriana al estándar universal.",
            "descripcion_en": "Elevated the Ecuadorian academic guitar to the universal standard.",
            "puntos_requeridos": 350,
            "icono": "fas fa-guitar",
            "rareza": "Legendaria",
            "color_borde": "#e67e22",
            "artista": "Carlos Bonilla Chávez"
        },
        {
            "nombre": "Segundo Luis Moreno",
            "descripcion": "El Arqueólogo Sonoro. Desenterró el pasado para iluminar nuestro presente.",
            "descripcion_en": "The Sonic Archaeologist. Unearthed the past to illuminate our present.",
            "puntos_requeridos": 400,
            "icono": "fas fa-search",
            "rareza": "Legendaria",
            "color_borde": "#e67e22",
            "artista": "Segundo Luis Moreno"
        },
        {
            "nombre": "Llave del Gran Teatro",
            "descripcion": "La llave dorada que abre todas las puertas artísticas de la ciudad.",
            "descripcion_en": "The golden key that opens all the artistic doors of the city.",
            "puntos_requeridos": 450,
            "icono": "fas fa-key",
            "rareza": "Mítica",
            "color_borde": "#e74c3c"
        },
        {
            "nombre": "Alma Lencana",
            "descripcion": "Representación de la identidad pura de la casta y devoción lojana.",
            "descripcion_en": "Representation of the pure identity of the caste and devotion of Loja.",
            "puntos_requeridos": 500,
            "icono": "fas fa-crown",
            "rareza": "Suprema",
            "color_borde": "#00ffcc"
        }
    ]

    for c in nuevos_cromos:
        artista_obj = None
        if "artista" in c:
            artista_obj = Artista.objects.filter(nombre__icontains=c["artista"]).first()
            
        Cromo.objects.get_or_create(
            nombre=c["nombre"],
            defaults={
                "nombre_en": c["nombre"],
                "descripcion": c["descripcion"],
                "descripcion_en": c["descripcion_en"],
                "puntos_requeridos": c["puntos_requeridos"],
                "icono": c["icono"],
                "rareza": c["rareza"],
                "color_borde": c["color_borde"],
                "artista": artista_obj
            }
        )
        print(f"Cromo añadido al álbum: {c['nombre']} ({c['puntos_requeridos']} pts)")

if __name__ == '__main__':
    seed_mas_cromos()
    print("¡Expansión de Cromos completada existosamente!")

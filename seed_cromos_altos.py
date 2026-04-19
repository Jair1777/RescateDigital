import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Cromo

def seed_cromos_altos():
    nuevos_cromos = [
        {
            "nombre": "El Pasillo de Oro",
            "descripcion": "Un disco de oro representando las melodías eternas que han traspasado generaciones.",
            "descripcion_en": "A golden record representing the eternal melodies that have transcended generations.",
            "puntos_requeridos": 600,
            "icono": "fas fa-compact-disc",
            "rareza": "Suprema",
            "color_borde": "#ffd700"
        },
        {
            "nombre": "Director Sinfónico",
            "descripcion": "La batuta mágica capaz de congregar a los mejores instrumentistas del sur del país.",
            "descripcion_en": "The magic baton capable of gathering the best instrumentalists in the south of the country.",
            "puntos_requeridos": 800,
            "icono": "fas fa-magic",
            "rareza": "Suprema",
            "color_borde": "#ffd700"
        },
        {
            "nombre": "Estrella del Bolívar",
            "descripcion": "Una luz que simboliza los estrenos teatrales más prestigiosos de las décadas doradas.",
            "descripcion_en": "A light symbolizing the most prestigious theatrical premieres of the golden decades.",
            "puntos_requeridos": 1000,
            "icono": "fas fa-star",
            "rareza": "Trascendental",
            "color_borde": "#e056fd"
        },
        {
            "nombre": "Musa de los Valles",
            "descripcion": "La inspiración etérea que dicta las mejores letras a los compositores enamorados.",
            "descripcion_en": "The ethereal inspiration that dictates the best lyrics to enamored composers.",
            "puntos_requeridos": 1200,
            "icono": "fas fa-wind",
            "rareza": "Trascendental",
            "color_borde": "#e056fd"
        },
        {
            "nombre": "El Maestro Inmortal",
            "descripcion": "Otorgado únicamente a aquellos que han dedicado su alma a comprender el pentagrama lojano.",
            "descripcion_en": "Granted only to those who have dedicated their souls to understanding the Loja pentagram.",
            "puntos_requeridos": 1500,
            "icono": "fas fa-chess-king",
            "rareza": "Reliquia",
            "color_borde": "#ff004c"
        },
        {
            "nombre": "Loja, Capital Musical",
            "descripcion": "El máximo galardón. Tienes el corazón y el conocimiento digno de nuestra provincia hermana.",
            "descripcion_en": "The highest award. You have the heart and knowledge worthy of our sister province.",
            "puntos_requeridos": 2000,
            "icono": "fas fa-gem",
            "rareza": "Reliquia",
            "color_borde": "#00ffff"
        }
    ]

    for c in nuevos_cromos:
        Cromo.objects.get_or_create(
            nombre=c["nombre"],
            defaults={
                "nombre_en": c["nombre_en"] if "nombre_en" in c else c["nombre"],
                "descripcion": c["descripcion"],
                "descripcion_en": c["descripcion_en"],
                "puntos_requeridos": c["puntos_requeridos"],
                "icono": c["icono"],
                "rareza": c["rareza"],
                "color_borde": c["color_borde"]
            }
        )
        print(f"Cromo Alto Nivel añadido: {c['nombre']} ({c['puntos_requeridos']} pts)")

if __name__ == '__main__':
    seed_cromos_altos()
    print("¡Nuevos Cromos de Alto Nivel poblados existosamente!")

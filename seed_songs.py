import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from musica.models import Cancion, GeneroMusical
from artistas.models import Artista

# Map genres for easy lookup
gen_map = {g.nombre: g for g in GeneroMusical.objects.all()}

data = [
    {
        "artista": "Salvador Bustamante Celi",
        "cancion": "Dulce Jesús Mío",
        "genero": "Villancico",
        "url": "https://www.youtube.com/watch?v=0kG5mFq22-Q"
    },
    {
        "artista": "Salvador Bustamante Celi",
        "cancion": "Amor y Olvido",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=J8_7iH_O_s0"
    },
    {
        "artista": "Segundo Cueva Celi",
        "cancion": "Vaso de Lágrimas",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=4Yv5U_m03r8"
    },
    {
        "artista": "Segundo Cueva Celi",
        "cancion": "Pequeña Ciudadana",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=R9M-mXitDsc"
    },
    {
        "artista": "Manuel de Jesús Lozano",
        "cancion": "Ya no te quiero, pero no te olvido",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=W0nL93_69mE"
    },
    {
        "artista": "Manuel de Jesús Lozano",
        "cancion": "Traguito Lojano",
        "genero": "Pasacalle",
        "url": "https://www.youtube.com/watch?v=Kz69k0j7t9w"
    },
    {
        "artista": "Marcos Ochoa Muñoz",
        "cancion": "La Flor Zamorana",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=7M7O9u-I2tA"
    },
    {
        "artista": "Marcos Ochoa Muñoz",
        "cancion": "Nostalgias",
        "genero": "Pasillo",
        "url": "https://www.youtube.com/watch?v=3jK6F_O7K7Q"
    },
    {
        "artista": "David Pacheco Ochoa",
        "cancion": "El Chulla Quiteño",
        "genero": "Pasacalle",
        "url": "https://www.youtube.com/watch?v=tT8O9V99yGk"
    },
    {
        "artista": "David Pacheco Ochoa",
        "cancion": "Sangre Lojana",
        "genero": "Pasacalle",
        "url": "https://www.youtube.com/watch?v=BqB8GqjI6M4"
    },
    {
        "artista": "Emiliano Ortega Espinosa",
        "cancion": "Lojanita",
        "genero": "Pasacalle",
        "url": "https://www.youtube.com/watch?v=Xz5-vVq9n8o"
    },
    {
        "artista": "Carlos Bonilla Chávez",
        "cancion": "Cantares de mi Tierra",
        "genero": "Guitarra Clásica",
        "url": "https://www.youtube.com/watch?v=p79tCg-XvX0"
    }
]

for item in data:
    try:
        artista = Artista.objects.get(nombre=item['artista'])
        genero = gen_map.get(item['genero'])
        
        cancion, created = Cancion.objects.update_or_create(
            titulo=item['cancion'],
            compositor=artista,
            defaults={
                'genero': genero,
                'url_youtube': item['url'],
                'descripcion': f"Interpretación emblemática de {item['artista']}."
            }
        )
        if created:
            print(f"Canción añadida: {item['cancion']}")
        else:
            print(f"Canción actualizada: {item['cancion']}")
            
    except Artista.DoesNotExist:
        print(f"Error: Artista {item['artista']} no encontrado.")

print("Proceso de carga de canciones finalizado.")

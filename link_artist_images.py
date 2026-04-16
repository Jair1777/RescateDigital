import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

# Map filenames to artist names
mapping = {
    "Benjamín Carrión.jpg": "Benjamín Carrión",
    "Carlos Bonilla Chávez.jpg": "Carlos Bonilla Chávez",
    "David Pacheco Ochoa.jpg": "David Pacheco Ochoa",
    "Emiliano Ortega Espinosa.jpg": "Emiliano Ortega Espinosa",
    "Manuel de Jesús Lozano.jpg": "Manuel de Jesús Lozano",
    "Salvador Bustamante Celi.jpg": "Salvador Bustamante Celi",
    "Segundo Cueva Celi.jpg": "Segundo Cueva Celi",
    "Segundo Luis Moreno.jpg": "Segundo Luis Moreno"
}

media_path = "artistas/"

for filename, artist_name in mapping.items():
    try:
        artista = Artista.objects.get(nombre=artist_name)
        artista.imagen_perfil = media_path + filename
        artista.save()
        print(f"Imagen vinculada para: {artist_name}")
    except Artista.DoesNotExist:
        print(f"Error: No se encontró al artista {artist_name} en la base de datos.")

print("Proceso de vinculación de imágenes finalizado.")

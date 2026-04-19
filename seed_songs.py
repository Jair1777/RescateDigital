import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from musica.models import GeneroMusical, Cancion
from artistas.models import Artista

songs_data = [
    ('Sigan Bailando', 'Marcos Ochoa Muñoz', 'Pasacalle', 'Un ritmo lleno de energía, ideal para mostrar la alegría de las fiestas lojanas.', 'https://www.youtube.com/watch?v=Fj-9LzZ5L7M'),
    ('Para tus ojos', 'Segundo Cueva Celi', 'Pasillo', 'Una de sus composiciones más románticas y técnicamente hermosas.', 'https://www.youtube.com/watch?v=HQfFPlpdYqo'),
    ('Linda Loja', 'Hermanos Quezada', 'Pasacalle', 'Un tema icónico que describe la belleza de la ciudad, muy usado en eventos cívicos.', 'https://www.youtube.com/watch?v=R95-X7zV_2k'),
    ('Los Huerfanitos', 'Manuel de Jesús Lozano', 'Pasacalle', 'Un clásico de las bandas de pueblo que compuso el \"Juglar de Loja\".', 'https://www.youtube.com/watch?v=W3A9p2S-Wv0'),
    ('Ojos Azules', 'David Pacheco Ochoa', 'Vals', 'Muestra la versatilidad de Pacheco Ochoa en ritmos más pausados y melódicos.', 'https://www.youtube.com/watch?v=ZtN_q-GkO9k'),
    ('El Minero', 'Dagoberto Vilela', 'Pasacalle', 'Un homenaje a los trabajadores de la región sur del Ecuador, con un ritmo contagioso.', 'https://www.youtube.com/watch?v=Dk-m5i8Z_tU'),
    ('Mosaico de Pasillos', 'Medardo Luzuriaga', 'Pasillo', 'Una excelente muestra de cómo los autores lojanos arreglaban música para orquestas.', 'https://www.youtube.com/watch?v=5U9jR6_X3oY'),
    ('Corazón que no olvida', 'Héctor Román', 'Pasillo', 'Un autor lojano menos mencionado pero con una sensibilidad exquisita.', 'https://www.youtube.com/watch?v=L2GkYl-M6L0'),
    ('Misa de la Coronación', 'Salvador Bustamante Celi', 'Música Sacra', 'Para mostrar su legado en la música religiosa de la Catedral de Loja.', 'https://www.youtube.com/watch?v=XhYn2V8W9A0'),
    ('Recuerdos de Amor', 'Tito Quinde', 'Pasillo', 'Representante de la generación de músicos que mantuvieron viva la tradición en la segunda mitad del siglo XX.', 'https://www.youtube.com/watch?v=vV7Y_9I5n0k'),
]

for title, artist_name, genre_name, desc, url in songs_data:
    genre, _ = GeneroMusical.objects.get_or_create(
        nombre=genre_name,
        defaults={
            'slug': genre_name.lower().replace(' ', '-'),
            'descripcion_historica': f'Género {genre_name}.',
            'caracteristicas_musicales': '...'
        }
    )
    
    artist, _ = Artista.objects.get_or_create(
        nombre=artist_name,
        defaults={
            'biografia': 'Artista lojano destacado.'
        }
    )
    
    cancion, created = Cancion.objects.get_or_create(
        titulo=title,
        genero=genre,
        defaults={
            'compositor': artist,
            'descripcion': desc,
            'url_youtube': url
        }
    )
    if not created:
        cancion.url_youtube = url
        cancion.descripcion = desc
        cancion.compositor = artist
        cancion.save()

print('Songs seeded successfully.')

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

data = [
    {
        "nombre": "Salvador Bustamante Celi",
        "composiciones": "Más de 100 obras. Obras destacadas: Los Coraceros, Ya viene el niñito, Loja, mi ciudad.",
        "obras_destacadas_resumen": "Destacan: Los Coraceros (Pasodoble), Ya viene el niñito (Villancico), Loja, mi ciudad (Pasillo)."
    },
    {
        "nombre": "Segundo Cueva Celi",
        "composiciones": "Más de 80 obras. Obras destacadas: Pequeña Ciudadana, Vaso de Lágrimas, Laura.",
        "obras_destacadas_resumen": "Destacan: Pequeña Ciudadana (Pasillo), Vaso de Lágrimas (Pasillo), Laura (Pasillo)."
    },
    {
        "nombre": "David Pacheco Ochoa",
        "composiciones": "Aproximadamente 100 obras. Obras destacadas: Vida Mía, El Chinchonal, Reír Llorando.",
        "obras_destacadas_resumen": "Destacan: Vida Mía (Pasillo), El Chinchonal (Pasacalle), Reir Llorando (Pasillo)."
    },
    {
        "nombre": "Daniel Armijos Carrión",
        "composiciones": "Cerca de 30 obras. Obras de referencia: Pasillo a Loja, Retazos de vida, Marcha a la Virgen de El Cisne.",
        "obras_destacadas_resumen": "Destacan: Pasillo a Loja, Retazos de vida, Marcha a la Virgen de El Cisne."
    },
    {
        "nombre": "Manuel de Jesús Lozano",
        "composiciones": "Más de 30 obras. Obras de referencia: Corazón que no olvida, Pasillo a mi madre, Amor y nostalgia.",
        "obras_destacadas_resumen": "Destacan: Corazon que no olvida, Pasillo a mi madre, Amor y nostalgia."
    },
    {
        "nombre": "Marcos Ochoa Muñoz",
        "composiciones": "Cerca de 30 obras. Obras destacadas: A orillas del Zamora, Pasillo Lojano, Recuerdos de mi tierra.",
        "obras_destacadas_resumen": "Destacan: A orillas del Zamora, Pasillo Lojano, Recuerdos de mi tierra."
    },
    {
        "nombre": "Francisco Rodas Bustamante",
        "composiciones": "Cerca de 30 obras. Obras destacadas: Himno a la Virgen, Marcha Fúnebre No. 1, Cantata Lojana.",
        "obras_destacadas_resumen": "Destacan: Himno a la Virgen, Marcha Funebre No. 1, Cantata Lojana."
    },
    {
        "nombre": "Emiliano Ortega",
        "composiciones": "Cerca de 30 obras. Obras destacadas: Pasillo a la mujer lojana, Canto a Loja, Melodía del sur.",
        "obras_destacadas_resumen": "Destacan: Pasillo a la mujer lojana, Canto a Loja, Melodia del sur."
    },
    {
        "nombre": "Julio Cañar",
        "composiciones": "Más de 30 obras. Obras destacadas: Rosas Lojanas, Pasacalle Lojano, Homenaje al maestro.",
        "obras_destacadas_resumen": "Destacan: Rosas Lojanas, Pasacalle Lojano, Homenaje al maestro."
    },
    {
        "nombre": "Víctor Moreno Proaño",
        "composiciones": "Cerca de 30 obras. Obras destacadas: Sinfonía Lojana, Pasillo de la tarde, Ecos del sur.",
        "obras_destacadas_resumen": "Destacan: Sinfonia Lojana, Pasillo de la tarde, Ecos del sur."
    }
]

for item in data:
    artista = Artista.objects.filter(nombre__iexact=item["nombre"]).first()
    if artista:
        artista.composiciones_resumen = item["composiciones"]
        # Update summarized box too
        artista.obras_destacadas_resumen = item["obras_destacadas_resumen"]
        artista.save()
        print(f"Actualizado: {item['nombre']}")

print("Carga de obras destacadas completada.")

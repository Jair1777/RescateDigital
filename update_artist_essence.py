import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

esencias = {
    "Salvador Bustamante Celi": """La Devoción
Su esencia es lo sagrado y lo institucional. Bustamante no solo escribía música; construía catedrales sonoras. Su espíritu era el de un arquitecto que buscaba elevar el espíritu humano hacia lo divino, ya fuera a través de un villancico sencillo o una misa compleja. Es la base sólida y formal de Loja.""",

    "Segundo Cueva Celi": """La Elegancia
Su esencia es el refinamiento. Cueva Celi era un aristócrata del sentimiento; tomaba la tristeza popular y la vestía de gala con armonías impresionistas. Su música no es para el ruido, sino para la escucha atenta. Representa la nostalgia culta y el perfeccionismo estético.""",

    "Manuel de Jesús Lozano": """La Bohemio-Sensibilidad
Su esencia es la cercanía. "El Juglar" no buscaba la complejidad técnica por encima del sentimiento, sino la conexión directa con el corazón. Su esencia es la de la serenata a medianoche, el romance honesto y la lealtad a los amigos. Es el alma humana en su estado más puro y sencillo.""",

    "Marcos Ochoa Muñoz": """La Disciplina
Su esencia es el apostolado docente. Marcos Ochoa entendía que el talento sin orden se pierde. Su espíritu era el de un guía que veía en cada joven lojano una semilla de arte. Representa la entrega desinteresada al crecimiento del otro y el respeto absoluto por la técnica musical.""",

    "Emiliano Ortega Espinosa": """El Paisajismo
Su esencia es la pertenencia. Ortega era un observador enamorado de su entorno. Su esencia es el color de los valles de Loja, el aroma de sus flores y la idiosincrasia de su gente. Él le dio palabras a la tierra para que la música tuviera un hogar donde descansar.""",

    "David Pacheco Ochoa": """El Vigor
Su esencia es la vitalidad. Mientras otros buscaban la introspección, Pacheco Ochoa buscaba el movimiento y la alegría colectiva. Representa la fuerza de la banda de pueblo, el brillo de las tompetas y la capacidad de la música para unir a una nación entera en un solo baile.""",

    "Carlos Bonilla Chávez": """La Innovación
Su esencia es la trascendencia. Bonilla Chávez era un visionario que no se conformaba con lo establecido. Su esencia es la del explorador que toma sus raíces andinas y las proyecta hacia el futuro y el mundo, demostrando que lo propio tiene una dignidad universal.""",

    "Segundo Luis Moreno": """La Verdad
Su esencia es la curiosidad científica. Moreno no se conformaba con escuchar; necesitaba entender el "por qué". Su espíritu es el del arqueólogo que desentierra sonidos olvidados para que el presente sepa de dónde viene. Es la conciencia histórica de nuestra música.""",

    "Benjamín Carrión": """La Esperanza
Su esencia es la grandeza espiritual. Carrión creía ciegamente en el poder de la belleza como defensa nacional. Su esencia es la convicción de que el arte es la única herramienta capaz de reconstruir la dignidad de un pueblo. Es el faro que ilumina y protege a todos los demás creadores."""
}

for nombre, texto in esencias.items():
    try:
        artista = Artista.objects.get(nombre=nombre)
        artista.esencia = texto
        artista.save()
        print(f"Esencia actualizada para: {nombre}")
    except Artista.DoesNotExist:
        print(f"Error: No se encontró al artista {nombre} en la base de datos.")

print("Proceso de actualización de esencias finalizado.")

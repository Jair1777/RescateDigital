import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

cronologias = {
    "Salvador Bustamante Celi": "El pionero. Su vida marca la transición del siglo XIX al XX, enfocándose en la música sacra y la creación de las primeras instituciones musicales de Loja. Es el pilar sobre el cual se sostiene toda la tradición posterior.",
    "Segundo Luis Moreno": "El investigador. Aunque contemporáneo de Bustamante, su enfoque fue la preservación histórica. Su vida larga le permitió documentar la música de casi tres siglos de historia ecuatoriana.",
    "David Pacheco Ochoa": "El embajador rítmico. Su carrera se desarrolló fuertemente en las bandas militares, siendo el responsable de que los ritmos lojanos (como el pasacalle) se volvieran populares en el norte del país y en la capital.",
    "Benjamín Carrión": "El ideólogo. Su aparición cronológica es clave, ya que su madurez intelectual coincidió con la necesidad de organizar el arte ecuatoriano, fundando la Casa de la Cultura en 1944.",
    "Emiliano Ortega Espinosa": "El poeta de la transición. Nace justo antes del cambio de siglo y se convierte en el puente entre la música clásica académica y la canción popular con letras profundamente regionales.",
    "Segundo Cueva Celi": "El renovador. Pertenece a la generación que modernizó el pasillo. Su obra se consolida en las décadas de 1920 y 1930, dándole a Loja su identidad musical más elegante.",
    "Manuel de Jesús Lozano": "El juglar eterno. Vivió casi todo el siglo XX, lo que le permitió ser el guardián de la bohemia lojana y ver cómo sus canciones se convertían en clásicos inmortales que se cantan hasta hoy.",
    "Marcos Ochoa Muñoz": "El formador. Su vida representa la etapa de consolidación educativa en Loja. Se encarga de que el legado de sus antecesores no se perdiera, enseñándolo en las aulas a las nuevas generaciones.",
    "Carlos Bonilla Chávez": "El virtuoso moderno. Es el más contemporáneo de la lista. Su cronología muestra la evolución hacia la guitarra de concierto y la internacionalización definitiva de los sonidos nacionales en escenarios clásicos."
}

for nombre, texto in cronologias.items():
    try:
        artista = Artista.objects.get(nombre=nombre)
        artista.obras_destacadas_resumen = texto
        artista.save()
        print(f"Cronología actualizada para: {nombre}")
    except Artista.DoesNotExist:
        print(f"Error: No se encontró al artista {nombre} en la base de datos.")

print("Proceso de actualización de cronologías finalizado.")

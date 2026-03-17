import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

nombres = [
    "Salvador Bustamante Cánovas",
    "Segundo Cueva Celi",
    "Manuel de J. Lozano",
    "Marcos Ochoa Muñoz",
    "Emiliano Ortega",
    "Víctor Moreno Proaño",
    "Daniel Armijos Carrión",
    "David Pacheco Ochoa",
    "Julio Cañar",
    "Francisco Rodas Bustamante"
]

bios = {
    "Salvador Bustamante Cánovas": "Destacado compositor lojano, conocido por su gran aporte a la música sacra y tradicional de la región.",
    "Segundo Cueva Celi": "Músico y compositor, prolífico creador de pasillos y yaravíes que son himnos populares en el sur del Ecuador.",
    "Manuel de J. Lozano": "Maestro de capilla y compositor, su obra trasciende en los géneros sacros y populares.",
    "Marcos Ochoa Muñoz": "Músico lojano de destacada trayectoria en la enseñanza y composición de piezas tradicionales.",
    "Emiliano Ortega": "Renombrado músico y educador ecuatoriano, parte fundamental de la identidad musical sureña.",
    "Víctor Moreno Proaño": "Compositor y promotor cultural, enriqueció el repertorio musical lojano con innumerables obras.",
    "Daniel Armijos Carrión": "Pianista y compositor cuyas obras evocan el paisaje romántico y bucólico de Loja.",
    "David Pacheco Ochoa": "Talentoso compositor y arreglista ecuatoriano de gran trascendencia histórica.",
    "Julio Cañar": "Referente de la música nacional que dejó un legado imborrable en el acervo popular lojano.",
    "Francisco Rodas Bustamante": "Músico multifacético y visionario que contribuyó al crecimiento de las bandas y agrupaciones de la época."
}

for nombre in nombres:
    artista, created = Artista.objects.get_or_create(
        nombre=nombre,
        defaults={'biografia': bios.get(nombre, "Biografía en construcción.")}
    )
    if created:
        print(f"Creado: {nombre}")
    else:
        print(f"Ya existe: {nombre}")

print("Proceso de carga de artistas finalizado.")

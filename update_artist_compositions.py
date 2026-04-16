import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

composiciones = {
    "Salvador Bustamante Celi": """- "Dulce Jesús Mío" (Villancico): Probablemente su obra más escuchada. Define la Navidad en todo el Ecuador.
- "Amor y Olvido" (Pasillo): Una de sus piezas románticas más logradas técnicamente.
- "El Huerfanito" (Pasacalle): Un clásico del repertorio popular.
- "Los Claveles" (Valse): Obra de gran elegancia para salones.
- "Misa de la Coronación de la Virgen del Cisne" (1930): Una obra sacra de gran envergadura compuesta para la coronación canónica de "La Churona".""",

    "Segundo Cueva Celi": """Fue un autor extremadamente prolífico, con más de 3,000 composiciones que elevaron el pasillo lojano.
- "Vaso de Lágrimas" (Pasillo): Su obra cumbre, con letra de José Ángel Buesa.
- "Pequeña Ciudadana" (Pasillo, 1925): Dedicada a la belleza de la mujer lojana.
- "Corazón que no olvida" (Pasillo): Un estándar del cancionero nacional.
- "Divagando en el Zamora" (Música descriptiva): Una pieza que evoca los paisajes de su ciudad.
- "Hacia el Ideal" (Himno): Obra que demuestra su capacidad para la música marcial y educativa.""",

    "Manuel de Jesús Lozano": """Sus temas son fundamentales en las serenatas lojanas.
- "Ya no te quiero, pero no te olvido" (Pasillo, 1935): Compuesta en Macará, es su obra más famosa a nivel internacional.
- "El Lojanito" (Sanjuanito, 1924): Escrita cuando solo tenía 16 años, mostrando su precocidad.
- "Traguito Lojano" (Pasacalle): El alma de las festividades locales.
- "Bajo el cielo de Loja" (Pasillo): Una oda a su tierra natal.""",

    "Marcos Ochoa Muñoz": """Destaca por su refinamiento en el piano y la armonización.
- "Nostalgias" (Pasillo): Una pieza de gran carga sentimental.
- "La Flor Zamorana" (Pasillo): Con letra de Alberto Zambrano, es un ícono del repertorio regional.
- "Imploración" (Pasillo): Famosa por sus arreglos de cuerda.
- "Acuérdate de mí" (Pasillo): Una de las más interpretadas por tríos y solistas.""",

    "Emiliano Ortega Espinosa": """Aunque fue un gran literato, sus composiciones musicales son fundamentales.
- "Española" (Pasillo): Letra y música que evocan la herencia cultural.
- "Lojanita" (Pasacalle): Una de las canciones más alegres y representativas de la ciudad.
- "El Alma en los labios" (Versión): Realizó importantes arreglos y difusiones de textos poéticos musicalizados.""",

    "David Pacheco Ochoa": """El maestro de los ritmos vibrantes y las bandas de pueblo.
- "El Chulla Quiteño" (Pasacalle, 1946): Su obra más famosa, considerada el himno popular de la capital de Ecuador.
- "Sangre Lojana" (Pasacalle): Un tributo a sus raíces.
- "Ojos Azules" (Vals): Una composición que destaca por su dulzura melódica.""",

    "Carlos Bonilla Chávez": """Revolucionó la guitarra clásica con ritmos nacionales.
- "Cantares de mi Tierra" (Suite para guitarra): Una serie de piezas que adaptan el pasillo y el aire típico a la guitarra de concierto.
- "Atahualpa" (Yumbo): Una obra que explora las raíces prehispánicas.
- "Poncho Andino" (Danza): Fusión de técnica clásica con ritmos andinos.""",

    "Segundo Luis Moreno": """Más allá de sus composiciones, su legado es la documentación.
- "La Campaña de Ambato" (Marcha): Una de sus obras marciales más conocidas.
- "Cantos Indígenas" (Recopilación/Arreglo): Transcribió y armonizó cientos de melodías ancestrales.
- "Suite Ecuatoriana" (Música de cámara): Obra que busca dar una estructura clásica a temas criollos.""",

    "Benjamín Carrión": """Como indicamos antes, él no fue compositor musical, pero su "obra" principal es institucional:
- Fundación de la Casa de la Cultura Ecuatoriana (1944): El espacio que permitió que todas las composiciones anteriores se grabaran, editaran y preservaran.
- "Cartas al Ecuador" (1943): Ensayo donde plantea la necesidad de fortalecer la identidad artística nacional."""
}

for nombre, texto in composiciones.items():
    try:
        artista = Artista.objects.get(nombre=nombre)
        artista.composiciones_resumen = texto
        artista.save()
        print(f"Composiciones actualizadas para: {nombre}")
    except Artista.DoesNotExist:
        print(f"Error: No se encontró al artista {nombre} en la base de datos.")

print("Proceso de actualización de composiciones finalizado.")

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

legados = {
    "Salvador Bustamante Celi": """El Arquitecto de la Identidad Musical
Su legado es la institucionalización. No solo compuso música, sino que creó las estructuras para que Loja fuera una potencia artística.

- La Navidad Ecuatoriana: Definió la sonoridad de la Navidad en todo el país. Sin sus villancicos, la estética religiosa del Ecuador sería completamente distinta.
- Formación Académica: Al fundar la primera orquesta y sentar las bases del conservatorio, permitió que el talento empírico lojano se transformara en conocimiento académico.""",

    "Segundo Cueva Celi": """El Poeta del Piano y la Nostalgia
Su legado es la sofisticación del pasillo.

- Evolución del Género: Elevó el pasillo de una canción popular de cantina o salón a una pieza de concierto con armonías complejas influenciadas por el romanticismo europeo (Chopin).
- Identidad Lojana: Logró que el pasillo de Loja se diferenciara del resto del país por su aire más melancólico, culto y técnicamente exigente.""",

    "Manuel de Jesús Lozano": """El Guardián de la Bohemia
Su legado es el romanticismo puro y la cercanía popular.

- El Cancionero Popular: Sus obras son el alma de la serenata lojana. Representa la transición perfecta entre el músico de academia y el músico del pueblo.
- Preservación: Su archivo personal "Mi tesoro artístico" es una de las fuentes documentales más valiosas para entender la evolución de la música local en el siglo XX.""",

    "Marcos Ochoa Muñoz": """El Maestro de Generaciones
Su legado es la docencia y la técnica.

- Educación Musical: Dedicó su vida a formar a los nuevos talentos en el Colegio Bernardo Valdivieso y el Conservatorio. Muchos de los músicos actuales de Loja son "nietos" musicales de su enseñanza.
- Perfeccionismo: Impuso un estándar de excelencia en la ejecución de instrumentos como el piano y el acordeón.""",

    "Emiliano Ortega Espinosa": """El Vínculo entre Letra y Sonido
Su legado es la poética de la tierra.

- Paisajismo Musical: A través de sus letras, inmortalizó la geografía y las costumbres de Loja. Hizo que el lojano se sintiera orgulloso de su entorno a través del canto.
- Intelectualidad Activa: Demostró que el artista también debe ser un ciudadano comprometido con la gestión cultural y política de su ciudad.""",

    "David Pacheco Ochoa": """El Embajador del Ritmo
Su legado es la nacionalización de la música lojana.

- Exportación Cultural: Al dirigir bandas militares en todo el país, llevó el estilo compositivo lojano a cada rincón del Ecuador.
- El Pasacalle como Símbolo: Con "El Chulla Quiteño", demostró que un compositor lojano podía interpretar y definir el alma de otras ciudades, unificando la identidad nacional.""",

    "Carlos Bonilla Chávez": """El Revolucionario de la Guitarra
Su legado es la universalización de los ritmos andinos.

- La Guitarra de Concierto: Sacó a la guitarra de su rol de simple acompañante y la convirtió en un instrumento solista de primer nivel.
- Dignificación de lo Indígena: Fue de los primeros en llevar ritmos como el yumbo o el danzante a las partituras clásicas, dándoles un valor estético global.""",

    "Segundo Luis Moreno": """El Científico de la Música
Su legado es la memoria histórica.

- Etnomusicología: Fue el primer ecuatoriano en estudiar la música con rigor científico. Gracias a él, sabemos cómo sonaba la música prehispánica y colonial.
- Rescate Documental: Sin sus libros, la historia de la música en Ecuador sería un conjunto de mitos sin fundamento técnico.""",

    "Benjamín Carrión": """El Ideólogo de la Nación-Cultura
Su legado es la protección y difusión del arte.

- La Casa de la Cultura: Creó el "hogar" para todos los artistas mencionados. Su idea de que Ecuador debe ser una potencia cultural es lo que justifica que hoy sigamos rescatando este legado.
- Autoestima Nacional: Cambió la narrativa del país, pasando de la derrota territorial a la victoria intelectual."""
}

for nombre, texto in legados.items():
    try:
        artista = Artista.objects.get(nombre=nombre)
        artista.legado_resumen = texto
        artista.save()
        print(f"Legado actualizado para: {nombre}")
    except Artista.DoesNotExist:
        print(f"Error: No se encontró al artista {nombre} en la base de datos.")

print("Proceso de actualización de legados finalizado.")

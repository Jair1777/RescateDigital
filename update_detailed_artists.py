import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

data = {
    "Dagoberto Vilela": {
        "esencia": "Su esencia reside en el fervor telúrico. Vilela no solo escribía música; él \"pintaba\" los paisajes de la provincia con sonidos. Tenía la capacidad única de transformar el sentimiento de pertenencia a una tierra en un ritmo bailable y vibrante. Es el compositor que logró que el lojano, al escuchar un pasacalle, sintiera que su hogar era el centro del universo.",
        "biografia": "Nacido en el corazón de una Loja que empezaba a conectarse con el resto del país, Vilela se formó en la escuela del día a día, en contacto directo con las bandas municipales y los músicos de retreta. Su carrera fue una constante búsqueda por dignificar los ritmos populares. A diferencia de los músicos puramente académicos, Dagoberto se sumergió en la cultura del pueblo, entendiendo que la música debía ser una herramienta de unidad social. Recorrió la provincia recopilando vivencias que luego transformaría en partituras inmortales.",
        "obras_destacadas_resumen": "Desarrolló su obra en un periodo de consolidación del Estado-Nación ecuatoriano (mediados del siglo XX). En este tiempo, las provincias buscaban símbolos propios para diferenciarse. Loja, al estar geográficamente aislada, encontró en la música de Vilela una forma de decir \"aquí estamos\". Sus composiciones surgieron en el auge del nacionalismo, donde el pasacalle se convirtió en el ritmo de la resistencia y el orgullo regional frente a la centralización de Quito o Guayaquil.",
        "composiciones_resumen": "Su obra maestra indiscutible es \"Tierras Lojanas\", un pasacalle que por su estructura y letra es coreado como un himno oficial. También legó \"El Minero\", una pieza que rinde tributo al duro trabajo en los yacimientos del sur, y \"Linda Lojanita\", donde explora la lírica romántica fusionada con el ritmo festivo.",
        "legado_resumen": "Vilela dejó un legado de patriotismo sonoro. Gracias a él, el pasacalle lojano adquirió una estructura definida y una temática centrada en el paisaje y el honor. Su música es el pegamento cultural que une a los cantones de la provincia, siendo estudiada hoy como el ejemplo perfecto de \"música con identidad\"."
    },
    "Hermanos Quezada": {
        "esencia": "Su esencia es la perfección del empaste. En ellos, la música no es una competencia de solistas, sino una comunión de voces. Representan la elegancia del salón lojano llevada al formato de dúo y trío. Su espíritu es el de la serenata culta, donde cada nota está fríamente calculada para conmover sin perder la compostura técnica.",
        "biografia": "Este grupo familiar nació bajo la influencia directa de la gran escuela de cuerdas de Loja. Desde muy jóvenes, los Hermanos Quezada demostraron una disciplina casi militar en el estudio de la guitarra y la armonización vocal. Su trayectoria los llevó a las principales radiodifusoras del país en una época donde la radio era el único vínculo cultural de la nación. No solo fueron intérpretes de sus propias obras, sino que se convirtieron en los \"curadores\" de la música lojana, seleccionando y grabando versiones definitivas de temas de otros autores, dándoles un sello de calidad que hasta hoy es difícil de superar.",
        "obras_destacadas_resumen": "Vivieron la transición de la música interpretada en vivo en los portales de las casas hacia la industria del disco de acetato. Su auge coincide con la \"Época de Oro del Pasillo\" en Ecuador. En un momento donde la influencia extranjera (como el tango o el bolero) era fuerte, los Hermanos Quezada defendieron la pureza de la cuerda y la voz ecuatoriana, manteniendo a Loja como el bastión de la resistencia musical tradicional.",
        "composiciones_resumen": "Son los creadores del icónico tema \"Linda Loja\", una canción que sobrepasó las fronteras provinciales para convertirse en un referente del catálogo nacional. Además, sus composiciones instrumentales para guitarra demuestran una técnica depurada que fusiona lo popular con lo clásico.",
        "legado_resumen": "Su legado es el canon del dúo lojano. Establecieron los parámetros de cómo se debe arreglar una voz segunda y cómo debe sonar una guitarra de acompañamiento en el pasillo y el pasacalle. Son la referencia obligada para cualquier trío moderno que desee interpretar música nacional con respeto y altura."
    },
    "Héctor Román": {
        "esencia": "Su esencia es la melancolía intelectual. Román no escribía para la masa, sino para el individuo que sufre y ama en silencio. Su música tiene una carga filosófica; es el pensamiento lojano transformado en intervalos musicales. Es la esencia de la \"Loja Culta\", aquella que encuentra belleza en la tristeza y profundidad en la sencillez de una melodía.",
        "biografia": "Héctor Román fue un estudioso incansable de la teoría musical. Su vida fue un apostolado hacia la belleza estética. A pesar de tener el talento para brillar en escenarios internacionales, prefirió la vida de compositor y pedagogo, influyendo silenciosamente en cientos de músicos. Su trayectoria está marcada por una producción constante pero selecta, donde cada obra pasaba por un riguroso proceso de revisión antes de ser entregada al público. Fue un músico de músicos, respetado por su capacidad para armonizar de formas que sorprendían incluso a los más académicos.",
        "obras_destacadas_resumen": "Su obra se desarrolla en un periodo de introspección para las artes en Ecuador, tras los conflictos fronterizos y sociales de mediados de siglo. En este contexto, la música de Román sirvió como un bálsamo, una forma de refugio intelectual que buscaba la paz a través de la armonía. Representa la resistencia de la música \"de cámara\" frente a la creciente comercialización de los ritmos tropicales.",
        "composiciones_resumen": "Destaca su pasillo \"Corazón que no olvida\", una pieza que utiliza progresiones armónicas inusuales para la época. Sus obras para piano y voz son consideradas \"lieders lojanos\" por su similitud con la canción artística europea, pero con el alma innegablemente andina.",
        "legado_resumen": "El legado de Román es la sofisticación de la raíz. Nos enseñó que el pasillo puede ser tan complejo como una sonata y que la música popular no debe ser sinónimo de música simple. Dejó un estándar de excelencia compositiva que obliga a los nuevos autores a estudiar música en profundidad antes de pretender escribir un tema nacional."
    },
    "Medardo Luzuriaga": {
        "esencia": "Su esencia es el dinamismo universal. Don Medardo fue el puente entre el conservatorio y la plaza pública. Tenía el \"oído absoluto\" para entender qué hacía vibrar al pueblo ecuatoriano. Su espíritu era de una alegría inagotable, pero siempre sustentada en un conocimiento técnico feroz. Es la prueba viviente de que Loja puede exportar alegría rítmica al mundo entero.",
        "biografia": "Lojano de pura cepa, se formó en el Conservatorio Nacional de Música. Su destreza con el saxofón y el piano era legendaria antes de fundar su orquesta. En 1967, dio el paso que cambiaría la historia de la música ecuatoriana: fundó \"Don Medardo y sus Player’s\". A partir de ahí, su trayectoria fue un ascenso meteórico, grabando más de un centenar de discos y convirtiéndose en el artista ecuatoriano que más ha hecho bailar al país. Su éxito no fue casualidad, sino producto de su capacidad para arreglar ritmos lojanos con instrumentos de viento-metal, dándoles una potencia nunca antes vista.",
        "obras_destacadas_resumen": "Vivió el auge de las \"Big Bands\" y la llegada de la cumbia a Sudamérica. Don Medardo supo leer el cambio de época: el paso de la sociedad rural a la urbana. Su música fue la banda sonora de la modernización de Ecuador, de las grandes fiestas populares en las calles y de la consolidación de la identidad mestiza que abraza tanto el pasacalle como la música tropical.",
        "composiciones_resumen": "Aunque su fuerte fue el arreglo y la dirección, sus temas icónicos como \"Cumbia Chonera\", \"El Aguacerito\" y sus mosaicos de pasillos y pasacalles lojanos orquestados, son piezas fundamentales de la cultura popular.",
        "legado_resumen": "Su legado es la globalización de la sonoridad lojana. Sacó a los ritmos de Loja de la pequeña sala de cuerdas y los puso en los escenarios más grandes de América. Demostró que la formación lojana es tan sólida que puede dominar cualquier género, desde lo clásico hasta lo tropical, convirtiéndose en el máximo referente de la orquesta bailable en el país."
    },
    "Tito Quinde": {
        "esencia": "Su esencia es la fidelidad histórica. Quinde es el guardián de las llaves del pasado. Su espíritu es el de un restaurador de arte: toma las canciones que el tiempo amenaza con borrar y les devuelve el brillo original, pero con una técnica moderna. Representa la constancia y la humildad del artista que pone su talento al servicio del legado de sus antepasados.",
        "biografia": "Tito Quinde ha sido una figura omnipresente en el quehacer musical lojano de las últimas décadas. Su trayectoria se ha desarrollado entre la dirección de coros, orquestas y conjuntos de cámara. Se ha especializado en el rescate de partituras olvidadas de los grandes maestros como Bustamante Celi o Cueva Celi, realizando arreglos que permiten que estas obras sean interpretadas por músicos contemporáneos. Su vida es un testimonio de servicio a la ciudad de Loja, siendo un gestor cultural activo que no permite que el silencio gane la batalla a la memoria.",
        "obras_destacadas_resumen": "Su labor es crucial en el siglo XXI, una era de gratificación instantánea y música desechable. En este contexto, Quinde actúa como un contrapunto necesario, recordando a la sociedad que una cultura sin memoria musical está condenada a perder su alma. Representa el esfuerzo por mantener a Loja como \"Capital Musical\" en un entorno globalizado.",
        "composiciones_resumen": "Su obra \"Recuerdos de Amor\" es una pieza de una ternura técnica envidiable. También ha compuesto numerosas obras de carácter religioso y cívico que se interpretan en las festividades de la Virgen del Cisne, manteniendo viva la tradición de la música sacra lojana.",
        "legado_resumen": "El legado de Tito Quinde es el archivo vivo. Gracias a él, el repertorio lojano no se ha estancado; ha seguido evolucionando sin perder su esencia. Su mayor contribución es haber formado y guiado a grupos de jóvenes, transmitiéndoles no solo la técnica, sino el amor y el respeto por el patrimonio sonoro de su tierra."
    }
}

for name, info in data.items():
    try:
        a = Artista.objects.get(nombre=name)
        a.esencia = info['esencia']
        a.biografia = info['biografia']
        a.obras_destacadas_resumen = info['obras_destacadas_resumen'] # Used for Contexto Historico
        a.composiciones_resumen = info['composiciones_resumen']
        a.legado_resumen = info['legado_resumen']
        a.save()
        print(f"Detailed bio updated for {name}")
    except Exception as e:
        print(f"Error on {name}: {e}")

# Copy to English and French fields to not break template languages
for a in Artista.objects.all():
    name = a.nombre
    if name in data:
        for f in ['esencia', 'biografia', 'obras_destacadas_resumen', 'composiciones_resumen', 'legado_resumen']:
            setattr(a, f + '_en', getattr(a, f))
            setattr(a, f + '_fr', getattr(a, f))
        a.save()

print("All artist bios fully detailed and synced across languages!")

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

nombres = [
    "Salvador Bustamante Celi",
    "Segundo Cueva Celi",
    "Manuel de Jesús Lozano",
    "Marcos Ochoa Muñoz",
    "Emiliano Ortega Espinosa",
    "David Pacheco Ochoa",
    "Carlos Bonilla Chávez",
    "Segundo Luis Moreno",
    "Benjamín Carrión"
]

bios = {
    "Salvador Bustamante Celi": """Nació en Loja el 10 de marzo de 1876. Inició sus estudios en la escuela de los Hermanos Cristianos, donde su talento musical fue detectado tempranamente por el maestro Miguel Cabrera. Gracias a una beca del Cabildo lojano en 1889, viajó a Quito para estudiar en la Escuela de Artes y Oficios de los Salesianos; aunque inicialmente fue para aprender talabartería, los religiosos rápidamente lo integraron a la estudiantina al ver su destreza innata.

Su carrera tomó un rumbo internacional en 1906 cuando se radicó en Lima, Perú. Allí perfeccionó sus conocimientos en armonía, contrapunto y fuga, llegando a ser el organista de la Catedral de Lima. Regresó a Ecuador en 1910 debido al conflicto fronterizo, estableciéndose primero en Guayaquil —donde fue organista en la iglesia de San Francisco— y finalmente regresando a su natal Loja. Fue un músico de una versatilidad asombrosa: compuso desde marchas militares y fúnebres hasta los villancicos más populares del país. Falleció el 8 de marzo de 1935, dejando un vacío inmenso pero un legado institucional que culminó en la creación del conservatorio que hoy lleva su nombre.""",

    "Segundo Cueva Celi": """Nacido en Loja el 10 de enero de 1901, Segundo Cueva Celi es quizás el músico más representativo del "sentir" lojano. Proveniente de una familia de músicos (sobrino de Salvador Bustamante Celi), fue un niño prodigio que a los ocho años ya realizaba presentaciones públicas. Aprendió de forma autodidacta la guitarra y el rondín antes de recibir formación formal con los Hermanos Cristianos y, posteriormente, con su tío Salvador.

A los 15 años fundó el "Sexteto Loja" y a los 17 ya componía música religiosa. Su genialidad radicaba en la renovación del pasillo, dotándolo de una estructura armónica más compleja influenciada por su admiración hacia Chopin (específicamente en sus valses y nocturnos). A lo largo de su vida, desempeñó cargos como profesor de canto en escuelas fiscales, miembro fundador de la Casa de la Cultura Núcleo de Loja y docente en la Escuela Superior de Música. Recibió la Medalla al Mérito en grado de Caballero por parte del Gobierno Nacional antes de fallecer en Quito el 17 de abril de 1969. Se estima que su obra supera las 3,000 composiciones.""",

    "Manuel de Jesús Lozano": """Conocido como el "Juglar de Loja", nació el 30 de diciembre de 1908. Su historia es la de una pasión indomable: a los ocho años ya dominaba el bandolín y la guitarra. Al observar esto, su madre pidió a Salvador Bustamante Celi que lo tomara como discípulo. Bajo su tutela, Lozano eligió el violín como su instrumento principal, convirtiéndose en un intérprete prodigioso que lograba una "transparencia del alma" en cada ejecución.

A pesar de su inmensa carrera musical, Lozano mantuvo una vida profesional activa en el sector público, trabajando en el Telégrafo y en el Banco Nacional de Fomento como radio-operador. Sin embargo, su tiempo libre lo dedicaba enteramente a la composición en su archivo privado que llamó "Mi tesoro artístico". En 1935, mientras se encontraba en Macará, compuso la música para el poema de su amigo José Ruiz: el inmortal pasillo "Ya no te quiero, pero no te olvido". Su música se caracteriza por una profunda solidaridad humana y un romanticismo puro. Falleció el 23 de abril de 1994, siendo recordado como uno de los compositores más sensibles de la provincia.""",

    "Marcos Ochoa Muñoz": """Nacido en Loja el 21 de mayo de 1918, Ochoa Muñoz representó la excelencia técnica y académica. Fue alumno de Segundo Cueva Celi en Loja y luego se trasladó al Conservatorio Nacional en Quito para estudiar con maestros como Pedro Noroña. Su dominio del acordeón y el piano le permitió crear composiciones que fusionaban lo popular con lo docto de una manera excepcional.

Fue un pilar fundamental en la educación musical, ejerciendo la docencia en el Colegio Bernardo Valdivieso y en el Conservatorio Salvador Bustamante Celi. Su obra es variada: desde misas y marchas triunfales hasta los pasillos nostálgicos que hoy son himnos culturales para los lojanos. Uno de sus hitos más recordados es la colaboración con Alberto Zambrano para la creación de "La Flor Zamorana", una pieza que capturó la esencia del paisaje y la identidad local. Su legado no solo vive en sus partituras, sino también en el parque y monumento que Loja erigió en su honor, reconociéndolo como un maestro que formó a generaciones enteras de nuevos músicos.""",

    "Emiliano Ortega Espinosa": """Nacido en Loja el 8 de febrero de 1898, fue un personaje polifacético: poeta, músico, periodista y político. Se le considera uno de los intelectuales más influyentes de su generación. Inició sus estudios en el Colegio Bernardo Valdivieso, donde brotó su amor por las letras y la música. Su formación musical fue autodidacta en gran medida, aunque perfeccionó su técnica rodeado de la élite intelectual de la época.

Ortega fue un maestro en capturar la identidad lojana en versos. Fue el autor de las letras de canciones emblemáticas como el pasillo "Española" y el pasacalle "Lojanita", piezas que se convirtieron en himnos populares. Además de su labor artística, sirvió a su ciudad como Concejal y Presidente del Municipio de Loja, y fue un miembro activo de la Casa de la Cultura Ecuatoriana. Su legado reside en haber fusionar la poesía culta con el sentimiento popular, logrando que sus letras trascendieran los salones para ser cantadas por todo el pueblo.""",

    "David Pacheco Ochoa": """Este destacado compositor y director de bandas nació en Loja el 29 de diciembre de 1888. Fue un músico que entendió como pocos la importancia de la música festiva y comunitaria. Se desempeñó como director de bandas militares en diversas provincias del país, lo que le permitió difundir el estilo musical lojano por todo el territorio nacional.

Su obra más famosa es, sin duda, el pasacalle "El Chulla Quiteño", una pieza que, aunque dedicada a la capital, fue compuesta por este lojano de cepa y se ha convertido en el segundo himno de Quito. Pacheco Ochoa fue un prolífico creador de pasillos, pasacalles y valses, caracterizados por una alegría contagiosa y una estructura rítmica impecable. Su legado es vital para entender la música de banda en Ecuador, elevando el nivel de estas agrupaciones y dotándolas de un repertorio nacionalista de alta calidad.""",

    "Carlos Bonilla Chávez": """Aunque nació en Quito, su vínculo con la música nacional y su influencia en el ámbito académico lo hacen indispensable en esta lista. Fue un guitarrista y compositor de formación académica rigurosa que revolucionó la guitarra clásica en Ecuador. Estudió en el Conservatorio Nacional de Música y se especializó en el contrabajo, pero fue su maestría con las seis cuerdas la que le dio fama internacional.

Bonilla Chávez fue el fundador de la cátedra de Guitarra en el Conservatorio Nacional, formando a las primeras generaciones de guitarristas profesionales del país. Como compositor, logró algo histórico: escribir obras para guitarra clásica basadas en ritmos autóctonos como el yaraví, el yumbo y el pasillo (por ejemplo, su famosa "Cantares de mi Tierra"). Su legado es la elevación de la música popular ecuatoriana a los escenarios de concierto más prestigiosos del mundo, demostrando que nuestros ritmos poseen una complejidad técnica y estética digna de la música universal.""",

    "Segundo Luis Moreno": """Nacido en Cotacachi, es considerado el padre de la musicología en Ecuador. Su vida fue una incansable investigación sobre los orígenes y la estructura de la música indígena y mestiza. Fue director de bandas militares y de los conservatorios de Quito, Cuenca y Guayaquil. Su formación fue rigurosa, pero su verdadera pasión fue el trabajo de campo.

Su obra cumbre es la monumental "Historia de la Música en el Ecuador", una investigación detallada que por primera vez organizó científicamente el conocimiento musical del país. Además de su labor como historiador, compuso numerosas obras sinfónicas y música de cámara. Su legado es la base sobre la cual se asienta todo estudio serio de la música ecuatoriana actual; sin su esfuerzo de recopilación y análisis, gran parte de nuestra herencia sonora prehispánica y colonial se habría perdido para siempre.""",

    "Benjamín Carrión": """Nacido en Loja el 20 de abril de 1897, Carrión no fue un compositor de música, pero es el arquitecto del "Ecuador como potencia cultural". Diplomático, escritor y ensayista, es una de las figuras más importantes de la historia intelectual del país. Su visión era clara: si Ecuador no podía ser una potencia militar o económica, debía ser una "Nación Pequeña, pero de Gran Cultura".

En 1944 fundó la Casa de la Cultura Ecuatoriana, la institución más relevante para el fomento de las artes en el país. Fue un promotor incansable de los artistas lojanos y nacionales, asegurándose de que la música, la pintura y la literatura tuvieran espacios de difusión dignos. Su legado es el marco institucional y filosófico que permitió que figuras como las mencionadas anteriormente fueran reconocidas y valoradas. Como autor de obras como "Atahualpa" y "San Miguel de Unamuno", dejó una huella imborrable en el pensamiento latinoamericano."""
}

for nombre in nombres:
    artista, created = Artista.objects.update_or_create(
        nombre=nombre,
        defaults={'biografia': bios.get(nombre, "Biografía en construcción.")}
    )
    if created:
        print(f"Creado: {nombre}")
    else:
        print(f"Actualizado: {nombre}")

print("Proceso de carga de artistas finalizado.")

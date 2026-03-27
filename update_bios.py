import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

data = [
    {
        "nombre": "Salvador Bustamante Celi",
        "aliases": ["Salvador Bustamante Cánovas", "Salvador Bustamante Celi"],
        "biografia": "Salvador Bustamante Celi nació el 1 de marzo de 1876 en Loja, Ecuador, y falleció en 1935. Es considerado uno de los músicos más importantes del país y una figura clave en el desarrollo de la música académica ecuatoriana. Desde temprana edad mostró talento musical, lo que lo llevó a formarse y dedicarse plenamente a la composición y enseñanza.\n\nA lo largo de su vida realizó más de 100 composiciones, abarcando géneros como la música religiosa, sinfónica y popular. Entre sus obras destacan villancicos, cantatas y piezas litúrgicas que fueron interpretadas en iglesias y eventos importantes. Su estilo combinaba influencias europeas con elementos propios de la identidad lojana.\n\nAdemás de su trabajo como compositor, desempeñó un papel fundamental como educador musical, formando a varias generaciones de artistas. Fundó instituciones y promovió la enseñanza formal de la música en Loja, lo que marcó un antes y un después en la cultura local.\n\nSu legado cultural es enorme, ya que sentó las bases para que Loja sea reconocida como la Capital Musical del Ecuador. Su influencia se mantiene vigente en conservatorios, escuelas y en la tradición musical de la región.",
        "periodo_vida": "1 de marzo de 1876 – 1935",
        "composiciones": "Más de 100 obras entre música religiosa, académica y popular",
        "obras_destacadas": "Cantatas, villancicos, obras religiosas y piezas sinfónicas",
        "legado": "Sentó las bases de la música en Loja, formando generaciones de músicos y contribuyendo a que la ciudad sea reconocida como la Capital Musical del Ecuador."
    },
    {
        "nombre": "Segundo Cueva Celi",
        "biografia": "Segundo Cueva Celi nació el 10 de enero de 1901 en Loja y falleció en 1969. Fue uno de los más destacados compositores del pasillo ecuatoriano, género que representa profundamente la identidad cultural del país. Desde joven mostró una gran sensibilidad artística y vocación por la música.\n\nDurante su trayectoria compuso más de 80 obras, principalmente pasillos y canciones románticas. Entre sus composiciones más reconocidas se encuentran Pequeña ciudadana, Vaso de lágrimas y Laura, piezas que han trascendido generaciones por su profundidad emocional y belleza melódica.\n\nSu música se caracteriza por expresar sentimientos de amor, nostalgia y melancolía, elementos propios del pasillo lojano. Gracias a su talento, logró posicionarse como uno de los referentes más importantes de este género a nivel nacional.\n\nEl legado cultural de Segundo Cueva Celi es fundamental, ya que consolidó el pasillo lojano como uno de los géneros más representativos del Ecuador. Su influencia continúa vigente en músicos contemporáneos y en la tradición cultural del país.",
        "periodo_vida": "10 de enero de 1901 – 1969",
        "composiciones": "Más de 80 pasillos y canciones",
        "obras_destacadas": "Pequeña ciudadana, Vaso de lágrimas, Laura",
        "legado": "Consolidó el pasillo lojano como género representativo del Ecuador, influyendo en músicos posteriores."
    },
    {
        "nombre": "David Pacheco Ochoa",
        "biografia": "David Pacheco Ochoa nació el 14 de diciembre de 1920 en Loja, Ecuador. Fue un destacado compositor, director musical y educador que dedicó gran parte de su vida a la promoción y enseñanza de la música en su ciudad natal.\n\nA lo largo de su carrera compuso aproximadamente 100 obras, incluyendo pasillos, marchas e himnos institucionales. Su producción musical refleja tanto la tradición lojana como su compromiso con la formación de nuevas generaciones de músicos.\n\nAdemás de su trabajo como compositor, tuvo una importante labor como docente, contribuyendo a la educación musical de muchos jóvenes. Su participación en instituciones culturales fortaleció el desarrollo artístico de la región.\n\nSu legado cultural radica en la difusión de la música lojana y en la formación de nuevos talentos. Gracias a su trabajo, la música de Loja continuó evolucionando y manteniendo su relevancia a nivel nacional.",
        "periodo_vida": "14 de diciembre de 1920 – (no registrado)",
        "composiciones": "Aproximadamente 100 obras",
        "obras_destacadas": "Pasillos, marchas, himnos institucionales",
        "legado": "Su trabajo fortaleció la educación musical y ayudó a difundir la música lojana en el país."
    },
    {
        "nombre": "Daniel Armijos Carrión",
        "biografia": "Daniel Armijos Carrión fue un musician lojano del siglo XX, aunque no se cuenta con registros exactos de su fecha de nacimiento ni de su fallecimiento. Formó parte de la tradición musical de Loja, participando activamente en el desarrollo cultural de la ciudad.\n\nSe destacó principalmente en la composición de música para bandas y en la creación de pasillos, contribuyendo a mantener viva la identidad musical de la región. Sus obras fueron interpretadas en eventos culturales y festividades locales.\n\nSu trabajo se enmarca dentro de una generación de músicos que fortalecieron la música popular lojana, asegurando su continuidad a lo largo del tiempo. Su participación fue clave en agrupaciones musicales tradicionales.\n\nEl legado cultural de Armijos Carrión radica en su aporte a la música comunitaria y en la preservación de las tradiciones musicales de Loja, siendo parte importante del patrimonio cultural de la provincia.",
        "periodo_vida": "No documentado con exactitud",
        "composiciones": "Varias obras (principalmente para bandas)",
        "obras_destacadas": "Pasillos y música instrumental",
        "legado": "Ayudó a mantener viva la tradición musical lojana en agrupaciones populares."
    },
    {
        "nombre": "Manuel de Jesús Lozano",
        "aliases": ["Manuel de J. Lozano"],
        "biografia": "Manuel de Jesús Lozano fue un compositor lojano del siglo XX, del cual no se tienen datos precisos sobre su nacimiento y fallecimiento. Sin embargo, su nombre se mantiene vigente dentro de la historia musical de Loja por su aporte al desarrollo del pasillo.\n\nDurante su trayectoria realizó varias composiciones que se integraron al repertorio musical tradicional de la región. Sus obras reflejan las características propias del pasillo lojano, como la melancolía y el romanticismo.\n\nFormó parte de una generación de músicos que consolidaron la música popular en Loja, contribuyendo a su difusión y permanencia en la cultura local. Su trabajo ayudó a fortalecer la identidad musical de la ciudad.\n\nSu legado cultural se encuentra en la continuidad del pasillo como expresión artística representativa del Ecuador, siendo parte del proceso que convirtió a Loja en un centro musical importante.",
        "periodo_vida": "No registrado",
        "composiciones": "Varias obras dentro del pasillo",
        "obras_destacadas": "Música popular lojana",
        "legado": "Contribuyó a consolidar el estilo musical lojano como símbolo cultural."
    },
    {
        "nombre": "Marcos Ochoa Muñoz",
        "biografia": "Marcos Ochoa Muñoz fue un compositor lojano del siglo XX, reconocido por su participación en la creación y difusión de la música tradicional de la región. Aunque no se dispone de fechas exactas de su vida, su aporte es ampliamente valorado.\n\nCompuso diversas obras dentro del género del pasillo y otras formas musicales populares. Sus composiciones reflejan la identidad cultural lojana y fueron interpretadas en distintos espacios artísticos.\n\nSu trabajo contribuyó al fortalecimiento del repertorio musical de Loja, siendo parte de una generación que impulsó la música como elemento clave de la cultura local.\n\nEl legado cultural de Marcos Ochoa Muñoz radica en su contribución al desarrollo de la música tradicional ecuatoriana, ayudando a preservar y difundir las raíces musicales de su región.",
        "periodo_vida": "No documentado",
        "composiciones": "Obras musicales tradicionales",
        "obras_destacadas": "Pasillos lojanos",
        "legado": "Aportó al fortalecimiento de la identidad musical de Loja."
    },
    {
        "nombre": "Francisco Rodas Bustamante",
        "biografia": "Francisco Rodas Bustamante fue un músico lojano que participó en el desarrollo de la música tanto religiosa como popular. No existen registros exactos sobre su nacimiento y muerte, pero su aporte se ubica en las primeras etapas de la música lojana.\n\nDurante su vida realizó composiciones que contribuyeron a la transición entre la música religiosa y la música popular en la región. Su trabajo ayudó a diversificar el panorama musical de Loja.\n\nFue parte de una generación que sentó las bases para el desarrollo posterior del pasillo y otras expresiones musicales. Su influencia se percibe en la evolución de la música lojana.\n\nSu legado cultural se encuentra en su contribución al crecimiento de la música en Loja, siendo uno de los precursores de su riqueza artística.",
        "periodo_vida": "No registrado",
        "composiciones": "Música religiosa y popular",
        "obras_destacadas": "Obras dentro de la tradición lojana",
        "legado": "Aportó al desarrollo de diferentes géneros musicales en la región."
    },
    {
        "nombre": "Emiliano Ortega",
        "biografia": "Emiliano Ortega fue una figura cultural vinculada al desarrollo artístico de Loja. Aunque no se dispone de información detallada sobre su vida, se reconoce su participación en el ámbito cultural de la región.\n\nSe destacó por su aporte a la música y al arte, formando parte del movimiento cultural que impulsó el desarrollo artístico de la ciudad. Su trabajo contribuyó al crecimiento de la identidad cultural lojana.\n\nParticipó en actividades culturales que ayudaron a consolidar a Loja como un referente artístico en el Ecuador. Su presencia fue importante dentro de la comunidad artística.\n\nEl legado cultural de Emiliano Ortega radica en su contribución al fortalecimiento del arte y la cultura en Loja, siendo parte del proceso que posicionó a la ciudad como un centro cultural.",
        "periodo_vida": "No documentado",
        "composiciones": "Producción artística variada",
        "obras_destacadas": "Aportes culturales locales",
        "legado": "Su participación fortaleció el desarrollo artístico de Loja."
    },
    {
        "nombre": "Julio Cañar",
        "biografia": "Julio Cañar fue un músico lojano del cual existe poca información documentada. Sin embargo, es reconocido dentro del ámbito cultural como parte del desarrollo musical de la región.\n\nSe le atribuye participación en la música tradicional lojana, contribuyendo al repertorio cultural de la provincia. Su trabajo formó parte de las expresiones artísticas locales.\n\nPerteneció a una generación de músicos que ayudaron a mantener vivas las tradiciones musicales de Loja, participando en eventos y actividades culturales.\n\nSu legado cultural se basa en su contribución al entorno musical de Loja, siendo parte de la construcción de su identidad cultural.",
        "periodo_vida": "No registrado",
        "composiciones": "No precisadas",
        "obras_destacadas": "Tradición musical local",
        "legado": "Contribuyó al entorno musical tradicional de la provincia."
    },
    {
        "nombre": "Víctor Moreno Proaño",
        "biografia": "Víctor Moreno Proaño fue un músico lojano del siglo XX que participó en el desarrollo de la música instrumental y tradicional. No se dispone de datos exactos sobre su nacimiento y fallecimiento.\n\nDurante su trayectoria realizó composiciones musicales que formaron parte del repertorio artístico de la región. Su trabajo contribuyó al crecimiento de la música lojana.\n\nSe destacó como intérprete y compositor, participando en el movimiento cultural de Loja. Su aporte ayudó a fortalecer la identidad musical de la ciudad.\n\nSu legado cultural radica en su contribución al desarrollo musical de Loja, siendo parte de la tradición que consolidó a la ciudad como un referente cultural del Ecuador.",
        "periodo_vida": "No documentado",
        "composiciones": "Música instrumental",
        "obras_destacadas": "Obras tradicionales",
        "legado": "Su aporte forma parte del desarrollo musical de Loja."
    }
]

for item in data:
    # Try alternate names or exact name
    search_names = [item["nombre"]] + item.get("aliases", [])
    artista = None
    for n in search_names:
        artista = Artista.objects.filter(nombre__iexact=n).first()
        if artista:
            break
    
    if artista:
        artista.nombre = item["nombre"] # Update name to canonical (e.g. Celi instead of Cánovas)
        artista.biografia = item["biografia"]
        artista.periodo_vida = item["periodo_vida"]
        artista.composiciones_resumen = item["composiciones"]
        artista.obras_destacadas_resumen = item["obras_destacadas"]
        artista.legado_resumen = item["legado"]
        artista.save()
        print(f"Actualizado: {item['nombre']}")
    else:
        # Create if not exists? I'll just create a new one to be sure.
        Artista.objects.create(
            nombre=item["nombre"],
            biografia=item["biografia"],
            periodo_vida=item["periodo_vida"],
            composiciones_resumen=item["composiciones"],
            obras_destacadas_resumen=item["obras_destacadas"],
            legado_resumen=item["legado"]
        )
        print(f"Creado nuevo: {item['nombre']}")

print("Carga de biografías completada.")

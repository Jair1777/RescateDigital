import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from gamificacion.models import Quiz, Pregunta, Opcion

quizzes_data = [
    {
        "titulo": "Reto: Salvador Bustamante Celi",
        "descripcion": "Pon a prueba tus conocimientos sobre el pionero de la música académica lojana.",
        "preguntas": [
            {"texto": "¿En qué fecha nació Salvador Bustamante Celi?", "opciones": [("1 de marzo de 1876", True), ("10 de mayo de 1890", False), ("15 de julio de 1885", False)]},
            {"texto": "¿En qué ciudad nació?", "opciones": [("Loja", True), ("Cuenca", False), ("Quito", False)]},
            {"texto": "¿Cuántas composiciones realizó aproximadamente?", "opciones": [("Más de 100", True), ("Cerca de 50", False), ("Exactamente 10", False)]},
            {"texto": "¿Qué géneros abarcó su obra?", "opciones": [("Religiosa, sinfónica y popular", True), ("Solo música sacra", False), ("Únicamente pasillos", False)]},
            {"texto": "¿En qué país falleció?", "opciones": [("Ecuador", True), ("Perú", False), ("Colombia", False)]},
            {"texto": "¿Qué tipo de obra destaca en su repertorio litúrgico?", "opciones": [("Cantatas y piezas litúrgicas", True), ("Óperas italianas", False), ("Sinfonías modernas", False)]},
            {"texto": "Además de compositor, ¿qué otro papel fundamental desempeñó?", "opciones": [("Educador musical", True), ("Pintor", False), ("Político", False)]},
            {"texto": "¿Qué combinación de influencias tenía su estilo?", "opciones": [("Europeas e identidad lojana", True), ("Africanas y asiáticas", False), ("Andinas y caribeñas", False)]},
            {"texto": "¿Cómo es reconocida Loja gracias a su legado?", "opciones": [("Capital Musical del Ecuador", True), ("Ciudad de las Flores", False), ("Centro del Mundo", False)]},
            {"texto": "¿Su influencia persiste hoy en día?", "opciones": [("Sí, en conservatorios y escuelas", True), ("No, su obra se perdió", False), ("Solo en pequeños círculos", False)]}
        ]
    },
    {
        "titulo": "Reto: Segundo Cueva Celi",
        "descripcion": "Descubre cuánto sabes sobre el maestro del pasillo lojano.",
        "preguntas": [
            {"texto": "¿En qué fecha nació Segundo Cueva Celi?", "opciones": [("10 de enero de 1901", True), ("1 de marzo de 1876", False), ("15 de mayo de 1910", False)]},
            {"texto": "¿Cuál es el género que más representa su identidad cultural?", "opciones": [("Pasillo", True), ("Yaraví", False), ("Sanjuanito", False)]},
            {"texto": "¿A qué edad mostró vocación por la música?", "opciones": [("Desde joven", True), ("A los 40 años", False), ("Cerca de su vejez", False)]},
            {"texto": "¿Cuántas obras compuso durante su trayectoria?", "opciones": [("Más de 80", True), ("Menos de 20", False), ("Cerca de 200", False)]},
            {"texto": "¿Cuál de estas piezas es una composición reconocida suya?", "opciones": [("Pequeña ciudadana", True), ("Guayaquil de mis amores", False), ("El alma en los labios", False)]},
            {"texto": "¿De qué trata principalmente su música?", "opciones": [("Amor, nostalgia y melancolía", True), ("Guerra y política", False), ("Naturaleza y animales", False)]},
            {"texto": "¿En qué año falleció?", "opciones": [("1969", True), ("1935", False), ("1990", False)]},
            {"texto": "¿Cómo se posicionó gracias a su talento?", "opciones": [("Como referente del género nacional", True), ("Como director de orquesta extranjera", False), ("Como cantante de ópera", False)]},
            {"texto": "¿Su influencia continúa vigente?", "opciones": [("Sí, en músicos contemporáneos", True), ("No, solo se escucha en museos", False), ("Solo fuera del Ecuador", False)]},
            {"texto": "¿Qué consolidó su legado cultural?", "opciones": [("El pasillo lojano como representativo", True), ("La música rock en Loja", False), ("La enseñanza de la danza clásica", False)]}
        ]
    },
    {
        "titulo": "Reto: David Pacheco Ochoa",
        "descripcion": "Pon a prueba tu conocimiento sobre el director y educador musical David Pacheco Ochoa.",
        "preguntas": [
            {"texto": "¿En qué fecha nació David Pacheco Ochoa?", "opciones": [("14 de diciembre de 1920", True), ("10 de enero de 1901", False), ("1 de marzo de 1876", False)]},
            {"texto": "Además de compositor, ¿qué otras funciones desempeñó?", "opciones": [("Director musical y educador", True), ("Médico y científico", False), ("Escritor y novelista", False)]},
            {"texto": "¿A qué dedicó gran parte de su vida en su ciudad natal?", "opciones": [("Promoción y enseñanza de la música", True), ("Construcción de edificios", False), ("Comercio de instrumentos", False)]},
            {"texto": "¿Aproximadamente cuántas obras compuso?", "opciones": [("100 obras", True), ("10 obras", False), ("500 obras", False)]},
            {"texto": "¿Cuáles eran algunos de sus géneros de composición?", "opciones": [("Pasillos, marchas e himnos", True), ("Óperas y ballets", False), ("Jazz y Blues", False)]},
            {"texto": "¿Qué refleja su producción musical?", "opciones": [("La tradición lojana y compromiso educativo", True), ("La modernidad industrial", False), ("La influencia del rock and roll", False)]},
            {"texto": "¿Qué grupo de personas se benefició de su labor docente?", "opciones": [("Jóvenes músicos", True), ("Ancianos jubilados", False), ("Turistas extranjeros", False)]},
            {"texto": "¿En qué consistió su participación en instituciones culturales?", "opciones": [("Fortaleció el desarrollo artístico regional", True), ("Diseñó museos arqueológicos", False), ("Gestionó fondos bancarios", False)]},
            {"texto": "¿En qué radica su mayor legado cultural?", "opciones": [("Difusión de la música y formación de talentos", True), ("Venta masiva de discos", False), ("Descubrimiento de nuevos instrumentos", False)]},
            {"texto": "¿Fue relevante su trabajo a nivel nacional?", "opciones": [("Sí, mantuvo la relevancia de Loja", True), ("No, solo fue local", False), ("Poco, no fue muy conocido", False)]}
        ]
    },
    {
        "titulo": "Reto: Daniel Armijos Carrión",
        "descripcion": "Aprende sobre Daniel Armijos Carrión y su aporte a la música para bandas.",
        "preguntas": [
            {"texto": "¿Se tiene registro exacto de su fecha de nacimiento?", "opciones": [("No se cuenta con registros exactos", True), ("Sí, nació en 1900", False), ("Se sabe que fue en la colonia", False)]},
            {"texto": "¿En qué siglo se sitúa su actividad musical?", "opciones": [("Siglo XX", True), ("Siglo XVIII", False), ("Siglo XIX", False)]},
            {"texto": "¿En qué tipo de música se destacó principalmente?", "opciones": [("Música para bandas y pasillos", True), ("Canto gregoriano", False), ("Música electrónica temprana", False)]},
            {"texto": "¿A qué ayudó a mantener viva su obra?", "opciones": [("La identidad musical de la región", True), ("La lengua quichua", False), ("La gastronomía local", False)]},
            {"texto": "¿En qué espacios eran interpretadas sus obras?", "opciones": [("Eventos culturales y festividades", True), ("Teatros internacionales de ópera", False), ("En el extranjero únicamente", False)]},
            {"texto": "¿A qué generación de músicos perteneció?", "opciones": [("Músicos que fortalecieron la música popular", True), ("Vanguardistas abstractos", False), ("Compositores de música pop", False)]},
            {"texto": "¿Fue clave su participación en qué tipo de agrupaciones?", "opciones": [("Agrupaciones musicales tradicionales", True), ("Orquestas de cámara europeas", False), ("Coros estudiantiles", False)]},
            {"texto": "¿Cuál es su legado cultural principal?", "opciones": [("Aporte a la música comunitaria y preservación", True), ("Creación del primer conservatorio", False), ("Invención de la flauta traversa", False)]},
            {"texto": "¿De qué provincia se considera su obra parte del patrimonio?", "opciones": [("Loja", True), ("Pichincha", False), ("Guayas", False)]},
            {"texto": "¿Su obra aseguró la continuidad de la música popular?", "opciones": [("Sí, a lo largo del tiempo", True), ("No, fue olvidada rápido", False), ("Solo por un par de años", False)]}
        ]
    },
    {
        "titulo": "Reto: Manuel de Jesús Lozano",
        "descripcion": "Pon a prueba tus conocimientos sobre Manuel de Jesús Lozano.",
        "preguntas": [
            {"texto": "¿En qué siglo se sitúa la trayectoria de Manuel de Jesús Lozano?", "opciones": [("Siglo XX", True), ("Siglo XIX", False), ("Siglo XXI", False)]},
            {"texto": "¿Se tienen datos precisos sobre su nacimiento?", "opciones": [("No se tienen datos precisos", True), ("Sí, coinciden con 1920", False), ("Se sabe que fue en 1890", False)]},
            {"texto": "¿Por qué género destaca principalmente su aporte?", "opciones": [("Pasillo", True), ("Vals", False), ("Bolero", False)]},
            {"texto": "¿A qué repertorio se integraron sus composiciones?", "opciones": [("Música tradicional de la región", True), ("Éxitos de radio moderna", False), ("Sinfonías clásicas", False)]},
            {"texto": "¿Qué características reflejan sus obras?", "opciones": [("Melancolía y romanticismo", True), ("Alegría y euforia", False), ("Sátira política", False)]},
            {"texto": "¿A qué contribuyó su generación de músicos?", "opciones": [("Difusión y permanencia de la cultura local", True), ("Eliminación de tradiciones antiguas", False), ("Creación de nuevos idiomas", False)]},
            {"texto": "¿Ayudó su trabajo a la identidad musical de la ciudad?", "opciones": [("Sí, a fortalecerla", True), ("No, no tuvo impacto", False), ("Poco, era muy experimental", False)]},
            {"texto": "¿Dónde se encuentra su legado cultural?", "opciones": [("En la continuidad del pasillo as expresión artística", True), ("En la arquitectura de teatros", False), ("En la pintura de retratos", False)]},
            {"texto": "¿A qué proceso ayudó dentro de la historia de Loja?", "opciones": [("Convertirla en un centro musical importante", True), ("Aumentar la producción agrícola", False), ("Industrializar la ciudad", False)]},
            {"texto": "¿Su nombre se mantiene vigente hoy?", "opciones": [("Sí, dentro de la historia musical", True), ("No, es desconocido", False), ("Solo en sus familiares", False)]}
        ]
    },
    {
        "titulo": "Reto: Marcos Ochoa Muñoz",
        "descripcion": "Descubre cuánto sabes sobre Marcos Ochoa Muñoz y el pasillo lojano.",
        "preguntas": [
            {"texto": "¿En qué siglo destacó Marcos Ochoa Muñoz?", "opciones": [("Siglo XX", True), ("Siglo XIX", False), ("Siglo XVII", False)]},
            {"texto": "¿Se dispone de fechas exactas de su vida?", "opciones": [("No se dispone de fechas exactas", True), ("Sí, nació en 1915", False), ("Solo se sabe el año de su muerte", False)]},
            {"texto": "¿Por qué es reconocido este compositor?", "opciones": [("Creación y difusión de música tradicional", True), ("Construcción de instrumentos de viento", False), ("Escribir poemas épicos", False)]},
            {"texto": "¿Qué géneros compuso principalmente?", "opciones": [("Pasillo y formas populares", True), ("Música para cine", False), ("Óperas dramáticas", False)]},
            {"texto": "¿Qué reflejan sus composiciones?", "opciones": [("Identidad cultural lojana", True), ("Influencia del rock inglés", False), ("Sonidos del amazonas", False)]},
            {"texto": "¿En qué espacios fueron interpretadas sus obras?", "opciones": [("Distintos espacios artísticos", True), ("Solo en el ámbito privado", False), ("Únicamente en iglesias", False)]},
            {"texto": "¿A qué contribuyó su trabajo?", "opciones": [("Fortalecimiento del repertorio musical de Loja", True), ("Modificar la geografía de la ciudad", False), ("A la banca nacional", False)]},
            {"texto": "¿Qué impulsó su generación de músicos?", "opciones": [("La música como elemento clave de la cultura", True), ("La danza folclórica exclusivamente", False), ("La literatura en verso", False)]},
            {"texto": "¿Dónde radica su legado cultural?", "opciones": [("Contribución al desarrollo de la música tradicional", True), ("Venta de partituras antiguas", False), ("Creación de la televisión lojana", False)]},
            {"texto": "¿Ayudó a preservar las raíces musicales?", "opciones": [("Sí, de su región", True), ("No, prefirió la música extranjera", False), ("Poco, era muy comercial", False)]}
        ]
    },
    {
        "titulo": "Reto: Francisco Rodas Bustamante",
        "descripcion": "Conoce más sobre el precursor Francisco Rodas Bustamante.",
        "preguntas": [
            {"texto": "¿En qué tipos de música participó Francisco Rodas Bustamante?", "opciones": [("Religiosa y popular", True), ("Opera y Zarzuela", False), ("Jazz y Blues", False)]},
            {"texto": "¿Se tiene registro de su nacimiento?", "opciones": [("No existen registros exactos", True), ("S, naci en 1850", False), ("Naci en el siglo XVIII", False)]},
            {"texto": "¿En qué etapa de la música lojana se ubica su aporte?", "opciones": [("Primeras etapas", True), ("Etapa contemporánea", False), ("Fines del siglo XXI", False)]},
            {"texto": "¿A qué transición contribuyeron sus composiciones?", "opciones": [("Entre música religiosa y popular", True), ("Entre Barroco y Renacentismo", False), ("Entre Acústico y Eléctrico", False)]},
            {"texto": "¿Qué ayudó a diversificar su trabajo?", "opciones": [("El panorama musical de Loja", True), ("La economía de los músicos", False), ("La fabricación de guitarras", False)]},
            {"texto": "¿Sentó las bases para el desarrollo de qué género?", "opciones": [("Pasillo", True), ("Rock", False), ("Salsa", False)]},
            {"texto": "¿Su influencia se percibe hoy?", "opciones": [("Sí, en la evolución de la música lojana", True), ("No, es imperceptible", False), ("Solo en documentos viejos", False)]},
            {"texto": "¿Cuál es su legado cultural principal?", "opciones": [("Contribución al crecimiento musical regional", True), ("Invención de la notación musical", False), ("Formación del coro nacional", False)]},
            {"texto": "¿Cómo se le considera respecto a la riqueza artística de Loja?", "opciones": [("Uno de los precursores", True), ("Un detractor", False), ("Un observador pasivo", False)]},
            {"texto": "¿Hubo información exhaustiva de su vida?", "opciones": [("No, existen pocos datos cronológicos", True), ("Sí, hay una biografía de 500 páginas", False), ("Había fotos de él", False)]}
        ]
    },
    {
        "titulo": "Reto: Emiliano Ortega",
        "descripcion": "Aprende sobre la figura cultural Emiliano Ortega.",
        "preguntas": [
            {"texto": "¿Cómo se describe a Emiliano Ortega?", "opciones": [("Figura cultural vinculada al arte", True), ("Arquitecto de renombre", False), ("General del ejército", False)]},
            {"texto": "¿Se tiene información detallada sobre su vida?", "opciones": [("No se dispone de mucha información detallada", True), ("S, hay un archivo completo", False), ("Muri recientemente", False)]},
            {"texto": "¿En qué ámbito se reconoce su participación?", "opciones": [("Cultural de la región", True), ("Deportivo nacional", False), ("Científico espacial", False)]},
            {"texto": "¿Por qué se destacó?", "opciones": [("Aporte a la música y al arte", True), ("Descubrimiento de minas", False), ("Participación en regatas", False)]},
            {"texto": "¿A qué movimiento cultural perteneció?", "opciones": [("Al que impulsó el desarrollo artístico de Loja", True), ("Al impresionismo francés", False), ("Al surrealismo", False)]},
            {"texto": "¿A qué contribuyó su trabajo?", "opciones": [("Al crecimiento de la identidad cultural lojana", True), ("A la construcción de vías", False), ("Al aumento de la población", False)]},
            {"texto": "¿En qué tipo de actividades participó?", "opciones": [("Actividades culturales que consolidaron a Loja", True), ("Juntas de negocios internacionales", False), ("Misiones diplomáticas", False)]},
            {"texto": "¿Como qué se reconoce a Loja gracias a estos aportes?", "opciones": [("Referente artístico en el Ecuador", True), ("Centro financiero", False), ("Puerto marítimo", False)]},
            {"texto": "¿Fue importante su presencia en la comunidad artística?", "opciones": [("Sí, fue importante", True), ("No, pasó desapercibido", False), ("Solo al final de su vida", False)]},
            {"texto": "¿Qué posicionó su legado cultural?", "opciones": [("A la ciudad como centro cultural", True), ("A Loja como capital industrial", False), ("Al país como potencia mundial", False)]}
        ]
    },
    {
        "titulo": "Reto: Julio Cañar",
        "descripcion": "Descubre lo que se sabe de Julio Cañar.",
        "preguntas": [
            {"texto": "¿Cómo es la información documentada sobre Julio Cañar?", "opciones": [("Existe poca información", True), ("Es muy abundante", False), ("Se perdió en un incendio", False)]},
            {"texto": "¿En qué ámbito es reconocido?", "opciones": [("Cultural lojano", True), ("Política internacional", False), ("Deportes de riesgo", False)]},
            {"texto": "¿A qué tipo de música se le atribuye participación?", "opciones": [("Tradicional lojana", True), ("Electrónica experimental", False), ("Canto de ópera alemán", False)]},
            {"texto": "¿A qué repertorio contribuyó?", "opciones": [("Cultural de la provincia", True), ("Canciones de cuna mundiales", False), ("Repertorio coral barroco", False)]},
            {"texto": "¿De qué formó parte su trabajo?", "opciones": [("Expresiones artísticas locales", True), ("Grandes producciones de Hollywood", False), ("Publicidad de radio", False)]},
            {"texto": "¿A qué generación de músicos perteneció?", "opciones": [("A los que ayudaron a mantener vivas las tradiciones", True), ("A los modernistas abstractos", False), ("A la generación de cristal", False)]},
            {"texto": "¿En qué solía participar según el ámbito local?", "opciones": [("Eventos y actividades culturales", True), ("Competencias de atletismo", False), ("Foros de agricultura", False)]},
            {"texto": "¿En qué se basa su legado cultural?", "opciones": [("Contribución al entorno musical de Loja", True), ("Venta de instrumentos", False), ("Escribir una enciclopedia", False)]},
            {"texto": "¿De qué construcción fue parte?", "opciones": [("Identidad cultural local", True), ("Puentes de piedra", False), ("Sistema de riego", False)]},
            {"texto": "¿Se sabe dónde nació?", "opciones": [("Se sabe que fue en Loja, pero sin detalles", True), ("S, naci en Quito", False), ("No se conoce el pas", False)]}
        ]
    },
    {
        "titulo": "Reto: Víctor Moreno Proaño",
        "descripcion": "Aprende sobre Víctor Moreno Proaño y su aporte instrumental.",
        "preguntas": [
            {"texto": "¿A qué siglo perteneció Víctor Moreno Proaño?", "opciones": [("Siglo XX", True), ("Siglo XIX", False), ("Siglo XVIII", False)]},
            {"texto": "¿En qué tipo de música participó?", "opciones": [("Instrumental y tradicional", True), ("Opera dramática", False), ("Pop melódico", False)]},
            {"texto": "¿Se dispone de datos exactos de su fallecimiento?", "opciones": [("No se dispone de datos exactos", True), ("S, fue en 1950", False), ("Falleci hace pocos aos", False)]},
            {"texto": "¿Integraron sus obras el repertorio artístico de qué región?", "opciones": [("Región de Loja", True), ("Costa ecuatoriana", False), ("Selva Amazónica", False)]},
            {"texto": "¿A qué contribuyó su trabajo musical?", "opciones": [("Crecimiento de la música lojana", True), ("Producción de café", False), ("Turismo de playas", False)]},
            {"texto": "¿Cómo se destacó además de compositor?", "opciones": [("Como intérprete", True), ("Como guitarrista de jazz", False), ("Como luthier", False)]},
            {"texto": "¿En qué movimiento participó en Loja?", "opciones": [("Movimiento cultural", True), ("Movimiento estudiantil de protesta", False), ("Guerra civil", False)]},
            {"texto": "¿Ayudó a fortalecer qué identidad?", "opciones": [("Identidad musical de la ciudad", True), ("Identidad nacional deportiva", False), ("Sentimiento de culpa", False)]},
            {"texto": "¿Cuál es su legado cultural?", "opciones": [("Contribución al desarrollo musical de Loja", True), ("Creación de la radio municipal", False), ("Primer concurso de villancicos", False)]},
            {"texto": "¿Como qué se consolidó la ciudad gracias a esta tradición?", "opciones": [("Referente cultural del Ecuador", True), ("Centro de negocios", False), ("Ciudad fantasma", False)]}
        ]
    }
]

for q_data in quizzes_data:
    quiz, created = Quiz.objects.get_or_create(
        titulo=q_data["titulo"],
        defaults={"descripcion": q_data["descripcion"]}
    )
    if not created:
        # Clear old questions if any (optional, but good for reruns)
        quiz.preguntas.all().delete()
    
    for p_data in q_data["preguntas"]:
        pregunta = Pregunta.objects.create(quiz=quiz, texto_pregunta=p_data["texto"])
        for texto_opcion, es_correcta in p_data["opciones"]:
            Opcion.objects.create(pregunta=pregunta, texto=texto_opcion, es_correcta=es_correcta)

print("Carga de quizzes finalizada exitosamente.")

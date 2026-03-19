import os
import re
import polib

templates_dir = 'templates'

trans_re = re.compile(r'{%\s*trans\s+[\'"](.*?)[\'"]\s*%}')
blocktrans_re = re.compile(r'{%\s*blocktrans\s*%}(.*?){%\s*endblocktrans\s*%}', re.DOTALL)

strings = set()

for root, dirs, files in os.walk(templates_dir):
    for f in files:
        if f.endswith('.html'):
            with open(os.path.join(root, f), 'r', encoding='utf-8') as file:
                content = file.read()
                for match in trans_re.findall(content):
                    strings.add(match)
                for match in blocktrans_re.findall(content):
                    strings.add(match.strip())

translations_en = {
    "Inicio": "Home",
    "Historia musical": "Musical History",
    "Artistas": "Artists",
    "Juegos": "Games",
    "Sobre el proyecto": "About the Project",
    "Cerrar Sesión": "Logout",
    "Login": "Login",
    "Un proyecto destinado a la recuperación, digitalización y puesta en valor del patrimonio musical de la ciudad de Loja, Ecuador.": "A project aimed at the recovery, digitization, and enhancement of the musical heritage of the city of Loja, Ecuador.",
    "Navegación": "Navigation",
    "Historia Musical": "Musical History",
    "Archivo Digital": "Digital Archive",
    "Institucional": "Institutional",
    "Sobre el Proyecto": "About the Project",
    "Investigadores": "Researchers",
    "Alianzas": "Alliances",
    "Contacto": "Contact",
    "Rescate Digital de la Historia Musical Lojana. Todos los derechos reservados.": "Digital Rescue of Loja's Musical History. All rights reserved.",
    "Patrimonio Cultural de Loja": "Cultural Heritage of Loja",
    "Rescate Digital de la": "Digital Rescue of the",
    "Historia": "History",
    "Musical": "Musical",
    "Lojana": "Lojana",
    "Explorar Archivo": "Explore Archive",
    "Conocer el Proyecto": "Know the Project",
    "Acerca de la Plataforma": "About the Platform",
    "La creación de una página web dedicada al Rescate Digital de la Historia Musical Lojana surge de la necesidad de preservar, difundir y revalorizar el patrimonio cultural de Loja, reconocido como uno de los principales referentes musicales del Ecuador.": "The creation of a website dedicated to the Digital Rescue of Loja's Musical History arises from the need to preserve, disseminate, and revalue the cultural heritage of Loja, recognized as one of the main musical references in Ecuador.",
    "A lo largo del tiempo, gran parte de la riqueza musical lojana incluyendo compositores, intérpretes, obras y tradiciones ha permanecido dispersa, poco documentada o en riesgo de perderse debido al paso del tiempo y la falta de digitalización. Por ello, este proyecto busca recopilar y organizar esta información en un espacio accesible, moderno y dinámico.": "Over time, much of Loja's musical wealth, including composers, performers, works, and traditions, has remained dispersed, poorly documented, or at risk of being lost due to the passage of time and lack of digitization. Therefore, this project seeks to collect and organize this information in an accessible, modern, and dynamic space.",
    "La plataforma digital permitirá que nuevas generaciones conozcan y se conecten con sus raíces culturales, al mismo tiempo que facilita el acceso a investigadores, estudiantes y público en general interesado en la música lojana. Además, contribuirá a fortalecer la identidad cultural y promover el reconocimiento de los artistas locales.": "The digital platform will allow new generations to know and connect with their cultural roots, while facilitating access to researchers, students, and the general public interested in Loja's music. In addition, it will help strengthen cultural identity and promote the recognition of local artists.",
    "En un mundo cada vez más digital, preservar la historia musical a través de herramientas tecnológicas no solo es una oportunidad, sino una responsabilidad para garantizar que este legado perdure en el tiempo.": "In an increasingly digital world, preserving musical history through technological tools is not only an opportunity but a responsibility to ensure that this legacy endures over time.",
    "Desarrolladores Web:": "Web Developers:",
    "Somos Jostin Torres y Jair Chávez": "We are Jostin Torres and Jair Chávez",
    "estudiantes de la Unidad Educativa Fiscomisional La Dolorosa. Nos complace darles la bienvenida a este espacio digital creado con el propósito de rescatar, preservar y difundir la historia musical lojana.": "students of the La Dolorosa Fiscomisional Educational Unit. We are pleased to welcome you to this digital space created with the purpose of rescuing, preserving, and disseminating Loja's musical history.",
    "Este proyecto nace de nuestro interés por valorar nuestras raíces culturales y aportar, desde la educación y la tecnología, a la conservación del legado musical de nuestra región. A través de esta página, buscamos que más personas conozcan la riqueza artística de Loja y se conecten con su identidad cultural.": "This project was born out of our interest in valuing our cultural roots and contributing, from education and technology, to the conservation of our region's musical legacy. Through this page, we hope more people will know the artistic wealth of Loja and connect with its cultural identity.",
    "Esperamos que este sitio sea una fuente de aprendizaje, inspiración y orgullo para todos quienes lo visiten.": "We hope this site will be a source of learning, inspiration, and pride for all who visit it.",
    "Curiosidad": "Curiosity",
    "El pasillo ecuatoriano tiene fuertes raíces en los valses europeos, adaptados brillantemente al sentimiento andino característico de Loja.": "The Ecuadorian pasillo has strong roots in European waltzes, brilliantly adapted to the Andean sentiment characteristic of Loja.",
    "Archivo Vivo": "Living Archive",
    "En la época de oro de la música lojana, se registraron más de 400 partituras manuscritas invaluables para nuestro patrimonio.": "In the golden age of Loja's music, more than 400 handwritten scores invaluable to our heritage were recorded.",
    "Capital Musical": "Musical Capital",
    "Loja es reconocida a nivel sudamericano por exportar grandes talentos históricos en el ámbito de la música sacra y académica.": "Loja is recognized at the South American level for exporting great historical talents in the field of sacred and academic music.",
    "Únete": "Join",
    "La plataforma planea permitir aportes de la comunidad para contar historias inéditas sobre nuestros artistas.": "The platform plans to allow community contributions to tell unpublished stories about our artists.",
    "Aprende Jugando": "Learn by Playing",
    "Explora nuestra plataforma interactiva y pon a prueba tus conocimientos sobre la música lojana.": "Explore our interactive platform and test your knowledge of Loja's music.",
    "Quiz Musical": "Musical Quiz",
    "¿Cuánto sabes sobre los géneros, compositores e instrumentos típicos de Loja?": "How much do you know about the genres, composers, and typical instruments of Loja?",
    "Jugar ahora": "Play now",
    "Sistema de Puntos": "Point System",
    "Completa desafíos, desbloquea insignias y conviértete en un Experto Musical.": "Complete challenges, unlock badges, and become a Musical Expert.",
    "Ver ranking": "View ranking",
    "Línea del Tiempo Musical": "Musical Timeline",
    "Viaja a través de los siglos y descubre cómo Loja se convirtió en el epicentro sonoro del Ecuador. Desde las influencias coloniales hasta las composiciones vanguardistas del siglo XXI.": "Travel through the centuries and discover how Loja became the sonic epicenter of Ecuador. From colonial influences to avant-garde compositions of the 21st century.",
    "Explorar la Cronología": "Explore the Chronology",
    "Preservando el legado sonoro y la herencia cultural de la capital musical del Ecuador a través de la tecnología digital.": "Preserving the sonic legacy and cultural heritage of the musical capital of Ecuador through digital technology."
}

translations_fr = {
    "Inicio": "Accueil",
    "Historia musical": "Histoire musicale",
    "Artistas": "Artistes",
    "Juegos": "Jeux",
    "Sobre el proyecto": "À propos du projet",
    "Cerrar Sesión": "Se déconnecter",
    "Login": "Connexion",
    "Un proyecto destinado a la recuperación, digitalización y puesta en valor del patrimonio musical de la ciudad de Loja, Ecuador.": "Un projet visant à la récupération, la numérisation et la mise en valeur du patrimoine musical de la ville de Loja, en Équateur.",
    "Navegación": "Navigation",
    "Historia Musical": "Histoire Musicale",
    "Archivo Digital": "Archives Numériques",
    "Institucional": "Institutionnel",
    "Sobre el Proyecto": "À propos du Projet",
    "Investigadores": "Chercheurs",
    "Alianzas": "Alliances",
    "Contacto": "Contact",
    "Rescate Digital de la Historia Musical Lojana. Todos los derechos reservados.": "Sauvetage Numérique de l'Histoire Musicale Lojana. Tous droits réservés.",
    "Patrimonio Cultural de Loja": "Patrimoine Culturel de Loja",
    "Rescate Digital de la": "Sauvetage Numérique de l'",
    "Historia": "Histoire",
    "Musical": "Musicale",
    "Lojana": "Lojana",
    "Explorar Archivo": "Explorer les Archives",
    "Conocer el Proyecto": "Découvrir le Projet",
    "Acerca de la Plataforma": "À propos de la Plateforme",
    "La creación de una página web dedicada al Rescate Digital de la Historia Musical Lojana surge de la necesidad de preservar, difundir y revalorizar el patrimonio cultural de Loja, reconocido como uno de los principales referentes musicales del Ecuador.": "La création d'un site web dédié au Sauvetage Numérique de l'Histoire Musicale de Loja naît de la nécessité de préserver, diffuser et revaloriser le patrimoine culturel de Loja, reconnu comme l'une des principales références musicales de l'Équateur.",
    "A lo largo del tiempo, gran parte de la riqueza musical lojana incluyendo compositores, intérpretes, obras y tradiciones ha permanecido dispersa, poco documentada o en riesgo de perderse debido al paso del tiempo y la falta de digitalización. Por ello, este proyecto busca recopilar y organizar esta información en un espacio accesible, moderno y dinámico.": "Au fil du temps, une grande partie de la richesse musicale de Loja, y compris les compositeurs, les interprètes, les œuvres et les traditions, est restée dispersée, peu documentée ou risque d'être perdue à cause du passage du temps et du manque de numérisation. Par conséquent, ce projet cherche à collecter et organiser ces informations dans un espace accessible, moderne et dynamique.",
    "La plataforma digital permitirá que nuevas generaciones conozcan y se conecten con sus raíces culturales, al mismo tiempo que facilita el acceso a investigadores, estudiantes y público en general interesado en la música lojana. Además, contribuirá a fortalecer la identidad cultural y promover el reconocimiento de los artistas locales.": "La plateforme numérique permettra aux nouvelles générations de connaître et de se connecter à leurs racines culturelles, tout en facilitant l'accès aux chercheurs, aux étudiants et au grand public intéressés par la musique de Loja. De plus, elle contribuera à renforcer l'identité culturelle et à promouvoir la reconnaissance des artistes locaux.",
    "En un mundo cada vez más digital, preservar la historia musical a través de herramientas tecnológicas no solo es una oportunidad, sino una responsabilidad para garantizar que este legado perdure en el tiempo.": "Dans un monde de plus en plus numérique, préserver l'histoire musicale par le biais d'outils technologiques n'est pas seulement une opportunité, mais une responsabilité pour garantir que cet héritage perdure dans le temps.",
    "Desarrolladores Web:": "Développeurs Web:",
    "Somos Jostin Torres y Jair Chávez": "Nous sommes Jostin Torres et Jair Chávez",
    "estudiantes de la Unidad Educativa Fiscomisional La Dolorosa. Nos complace darles la bienvenida a este espacio digital creado con el propósito de rescatar, preservar y difundir la historia musical lojana.": "étudiants de l'Unité Éducative Fiscomisionnelle La Dolorosa. Nous sommes heureux de vous accueillir dans cet espace numérique créé dans le but de sauver, préserver et diffuser l'histoire musicale de Loja.",
    "Este proyecto nace de nuestro interés por valorar nuestras raíces culturales y aportar, desde la educación y la tecnología, a la conservación del legado musical de nuestra región. A través de esta página, buscamos que más personas conozcan la riqueza artística de Loja y se conecten con su identidad cultural.": "Ce projet est né de notre intérêt à valoriser nos racines culturelles et à contribuer, par l'éducation et la technologie, à la conservation du patrimoine musical de notre région. À travers cette page, nous espérons que davantage de personnes connaîtront la richesse artistique de Loja et se connecteront à son identité culturelle.",
    "Esperamos que este sitio sea una fuente de aprendizaje, inspiración y orgullo para todos quienes lo visiten.": "Nous espérons que ce site sera une source d'apprentissage, d'inspiration et de fierté pour tous ceux qui le visitent.",
    "Curiosidad": "Curiosité",
    "El pasillo ecuatoriano tiene fuertes raíces en los valses europeos, adaptados brillantemente al sentimiento andino característico de Loja.": "Le pasillo équatorien a de fortes racines dans les valses européennes, brillamment adaptées au sentiment andin caractéristique de Loja.",
    "Archivo Vivo": "Archive Vivante",
    "En la época de oro de la música lojana, se registraron más de 400 partituras manuscritas invaluables para nuestro patrimonio.": "À l'âge d'or de la musique de Loja, plus de 400 partitions manuscrites inestimables pour notre patrimoine ont été enregistrées.",
    "Capital Musical": "Capitale Musicale",
    "Loja es reconocida a nivel sudamericano por exportar grandes talentos históricos en el ámbito de la música sacra y académica.": "Loja est reconnue au niveau sud-américain pour exporter de grands talents historiques dans le domaine de la musique sacrée et académique.",
    "Únete": "Rejoignez-nous",
    "La plataforma planea permitir aportes de la comunidad para contar historias inéditas sobre nuestros artistas.": "La plateforme prévoit de permettre les contributions de la communauté pour raconter des histoires inédites sur nos artistes.",
    "Aprende Jugando": "Apprendre en Jouant",
    "Explora nuestra plataforma interactiva y pon a prueba tus conocimientos sobre la música lojana.": "Explorez notre plateforme interactive et testez vos connaissances sur la musique de Loja.",
    "Quiz Musical": "Quiz Musical",
    "¿Cuánto sabes sobre los géneros, compositores e instrumentos típicos de Loja?": "Que savez-vous des genres, des compositeurs et des instruments typiques de Loja?",
    "Jugar ahora": "Jouez maintenant",
    "Sistema de Puntos": "Système de Points",
    "Completa desafíos, desbloquea insignias y conviértete en un Experto Musical.": "Complétez des défis, débloquez des insignes et devenez un Expert Musical.",
    "Ver ranking": "Voir le classement",
    "Línea del Tiempo Musical": "Chronologie Musicale",
    "Viaja a través de los siglos y descubre cómo Loja se convirtió en el epicentro sonoro del Ecuador. Desde las influencias coloniales hasta las composiciones vanguardistas del siglo XXI.": "Voyagez à travers les siècles et découvrez comment Loja est devenue l'épicentre sonore de l'Équateur. Des influences coloniales aux compositions avant-gardistes du XXIe siècle.",
    "Explorar la Cronología": "Explorer la Chronologie",
    "Preservando el legado sonoro y la herencia cultural de la capital musical del Ecuador a través de la tecnología digital.": "Préserver l'héritage sonore et le patrimoine culturel de la capitale musicale de l'Équateur grâce à la technologie numérique."
}

def build_po(lang_code, lang_name, trans_dict):
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2023-01-01 12:00+0000',
        'PO-Revision-Date': '2023-01-01 12:00+0000',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': f'{lang_name} <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
        'Language': lang_code
    }
    
    for string in strings:
        entry = polib.POEntry(
            msgid=string,
            msgstr=trans_dict.get(string, f"[{lang_code}] {string}")
        )
        po.append(entry)
        
    os.makedirs(f'locale/{lang_code}/LC_MESSAGES', exist_ok=True)
    po.save(f'locale/{lang_code}/LC_MESSAGES/django.po')
    po.save_as_mofile(f'locale/{lang_code}/LC_MESSAGES/django.mo')

build_po('en', 'English', translations_en)
build_po('fr', 'Français', translations_fr)
print("Translations built successfully!")

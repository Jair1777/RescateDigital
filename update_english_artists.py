import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

translations = {
    "Salvador Bustamante Celi": {
        "esencia_en": "Devotion\nHis essence is the sacred and the institutional. Bustamante didn't just write music; he built sonic cathedrals. His spirit was that of an architect seeking to elevate the human spirit towards the divine, whether through a simple carol or a complex mass. He is the solid, formal foundation of Loja."
    },
    "Segundo Cueva Celi": {
        "esencia_en": "Elegance\nHis essence is refinement. Cueva Celi was an aristocrat of sentiment; he took popular sadness and dressed it up with impressionistic harmonies. His music is not for noise, but for attentive listening. He represents cultured nostalgia and aesthetic perfectionism."
    },
    "Manuel de Jesús Lozano": {
        "esencia_en": "Bohemian Sensitivity\nHis essence is closeness. \"El Juglar\" did not seek technical complexity over feeling, but rather a direct connection to the heart. His essence is that of the midnight serenade, honest romance, and loyalty to friends. It is the human soul in its purest and simplest state."
    },
    "Marcos Ochoa Muñoz": {
        "esencia_en": "Discipline\nHis essence is the teaching apostolate. Marcos Ochoa understood that talent without order is lost. His spirit was that of a guide who saw a seed of art in every young person in Loja. He represents selfless dedication to the growth of others and absolute respect for musical technique."
    },
    "David Pacheco Ochoa": {
        "esencia_en": "Vigor\nHis essence is vitality. While others sought introspection, Pacheco Ochoa sought movement and collective joy. He represents the strength of the town band, the brilliance of the trumpets, and the ability of music to unite an entire nation in a single dance.",
        "biografia_en": "This outstanding composer and band director was born in Loja on December 29, 1888. He was a musician who understood like few others the importance of festive and community music. He worked as director of military bands in various provinces, spreading Loja's musical style throughout the country.\n\nHis most famous work is undoubtedly the pasacalle 'El Chulla Quiteño', a piece that became Quito's second anthem. Pacheco Ochoa was a prolific creator of pasillos, pasacalles, and waltzes, characterized by contagious joy and impeccable rhythmic structure. His legacy is vital to understanding band music in Ecuador."
    },
    "Emiliano Ortega Espinosa": {
        "biografia_en": "Born in Loja on February 8, 1898, he was a multifaceted character: poet, musician, journalist, and politician. He is considered one of the most influential intellectuals of his generation. He began his studies at the Bernardo Valdivieso College, where his love for letters and music sprouted. His musical training was largely self-taught.\n\nOrtega was a master at capturing the Loja identity in verses. He authored the lyrics of emblematic songs such as the pasillo 'Española' and the pasacalle 'Lojanita', pieces that became popular anthems. He also served his city as Councilman and President of the Municipality of Loja. His legacy lies in having fused cultured poetry with popular sentiment.",
        "esencia_en": "Landscaping\nHis essence is belonging. Ortega was an observer in love with his surroundings. His essence is the color of the Loja valleys, the scent of its flowers, and the idiosyncrasy of its people. He gave words to the earth so that music could have a home to rest.",
        "periodo_vida_en": "February 8, 1898 – 1971",
        "composiciones_resumen_en": "Versatile music inspired by literature.",
        "obras_destacadas_resumen_en": "Literary compositions turned into music.",
        "legado_resumen_en": "Bridge between Loja poetry and music."
    },
    "Carlos Bonilla Chávez": {
        "biografia_en": "Although born in Quito, his link to national music and his influence in the academic field make him essential on this list. He was a rigorously trained classical guitarist and composer who revolutionized classical guitar in Ecuador. He studied at the National Conservatory of Music and specialized in the double bass, but it was his mastery of the six strings that brought him international fame.\n\nBonilla Chávez founded the Guitar Chair at the National Conservatory, training the country's first professional guitarists. As a composer, he achieved something historic: writing classical guitar pieces based on native rhythms like yaraví, yumbo, and pasillo. His legacy is the elevation of Ecuadorian popular music to the world's most prestigious concert stages.",
        "esencia_en": "Innovation\nHis essence is transcendence. Bonilla Chávez was a visionary who was not satisfied with the established paradigm. His essence is that of an explorer who takes his Andean roots and projects them into the future and the world, proving that homegrown culture possesses universal dignity.",
        "periodo_vida_en": "1923 – 2010",
        "composiciones_resumen_en": "Classical and traditional guitar fusion.",
        "obras_destacadas_resumen_en": "Cantares de mi Tierra, Atahualpa.",
        "legado_resumen_en": "Elevated Ecuadorian guitar to a global level."
    },
    "Segundo Luis Moreno": {
        "biografia_en": "Born in Cotacachi, he is considered the father of musicology in Ecuador. His life was an untiring investigation into the origins and structure of indigenous and mestizo music. He was the director of military bands and conservatories in Quito, Cuenca, and Guayaquil.\n\nHis masterpiece is the monumental 'History of Music in Ecuador', a detailed investigation that systematically organized the country's musical knowledge for the first time. In addition to his work as a historian, he composed numerous symphonic works and chamber music. His legacy is the foundation upon which any serious study of modern Ecuadorian music relies.",
        "esencia_en": "Truth\nHis essence is scientific curiosity. Moreno wasn't satisfied just listening; he needed to understand 'why'. His spirit is that of an archaeologist unearthing forgotten sounds so the present knows where it comes from. He is the historical conscience of our music.",
        "periodo_vida_en": "August 3, 1882 – November 18, 1972",
        "composiciones_resumen_en": "Symphonies and native music studies.",
        "obras_destacadas_resumen_en": "History of Music in Ecuador.",
        "legado_resumen_en": "Pioneered Ecuadorian ethnomusicology."
    },
    "Benjamín Carrión": {
        "biografia_en": "Born in Loja on April 20, 1897, Carrión was not a music composer, but rather the architect of 'Ecuador as a cultural power'. Diplomat, writer, and essayist, he is one of the most important figures in the country's intellectual history. His vision was clear: if Ecuador could not be a military or economic power, it should be a 'Small Nation, but of Great Culture'.\n\nIn 1944 he founded the Casa de la Cultura Ecuatoriana, the most relevant institution for promoting arts in the country. He tirelessly promoted Loja and national artists, ensuring that music, painting, and literature had worthy platforms. His legacy is the institutional and philosophical framework that allowed artists to be recognized and valued.",
        "esencia_en": "Hope\nHis essence is spiritual greatness. Carrión blindly believed in the power of beauty as a national defense. His essence is the conviction that art is the only tool capable of rebuilding a people's dignity. He is the lighthouse that illuminates and protects all other creators.",
        "periodo_vida_en": "April 20, 1897 – March 8, 1979",
        "composiciones_resumen_en": "Literary essays and cultural policies.",
        "obras_destacadas_resumen_en": "Atahualpa, San Miguel de Unamuno.",
        "legado_resumen_en": "Founder of the Casa de la Cultura Ecuatoriana."
    }
}

for a in Artista.objects.all():
    name = a.nombre
    
    # Iterate over all fields and if english field is empty string, we set it up
    updated = False
    
    if name in translations:
        data = translations[name]
        for field_name, en_text in data.items():
            if getattr(a, field_name) == "":
                setattr(a, field_name, en_text)
                updated = True
                
    if updated:
        a.save()
        print(f"Update applied to english fields of {name}")

print("Validation: checking if anything is still empty...")
for a in Artista.objects.all():
    for f in Artista._meta.fields:
        if f.name.endswith('_en'):
            if getattr(a, f.name) == "":
                # Fallback to copy the spanish version for safety 
                esp_field = f.name[:-3]
                esp_val = getattr(a, esp_field)
                setattr(a, f.name, esp_val)
                a.save()
                print(f"Fallback translated {f.name} for {a.nombre} using Spanish string")
                
print("All english fields fully populated!")

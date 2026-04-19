from django.shortcuts import render
from artistas.models import Artista
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def inicio(request):
    # Fetch all artists to display on home page
    artistas = Artista.objects.all().order_by('nombre')
    notificaciones = []
    has_unread = False
    if request.user.is_authenticated:
        notificaciones = request.user.notificaciones.all().order_by('-fecha')[:5]
        has_unread = request.user.notificaciones.filter(leida=False).exists()
    return render(request, 'core/inicio.html', {
        'artistas': artistas,
        'notificaciones': notificaciones,
        'has_unread': has_unread
    })

@login_required
def marcar_notificaciones_leidas(request):
    if request.method == 'POST':
        request.user.notificaciones.filter(leida=False).update(leida=True)
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error'})

def proyecto(request):
    return render(request, 'core/proyecto.html')

def historia(request):
    return render(request, 'core/historia.html')

from django.core.management import call_command
from django.http import HttpResponse

def run_migrations(request):
    try:
        call_command('migrate', interactive=False)
        return HttpResponse("Migrations applied successfully!")
    except Exception as e:
        return HttpResponse(f"Migration failed: {e}")

def mapa_musical(request):
    puntos = [
        {
            "id": "catedral", 
            "nombre": "Catedral de Loja", 
            "lat": -3.9936, "lng": -79.2043, 
            "icon": "fas fa-church", 
            "desc": "La Catedral ha sido históricamente el epicentro de la música sacra desde la fundación de la ciudad. Durante siglos, sus paredes albergaron órganos tubulares y coros litúrgicos donde maestros de capilla como Francisco Rodas Bustamante y el mismísimo Salvador Bustamante Celi compusieron e interpretaron misas, cantatas y villancicos que nutrieron las raíces musicales de las festividades marianas. Su archivo musical es considerado uno de los patrimonios más invaluables del sur del país."
        },
        {
            "id": "museo", 
            "nombre": "Museo de la Música Lojana", 
            "lat": -3.9984, "lng": -79.2061, 
            "icon": "fas fa-guitar", 
            "desc": "Ubicado en el Centro Cultural Alfredo Mora Reyes, el Museo de la Música resguarda los tesoros más íntimos de nuestros artistas: antiguas partituras manuscritas, instrumentos originales, vestimentas, medallas de condecoración y discos de vinilo de la primera mitad del siglo XX. Es un santuario vivo que mantiene encendida la llama de la identidad mestiza local y documenta la proclamación de Loja como cuna incuestionable del arte."
        },
        {
            "id": "teatro_bolivar", 
            "nombre": "Teatro Bolívar", 
            "lat": -3.9958, "lng": -79.2023, 
            "icon": "fas fa-theater-masks", 
            "desc": "El mítico Teatro Bolívar, de arquitectura clásica, es el símbolo de la élite artística y bohemia del pasado siglo. En sus escenarios resonaron orquestas completas, conjuntos corales y se estrenaron algunos de los pasillos más legendarios dirigidos por Segundo Cueva Celi. Durante décadas, toda presentación de élite, galas folclóricas y la música de academia tenían lugar de forma exclusiva entre estas paredes llenas de memoria sonora."
        },
        {
            "id": "san_sebastian", 
            "nombre": "Plaza de la Independencia (San Sebastián)", 
            "lat": -4.0003, "lng": -79.2079, 
            "icon": "fas fa-monument", 
            "desc": "San Sebastián no solo es la cuna de los movimientos independentistas locales, sino también el hogar de las emblemáticas 'Retretas Sonoras'. Cada domingo, las bandas municipales y grupos populares se reunían en su glorieta central para deleitar al pueblo con pasacalles y pasillos. La plaza simboliza la música comunitaria y festiva, el punto de encuentro natural entre los juglares, los compositores enamorados y las románticas noches lojanas."
        },
        {
            "id": "teatro_carrion", 
            "nombre": "Teatro Nacional Benjamín Carrión", 
            "lat": -3.9749, "lng": -79.1979, 
            "icon": "fas fa-star", 
            "desc": "El monumental y moderno Teatro Nacional representa la era contemporánea y la proyección hacia el futuro del arte nacional. Nombrado en honor al intelectual más grande de Ecuador, este imponente escenario es la sede principal de la Orquesta Sinfónica de Loja y el núcleo del mundialmente reconocido 'Festival Internacional de Artes Vivas'. Su enorme aforo atestigua el orgullo intacto por nuestra música sinfónica y las nuevas grandes fusiones."
        },
        {
            "id": "conservatorio", 
            "nombre": "Conservatorio S. Bustamante Celi", 
            "lat": -3.9681, "lng": -79.2025, 
            "icon": "fas fa-university", 
            "desc": "Considerado la escuela o 'Alma Mater' de los más grandes exponentes del país en la actualidad. El Conservatorio fue indispensable para elevar la calidad de los artistas lojanos a un estándar académico internacional. Sus aulas, que siguen retumbando todos los días con pianos, violines o contrabajos, son la prueba patente de que en Loja el talento musical no es solo un regalo histórico, sino una ciencia que se estudia y perfecciona con infinita disciplina."
        }
    ]
    return render(request, 'core/mapa.html', {'puntos': puntos})

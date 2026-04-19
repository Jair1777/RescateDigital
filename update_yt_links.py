import os
import subprocess
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from musica.models import Cancion

def update_links():
    for c in Cancion.objects.all():
        artist_name = c.compositor.nombre if c.compositor else ""
        query = f'ytsearch1:{c.titulo} {artist_name} musica ecuatoriana'
        try:
            vid = subprocess.check_output(['.\\venv\\Scripts\\yt-dlp.exe', '--get-id', query], text=True).strip()
            if vid:
                # yt-dlp might return multiple lines if it finds a playlist, taking the first one
                vid = vid.split('\n')[0].strip()
                c.url_youtube = f'https://www.youtube.com/watch?v={vid}'
                c.save()
                print(f'Updated {c.titulo} -> {c.url_youtube}')
            else:
                print(f'No results for {c.titulo}')
        except Exception as e:
            print(f'Failed {c.titulo}: {e}')

if __name__ == '__main__':
    update_links()

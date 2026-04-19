import os
import django
import yt_dlp

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from musica.models import Cancion

def download_audio():
    os.makedirs('media/musica/audios', exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'media/musica/audios/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
        'quiet': True,
        'no_warnings': True,
    }

    for cancion in Cancion.objects.all():
        if cancion.url_youtube and not cancion.archivo_audio:
            print(f"Downloading {cancion.titulo} - {cancion.url_youtube}")
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info_dict = ydl.extract_info(cancion.url_youtube, download=True)
                    video_id = info_dict.get('id', None)
                    filename = f"musica/audios/{video_id}.mp3"
                    
                    if os.path.exists(f"media/{filename}"):
                        cancion.archivo_audio = filename
                        cancion.save()
                        print(f"Saved {filename} to {cancion.titulo}")
            except Exception as e:
                print(f"Failed to download {cancion.titulo}: {e}")

if __name__ == '__main__':
    download_audio()

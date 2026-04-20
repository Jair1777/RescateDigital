import os
import shutil
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rescate_musical.settings')
django.setup()

from artistas.models import Artista

# Source and Destination paths
downloads_path = r"C:\Users\Jostin Torres\Downloads\artistas"
media_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'artistas')

if not os.path.exists(media_root):
    os.makedirs(media_root)

# New artist mapping (using exact filenames from dir output)
# Note: 'Hctor Romn.jpg' might be 'Héctor Román.jpg' but let's use glob to find matches if possible
new_artists = {
    "Dagoberto Vilela": "Dagoberto Vilela.jpg",
    "Hermanos Quezada": "Hermanos Quezada.jpg",
    "Héctor Román": "Héctor Román.jpg",
    "Medardo Luzuriaga": "Medardo Luzuriaga (Don Medardo).jpg",
    "Tito Quinde": "Tito Quinde.jpg"
}

# The previous ones just in case they weren't copied
previous_artists = {
    "Benjamín Carrión": "Benjamín Carrión.jpg",
    "Carlos Bonilla Chávez": "Carlos Bonilla Chávez.jpg",
    "David Pacheco Ochoa": "David Pacheco Ochoa.jpg",
    "Emiliano Ortega Espinosa": "Emiliano Ortega Espinosa.jpg",
    "Manuel de Jesús Lozano": "Manuel de Jesús Lozano.jpg",
    "Marcos Ochoa Muñoz": "Marcos Ochoa Muñoz.jpg",
    "Salvador Bustamante Celi": "Salvador Bustamante Celi.jpg",
    "Segundo Cueva Celi": "Segundo Cueva Celi.jpg",
    "Segundo Luis Moreno": "Segundo Luis Moreno.jpg"
}

all_mappings = {**new_artists, **previous_artists}

available_files = os.listdir(downloads_path)
print(f"Files in downloads: {available_files}")

for artist_name, filename in all_mappings.items():
    # Try to find the file even if encoding is weird
    target_file = None
    if filename in available_files:
        target_file = filename
    else:
        # Try a more fuzzy match if not found (for characters like é)
        for f in available_files:
            if f.lower().replace(' ', '') == filename.lower().replace(' ', ''):
                target_file = f
                break
    
    if not target_file:
        # One last try check if base names match
        base_target = os.path.splitext(filename)[0].lower()
        for f in available_files:
            if base_target in f.lower():
                target_file = f
                break

    if target_file:
        src = os.path.join(downloads_path, target_file)
        # Standardize filename for media storage to avoid encoding issues in URLs
        norm_filename = filename.replace(' ', '_').lower()
        dst = os.path.join(media_root, norm_filename)
        
        try:
            shutil.copy2(src, dst)
            try:
                artista = Artista.objects.get(nombre=artist_name)
                artista.imagen_perfil = f"artistas/{norm_filename}"
                artista.save()
                print(f"Succees: Updated {artist_name} with {norm_filename}")
            except Artista.DoesNotExist:
                # Try partial match for artist name
                artista = Artista.objects.filter(nombre__icontains=artist_name).first()
                if artista:
                    artista.imagen_perfil = f"artistas/{norm_filename}"
                    artista.save()
                    print(f"Success (partial match): Updated {artista.nombre} with {norm_filename}")
                else:
                    print(f"Error: Artist '{artist_name}' not found in database.")
        except Exception as e:
            print(f"Error copying {target_file}: {e}")
    else:
        print(f"Warning: File {filename} not found for {artist_name}")

print("Sync complete.")

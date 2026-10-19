import os
import json

# Path ng folder kung saan nakalagay ang mga kanta
SONGS_DIR = 'song files'
OUTPUT_FILE = 'songs.json'

# Allowed extensions
VALID_EXTENSIONS = ('.mp4', '.avi', '.mp3', '.mid', '.kar')

def generate_json():
    if not os.path.exists(SONGS_DIR):
        print(f"Error: Hindi mahanap ang folder na '{SONGS_DIR}'. Siguraduhing nandoon ito sa parehong directory.")
        return

    # Kumuha ng listahan ng mga files
    files = [f for f in os.listdir(SONGS_DIR) if f.lower().endswith(VALID_EXTENSIONS)]
    
    # I-sort Alphabetically bago gawan ng paunang ID
    files.sort(key=lambda x: x.lower())

    songs = []
    start_id = 1001

    for idx, filename in enumerate(files):
        # Alisin ang extension para sa Title
        title = os.path.splitext(filename)[0]
        file_ext = os.path.splitext(filename)[1].lower()
        
        # Alamin kung Audio o Video
        song_type = 'audio' if file_ext in ('.mp3', '.mid', '.kar') else 'video'

        songs.append({
            "id": start_id + idx,
            "title": title,
            "url": f"song files/{filename}",
            "type": song_type
        })

    # Isulat sa songs.json file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(songs, f, indent=2, ensure_ascii=False)

    print(f"✅ Tagumpay! Naiproseso ang {len(songs)} kanta at naisulat sa '{OUTPUT_FILE}'.")

if __name__ == '__main__':
    generate_json()
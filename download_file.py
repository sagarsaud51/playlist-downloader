import json
import os
from yt_dlp import YoutubeDL

def load_playlist(file_path):
    """Load playlist JSON from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def download_track(track_info, folder_path):
    """Download a single track to the specified folder."""
    search_query = f"{track_info['artist']} - {track_info['track']}"
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'default_search': 'ytsearch',
        'noplaylist': True,
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

def process_playlist(playlist_path, folder_path):
    """Process a single playlist file."""
    playlist_data = load_playlist(playlist_path)
    print(playlist_data)
    folder_name = playlist_data.get('playlist_name').replace(' ', '-')
    folder_path = os.path.join(folder_path, folder_name)

    # Ensure the specific playlist directory exists
    os.makedirs(folder_path, exist_ok=True)

    for song in playlist_data.get('songs', []):
        try:
            download_track(song, folder_path)
        except Exception as e:
            print(f"Error downloading {song['artist']} - {song['track']}: {e}")

def read_and_process_playlists(directory="playlists", log_file="processed_playlists.log"):
    """Read all JSON files in a directory and process them if not already done."""
    processed_files = set()
    if os.path.exists(log_file):
        with open(log_file, 'r', encoding='utf-8') as file:
            processed_files = set(file.read().splitlines())

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if filename.endswith(".json"):
            if filename in processed_files:
                print(f"Skipping already processed file: {file_path}")
            else:
                print(f"Processing file: {file_path}")
                process_playlist(file_path, 'downloads')
                with open(log_file, 'a', encoding='utf-8') as file:
                    file.write(filename + '\n')

if __name__ == "__main__":
    # Ensure the downloads directory exists
    os.makedirs('downloads', exist_ok=True)
    read_and_process_playlists("playlists")  # Update with your actual directory

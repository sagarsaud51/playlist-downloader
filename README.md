# Playlist Downloader

The Playlist Downloader script automates the process of downloading tracks from playlists defined in JSON format. It uses yt-dlp to search and download tracks from YouTube, converting them to MP3 format for local playback.

## Features
 - Reads playlists from JSON files.
 - Downloads each track in the playlist from YouTube.
 - Converts downloaded videos to MP3 format.
 - Skips already processed playlists to avoid redundancy.

## Requirements
- Python 3.6 or newer
- yt-dlp
- ffmpeg


## Setup
1. Clone the repository:

    ```
    git clone https://github.com/sagarsaud51/playlist-downloader.git

    cd playlist-downloader
    ```

2. Install dependencies:

Ensure you have Python installed on your system. Then, install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

3. Install FFmpeg:
Make sure you have FFmpeg installed on your system as it is required for converting videos to audio files. Visit FFmpeg's official site for installation instructions.

## Usage
1. Create JSON files for your playlists in the **playlists** directory. Each JSON file should follow this format:
```
{
  "playlist_name": "My Favorite Songs",
  "songs": [
    {
      "artist": "Artist Name",
      "track": "Track Name"
    },
    ...
  ]
}
```

2. Run the script:

```
python download_file.py
```

The script will process each playlist, downloading and converting each track into an MP3 file, organized into folders by playlist name within the downloads directory.

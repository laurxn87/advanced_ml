import spotipy 
from spotipy.oauth2 import SpotifyOAuth
from playback import Playback
from playback_display import PlaybackDisplay
from librespot_manager import LibrespotManager
from pathlib import Path 

scope = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
playback = Playback(sp)

print("\nSpotify Playback Control")

project_root = Path(__file__).resolve().parent
print(project_root)

librespot = LibrespotManager(project_root)
librespot.start()

while True:

    # Display current song info
    current_song = playback.get_current_song()

    # Keep showing the display while the song remains the same
    while True:

        try:
            if current_song is None:
                break

            display = PlaybackDisplay(current_song, playback)
            display.show_display()

            next_song = playback.get_current_song()
            if next_song is None:
                break
            # stop loop if song changed
            if next_song.title != current_song.title or next_song.artist != current_song.artist:
                current_song = next_song
                break
            # otherwise continue showing the same song
            current_song = next_song

        except KeyboardInterrupt:
            print('EXITING PROGRAM')

        finally: 
            librespot.stop()

    
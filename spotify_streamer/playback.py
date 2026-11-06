import spotipy
from spotipy.oauth2 import SpotifyOAuth
from song import Song

class Playback:
    def __init__(self, sp: spotipy.Spotify):
        self.sp = sp
        self.current_song = self.get_current_song()
        # Call current_playback() once to avoid repeated calls that may return None
        playback = sp.current_playback()
        self.is_playing = bool(playback and playback.get('is_playing'))

    def play(self, song: str) -> None:
        self.current_song = song
        self.is_playing = True
        self.sp.start_playback()  # Start playback using Spotipy
        print(f"Playing: {song}")

    def pause(self) -> None:
        if self.is_playing:
            self.is_playing = False
            self.sp.pause_playback()
            print(f"Paused: {self.current_song}")
        else:
            print("No song is currently playing.")
    
    def next_track(self) -> None:
        self.sp.next_track()
        self.current_song = self.get_current_song()
        print(f"Next track: {self.current_song}")

    def previous_track(self) -> None:
        self.sp.previous_track()
        self.current_song = self.get_current_song()
        print(f"Previous track: {self.current_song}")

    def get_current_song(self) -> Song | None:
        current_song = self.sp.current_user_playing_track()
        song = None
        if current_song is None:
            print("No song is currently playing.")
        else:
            song = Song(
                title=current_song['item']['name'],
                artist=current_song['item']['artists'][0]['name'],
                album_name=current_song['item']['album']['name'],
                album_art_uri=current_song['item']['album']['images'][0]['url'] if current_song['item']['album']['images'] else "",
                duration_ms=current_song['item']['duration_ms'],
                progress_ms=current_song['progress_ms']
            )
        self.current_song = song #update the current song attribute
        return song

    def get_current_song_info(self) -> dict | None:
        current_song = self.sp.current_user_playing_track()
        if current_song is None:
            print("No song is currently playing.")
            return None
        else:
            return {
                "title": current_song['item']['name'],
                "artist": current_song['item']['artists'][0]['name'],
            }
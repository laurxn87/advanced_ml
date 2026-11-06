from song import Song
from playback import Playback
from common import Common

class PlaybackDisplay:
    def __init__(self, song: Song | None, playback: Playback):
        self.song = song
        self.playback = playback
        # Guard against song being None and lyrics being missing
        self.current_lyric = (
            self.song.lyrics.get_lyric_at_time(self.song.progress_ms / 1000)
            if (self.song and getattr(self.song, 'lyrics', None))
            else None
        )

    def show_song_info(self) -> None:
        if self.song and self.song.title and self.song.artist:
            print(f"Now Playing: {self.song.title} by {self.song.artist}")
            print(f"Album: {self.song.album_name}")
            print(f"Duration: {self.song.duration_ms} ms")
            print(f"Progress: {self.song.progress_ms} ms")
        else:
            print("No song is currently playing.")

    def show_album_art(self) -> None:
        album_art_uri = getattr(self.song, 'album_art_uri', None) if self.song else None
        if album_art_uri:
            try:
                # Convert the album art URI to an ASCII image
                ascii_art = Common().convert_album_art_to_ascii(album_art_uri=album_art_uri, width=20)
                print(ascii_art)
            except Exception as e:
                print(f"Error displaying album art: {e}")
        else:
            print("No album art available.")


    def show_lyrics(self) -> None:
        if self.song and self.song.lyrics:
            # get the lyric at the current progress time plus 1000 milliseconds to anticipate the next lyric
            next_lyric = self.song.lyrics.get_lyric_at_time(self.song.progress_ms + 1000) if self.song and self.song.lyrics else None
            if next_lyric != self.current_lyric:
                self.current_lyric = next_lyric
                print(next_lyric)
            else:
                return

    def show_display(self):
        # display the song name 
        self.show_song_info()

        # display the song album art
        self.show_album_art()

        # whilst the same song is playing (title and artist), display the lyrics
        playback_song = self.playback.get_current_song_info()

        def get_song_title_and_artist(song_info):
            if isinstance(song_info, dict):
                return song_info.get('title'), song_info.get('artist')
            return getattr(song_info, 'title', None), getattr(song_info, 'artist', None)

        while self.playback.is_playing:
            playback_title, playback_artist = get_song_title_and_artist(playback_song)
            current_title = getattr(self.song, 'title', None)
            current_artist = getattr(self.song, 'artist', None)

            # exit the loop if the song has changed
            if playback_title != current_title or playback_artist != current_artist:
                break

            self.show_lyrics()

            if self.song:
                self.song.update_progress()  # Update the song's progress

            playback_song = self.playback.get_current_song_info()

            
        
        
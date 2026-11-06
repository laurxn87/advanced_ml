from lyrics import Lyrics
import time 

class Song: 
    def __init__(self, title: str, artist: str, album_name: str, album_art_uri: str, duration_ms: int, progress_ms: int):
        self.title = title
        self.artist = artist
        self.album_art_uri = album_art_uri
        self.album_name = album_name
        self.progress_ms = progress_ms
        self.duration_ms = duration_ms
        self.lyrics = Lyrics(self.title, self.artist)
        self.check_time = time.time()  # Store the start time for progress tracking


    def update_progress(self) -> None:
        time_elapsed = time.time() - self.check_time
        self.progress_ms = self.progress_ms + int(time_elapsed * 1000)  # Update progress in milliseconds
        self.check_time = time.time()  # Reset the check time for the next update
        # wait for a short duration to avoid rapid updates
        time.sleep(0.01)  # Sleep for 10 milliseconds to avoid rapid updates

    def __str__(self):
        return f"{self.title} by {self.artist} - {self.duration_ms} ms"
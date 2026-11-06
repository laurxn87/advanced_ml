import syncedlyrics
import re 

class Lyrics:
    def __init__(self, song_title: str, artist_name: str):
        self.song_title = song_title
        self.artist_name = artist_name
        self.lyrics = self._get_lyrics()  # Fetch lyrics when the object is created

    def _get_lyrics(self) -> list:
        lrc = syncedlyrics.search(f"{self.song_title} {self.artist_name}", lang='en', enhanced=True)
        if lrc:
            self.lyrics = self._parse_lrc(lrc)
            return self.lyrics
        else:
            return []  # No lyrics found

    def _parse_lrc(self, lrc_text: str) -> list:
        """Parses LRC text into a list of (seconds, text) tuples."""
        lyrics = []
        pattern = re.compile(r'\[(\d{2}):(\d{2})\.(\d{2,3})\]\s*(.*)')
        for line in lrc_text.strip().split('\n'):
            match = pattern.match(line.strip())
            if match:
                minutes, seconds, millis, text = match.groups()
                total_seconds = int(minutes) * 60 + int(seconds) + int(millis) / (1000 if len(millis) == 3 else 100)
                lyrics.append((total_seconds, text))
        return sorted(lyrics)

    def get_lyric_at_time(self, time_in_milliseconds: float) -> str:
        """Returns the active lyric text for a given time in seconds."""
        active_lyric = ""
        for time_tag, text in self.lyrics:
            if time_in_milliseconds >= time_tag * 1000:  # Convert milliseconds to seconds
                active_lyric = text
            else:
                break
        return active_lyric

                
    def __str__(self):
        return f"Lyrics for '{self.song_title}' by {self.artist_name}"
class Album:
    def __init__(self, title: str, artist: str, album_art_uri: str, year: int):
        self.title = title
        self.artist = artist
        self.year = year
        self.songs = [] 
        self.album_art_uri = album_art_uri  # Placeholder for album art URI

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.year})"
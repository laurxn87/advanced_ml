class Playlist:
    def __init__(self, name: str, owner: str):
        self.name = name
        self.owner = owner
        self.songs = []

    def __str__(self):
        return f"{self.name} - {len(self.songs)} songs"
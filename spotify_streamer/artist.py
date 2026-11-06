class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def __str__(self):
        return f"{self.name} - {len(self.albums)} albums"
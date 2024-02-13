class Track:
    """Track represents a singular piece of music on Spotify"""

    def __init__(self, name, id, artist):
        """
        :param name: Track name
        :param id: Spotify ID
        :param artist: Artist of Track
        """
        self.name = name
        self.id = id
        self.artist = artist

    def create_spotify_uri(self):
        return f"spotify:track:{self.id}"

    def __str__(self):
        return f"{self.name} by {self.artist}"
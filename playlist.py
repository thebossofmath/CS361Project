class Playlist:
    """Playlist is a Spotify playlist"""

    def __init__(self, name, id):
        """
        :param name: Name of Playlist
        :param id: Id of Playlist
        """
        self.name = name
        self.id = id

    def __str__(self):
        return f"Playlist {self.name}"
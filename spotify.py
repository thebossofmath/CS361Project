import json
import requests
from track import Track
from playlist import Playlist


class Spotify:
    """Spotify will use the spotify API to create playlist"""

    def __init__(self, auth_token, id):
        """
        :param auth_token: Spotify API token
        :param id: Spotify User id
        """
        self.auth_token = auth_token
        self.id = id

    def create_playlist(self):
        data = json.dumps({
            "name": "Randomly Generated Taylor Swift Playlist",
            "description": "This playlist was generated using an app developed in CS 361",
            "public": True
        })
        url = f"https://api.spotify.com/v1/users/{self.id}/playlists"
        response = self.post_api_request(url, data)
        response_json = response.json()
        playlist_id = response_json["id"]
        playlist = Playlist("Randomly Generated Taylor Swift Playlist", playlist_id)
        return playlist

    def populate_playlist(self, playlist, tracks):
        tracks_uris = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(tracks_uris)
        url = f"https://api.spotify.com/v1/playlists/{playlist.id}/tracks"
        response = self.post_api_request(url, data)
        response_json = response.json()
        return response_json
    def post_api_request(self, url, data):
        response = requests.post(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.auth_token}"
            }
        )
        return response

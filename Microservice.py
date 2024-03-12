
import zmq
from spotify import Spotify
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

user_id = "1287914872"
auth_code = "BQDD_lsaSIXlK-QuWBaFn-mdpH4WLikk2Z8iLVrXuK8eo5YODTiJNK_kTSyKa0XXaihMeHyr1ivRsMRL13iwmxop32LHYCIkturVk7Zi-oLTrlnz9aA"
server = Spotify(auth_code, user_id)

while True:
    artist_id = socket.recv()
    print(f"Received artist id: {artist_id}")
    artist_id = artist_id.decode("utf-8")
    albums = server.get_albums(artist_id)
    track_ids = []
    # loop through all the albums
    for album in albums["items"]:
        tracks = server.get_tracks(album["id"])
        # loop through all the tracks in the album
        for track in tracks["items"]:
            track_ids.append(track["id"])
    # choose a random song from our list
    chosen_id = random.choice(track_ids)
    print(f"Sending track id: {chosen_id}")
    socket.send_string(chosen_id)
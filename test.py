import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json
import os

load_dotenv()
DEVI_ID = os.getenv("DEVI_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# Spotify Authentication
spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080/callback",
                                                scope="user-read-currently-playing,user-read-playback-state,user-modify-playback-state"))

album_id = '1054179831081'
with open('albums.json', 'r') as file:
    mapping = json.load(file)


album_info = mapping[album_id]

current_playing = spfy.current_playback()['item']['album']['uri']

requested_album = album_info['request_body']['context_uri']

if current_playing == requested_album:
    print("Already playing requested album")
else:
    spfy.start_playback(device_id=DEVI_ID, context_uri=album_info['request_body']['context_uri'], offset={"position":0})

# spfy.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1YWoHzj5wHnG7m6gLlwBQd')

#current = spfy.current_user_playing_track()




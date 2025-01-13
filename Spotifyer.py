import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
DEVI_ID = os.getenv("DEVI_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def play(album_id):
    spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8080/callback",
                                                scope="user-read-currently-playing,user-read-playback-state,user-modify-playback-state"))
    
    with open('albums.json', 'r') as file:
        mapping = json.load(file)

    try:
        album_info = mapping[album_id]
    except KeyError:
        return
    
    current_playing = spfy.current_playback()['item']['album']['uri']
    requested_album = album_info['request_body']['context_uri']

    if current_playing == requested_album:
        print("Already playing requested album")
    else:
        print("Playing "+album_info['name'])
        spfy.start_playback(device_id=DEVI_ID, context_uri=album_info['request_body']['context_uri'], offset={"position":0})
    
    return spfy.current_playback()
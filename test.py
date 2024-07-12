#!/usr/bin/env python
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import json

DEVICE_ID=""
CLIENT_ID=""
CLIENT_SECRET=""

# Spotify Authentication
spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-read-currently-playing,user-read-playback-state,user-modify-playback-state"))

spfy.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:1YWoHzj5wHnG7m6gLlwBQd')
#current = spfy.current_user_playing_track()

# print(json.dumps(current, sort_keys=True, indent=4))
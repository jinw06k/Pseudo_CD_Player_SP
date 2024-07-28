#!/usr/bin/env python
import requests
from Refresh import Refresh
import json

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
SPOTIFY_API_URL = "{}/{}".format(SPOTIFY_API_BASE_URL, API_VERSION)

DEVICE_ID=""

def play(album):
    authorization_header = getAuthorizationHeader()
    play_endpoint = "{}/me/player/play?device_id={}}".format(SPOTIFY_API_URL, DEVICE_ID)

    # before requesting, get current playing info and compare to the album. 
    # If the album is already playing, don't send the request
    play_request = requests.put(play_endpoint, headers=authorization_header, data=json.dumps(album['spotify_body']))

    return play_request.status_code
                
def getAuthorizationHeader():
    refreshCaller = Refresh()
    authorization_header = {"Authorization": "Bearer {}".format(refreshCaller.refresh())}
    return authorization_header
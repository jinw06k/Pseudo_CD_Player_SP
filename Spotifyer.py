#!/usr/bin/env python
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
from RFID_Reader import *

DEVICE_ID=""
CLIENT_ID=""
CLIENT_SECRET=""

while True:
    try:
        spfy = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080/callback",
                                                       scope="user-read-currently-playing,user-read-playback-state,user-modify-playback-state"))
        
        # new scan?
        while True:
            current_playing = spfy.current_user_playing_track()

            print("Waiting for new scan...")
            album_json = read_album_json()
            print("Album name is:", album_json['name'])
            
            if (id==-1):
                sleep(3)
            
            else:
                if current_playing is not None:
                    if (current_playing['item']['album']['uri'] == album_json['uri']):
                        continue
                else:
                    spfy.start_playback(device_id=DEVICE_ID, context_uri=album_json['uri'])
                    sleep(2)
                
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
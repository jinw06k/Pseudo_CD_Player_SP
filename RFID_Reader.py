# from adafruit_pn532.i2c import PN532_I2C

# https://github.com/adafruit/Adafruit_Python_PN532/tree/master
import Adafruit_PN532 as PN532
import json
import board
import busio
from digitalio import DigitalInOut

import RPi.GPIO as GPIO
from Spotifyer import *

SSEL = 18 # Blue
MOSI = 17 # Orange
MISO = 27 # Green
SCLK = 22 # Yellow

pn532 = PN532.PN532(cs=SSEL, sclk=SCLK, mosi=MOSI, miso=MISO)
pn532.begin()
pn532.SAM_configuration()


def read_album_json():
    id = pn532.read_passive_target(timeout=0.5)
    album_json = get_id_json_mapping(id)
    return album_json


def get_id_json_mapping(rfid_id):
    with open('id_to_playlist_mapping.json', 'r') as mapping_file:
        mapping = json.load(mapping_file)

    try:
        album_json = mapping[rfid_id]
    except KeyError:
        print('This card has not been linked to a command')
        album_json = 0

    return album_json

def main():
    try:
        while True:
            alb = read_album_json()
            play(alb)

    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
    except Exception:
        GPIO.cleanup()
        raise

def authenticate():
    pass

if __name__ == "__main__":
    main()
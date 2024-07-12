from adafruit_pn532.i2c import PN532_I2C
import json
import board
import busio
from digitalio import DigitalInOut

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)

# harware reset
reset_pin = DigitalInOut(board.D6)
# On Raspberry Pi, you must also connect a pin to P32 "H_Request" for hardware
req_pin = DigitalInOut(board.D12)
pn532 = PN532_I2C(i2c, debug=False, reset=reset_pin, req=req_pin)

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
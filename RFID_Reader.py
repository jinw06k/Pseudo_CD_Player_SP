import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from Spotifyer import *
from time import sleep

reader = SimpleMFRC522()

def startListening():
    try:
        while True:
            id = reader.read()[0]
            print(id)
            play(str(id))
            sleep(3)
            
    except Exception:
        GPIO.cleanup()
        raise

def main():
    startListening()

if __name__ == "__main__":
    main()
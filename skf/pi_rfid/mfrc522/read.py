import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try: 
        print("Nå skal vi se om vi får data ")
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup() 
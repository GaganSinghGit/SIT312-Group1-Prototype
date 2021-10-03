import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import requests
import time
import os
from datetime import datetime


GPIO.setwarnings(False)

reader= SimpleMFRC522()

def read_card():
    card_d = None
    card_id, name = reader.read()
    now = datetime.now()
    return card_id, now

values = []
def store_values(value, DT):
    DT_string = DT.strftime("%d/%m/%Y %H:%M:%S")
    values.append([value, DT_string])
    
    


def main():
    try:
        card_id, DT = read_card()
        if card_id != None:
            print(card_id)
            store_values(card_id, DT)
        print(values)
        main()
    except KeyboardInterrupt:
        print("Quit")
        GPIO.cleanup()

main()


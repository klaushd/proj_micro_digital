import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

nome_lista = ["Pedro", "Aline", "Guilherme", "Klaus", "Victor", "Sergio", "Murilo"]

def get_num():
    """Use input() to get a valid number from 1 to 8. Retry till success!"""
    i = 0
    while (i > 8) or (i < 1):
        try:
            i = int(input("Enter ID # from 1-8: "))
            #nome_unico = input('Digite o seu nome: \n')
            #nome_lista.insert(get_num()-1, nome_unico)
            print(nome_lista[i-1])       
        except ValueError:
            pass
    return i

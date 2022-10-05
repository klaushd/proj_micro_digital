import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

from numero_digital import *
import serial
uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)

finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

nome_lista = ["Pedro", "Aline", "Guilherme", "Klaus", "Victor", "Sergio", "Murilo"]

def get_name():
    """input your name"""
    while (i > 1) or (i < 8):
        try:
            
        except ValueError:
            pass
    return nome_unico
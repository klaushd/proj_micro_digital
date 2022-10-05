# Espaço para importação dos códigos

import time
import board
from digitalio import DigitalInOut, Direction
import adafruit_fingerprint
from gpiozero import LED
from time import sleep

# Importação das Funções

from cadastro_digital import *
from detalhe_digital import *
from numero_digital import *
from verifica_digital import *

# Programa Principal

led_red = LED(17)
led_green = LED(27)
 
if finger.read_templates() != adafruit_fingerprint.OK:
    raise RuntimeError("Failed to read templates")

if get_fingerprint():
    print("Detected #", finger.finger_id, "with confidence", finger.confidence)
    led_green.on()
    sleep(1)
    led_green.off()
    sleep(1)
else:
    print("Finger not found")
    led_red.on()
    sleep(1)
    led_red.off()
    sleep(1)
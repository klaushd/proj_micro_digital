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

if finger.delete_model(get_num()) == adafruit_fingerprint.OK:
    print("Deleted!")
else:                                                                                                                                                        
    print("Failed to delete")
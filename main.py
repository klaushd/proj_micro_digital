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
from check import *
from wrong import *


# Programa Principal

led_red = LED(17)
led_green = LED(27)
nome_lista = ["Pedro", "Aline", "Guilherme", "Klaus", "Victor", "Sergio", "Murilo"]

while True:
    print("----------------")
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    print("Fingerprint templates:", finger.templates)
    print("e) adicionar digital")
    print("f) buscar digital")
    print("d) deletar digital")
    print("----------------")
    c = input("> ")

    if c == "e":
         enroll_finger(get_num())
         #enroll_finger(get_name())
         
    if c == "f":
        if get_fingerprint():
            print("Detected #", finger.finger_id, "with confidence", finger.confidence)
            #print("Bem vindo,", nome_lista[finger.finger_id-1])
            led_green.on()
            sleep(1)
            check()
            led_green.off()
            sleep(1)
        else:
            print("Finger not found")
            led_red.on()
            sleep(1)
            wrong()
            led_red.off()
            sleep(1)
    if c == "d":
        if finger.delete_model(get_num()) == adafruit_fingerprint.OK:
            print("Deleted!")
        else:                                                                                                                                                        
            print("Failed to delete")
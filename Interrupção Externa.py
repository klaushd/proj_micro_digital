#! /usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as gpio
import time
def rotina_interrupcao():
    print("Entrou na Interrupcao")
gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)
gpio.setup(22, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.add_event_detect(22, gpio.RISING, callback=rotina_interrupcao, bouncetime=300)
try:
    while True:
        gpio.output(23, gpio.HIGH)
        time.sleep(2)
        gpio.output(23, gpio.LOW)
        time.sleep(2)
except Exception:
    gpio.cleanup()
exit()
import RPi.GPIO as gpio
import time

# Configurando como BCM, numeracao do GPIO
gpio.setmode(gpio.BCM)

# Configurando a direcao do pino
gpio.setup(24, gpio.IN, pull_up_down = gpio.PUD_DOWN)
try:
    while True:
        if (gpio.input(24) == 1):
            print("botão pressionado")
        else:
            print("botão desligado")
        time.sleep(0.2)
except:
    gpio.cleanup()
exit()

gpio.cleanup()
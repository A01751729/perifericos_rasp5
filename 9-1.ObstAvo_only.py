#ObstAvo_only.py
#Andrés Méndez Cortez
#obtiene lecturas digitales del sensor infrarojo

from gpiozero import DigitalInputDevice
from time import sleep

sensor = DigitalInputDevice(27)  # GPIO17

try:
    while True:
        if not sensor.value:
            print("Obstáculo detectado!")
        else:
            print("Sin obstáculos")
        sleep(0.1)
        
except KeyboardInterrupt:
    print("Programa terminado")

#us_sin_boton.py
#Andrés Méndez Cortez
#obtiene lecturas de distancia de un sensor ultrasonico

from gpiozero import DistanceSensor
from time import sleep

sensor=DistanceSensor(echo=24,trigger=23, max_distance=1.0)

try:
    while True:
            distancia=sensor.distance*100
            print(f"Distancia:{distancia:.3f} cm")
            sleep(1)

except KeyboardInterrupt:
    print("\n El  usuario interrumpió la medición.")

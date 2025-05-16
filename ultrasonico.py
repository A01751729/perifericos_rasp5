#ultrasonico.py
#Andrés Méndez Cortez
#un boton activa la lectura de un sensor ultrasonico de distancia

from gpiozero import DistanceSensor,Button
from time import sleep

sensor=DistanceSensor(echo=24,trigger=23, max_distance=1.0)
boton=Button(17)

try:
    while True:
        if boton.is_pressed:
            distancia=sensor.distance*100
            print(f"Distancia:{distancia:.3f} cm")
            sleep(1)
        else:
            print("Esperando boton")
            sleep(1)

except KeyboardInterrupt:
    print("\n El  usuario interrumpió la medición.")


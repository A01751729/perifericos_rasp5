#sensor_sonido.py
#Andrés Méndez Cortez
#obtiene lecturas si se detecta un sonido (ej aplausos)

from gpiozero import Button
from signal import pause

sonido=Button(17)
def detectar():
	print("Sonido detectado")

sonido.when_pressed=detectar

print("esperando..")
pause()

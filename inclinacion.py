#inclinacion.py
#Andrés Méndez Cortez
#revisa si el sensor de inclinacion se enciende

from gpiozero import Button
from signal import pause

sensor_i=Button(22)
sensor_i.when_pressed=lambda:print("inclinacion detectada")
print("pon el sensor vertical y luego muevelo")
pause()

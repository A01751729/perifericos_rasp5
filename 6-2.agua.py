#agua.py
#Andrés Méndez Cortez
#imprime si hay presencia de agua

from gpiozero import Button
from signal import pause

signal_pir=Button(24)
signal_pir.when_pressed=lambda: print ("Agua detectada")

print("mojalo (con cuidado) para probarlo")
pause()

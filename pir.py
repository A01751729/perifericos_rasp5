from gpiozero import Button
from signal import pause

signal_pir=Button(23)
signal_pir.when_pressed=lambda: print ("Movimiento detectado")

print("muevete para probarlo")
pause()

#led_boton.py
#Andrés Méndez Cortez
#controla el encendido de un led con un boton

from gpiozero import LED,Button
from time import sleep
from signal import pause
led= LED(17)
boton=Button(14)

try:
    while True:
        if boton.is_pressed:
            led.on()
            sleep(1)
        else:
            print("Esperando boton")
            led.off()
            sleep(1)

except KeyboardInterrupt:
    print("\n El  usuario interrumpió con teclado.")

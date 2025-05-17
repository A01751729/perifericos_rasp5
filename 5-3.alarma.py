#alarma.py
#Andrés Méndez Cortez
#si hay un sonido detectado el buzzer emite una alarma

from gpiozero import Button
from gpiozero import Buzzer
from time import sleep

zumbador = Buzzer(18)
sonido=Button(17)
try:
    while True:
    	if sonido.is_pressed:
    		zumbador.on()
    		sleep(0.2)
    		zumbador.off()
    		sleep(0.2)
except KeyboardInterrupt:
	zumbador.off()

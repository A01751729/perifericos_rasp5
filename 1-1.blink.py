#blink.py
#Andrés Méndez Cortez
#parpadea un led
from gpiozero import LED
from time import sleep

led= LED(17)

while True:
	led.on()
	sleep(1)
	led.off()
	sleep(1)

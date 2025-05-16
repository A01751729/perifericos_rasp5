from gpiozero import Buzzer
from time import sleep
Zumbador=Buzzer(18)

try:
	while True:
		Zumbador.on()
		sleep(0.5)
		Zumbador.off()
		sleep(0.5)
except KeyboardInterrupt:
	Zumbador.off()

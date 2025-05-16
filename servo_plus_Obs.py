#servo_plus_Obs.py
#Andrés Méndez Cortez
#si el sensor infrarojo detecta algo, se levanta el servo, como pluma de estacionamiento

from gpiozero import Servo
from gpiozero import DigitalInputDevice
from time import sleep

# Adjust pulse widths if needed for your servo
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
sensor = DigitalInputDevice(27)

try:
    while True:
        if not sensor.value:
            
            print("Obstáculo confirmado, levantando pluma")
            servo.mid()
        
        else:
        	print("No hay obstaculo, bajando pluma")
        	servo.min()
        sleep(0.05)
except KeyboardInterrupt:
    print("Program stopped")

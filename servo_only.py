from gpiozero import Servo
from time import sleep

# Adjust pulse widths if needed for your servo
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

try:
    while True:
        servo.mid()
        print("Mid position")
        sleep(1)
        
        servo.min()
        print("Min position")
        sleep(1)
        
        servo.max()
        print("Max position")
        sleep(1)

except KeyboardInterrupt:
    print("Program stopped")

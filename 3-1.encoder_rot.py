#encoder_rot.py
#Andrés Méndez Cortez
#marca la pocision del encoder en terminal

from gpiozero import RotaryEncoder
from signal import pause

encoder = RotaryEncoder(a=5, b=6, max_steps=100)

def posicion():
    print(f"Posición actual: {encoder.steps}")

encoder.when_rotated = posicion

print("gira la perilla")
pause()

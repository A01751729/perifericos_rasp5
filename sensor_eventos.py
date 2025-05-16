#sensor_eventos.py
#Andrés Méndez Cortez
#revisa si hay inclinación, agua o movimiento con el pir

from gpiozero import Button 
from signal import pause

# Crear el archivo y escribir cabecera
with open("registroSensores.txt", "w") as registroSensores:
    registroSensores.write("Registro de los eventos.\n")

# Funciones que abren y escriben en el archivo cada vez
def evento_inclinacion():
    with open("registroSensores.txt", "a") as f:
        f.write("Inclinación detectada\n")

def evento_movimiento():
    with open("registroSensores.txt", "a") as f:
        f.write("Movimiento detectado\n")

def evento_agua():
    with open("registroSensores.txt", "a") as f:
        f.write("Agua detectada\n")

# Asociar sensores a funciones
signal_tilt = Button(22)
signal_tilt.when_pressed = evento_inclinacion

signal_pir = Button(23)
signal_pir.when_pressed = evento_movimiento

signal_ag = Button(24)
signal_ag.when_pressed = evento_agua

print("Mueve el tip switch para probarlo")
print("Mueve el PIR para probarlo")
print("Ponle agua para probarlo")

pause()


#DHT11.py
#Andrés Méndez Cortez
#obtiene datos de temperatura y humedad con el DHT11 en un entorno virtual


import time
import adafruit_dht
import board

dht=adafruit_dht.DHT11(board.D4)

try:
	while True:
		temp=dht.temperature
		humedad=dht.humidity
		print(f"Temperatura: {temp}°C Humedad:{humedad}%")
		time.sleep(2)
except KeyboardInterrupt:
	print("Lectura detenida por el usuario")
except RuntimeError as Error:
	print(f"Error de lectura {Error}")

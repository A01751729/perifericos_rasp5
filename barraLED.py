from gpiozero import LEDBarGraph
from time import sleep

graph = LEDBarGraph(12,13,14,15,16,17,18,19,20,21)

try:
    while True:
        for i in range(11):  # encendido
            graph.value = i / 10
            sleep(0.5)
        for i in reversed(range(11)):  # apagado
            graph.value = i / 10
            sleep(0.3)
except KeyboardInterrupt:
    graph.off()
    print("apagado")

#!/usr/bin/env python3
from gpiozero import DigitalOutputDevice, Button
from time import sleep

class Keypad:
    def __init__(self, rows_pins, cols_pins, keys):
        """
        Initialize the Keypad with specified row and column pins and keypad layout.
        :param rows_pins: List of GPIO pins for the rows.
        :param cols_pins: List of GPIO pins for the columns.
        :param keys: List of keys in the keypad layout.
        """
        # Inicializa los pines de las filas como DigitalOutputDevice
        self.rows = [DigitalOutputDevice(pin) for pin in rows_pins]
        # Inicializa los pines de las columnas como Buttons
        self.cols = [Button(pin, pull_up=False) for pin in cols_pins]
        self.keys = keys  # Establece el diseño del teclado

    def read(self):
        """
        Read the currently pressed keys on the keypad.
        :return: A list of pressed keys.
        """
        pressed_keys = ""
        # Escanea cada fila y columna para identificar las teclas presionadas
        for i, row in enumerate(self.rows):
            row.on()  # Habilita la fila actual
            for j, col in enumerate(self.cols):
                if col.is_pressed:  # Verifica si el botón de la columna está presionado
                    # Calcula el índice de la tecla basado en la fila y columna
                    index = i * len(self.cols) + j
                    pressed_keys=self.keys[index]
            row.off()  # Deshabilita la fila actual
        return pressed_keys

try:
    # Configura filas, columnas y diseño del teclado
    rows_pins = [5, 6, 13, 19]
    cols_pins = [4, 17, 27, 22]
    keys = ["1", "2", "3", "A",
            "4", "5", "6", "B",
            "7", "8", "9", "C",
            "*", "0", "#", "D"]

    # Crea una instancia de la clase Keypad
    keypad = Keypad(rows_pins, cols_pins, keys)
 

    # Lee continuamente el teclado e imprime las nuevas teclas presionadas
    while True:
        pressed_keys = keypad.read()
        if pressed_keys:
        	print(pressed_keys)  # Imprime la lista de teclas presionadas
        sleep(0.3)  # Pequeña pausa para reducir la carga de la CPU

except KeyboardInterrupt:
    # Maneja una interrupción del teclado (Ctrl+C) para salir limpiamente
    pass

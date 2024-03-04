# /home/pi/Desktop/DetectorDeMugrientos/Code/LuzBlanca.py

import RPi.GPIO as GPIO  # Importa el módulo GPIO para interactuar con los pines de entrada y salida del Raspberry Pi.
import time  # Importa el módulo time para realizar pausas durante la ejecución del código.

# Define la clase ClaseLuzBlanca para controlar una luz mediante un relé.
class ClaseLuzBlanca:
    # El constructor de la clase que inicializa la luz con el pin del relé especificado.
    def __init__(self, pin_relay):
        self.pin_relay = pin_relay  # Almacena el pin del relé asignado a la luz.
        GPIO.setmode(GPIO.BCM)  # Configura los pines del GPIO en el modo BCM (Broadcom SOC channel).
        GPIO.setup(self.pin_relay, GPIO.OUT)  # Configura el pin del relé como salida.

    # Método para activar la luz. Hace que la luz parpadee durante la duración especificada.
    def play(self, duracion):
        tiempo_inicio = time.time()  # Registra el tiempo de inicio de la operación.
        # Bucle que mantiene la luz parpadeando durante la duración especificada.
        while (time.time() - tiempo_inicio) <= duracion:
            GPIO.output(self.pin_relay, GPIO.HIGH)  # Enciende la luz.
            time.sleep(0.1)  # Espera 0.1 segundos.
            GPIO.output(self.pin_relay, GPIO.LOW)  # Apaga la luz.
            time.sleep(0.1)  # Espera otros 0.1 segundos antes de continuar el bucle.

    # Método para detener la luz. Apaga la luz inmediatamente.
    def stop(self):
        GPIO.output(self.pin_relay, GPIO.LOW)  # Asegura que la luz esté apagada configurando el pin del relé en bajo.

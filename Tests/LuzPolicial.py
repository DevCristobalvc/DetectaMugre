import RPi.GPIO as GPIO  # Importa el módulo GPIO para controlar los pines de GPIO en el Raspberry Pi.
import time  # Importa el módulo time, que en este caso podría usarse para temporizaciones, aunque no se aplica directamente aquí.

# Define la clase ClaseLuzPolicial para manejar el encendido y apagado de una luz conectada a través de un relé.
class ClaseLuzPolicial:
    # Constructor de la clase que inicializa la luz con el pin del relé especificado.
    def __init__(self, pin_relay):
        self.pin_relay = pin_relay  # Almacena el número de pin del relé que controla la luz.
        GPIO.setmode(GPIO.BCM)  # Configura el sistema para usar la numeración de pines BCM (Broadcom).
        GPIO.setup(self.pin_relay, GPIO.OUT)  # Configura el pin del relé como salida.

    # Método para "activar" la luz, en este caso, simula el efecto de encender la luz policial.
    def play(self):
        GPIO.output(self.pin_relay, GPIO.HIGH)  # Establece el pin del relé en alto, encendiendo la luz.

    # Método para detener o apagar la luz.
    def stop(self):
        GPIO.output(self.pin_relay, GPIO.LOW)  # Establece el pin del relé en bajo, apagando la luz.

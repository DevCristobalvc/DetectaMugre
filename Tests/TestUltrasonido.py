import RPi.GPIO as GPIO
import time

# Configuración de pines para los sensores
TRIGGER_A = 18
ECHO_A = 24

TRIGGER_B = 8
ECHO_B = 23

# Distancia máxima para detener la medición (en centímetros)
DISTANCIA_MAXIMA = 250

# Tiempo de espera después de detectar una distancia menor a 250cm (en segundos)
TIEMPO_ESPERA = 2

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_A, GPIO.OUT)
GPIO.setup(ECHO_A, GPIO.IN)

GPIO.setup(TRIGGER_B, GPIO.OUT)
GPIO.setup(ECHO_B, GPIO.IN)

def medir_distancia(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, True)
    time.sleep(0.00001)
    GPIO.output(trigger_pin, False)

    inicio_tiempo = time.time()
    fin_tiempo = time.time()

    while GPIO.input(echo_pin) == 0:
        inicio_tiempo = time.time()

    while GPIO.input(echo_pin) == 1:
        fin_tiempo = time.time()

    duracion = fin_tiempo - inicio_tiempo
    distancia = (duracion * 34300) / 2  # La velocidad del sonido es aproximadamente 34300 cm/s

    return distancia

try:
    while True:
        distancia_A = medir_distancia(TRIGGER_A, ECHO_A)
        distancia_B = medir_distancia(TRIGGER_B, ECHO_B)

        print(f"Distancia Sensor A: {distancia_A:.2f} cm | Distancia Sensor B: {distancia_B:.2f} cm")

        if distancia_A < DISTANCIA_MAXIMA or distancia_B < DISTANCIA_MAXIMA:
            print("¡Objeto detectado!")
            time.sleep(TIEMPO_ESPERA)  # Espera antes de realizar la próxima medición
finally:
    GPIO.cleanup()

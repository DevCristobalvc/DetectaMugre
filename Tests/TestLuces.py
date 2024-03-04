import RPi.GPIO as GPIO
import time

# Configura el modo de la GPIO
GPIO.setmode(GPIO.BCM)

# Define el número del pin que estás utilizando
pin_relay = 17

# Configura el pin como salida
GPIO.setup(pin_relay, GPIO.OUT)

# Establece el tiempo total de ejecución en segundos
tiempo_total = 25
tiempo_paso = 0.1  # Tiempo de espera en cada paso (en segundos)

try:
    tiempo_inicio = time.time()  # Guarda el tiempo de inicio
    while (time.time() - tiempo_inicio) <= tiempo_total:
        # Activa el relé (enciende la tira LED)
        GPIO.output(pin_relay, GPIO.HIGH)
        time.sleep(tiempo_paso)

        # Desactiva el relé (apaga la tira LED)
        GPIO.output(pin_relay, GPIO.LOW)
        time.sleep(tiempo_paso)

    # Después de que el bucle termina, apaga las luces
    GPIO.output(pin_relay, GPIO.LOW)

finally:
    # Limpia la configuración de la GPIO antes de salir
    GPIO.cleanup()

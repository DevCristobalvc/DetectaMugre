# /home/pi/Desktop/DetectorDeMugrientos/Code/Ultrasonidos.py

import RPi.GPIO as GPIO  # Importa el módulo GPIO para controlar los pines de la Raspberry Pi.
import time  # Importa el módulo time para manejar los tiempos de espera.

GPIO.setwarnings(False)  # Desactiva las advertencias para evitar mensajes de salida no deseados al usar los pines de GPIO.

# Configuración de pines para los sensores de ultrasonidos.
TRIGGER_A = 18  # Define el pin de disparo para el primer sensor de ultrasonidos.
ECHO_A = 24  # Define el pin de eco para el primer sensor de ultrasonidos.
TRIGGER_B = 8  # Define el pin de disparo para el segundo sensor de ultrasonidos.
ECHO_B = 23  # Define el pin de eco para el segundo sensor de ultrasonidos.

# Configuración de GPIO.
GPIO.setmode(GPIO.BCM)  # Establece el modo de numeración de pines como BCM (Broadcom SOC channel).
GPIO.setup(TRIGGER_A, GPIO.OUT)  # Configura el pin de disparo del primer sensor como salida.
GPIO.setup(ECHO_A, GPIO.IN)  # Configura el pin de eco del primer sensor como entrada.
GPIO.setup(TRIGGER_B, GPIO.OUT)  # Configura el pin de disparo del segundo sensor como salida.
GPIO.setup(ECHO_B, GPIO.IN)  # Configura el pin de eco del segundo sensor como entrada.

def medir_distancia(trigger_pin, echo_pin):
    GPIO.output(trigger_pin, True)  # Activa el pin de disparo enviando un pulso.
    time.sleep(0.00001)  # Espera 10 microsegundos.
    GPIO.output(trigger_pin, False)  # Desactiva el pin de disparo.

    inicio_tiempo = time.time()  # Guarda el tiempo actual como el tiempo de inicio.
    fin_tiempo = time.time()  # Inicializa el tiempo de fin con el tiempo actual.

    while GPIO.input(echo_pin) == 0:  # Espera a que el pin de eco se ponga en alto.
        inicio_tiempo = time.time()

    while GPIO.input(echo_pin) == 1:  # Espera a que el pin de eco se ponga en bajo, indicando recepción del eco.
        fin_tiempo = time.time()

    duracion = fin_tiempo - inicio_tiempo  # Calcula la duración del pulso de eco.
    distancia = (duracion * 34300) / 2  # Calcula la distancia basándose en la velocidad del sonido (34300 cm/s) y el tiempo de ida y vuelta.

    return distancia  # Devuelve la distancia calculada.

def objeto_detectado(distancia_maxima):
    distancia_A = medir_distancia(TRIGGER_A, ECHO_A)  # Mide la distancia usando el primer sensor.
    distancia_B = medir_distancia(TRIGGER_B, ECHO_B)  # Mide la distancia usando el segundo sensor.
    return distancia_A < distancia_maxima or distancia_B < distancia_maxima  # Devuelve True si algún objeto está dentro de la distancia máxima.

def limpiar_pines():
    GPIO.cleanup()  # Limpia la configuración de los pines GPIO, es útil para reiniciar el estado de los GPIO cuando se termina de ejecutar el programa.

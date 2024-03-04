import RPi.GPIO as GPIO
import time

# Configuración inicial de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pines de los relés
PIN_LUZ_BLANCA = 17
PIN_LUZ_POLICIAL = 27

# Configuración de los pines como salida
GPIO.setup(PIN_LUZ_BLANCA, GPIO.OUT)
GPIO.setup(PIN_LUZ_POLICIAL, GPIO.OUT)

# Función para obtener el estado de la luz
def estado_luz(pin):
    estado = GPIO.input(pin)
    if pin == PIN_LUZ_POLICIAL:  # Si es el relé policial, el estado es inverso
        return "Encendida" if estado == GPIO.LOW else "Apagada"
    else:
        return "Encendida" if estado == GPIO.HIGH else "Apagada"

# Función para controlar las luces
def controlar_luces():
    while True:
        luz = input("Ingrese 'blanca' para la luz blanca, 'policial' para la luz policial, 'estado' para consultar el estado, o 'salir' para terminar: ")
        if luz == "salir":
            break
        elif luz == "estado":
            print("Estado luz blanca:", estado_luz(PIN_LUZ_BLANCA))
            print("Estado luz policial:", estado_luz(PIN_LUZ_POLICIAL))
            continue

        accion = input("Ingrese 1 para encender o 0 para apagar: ")
        
        if luz == "blanca":
            if accion == "1":
                GPIO.output(PIN_LUZ_BLANCA, GPIO.HIGH)  # Encender
            elif accion == "0":
                GPIO.output(PIN_LUZ_BLANCA, GPIO.LOW)   # Apagar
            else:
                print("Acción no reconocida.")
                
        elif luz == "policial":
            if accion == "1":
                GPIO.output(PIN_LUZ_POLICIAL, GPIO.HIGH)  # Encender (inverso)
            elif accion == "0":
                GPIO.output(PIN_LUZ_POLICIAL, GPIO.LOW) # Apagar (inverso)
            else:
                print("Acción no reconocida.")
                
        else:
            print("Selección de luz no reconocida.")

try:
    controlar_luces()
except KeyboardInterrupt:
    print("Programa terminado por el usuario.")
finally:
    GPIO.cleanup()
    print("GPIO limpio y programa terminado.")

# /home/pi/Desktop/DetectorDeMugrientos/Code/Main.py

# Importacion de biblioteca y modulo
import time # Controlar operaciones de tiempo
import RPi.GPIO as GPIO # Controlar los pines de Entrada/Salida

# importa archivos locales
from Ultrasonidos import objeto_detectado # Importa la función para detectar objetos con el sensor de ultrasonidos
from Foto import Camara # Importa la clase para manejar la cámara
from LuzBlanca import ClaseLuzBlanca # Importa la clase para controlar la luz blanca
from LuzPolicial import ClaseLuzPolicial # Importa la clase para controlar la luz policial
from Audio import ReproductorAudio # Importa la clase para reproducir audio
from CargaFTP import upload_file_to_praktil # Importa la clase para cargar la foto

# Constantes y configuraciones
DISTANCIA_MAXIMA = 200  # Define la distancia máxima en cm para la detección de objetos
DURACION_ACTIVIDAD = 23  # Duración en segundos de la actividad (luces encendidas, reproducción de audio)
TIEMPO_PARA_FOTO = 0  # Tiempo para tomar la foto después de detectar el objeto
ruta_audio = "/home/pi/Desktop/DetectorDeMugrientos/Audio/audio.wav" # Ruta del archivo de audio a reproducir
ruta_fotos = "/home/pi/Desktop/DetectorDeMugrientos/Fotos" # Directorio para guardar las fotos capturadas

# Creación de instancias de los dispositivos a utilizar
reproductor = ReproductorAudio(ruta_audio)  # Instancia para manejar la reproducción de audio
luzblanca = ClaseLuzBlanca(17)  # Instancia para controlar la luz blanca conectada al pin GPIO 17
luzpolicial = ClaseLuzPolicial(27)  # Instancia para controlar la luz policial conectada al pin GPIO 27
camara = Camara(ruta_fotos)  # Instancia para manejar la captura de fotos

# Funcion principal donde se hacen llamado a los metodos de los archivos 
def ejecutar_funcionalidades():
    
    while True:  # Bucle principal
        if objeto_detectado(DISTANCIA_MAXIMA): # Verifica si se detecta un objeto dentro de la distancia máxima
            
            # Declara nuevamente los pines por el Cleanup
            luzpolicial = ClaseLuzPolicial(27)
            luzblanca = ClaseLuzBlanca(17)
            print("¡Objeto detectado! Activando funcionalidades.")
            
            # Inicia reproducción del audio
            reproductor.play()
            
            # Espera para tomar la foto
            time.sleep(TIEMPO_PARA_FOTO)
            camara.play() # Toma la foto
            
            # Carga la foto a Praktil
            upload_file_to_praktil(camara.ruta_de_foto())
            
            # Enciende luces
            luzblanca.play(DURACION_ACTIVIDAD) # Parpadea la luz blanca durante DURACION_ACTIVIDAD
            luzpolicial.play() # Enciende la luz policial
            
            
            # Detiene todas las funcionalidades después de la ejecución
            reproductor.stop()
            luzblanca.stop()
            luzpolicial.stop()
            GPIO.cleanup([17, 27]) # En lugar de hacer stop, hacer cleanup para apagar todo

        time.sleep(1) # Espera 1 segundo antes de la próxima medición para evitar detecciones constantes

try:
    ejecutar_funcionalidades() # Ejecuta nuevamente el bucle 
    
except KeyboardInterrupt:
    print("Detención manual del programa.") # Permite detener el programa de forma manual con Ctrl+C
    
finally:
    GPIO.cleanup() # Limpia la configuración de los pines GPIO al finalizar el programa

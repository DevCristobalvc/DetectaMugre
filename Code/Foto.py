# /home/pi/Desktop/DetectorDeMugrientos/Code/Foto.py

import time  # Importa el módulo time para manejar operaciones relacionadas con el tiempo, como pausas.
import cv2  # Importa OpenCV (cv2) para operaciones relacionadas con la visión por computadora.
import os  # Importa el módulo os para interactuar con el sistema operativo, como manejo de archivos y directorios.

# Define la clase Camara para interactuar con una cámara web y guardar fotos.
class Camara:
    # Constructor de la clase que inicializa una instancia con una ruta de guardado especificada.
    def __init__(self, ruta_guardado):
        self.ruta_guardado = ruta_guardado  # Almacena la ruta de guardado de las fotos.
        self.ruta_completa = None # Inicializa la variable para su uso desde cualquier método

    # Método para capturar una foto con la cámara y guardarla.
    def play(self):
        cam = cv2.VideoCapture(0)  # Inicializa la captura de video con la primera cámara web disponible.
        time.sleep(0.5)  # Espera 0.5 segundos para permitir que la cámara se inicie correctamente.
        ret, frame = cam.read()  # Captura un fotograma de la cámara.

        # Verifica si el fotograma fue capturado correctamente.
        if ret:
            # Cuenta las fotos existentes en la ruta de guardado para nombrar la nueva foto de forma secuencial.
            fotos_existentes = len([nombre for nombre in os.listdir(self.ruta_guardado) if os.path.isfile(os.path.join(self.ruta_guardado, nombre))])
            nombre_archivo = f"foto_{fotos_existentes + 1}.jpg"  # Define el nombre del archivo de la nueva foto.
            self.ruta_completa = os.path.join(self.ruta_guardado, nombre_archivo)  # Construye la ruta completa donde se guardará la foto.
            cv2.imwrite(self.ruta_completa, frame)  # Guarda el fotograma capturado como una imagen JPG en la ruta especificada.
            print(f"Foto tomada y guardada en: {self.ruta_completa}")  # Imprime una confirmación con la ruta de la foto guardada.
        else:
            print("No se pudo capturar la imagen.")  # Informa si no se pudo capturar el fotograma.
            
    # Metodo para obtener la ruta de la foto tomada       
    def ruta_de_foto(self):
        return self.ruta_completa

    # Método stop para la cámara.
    def stop(self):
        pass  # Este método está vacío (indicado por 'pass') porque la liberación de la cámara no se maneja aquí.

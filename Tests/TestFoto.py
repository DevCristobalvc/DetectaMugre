# Importa las bibliotecas necesarias
import cv2
import os

# Define la función para tomar una foto
def tomar_foto(ruta_guardado):
    # Obtiene la cantidad actual de fotos en la carpeta
    fotos_actuales = len(os.listdir(ruta_guardado))

    # Inicializa la cámara
    cam = cv2.VideoCapture(0)

    # Lee la imagen de la cámara
    ret, frame = cam.read()

    # Cierra la cámara
    cam.release()

    if ret:
        # Guarda la imagen en la ruta especificada
        nombre_archivo = f"foto_{fotos_actuales + 1}.jpg"
        ruta_completa = os.path.join(ruta_guardado, nombre_archivo)
        cv2.imwrite(ruta_completa, frame)
        print(f"Foto tomada y guardada en: {ruta_completa}")
    else:
        print("No se pudo capturar la imagen.")

# Llamada a la función para tomar una foto
tomar_foto("/home/pi/Desktop/DetectorDeMugrientos/Fotos")

# Continúa con el resto del código de tu proyecto...

# /home/pi/Desktop/DetectorDeMugrientos/Code/Audio.py

import pygame  # Importa la biblioteca pygame, que se utiliza para crear videojuegos pero también ofrece soporte para la reproducción de audio.

class ReproductorAudio:
    # Constructor de la clase ReproductorAudio
    def __init__(self, ruta_audio):
        pygame.mixer.init()  # Inicializa el módulo mixer de pygame, que es necesario para la reproducción de sonido.
        pygame.mixer.music.load(ruta_audio)  # Carga el archivo de audio especificado por la ruta dada en el argumento 'ruta_audio'.

    # Método para comenzar la reproducción del audio
    def play(self):
        pygame.mixer.music.play()  # Inicia la reproducción del archivo de audio previamente cargado.

    # Método para detener la reproducción del audio
    def stop(self):
        pygame.mixer.music.stop()  # Detiene la reproducción del archivo de audio.


import pygame

class ReproductorAudio:
    def __init__(self, ruta_audio):
        pygame.mixer.init()
        pygame.mixer.music.load(ruta_audio)

    def reproducir(self):
        pygame.mixer.music.play()

    def detener(self):
        pygame.mixer.music.stop()

# Variables para controlar la reproducción
play = True
stop = False

# Ruta del archivo de audio
ruta_audio = "/home/pi/Desktop/DetectorDeMugrientos/Audio/audio.wav"

# Instanciar el objeto ReproductorAudio
reproductor = ReproductorAudio(ruta_audio)

# Control de la reproducción
if play:
    reproductor.reproducir()

if stop:
    reproductor.detener()

# DetectaMugre

### Objetivo
DetectaMugre es un proyecto que busca implementar una foto multa ambiental 

### Actualidad
En la version 1.4 mediante la activacion de sensores ultra sonio se realizan la activacion de, sonido, luces y camara, donde esta ultima mediante un protocolo ftp logra cargar las fotos a un host

### Materiales
Una raspberry pi 4 que controla, dos sensores ultrasonicos HC-SR04, camara web xxx, bafle de sonido xxx, interruptor 2 RELAY MODULE, tira led de un metro de largo, inversor electrico MH-Power MB, bateria de moto xxx, boton de encendido, jumpers H-m, M-h, M-m, H-h, amarras de 10 cm, Caja de madera 20cm x 20cm x 20cm

# Codigo

## Estructura de archivos
```
proyecto/
│
├── Audio/
│ ├── audio.wav
│ 
├── Code/
│ ├── Main.py
│ ├── Foto.py
│ ├── Ultrasonidos
│ ├── LuzBlanca.py
│ ├── LuzPolicial.py
│ ├── CargaFTP.py
│ ├── Audio.py
│ └── Iniciador.sh
│
├── Test/
│ ├── TestFoto.py
│ ├── TestUltrasonidos
│ ├── TestLuzBlanca.py
│ ├── TestLuzPolicial.py
│ ├── TestCargaFTP.py
│ ├── TestAudio.py
│
├── Fotos/
│
├── ChangeLog.txt
├── README.md
└── .gitignore
```
   

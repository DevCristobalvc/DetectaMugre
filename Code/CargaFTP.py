# /home/pi/Desktop/DetectorDeMugrientos/Code/CargaFTP.py

from ftplib import FTP

def upload_file_to_praktil(ruta_archivo_local):
    ftp = FTP()
    ftp.connect('ftp.praktil.co', 21)
    ftp.login(user='cristobal@praktil.co', passwd='Valencia9965.')
    ftp.cwd('/fotos')  # Cambia el directorio inicial al directorio /fotos
    nombre_archivo_remoto = ruta_archivo_local.split('/')[-1]  # Obtiene solo el nombre del archivo
    with open(ruta_archivo_local, 'rb') as archivo_local:
        ftp.storbinary('STOR ' + nombre_archivo_remoto, archivo_local)
    ftp.quit()

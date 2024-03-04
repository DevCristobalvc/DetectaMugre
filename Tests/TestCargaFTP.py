from ftplib import FTP

# Configura la conexión FTP al puerto 21 explícitamente
ftp = FTP()
ftp.connect('ftp.praktil.co', 21)
ftp.login(user='cristobal@praktil.co', passwd='Valencia9965.')

# Carga un archivo
nombre_archivo_local = '/home/pi/Desktop/DetectorDeMugrientos/Fotos/foto_1.jpg'
nombre_archivo_remoto = 'foto_1.jpg'

with open(nombre_archivo_local, 'rb') as archivo_local:
    ftp.storbinary('STOR ' + nombre_archivo_remoto, archivo_local)

# Cierra la conexión FTP
ftp.quit()

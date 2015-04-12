# -*- coding: utf-8 -*-

import sys
import MySQLdb
import string
import os

#copias de carpetas
os.system("cp -R /var/www /home/bakup")
os.system("cp -R /srv/titaniumsystem /home/backup")
os.system("cp -R /etc/apache2/sites-available/ /home/backup")
os.system("cp -R /var/lib/mysql /home/backup")


#exportacion de la base de datos
os.system("mysqldump --user=1234 --password=1234 -A > /home/backup/backup.sql")



#compresion en un .zip 
os.system("zip -R /home/backup/'date'.zip")

#os.listdir("/home/backup")
os.system("cd /home/backup")

for archivozip in os.listdir("/home/backup"):
	if archivozip.endswith(".zip"):
		#copia backup
		os.system("scp archivozip backup@jarvir.titaniumsystem.es:/home/backup")

	else
		print "No hay archivos zip en el directorio"


#borramos todo el contenido del directorio backup para dejarlo limpio
os.system("rm -R /home/backup")





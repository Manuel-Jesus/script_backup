# -*- coding: utf-8 -*-

import sys
import MySQLdb
import string
import os



#copias de carpetas
os.system("cp -R /var/www /home/bakup")
os.system("cp -R /srv/titaniumsystem /home/backup")
os.system("cp -R /etc/apache2/sites-enabled/ /home/backup")
os.system("cp -R /etc/apache2/sites-avaiable/ /home/backup")
#os.system("cp -R /var/lib/mysql /home/backup")#ya hacemos mysqldump


#exportacion de la base de datos
os.system("mysqldump --user=11111 --password=11111 -A > /home/backup/backup.sql")



#compresion en un .zip
fecha=time.strftime("%x").replace('/','_')

os.system("zip -R /home/backup/"+fecha+".zip")

#os.listdir("/home/backup")
os.system("cd /home/backup")

hayarchivozip = False

for archivozip in os.listdir("/home/backup"):
        if archivozip.endswith(".zip"):
                #copia backup
                os.system("sshpass -p '1111' scp archivozip backup@192.168.122.188:/home/backup")
                hayarchivozip = true

if not hayarchivozip:
        print "no hay archivo zip"



#borramos todo el contenido del directorio backup para dejarlo limpio
os.system("rm -R /home/backup")

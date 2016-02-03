# -*- coding: utf-8 -*-
import time
import json
import string
import os


#cargamos la configuracion

settingsf=open("settings.json")
settings=json.load(settingsf)
directorios=settings["directorios"]
directorioTemporal=settings["directorioTemporal"]
destino_user=settings["destino_user"]
destino_host=settings["destino_host"]
destino_dir=settings["destino_dir"]
sql_usuario=settings["sql_usuario"]
sql_pass=settings["sql_pass"]

#copias de carpetas
for carpeta in directorios:
    os.system("cp -R "+carpeta+" "+directorioTemporal)

#compresion en un .zip
fecha=time.strftime('%Y_%m_%d')
os.system("zip -R /home/backup/"+fecha+".zip")

#exportacion de la base de datos
os.system("mysqldump --user="+sql_usuario+" -p"+sql_pass+" -A > "+directorioTemporal+fecha+".sql")


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

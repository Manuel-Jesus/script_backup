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

#calculamos la fecha
fecha=time.strftime('%Y-%m-%d')

#exportacion de la base de datos
os.system("mysqldump --user="+sql_usuario+" -p"+sql_pass+" -A > "+directorioTemporal+fecha+".sql")
os.system("zip "+directorioTemporal+fecha+".zip")
for carpeta in directorios:
    os.system("zip -R "+directorioTemporal+fecha+".zip" + " "+carpeta)

# -*- coding: utf-8 -*-
import time
import json
import string
import os

#calculamos la fecha en el formato necesario
fecha=time.strftime('%Y-%m-%d')

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
hostname=settings["hostname"]
local_load_folder=settings["local_load_folder"]
nombreArchivo=hostname+"_"+fecha
direccionArchivo=local_load_folder+nombreArchivo


#montando directorio remoto

os.system("sshfs "+destino_user+"@"+destino_host+":"+destino_dir+" "+local_load_folder+" -o IdentiyFile=~/.ssh/"+hostname)


#exportacion de la base de datos
os.system("mysqldump --user="+sql_usuario+" -p"+sql_pass+" -A > "+direccionArchivo+".sql")
#print ("mysqldump --user="+sql_usuario+" -p"+sql_pass+" -A > "+direccionArchivo+".sql")
os.system("zip -r "+direccionArchivo+".zip "+direccionArchivo+".sql")
os.system("rm "+direccionArchivo+".sql")#borrando archivo sql innecesario


#Comprimiendo directorios indicados
for carpeta in directorios:
    os.system("zip -r "+direccionArchivo+".zip" + " "+carpeta)

#Copiamos archivo a la maquina de destino con SCP
#os.system("scp -i ~/.ssh/"+hostname+" "+direccionArchivo+".zip "+destino_user+"@"+destino_host+":"+destino_dir)

#borramos el zip creado

##os.system("rm "+direccionArchivo+".zip")

#Desmontamos el directorio remoto

os.system("umount "+local_load_folder)

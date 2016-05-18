# -*- coding: utf-8 -*-
import json
import string
import os


print("ATENCION: este programa requiere que el usuario introduzca la contraseña del usuario y host de destino")
#cargamos la configuracion necesaria en este caso
settingsf=open("settings.json")
settings=json.load(settingsf)
destino_user=settings["destino_user"]
destino_host=settings["destino_host"]
hostname=settings["hostname"]

#Creamos una clave ssh:
os.system('ssh-keygen -b 4096 -t rsa -f ~/.ssh/'+hostname+' -q -N ""')

#Copiamos la clave ssh al destino

os.system('ssh-copy-id -i ~/.ssh/'+hostname+' '+destino_user+'@'+destino_host)

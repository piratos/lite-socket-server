#!/usr/bin/python
#client server python  sayf_piratos
import socket, sys

HOST = '41.231.22.148'
PORT = 50000
#socket creation
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#try to connect to server
try:
	my_socket.connect((HOST,PORT))
except socket.error:
	print "[-] cannot connect to server %s on port %s" %(HOST, PORT)
	sys.exit()
print "[+] connected to server %s on port %s" %(HOST, PORT)
msg_server = my_socket.recv(1024)

while 1:
	if msg_server.upper() in ("END", ""):
		break
	print "[+]<< ", msg_server
	msg_client=raw_input("[+]>> ")
	my_socket.send(msg_client)
	msg_server = my_socket.recv(1024)
#stop connection
print "[-] Connection ended !"
my_socket.close()

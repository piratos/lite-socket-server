#!/usr/bin/python
import socket, sys
HOST = '192.168.150.1'
PORT = 50000
# socket creation
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# trying to bind
try:
	my_socket.bind((HOST, PORT))
except socket.error:
	print "[-] socket adress linking has encoutered a problem !"
	sys.exit()

while 1:
	print "[*] waiting for new connections .."
	my_socket.listen(5)
	#connecting
	connection, adress = my_socket.accept()
	print "[+] New client connected with ip %s , port %s" %(adress[0], adress[1])
	#send server respence
	connection.send("welcome in my server :)")
	msg_client=connection.recv(1024)
	while 1:
		print "[++]<< ",msg_client
		if msg_client.upper() in ("END",""):
			break
		msg_server = raw_input("[++]>> ")
		connection.send(msg_server)
		msg_client = connection.recv(1024)
	#ending connection
	connection.send("ending session on this server ! GoodBye !")
	print"[-] connection ended !"
	connection.close()
	
	answer = raw_input("<C>ontinue or <E>nd ? ")
	if answer.upper()=="E":
		break

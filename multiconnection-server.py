#!/usr/bin/python
#sayf_piratos multi connection socket ezrver handler
HOST = raw_input("[+] enter the ip to listen to : ")
PORT=40000

import socket, sys, threading

class ThreadClient(threading.Thread):
	
	def __init__(self, conn, name):
		threading.Thread.__init__(self)
		self.connection = conn
		self.name = name

	def run(self):
		while 1:
			msg_client = self.connection.recv(1024)
			if msg_client.upper() in ("END",""):
				break
			message = "[+]%s >>> %s " %(self.name, msg_client)
			print message
			for key in connected_clients:
				if key != self.name:
					connected_clients[key].send(message)
		self.connection.close()
		del connected_clients[self.name]
		print "[-] client %s disconnected !" %self.name
		print "[*] clients connected are : %s" %str(connected_clients.keys())

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	my_socket.bind((HOST, PORT))
except :
	print "[-] cannot connect to address %s on port %s" %(HOST, PORT)
	sys.exit
print "[+] connection to %s established on port %s" %(HOST, PORT)
print "[*] waiting for messages ..."
my_socket.listen(5)
connected_clients={}
while 1:
	connection, address = my_socket.accept()
	name = connection.recv(1024)
	th = ThreadClient(connection,name)
	th.start()
	connected_clients[th.name] = connection
	print "[*] client %s connected, ip adress %s, port %s." %(th.name, address[0], address[1])

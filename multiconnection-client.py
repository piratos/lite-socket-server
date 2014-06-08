#!/usr/bin/python
#sayf_piratos multiconnection handler server
import socket, sys, threading

HOST = raw_input("[+] enter the server's ip to connect to : ")
PORT=40000

class ThreadReception(threading.Thread):
	
	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection = conn #socket connection reference

	def run(self):
		while 1:
			recieved_message = self.connection.recv(1024)
			print recieved_message
			if recieved_message.upper() in ("END",""):
				break
		th_E._Thread__stop()
		print "[-] connection ended !"
		self.connection.close()

class ThreadEmission(threading.Thread):

	def __init__(self, conn):
		threading.Thread.__init__(self)
		self.connection = conn #socket connection reference
		print "[+]>>> what is your name ?"
		sent_message = raw_input("[+]>>> ")

	def run(self):
		while 1:
			sent_message = raw_input("[+]>>> ")
			self.connection.send(sent_message)
#connecting
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	connection.connect((HOST, PORT))
except socket.error:
	print "[-] connection failed !"
	sys.exit()
print "[+] connection established with server"
#start threads both send and recieve one
th_E = ThreadEmission(connection)
th_R = ThreadReception(connection)
th_E.start()
th_R.start()

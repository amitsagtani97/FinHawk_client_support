# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

server.bind(("0.0.0.0", 6677)) 

server.listen(100) 

list_of_clients = [] 

def clientthread(conn, addr): 
	conn.send("Welcome to this chatroom!") 

	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 
					print "<" + addr[0] + "> " + message 
					message_to_send = "<" + addr[0] + "> " + message 
					broadcast(message_to_send, conn) 

				else: 
					remove(conn) 

			except: 
				continue

def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message) 
			except: 
				clients.close() 

				remove(clients) 

def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 
	conn, addr = server.accept() 
	list_of_clients.append(conn) 
	print addr[0] + " connected"
	start_new_thread(clientthread,(conn,addr))	 

conn.close() 
server.close()
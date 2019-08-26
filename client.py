# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
from common_ans import common_ans

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.connect(("0.0.0.0", 6677)) 
commonAns = common_ans()
ans= commonAns.getAnswers()
print(ans)
while True: 
	sockets_list = [sys.stdin, server]
	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048)
			#print ans.keys()
			if ans.has_key(str(message)):
				message = ans[message] 
			print message 
		else: 
			message = sys.stdin.readline()
			if message in list(ans.keys()):
				message = ans[message]
			server.send(message) 
			sys.stdout.flush() 
server.close()
import socket


client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 1337))

get_send_data()
get_print_res()

def get_send_data():
	data = raw_input()
	client_socket.send(data)

def get_print_res():
	server_data = client_socket.recv(1337)
	print "server's response:" +  server_data

client_socket.close()
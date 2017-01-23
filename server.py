import socket


server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 1337))

while True:
	listen()
	client_connect()
	recive_send_data()

def listen():
	server_socket.listen(1)

def client_connect():
	(client_socket, client_address) = server_socket.accept()

def recive_send_data():
	client_msg = client_socket.recv(1024)
	client_socket.send(client_msg)


client_socket.close()
server_socket.close()
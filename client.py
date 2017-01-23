import socket


client_socket = socket.socket()
client_socket.connect(("127.0.0.1", 1337))

data = raw_input()
client_socket.send(data)
server_data = client_socket.recv(1337)
print "server's response:" +  server_data

client_socket.close()
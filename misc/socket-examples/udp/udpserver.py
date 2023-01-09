'''
Example UDP server.

Taken from Kurose and Ross with slight modifications.
Example is for demonstration purposes and does not include error-checking
code that would be best practice.
'''
import socket



server_ip = 'localhost'
server_port = 12000
buffer_size = 2048

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((server_ip, server_port))

print('The server is ready to receive')

while True:
    message, client_address = server_socket.recvfrom(buffer_size)
    modified_message = message.decode('utf-8').upper()
    server_socket.sendto(modified_message.encode('utf-8'), client_address)

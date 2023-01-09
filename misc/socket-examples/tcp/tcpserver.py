'''
Example TCP server.

Taken from Kurose and Ross with slight modifications.
Example is for demonstration purposes and does not include error-checking
code that would be best practice.
'''
import socket



server_ip = 'localhost'
server_port = 12000
buffer_size = 1024

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))

server_socket.listen()

print('The server is ready to receive')

while True:
    connection_socket, addr = server_socket.accept()
    sentence = connection_socket.recv(buffer_size).decode('utf-8')
    modified_sentence = sentence.upper()
    connection_socket.send(modified_sentence.encode('utf-8'))
    connection_socket.close()

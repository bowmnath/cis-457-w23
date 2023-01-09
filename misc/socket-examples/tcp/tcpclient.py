'''
Example TCP client.

Taken from Kurose and Ross with slight modifications.
Example is for demonstration purposes and does not include error-checking
code that would be best practice.
'''
import socket



server_ip = 'localhost'
server_port = 12000
buffer_size = 1024

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

sentence = input('Input lowercase sentence:')
client_socket.send(sentence.encode('utf-8'))

modified_sentence = client_socket.recv(buffer_size)
print('From Server: ', modified_sentence.decode('utf-8'))
client_socket.close()

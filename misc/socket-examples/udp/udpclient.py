'''
Example UDP client.

Taken from Kurose and Ross with slight modifications.
Example is for demonstration purposes and does not include error-checking
code that would be best practice.
'''
import socket



server_ip = 'localhost'
server_port = 12000
buffer_size = 2048

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentence:')

client_socket.sendto(message.encode('utf-8'), (server_ip, server_port))
modified_message, server_address = client_socket.recvfrom(buffer_size)
print(modified_message.decode('utf-8'))
client_socket.close()
